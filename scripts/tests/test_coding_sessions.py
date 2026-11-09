"""Offline collaboration tests: temporary projects, local remotes, fake GitHub."""
from contextlib import closing, redirect_stdout
import io
import json
import os
from pathlib import Path
import shutil
import sqlite3
import subprocess
import sys
import tempfile
import unittest
from unittest.mock import patch

sys.path.insert(0, str(Path(__file__).resolve().parents[1]))
import coding_session as session
import merge_qualcoder as merger

ROOT = Path(__file__).resolve().parents[2]


def command(cwd, *args):
    return subprocess.check_output(args, cwd=cwd, text=True, stderr=subprocess.PIPE).strip()


def fixture(project):
    (project / 'documents').mkdir(parents=True)
    original = sqlite3.connect((ROOT / 'data/coding.qda/data.qda').as_uri() + '?mode=ro', uri=True)
    schema = [r[0] for r in original.execute("SELECT sql FROM sqlite_master WHERE type='table'")]
    original.close()
    with closing(sqlite3.connect(project / 'data.qda')) as conn, conn:
        for sql in schema:
            conn.execute(sql)
        conn.execute("INSERT INTO project(databaseversion,codername,memo) VALUES ('v17','default','Shared research')")
        for name in ['default', 'Baseline']:
            conn.execute('INSERT INTO coder_names(name,visibility) VALUES (?,1)', (name,))
        conn.execute("INSERT INTO code_cat(catid,name) VALUES (1,'Social')")
        conn.execute("INSERT INTO code_name(cid,name,catid) VALUES (1,'Review',1)")
        for fid in [1, 2]:
            text = 'Human review is required. AI use must be disclosed.\n'
            name = f'{fid}.md'
            (project / 'documents' / name).write_text(text)
            conn.execute('INSERT INTO source(id,name,fulltext,mediapath) VALUES (?,?,?,?)', (fid, name, text, '/docs/' + name))
            conn.execute('INSERT INTO cases(caseid,name) VALUES (?,?)', (fid, f'Case {fid}'))
            conn.execute('INSERT INTO case_text(caseid,fid,pos0,pos1) VALUES (?,?,0,?)', (fid, fid, len(text)))
        conn.execute("INSERT INTO code_text(ctid,cid,fid,pos0,pos1,seltext,owner,date) VALUES (1,1,1,0,5,'Human','Baseline','2026-01-01')")


def sql(project, statement, values=()):
    with closing(sqlite3.connect(project / 'data.qda')) as conn, conn:
        conn.execute(statement, values)


def coding(project, coder, fid=1, start=6, end=12, memo=None):
    with closing(sqlite3.connect(project / 'data.qda')) as conn, conn:
        text = conn.execute('SELECT fulltext FROM source WHERE id=?', (fid,)).fetchone()[0]
        conn.execute('INSERT INTO code_text(cid,fid,pos0,pos1,seltext,owner,memo,date) VALUES (1,?,?,?,?,?,?,?)',
                     (fid, start, end, text[start:end], coder, memo, '2026-01-02'))


class MergerTests(unittest.TestCase):
    def setUp(self):
        self.temp = tempfile.TemporaryDirectory()
        self.root = Path(self.temp.name)
        self.base = self.root / 'base.qda'
        fixture(self.base)
        self.dest = self.root / 'destination.qda'
        self.donor = self.root / 'submission.qda'
        shutil.copytree(self.base, self.dest)
        shutil.copytree(self.base, self.donor)

    def tearDown(self):
        self.temp.cleanup()

    def plan(self, coder='Alice'):
        return merger.plan_merge(*(merger.read_project(p) for p in (self.base, self.dest, self.donor)), coder)

    def test_different_documents_and_same_document_preserve_independence(self):
        coding(self.dest, 'Bob', fid=2)
        coding(self.dest, 'Bob', fid=1)
        coding(self.donor, 'Alice', fid=1)
        sql(self.donor, "INSERT INTO annotation(fid,pos0,pos1,owner,memo) VALUES (1,0,5,'Alice','Interpretation')")
        report = self.plan()
        self.assertFalse(report['conflicts'])
        output = self.root / 'merged.qda'
        merger.write_candidate(self.base, self.dest, self.donor, 'Alice', output, report)
        rows = merger.read_project(output)['data']['code_text']
        self.assertEqual(len(rows), 4)
        self.assertEqual(len({r['ctid'] for r in rows}), 4)
        self.assertEqual({r['owner'] for r in rows}, {'Alice', 'Bob', 'Baseline'})
        self.assertEqual(len(merger.read_project(output)['data']['annotation']), 1)
        self.assertEqual(len(merger.read_project(self.base)['data']['code_text']), 1)

    def test_one_sided_edits_and_deletions(self):
        sql(self.donor, "UPDATE code_text SET memo='Reviewed' WHERE ctid=1")
        self.assertEqual(self.plan('Baseline')['summary'], {'code_text:edit': 1})
        sql(self.donor, 'DELETE FROM code_text')
        report = self.plan('Baseline')
        self.assertEqual(report['summary'], {'code_text:delete': 1})
        output = self.root / 'deleted.qda'
        merger.write_candidate(self.base, self.dest, self.donor, 'Baseline', output, report)
        self.assertEqual(merger.read_project(output)['data']['code_text'], [])

    def test_conflicting_edits_and_delete_vs_edit(self):
        sql(self.dest, "UPDATE code_text SET memo='Ours' WHERE ctid=1")
        sql(self.donor, "UPDATE code_text SET memo='Theirs' WHERE ctid=1")
        self.assertEqual(len(self.plan('Baseline')['conflicts']), 1)
        sql(self.donor, 'DELETE FROM code_text')
        self.assertEqual(len(self.plan('Baseline')['conflicts']), 1)
        output = self.root / 'conflicted.qda'
        with self.assertRaisesRegex(merger.MergeError, 'Conflicts'):
            merger.write_candidate(self.base, self.dest, self.donor, 'Baseline', output)
        self.assertFalse(output.exists())

    def test_identical_additions_and_edits_coalesce_despite_ids_dates(self):
        coding(self.dest, 'Alice')
        coding(self.donor, 'Alice')
        sql(self.donor, "UPDATE code_text SET ctid=99,date='2026-02-01' WHERE owner='Alice'")
        self.assertEqual(self.plan()['summary'], {})
        for project in (self.dest, self.donor):
            sql(project, "DELETE FROM code_text WHERE owner='Alice'")
        sql(self.dest, "UPDATE code_text SET memo='same' WHERE ctid=1")
        sql(self.donor, "UPDATE code_text SET memo='same',date='2026-02-01' WHERE ctid=1")
        self.assertEqual(self.plan('Baseline')['summary'], {})

    def test_incompatible_same_owner_additions_conflict(self):
        coding(self.dest, 'Alice', memo='ours')
        coding(self.donor, 'Alice', memo='theirs')
        self.assertEqual(len(self.plan()['conflicts']), 1)

    def test_structure_changes_and_other_coder_edits_are_rejected(self):
        for statement, pattern in [
            ("UPDATE code_name SET name='New name'", 'fixed table'),
            ("UPDATE cases SET memo='Changed'", 'fixed table'),
            ("UPDATE source SET fulltext='Changed'", 'excerpt|offset|fixed table'),
            ("UPDATE code_text SET memo='Someone else changed this'", 'another coder')]:
            with self.subTest(statement=statement):
                shutil.copy2(self.base / 'data.qda', self.donor / 'data.qda')
                sql(self.donor, statement)
                with self.assertRaisesRegex(merger.MergeError, pattern):
                    self.plan()

    def test_invalid_offsets_and_excerpts_rejected(self):
        coding(self.donor, 'Alice')
        sql(self.donor, 'UPDATE code_text SET pos1=999 WHERE owner=?', ('Alice',))
        with self.assertRaisesRegex(merger.MergeError, 'offsets'):
            self.plan()
        sql(self.donor, "UPDATE code_text SET pos1=12,seltext='wrong' WHERE owner='Alice'")
        with self.assertRaisesRegex(merger.MergeError, 'excerpt'):
            self.plan()

    def test_changed_document_file_rejected(self):
        (self.donor / 'documents/1.md').write_text('Changed')
        with self.assertRaisesRegex(merger.MergeError, 'document/media|Document copy'):
            self.plan()

    def test_graph_reference_blocks_deletion(self):
        for project in [self.base, self.dest, self.donor]:
            sql(project, 'INSERT INTO gr_free_text_item(gfreeid,ctid) VALUES (1,1)')
        sql(self.donor, 'DELETE FROM code_text')
        with self.assertRaisesRegex(merger.MergeError, 'graph reference'):
            self.plan('Baseline')

    def test_ui_changes_ignored_and_destination_ui_retained(self):
        sql(self.donor, "UPDATE project SET codername='Alice',bookmarkpos=9")
        sql(self.dest, "UPDATE project SET codername='Bob',bookmarkpos=12")
        coding(self.donor, 'Alice')
        report = self.plan()
        out = self.root / 'ui.qda'
        merger.write_candidate(self.base, self.dest, self.donor, 'Alice', out, report)
        self.assertEqual(merger.read_project(out)['data']['project'][0]['codername'], 'Bob')

    def test_closed_database_and_preview_revalidation(self):
        conn = sqlite3.connect(self.donor / 'data.qda')
        conn.execute('SELECT * FROM project').fetchall()
        try:
            with self.assertRaisesRegex(merger.MergeError, 'Close QualCoder'):
                merger.ensure_closed(self.donor)
        finally:
            conn.close()
        report = self.plan()
        coding(self.donor, 'Alice')
        with self.assertRaisesRegex(merger.MergeError, 'changed after preview'):
            merger.write_candidate(self.base, self.dest, self.donor, 'Alice', self.root / 'stale.qda', report)

    def test_cli_cannot_write_report_into_an_input_project(self):
        original = (self.base / 'data.qda').read_bytes()
        result = subprocess.run([sys.executable, '-B', str(ROOT / 'scripts/merge_qualcoder.py'),
                                 '--base', str(self.base), '--destination', str(self.dest),
                                 '--submission', str(self.donor), '--coder', 'Alice',
                                 '--report', str(self.base / 'data.qda')], capture_output=True, text=True)
        self.assertEqual(result.returncode, 2)
        self.assertIn('Report must be outside', result.stderr)
        self.assertEqual((self.base / 'data.qda').read_bytes(), original)


class FakeGitHub:
    def __init__(self, repo):
        self.repo = repo
        self.prs = {}
        self.fail_create = False
        self.fail_close = False

    def __call__(self, *args):
        def option(name):
            return str(args[args.index(name) + 1])
        operation = args[1]
        if operation == 'list':
            fields = option('--json').split(',')
            return json.dumps([{k: dict(number=n, **p)[k] for k in fields} for n, p in self.prs.items()
                               if p['headRefName'] == option('--head') and
                               (option('--state') == 'all' or p['state'].lower() == option('--state'))])
        if operation == 'create':
            if self.fail_create:
                self.fail_create = False
                raise merger.MergeError('Simulated GitHub outage')
            n = len(self.prs) + 1
            branch = option('--head')
            self.prs[n] = dict(state='OPEN', isDraft=True, isCrossRepository=False,
                               headRefName=branch, headRefOid=command(self.repo, 'git', 'rev-parse', branch),
                               baseRefName='master', body=Path(option('--body-file')).read_text(),
                               url=f'https://example.invalid/pr/{n}', comments=[])
            return self.prs[n]['url']
        number = int(args[2])
        pr = self.prs[number]
        if operation == 'view':
            return json.dumps({k: pr[k] for k in option('--json').split(',')})
        if operation == 'comment':
            pr['comments'].append(dict(body=Path(option('--body-file')).read_text()))
            return ''
        if operation == 'close':
            if self.fail_close:
                self.fail_close = False
                raise merger.MergeError('Simulated PR closure outage')
            pr['state'] = 'CLOSED'
            return ''
        raise AssertionError(args)


class WorkflowTests(unittest.TestCase):
    def setUp(self):
        self.temp = tempfile.TemporaryDirectory()
        self.root = Path(self.temp.name)
        self.repo = self.root / 'repo'
        self.remote = self.root / 'remote.git'
        self.repo.mkdir()
        command(self.root, 'git', 'init', '--bare', '--initial-branch=master', str(self.remote))
        command(self.repo, 'git', 'init', '--initial-branch=master')
        command(self.repo, 'git', 'config', 'user.name', 'Test Maintainer')
        command(self.repo, 'git', 'config', 'user.email', 'test@example.invalid')
        command(self.repo, 'git', 'config', 'commit.gpgsign', 'false')
        fixture(self.repo / session.PROJECT)
        (self.repo / '.gitignore').write_text('__pycache__/\ndata/*_BKUP_*.qda/\ndata/*.qda/ai_data/\n')
        command(self.repo, 'git', 'add', '.')
        command(self.repo, 'git', 'commit', '-m', 'Shared baseline')
        command(self.repo, 'git', 'remote', 'add', 'origin', str(self.remote))
        command(self.repo, 'git', 'push', '-u', 'origin', 'master')
        self.workflow = session.Workflow(self.repo)
        self.github = FakeGitHub(self.repo)
        self.workflow.gh = self.github
        self.gh_path = patch.object(session.shutil, 'which', return_value='/mock/gh')
        self.gh_path.start()
        self.addCleanup(self.gh_path.stop)
        self.output = io.StringIO()
        self.redirect = redirect_stdout(self.output)
        self.redirect.__enter__()

    def tearDown(self):
        self.redirect.__exit__(None, None, None)
        self.temp.cleanup()

    def start(self, coder='Alice'):
        with patch('builtins.input', return_value=coder):
            self.workflow.start()

    def complete(self, coder='Alice', fid=1):
        self.start(coder)
        coding(self.repo / session.PROJECT, coder, fid=fid)
        with patch('builtins.input', return_value='y'):
            self.workflow.finish()
        return self.workflow.state['completed'][-1]

    def submit(self, coder='Alice', fid=1):
        done = self.complete(coder, fid)
        self.workflow.request_merge(done['id'])
        # Simulate the server-side Action; clients no longer create PRs.
        body = self.root / f'{done["id"]}-pr.md'
        body.write_text('<!-- qualcoder-session-v1: ' + json.dumps({'id': done['id'], 'head': done['head']}) + ' -->')
        self.github('pr', 'create', '--head', done['branch'], '--body-file', body)
        return done

    def test_start_finish_cancel_and_recovery(self):
        base = command(self.repo, 'git', 'rev-parse', 'HEAD')
        self.start()
        branch = self.workflow.branch()
        self.assertTrue(branch.startswith('coding/alice/'))
        self.assertEqual(merger.read_project(self.repo / session.PROJECT)['data']['project'][0]['codername'], 'Alice')
        coding(self.repo / session.PROJECT, 'Alice')
        with patch('builtins.input', return_value='n'):
            self.workflow.finish()
        self.assertEqual(command(self.repo, 'git', 'rev-parse', 'HEAD'), base)
        self.assertEqual(self.workflow.branch(), branch)
        with patch('builtins.input', return_value='y'):
            self.workflow.finish()
        self.assertEqual(self.workflow.branch(), 'master')
        self.assertIsNone(self.workflow.state['active'])
        done = self.workflow.state['completed'][0]
        files = command(self.repo, 'git', 'diff', '--name-only', base, done['head']).splitlines()
        self.assertEqual(set(files), {session.DATABASE, f'coding/sessions/{done["id"]}.json'})

    def test_finish_recovers_after_commit_before_state_update(self):
        self.start()
        coding(self.repo / session.PROJECT, 'Alice')
        real_save = self.workflow.save
        calls = 0
        def crash():
            nonlocal calls
            calls += 1
            if calls == 2:
                raise OSError('Interrupted after commit')
            real_save()
        with patch.object(self.workflow, 'save', crash), patch('builtins.input', return_value='y'):
            with self.assertRaisesRegex(OSError, 'Interrupted'):
                self.workflow.finish()
        recovered = session.Workflow(self.repo)
        self.assertEqual(recovered.state['active']['phase'], 'committing')
        recovered.finish()
        self.assertEqual(recovered.branch(), 'master')
        self.assertEqual(len(recovered.state['completed']), 1)

    def test_dirty_checkout_default_name_and_other_coder_edits(self):
        (self.repo / 'unrelated.txt').write_text('Do not stage')
        with self.assertRaisesRegex(merger.MergeError, 'uncommitted'):
            self.start()
        (self.repo / 'unrelated.txt').unlink()
        with self.assertRaisesRegex(merger.MergeError, 'nonempty coder'):
            self.start('default')
        self.start()
        sql(self.repo / session.PROJECT, "UPDATE code_text SET memo='Changed baseline owner' WHERE ctid=1")
        with self.assertRaisesRegex(merger.MergeError, 'another coder'):
            self.workflow.finish()
        self.assertEqual(command(self.repo, 'git', 'diff', '--cached', '--name-only'), '')

    def test_request_retry_duplicate_and_amended_submission(self):
        done = self.complete()
        with patch.object(session.shutil, 'which', return_value=None), patch.object(self.workflow, 'gh', side_effect=AssertionError('No GitHub CLI calls allowed')):
            self.workflow.request_merge(done['id'])
            self.workflow.request_merge(done['id'])
        self.assertEqual(command(self.remote, 'git', 'rev-parse', done['branch']), done['head'])
        self.assertEqual(len(self.github.prs), 0)
        command(self.repo, 'git', 'switch', done['branch'])
        command(self.repo, 'git', 'commit', '--allow-empty', '-m', 'Unexpected extra commit')
        with self.assertRaisesRegex(merger.MergeError, 'amended'):
            self.workflow.request_merge(done['id'])

    def test_publish_menu_offers_only_unpublished_sessions(self):
        published = self.submit('Alice')
        pending = self.complete('Bob')
        with patch('builtins.input', side_effect=AssertionError('Only Bob should be eligible; no menu is needed')):
            self.workflow.request_merge(None)
        self.assertEqual(command(self.remote, 'git', 'rev-parse', pending['branch']), pending['head'])
        self.assertEqual(published['publication_status'], 'published')
        with patch.object(session, 'git', wraps=session.git) as git_calls, patch('builtins.input', side_effect=AssertionError('No unpublished sessions should be offered')):
            self.workflow.request_merge(None)
        self.assertFalse(any(call.args[1] == 'push' for call in git_calls.call_args_list))
        self.assertIn('No unpublished completed sessions', self.output.getvalue())

    def test_old_registry_detects_already_published_remote_snapshot(self):
        done = self.complete()
        command(self.repo, 'git', 'push', 'origin', done['branch'])
        self.assertNotIn('publication_status', done)
        with patch.object(session, 'git', wraps=session.git) as git_calls:
            self.workflow.request_merge(done['id'])
        self.assertFalse(any(call.args[1] == 'push' for call in git_calls.call_args_list))
        self.assertEqual(done['publication_status'], 'published')
        self.assertIn('already published; nothing was pushed', self.output.getvalue())

    def test_integrated_sessions_stay_hidden_after_remote_branch_cleanup(self):
        done = self.submit()
        with patch('builtins.input', return_value='y'):
            self.workflow.integrate(1)
        command(self.repo, 'git', 'push', 'origin', '--delete', done['branch'])
        with patch.object(session, 'git', wraps=session.git) as git_calls:
            self.workflow.request_merge(None)
            self.workflow.request_merge(done['id'])
        self.assertFalse(any(call.args[1] == 'push' for call in git_calls.call_args_list))
        self.assertEqual(done['publication_status'], 'integrated')
        self.assertIn('already integrated; nothing was pushed', self.output.getvalue())

    def test_deleted_published_branch_is_not_resurrected(self):
        done = self.submit()
        command(self.repo, 'git', 'push', 'origin', '--delete', done['branch'])
        self.workflow.request_merge(None)
        self.assertEqual(done['publication_status'], 'published')
        self.assertEqual(command(self.repo, 'git', 'ls-remote', '--heads', 'origin', 'refs/heads/' + done['branch']), '')

    def test_publication_check_network_failure_does_not_push_or_mark_published(self):
        done = self.complete()
        with patch.object(session, 'fetch_master', side_effect=merger.MergeError('Network unavailable')):
            with self.assertRaisesRegex(merger.MergeError, 'Network unavailable'):
                self.workflow.request_merge(done['id'])
        self.assertNotIn('publication_status', done)
        self.assertEqual(command(self.repo, 'git', 'ls-remote', '--heads', 'origin', 'refs/heads/' + done['branch']), '')

    def test_branch_only_integration_without_gh_and_repeat(self):
        done = self.complete()
        with patch.object(session.shutil, 'which', return_value=None), patch.object(self.workflow, 'gh', side_effect=AssertionError('No GitHub CLI calls allowed')):
            self.workflow.request_merge(done['id'])
            with patch('builtins.input', return_value='y'):
                self.workflow.integrate(branch=done['branch'])
            head = command(self.remote, 'git', 'rev-parse', 'master')
            self.workflow.integrate(branch=done['branch'])
            self.assertEqual(command(self.remote, 'git', 'rev-parse', 'master'), head)
            with self.assertRaisesRegex(merger.MergeError, 'gh is required'):
                self.workflow.integrate(1)
        rows = merger.read_project(self.repo / session.PROJECT)['data']['code_text']
        self.assertEqual({r['owner'] for r in rows}, {'Baseline', 'Alice'})
        audit = json.loads((self.repo / f'coding/merges/{done["id"]}.json').read_text())
        self.assertIsNone(audit['pr'])

    def test_branch_integration_can_close_notification_later(self):
        done = self.submit()
        with patch.object(session.shutil, 'which', return_value=None), patch('builtins.input', return_value='y'):
            self.workflow.integrate(branch=done['branch'])
        self.assertEqual(self.github.prs[1]['state'], 'OPEN')
        before = command(self.remote, 'git', 'rev-parse', 'master')
        self.workflow.integrate(1)
        self.assertEqual(command(self.remote, 'git', 'rev-parse', 'master'), before)
        self.assertEqual(self.github.prs[1]['state'], 'CLOSED')

    def test_branch_integration_comments_once_without_closing(self):
        done = self.submit()
        with patch('builtins.input', return_value='y'):
            self.workflow.integrate(branch=done['branch'])
        before = command(self.remote, 'git', 'rev-parse', 'master')
        self.assertEqual(self.github.prs[1]['state'], 'OPEN')
        self.assertEqual(len(self.github.prs[1]['comments']), 1)
        self.assertIn(before, self.github.prs[1]['comments'][0]['body'])
        self.workflow.integrate(branch=done['branch'])
        self.assertEqual(len(self.github.prs[1]['comments']), 1)
        self.assertEqual(command(self.remote, 'git', 'rev-parse', 'master'), before)

    def test_branch_comment_failure_can_be_retried_without_reintegration(self):
        done = self.submit()
        gh = self.workflow.gh
        def outage(*args):
            if args[1] == 'comment':
                raise merger.MergeError('Simulated comment outage')
            return gh(*args)
        with patch.object(self.workflow, 'gh', side_effect=outage), patch('builtins.input', return_value='y'):
            self.workflow.integrate(branch=done['branch'])
        before = command(self.remote, 'git', 'rev-parse', 'master')
        self.assertIn('comment could not be posted', self.output.getvalue())
        self.assertEqual(self.github.prs[1]['comments'], [])
        self.workflow.integrate(branch=done['branch'])
        self.assertEqual(command(self.remote, 'git', 'rev-parse', 'master'), before)
        self.assertEqual(len(self.github.prs[1]['comments']), 1)

    def test_branch_notification_ignores_mismatched_snapshot(self):
        done = self.submit()
        self.github.prs[1]['headRefOid'] = 'a' * 40
        with patch('builtins.input', return_value='y'):
            self.workflow.integrate(branch=done['branch'])
        self.assertEqual(self.github.prs[1]['comments'], [])
        self.assertEqual(self.github.prs[1]['state'], 'OPEN')

    def test_two_coders_same_document_integration_and_repeat(self):
        self.submit('Alice')
        self.submit('Bob')
        with patch('builtins.input', return_value='y'):
            self.workflow.integrate(1)
            self.workflow.integrate(2)
        rows = merger.read_project(self.repo / session.PROJECT)['data']['code_text']
        self.assertEqual({r['owner'] for r in rows}, {'Alice', 'Bob', 'Baseline'})
        self.assertEqual(len({r['ctid'] for r in rows}), 3)
        commit = command(self.repo, 'git', 'rev-parse', 'HEAD')
        self.workflow.integrate(2)
        self.assertEqual(command(self.repo, 'git', 'rev-parse', 'HEAD'), commit)
        self.assertEqual(len(self.github.prs[2]['comments']), 1)
        self.assertEqual(self.github.prs[1]['state'], 'CLOSED')

    def test_different_cases_and_failed_pr_closure_retry(self):
        self.submit('Alice', fid=1)
        self.submit('Bob', fid=2)
        self.github.fail_close = True
        with patch('builtins.input', return_value='y'):
            with self.assertRaisesRegex(merger.MergeError, 'closure outage'):
                self.workflow.integrate(1)
        published = command(self.remote, 'git', 'rev-parse', 'master')
        self.workflow.integrate(1)
        self.assertEqual(command(self.remote, 'git', 'rev-parse', 'master'), published)
        with patch('builtins.input', return_value='y'):
            self.workflow.integrate(2)
        rows = merger.read_project(self.repo / session.PROJECT)['data']['code_text']
        self.assertEqual({(r['owner'], r['fid']) for r in rows}, {('Baseline', 1), ('Alice', 1), ('Bob', 2)})

    def advance_remote(self):
        clone = self.root / ('other-' + os.urandom(4).hex())
        command(self.root, 'git', 'clone', str(self.remote), str(clone))
        command(clone, 'git', 'config', 'user.name', 'Other Maintainer')
        command(clone, 'git', 'config', 'user.email', 'other@example.invalid')
        command(clone, 'git', 'config', 'commit.gpgsign', 'false')
        (clone / 'README.md').write_text('Remote advanced')
        command(clone, 'git', 'add', 'README.md')
        command(clone, 'git', 'commit', '-m', 'Concurrent maintenance')
        command(clone, 'git', 'push', 'origin', 'master')

    def test_remote_advancement_requires_new_preview(self):
        self.submit()
        def approve_after_advancement(_):
            self.advance_remote()
            return 'y'
        with patch('builtins.input', side_effect=approve_after_advancement):
            with self.assertRaisesRegex(merger.MergeError, 'advanced'):
                self.workflow.integrate(1)
        self.assertEqual(self.github.prs[1]['state'], 'OPEN')
        with patch('builtins.input', return_value='y'):
            self.workflow.integrate(1)
        self.assertTrue((self.repo / 'README.md').exists())

    def test_integration_cancel_leaves_master_unchanged(self):
        self.submit()
        master = command(self.remote, 'git', 'rev-parse', 'master')
        with patch('builtins.input', return_value='n'):
            self.workflow.integrate(1)
        self.assertEqual(command(self.remote, 'git', 'rev-parse', 'master'), master)
        self.assertEqual(self.github.prs[1]['state'], 'OPEN')

    def test_rejected_push_preserves_remote_and_can_be_retried(self):
        self.submit()
        original = session.git
        rejected = False
        def race(repo, *args, **kwargs):
            nonlocal rejected
            if args[:2] == ('push', 'origin') and any(str(a).endswith(':refs/heads/master') for a in args) and not rejected:
                rejected = True
                self.advance_remote()
            return original(repo, *args, **kwargs)
        with patch.object(session, 'git', side_effect=race), patch('builtins.input', return_value='y'):
            with self.assertRaisesRegex(merger.MergeError, 'push failed'):
                self.workflow.integrate(1)
        self.assertTrue(rejected)
        self.assertEqual(self.github.prs[1]['state'], 'OPEN')
        self.assertIn('Concurrent maintenance', command(self.remote, 'git', 'log', '-1', '--format=%s', 'master'))
        with patch('builtins.input', return_value='y'):
            self.workflow.integrate(1)
        self.assertTrue((self.repo / 'README.md').exists())

    def test_start_network_failure_leaves_checkout_untouched(self):
        before = command(self.repo, 'git', 'rev-parse', 'HEAD')
        with patch.object(session, 'fetch_master', side_effect=merger.MergeError('Network unavailable')):
            with self.assertRaisesRegex(merger.MergeError, 'Network unavailable'):
                self.start()
        self.assertEqual(self.workflow.branch(), 'master')
        self.assertIsNone(self.workflow.state.get('active'))
        self.assertEqual(command(self.repo, 'git', 'rev-parse', 'HEAD'), before)
        self.assertFalse(session.dirty_paths(self.repo))

    def test_bash_entrypoint_and_changed_pr_head(self):
        result = subprocess.run(['bash', str(ROOT / 'scripts/coding-session.sh'), '--repo', str(self.repo), 'status'], text=True, capture_output=True)
        self.assertEqual(result.returncode, 0, result.stdout + result.stderr)
        self.assertIsNone(json.loads(result.stdout)['active'])
        self.submit()
        self.github.prs[1]['headRefOid'] = 'a' * 40
        with self.assertRaisesRegex(merger.MergeError, 'snapshot changed'):
            self.workflow.integrate(1)

    def test_modified_candidate_requires_new_review(self):
        self.submit()
        original = command(self.remote, 'git', 'rev-parse', 'master')
        def edit_candidate(_):
            candidate = next(self.workflow.local.glob('integration-*/candidate.qda'))
            sql(candidate, "UPDATE project SET memo='Changed during review'")
            return 'y'
        with patch('builtins.input', side_effect=edit_candidate):
            with self.assertRaisesRegex(merger.MergeError, 'Candidate changed'):
                self.workflow.integrate(1)
        self.assertEqual(command(self.remote, 'git', 'rev-parse', 'master'), original)
        self.assertEqual(self.github.prs[1]['state'], 'OPEN')


if __name__ == '__main__':
    unittest.main()
