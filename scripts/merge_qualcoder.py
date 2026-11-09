"""Three-way text-coding merge for closed QualCoder v17 projects.

Preview is the default. --apply writes a new project, never an input project.
Only Python's standard library and lsof are required.
"""
import argparse
from collections import Counter
from contextlib import closing
import hashlib
import json
import os
from pathlib import Path
import shutil
import sqlite3
import stat
import subprocess
import tempfile

TABLES = {
    'code_text': ('ctid', ('fid', 'cid', 'pos0', 'pos1', 'owner')),
    'annotation': ('anid', ('fid', 'pos0', 'pos1', 'owner')),
}
UI_TABLES = {'manage_files_display', 'files_filter'}
UI_FIELDS = {'date', 'codername', 'bookmarkfile', 'bookmarkpos', 'recently_used_codes',
             'avbookmarkfile', 'avbookmarkmsec', 'avbookmarktextpos'}


class MergeError(ValueError):
    pass


def ensure_closed(project):
    database = Path(project) / 'data.qda'
    if not database.is_file():
        raise MergeError(f'QualCoder database not found: {database}')
    result = subprocess.run(['lsof', '-t', str(database.resolve())], text=True, capture_output=True)
    if result.returncode not in (0, 1) or result.stdout.strip():
        raise MergeError(f'Close QualCoder (and other database readers) first: {database}')


def read_project(project):
    project = Path(project).resolve()
    with closing(sqlite3.connect((project / 'data.qda').as_uri() + '?mode=ro', uri=True)) as conn:
        conn.row_factory = sqlite3.Row
        if conn.execute('PRAGMA integrity_check').fetchone()[0] != 'ok':
            raise MergeError('Database integrity check failed')
        schema = dict(conn.execute("SELECT name,sql FROM sqlite_master WHERE type='table' ORDER BY name"))
        data = {table: [dict(r) for r in conn.execute(f'SELECT * FROM "{table}" ORDER BY rowid')]
                for table in schema}
    if len(data.get('project', [])) != 1 or data['project'][0]['databaseversion'] != 'v17':
        raise MergeError('Only QualCoder schema v17 is supported')
    required = {'source', 'cases', 'case_text', 'code_name', 'code_cat', 'coder_names', *TABLES}
    if not required <= data.keys():
        raise MergeError('Incomplete QualCoder schema')
    files = {}
    for path in project.rglob('*'):
        rel = path.relative_to(project)
        if path.is_symlink():
            raise MergeError(f'Symlink in project: {rel}')
        if not path.is_file() or rel.parts[0] == 'ai_data' or rel.name in ('data.qda', 'data.qda-wal', 'data.qda-shm', 'data.qda-journal'):
            continue
        files[rel.as_posix()] = hashlib.sha256(path.read_bytes()).hexdigest()
    snapshot = dict(schema=schema, data=data, files=files)
    validate_records(snapshot)
    for source in data['source']:
        media = source.get('mediapath') or ''
        if source['fulltext'] is not None and media.startswith('/docs/'):
            copy = (project / 'documents' / media[6:]).resolve()
            if not copy.is_relative_to(project / 'documents'):
                raise MergeError('Document path escapes the project')
            if copy.suffix.lower() in ('.md', '.txt', '.rst') and (
                    not copy.is_file() or copy.read_text(encoding='utf-8-sig') != source['fulltext']):
                raise MergeError(f'Document copy differs from stored text: {source["name"]}')
    return snapshot


def text_span_candidates(text, start, end):
    """Native Qt/UTF-16 positions first, legacy Python code-point positions second.

    Never rewrite persisted offsets. Text coding carries seltext, allowing its
    convention to be verified by exact equality. Annotations have no seltext;
    their preview uses native UTF-16 when both interpretations are valid.
    """
    if not isinstance(start, int) or not isinstance(end, int) or not 0 <= start < end:
        return []
    candidates = []
    encoded = text.encode('utf-16-le')
    if end <= len(encoded) // 2:
        try:
            candidates.append(encoded[start * 2:end * 2].decode('utf-16-le'))
        except UnicodeDecodeError:
            pass  # A native selection must not split a surrogate pair.
    if end <= len(text):
        legacy = text[start:end]
        if legacy not in candidates:
            candidates.append(legacy)
    return candidates


def validate_records(snapshot):
    data = snapshot['data']
    sources = {r['id']: r for r in data['source']}
    codes = {r['cid'] for r in data['code_name']}
    for table in TABLES:
        for row in data[table]:
            source = sources.get(row['fid'])
            if source is None or source['fulltext'] is None:
                raise MergeError(f'{table}: missing text source')
            text = source['fulltext']
            spans = text_span_candidates(text, row['pos0'], row['pos1'])
            record_id = row[TABLES[table][0]]
            location = f'{table} record {record_id}, document {source["name"]}, offsets {row["pos0"]}:{row["pos1"]}'
            if not spans:
                raise MergeError(f'Invalid offsets: {location}')
            if not row['owner']:
                raise MergeError(f'{table}: missing coder attribution')
            if table == 'code_text':
                if row['cid'] not in codes:
                    raise MergeError(f'Unknown code reference {row["cid"]}: {location}')
                if row['seltext'] not in spans:
                    raise MergeError(f'Coded excerpt does not match document in UTF-16 or code-point coordinates: {location}')
    coding_ids = {r['ctid'] for r in data['code_text']}
    for row in data.get('gr_free_text_item', []):
        for column in ('ctid', 'memo_ctid'):
            if row.get(column) and row[column] > 0 and row[column] not in coding_ids:
                raise MergeError(f'Dangling graph reference: {column}={row[column]}')
    case_ids = {r['caseid'] for r in data['cases']}
    for row in data['case_text']:
        if row['fid'] not in sources or row['caseid'] not in case_ids:
            raise MergeError('Dangling case/document reference')


def fixed_structure(base, other):
    if base['schema'] != other['schema']:
        raise MergeError('Database schema changed during the coding round')
    if base['files'] != other['files']:
        raise MergeError('Project document/media files changed during the coding round')
    for table, rows in base['data'].items():
        if table in TABLES or table in UI_TABLES or table == 'coder_names':
            continue
        def comparable(records):
            if table == 'project':
                return [{k: v for k, v in r.items() if k not in UI_FIELDS} for r in records]
            return records
        if comparable(rows) != comparable(other['data'][table]):
            raise MergeError(f'Unsupported change to fixed table: {table}')
    before = {r['name'] for r in base['data']['coder_names']}
    after = {r['name'] for r in other['data']['coder_names']}
    if not before <= after:
        raise MergeError('Existing coder registrations cannot be removed or renamed')


def key(table, row):
    return tuple(row[c] for c in TABLES[table][1])


def content(table, row):
    if row is None:
        return None
    return {k: v for k, v in row.items() if k not in (TABLES[table][0], 'date')}


def plan_merge(base, destination, submission, coder):
    if not coder.strip() or coder.strip().lower() == 'default':
        raise MergeError('A named coder other than default is required')
    fixed_structure(base, destination)
    fixed_structure(base, submission)
    original_names = {r['name'] for r in base['data']['coder_names']}
    if {r['name'] for r in submission['data']['coder_names']} - original_names - {coder}:
        raise MergeError('Submission registered another coder')
    changes, conflicts = [], []
    source_names = {r['id']: r['name'] for r in base['data']['source']}
    code_names = {r['cid']: r['name'] for r in base['data']['code_name']}
    case_names = {r['caseid']: r['name'] for r in base['data']['cases']}
    for table in TABLES:
        b, d, s = ({key(table, r): r for r in snap['data'][table]} for snap in (base, destination, submission))
        for identity in sorted(b.keys() | s.keys(), key=repr):
            before, ours, theirs = b.get(identity), d.get(identity), s.get(identity)
            if content(table, before) == content(table, theirs):
                continue
            row = theirs or before
            if row['owner'] != coder:
                raise MergeError(f'Submission changes another coder\'s {table}: {row["owner"]}')
            if table == 'code_text' and (row.get('avid') or next(r for r in base['data']['source'] if r['id'] == row['fid']).get('av_text_id')):
                raise MergeError('Audio/video transcript coding is outside this merger\'s scope')
            detail = dict(table=table, identity=list(identity), before=before, incoming=theirs,
                          document=source_names[row['fid']], owner=row['owner'],
                          cases=sorted({case_names[r['caseid']] for r in base['data']['case_text'] if r['fid'] == row['fid']}))
            source = next(r for r in base['data']['source'] if r['id'] == row['fid'])
            media = source.get('mediapath') or ''
            detail['document_path'] = 'documents/' + media[6:] if media.startswith('/docs/') else None
            detail['excerpt'] = (row['seltext'] if table == 'code_text' else
                                 text_span_candidates(source['fulltext'], row['pos0'], row['pos1'])[0])
            if table == 'code_text':
                detail['code'] = code_names[row['cid']]
            if content(table, ours) == content(table, theirs):
                continue
            if content(table, ours) != content(table, before):
                conflicts.append(dict(detail, destination=ours, reason='Concurrent edit, delete-versus-edit, or incompatible addition'))
            else:
                changes.append(dict(detail, operation='delete' if theirs is None else 'add' if before is None else 'edit'))
    report = dict(coder=coder, changes=changes, conflicts=conflicts,
                  summary=dict(Counter(f'{c["table"]}:{c["operation"]}' for c in changes)))
    report['by_document'] = [
        dict(document=document, owner=owner,
             path=next(c['document_path'] for c in changes if c['document'] == document),
             cases=sorted({case for c in changes if c['document'] == document for case in c['cases']}),
             summary=dict(Counter(f'{c["table"]}:{c["operation"]}' for c in changes
                                  if c['document'] == document and c['owner'] == owner)))
        for document, owner in sorted({(c['document'], c['owner']) for c in changes})]
    if destination['data'].get('gr_memo_item') and any(c['table'] == 'code_text' and c['operation'] == 'delete' for c in changes):
        raise MergeError('Review graph memo references in QualCoder before deleting coding')
    # Check references against the proposed result, including deletion of coding
    # still referenced by destination graphs. Allocate IDs above all live IDs.
    projected = projected_data(destination, report)
    validate_records(dict(data=projected))
    return report


def projected_data(destination, report):
    data = {table: [dict(r) for r in rows] for table, rows in destination['data'].items()}
    for table, (pk, _) in TABLES.items():
        rows = {key(table, r): r for r in data[table]}
        next_id = max((r[pk] for r in rows.values()), default=0) + 1
        for change in report['changes']:
            if change['table'] != table:
                continue
            identity = tuple(change['identity'])
            old = rows.pop(identity, None)
            if change['incoming'] is not None:
                row = dict(change['incoming'])
                row[pk] = old[pk] if old else next_id
                if old is None:
                    next_id += 1
                rows[identity] = row
        data[table] = sorted(rows.values(), key=lambda r: r[pk])
    if report['coder'] not in {r['name'] for r in data['coder_names']}:
        data['coder_names'].append(dict(name=report['coder'], visibility=1))
    return data


def write_candidate(base_path, destination_path, submission_path, coder, output, expected_report=None):
    paths = [Path(p).resolve() for p in (base_path, destination_path, submission_path)]
    output = Path(output).resolve()
    if output.exists() or any(output.is_relative_to(p) or p.is_relative_to(output) for p in paths):
        raise MergeError('Output must be a new directory separate from all input projects')
    for path in paths:
        ensure_closed(path)
    snapshots = [read_project(p) for p in paths]
    report = plan_merge(*snapshots, coder)
    if report['conflicts']:
        raise MergeError('Conflicts require review; no candidate was written')
    if expected_report is not None and expected_report != report:
        raise MergeError('Inputs changed after preview; review a fresh merge')
    output.parent.mkdir(parents=True, exist_ok=True)
    staging_root = Path(tempfile.mkdtemp(prefix='.qualcoder-merge-', dir=output.parent))
    staging = staging_root / 'candidate.qda'
    try:
        shutil.copytree(paths[1], staging, ignore=shutil.ignore_patterns('data.qda-wal', 'data.qda-shm', 'data.qda-journal'))
        # Destination snapshots on master are intentionally read-only. Only the
        # new candidate copy is made writable; input permissions stay untouched.
        staged_database = staging / 'data.qda'
        staged_database.chmod(stat.S_IMODE(staged_database.stat().st_mode) | stat.S_IWUSR)
        expected = projected_data(snapshots[1], report)
        with closing(sqlite3.connect(staging / 'data.qda')) as conn, conn:
            for table, (pk, _) in TABLES.items():
                for change in report['changes']:
                    if change['table'] != table:
                        continue
                    columns = TABLES[table][1]
                    identity = tuple(change['identity'])
                    where = ' AND '.join(f'"{c}" IS ?' for c in columns)
                    conn.execute(f'DELETE FROM {table} WHERE {where}', identity)
                    if change['incoming'] is not None:
                        row = next(r for r in expected[table] if key(table, r) == identity)
                        fields = list(row)
                        conn.execute(f'INSERT INTO {table} ({",".join(fields)}) VALUES ({",".join("?" for _ in fields)})', [row[f] for f in fields])
            conn.execute('INSERT OR IGNORE INTO coder_names(name,visibility) VALUES (?,1)', (coder,))
        actual = read_project(staging)
        for table, rows in expected.items():
            if sorted(rows, key=repr) != sorted(actual['data'][table], key=repr):
                raise MergeError(f'Unexpected candidate mutation: {table}')
        if actual['files'] != snapshots[1]['files']:
            raise MergeError('Unexpected document mutation')
        os.replace(staging, output)
    finally:
        shutil.rmtree(staging_root)
    return report


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    for name in ('base', 'destination', 'submission', 'coder'):
        parser.add_argument('--' + name, required=True)
    parser.add_argument('--output', type=Path)
    parser.add_argument('--report', type=Path)
    parser.add_argument('--apply', action='store_true')
    args = parser.parse_args()
    try:
        for path in (args.base, args.destination, args.submission):
            ensure_closed(path)
        report = plan_merge(*(read_project(p) for p in (args.base, args.destination, args.submission)), args.coder)
        print(json.dumps(report, indent=2, ensure_ascii=False))
        if args.report:
            if any(args.report.resolve().is_relative_to(Path(p).resolve()) for p in (args.base, args.destination, args.submission)):
                raise MergeError('Report must be outside the input projects')
            args.report.write_text(json.dumps(report, indent=2, ensure_ascii=False) + '\n')
        if report['conflicts']:
            return 2
        if args.apply:
            if not args.output:
                raise MergeError('--apply requires --output')
            write_candidate(args.base, args.destination, args.submission, args.coder, args.output, report)
        return 0
    except (MergeError, OSError, sqlite3.Error) as error:
        parser.exit(2, f'Cannot merge: {error}\n')


if __name__ == '__main__':
    raise SystemExit(main())
