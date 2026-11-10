"""Destructive taxonomy maintenance is tested on isolated fixture projects only."""
from pathlib import Path
import stat
import sys
import tempfile
import unittest
from unittest.mock import patch

sys.path.insert(0, str(Path(__file__).resolve().parents[1]))
from import_sustainability_taxonomy import load_taxonomy, reset_project, code_memo
from merge_qualcoder import MergeError, read_project
from test_coding_sessions import fixture, sql

ROOT = Path(__file__).resolve().parents[2]


class TaxonomyImportTests(unittest.TestCase):
    def setUp(self):
        self.temporary = tempfile.TemporaryDirectory()
        self.addCleanup(self.temporary.cleanup)
        self.root = Path(self.temporary.name)
        self.project = self.root / 'coding.qda'
        fixture(self.project)
        sql(self.project, "INSERT INTO annotation(fid,pos0,pos1,owner,memo) VALUES (1,0,5,'Baseline','Old note')")
        self.backups = self.root / 'backups'
        self.taxonomy = ROOT / 'coding/taxonomy.json'

    def test_preview_preserves_input_and_does_not_create_backup(self):
        before = (self.project / 'data.qda').read_bytes()
        with patch('import_sustainability_taxonomy.ensure_closed'):
            report = reset_project(self.project, self.taxonomy, self.backups)
        self.assertFalse(report['applied'])
        self.assertEqual(report['removed']['code_text'], 1)
        self.assertEqual(report['removed']['annotation'], 1)
        self.assertEqual((self.project / 'data.qda').read_bytes(), before)
        self.assertFalse(self.backups.exists())

    def test_import_resets_coding_and_preserves_corpus_backup_and_permissions(self):
        (self.project / 'data.qda').chmod(0o444)
        before = read_project(self.project)
        with patch('import_sustainability_taxonomy.ensure_closed'):
            report = reset_project(self.project, self.taxonomy, self.backups, apply=True)
        after = read_project(self.project)
        self.assertEqual(read_project(Path(report['backup'])), before)
        for table in ('source', 'cases', 'case_text', 'coder_names'):
            self.assertEqual(after['data'][table], before['data'][table])
        for table in ('code_text', 'annotation', 'code_av', 'code_image'):
            self.assertEqual(after['data'][table], [])
        self.assertEqual(len(after['data']['code_cat']), 5)
        codes = after['data']['code_name']
        self.assertEqual(len(codes), 25)
        taxonomy = load_taxonomy(self.taxonomy)
        self.assertEqual([r['memo'] for r in codes], [code_memo(c, taxonomy) for c in taxonomy['categories']])
        self.assertIn('Security Concerns', {c['name'] for c in codes})
        social = next(c for c in codes if c['name'] == 'Social Engineering')
        self.assertIn('Sustainability Category Correlations.xlsx', social['memo'])
        self.assertIn('Definitions!A31', social['memo'])
        self.assertEqual(stat.S_IMODE((self.project / 'data.qda').stat().st_mode), 0o444)
        self.assertTrue(Path(report['report']).is_file())

    def test_failed_candidate_keeps_original_database(self):
        before = (self.project / 'data.qda').read_bytes()
        with patch('import_sustainability_taxonomy.ensure_closed'), \
                patch('import_sustainability_taxonomy.check_candidate', side_effect=MergeError('Test rejection')):
            with self.assertRaises(MergeError):
                reset_project(self.project, self.taxonomy, self.backups, apply=True)
        self.assertEqual((self.project / 'data.qda').read_bytes(), before)
        self.assertEqual(len(list(self.backups.glob('*.qda'))), 1)

    def test_graphs_and_open_project_are_not_silently_destroyed(self):
        sql(self.project, "INSERT INTO graph(grid,name) VALUES (1,'Existing graph')")
        before = (self.project / 'data.qda').read_bytes()
        with patch('import_sustainability_taxonomy.ensure_closed'):
            with self.assertRaisesRegex(MergeError, 'graphs'):
                reset_project(self.project, self.taxonomy, self.backups, apply=True)
        with patch('import_sustainability_taxonomy.ensure_closed', side_effect=MergeError('Close QualCoder')):
            with self.assertRaisesRegex(MergeError, 'Close QualCoder'):
                reset_project(self.project, self.taxonomy, self.backups, apply=True)
        self.assertEqual((self.project / 'data.qda').read_bytes(), before)

    def test_source_taxonomy_status_and_count_are_explicit(self):
        taxonomy = load_taxonomy(self.taxonomy)
        self.assertEqual(len(taxonomy['categories']), 25)
        self.assertEqual(sum(c['status'] == 'source_authored' for c in taxonomy['categories']), 20)
        self.assertTrue(all(c['source_definition'] is None for c in taxonomy['categories'] if c['dimension'] == 'Individual'))


if __name__ == '__main__':
    unittest.main()
