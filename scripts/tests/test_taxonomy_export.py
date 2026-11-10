"""Verify publication exports and reference-only database maintenance."""
import json
from pathlib import Path
import sys
import tempfile
import unittest

sys.path.insert(0, str(Path(__file__).resolve().parents[1]))
from export_coding_taxonomy import read_taxonomy, render, update_protocol, update_reference_memos, reference_memo
from merge_qualcoder import read_project
from test_coding_sessions import fixture, sql

ROOT = Path(__file__).resolve().parents[2]


class TaxonomyExportTests(unittest.TestCase):
    def test_reference_updates_preserve_records_and_repeat_without_changes(self):
        taxonomy = json.loads((ROOT / 'coding/taxonomy.json').read_text())
        with tempfile.TemporaryDirectory() as directory:
            project = Path(directory) / 'project.qda'
            fixture(project)
            sql(project, "UPDATE code_name SET name='Carbon Footprint',memo='Researcher note' WHERE cid=1")
            before = read_project(project)
            backup, count = update_reference_memos(project, taxonomy)
            self.assertEqual(count, 2)
            self.assertTrue(backup.exists())
            after = read_project(project)
            for table, rows in before['data'].items():
                if table in ('code_cat', 'code_name'):
                    for original, updated in zip(rows, after['data'][table]):
                        self.assertEqual({k:v for k,v in original.items() if k != 'memo'},
                                         {k:v for k,v in updated.items() if k != 'memo'})
                else:
                    self.assertEqual(rows, after['data'][table])
            self.assertEqual(after['data']['code_name'][0]['memo'], reference_memo(taxonomy, code=taxonomy['categories'][0]))
            self.assertIn('roy2026taxonomy', after['data']['code_name'][0]['memo'])
            self.assertIn('becker2015sustainability', after['data']['code_cat'][0]['memo'])
            self.assertEqual(update_reference_memos(project, taxonomy), (None, 0))
            export = render(read_taxonomy(project), taxonomy, detailed=True)
            self.assertIn(taxonomy['categories'][0]['source_definition'], export)
            self.assertIn('Carbon Footprint', export)
            protocol = Path(directory) / 'protocol.md'
            protocol.write_text('Before\n\n## Threats to validity\n\nAfter\n')
            update_protocol(protocol, export)
            first = protocol.read_text()
            update_protocol(protocol, export)
            self.assertEqual(protocol.read_text(), first)
            self.assertTrue(first.startswith('Before\n'))
            self.assertTrue(first.endswith('After\n'))
