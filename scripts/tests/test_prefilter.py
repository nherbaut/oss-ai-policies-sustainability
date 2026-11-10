from contextlib import redirect_stdout
import csv
import hashlib
import importlib.util
import io
import json
from pathlib import Path
import sqlite3
import sys
import tempfile
from types import SimpleNamespace
import unittest
from unittest.mock import patch

sys.path.insert(0, str(Path(__file__).resolve().parents[1]))
from compute_rq_similarity import annotation_sample, run
from detect_document_duplicates import export_duplicates
from evaluate_prefilter import evaluate
from prefilter_common import ROOT, PrefilterError, digest, write_csv, write_json
from prefilter_embeddings import (global_embedding, input_length, load_queries, make_chunks,
                                  normalize, score_document)


class CharTokenizer:
    """Deterministic tokenizer for boundary tests; no model downloads."""
    def __call__(self, text, add_special_tokens=True, return_offsets_mapping=False, **kwargs):
        positions = [(i, i + 1) for i, c in enumerate(text) if not c.isspace()]
        ids = [ord(text[a]) for a, _ in positions]
        result = dict(input_ids=[1, *ids, 2] if add_special_tokens else ids)
        if return_offsets_mapping:
            result['offset_mapping'] = positions
        return result

    def decode(self, ids, **kwargs):
        return ''.join(chr(n) for n in ids)


class CorpusFixture:
    def setUp(self):
        self.temporary = tempfile.TemporaryDirectory()
        self.addCleanup(self.temporary.cleanup)
        self.root = Path(self.temporary.name)
        self.project = self.root / 'fixture.qda'
        self.project.mkdir()
        self.database = self.project / 'data.qda'
        self.output = self.root / 'run'
        with sqlite3.connect(self.database) as conn:
            conn.executescript('''
                CREATE TABLE project (databaseversion TEXT);
                INSERT INTO project VALUES ('v17');
                CREATE TABLE source (id INTEGER PRIMARY KEY, name TEXT, fulltext TEXT, memo TEXT);
                CREATE TABLE cases (caseid INTEGER PRIMARY KEY, name TEXT);
                CREATE TABLE case_text (fid INTEGER, caseid INTEGER);
                INSERT INTO cases VALUES (1,'project/a'), (2,'project/b');
                INSERT INTO case_text VALUES (1,1), (2,2), (3,1);
            ''')
            for identity, text in [(1, '# Mission\n\nAI code maintenance and reviewer trust. 😀\n\nWater and energy matter.'),
                                   (2, '# Mission\n\nAI code maintenance and reviewer trust. 😀\n\nWater and energy matter.'),
                                   (3, ' # Mission\n\nAI code maintenance and reviewer trust. 😀\n\nWater and energy matter.'),
                                   (4, ' \n'), (5, None)]:
                memo = json.dumps(dict(schema='oss-ai-policies/document-import-v1',
                                       provenance=[dict(path=f'policies/{identity}.md', role='ai_policy')]))
                conn.execute('INSERT INTO source VALUES (?,?,?,?)', (identity, 'policy.md', text, memo))


class CorpusTests(CorpusFixture, unittest.TestCase):
    def test_exact_duplicates_preserve_occurrences_and_database(self):
        before = self.database.read_bytes()
        report = export_duplicates(self.project, self.output)
        self.assertEqual((report['documents'], report['unique_texts']), (4, 3))
        self.assertEqual(len(report['duplicate_groups']), 1)
        group = report['duplicate_groups'][0]
        self.assertEqual(group['representative_id'], 1)
        self.assertEqual([m['entity'] for m in group['members']], ['project/a', 'project/b'])
        self.assertEqual([d['id'] for d in report['empty_documents']], [4])
        self.assertEqual(report['excluded_sources'][0]['id'], 5)
        self.assertEqual(self.database.read_bytes(), before)
        with (self.output / 'duplicates.csv').open() as stream:
            self.assertEqual(len(list(csv.DictReader(stream))), 4)

    def test_output_must_not_enter_or_contain_project(self):
        for output in [self.project, self.project / 'reports', self.root]:
            with self.subTest(output=output), self.assertRaises(PrefilterError):
                export_duplicates(self.project, output)


class QueryAndChunkTests(unittest.TestCase):
    def test_queries_are_complete_and_hypotheses_excluded(self):
        _, expanded = load_queries(ROOT / 'protocol.md', ROOT / 'scripts/prefilter_queries.json', 'expanded')
        _, original = load_queries(ROOT / 'protocol.md', ROOT / 'scripts/prefilter_queries.json', 'original')
        self.assertEqual([len(r['queries']) for r in expanded], [6, 6, 6, 4])
        self.assertEqual([len(r['queries']) for r in original], [1] * 4)
        self.assertTrue(all('H1:' not in r['scientific_question'] for r in expanded))
        with tempfile.TemporaryDirectory() as temporary:
            protocol = Path(temporary) / 'protocol.md'
            for text in ['', '- **RQ1.**\n', '- **RQ1.** A?\n- **RQ1.** B?\n', '- **RQ1.** Only one?\n']:
                protocol.write_text(text)
                with self.subTest(text=text), self.assertRaises(PrefilterError):
                    load_queries(protocol, ROOT / 'scripts/prefilter_queries.json', 'expanded')

    def test_long_unicode_text_is_covered_without_truncation(self):
        text = 'Intro 😀\n\n# Mission\n\n' + ('abcdefghij 😀 ' * 90) + '\n\n## Water\n\nLast paragraph.'
        tokenizer = CharTokenizer()
        chunks = make_chunks(text, tokenizer, chunk_tokens=60, max_length=128)
        self.assertGreater(len(chunks), 10)
        self.assertEqual(''.join(text[c['start']:c['end']] for c in chunks), text)
        self.assertTrue(all(input_length(tokenizer, c['input']) <= 60 for c in chunks))
        self.assertTrue(all(c['weight'] > 0 for c in chunks))
        self.assertTrue(any(c['title'] == 'Water' for c in chunks))

    def test_overlap_preserves_coverage_and_progress(self):
        text = '# Intro\n\n' + ('A paragraph of words.\n\n' * 50)
        chunks = make_chunks(text, CharTokenizer(), chunk_tokens=60, overlap=8, max_length=128)
        covered = [False] * len(text)
        for chunk in chunks:
            for i in range(chunk['start'], chunk['end']):
                covered[i] = True
        self.assertTrue(all(covered))
        self.assertTrue(all(a['end'] < b['end'] for a, b in zip(chunks, chunks[1:])))
        self.assertTrue(any(a['end'] > b['start'] for a, b in zip(chunks, chunks[1:])))
        self.assertTrue(all(input_length(CharTokenizer(), c['input']) <= 60 for c in chunks))

    def test_code_fences_do_not_create_sections_and_parameters_are_validated(self):
        chunks = make_chunks('# Real\n\n```md\n# Fake\n```\n\nTail', CharTokenizer(), 100, max_length=128)
        self.assertTrue(all(c['title'] == 'Real' for c in chunks))
        for size, overlap in [(513, 0), (10, 0), (64, 32), (64, -1)]:
            with self.subTest(size=size, overlap=overlap), self.assertRaises(PrefilterError):
                make_chunks('Text', CharTokenizer(), size, overlap)

    def test_stratified_sample_is_reproducible_and_groups_are_unique(self):
        documents, rows = [], []
        for i in range(180):
            doc = dict(id=i, text=str(i), sha256=digest(str(i)), entity='project', name='policy.md', provenance=[])
            documents.append(doc)
            rows.append(dict(document_id=i, sha256=doc['sha256'], representative_id=i,
                             entity='project', name='policy.md', role=['ai_policy', 'contributing'][i % 2],
                             characters=i + 1, status='scored'))
        rqs = [dict(id='RQ1')]
        labels, texts = annotation_sample(documents, rows, rqs)
        self.assertEqual((labels, texts), annotation_sample(documents, rows, rqs))
        self.assertEqual(len(labels), 60)
        self.assertEqual(len({r['sha256'] for r in labels}), 60)
        self.assertEqual(sum(r['split'] == 'evaluation' for r in labels), 20)
        self.assertEqual({r['baseline_rank_band'] for r in labels}, {'high', 'middle', 'low'})
        self.assertTrue(all(r['RQ1_label'] == '' for r in labels))


@unittest.skipUnless(importlib.util.find_spec('numpy'), 'Optional NumPy dependency is not installed')
class VectorTests(CorpusFixture, unittest.TestCase):
    def test_weighted_global_vector_and_query_maximum(self):
        import numpy as np
        vector = global_embedding([[1, 0], [0, 1]], [3, 1])
        np.testing.assert_allclose(vector, np.array([3, 1]) / np.sqrt(10), atol=1e-6)
        rqs = [dict(id='RQ1', queries=[dict(id='x'), dict(id='y')]), dict(id='RQ2', queries=[dict(id='negative')])]
        scores = score_document(vector, [[1, 0], [0, 1]], [[1, 0], [0, 1], [-1, 0]], rqs)
        self.assertAlmostEqual(scores['RQ1']['score'], 3 / np.sqrt(10), places=6)
        self.assertEqual(scores['RQ1']['query_id'], 'x')
        self.assertAlmostEqual(scores['RQ1']['passage_score'], 1)
        self.assertLess(scores['RQ2']['score'], 0)
        for invalid in [[[0, 0]], [[float('nan'), 1]]]:
            with self.assertRaises(PrefilterError):
                normalize(invalid)

    def arguments(self, **overrides):
        args = dict(protocol=ROOT / 'protocol.md', queries=ROOT / 'scripts/prefilter_queries.json',
                    project=self.project, output_dir=self.output, cache_dir=None, query_mode='expanded',
                    device='cpu', batch_size=4, chunk_tokens=60, overlap_tokens=0, allow_download=False, limit=None)
        args.update(overrides)
        return SimpleNamespace(**args)

    def fake_run(self, **overrides):
        import numpy as np

        class Model:
            calls = []
            max_seq_length = 512
            tokenizer = CharTokenizer()

            def __init__(self, *args, **kwargs):
                pass

            def get_sentence_embedding_dimension(self):
                return 8

            def encode(self, texts, **kwargs):
                self.calls.extend(texts)
                return np.array([[1, len(t), *[t.lower().count(word) for word in
                                               ['ai', 'mission', 'water', 'trust', 'code', 'review']]] for t in texts], dtype=np.float32)

        with patch.dict(sys.modules, sentence_transformers=SimpleNamespace(SentenceTransformer=Model)), \
                patch('compute_rq_similarity.importlib.metadata.version', return_value='test'), redirect_stdout(io.StringIO()):
            manifest = run(self.arguments(**overrides))
        return manifest, Model.calls

    def test_pipeline_cache_duplicates_empty_texts_and_human_labels(self):
        before = hashlib.sha256(self.database.read_bytes()).hexdigest()
        first, calls = self.fake_run()
        self.assertTrue(calls)
        self.assertEqual(first['counts']['unique_scored'], 2)
        self.assertEqual(first['counts']['scored'], 3)
        with (self.output / 'scores.csv').open() as stream:
            rows = {int(r['document_id']): r for r in csv.DictReader(stream)}
        self.assertEqual(rows[1]['RQ1_score'], rows[2]['RQ1_score'])
        self.assertEqual(rows[4]['RQ1_score'], '')
        self.assertEqual(rows[4]['rank'], '')
        with (self.output / 'annotation.csv').open() as stream:
            labels = list(csv.DictReader(stream))
        fields = list(labels[0])
        labels[0]['notes'] = 'Human work must survive a rerun'
        write_csv(self.output / 'annotation.csv', labels, fields)
        second, calls = self.fake_run()
        self.assertEqual(second['counts']['document_cache_hits'], 2)
        self.assertEqual(calls, [])
        self.assertIn('Human work must survive', (self.output / 'annotation.csv').read_text())
        original, calls = self.fake_run(query_mode='original')
        self.assertEqual(original['counts']['document_cache_hits'], 2)
        self.assertEqual(len(calls), 4)
        with self.assertRaises(PrefilterError):
            evaluate(self.output / 'annotation.csv', [self.output], [1])
        for row in labels:
            for rq in first['rqs']:
                row[f'{rq["id"]}_label'] = 'useful'
        write_csv(self.output / 'annotation.csv', labels, fields)
        metrics = evaluate(self.output / 'annotation.csv', [self.output], [1])
        self.assertTrue(all(m['precision'] == 1 for m in metrics['runs'][0]['metrics']))
        labels[0]['sha256'] = 'stale'
        write_csv(self.output / 'annotation.csv', labels, fields)
        with self.assertRaises(PrefilterError):
            evaluate(self.output / 'annotation.csv', [self.output], [1])
        third, calls = self.fake_run(chunk_tokens=80)
        self.assertEqual(third['counts']['document_cache_hits'], 0)
        self.assertTrue(calls)
        self.assertEqual(hashlib.sha256(self.database.read_bytes()).hexdigest(), before)


class EvaluationTests(unittest.TestCase):
    def test_metrics_are_within_sample_and_ignore_uncertain_labels(self):
        with tempfile.TemporaryDirectory() as temporary:
            root = Path(temporary)
            rows, labels = [], []
            for i in range(8):
                rows.append(dict(document_id=i, sha256=str(i), status='scored', RQ1_score=1 - i / 10))
                labels.append(dict(document_id=i, sha256=str(i), split='evaluation' if i < 4 else 'tuning',
                                   RQ1_label=['uncertain', 'useful', 'not_useful', 'useful'][i % 4]))
            write_csv(root / 'scores.csv', rows, list(rows[0]))
            write_csv(root / 'annotation.csv', labels, list(labels[0]))
            write_json(root / 'manifest.json', dict(corpus_sha256='corpus', protocol_sha256='protocol',
                        rqs=[dict(id='RQ1')], documents=[dict(id=i, sha256=str(i)) for i in range(8)],
                        settings={}, query_mode='expanded'))
            report = evaluate(root / 'annotation.csv', [root], [1, 2])
            at_one, at_two = report['runs'][0]['metrics'][2:4]
            self.assertEqual((at_one['precision'], at_one['recall']), (1, .5))
            self.assertEqual((at_two['precision'], at_two['recall']), (.5, .5))
            self.assertEqual(at_one['uncertain'], 1)
            labels.append(dict(labels[0], split='tuning'))
            write_csv(root / 'annotation.csv', labels, list(labels[0]))
            with self.assertRaises(PrefilterError):
                evaluate(root / 'annotation.csv', [root], [1])


if __name__ == '__main__':
    unittest.main()
