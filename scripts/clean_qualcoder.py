"""Clean HTML in existing QualCoder documents; preview unless --apply is supplied.

Requires pandoc, beautifulsoup4, lxml and markdown-it-py. Original corpus files are never edited.
"""
import argparse
import hashlib
import json
import os
import re
import shutil
import sqlite3
import subprocess
from collections import Counter
from datetime import datetime
from pathlib import Path

from bs4 import BeautifulSoup, Comment
from markdown_it import MarkdownIt

ROOT = Path(__file__).resolve().parents[1]
VERSION = 'oss-ai-policies/clean-markdown-v1'
# Only actual HTML tags, not placeholders such as <username> or <repository>.
TAGS = ('a abbr address article aside audio b blockquote body br button caption '
        'center cite code col colgroup dd del details dfn dialog div dl dt em '
        'fieldset figcaption figure footer form h1 h2 h3 h4 h5 h6 head header '
        'hr html i iframe img input kbd label legend li link main mark menu meta '
        'nav noscript object ol optgroup option p picture pre q s samp script '
        'section select small source span strike strong style sub summary sup '
        'svg table tbody td textarea tfoot th thead time title tr u ul var video').split()
TAG = re.compile(r'</?(?:' + '|'.join(TAGS) + r')\b(?:[^>"\']|"[^"]*"|\'[^\']*\')*>', re.I)


def sha(text):
    return hashlib.sha256(text.encode('utf-8')).hexdigest()


def protect_code(text):
    """Mask code examples before examining/normalizing HTML, retaining exact text."""
    saved = {}
    # A nonce derived from the document avoids collisions with its actual prose.
    prefix = 'QCCODE' + sha(text)[:16]
    def mask(match):
        key = prefix + str(len(saved)) + 'END'
        saved[key] = match.group()
        return key
    # Parse block context: indentation inside an HTML layout is not a code
    # example, whereas standalone indented code and fences are literal.
    lines = text.splitlines(keepends=True)
    for token in reversed(MarkdownIt('commonmark').parse(text)):
        if token.type in ('fence', 'code_block') and token.map:
            start, end = token.map
            value = ''.join(lines[start:end])
            key = prefix + str(len(saved)) + 'END'
            saved[key] = value.rstrip('\n')
            lines[start:end] = [key + '\n']
    text = ''.join(lines)
    text = re.sub(r'(`+)([^`]|(?!\1)`)*?\1', mask, text)
    return text, saved


def restore_code(text, saved):
    for key, value in saved.items():
        text = text.replace(key, value)
    return text


def pandoc(text, reader, writer):
    return subprocess.run(['pandoc', '--from=' + reader, '--to=' + writer,
                           '--wrap=none'], input=text, text=True,
                          capture_output=True, check=True, timeout=60).stdout


def flatten_table(table):
    for node in list(table.find_all(['caption', 'thead', 'tbody', 'tfoot', 'tr', 'td', 'th', 'colgroup', 'col'])):
        if node.find_parent('table') is table:
            if node.name in ('td', 'th', 'caption'):
                node.name = 'div'
                node.attrs = {}
            else:
                node.unwrap()
    table.name = 'div'
    table.attrs = {}


def clean(text):
    masked, saved = protect_code(text)
    if not TAG.search(masked) and not re.search(r'!\[[^\]]*\]\(data:image/', masked):
        return text, []
    # Pandoc's Markdown reader handles mixed Markdown inside HTML blocks. Fold
    # multiline attributes first, without changing literal code examples.
    def normalize_tag(match):
        tag = re.sub(r'\s*\n\s*', ' ', match.group())
        # Entity-encoded tags in tooltip attributes confuse Pandoc's Markdown
        # reader (notably anti-spam email markup). They are not visible prose.
        return re.sub(r'\s+title=("[^"]*(?:&lt;|&gt;)[^"]*"|\'[^\']*(?:&lt;|&gt;)[^\']*\')', '', tag, flags=re.I)
    masked = TAG.sub(normalize_tag, masked)
    lines = masked.splitlines(keepends=True)
    for token in reversed(MarkdownIt('commonmark').parse(masked)):
        if token.type == 'html_block' and token.level == 0 and token.map:
            start, end = token.map
            for index in range(start, end):
                lines[index] = re.sub(r'^[ \t]+(?=</?(?:' + '|'.join(TAGS) + r')\b)', '', lines[index])
    masked = ''.join(lines)
    # Pandoc accepts arbitrary raw HTML names; protect prose placeholders that
    # an HTML parser would otherwise silently discard as unknown elements.
    masked = re.sub(r'<(/?)([A-Za-z][\w:-]*)([^<>]*?)>',
                    lambda m: m.group() if m[2].lower() in TAGS else '&lt;' + m.group()[1:], masked)
    html = pandoc(restore_code(masked, saved),
                  'markdown-smart-citations+raw_html+markdown_in_html_blocks', 'html')
    soup = BeautifulSoup(html, 'lxml')
    for node in soup.find_all(string=lambda s: isinstance(s, Comment)):
        node.extract()
    for node in soup.find_all(['script', 'style']):
        node.decompose()
    for node in soup.find_all('svg'):
        description = ' '.join(x.get_text(' ', strip=True) for x in node.find_all(['text', 'title', 'desc']))
        node.replace_with(description or node.get('aria-label', ''))
    for node in soup.find_all('img'):
        if node.get('src', '').startswith('data:'):
            node.replace_with(node.get('alt', ''))
    # Empty decoration links and heading permalink symbols obscure the prose.
    for node in soup.find_all('a'):
        if not node.get_text(strip=True) and not node.find('img'):
            node.decompose()
        elif 'headerlink' in node.get('class', []) and node.get_text(strip=True) in ('#', '¶'):
            node.decompose()
    # Pandoc can emit only "[TABLE]" for nested/complex layout tables. Flatten
    # these into paragraphs before conversion, retaining every cell's content.
    for table in list(soup.find_all('table')):
        complex_table = table.find('table') or table.find(['div', 'p', 'ul', 'ol', 'h1', 'h2', 'h3', 'pre'])
        if complex_table:
            flatten_table(table)
    result = pandoc(str(soup), 'html', 'gfm-raw_html').strip() + '\n'
    if '[TABLE]' in result and soup.find('table'):
        for table in list(soup.find_all('table')):
            flatten_table(table)
        result = pandoc(str(soup), 'html', 'gfm-raw_html').strip() + '\n'
    if not result.strip():
        raise ValueError('Conversion produced empty text')
    # Detect writer failures like [TABLE] without relying on document length:
    # large image payload removal can legitimately reduce a file by >99%.
    def normalized(value):
        return re.sub(r'[\W_]+', '', value)
    # Check text nodes separately: Markdown links introduce URLs between nodes,
    # and emphasis/footnote syntax changes apparent word boundaries. Neither is
    # lost prose. Long repeated text fragments must retain their multiplicity.
    fragments = Counter(normalized(str(node)) for node in soup.find_all(string=True)
                        if len(normalized(str(node))) >= 2)
    def missing_fragments(markdown):
        actual = normalized(markdown)
        return [fragment[:100] for fragment, count in fragments.items()
                if fragment not in actual or (len(fragment) > 16 and actual.count(fragment) < count)]
    missing = missing_fragments(result)
    if missing:
        # Mixed list/HTML layouts may produce malformed nesting that Pandoc's
        # HTML reader truncates. Remove layout wrappers and retry, keeping the
        # semantic elements (headings, lists, links, emphasis and code).
        for node in list(soup.find_all(['div', 'span'])):
            if node.name == 'div':
                node.insert_before(soup.new_tag('br'))
                node.insert_after(soup.new_tag('br'))
            node.unwrap()
        result = pandoc(str(soup), 'html', 'gfm-raw_html').strip() + '\n'
        missing = missing_fragments(result)
        if missing:
            raise ValueError('Visible text missing after conversion: ' + ', '.join(list(missing)[:12]))
    masked_result, literal_code = protect_code(result)
    masked_result = re.sub(r'(?m)^[ \t]+$', '', masked_result)
    result = restore_code(re.sub(r'\n{3,}', '\n\n', masked_result), literal_code)
    literal_free, _ = protect_code(result)
    warnings = []
    if TAG.search(literal_free) or re.search(r'\\<(?:' + '|'.join(TAGS) + r')\b', literal_free, re.I):
        warnings.append('Possible HTML remnants outside code examples')
    if len(result) < len(text) * .1:
        warnings.append('Output is less than 10% of original length; inspect retained prose')
    return result, warnings


def connect(project, readonly=True):
    db = (project / 'data.qda').resolve()
    conn = sqlite3.connect(db.as_uri() + ('?mode=ro' if readonly else '?mode=rw'), uri=True)
    conn.row_factory = sqlite3.Row
    if conn.execute('SELECT databaseversion FROM project').fetchone()[0] != 'v17':
        conn.close()
        raise ValueError('Only inspected QualCoder schema v17 is supported')
    return conn


def file_path(project, source):
    media = source['mediapath']
    if not media or not media.startswith('/docs/'):
        raise ValueError('Source has no internal document copy')
    path = (project / 'documents' / media[6:]).resolve()
    if not path.is_relative_to((project / 'documents').resolve()):
        raise ValueError('Document path escapes project')
    return path


def positional_reasons(conn, source):
    fid = source['id']
    reasons = []
    for table, column in [('code_text', 'fid'), ('annotation', 'fid'),
                          ('code_av', 'id'), ('code_image', 'id')]:
        if conn.execute(f'SELECT 1 FROM {table} WHERE {column}=? LIMIT 1', (fid,)).fetchone():
            reasons.append(table)
    if source['av_text_id'] or conn.execute('SELECT 1 FROM source WHERE av_text_id=?', (fid,)).fetchone():
        reasons.append('audio/video transcript')
    if conn.execute('SELECT 1 FROM case_text WHERE fid=? AND (pos0 IS NOT 0 OR pos1 IS NOT ?)',
                    (fid, len(source['fulltext']))).fetchone():
        reasons.append('partial case link')
    p = conn.execute('SELECT bookmarkfile,bookmarkpos,avbookmarkfile,avbookmarktextpos FROM project').fetchone()
    if (p[0] == fid and p[1]) or (p[2] == fid and p[3]):
        reasons.append('bookmark position')
    return reasons


def plan(conn, project):
    operations, report = [], []
    for row in conn.execute('SELECT * FROM source ORDER BY id').fetchall():
        source = dict(row)
        text = source['fulltext']
        item = dict(source_id=source['id'], name=source['name'])
        report.append(item)
        if text is None:
            item.update(status='skipped', reason='non-text source')
            continue
        reasons = positional_reasons(conn, source)
        if reasons:
            item.update(status='skipped', reason=', '.join(reasons))
            continue
        try:
            metadata = json.loads(source['memo'] or '{}')
        except ValueError:
            metadata = None
        if not isinstance(metadata, dict):
            metadata = {'previous_memo': source['memo']}
        previous = metadata.get('conversion', {})
        if previous.get('version') == VERSION:
            if previous['converted_sha256'] != sha(text):
                item.update(status='failed', reason='Previously converted text changed; review required')
            else:
                item.update(status='unchanged', reason='already converted')
            continue
        try:
            converted, warnings = clean(text)
            if converted == text:
                item.update(status='unchanged', reason='no HTML requiring conversion')
                continue
            path = file_path(project, source)
            if path.read_text(encoding='utf-8-sig') != text:
                raise ValueError('Document copy differs from database text')
            metadata['conversion'] = dict(version=VERSION, original_sha256=sha(text),
                                          converted_sha256=sha(converted))
            metadata['text_format'] = 'Clean Markdown for coding; original corpus retained.'
            item.update(status='converted', original_length=len(text), converted_length=len(converted),
                        original_sha256=sha(text), converted_sha256=sha(converted), warnings=warnings)
            operations.append(dict(source=source, text=converted, path=path,
                                   memo=json.dumps(metadata, indent=2, ensure_ascii=False)))
        except (ValueError, OSError, subprocess.SubprocessError) as error:
            item.update(status='failed', reason=str(error))
    return operations, report


def verify(conn, saved, operations, project):
    """Compare the entire database against the backup, allowing only intended edits."""
    changes = {op['source']['id']: op for op in operations}
    for (table,) in saved.execute("SELECT name FROM sqlite_master WHERE type='table'"):
        old = [dict(r) for r in saved.execute(f'SELECT * FROM "{table}" ORDER BY rowid')]
        if table == 'source':
            for row in old:
                if row['id'] in changes:
                    op = changes[row['id']]
                    row.update(fulltext=op['text'], memo=op['memo'])
        elif table == 'case_text':
            for row in old:
                if row['fid'] in changes:
                    row['pos1'] = len(changes[row['fid']]['text'])
        assert old == [dict(r) for r in conn.execute(f'SELECT * FROM "{table}" ORDER BY rowid')], table
    for op in operations:
        assert file_path(project, op['source']).read_text(encoding='utf-8-sig') == op['text']
    assert conn.execute('PRAGMA integrity_check').fetchone()[0] == 'ok'
    assert not conn.execute('PRAGMA foreign_key_check').fetchall()


def apply(project, operations):
    database = project / 'data.qda'
    busy = subprocess.run(['lsof', '-t', str(database)], capture_output=True, text=True)
    if busy.returncode not in (0, 1) or busy.stdout.strip():
        raise RuntimeError('Cannot confirm database is closed; close QualCoder before applying')
    stamp = datetime.now().astimezone().strftime('%Y%m%d-%H%M%S-%f')
    backup = ROOT / 'data/qualcoder-backups' / f'coding-before-markdown-cleanup-{stamp}.qda'
    shutil.copytree(project, backup)
    with sqlite3.connect(database) as live, sqlite3.connect(backup / 'data.qda') as saved:
        live.backup(saved)
    conn = connect(project, False)
    changed_files = []
    try:
        conn.execute('BEGIN IMMEDIATE')
        for op in operations:
            source = op['source']
            current = dict(conn.execute('SELECT * FROM source WHERE id=?', (source['id'],)).fetchone())
            if current != source or positional_reasons(conn, current):
                raise ValueError('Project changed after preview; rerun conversion')
            if op['path'].read_text(encoding='utf-8-sig') != source['fulltext']:
                raise ValueError('Document copy changed after preview')
            staged = op['path'].with_name(op['path'].name + '.cleaning')
            if staged.exists():
                raise ValueError('Staging file already exists: ' + str(staged))
            try:
                staged.write_text(op['text'], encoding='utf-8')
                os.replace(staged, op['path'])
            finally:
                if staged.exists():
                    staged.unlink()
            changed_files.append(op['path'])
            conn.execute('UPDATE source SET fulltext=?,memo=? WHERE id=?', (op['text'], op['memo'], source['id']))
            conn.execute('UPDATE case_text SET pos1=? WHERE fid=?', (len(op['text']), source['id']))
        with connect(backup) as saved:
            verify(conn, saved, operations, project)
        conn.commit()
    except BaseException:
        conn.rollback()
        for path in changed_files:
            shutil.copy2(backup / path.relative_to(project), path)
        raise
    finally:
        conn.close()
    return backup


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--project', type=Path, default=ROOT / 'data/coding.qda')
    parser.add_argument('--apply', action='store_true')
    parser.add_argument('--report', type=Path, help='Write a JSON report (preview otherwise writes no files)')
    args = parser.parse_args()
    project = args.project.resolve()
    with connect(project) as conn:
        operations, documents = plan(conn, project)
    report = dict(project=str(project), version=VERSION,
                  pandoc=subprocess.run(['pandoc', '--version'], capture_output=True, text=True, check=True).stdout.splitlines()[0],
                  summary=dict(Counter(item['status'] for item in documents)), documents=documents)
    print(json.dumps(report['summary'], indent=2))
    if args.apply and operations:
        # Close the preview connection before lsof's live-access check.
        conn.close()
        report['backup'] = str(apply(project, operations))
        report['applied_at'] = datetime.now().astimezone().isoformat()
        print('Backup:', report['backup'])
    report_path = args.report
    if args.apply and report_path is None:
        report_path = ROOT / 'analysis/corpus-assessment/qualcoder-cleanup.json'
    if report_path:
        report_path.write_text(json.dumps(report, indent=2, ensure_ascii=False) + '\n')


if __name__ == '__main__':
    main()
