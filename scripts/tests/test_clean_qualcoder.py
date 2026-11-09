import json
from pathlib import Path
import sqlite3
import sys
import tempfile
import unittest
from unittest.mock import patch

sys.path.insert(0, str(Path(__file__).resolve().parents[1]))
import clean_qualcoder as cleaner
import import_qualcoder as importer


class ConversionTests(unittest.TestCase):
    def test_mixed_html_and_literal_code(self):
        text = '''# Policy

<div class="layout">

## Rules

Use <strong>human review</strong> and <a href="https://example.com"
title="Policy">this policy</a>.

<div style="display:none">Hidden policy evidence</div>

</div>

```html
<div class="example">literal</div>
```

Use `<span>example</span>` and <username>.
'''
        out, warnings = cleaner.clean(text)
        for expected in ['# Policy', '## Rules', '**human review**',
                         '[this policy](https://example.com "Policy")',
                         'Hidden policy evidence', '<div class="example">literal</div>',
                         '`<span>example</span>`', 'username']:
            self.assertIn(expected, out)
        self.assertNotIn('class="layout"', out)
        self.assertFalse(warnings)

    def test_table_image_and_decoration(self):
        out, _ = cleaner.clean('''<div><script>unwanted()</script><style>.x{color:red}</style>
<!-- comment --><svg><path d="huge"/></svg>
<img src="data:image/png;base64,HUGE" alt="Architecture diagram">
<table><tr><th>Rule</th><th>Meaning</th></tr>
<tr><td>Review</td><td>Humans decide</td></tr></table></div>''')
        for value in ['Architecture diagram', 'Review', 'Humans decide', '|']:
            self.assertIn(value, out)
        for value in ['unwanted', 'color:red', 'comment', 'HUGE', '<svg']:
            self.assertNotIn(value, out)

    def test_plain_markdown_is_unchanged(self):
        text = '# Rules\n\nRead policy.\n\n```html\n<div>example</div>\n```\n'
        self.assertEqual(cleaner.clean(text), (text, []))

    def test_empty_conversion_rejected(self):
        with self.assertRaises(ValueError):
            cleaner.clean('<script>nothing substantive</script>')

    def test_layout_tables_and_indented_html_preserve_prose(self):
        out, warnings = cleaner.clean('''<div>
    <img alt="Logo" src="logo.svg">
</div>

<table><tr><td>Navigation</td><td><table><tr><td>
<h2>Project overview</h2><p>Important evidence inside layout.</p>
</td></tr></table></td></tr></table>''')
        for expected in ['![Logo](logo.svg)', 'Navigation', 'Project overview', 'Important evidence inside layout.']:
            self.assertIn(expected, out)
        self.assertNotIn('[TABLE]', out)
        self.assertFalse(warnings)

    def test_email_markup_is_not_parsed_as_a_citation(self):
        out, warnings = cleaner.clean('Email: <span>t<span>e</span>amtype</span>@zormit<i title="&lt;/i&gt;mailto:">.</i>de')
        self.assertIn('teamtype@zormit', out)
        self.assertNotIn('mailto:', out)
        self.assertFalse(warnings)

    def test_html_links_inside_markdown_lists(self):
        out, warnings = cleaner.clean('''<div class="wrapper">

- <div class="label">

  <a href="https://example.com/one"
  class="navigation">First rule</a>

  </div>

- <div class="label">

  <a href="https://example.com/two"
  class="navigation">Second rule</a>

  </div>

</div>

## Policy

Preserve the entire policy.''')
        for expected in ['[First rule](https://example.com/one)',
                         '[Second rule](https://example.com/two)', 'Preserve the entire policy.']:
            self.assertIn(expected, out)
        self.assertFalse(warnings)

    def test_truncated_conversion_is_rejected(self):
        original = cleaner.pandoc
        def truncate(text, reader, writer):
            if reader == 'html':
                return 'Incomplete output\n'
            return original(text, reader, writer)
        with patch.object(cleaner, 'pandoc', truncate):
            with self.assertRaisesRegex(ValueError, 'Visible text missing'):
                cleaner.clean('<div>This important policy must survive conversion.</div>')


class ProjectTests(unittest.TestCase):
    def setUp(self):
        self.temp = tempfile.TemporaryDirectory()
        self.root = Path(self.temp.name)
        self.project = self.root / 'data/test.qda'
        (self.project / 'documents').mkdir(parents=True)
        # Use the actual schema to exercise all database preservation checks.
        live = sqlite3.connect((cleaner.ROOT / 'data/coding.qda/data.qda').as_uri() + '?mode=ro', uri=True)
        schema = [r[0] for r in live.execute("SELECT sql FROM sqlite_master WHERE type='table'")]
        live.close()
        conn = sqlite3.connect(self.project / 'data.qda')
        for sql in schema:
            conn.execute(sql)
        conn.execute("INSERT INTO project(databaseversion,codername) VALUES ('v17','test')")
        conn.execute("INSERT INTO cases(caseid,name) VALUES (1,'Example')")
        conn.execute("INSERT INTO code_name(cid,name) VALUES (1,'Review')")
        for fid, text in enumerate(['# Rules\n\n<div>Human <b>review</b>.</div>\n',
                                    '<div>Already coded</div>\n',
                                    '<div>Annotated</div>\n',
                                    '<div>Partial link</div>\n'], 1):
            name = f'{fid}.md'
            meta = dict(schema=importer.MARKER, entity='Example', text_sha256=cleaner.sha(text),
                        provenance=[], text_format='Original Markdown/text; no analytical codes imported.')
            conn.execute('INSERT INTO source(id,name,fulltext,mediapath,memo) VALUES (?,?,?,?,?)',
                         (fid, name, text, '/docs/' + name, json.dumps(meta)))
            conn.execute('INSERT INTO case_text(caseid,fid,pos0,pos1) VALUES (1,?,0,?)',
                         (fid, 5 if fid == 4 else len(text)))
            (self.project / 'documents' / name).write_text(text)
        conn.execute("INSERT INTO code_text(cid,fid,seltext,pos0,pos1) VALUES (1,2,'Already coded',5,18)")
        conn.execute("INSERT INTO annotation(fid,pos0,pos1,memo) VALUES (3,5,14,'Keep')")
        conn.commit()
        conn.close()

    def tearDown(self):
        self.temp.cleanup()

    def preview(self):
        conn = cleaner.connect(self.project)
        try:
            return cleaner.plan(conn, self.project)
        finally:
            conn.close()

    def test_apply_preserves_coding_and_second_run_is_empty(self):
        ops, report = self.preview()
        self.assertEqual([o['source']['id'] for o in ops], [1])
        self.assertEqual([r['status'] for r in report], ['converted', 'skipped', 'skipped', 'skipped'])
        original = ops[0]['source']['fulltext']
        with patch.object(cleaner, 'ROOT', self.root):
            backup = cleaner.apply(self.project, ops)
        self.assertTrue((backup / 'data.qda').exists())
        self.assertEqual((backup / 'documents/1.md').read_text(), original)
        self.assertFalse(self.preview()[0])
        conn = cleaner.connect(self.project)
        # The importer must retain cleaned text, source identity and link range.
        documents = [dict(entity='Example', text=original, text_sha256=cleaner.sha(original),
                          role='policy', provenance=[])]
        planned, cases = importer.plan(conn, ['Example'], documents)
        self.assertEqual(cases, [])
        self.assertEqual(planned[0]['existing']['id'], 1)
        self.assertEqual(planned[0]['text'], ops[0]['text'])
        self.assertTrue(planned[0]['already_linked'])
        self.assertEqual(planned[0]['memo'], ops[0]['memo'])
        # An unrecorded edit must never be silently accepted by the importer.
        conn.close()
        conn = cleaner.connect(self.project, False)
        conn.execute("UPDATE source SET fulltext='unexpected edit' WHERE id=1")
        conn.commit()
        with self.assertRaises(ValueError):
            importer.plan(conn, ['Example'], documents)
        conn.close()

    def test_failure_restores_database_and_files(self):
        ops, _ = self.preview()
        original = (self.project / 'documents/1.md').read_bytes()
        with patch.object(cleaner, 'ROOT', self.root), patch.object(cleaner, 'verify', side_effect=ValueError('injected')):
            with self.assertRaisesRegex(ValueError, 'injected'):
                cleaner.apply(self.project, ops)
        self.assertEqual((self.project / 'documents/1.md').read_bytes(), original)
        self.assertEqual(len(self.preview()[0]), 1)


if __name__ == '__main__':
    unittest.main()
