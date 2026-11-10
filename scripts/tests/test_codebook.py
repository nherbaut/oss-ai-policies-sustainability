"""Codebook identity, authority, theory publication and synchronization tests."""
from copy import deepcopy
import hashlib
import json
from pathlib import Path
import shutil
import sqlite3
import subprocess
import tempfile
import unittest
from unittest.mock import patch

import test_coding_sessions as fixtures
from test_coding_sessions import command, fixture, coding, sql
import codebook as cb
import coding_session as cs
import coding_guards as guards
import merge_qualcoder as merger


class CodebookTests(unittest.TestCase):
    def setUp(self):
        self.temp = tempfile.TemporaryDirectory()
        self.addCleanup(self.temp.cleanup)
        self.root = Path(self.temp.name)
        self.base = self.root / 'base.qda'
        fixture(self.base)
        self.snapshot = merger.read_project(self.base)
        self.book = cb.export(self.snapshot)
        self.code = next(k for k, e in self.book['entities'].items() if e['kind'] == 'code')
        self.category = next(k for k, e in self.book['entities'].items() if e['kind'] == 'category')

    def modified(self, statement, origin, coder=None):
        project = self.root / (origin + '.qda')
        shutil.copytree(self.base, project)
        sql(project, statement)
        snap = merger.read_project(project)
        return snap, cb.export(snap, self.book, origin, coder)

    def test_numeric_collisions_are_remapped_in_coding_and_graph_references(self):
        a, ab = self.modified("INSERT INTO code_name(cid,name,owner) VALUES (2,'Local','Alice')", 'alice', 'Alice')
        b, bb = self.modified("INSERT INTO code_name(cid,name,owner) VALUES (2,'Theory','Maintainer')", 'theory')
        local_id = next(k for k in ab['entities'] if k not in self.book['entities'])
        a['data']['code_text'][0]['cid'] = 2
        a['data']['gr_cdct_line_item'] = [dict(glineid=1, fromcid=2, tocid=1, fromcatid=1, tocatid=None)]
        a['data']['gr_memo_item'] = [dict(memo_source_type='code', memo_source_id=2)]
        merged, aliases = cb.merge(self.book, bb, ab)
        self.assertEqual(merged['entities'][local_id]['id'], 3)
        normalized = cb.normalize(a, ab, merged, aliases)
        self.assertEqual(normalized['data']['code_text'][0]['cid'], 3)
        self.assertEqual(normalized['data']['gr_cdct_line_item'][0]['fromcid'], 3)
        self.assertEqual(normalized['data']['gr_memo_item'][0]['memo_source_id'], 3)
        self.assertEqual(normalized['data']['code_text'][0]['pos1'], 5)
        for table in ('code_image', 'code_av'):
            a['data'][table] = [dict(cid=2)]
        a['data']['gr_free_line_item'] = [dict(fromcid=2, tocid=1, fromcatid=1, tocatid=1)]
        mapped = cb.normalize(a, ab, merged)
        self.assertEqual(mapped['data']['code_av'][0]['cid'], 3)
        self.assertEqual(mapped['data']['code_image'][0]['cid'], 3)
        self.assertEqual(mapped['data']['gr_free_line_item'][0]['fromcid'], 3)

    def test_same_name_requires_explicit_revision_bound_decision(self):
        a, ab = self.modified("INSERT INTO code_name(cid,name,owner) VALUES (2,'New','Alice')", 'alice', 'Alice')
        b, bb = self.modified("INSERT INTO code_name(cid,name,owner) VALUES (2,'New','Maintainer')", 'theory')
        local = next(k for k in ab['entities'] if k not in self.book['entities'])
        shared = next(k for k in bb['entities'] if k not in self.book['entities'])
        with self.assertRaises(cb.CodebookConflict):
            cb.merge(self.book, bb, ab)
        r = dict(revision=bb['revision'], choices=[dict(entity=local, action='adopt-shared', target=shared)])
        result, aliases = cb.merge(self.book, bb, ab, r)
        self.assertEqual(result, bb)
        self.assertEqual(aliases, {local: shared})
        r['choices'] = [dict(entity=local, action='rename-local', name='Local new')]
        result, aliases = cb.merge(self.book, bb, ab, r)
        self.assertEqual(result['entities'][local]['name'], 'Local new')
        r['revision'] = 'wrong'
        with self.assertRaisesRegex(merger.MergeError, 'stale'):
            cb.merge(self.book, bb, ab, r)
        with self.assertRaisesRegex(merger.MergeError, 'JSON object'):
            cb.merge(self.book, bb, ab, [])

    def test_shared_authority_deletion_cycles_and_owner_checks(self):
        _, renamed = self.modified("UPDATE code_name SET name='Renamed'", 'rename')
        with self.assertRaisesRegex(merger.MergeError, 'Shared'):
            cb.unchanged_shared(self.book, renamed)
        deleted = cb.book({k: v for k, v in self.book['entities'].items() if k != self.code})
        with self.assertRaisesRegex(merger.MergeError, 'Deleting'):
            cb.merge(self.book, self.book, deleted)
        cyclic = deepcopy(self.book['entities'])
        cyclic[self.category]['parent'] = self.category
        with self.assertRaisesRegex(merger.MergeError, 'cycle'):
            cb.book(cyclic)
        with self.assertRaisesRegex(merger.MergeError, 'belong'):
            self.modified("INSERT INTO code_name(cid,name,owner) VALUES (2,'Other','Bob')", 'other', 'Alice')

    def test_field_conflicts_and_nonconflicting_theory_refinements(self):
        _, ours = self.modified("UPDATE code_name SET name='Ours'", 'ours')
        _, theirs = self.modified("UPDATE code_name SET name='Theirs'", 'theirs')
        with self.assertRaises(cb.CodebookConflict):
            cb.merge(self.book, ours, theirs)
        _, memo = self.modified("UPDATE code_name SET memo='Definition'", 'memo')
        merged, _ = cb.merge(self.book, ours, memo)
        self.assertEqual(merged['entities'][self.code]['name'], 'Ours')
        self.assertEqual(merged['entities'][self.code]['memo'], 'Definition')

    def test_late_theory_preserves_assignments_and_reports_impacted_passages(self):
        incoming = deepcopy(self.snapshot)
        incoming['data']['code_text'].append(dict(incoming['data']['code_text'][0], ctid=2, owner='Alice'))
        incoming['data']['coder_names'].append(dict(name='Alice', visibility=1))
        _, theory = self.modified("UPDATE code_name SET memo='Broader definition'", 'theory')
        destination = cb.normalize(self.snapshot, self.book, theory)
        context = dict(shared=self.book, proposals={}, aliases={})
        report, expected, merged = cb.submission_plan(self.snapshot, destination, incoming, self.book, theory, context, 'alice', 'Alice')
        self.assertEqual(report['summary'], {'code_text:add': 1})
        self.assertEqual(report['late_theory']['affected_passages'][0]['owner'], 'Alice')
        self.assertEqual(len(expected['data']['code_text']), 2)
        self.assertEqual(merged, theory)
        out = self.root / 'candidate.qda'
        cb.write_snapshot(self.base, expected, out)
        self.assertEqual(merger.read_project(out), expected)
        self.assertEqual(merger.read_project(self.base), self.snapshot)

    def test_candidate_includes_uncheckpointed_wal_data(self):
        conn = sqlite3.connect(self.base / 'data.qda')
        conn.execute('PRAGMA journal_mode=WAL')
        conn.execute("UPDATE code_name SET memo='Recovered from WAL'")
        conn.commit()
        copied = self.root / 'wal.qda'
        shutil.copytree(self.base, copied)
        conn.close()
        snapshot = merger.read_project(copied)
        output = self.root / 'wal-candidate.qda'
        cb.write_snapshot(copied, snapshot, output)
        standalone = self.root / 'standalone.db'
        shutil.copy2(output / 'data.qda', standalone)
        with sqlite3.connect(standalone) as candidate:
            self.assertEqual(candidate.execute('SELECT memo FROM code_name').fetchone()[0], 'Recovered from WAL')
        self.assertEqual(merger.read_project(output), snapshot)


class CodebookWorkflowTests(unittest.TestCase):
    fixed_codebook_fixture = False
    setUp = fixtures.WorkflowTests.setUp
    tearDown = fixtures.WorkflowTests.tearDown
    start = fixtures.WorkflowTests.start

    def initialize(self):
        self.workflow.codebook_init()
        command(self.repo, 'git', 'add', cb.REGISTRY)
        command(self.repo, 'git', 'commit', '-m', 'Initialize shared codebook')
        command(self.repo, 'git', 'push', 'origin', 'master')

    def maintenance(self, statement, name='theory'):
        # Simulate a maintainer in a separate checkout so an active coder never switches branches.
        repo = self.root / name
        command(self.root, 'git', 'clone', str(self.remote), str(repo))
        command(repo, 'git', 'config', 'user.name', 'Maintainer')
        command(repo, 'git', 'config', 'user.email', 'maintainer@example.org')
        command(repo, 'git', 'switch', '-c', 'maintenance/' + name)
        workflow = cs.Workflow(repo)
        guards.install(repo)
        guards.writable_database(repo)  # Explicit manual theory editing.
        sql(repo / cs.PROJECT, statement)
        workflow.codebook_register()
        command(repo, 'git', 'add', cs.DATABASE, cb.REGISTRY, 'coding/theory')
        command(repo, 'git', 'commit', '-m', 'Register theory')
        command(repo, 'git', 'push', 'origin', 'HEAD')
        command(repo, 'git', 'switch', 'master')
        with patch('builtins.input', return_value='y'):
            workflow.theory_publish('maintenance/' + name)
        return repo

    def test_init_preserves_database_and_inductive_proposals_integrate(self):
        before = (self.repo / cs.DATABASE).read_bytes()
        self.initialize()
        self.assertEqual((self.repo / cs.DATABASE).read_bytes(), before)
        self.start()
        sql(self.repo / cs.PROJECT, "INSERT INTO code_name(cid,name,owner,memo) VALUES (2,'Inductive','Alice','Local definition')")
        coding(self.repo / cs.PROJECT, 'Alice')
        sql(self.repo / cs.PROJECT, "UPDATE code_text SET cid=2 WHERE owner='Alice'")
        with patch('builtins.input', return_value='y'):
            self.workflow.finish()
        done = self.workflow.state['completed'][-1]
        self.assertEqual(done['codebook_proposals'][0]['after']['name'], 'Inductive')
        self.workflow.request_merge(done['id'])
        with patch('builtins.input', return_value='y'):
            self.workflow.integrate(branch=done['branch'])
        snap = merger.read_project(self.repo / cs.PROJECT)
        self.assertEqual(len(snap['data']['code_text']), 2)
        registry = json.loads((self.repo / cb.REGISTRY).read_text())
        self.assertEqual(len(registry['entities']), 3)
        self.assertEqual(cb.export(snap, registry), registry)
        self.assertFalse((self.repo / cs.DATABASE).stat().st_mode & 0o222)

    def test_sync_requires_new_theory_remaps_local_ids_and_retains_coding(self):
        self.initialize()
        self.start()
        original = deepcopy(self.workflow.state['active'])
        coding(self.repo / cs.PROJECT, 'Alice')
        sql(self.repo / cs.PROJECT, "INSERT INTO code_name(cid,name,owner) VALUES (2,'Local','Alice')")
        sql(self.repo / cs.PROJECT, "UPDATE code_text SET cid=2 WHERE owner='Alice'")
        self.maintenance("INSERT INTO code_name(cid,name,owner) VALUES (2,'Theory','Maintainer')")
        with self.assertRaisesRegex(merger.MergeError, 'coding-sync'):
            self.workflow.finish()
        with patch('builtins.input', return_value='y'):
            self.workflow.sync()
        active = self.workflow.state['active']
        self.assertEqual(active['base'], original['base'])
        self.assertNotEqual(active['checkpoint'], active['base'])
        snap = merger.read_project(self.repo / cs.PROJECT)
        local_id = next(r['cid'] for r in snap['data']['code_name'] if r['name'] == 'Local')
        self.assertEqual(local_id, 3)
        self.assertEqual(next(r['cid'] for r in snap['data']['code_text'] if r['owner'] == 'Alice'), local_id)
        checkpoint = active['checkpoint']
        self.workflow.sync()
        self.assertEqual(active['checkpoint'], checkpoint)
        with patch('builtins.input', return_value='y'):
            self.workflow.finish()
        done = self.workflow.state['completed'][-1]
        self.workflow.request_merge(done['id'])
        with patch('builtins.input', return_value='y'):
            self.workflow.integrate(branch=done['branch'])
        self.assertEqual(len(merger.read_project(self.repo / cs.PROJECT)['data']['code_text']), 2)

    def test_late_theory_after_completion_is_reviewed_on_integration(self):
        self.initialize()
        self.start()
        coding(self.repo / cs.PROJECT, 'Alice')
        with patch('builtins.input', return_value='y'):
            self.workflow.finish()
        done = self.workflow.state['completed'][-1]
        self.workflow.request_merge(done['id'])
        self.maintenance("UPDATE code_name SET memo='Theory update'")
        with patch('builtins.input', return_value='y'):
            self.workflow.integrate(branch=done['branch'])
        audit = json.loads((self.repo / f'coding/merges/{done["id"]}.json').read_text())
        self.assertEqual(audit['report']['late_theory']['affected_passages'][0]['owner'], 'Alice')
        self.assertEqual(merger.read_project(self.repo / cs.PROJECT)['data']['code_name'][0]['memo'], 'Theory update')

    def test_coder_shared_edits_rejected_and_manual_sync_commits_blocked(self):
        self.initialize()
        self.start()
        sql(self.repo / cs.PROJECT, "UPDATE code_name SET memo='Coder shared edit'")
        with self.assertRaisesRegex(merger.MergeError, 'Shared'):
            self.workflow.finish()
        command(self.repo, 'git', 'add', cs.DATABASE)
        with self.assertRaises(Exception):
            command(self.repo, 'git', 'commit', '-m', 'Manual shared edit')

    def test_sync_commit_failure_rolls_back_and_can_retry(self):
        self.initialize()
        self.start()
        coding(self.repo / cs.PROJECT, 'Alice')
        self.maintenance("UPDATE code_name SET memo='New definition'")
        original_db = (self.repo / cs.DATABASE).read_bytes()
        original_state = deepcopy(self.workflow.state)
        original_git = cs.git
        def fail(repo, *args, **kwargs):
            if args[0] == 'commit' and kwargs.get('commit_kind') == 'sync':
                raise merger.MergeError('Injected commit failure')
            return original_git(repo, *args, **kwargs)
        with patch.object(cs, 'git', side_effect=fail), patch('builtins.input', return_value='y'):
            with self.assertRaisesRegex(merger.MergeError, 'Injected'):
                self.workflow.sync()
        self.assertEqual((self.repo / cs.DATABASE).read_bytes(), original_db)
        self.assertEqual(self.workflow.state, original_state)
        self.assertEqual(cs.dirty_paths(self.repo), {cs.DATABASE})
        with patch('builtins.input', return_value='y'):
            self.workflow.sync()
        self.assertEqual(self.workflow.state['active']['phase'], 'active')

    def test_sync_crash_after_commit_recovers_checkpoint(self):
        self.initialize()
        self.start()
        self.maintenance("UPDATE code_name SET memo='Updated'")
        save = self.workflow.save
        def crash():
            if self.workflow.state['active']['phase'] == 'active' and self.workflow.state['active']['checkpoint'] != self.workflow.state['active']['base']:
                raise OSError('Crash after commit')
            save()
        with patch.object(self.workflow, 'save', side_effect=crash), patch('builtins.input', return_value='y'):
            with self.assertRaisesRegex(OSError, 'Crash'):
                self.workflow.sync()
        self.workflow = cs.Workflow(self.repo)
        self.assertEqual(self.workflow.state['active']['phase'], 'syncing')
        with patch('builtins.input', return_value='y'):
            self.workflow.finish()
        self.assertIsNone(self.workflow.state['active'])

    def test_same_name_sync_adoption_and_second_sync(self):
        self.initialize()
        self.start()
        sql(self.repo / cs.PROJECT, "INSERT INTO code_name(cid,name,owner,memo) VALUES (2,'New','Alice','My definition')")
        coding(self.repo / cs.PROJECT, 'Alice')
        sql(self.repo / cs.PROJECT, "UPDATE code_text SET cid=2 WHERE owner='Alice'")
        self.maintenance("INSERT INTO code_name(cid,name,owner,memo) VALUES (2,'New','Maintainer','Shared definition')")
        original_db = (self.repo / cs.DATABASE).read_bytes()
        with self.assertRaises(cb.CodebookConflict) as caught:
            self.workflow.sync()
        self.assertEqual((self.repo / cs.DATABASE).read_bytes(), original_db)
        shared_commit = cs.fetch_master(self.repo)
        shared = cs.tracked_json(self.repo, shared_commit, cb.REGISTRY)
        target = next(k for k, v in shared['entities'].items() if v['name'] == 'New')
        context = self.workflow.state['active']['codebook_context']
        local = cb.branch_book(merger.read_project(self.repo / cs.PROJECT), context, self.workflow.state['active']['id'], 'Alice')
        proposal = next(k for k in local['entities'] if k not in context['shared']['entities'])
        decisions = self.root / 'decisions.json'
        cs.save_json(decisions, dict(revision=caught.exception.report['revision'],
                                    choices=[dict(entity=proposal, action='adopt-shared', target=target)]))
        with patch('builtins.input', return_value='y'):
            self.workflow.sync(decisions)
        snap = merger.read_project(self.repo / cs.PROJECT)
        self.assertEqual(len(snap['data']['code_name']), 2)
        self.assertEqual(next(r['memo'] for r in snap['data']['code_name'] if r['name'] == 'New'), 'Shared definition')
        self.assertFalse(self.workflow.state['active']['codebook_context']['proposals'])
        self.maintenance("UPDATE code_name SET memo='Second shared definition' WHERE name='New'", name='second')
        with patch('builtins.input', return_value='y'):
            self.workflow.sync()
            self.workflow.finish()
        done = self.workflow.state['completed'][-1]
        self.assertEqual(len(done['codebook_context']['history']), 2)
        self.workflow.request_merge(done['id'])
        with patch('builtins.input', return_value='y'):
            self.workflow.integrate(branch=done['branch'])
        self.assertEqual(len(merger.read_project(self.repo / cs.PROJECT)['data']['code_text']), 2)

    def test_sync_does_not_import_other_coders_passages(self):
        self.initialize()
        self.start()
        coding(self.repo / cs.PROJECT, 'Alice')
        maintainer = self.maintenance("UPDATE code_name SET memo='Definition'")
        workflow = cs.Workflow(maintainer)
        with patch('builtins.input', return_value='Bob'):
            workflow.start()
        coding(maintainer / cs.PROJECT, 'Bob', fid=2)
        sql(maintainer / cs.PROJECT, "INSERT INTO code_name(cid,name,owner) VALUES (2,'Bob proposal','Bob')")
        with patch('builtins.input', return_value='y'):
            workflow.finish()
        bob = workflow.state['completed'][-1]
        workflow.request_merge(bob['id'])
        with patch.object(cs.shutil, 'which', return_value=None), patch('builtins.input', return_value='y'):
            workflow.integrate(branch=bob['branch'])
        with patch('builtins.input', return_value='y'):
            self.workflow.sync()
        snap = merger.read_project(self.repo / cs.PROJECT)
        self.assertNotIn('Bob', {r['owner'] for r in snap['data']['code_text']})
        self.assertIn('Bob proposal', {r['name'] for r in snap['data']['code_name']})
        with patch('builtins.input', return_value='y'):
            self.workflow.finish()
        done = self.workflow.state['completed'][-1]
        self.workflow.request_merge(done['id'])
        with patch('builtins.input', return_value='y'):
            self.workflow.integrate(branch=done['branch'])
        self.assertEqual({r['owner'] for r in merger.read_project(self.repo / cs.PROJECT)['data']['code_text']}, {'Baseline','Alice','Bob'})

    def test_interruption_before_sync_commit_restores_backup(self):
        self.initialize()
        self.start()
        coding(self.repo / cs.PROJECT, 'Alice')
        self.maintenance("UPDATE code_name SET memo='Changed'")
        old_db = (self.repo / cs.DATABASE).read_bytes()
        save = self.workflow.save
        def crash_before_mutation():
            save()
            if self.workflow.state['active']['phase'] == 'syncing':
                raise OSError('Power loss before mutation')
        with patch.object(self.workflow, 'save', side_effect=crash_before_mutation), patch('builtins.input', return_value='y'):
            with self.assertRaisesRegex(OSError, 'Power loss'):
                self.workflow.sync()
        self.workflow = cs.Workflow(self.repo)
        self.assertEqual(self.workflow.state['active']['phase'], 'syncing')
        self.workflow.recover_sync(self.workflow.state['active'])
        self.assertEqual((self.repo / cs.DATABASE).read_bytes(), old_db)
        self.assertEqual(self.workflow.state['active']['phase'], 'active')
        self.assertEqual(cs.dirty_paths(self.repo), {cs.DATABASE})

    def test_make_entrypoints_use_the_codebook_protocol(self):
        self.initialize()
        for target, answer in [('coding-start', 'CLI Coder\n'), ('coding-sync', ''), ('coding-finish', 'y\n')]:
            result = subprocess.run(['make', target], cwd=self.repo, input=answer,
                                    text=True, capture_output=True)
            self.assertEqual(result.returncode, 0, result.stdout + result.stderr)
            if target == 'coding-start':
                sql(self.repo / cs.PROJECT,
                    "INSERT INTO code_name(cid,name,owner,supercid) VALUES (2,'Licence stuff','CLI Coder',1)")
        state = cs.Workflow(self.repo).state
        self.assertIsNone(state['active'])
        self.assertEqual(state['completed'][-1]['codebook_version'], 1)
        self.assertEqual(state['completed'][-1]['coder'], 'CLI Coder')
        proposal = state['completed'][-1]['codebook_proposals'][0]['after']
        self.assertEqual(proposal['name'], 'Licence stuff')
        self.assertIsNotNone(proposal['parent'])

    def test_start_requires_registry_before_prompt_or_session_creation(self):
        before = (self.repo / cs.DATABASE).read_bytes()
        branches = command(self.repo, 'git', 'branch', '--list')
        with patch('builtins.input') as prompt:
            with self.assertRaisesRegex(merger.MergeError, 'make coding-codebook-init'):
                self.workflow.start()
            prompt.assert_not_called()
        self.assertIsNone(self.workflow.state['active'])
        self.assertEqual(self.workflow.branch(), 'master')
        self.assertEqual(command(self.repo, 'git', 'branch', '--list'), branches)
        self.assertEqual((self.repo / cs.DATABASE).read_bytes(), before)
        result = subprocess.run(['make', 'coding-start'], cwd=self.repo, text=True, capture_output=True)
        self.assertNotEqual(result.returncode, 0)
        self.assertIn('coding/codebook.json is missing', result.stdout)

    def test_source_taxonomy_alone_does_not_enable_codebook_sessions(self):
        cs.save_json(self.repo / 'coding/taxonomy.json', {'version': 1})
        command(self.repo, 'git', 'add', 'coding/taxonomy.json')
        command(self.repo, 'git', 'commit', '-m', 'Source taxonomy')
        command(self.repo, 'git', 'push', 'origin', 'master')
        with self.assertRaisesRegex(merger.MergeError, 'source taxonomy'):
            self.workflow.start()
        self.assertIsNone(self.workflow.state['active'])
