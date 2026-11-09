import hashlib
import json
from pathlib import Path
import sqlite3
import sys
import tempfile
import unittest

sys.path.insert(0, str(Path(__file__).resolve().parents[1]))
import build_coding_site as site


class CodingSiteTests(unittest.TestCase):
    def setUp(self):
        self.temp = tempfile.TemporaryDirectory()
        self.addCleanup(self.temp.cleanup)
        self.root = Path(self.temp.name)
        self.project = self.root / 'test.qda'
        self.project.mkdir()
        self.database = self.project / 'data.qda'
        self.output = self.root / 'site'
        self.text = '😀 Alpha beta <script>alert(1)</script> café'
        with sqlite3.connect(self.database) as conn:
            conn.executescript('''
                CREATE TABLE project (databaseversion TEXT);
                INSERT INTO project VALUES ('v17');
                CREATE TABLE source (id INTEGER PRIMARY KEY, name TEXT, fulltext TEXT, memo TEXT);
                CREATE TABLE code_name (cid INTEGER PRIMARY KEY, name TEXT, memo TEXT, catid INTEGER,
                                        supercid INTEGER, color TEXT);
                CREATE TABLE code_cat (catid INTEGER PRIMARY KEY, name TEXT, memo TEXT, supercatid INTEGER);
                CREATE TABLE cases (caseid INTEGER PRIMARY KEY, name TEXT);
                CREATE TABLE case_text (id INTEGER PRIMARY KEY, fid INTEGER, caseid INTEGER);
                CREATE TABLE code_text (ctid INTEGER PRIMARY KEY, cid INTEGER, fid INTEGER, pos0 INTEGER,
                                        pos1 INTEGER, seltext TEXT, owner TEXT, memo TEXT, date TEXT, important INTEGER);
                CREATE TABLE annotation (anid INTEGER PRIMARY KEY, fid INTEGER, pos0 INTEGER,
                                         pos1 INTEGER, owner TEXT, memo TEXT, date TEXT);
                INSERT INTO code_cat VALUES (1, 'Root', 'Category memo', NULL), (2, 'Child', '', 1);
                INSERT INTO code_name VALUES (1, 'Quality', 'Code memo', 2, NULL, '#abcdef'),
                                             (2, 'Review', '', 2, 1, '#123456');
                INSERT INTO cases VALUES (1, 'a/project'), (2, 'b/project');
                INSERT INTO case_text VALUES (1, 1, 1), (2, 2, 2);
                INSERT INTO code_text VALUES (1, 1, 1, 3, 13, 'Alpha beta', 'Alice', 'First memo', '2026', 1),
                                             (2, 2, 1, 8, 12, 'beta', 'Bob', '', '2026', 0);
                INSERT INTO annotation VALUES (1, 1, 3, 8, 'Bob', 'Annotation memo', '2026');
            ''')
            memo = json.dumps({'schema': 'oss-ai-policies/document-import-v1', 'entity': 'a/project',
                               'provenance': [{'path': 'policies/a/policy.md'}]})
            conn.execute('INSERT INTO source VALUES (1, ?, ?, ?)', ('policy.md', self.text, memo))
            conn.execute('INSERT INTO source VALUES (2, ?, ?, ?)', ('policy.md', 'No coding here', 'Plain memo'))

    def change(self, sql):
        with sqlite3.connect(self.database) as conn:
            conn.execute(sql)

    def test_native_and_legacy_positions(self):
        self.assertEqual(site.browser_span(self.text, 3, 13, 'Alpha beta'), (3, 13))
        self.assertEqual(site.browser_span(self.text, 2, 12, 'Alpha beta'), (3, 13))
        self.assertEqual(site.browser_span(self.text, 3, 8), (3, 8))
        self.assertEqual(site.browser_span('😀x', 0, 1, '😀'), (0, 2))
        for start, end, selected in [(3, 13, 'wrong'), (-1, 3, None), (8, 3, None), (0, 999, None)]:
            with self.subTest(start=start, end=end), self.assertRaises(site.ExportError):
                site.browser_span(self.text, start, end, selected)

    def test_export_preserves_coding_and_database(self):
        before = hashlib.sha256(self.database.read_bytes()).hexdigest()
        summary = site.build(self.project, self.output)
        self.assertEqual(summary, dict(documents=2, codes=2, categories=2, codings=2, annotations=1))
        raw = (self.output / 'data.js').read_text()
        exported = json.loads(raw.removeprefix('window.CODING_DATA = ').removesuffix(';\n'))
        doc, other = exported['documents']
        self.assertEqual(doc['text'], self.text)
        self.assertEqual((doc['codings'][1]['start'], doc['codings'][1]['end']), (9, 13))
        self.assertEqual([item['owner'] for item in doc['codings']], ['Alice', 'Bob'])
        self.assertEqual(doc['codings'][0]['memo'], 'First memo')
        self.assertTrue(doc['codings'][0]['important'])
        self.assertEqual(doc['annotations'][0]['memo'], 'Annotation memo')
        self.assertEqual(other['entity'], 'b/project')
        self.assertEqual(other['codings'], [])
        self.assertEqual(hashlib.sha256(self.database.read_bytes()).hexdigest(), before)
        self.assertFalse((self.project / 'data.qda-journal').exists())
        self.assertTrue((self.output / '.nojekyll').is_file())
        self.assertEqual(site.build(self.project, self.output), summary)
        self.assertEqual((self.output / 'data.js').read_text(), raw)

    def test_empty_coding_is_valid(self):
        self.change('DELETE FROM code_text')
        self.change('DELETE FROM annotation')
        snapshot = site.read_snapshot(self.project)
        self.assertEqual(snapshot['summary']['codings'], 0)
        self.assertEqual(len(snapshot['documents']), 2)

    def test_invalid_references_or_offsets_do_not_produce_output(self):
        statements = [
            'UPDATE code_text SET cid=99 WHERE ctid=1',
            'UPDATE code_text SET fid=99 WHERE ctid=1',
            'UPDATE code_text SET pos1=999 WHERE ctid=1',
            "UPDATE code_text SET seltext='incorrect' WHERE ctid=1",
            'UPDATE code_name SET catid=99 WHERE cid=1',
            'UPDATE code_name SET supercid=2 WHERE cid=1',
            'UPDATE code_cat SET supercatid=2 WHERE catid=1',
            'UPDATE case_text SET caseid=99 WHERE id=1',
            'UPDATE annotation SET pos0=-1 WHERE anid=1',
        ]
        original = self.database.read_bytes()
        for sql in statements:
            with self.subTest(sql=sql):
                self.database.write_bytes(original)
                self.change(sql)
                with self.assertRaises(site.ExportError):
                    site.build(self.project, self.output)
                self.assertFalse(self.output.exists())

    def test_invalid_snapshot_keeps_previous_export(self):
        site.build(self.project, self.output)
        previous = (self.output / 'data.js').read_bytes()
        self.change('DELETE FROM code_name WHERE cid=1')
        with self.assertRaises(site.ExportError):
            site.build(self.project, self.output)
        self.assertEqual((self.output / 'data.js').read_bytes(), previous)

    def test_output_guards(self):
        for output in [self.project, self.project / 'export', self.root]:
            with self.subTest(output=output), self.assertRaises(site.ExportError):
                site.build(self.project, output)
        self.output.mkdir()
        (self.output / 'index.html').write_text('Unrelated file')
        with self.assertRaises(site.ExportError):
            site.build(self.project, self.output)
        self.assertEqual((self.output / 'index.html').read_text(), 'Unrelated file')


if __name__ == '__main__':
    unittest.main()
