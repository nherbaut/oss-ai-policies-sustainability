"""Stable codebook identities and semantic merges for QualCoder v17.

The registry is a sidecar: QualCoder's schema and native text offsets are intact.
Numeric IDs belong to a particular snapshot; UUIDs identify concepts across it.
"""
from contextlib import closing
from copy import deepcopy
import hashlib
import json
import os
from pathlib import Path
import shutil
import sqlite3
import stat
import tempfile
import uuid

from merge_qualcoder import MergeError, TABLES, key, plan_merge, projected_data, read_project, validate_records, ensure_closed

REGISTRY = 'coding/codebook.json'
KINDS = {'code': ('code_name', 'cid'), 'category': ('code_cat', 'catid')}
REFS = {'code_text': {'cid': 'code'}, 'code_image': {'cid': 'code'}, 'code_av': {'cid': 'code'},
        'gr_cdct_text_item': {'cid': 'code', 'catid': 'category', 'supercatid': 'category'},
        'gr_cdct_line_item': {'fromcid': 'code', 'tocid': 'code', 'fromcatid': 'category', 'tocatid': 'category'},
        'gr_free_line_item': {'fromcid': 'code', 'tocid': 'code', 'fromcatid': 'category', 'tocatid': 'category'}}


class CodebookConflict(MergeError):
    def __init__(self, report):
        self.report = report
        super().__init__('Codebook conflicts require explicit resolutions:\n' + json.dumps(report, indent=2, ensure_ascii=False))


def semantic(entity):
    return {k: v for k, v in entity.items() if k != 'id' and k != 'date'}


def book(entities):
    result = dict(version=1, entities=dict(sorted(deepcopy(entities).items())))
    result['revision'] = hashlib.sha256(json.dumps({k: semantic(v) for k, v in result['entities'].items()},
                                                sort_keys=True, ensure_ascii=False).encode()).hexdigest()
    validate_book(result)
    return result


def validate_book(registry):
    if not isinstance(registry, dict) or registry.get('version') != 1 or not isinstance(registry.get('entities'), dict):
        raise MergeError('Invalid codebook registry')
    ids, names = set(), set()
    entities = registry['entities']
    for identity, e in entities.items():
        try:
            if str(uuid.UUID(identity)) != identity:
                raise ValueError()
        except (ValueError, TypeError, AttributeError):
            raise MergeError('Invalid codebook UUID')
        if (not isinstance(e, dict) or e.get('kind') not in KINDS or type(e.get('id')) is not int or e['id'] <= 0
                or not isinstance(e.get('name'), str) or not e['name'].strip()):
            raise MergeError('Invalid codebook entity')
        for key, seen in (((e['kind'], e['id']), ids), ((e['kind'], e['name']), names)):
            if key in seen:
                raise MergeError('Duplicate codebook name or numeric ID')
            seen.add(key)
        for field, kind in [('parent', e['kind']), ('category', 'category')]:
            target = e.get(field)
            if target is not None and (target not in entities or entities[target]['kind'] != kind):
                raise MergeError(f'Dangling codebook reference: {identity}.{field}')
        visited, current = set(), identity
        while current is not None:
            if current in visited:
                raise MergeError('Codebook hierarchy contains a cycle')
            visited.add(current)
            current = entities[current].get('parent')
    expected = hashlib.sha256(json.dumps({k: semantic(v) for k, v in sorted(entities.items())},
                                        sort_keys=True, ensure_ascii=False).encode()).hexdigest()
    if registry.get('revision') != expected:
        raise MergeError('Codebook revision does not match its contents')


def export(snapshot, reference=None, origin='bootstrap', coder=None):
    """Capture GUI edits, retaining known UUIDs; no name-based identity guessing."""
    known = (reference or {}).get('entities', {})
    lookup = {(e['kind'], e['id']): identity for identity, e in known.items()}
    rows = {(kind, row[pk]): row for kind, (table, pk) in KINDS.items() for row in snapshot['data'][table]}
    for kind_id in rows:
        if kind_id not in lookup:
            lookup[kind_id] = str(uuid.uuid5(uuid.NAMESPACE_URL, f'qualcoder:{origin}:{kind_id[0]}:{kind_id[1]}'))
    entities = {}
    for (kind, number), row in rows.items():
        identity = lookup[kind, number]
        pk = KINDS[kind][1]
        e = {k: v for k, v in row.items() if k not in (pk, 'catid', 'supercatid', 'supercid')}
        e.update(kind=kind, id=number)
        parent = row.get('supercid' if kind == 'code' else 'supercatid')
        category = row.get('catid') if kind == 'code' else None
        try:
            e['parent'] = lookup[kind, parent] if parent else None
            if kind == 'code':
                e['category'] = lookup['category', category] if category else None
        except KeyError:
            raise MergeError('Dangling code/category hierarchy in database')
        entities[identity] = e
        if coder and identity not in known and row.get('owner') != coder:
            raise MergeError('New codes/categories must belong to the session coder')
    return book(entities)


def unchanged_shared(shared, actual):
    for identity, e in shared['entities'].items():
        if identity not in actual['entities'] or semantic(e) != semantic(actual['entities'][identity]):
            raise MergeError('Shared codes/categories cannot be edited or deleted on a coding branch; use a maintenance branch')


def no_deletions(base, incoming):
    if not base['entities'].keys() <= incoming['entities'].keys():
        raise MergeError('Deleting or merging shared codes/categories is not supported')


def merge(base, destination, incoming, resolutions=None):
    """Merge by UUID and field; destinations retain their local numeric IDs."""
    for b in (base, destination, incoming):
        validate_book(b)
    no_deletions(base, destination)
    no_deletions(base, incoming)
    if resolutions is not None and not isinstance(resolutions, dict):
        raise MergeError('Resolution file must contain a JSON object')
    resolutions = resolutions or {}
    if not isinstance(resolutions.get('choices', []), list):
        raise MergeError('Resolution choices must be a list')
    if resolutions and resolutions.get('revision') != destination['revision']:
        raise MergeError('Resolution file targets a stale codebook revision; preview again')
    theirs = deepcopy(incoming['entities'])
    aliases, conflicts, seen = {}, [], set()
    for choice in resolutions.get('choices', []):
        if not isinstance(choice, dict):
            raise MergeError('Each resolution choice must be an object')
        identity = choice.get('entity')
        if identity in seen or identity not in theirs or identity in base['entities']:
            raise MergeError('Resolutions must name distinct incoming proposals')
        seen.add(identity)
        if choice.get('action') == 'adopt-shared':
            target = choice.get('target')
            if target not in destination['entities'] or destination['entities'][target]['kind'] != theirs[identity]['kind']:
                raise MergeError('Adoption requires a shared concept of the same kind')
            aliases[identity] = target
            del theirs[identity]
        elif choice.get('action') == 'rename-local' and isinstance(choice.get('name'), str) and choice['name'].strip():
            theirs[identity]['name'] = choice['name']
        else:
            raise MergeError('Expected adopt-shared or rename-local resolution')
    for e in theirs.values():
        for field in ('parent', 'category'):
            if e.get(field) in aliases:
                e[field] = aliases[e[field]]
    result = deepcopy(destination['entities'])
    for identity, e in theirs.items():
        if identity not in base['entities']:
            if identity not in result:
                result[identity] = deepcopy(e)
            elif semantic(result[identity]) != semantic(e):
                conflicts.append(dict(entity=identity, reason='Incompatible proposal with existing UUID'))
            continue
        before, ours = base['entities'][identity], result[identity]
        for field in e.keys() - {'id', 'date'}:
            if e[field] == before.get(field):
                continue
            if ours.get(field) not in (before.get(field), e[field]):
                conflicts.append(dict(entity=identity, field=field, base=before.get(field), shared=ours.get(field), incoming=e[field]))
            else:
                ours[field] = e[field]
    used_names = {}
    for identity, e in result.items():
        key = e['kind'], e['name']
        if key in used_names:
            conflicts.append(dict(entity=identity, other=used_names[key], name=e['name'], reason='Independent same-name concepts; adopt-shared or rename-local explicitly'))
        used_names[key] = identity
    if conflicts:
        raise CodebookConflict(dict(revision=destination['revision'], conflicts=conflicts, choices=[]))
    for kind in KINDS:
        used = {e['id'] for e in destination['entities'].values() if e['kind'] == kind}
        next_id = max(used, default=0) + 1
        for identity, e in result.items():
            if e['kind'] != kind or identity in destination['entities']:
                continue
            if e['id'] in used:
                e['id'] = next_id
                next_id += 1
            used.add(e['id'])
            next_id = max(next_id, e['id'] + 1)
    return book(result), aliases


def normalize(snapshot, source_book, target_book, aliases=None):
    """Rewrite codebook IDs and every supported reference, never source offsets."""
    aliases = aliases or {}
    validate_book(source_book)
    validate_book(target_book)
    maps = {kind: {} for kind in KINDS}
    for identity, e in source_book['entities'].items():
        target = target_book['entities'].get(aliases.get(identity, identity))
        if target is None or target['kind'] != e['kind']:
            raise MergeError('Cannot map codebook identity into destination')
        maps[e['kind']][e['id']] = target['id']
    result = deepcopy(snapshot)
    for kind, (table, pk) in KINDS.items():
        fields = [k for k in snapshot['data'][table][0]] if snapshot['data'][table] else None
        # v17 columns; allow empty initial codebooks.
        if fields is None:
            fields = (['cid','name','memo','catid','owner','date','color','supercid'] if kind == 'code'
                      else ['catid','name','owner','date','memo','supercatid'])
        rows = []
        for e in target_book['entities'].values():
            if e['kind'] != kind:
                continue
            row = {f: e.get(f) for f in fields}
            row[pk] = e['id']
            row['supercid' if kind == 'code' else 'supercatid'] = target_book['entities'][e['parent']]['id'] if e.get('parent') else None
            if kind == 'code':
                row['catid'] = target_book['entities'][e['category']]['id'] if e.get('category') else None
            rows.append(row)
        result['data'][table] = sorted(rows, key=lambda r: r[pk])
    def remap(row, field, kind):
        number = row.get(field)
        if number is None or number <= 0:
            return
        if number not in maps[kind]:
            raise MergeError(f'Unknown {kind} reference: {field}={number}')
        row[field] = maps[kind][number]
    for table, fields in REFS.items():
        for row in result['data'].get(table, []):
            for field, kind in fields.items():
                remap(row, field, kind)
    for row in result['data'].get('gr_memo_item', []):
        kind = {'code': 'code', 'code_name': 'code', 'cid': 'code',
                'category': 'category', 'cat': 'category', 'code_cat': 'category', 'catid': 'category'}.get((row.get('memo_source_type') or '').lower())
        if kind:
            remap(row, 'memo_source_id', kind)
    if any(k != v for mapping in maps.values() for k, v in mapping.items()):
        result['data']['project'][0]['recently_used_codes'] = None
    existing_names = {row['name'] for row in result['data']['coder_names']}
    creators = {e.get('owner') for e in target_book['entities'].values()} - {None, ''}
    result['data']['coder_names'].extend(dict(name=name, visibility=1) for name in sorted(creators - existing_names))
    for table in TABLES:
        identities = [key(table, row) for row in result['data'][table]]
        if len(identities) != len(set(identities)):
            raise MergeError('Codebook adoption would collapse duplicate coding identities; review those passages first')
    validate_records(result)
    return result


def aligned(snapshots, registries, target, aliases=None):
    normalized = [normalize(s, r, target, (aliases or {}).get(i)) for i, (s, r) in enumerate(zip(snapshots, registries))]
    return normalized


def branch_book(snapshot, context, origin, coder):
    reference = book({**context['shared']['entities'], **context.get('proposals', {})})
    result = export(snapshot, reference, origin, coder)
    unchanged_shared(context['shared'], result)
    for identity, e in result['entities'].items():
        if identity not in context['shared']['entities'] and e.get('owner') != coder:
            raise MergeError('Local codebook proposals must belong to the session coder')
    return result


def delta(base, incoming, base_book, incoming_book, coder, aliases=None):
    if set(aliases or {}) & base_book['entities'].keys():
        raise MergeError('Aliases cannot replace original shared identities')
    b, s = aligned([base, incoming], [base_book, incoming_book], incoming_book, {0: aliases or {}})
    return plan_merge(b, b, s, coder)


def changes(before, after):
    return [dict(id=k, before=before['entities'].get(k), after=e)
            for k, e in after['entities'].items()
            if k not in before['entities'] or semantic(e) != semantic(before['entities'][k])]


def affected(snapshot, registry, change_list, coder=None):
    changed = {c['id'] for c in change_list}
    entities = registry['entities']
    def chain(identity):
        result = set()
        while identity:
            result.add(identity)
            identity = entities[identity].get('parent')
        return result
    ids = {}
    for identity, entity in entities.items():
        if entity['kind'] != 'code':
            continue
        dependencies = chain(identity)
        for code in list(dependencies):
            dependencies |= chain(entities[code].get('category'))
        if changed & dependencies:
            ids[entity['id']] = identity
    sources = {r['id']: r['name'] for r in snapshot['data']['source']}
    return [dict(document=sources[r['fid']], owner=r['owner'], code_id=r['cid'], code_uuid=ids[r['cid']],
                 pos0=r['pos0'], pos1=r['pos1'], excerpt=r['seltext'])
            for r in snapshot['data']['code_text'] if r['cid'] in ids and (coder is None or r['owner'] == coder)]


def submission_plan(base, destination, incoming, base_book, destination_book, context, origin, coder, resolutions=None):
    if export(destination, destination_book) != destination_book:
        raise MergeError('Master database and shared codebook registry disagree')
    local = branch_book(incoming, context, origin, coder)
    # Verify ownership and all frozen content before applying newer theory.
    delta(base, incoming, base_book, local, coder, context.get('aliases'))
    merged, aliases = merge(context['shared'], destination_book, local, resolutions)
    all_aliases = {**context.get('aliases', {}), **aliases}
    b, d, s = aligned([base, destination, incoming], [base_book, destination_book, local], merged,
                      {0: all_aliases, 2: aliases})
    report = plan_merge(b, d, s, coder)
    report['codebook_changes'] = changes(destination_book, merged)
    late = changes(context['shared'], destination_book)
    report['late_theory'] = dict(changes=late, affected_passages=affected(s, merged, late, coder))
    desired = deepcopy(d)
    desired['data'] = projected_data(d, report)
    return report, desired, merged


def write_snapshot(destination, expected, output):
    """Build a verified candidate in a separate directory, preserving inputs."""
    destination, output = Path(destination).resolve(), Path(output).resolve()
    if output.exists() or output.is_relative_to(destination) or destination.is_relative_to(output):
        raise MergeError('Candidate must be a new directory separate from its input')
    ensure_closed(destination)
    original = read_project(destination)
    if original['schema'] != expected['schema'] or original['files'] != expected['files']:
        raise MergeError('Candidate schema or corpus differs')
    output.parent.mkdir(parents=True, exist_ok=True)
    with tempfile.TemporaryDirectory(prefix='.codebook-', dir=output.parent) as temp:
        staging = Path(temp) / 'candidate.qda'
        shutil.copytree(destination, staging)
        database = staging / 'data.qda'
        database.chmod(stat.S_IMODE(database.stat().st_mode) | stat.S_IWUSR)
        def canonical(rows):
            return sorted((tuple(sorted(r.items())) for r in rows), key=repr)
        with closing(sqlite3.connect(database)) as conn, conn:
            # Publish one self-contained database even after a crashed WAL session.
            conn.execute('PRAGMA journal_mode=DELETE')
            for table, rows in expected['data'].items():
                if canonical(rows) == canonical(original['data'][table]):
                    continue
                conn.execute(f'DELETE FROM "{table}"')
                for row in rows:
                    fields = list(row)
                    conn.execute(f'INSERT INTO "{table}" ({",".join(fields)}) VALUES ({",".join("?" for _ in fields)})', list(row.values()))
        actual = read_project(staging)
        if actual['files'] != expected['files'] or any(canonical(rows) != canonical(actual['data'][table]) for table, rows in expected['data'].items()):
            raise MergeError('Candidate verification failed')
        os.replace(staging, output)
