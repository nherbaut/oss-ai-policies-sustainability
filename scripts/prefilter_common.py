"""Read-only corpus loading and deterministic reports for the prefilter tools."""
from collections import defaultdict
from contextlib import closing
import csv
import hashlib
import json
from pathlib import Path
import sqlite3

ROOT = Path(__file__).resolve().parents[1]
DEFAULT_PROJECT = ROOT / 'data/coding.qda'
DEFAULT_OUTPUT = ROOT / 'analysis/prefilter'


class PrefilterError(ValueError):
    pass


def digest(value):
    if not isinstance(value, str):
        value = json.dumps(value, ensure_ascii=True, sort_keys=True, separators=(',', ':'))
    return hashlib.sha256(value.encode('utf-8')).hexdigest()


def load_corpus(project):
    database = Path(project).resolve() / 'data.qda'
    if not database.is_file():
        raise PrefilterError(f'QualCoder database not found: {database}')
    with closing(sqlite3.connect(database.as_uri() + '?mode=ro', uri=True)) as conn:
        conn.row_factory = sqlite3.Row
        conn.execute('BEGIN')
        if conn.execute('PRAGMA integrity_check').fetchone()[0] != 'ok':
            raise PrefilterError('SQLite integrity check failed')
        versions = conn.execute('SELECT databaseversion FROM project').fetchall()
        if len(versions) != 1 or versions[0][0] != 'v17':
            raise PrefilterError('Only QualCoder v17 is supported')
        sources = [dict(row) for row in conn.execute('SELECT id,name,fulltext,memo FROM source ORDER BY id')]
        cases = defaultdict(set)
        for row in conn.execute('SELECT ct.fid,c.name FROM case_text ct JOIN cases c ON c.caseid=ct.caseid'):
            cases[row[0]].add(row[1])
    documents, excluded = [], []
    for row in sources:
        if row['fulltext'] is None:
            excluded.append(dict(id=row['id'], name=row['name'], reason='non_text_source'))
            continue
        text = row['fulltext']
        metadata = {}
        try:
            value = json.loads(row['memo'] or '{}')
            if isinstance(value, dict) and value.get('schema') == 'oss-ai-policies/document-import-v1':
                metadata = value
        except (ValueError, TypeError):
            pass
        provenance = metadata.get('provenance') or []
        provenance = [p for p in provenance if isinstance(p, dict)]
        roles = sorted({p['role'] for p in provenance if isinstance(p.get('role'), str)})
        documents.append(dict(id=row['id'], name=row['name'], text=text, sha256=digest(text),
                              entity=metadata.get('entity') or '; '.join(sorted(cases[row['id']])),
                              cases=sorted(cases[row['id']]), provenance=provenance,
                              role=';'.join(roles) or 'unknown', empty=not text.strip()))
    if not documents:
        raise PrefilterError('The project contains no text documents')
    return documents, excluded


def duplicate_groups(documents):
    groups = defaultdict(list)
    for doc in documents:
        members = groups[doc['sha256']]
        if members and members[0]['text'] != doc['text']:
            raise PrefilterError('SHA-256 collision between unequal document texts')
        members.append(doc)
    return {key: sorted(members, key=lambda d: d['id']) for key, members in sorted(groups.items())}


def document_metadata(doc):
    return {key: value for key, value in doc.items() if key != 'text'}


def output_directory(path, project, protected=()):
    output, project = Path(path).resolve(), Path(project).resolve()
    if output.is_relative_to(project) or project.is_relative_to(output):
        raise PrefilterError('Output must be outside the QualCoder project and its ancestors')
    if output in [Path(p).resolve().parent for p in protected]:
        raise PrefilterError('Output must not be the directory containing the protocol or query configuration')
    output.mkdir(parents=True, exist_ok=True)
    return output


def write_json(path, value):
    path = Path(path)
    if path.is_symlink():
        raise PrefilterError(f'Refusing to overwrite symlink: {path}')
    path.write_text(json.dumps(value, indent=2, ensure_ascii=False, allow_nan=False) + '\n', encoding='utf-8')


def write_csv(path, rows, fields):
    path = Path(path)
    if path.is_symlink():
        raise PrefilterError(f'Refusing to overwrite symlink: {path}')
    with path.open('w', encoding='utf-8', newline='') as stream:
        writer = csv.DictWriter(stream, fieldnames=fields)
        writer.writeheader()
        writer.writerows(rows)
