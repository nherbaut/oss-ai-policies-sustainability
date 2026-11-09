"""Import research documents into QualCoder v17, one case per dataset entity.

Default is a read-only preview. --apply creates a complete .qda backup and uses
one SQLite transaction. Original text is retained as Markdown; analytical codes
are not imported. Repeated runs reuse existing sources and whole-file case links.
"""
import argparse
import csv
import hashlib
import json
import re
import shutil
import sqlite3
from collections import Counter, defaultdict
from datetime import datetime
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
ANALYSIS = ROOT / 'analysis/corpus-assessment'
DATASET = ROOT / 'data/281/dataset1-multiple-ai-policies.csv'
MARKER = 'oss-ai-policies/document-import-v1'


def sha(data):
    return hashlib.sha256(data).hexdigest()


def skip_reason(text):
    if not text.strip(): return 'empty_text'
    if re.fullmatch(r'[.\w/@-]+\.(?:md|rst)', text.strip()): return 'path_stub'
    if re.search(r'Cookie monster!|Making sure you.re not a bot|Access Denied|Just a moment\.\.\.|Enable JavaScript and cookies to continue', text, re.I):
        return 'bot_or_access_page'
    if re.search(r'Impossible d.ouvrir|doesn.t have JavaScript enabled|version of (?:the|your) browser.{0,40}no longer supported', text, re.I):
        return 'rendering_problem'
    if len(text.strip()) < 200 and re.match(r'^Redirecting to\s+https?[:<]|^Redirecting to\s+<https?', text.strip(), re.I):
        return 'redirect_notice'
    return None


def memo_metadata(memo):
    try:
        item = json.loads(memo or '{}')
        return item if isinstance(item, dict) and item.get('schema') == MARKER else None
    except (TypeError, ValueError):
        return None


def load_documents():
    with DATASET.open(newline='', encoding='utf-8-sig') as f:
        table = list(csv.reader(f))
    entities = [r[0] for r in table[1:]]
    expected = json.loads((ANALYSIS / 'baseline.json').read_text())['dataset_entries']
    assert len(entities) == expected and len(set(entities)) == expected
    manifests = json.loads((ANALYSIS / 'source-manifest.json').read_text())
    groups, skipped = {}, []

    def consider(entity, path, role, metadata):
        source = ROOT / path
        text = source.read_text(encoding='utf-8-sig')
        reason = skip_reason(text)
        if reason:
            skipped.append({'entity': entity, 'path': path, 'role': role, 'reason': reason})
            return
        text_hash = sha(text.encode())
        key = (entity, text_hash)
        if key not in groups:
            groups[key] = {'entity': entity, 'text': text, 'text_sha256': text_hash,
                           'role': role, 'basename': source.name, 'provenance': []}
        provenance = {'path': path, 'role': role, 'original_file_sha256': sha(source.read_bytes()), **metadata}
        if provenance not in groups[key]['provenance']:
            groups[key]['provenance'].append(provenance)

    slots = {'ai_policy': 9, 'contributing': 10, 'agent': 11, 'other_policy': 13}
    for row in table[1:]:
        entity = row[0]
        for path in sorted((ROOT / 'data/281/policies' / entity).glob('*.md')):
            index = slots.get(path.stem)
            consider(entity, str(path.relative_to(ROOT)), path.stem,
                     {'source_url_cell': row[index] if index is not None else '',
                      'retrieved_at': None,
                      'notes': 'Local extraction. Original retrieval date is not recorded.'})
    for source in manifests:
        if source['entity'] not in entities:
            raise ValueError('Supplementary source has no dataset entity: ' + source['entity'])
        if source['status'] != 'downloaded':
            skipped.append({'entity': source['entity'], 'path': source.get('url'),
                            'role': source['role'], 'reason': source['status']})
            continue
        consider(source['entity'], source['snapshot'], source['role'],
                 {k: source.get(k) for k in ('id', 'url', 'resolved_url', 'accessed_at',
                                            'version', 'raw_snapshot', 'sha256')})
    return entities, list(groups.values()), skipped


def state(conn):
    sources = [dict(r) for r in conn.execute('SELECT id,name,fulltext,mediapath,memo,owner,date FROM source')]
    cases = {r['name']: r['caseid'] for r in conn.execute('SELECT caseid,name FROM cases')}
    assignments = defaultdict(set)
    for row in conn.execute('SELECT fid,c.name FROM case_text t JOIN cases c ON t.caseid=c.caseid'):
        assignments[row['fid']].add(row['name'])
    return sources, cases, assignments


def plan(conn, entities, documents):
    sources, cases, assignments = state(conn)
    indexed = {}
    by_hash = defaultdict(list)
    intended_entities = defaultdict(set)
    for doc in documents:
        intended_entities[doc['text_sha256']].add(doc['entity'])
    for source in sources:
        if source['fulltext'] is None: continue
        text_hash = sha(source['fulltext'].encode())
        by_hash[text_hash].append(source)
        metadata = memo_metadata(source['memo'])
        if metadata:
            indexed[(metadata['entity'], metadata['text_sha256'])] = source
    operations = []
    for raw_doc in documents:
        doc = dict(raw_doc)
        key = (doc['entity'], doc['text_sha256'])
        existing = indexed.get(key)
        if existing and existing['fulltext'] != doc['text']:
            previous = memo_metadata(existing['memo']) or {}
            conversion = previous.get('conversion', {})
            if (conversion.get('version') == 'oss-ai-policies/clean-markdown-v1'
                    and conversion.get('original_sha256') == doc['text_sha256']
                    and conversion.get('converted_sha256') == sha(existing['fulltext'].encode())):
                # Keep identity/provenance anchored to the original corpus hash,
                # but use the working text for case ranges and verification.
                doc['text'] = existing['fulltext']
            else:
                raise ValueError('Previously imported source text changed: ' + existing['name'])
        if existing is None:
            matches = [s for s in by_hash[doc['text_sha256']] if
                       doc['entity'] in assignments[s['id']] or
                       (not assignments[s['id']] and len(intended_entities[doc['text_sha256']]) == 1)]
            if len(matches) == 1:
                existing = matches[0]
        name_entity = re.sub(r'[^\w.-]+', '__', doc['entity'], flags=re.ASCII).strip('_')
        name_role = re.sub(r'[^\w.-]+', '-', doc['role'])
        filename = f'{name_entity}--{name_role}--{doc["text_sha256"][:12]}.md'
        metadata = {'schema': MARKER, 'entity': doc['entity'],
                    'text_sha256': doc['text_sha256'], 'provenance': doc['provenance'],
                    'text_format': 'Original Markdown/text; no analytical codes imported.'}
        if existing:
            previous = memo_metadata(existing['memo'])
            if previous and previous.get('conversion'):
                metadata['conversion'] = previous['conversion']
                metadata['text_format'] = previous['text_format']
            if previous and previous.get('previous_memo'):
                metadata['previous_memo'] = previous['previous_memo']
            elif existing['memo'] and previous is None:
                metadata['previous_memo'] = existing['memo']
        memo = json.dumps(metadata, indent=2, ensure_ascii=False)
        caseid = cases.get(doc['entity'])
        linked = existing and caseid is not None and conn.execute(
            'SELECT 1 FROM case_text WHERE caseid=? AND fid=? AND pos0=0 AND pos1=?',
            (caseid, existing['id'], len(doc['text']))).fetchone() is not None
        operations.append({**doc, 'existing': existing, 'filename': filename,
                           'memo': memo, 'already_linked': bool(linked)})
    return operations, [e for e in entities if e not in cases]


def verify(conn, entities, records, project):
    assert conn.execute('PRAGMA integrity_check').fetchone()[0] == 'ok'
    assert not conn.execute('PRAGMA foreign_key_check').fetchall()
    for entity in entities:
        assert conn.execute('SELECT 1 FROM cases WHERE name=?', (entity,)).fetchone()
    for record in records:
        row = conn.execute('SELECT fulltext,mediapath FROM source WHERE id=?', (record['source_id'],)).fetchone()
        assert row['fulltext'] == record['text']
        assert conn.execute('SELECT 1 FROM case_text WHERE caseid=? AND fid=? AND pos0=0 AND pos1=?',
                            (record['case_id'], record['source_id'], len(record['text']))).fetchone()
        path = row['mediapath']
        if path and path.startswith('/docs/'):
            assert (project / 'documents' / path[6:]).is_file()
            assert (project / 'documents' / path[6:]).read_text(encoding='utf-8-sig') == record['text']
    # All expected projects have at least one substantive source.
    linked = {r[0] for r in conn.execute('SELECT DISTINCT c.name FROM cases c JOIN case_text t ON c.caseid=t.caseid')}
    assert set(entities) <= linked


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--project', type=Path, default=ROOT / 'data/coding.qda')
    parser.add_argument('--apply', action='store_true', help='Back up and write the reviewed import.')
    args = parser.parse_args()
    project = args.project.resolve(); database = project / 'data.qda'
    if not database.is_file(): raise SystemExit('QualCoder database not found: ' + str(database))
    entities, documents, skipped = load_documents()
    conn = sqlite3.connect(database.as_uri() + '?mode=ro', uri=True)
    conn.row_factory = sqlite3.Row
    if conn.execute('SELECT databaseversion FROM project').fetchone()[0] != 'v17':
        raise SystemExit('Unexpected QualCoder schema; inspect it before importing.')
    operations, new_cases = plan(conn, entities, documents)
    changes = sum(not o['existing'] or o['existing']['memo'] != o['memo'] or not o['already_linked'] for o in operations)
    preview = {'dataset_projects': len(entities), 'substantive_documents': len(documents),
               'new_cases': len(new_cases), 'new_documents': sum(not o['existing'] for o in operations),
               'reused_documents': sum(bool(o['existing']) for o in operations),
               'new_case_links': sum(not o['already_linked'] for o in operations),
               'documents_needing_changes': changes, 'skipped_input_records': len(skipped),
               'skip_reasons': dict(Counter(s['reason'] for s in skipped))}
    print(json.dumps(preview, indent=2))
    conn.close()
    if not args.apply or not (changes or new_cases): return

    # Refuse live application access; SQLite's write lock also guards the transaction.
    import subprocess
    busy = subprocess.run(['lsof', '-t', str(database)], capture_output=True, text=True)
    if busy.stdout.strip():
        raise SystemExit('QualCoder database is open in another process; close the project before importing.')
    timestamp = datetime.now().astimezone().strftime('%Y%m%d-%H%M%S-%f')
    backup = ROOT / 'data/qualcoder-backups' / f'coding-before-import-{timestamp}.qda'
    backup.parent.mkdir(exist_ok=True)
    shutil.copytree(project, backup)
    # Ensure the main database snapshot includes any committed WAL contents.
    with sqlite3.connect(database) as live, sqlite3.connect(backup / 'data.qda') as saved:
        live.backup(saved)
    conn = sqlite3.connect(database, timeout=5)
    conn.row_factory = sqlite3.Row
    created_files = []
    try:
        conn.execute('BEGIN IMMEDIATE')
        operations, new_cases = plan(conn, entities, documents)
        before_coding = {t: [tuple(r) for r in conn.execute('SELECT * FROM ' + t)]
                         for t in ('code_name', 'code_cat', 'code_text', 'code_image', 'code_av', 'annotation')}
        owner = conn.execute('SELECT codername FROM project').fetchone()[0] or 'default'
        now = datetime.now().astimezone().strftime('%Y-%m-%d %H:%M:%S')
        for entity in new_cases:
            memo = 'Project case for dataset entry: ' + entity + '\nDocuments grouped by dataset label; no analytical classification implied.'
            cursor = conn.execute('INSERT INTO cases(name,memo,owner,date) VALUES (?,?,?,?)', (entity, memo, owner, now))
            for attribute in conn.execute("SELECT name FROM attribute_type WHERE caseOrFile='case'").fetchall():
                conn.execute('INSERT INTO attribute(name,attr_type,value,id,date,owner) VALUES (?,?,?,?,?,?)',
                             (attribute[0], 'case', '', cursor.lastrowid, now, owner))
        case_ids = {r['name']: r['caseid'] for r in conn.execute('SELECT caseid,name FROM cases')}
        imported = []
        for op in operations:
            if op['existing']:
                source_id = op['existing']['id']
                if op['existing']['memo'] != op['memo']:
                    conn.execute('UPDATE source SET memo=? WHERE id=?', (op['memo'], source_id))
            else:
                destination = project / 'documents' / op['filename']
                if destination.exists():
                    if destination.read_text(encoding='utf-8-sig') != op['text']:
                        raise ValueError('Refusing to overwrite differing document: ' + str(destination))
                else:
                    destination.write_text(op['text'], encoding='utf-8'); created_files.append(destination)
                cursor = conn.execute('INSERT INTO source(name,fulltext,mediapath,memo,owner,date) VALUES (?,?,?,?,?,?)',
                                      (op['filename'], op['text'], '/docs/' + op['filename'], op['memo'], owner, now))
                source_id = cursor.lastrowid
                for attribute in conn.execute("SELECT name FROM attribute_type WHERE caseOrFile='file'").fetchall():
                    conn.execute('INSERT INTO attribute(name,attr_type,value,id,date,owner) VALUES (?,?,?,?,?,?)',
                                 (attribute[0], 'file', '', source_id, now, owner))
            case_id = case_ids[op['entity']]
            if not op['already_linked']:
                conn.execute('INSERT INTO case_text(caseid,fid,pos0,pos1,owner,date,memo) VALUES (?,?,?,?,?,?,?)',
                             (case_id, source_id, 0, len(op['text']), owner, now, 'Entire document assigned to project case.'))
            actual = conn.execute('SELECT name,mediapath FROM source WHERE id=?', (source_id,)).fetchone()
            imported.append({**op, 'source_id': source_id, 'case_id': case_id,
                             'source_name': actual['name'], 'mediapath': actual['mediapath']})
        verify(conn, entities, imported, project)
        for table, rows in before_coding.items():
            assert [tuple(r) for r in conn.execute('SELECT * FROM ' + table)] == rows
        conn.commit()
    except BaseException:
        conn.rollback()
        for path in created_files: path.unlink()
        raise
    finally:
        conn.close()
    log = {'project': str(project.relative_to(ROOT)), 'backup': str(backup.relative_to(ROOT)),
           'imported_at': now, 'summary': preview, 'skipped': skipped,
           'documents': [{k: o[k] for k in ('entity','source_id','case_id','text_sha256','source_name','mediapath','provenance')}
                         for o in imported]}
    log_path = ANALYSIS / 'qualcoder-import.json'
    log_path.write_text(json.dumps(log, indent=2, ensure_ascii=False) + '\n')
    print('Imported. Full project backup:', backup.relative_to(ROOT))
    print('Import manifest:', log_path.relative_to(ROOT))


if __name__ == '__main__': main()
