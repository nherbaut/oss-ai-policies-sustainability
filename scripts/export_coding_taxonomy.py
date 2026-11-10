"""Export the live QualCoder taxonomy and its reference memos for publication."""
import argparse
from contextlib import closing
from datetime import datetime, timezone
import json
import html
import subprocess
import textwrap
from pathlib import Path
import shutil
import sqlite3
import stat

from merge_qualcoder import ensure_closed, MergeError

ROOT = Path(__file__).resolve().parents[1]
START = '<!-- BEGIN GENERATED CODING TAXONOMY -->'
END = '<!-- END GENERATED CODING TAXONOMY -->'


def reference_memo(taxonomy, dimension=None, code=None):
    excerpts = taxonomy['dimension_excerpts'][dimension] if code is None else code['memo_excerpts']
    return '\n\n'.join('“' + entry['text'] + '”\n\n— ' + entry['source'] for entry in excerpts)


def update_reference_memos(project, taxonomy):
    """Update only matching taxonomy memos in a backed-up SQLite transaction."""
    ensure_closed(project)
    database = project / 'data.qda'
    if database.is_symlink():
        raise MergeError('Refusing a database symlink')
    categories = {c['raw_label']: c for c in taxonomy['categories']}
    with closing(sqlite3.connect(database.as_uri() + '?mode=ro', uri=True)) as conn:
        updates = []
        for table, pk in [('code_cat', 'catid'), ('code_name', 'cid')]:
            for identity, name, memo in conn.execute(f'SELECT {pk},name,memo FROM {table}'):
                if table == 'code_cat' and name in taxonomy['dimension_references']:
                    block = reference_memo(taxonomy, dimension=name)
                elif table == 'code_name' and name in categories:
                    block = reference_memo(taxonomy, code=categories[name])
                else:
                    continue
                updated = block
                if memo != updated:
                    updates.append((table, pk, identity, memo, updated))
        for identity, memo in conn.execute('SELECT rowid,memo FROM project'):
            for marker in ('\n\n[Taxonomie de soutenabilité OSS/GenAI]\n', '\n\n[Taxonomy source excerpts]\n'):
                if marker in (memo or ''):
                    prefix = memo.split(marker, 1)[0]
                    excerpts = '\n\n'.join(reference_memo(taxonomy, dimension=d) for d in taxonomy['dimension_excerpts'])
                    updated = prefix + '\n\n[Taxonomy source excerpts]\n' + excerpts
                    if updated != memo:
                        updates.append(('project', 'rowid', identity, memo, updated))
                    break
    if not updates:
        return None, 0
    backup_dir = project.parent / 'qualcoder-backups'
    backup_dir.mkdir(exist_ok=True)
    backup = backup_dir / ('references-' + datetime.now(timezone.utc).strftime('%Y%m%d-%H%M%S-%f') + '.sqlite')
    mode = stat.S_IMODE(database.stat().st_mode)
    with closing(sqlite3.connect(database.as_uri() + '?mode=ro', uri=True)) as source, closing(sqlite3.connect(backup)) as target:
        source.backup(target)
    database.chmod(mode | stat.S_IWUSR)
    try:
        with closing(sqlite3.connect(database)) as conn, conn:
            conn.execute('BEGIN IMMEDIATE')
            for table, pk, identity, old, new in updates:
                cursor = conn.execute(f'UPDATE {table} SET memo=? WHERE {pk}=? AND memo IS ?', (new, identity, old))
                if cursor.rowcount != 1:
                    raise MergeError('A memo changed during preparation. Retry after closing QualCoder.')
            if conn.execute('PRAGMA integrity_check').fetchone()[0] != 'ok':
                raise MergeError('Database integrity check failed')
    finally:
        database.chmod(mode)
    return backup, len(updates)


def read_taxonomy(project):
    with closing(sqlite3.connect((project / 'data.qda').as_uri() + '?mode=ro', uri=True)) as conn:
        conn.row_factory = sqlite3.Row
        conn.execute('BEGIN')
        return {table: [dict(r) for r in conn.execute(f'SELECT * FROM {table} ORDER BY {pk}')]
                for table, pk in [('code_cat','catid'), ('code_name','cid')]}


def cell(text):
    return str(text or '').replace('\\', '\\\\').replace('|', '\\|').replace('\n', '<br>')


def render(snapshot, taxonomy, detailed=False):
    categories = {c['raw_label']: c for c in taxonomy['categories']}
    groups = {c['catid']: c for c in snapshot['code_cat']}
    def group_path(identity):
        names, seen = [], set()
        while identity is not None:
            if identity in seen or identity not in groups:
                raise MergeError('Invalid category hierarchy')
            seen.add(identity)
            group = groups[identity]
            names.insert(0, group['name'])
            identity = group['supercatid']
        return ' / '.join(names) or 'Uncategorised'
    lines = ['### Sustainability coding taxonomy', '',
             'The five high-level dimensions follow the Karlskrona manifesto [@becker2015sustainability]. '
             'The twenty categories assigned to the environmental, technical, social and economic dimensions '
             'are drawn from Roy et al. [@roy2026taxonomy]. The five individual-level categories are provisional '
             'literature-derived extensions whose original definitions require verification. '
             'Operational definitions and coding guidance are adaptations by the research team for OSS/GenAI.', '',
             '| Dimension | Category | Provenance |', '|---|---|---|']
    for row in snapshot['code_name']:
        definition = categories.get(row['name'])
        if definition and definition['status'] == 'source_authored':
            source = 'Roy et al. [@roy2026taxonomy]'
        elif definition:
            source = 'Provisional literature extension'
        else:
            source = 'See code memo for provenance'
        label = row['name']
        if row.get('supercid'):
            parent = next((r['name'] for r in snapshot['code_name'] if r['cid'] == row['supercid']), None)
            if parent is None:
                raise MergeError('Missing parent code')
            label = parent + ' / ' + label
        lines.append(f'| {cell(group_path(row["catid"]))} | {cell(label)} | {source} |')
    lines += ['', 'Source labels are retained to preserve traceability, including “Longitivity” and '
              '“Social Engineering”. The latter has divergent meanings in the source materials, '
              'which are documented in its QualCoder memo. Coding distinguishes policy requirements, '
              'stated concerns, possible effects and observed effects. Each new code or category receives '
              'a memo recording its reference and source location, or its inductive origin and supporting corpus passages.',
              '', 'The complete exported codebook includes the live QualCoder memos, operational definitions, '
              'coding guidance and reference details. Regenerate it with `make coding-taxonomy-export`.', '']
    if detailed:
        for table in ('code_cat', 'code_name'):
            for row in snapshot[table]:
                lines += ['### ' + row['name'], '', row.get('memo') or 'Provenance memo pending.', '']
        lines += ['## Bibliographic references', ''] + list(taxonomy['references'].values())
    return '\n'.join(lines) + '\n'


def export_diagram(snapshot, taxonomy, output):
    """Build a publication figure whose citations are supplied by its caption."""
    colours = ['#EDF5E6', '#E7F0FA', '#F2EAF7', '#FFF1DC', '#E3F3F0']
    lines = ['digraph taxonomy {',
             'graph [rankdir=TB, bgcolor="white", pad="0.25", nodesep="0.22", ranksep="0.5"];',
             'node [shape=plain, fontname="Arial", fontsize=12];',
             'edge [color="#87939C", penwidth=1.2, arrowhead=none];',
             'root [label=<<B>OSS / GenAI sustainability taxonomy</B>>];']
    groups = snapshot['code_cat']
    for index, group in enumerate(groups):
        key = 'group' + str(group['catid'])
        title = html.escape(group['name'])
        rows = [f'<TR><TD BGCOLOR="{colours[index % len(colours)]}" CELLPADDING="12"><B>{title}</B></TD></TR>']
        for code in snapshot['code_name']:
            if code['catid'] != group['catid']:
                continue
            label = '<BR/>'.join(html.escape(part) for part in textwrap.wrap(code['name'], 28))
            rows.append(f'<TR><TD ALIGN="LEFT" CELLPADDING="9">{label}</TD></TR>')
        label = '<TABLE BORDER="1" COLOR="#C7D0D7" CELLBORDER="0" CELLSPACING="0">' + ''.join(rows) + '</TABLE>'
        lines.append(f'{key} [label=<{label}>];')
        parent = 'group' + str(group['supercatid']) if group['supercatid'] else 'root'
        lines.append(f'{parent} -> {key};')
    roots = ['group' + str(g['catid']) for g in groups if not g['supercatid']]
    lines.append('{rank=same; ' + '; '.join(roots) + ';}')
    lines.append('}')
    dot = output / 'taxonomy.dot'
    dot.write_text('\n'.join(lines) + '\n')
    if not shutil.which('dot'):
        raise MergeError('Install Graphviz to render taxonomy.svg and taxonomy.png from taxonomy.dot')
    for extension in ('svg', 'png'):
        subprocess.run(['dot', '-T' + extension, '-Gdpi=160', str(dot), '-o', str(output / ('taxonomy.' + extension))], check=True)


def update_protocol(path, section):
    content = path.read_text()
    block = START + '\n' + section + END
    if START in content and END in content:
        before, rest = content.split(START, 1)
        _, after = rest.split(END, 1)
        content = before + block + after
    elif START in content or END in content:
        raise MergeError('Incomplete generated taxonomy markers in protocol')
    else:
        anchor = '## Threats to validity'
        if anchor not in content:
            raise MergeError('Cannot locate taxonomy insertion point')
        content = content.replace(anchor, block + '\n\n' + anchor, 1)
    path.write_text(content)


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--project', type=Path, default=ROOT / 'data/coding.qda')
    parser.add_argument('--taxonomy', type=Path, default=ROOT / 'coding/taxonomy.json')
    parser.add_argument('--output', type=Path, default=ROOT / 'coding/exports')
    parser.add_argument('--update-protocol', action='store_true')
    parser.add_argument('--update-reference-memos', action='store_true')
    args = parser.parse_args()
    taxonomy = json.loads(args.taxonomy.read_text())
    project = args.project.resolve()
    if args.update_reference_memos:
        backup, count = update_reference_memos(project, taxonomy)
        print(f'Updated {count} reference memos. Backup: {backup}')
    snapshot = read_taxonomy(project)
    args.output.mkdir(parents=True, exist_ok=True)
    caption = 'Sustainability coding taxonomy. Dimensions follow the Karlskrona manifesto [@becker2015sustainability], and twenty categories follow Roy et al. [@roy2026taxonomy]. Individual-level categories are provisional.'
    (args.output / 'taxonomy.md').write_text(f'![{caption}](taxonomy.png)\n\n' + render(snapshot, taxonomy, detailed=True))
    (args.output / 'taxonomy.json').write_text(json.dumps(dict(project=str(project), references=taxonomy['references'], **snapshot), indent=2, ensure_ascii=False) + '\n')
    shutil.copyfile(ROOT / 'refs.bib', args.output / 'refs.bib')
    export_diagram(snapshot, taxonomy, args.output)
    if args.update_protocol:
        import os
        figure = Path(os.path.relpath(args.output / 'taxonomy.png', ROOT)).as_posix()
        section = render(snapshot, taxonomy) + f'\n![{caption}]({figure}){{width=100%}}\n'
        update_protocol(ROOT / 'protocol.md', section)
    print(f'Exported taxonomy to {args.output}')


if __name__ == '__main__':
    main()
