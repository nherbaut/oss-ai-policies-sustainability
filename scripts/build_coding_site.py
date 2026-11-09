"""Export a read-only QualCoder v17 snapshot as a self-contained static site."""
import argparse
from contextlib import closing
import hashlib
import json
from pathlib import Path
import sqlite3
import sys

from merge_qualcoder import text_span_candidates


class ExportError(ValueError):
    pass


def browser_span(text, start, end, selected=None):
    """Validate native/legacy positions and return JavaScript UTF-16 offsets."""
    candidates = text_span_candidates(text, start, end)
    if not candidates or (selected is not None and selected not in candidates):
        raise ExportError(f'Invalid text span {start}:{end}')
    encoded = text.encode('utf-16-le')
    try:
        native = encoded[start * 2:end * 2].decode('utf-16-le') if end <= len(encoded) // 2 else None
    except UnicodeDecodeError:
        native = None
    if native is not None and (selected is None or native == selected):
        return start, end
    return len(text[:start].encode('utf-16-le')) // 2, len(text[:end].encode('utf-16-le')) // 2


def check_hierarchy(rows, key, parent, label):
    lookup = {row[key]: row for row in rows}
    for row in rows:
        seen = set()
        current = row[key]
        while current is not None:
            if current not in lookup:
                raise ExportError(f'{label}: missing parent {current}')
            if current in seen:
                raise ExportError(f'{label}: hierarchy cycle at {current}')
            seen.add(current)
            current = lookup[current].get(parent)


def read_snapshot(project):
    database = Path(project).resolve() / 'data.qda'
    if not database.is_file():
        raise ExportError(f'QualCoder database not found: {database}')
    with closing(sqlite3.connect(database.as_uri() + '?mode=ro', uri=True)) as conn:
        conn.row_factory = sqlite3.Row
        conn.execute('BEGIN')
        if conn.execute('PRAGMA integrity_check').fetchone()[0] != 'ok':
            raise ExportError('Database integrity check failed')
        versions = conn.execute('SELECT databaseversion FROM project').fetchall()
        if len(versions) != 1 or versions[0][0] != 'v17':
            raise ExportError('Only QualCoder schema v17 is supported')
        tables = ('source', 'code_name', 'code_cat', 'code_text', 'annotation', 'cases', 'case_text')
        data = {table: [dict(row) for row in conn.execute(f'SELECT * FROM "{table}" ORDER BY rowid')]
                for table in tables}

    codes = {row['cid']: row for row in data['code_name']}
    categories = {row['catid']: row for row in data['code_cat']}
    sources = {row['id']: row for row in data['source']}
    cases = {row['caseid']: row for row in data['cases']}
    check_hierarchy(data['code_cat'], 'catid', 'supercatid', 'Category')
    check_hierarchy(data['code_name'], 'cid', 'supercid', 'Code')
    for row in codes.values():
        if row['catid'] is not None and row['catid'] not in categories:
            raise ExportError(f'Code {row["cid"]}: missing category {row["catid"]}')

    documents = {}
    for row in sources.values():
        if row['fulltext'] is None:
            continue
        entity, provenance = '', []
        try:
            memo = json.loads(row['memo'] or '')
            if isinstance(memo, dict) and memo.get('schema') == 'oss-ai-policies/document-import-v1':
                entity = memo.get('entity') or ''
                provenance = [p.get('path', '') for p in memo.get('provenance', []) if isinstance(p, dict)]
        except (ValueError, TypeError):
            pass
        documents[row['id']] = dict(id=row['id'], name=row['name'], entity=entity,
                                    paths=provenance, text=row['fulltext'], memo=row['memo'] or '',
                                    cases=[], codings=[], annotations=[])
    for row in data['case_text']:
        if row['caseid'] not in cases or row['fid'] not in sources:
            raise ExportError('Dangling case/document reference')
        if row['fid'] in documents:
            names = documents[row['fid']]['cases']
            name = cases[row['caseid']]['name']
            if name not in names:
                names.append(name)

    for table, destination, pk in [('code_text', 'codings', 'ctid'), ('annotation', 'annotations', 'anid')]:
        for row in data[table]:
            location = f'{table} #{row[pk]}, document {row["fid"]}'
            if row['fid'] not in documents:
                raise ExportError(f'{location}: missing text document')
            if table == 'code_text' and row['cid'] not in codes:
                raise ExportError(f'{location}: missing code {row["cid"]}')
            document = documents[row['fid']]
            try:
                start, end = browser_span(document['text'], row['pos0'], row['pos1'],
                                          row['seltext'] if table == 'code_text' else None)
            except ExportError as exc:
                raise ExportError(f'{location}: {exc}') from exc
            item = dict(id=row[pk], start=start, end=end, owner=row['owner'] or '',
                        memo=row['memo'] or '', date=row['date'])
            if table == 'code_text':
                item.update(code=row['cid'], text=row['seltext'], important=bool(row['important']))
            document[destination].append(item)

    for document in documents.values():
        document['cases'].sort()
        if not document['entity']:
            document['entity'] = ', '.join(document['cases'])
    documents = sorted(documents.values(), key=lambda d: (d['entity'], d['name'], d['id']))
    result = dict(version=1, documents=documents,
                  codes=[dict(id=r['cid'], name=r['name'], memo=r['memo'] or '',
                              category=r['catid'], parent=r.get('supercid'), color=r['color'])
                         for r in data['code_name']],
                  categories=[dict(id=r['catid'], name=r['name'], memo=r['memo'] or '', parent=r['supercatid'])
                              for r in data['code_cat']])
    result['summary'] = dict(documents=len(documents), codes=len(codes), categories=len(categories),
                             codings=sum(len(d['codings']) for d in documents),
                             annotations=sum(len(d['annotations']) for d in documents))
    result['snapshot'] = hashlib.sha256(json.dumps(result, sort_keys=True, ensure_ascii=False).encode()).hexdigest()
    return result


def build(project, output):
    project, output = Path(project).resolve(), Path(output).resolve()
    if output.is_relative_to(project) or project.is_relative_to(output):
        raise ExportError('Output must be outside the QualCoder project and its ancestors')
    assets = Path(__file__).with_name('coding_site')
    names = ('index.html', 'style.css', 'app.js', 'data.js', '.nojekyll')
    if output.exists():
        if not output.is_dir() or (any(output.iterdir()) and not (output / '.coding-site').is_file()):
            raise ExportError('Output directory is not an existing coding-site export or an empty directory')
        if any((output / name).is_symlink() for name in (*names, '.coding-site')):
            raise ExportError('Output files must not be symlinks')
    data = read_snapshot(project)
    files = {name: (assets / name).read_text(encoding='utf-8') for name in names[:3]}
    files.update({'data.js': 'window.CODING_DATA = ' + json.dumps(data, ensure_ascii=True) + ';\n',
                  '.nojekyll': '', '.coding-site': 'QualCoder static export v1\n'})
    output.mkdir(parents=True, exist_ok=True)
    for name, content in files.items():
        (output / name).write_text(content, encoding='utf-8')
    return data['summary']


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--project', type=Path, default=Path('data/coding.qda'))
    parser.add_argument('--output', type=Path, default=Path('dist/coding-site'))
    args = parser.parse_args()
    try:
        summary = build(args.project, args.output)
    except (ExportError, sqlite3.Error, OSError) as exc:
        print(f'Coding site: {exc}', file=sys.stderr)
        return 2
    print(f'Site generated in {args.output}: {summary["documents"]} documents, '
          f'{summary["codes"]} codes, {summary["codings"]} coded passages, {summary["annotations"]} annotations.')
    return 0


if __name__ == '__main__':
    sys.exit(main())
