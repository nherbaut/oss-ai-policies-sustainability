"""Repository operations for shared theory and inductive codebook proposals."""
from copy import deepcopy
import hashlib
import json
import os
from pathlib import Path
import re
import shutil
import tempfile
import uuid

import codebook as cb
from merge_qualcoder import MergeError, ensure_closed, fixed_structure, read_project
from coding_guards import protect_database, writable_database


def api():
    # Loaded lazily so the command-line entrypoint has no import cycle.
    import coding_session
    return coding_session


def load_resolutions(path):
    return json.loads(Path(path).read_text()) if path else None


def replace_database(source, destination):
    """Publish a closed, verified SQLite file with a same-filesystem rename."""
    destination = Path(destination)
    fd, name = tempfile.mkstemp(prefix='.qualcoder-sync-', dir=destination.parent)
    os.close(fd)
    staging = Path(name)
    try:
        shutil.copy2(source, staging)
        os.replace(staging, destination)
    finally:
        staging.unlink(missing_ok=True)


def context_at(repo, session, head):
    cs = api()
    context = session['codebook_context']
    cs.ancestor(repo, session['base'], context['shared_commit'])
    cs.ancestor(repo, context['shared_commit'], 'refs/remotes/origin/master')
    shared = cs.tracked_json(repo, context['shared_commit'], cb.REGISTRY)
    if shared != context['shared'] or cs.tracked_json(repo, head, cb.REGISTRY) != shared:
        raise MergeError('Submitted shared codebook is not the recorded master revision')
    cb.validate_book(shared)
    return context


def validate_v2(repo, session, head, base, submitted):
    cs = api()
    if not session.get('completed_at'):
        raise MergeError('This synchronization checkpoint is not a completed session')
    context = context_at(repo, session, head)
    base_book = cs.tracked_json(repo, session['base'], cb.REGISTRY)
    incoming = read_project(submitted)
    local = cb.branch_book(incoming, context, session['id'], session['coder'])
    report = cb.delta(read_project(base), incoming, base_book, local, session['coder'], context.get('aliases'))
    if session.get('codebook_proposals') != cb.changes(context['shared'], local):
        raise MergeError('Submitted codebook proposals do not match the database')
    return report


class CodebookWorkflow:
    def codebook_init(self):
        cs = api()
        self.require_master()
        remote = cs.fetch_master(self.repo)
        if cs.git(self.repo, 'rev-parse', 'HEAD') != remote:
            raise MergeError('Update master to origin/master before initializing the codebook')
        if (self.repo / cb.REGISTRY).exists():
            raise MergeError('Codebook registry already initialized')
        # A deliberate clean boundary, including jobs created in other clones.
        refs = cs.git(self.repo, 'ls-remote', '--heads', 'origin', 'refs/heads/coding/*')
        if refs:
            raise MergeError('Integrate outstanding sessions and remove remote coding branches before initialization')
        for job in self.state.get('completed', []):
            if not cs.tracked_json(self.repo, remote, f'coding/merges/{job["id"]}.json', optional=True):
                raise MergeError('Integrate outstanding legacy sessions before initialization')
        snapshot = read_project(self.repo / cs.PROJECT)
        registry = cb.export(snapshot, origin=remote)
        cb.normalize(snapshot, registry, registry)
        cs.save_json(self.repo / cb.REGISTRY, registry)
        print(f'Created {cb.REGISTRY}; existing coding and database are unchanged. Commit and push this registry before starting sessions.')

    def codebook_start_context(self, session):
        cs = api()
        registry = cs.tracked_json(self.repo, session['base'], cb.REGISTRY, optional=True)
        if registry is None:
            return
        cb.validate_book(registry)
        actual = cb.export(read_project(self.repo / cs.PROJECT), registry)
        if actual != registry:
            raise MergeError('Master database and codebook registry disagree; register theory changes first')
        session.update(codebook_version=1, checkpoint=session['base'],
                       codebook_context=dict(shared=registry, shared_commit=session['base'], proposals={}, aliases={}, history=[]))

    def active_codebook(self):
        cs = api()
        session = self.state.get('active')
        if not session or not session.get('codebook_version'):
            raise MergeError('This command requires an active session started after codebook initialization')
        if self.branch() != session['branch']:
            raise MergeError(f'Resume the session branch first: {session["branch"]}')
        ensure_closed(self.repo / cs.PROJECT)
        self.recover_sync(session)
        if cs.git(self.repo, 'rev-parse', 'HEAD') != session.get('checkpoint', session['base']):
            raise MergeError('Unexpected commits on the session branch; use coding-sync, never Git merge/rebase')
        return session

    def recover_sync(self, session):
        cs = api()
        if session.get('phase') != 'syncing':
            return
        head = cs.git(self.repo, 'rev-parse', 'HEAD')
        if head == session.get('checkpoint', session['base']):
            backup = Path(session['sync_backup'])
            recovery = json.loads((backup / 'recovery.json').read_text())
            allowed = set(recovery['files'])
            if cs.dirty_paths(self.repo) - allowed:
                raise MergeError('Resolve unrelated work before recovering interrupted synchronization')
            for path, versions in recovery['files'].items():
                live = self.repo / path
                current = hashlib.sha256(live.read_bytes()).hexdigest() if live.exists() else None
                if current not in versions:
                    raise MergeError('Files changed since interrupted synchronization; inspect its backup before recovery')
                old = backup / path
                if old.exists() and hashlib.sha256(old.read_bytes()).hexdigest() != versions[0]:
                    raise MergeError('Synchronization backup changed; recovery stopped')
            writable_database(self.repo)
            for path, versions in recovery['files'].items():
                old, live = backup / path, self.repo / path
                if old.exists():
                    if path == cs.DATABASE:
                        replace_database(old, live)
                    else:
                        live.write_bytes(old.read_bytes())
                else:
                    live.unlink(missing_ok=True)
            cs.git(self.repo, 'reset', '--', *allowed)
            session.clear()
            session.update(recovery['session'])
            self.save()
            protect_database(self.repo)
            print('Restored the pre-synchronization database and metadata from the verified backup.')
            return
        manifest = cs.tracked_json(self.repo, head, f'coding/sessions/{session["id"]}.json')
        if (manifest.get('id') != session['id'] or manifest.get('checkpoint') != session.get('checkpoint', session['base'])
                or manifest.get('phase') != 'active' or manifest.get('completed_at')):
            raise MergeError('Invalid synchronization recovery checkpoint')
        cs.ancestor(self.repo, session['checkpoint'], head)
        if cs.git(self.repo, 'rev-list', '--count', session['checkpoint'] + '..' + head) != '1':
            raise MergeError('Unexpected synchronization history')
        cs.clean(self.repo)
        context_at(self.repo, manifest, head)
        session.clear()
        session.update(manifest, checkpoint=head, phase='active')
        self.save()
        protect_database(self.repo)
        print(f'Recovered synchronization checkpoint {head}.')

    def completion_report(self, session, temp):
        cs = api()
        master = cs.fetch_master(self.repo)
        shared = cs.tracked_json(self.repo, master, cb.REGISTRY)
        if shared['revision'] != session['codebook_context']['shared']['revision']:
            raise MergeError('The shared codebook changed. Close QualCoder and run make coding-sync before completing this session')
        base = cs.extract_project(self.repo, session['base'], temp)
        base_book = cs.tracked_json(self.repo, session['base'], cb.REGISTRY)
        incoming = read_project(self.repo / cs.PROJECT)
        context = session['codebook_context']
        local = cb.branch_book(incoming, context, session['id'], session['coder'])
        report = cb.delta(read_project(base), incoming, base_book, local, session['coder'], context.get('aliases'))
        report['codebook_proposals'] = cb.changes(context['shared'], local)
        return report, local

    def finish_codebook(self):
        cs = api()
        session = self.state['active']
        head = cs.git(self.repo, 'rev-parse', 'HEAD')
        manifest_path = f'coding/sessions/{session["id"]}.json'
        if session['phase'] == 'committing' and head != session['checkpoint']:
            manifest = cs.tracked_json(self.repo, head, manifest_path)
            with tempfile.TemporaryDirectory(dir=self.local) as temp:
                cs.validate_submission(self.repo, manifest, head, Path(temp))
            cs.clean(self.repo)
        else:
            session = self.active_codebook()
            allowed = {cs.DATABASE, manifest_path}
            if cs.dirty_paths(self.repo) - allowed:
                raise MergeError('Resolve unrelated files before completing the session')
            with tempfile.TemporaryDirectory(dir=self.local) as temp:
                report, local = self.completion_report(session, Path(temp))
            print(json.dumps(report, indent=2, ensure_ascii=False))
            if not cs.confirm('Commit and complete this coding session?'):
                return
            ensure_closed(self.repo / cs.PROJECT)
            with tempfile.TemporaryDirectory(dir=self.local) as temp:
                fresh, fresh_book = self.completion_report(session, Path(temp))
            if fresh != report or fresh_book != local or cs.dirty_paths(self.repo) - allowed:
                raise MergeError('Work changed after preview; review completion again')
            manifest = {k: deepcopy(v) for k, v in session.items() if k not in ('phase', 'sync_backup')}
            manifest.update(completed_at=cs.now(), summary=report['summary'], changed_documents=cs.changed_documents(report),
                            codebook_proposals=report['codebook_proposals'])
            manifest['codebook_context']['proposals'] = {k: v for k, v in local['entities'].items()
                                                       if k not in manifest['codebook_context']['shared']['entities']}
            cs.save_json(self.repo / manifest_path, manifest)
            session['phase'] = 'committing'
            self.save()
            cs.git(self.repo, 'add', '--', cs.DATABASE, manifest_path)
            cs.git(self.repo, 'commit', '-m', cs.coding_commit_message(f'Coding session: {session["coder"]} ({session["id"][:8]})', report),
                   '--', cs.DATABASE, manifest_path, commit_kind='session')
            head = cs.git(self.repo, 'rev-parse', 'HEAD')
            with tempfile.TemporaryDirectory(dir=self.local) as temp:
                cs.validate_submission(self.repo, manifest, head, Path(temp))
        completed = dict(manifest, head=head)
        self.state['completed'] = [s for s in self.state['completed'] if s['id'] != completed['id']] + [completed]
        self.state['active'] = None
        self.save()
        cs.git(self.repo, 'switch', 'master')
        protect_database(self.repo)
        print(f'Completed {completed["id"]}; snapshot {head}. Returned to master.')

    def sync(self, resolutions=None):
        cs = api()
        session = self.active_codebook()
        manifest_path = f'coding/sessions/{session["id"]}.json'
        allowed = {cs.DATABASE, manifest_path}
        if cs.dirty_paths(self.repo) - allowed:
            raise MergeError('Resolve unrelated files before synchronization (put resolution JSON outside the repository)')
        master = cs.fetch_master(self.repo)
        cs.ancestor(self.repo, session['base'], master)
        context = session['codebook_context']
        shared = cs.tracked_json(self.repo, master, cb.REGISTRY)
        if shared == context['shared']:
            print('Shared codebook is already current. No synchronization commit is needed.')
            return
        workspace = Path(tempfile.mkdtemp(prefix='sync-', dir=self.local))
        incoming = read_project(self.repo / cs.PROJECT)
        original_hash = hashlib.sha256((self.repo / cs.DATABASE).read_bytes()).hexdigest()
        base = cs.extract_project(self.repo, session['base'], workspace / 'base')
        base_book = cs.tracked_json(self.repo, session['base'], cb.REGISTRY)
        local = cb.branch_book(incoming, context, session['id'], session['coder'])
        cb.delta(read_project(base), incoming, base_book, local, session['coder'], context.get('aliases'))
        try:
            merged, aliases = cb.merge(context['shared'], shared, local, load_resolutions(resolutions))
        except cb.CodebookConflict as error:
            cs.save_json(workspace / 'conflicts.json', error.report)
            print(f'Conflict report: {workspace / "conflicts.json"}')
            raise
        expected = cb.normalize(incoming, local, merged, aliases)
        theory_changes = cb.changes(context['shared'], shared)
        report = dict(shared_revision=shared['revision'], theory_changes=theory_changes,
                      affected_passages=cb.affected(expected, merged, theory_changes, session['coder']),
                      proposals=cb.changes(shared, merged), aliases=aliases)
        cs.save_json(workspace / 'report.json', report)
        candidate = workspace / 'candidate.qda'
        cb.write_snapshot(self.repo / cs.PROJECT, expected, candidate)
        print(json.dumps(report, indent=2, ensure_ascii=False))
        print(f'Report and candidate: {workspace}')
        if not cs.confirm('Apply shared theory, preserve coding, and commit this synchronization?'):
            return
        ensure_closed(self.repo / cs.PROJECT)
        if (cs.fetch_master(self.repo) != master or cs.git(self.repo, 'rev-parse', 'HEAD') != session['checkpoint']
                or hashlib.sha256((self.repo / cs.DATABASE).read_bytes()).hexdigest() != original_hash
                or cs.dirty_paths(self.repo) - allowed):
            raise MergeError('Inputs changed after preview; synchronize again')
        ensure_closed(candidate)
        candidate_expected = read_project(candidate)
        if candidate_expected != expected:
            raise MergeError('Candidate changed during review')
        backup = workspace / 'backup'
        backup.mkdir()
        paths = [cs.DATABASE, cb.REGISTRY, manifest_path]
        originals = {p: (self.repo / p).read_bytes() if (self.repo / p).exists() else None for p in paths}
        for p, data in originals.items():
            if data is not None:
                target = backup / p
                target.parent.mkdir(parents=True, exist_ok=True)
                target.write_bytes(data)
        old_session = deepcopy(session)
        new_context = dict(shared=shared, shared_commit=master,
                           proposals={k: v for k, v in merged['entities'].items() if k not in shared['entities']},
                           aliases={**context.get('aliases', {}), **aliases},
                           history=context.get('history', []) + [dict(at=cs.now(), master=master, report=report)])
        progress = dict(session, phase='active', codebook_context=new_context)
        planned = {cs.DATABASE: (candidate / 'data.qda').read_bytes(),
                   cb.REGISTRY: (json.dumps(shared, indent=2, ensure_ascii=False) + '\n').encode(),
                   manifest_path: (json.dumps(progress, indent=2, ensure_ascii=False) + '\n').encode()}
        cs.save_json(backup / 'recovery.json', dict(session=old_session, files={
            p: [hashlib.sha256(data).hexdigest() if data is not None else None,
                hashlib.sha256(planned[p]).hexdigest()] for p, data in originals.items()}))
        session.update(phase='syncing', sync_backup=str(backup))
        self.save()
        committed = False
        try:
            writable_database(self.repo)
            replace_database(candidate / 'data.qda', self.repo / cs.DATABASE)
            cs.save_json(self.repo / cb.REGISTRY, shared)
            cs.save_json(self.repo / manifest_path, progress)
            cs.git(self.repo, 'add', '--', *paths)
            cs.git(self.repo, 'commit', '-m', f'Synchronize shared codebook {shared["revision"][:12]}', '--', *paths, commit_kind='sync')
            committed = True
            checkpoint = cs.git(self.repo, 'rev-parse', 'HEAD')
            session.clear()
            session.update(progress, checkpoint=checkpoint)
            self.save()
            protect_database(self.repo)
            print(f'Synchronized theory; original baseline retained. Checkpoint: {checkpoint}')
        except BaseException:
            # A commit can succeed just before an exception or interruption.
            # Leave its checkpoint recoverable rather than reverting its files.
            committed = committed or cs.git(self.repo, 'rev-parse', 'HEAD') != old_session['checkpoint']
            if not committed:
                writable_database(self.repo)
                for p, data in originals.items():
                    if data is None:
                        (self.repo / p).unlink(missing_ok=True)
                    else:
                        if p == cs.DATABASE:
                            replace_database(backup / p, self.repo / p)
                        else:
                            (self.repo / p).write_bytes(data)
                cs.git(self.repo, 'reset', '--', *paths)
                session.clear()
                session.update(old_session)
                self.save()
                protect_database(self.repo)
            raise

    def codebook_register(self):
        cs = api()
        if self.state.get('active') or not self.branch().startswith('maintenance/'):
            raise MergeError('Register theory on a manual maintenance/... branch without an active coding session')
        ensure_closed(self.repo / cs.PROJECT)
        master = cs.fetch_master(self.repo)
        base_commit = cs.git(self.repo, 'merge-base', 'HEAD', master)
        base_registry = cs.tracked_json(self.repo, base_commit, cb.REGISTRY)
        paths = cs.git(self.repo, 'ls-files', 'coding/theory').splitlines()
        manifests = [cs.tracked_json(self.repo, 'HEAD', p) for p in paths]
        matches = [m for m in manifests if m.get('branch') == self.branch()]
        # Also retain the UUID origin across repeated registrations before commit.
        for p in (self.repo / 'coding/theory').glob('*.json') if (self.repo / 'coding/theory').exists() else []:
            m = json.loads(p.read_text())
            if m.get('branch') == self.branch() and not any(x['id'] == m['id'] for x in matches):
                matches.append(m)
        if len(matches) > 1:
            raise MergeError('Multiple theory revisions for this maintenance branch')
        identity = matches[0]['id'] if matches else uuid.uuid4().hex
        if matches and matches[0]['base'] != base_commit:
            raise MergeError('Maintenance branch base changed; create a new maintenance branch')
        reference = json.loads((self.repo / cb.REGISTRY).read_text())
        cb.validate_book(reference)
        incoming = read_project(self.repo / cs.PROJECT)
        if not base_registry['entities'].keys() <= reference['entities'].keys():
            raise MergeError('Original shared identities cannot be removed from the registry')
        registry = cb.export(incoming, reference, identity)
        cb.no_deletions(base_registry, registry)
        manifest_path = f'coding/theory/{identity}.json'
        allowed = {cs.DATABASE, cb.REGISTRY, manifest_path}
        committed_changes = set(cs.git(self.repo, 'diff', '--name-only', base_commit, 'HEAD').splitlines())
        if (cs.dirty_paths(self.repo) | committed_changes) - allowed:
            raise MergeError('Theory branches may contain only their database, codebook registry, and theory manifest')
        with tempfile.TemporaryDirectory(dir=self.local) as temp:
            base = read_project(cs.extract_project(self.repo, base_commit, Path(temp)))
            b, s = cb.aligned([base, incoming], [base_registry, registry], registry)
            fixed_structure(b, s)
            for table in ('code_text', 'annotation'):
                if b['data'][table] != s['data'][table]:
                    raise MergeError('Theory registration cannot modify coding or annotations')
        cs.save_json(self.repo / cb.REGISTRY, registry)
        cs.save_json(self.repo / manifest_path, dict(version=1, id=identity, branch=self.branch(), base=base_commit,
                                                   registered_at=cs.now(), revision=registry['revision'], changes=cb.changes(base_registry, registry)))
        print(f'Registered theory changes. Review, commit and push: {cs.DATABASE}, {cb.REGISTRY}, {manifest_path}')

    def theory_publish(self, branch, resolutions=None):
        cs = api()
        self.require_master()
        if not branch or not branch.startswith('maintenance/'):
            raise MergeError('Use BRANCH=maintenance/...')
        cs.git(self.repo, 'check-ref-format', 'refs/heads/' + branch)
        ref = 'refs/qualcoder/theory/' + hashlib.sha256(branch.encode()).hexdigest()
        cs.git(self.repo, 'fetch', 'origin', f'refs/heads/{branch}:{ref}')
        head = cs.git(self.repo, 'rev-parse', ref)
        master = cs.fetch_master(self.repo)
        cs.ancestor(self.repo, 'master', master)
        paths = cs.git(self.repo, 'ls-tree', '-r', '--name-only', head, '--', 'coding/theory').splitlines()
        matches = [(p, cs.tracked_json(self.repo, head, p)) for p in paths]
        matches = [(p, m) for p, m in matches if m.get('branch') == branch]
        if len(matches) != 1:
            raise MergeError('Expected one registered theory revision for this branch')
        manifest_path, manifest = matches[0]
        identity = manifest['id']
        if manifest.get('version') != 1 or not re.fullmatch(r'[a-f0-9]{40,64}', manifest.get('base', '')):
            raise MergeError('Invalid theory manifest')
        if manifest_path != f'coding/theory/{identity}.json' or len(identity) != 32 or any(c not in '0123456789abcdef' for c in identity):
            raise MergeError('Invalid theory manifest identity')
        audit_path = f'coding/theory-revisions/{identity}.json'
        prior = cs.tracked_json(self.repo, master, audit_path, optional=True)
        if prior:
            if prior['submission'] != head:
                raise MergeError('Theory revision already published from a different snapshot')
            print('Theory revision already published. No changes made.')
            return
        cs.ancestor(self.repo, manifest['base'], head)
        cs.ancestor(self.repo, manifest['base'], master)
        changed = set(cs.git(self.repo, 'diff', '--name-only', manifest['base'], head).splitlines())
        if not changed <= {cs.DATABASE, cb.REGISTRY, manifest_path} or manifest_path not in changed:
            raise MergeError('Unexpected files in theory submission')
        workspace = Path(tempfile.mkdtemp(prefix='theory-', dir=self.local))
        worktree = workspace / 'worktree'
        try:
            base = read_project(cs.extract_project(self.repo, manifest['base'], workspace / 'base'))
            incoming = read_project(cs.extract_project(self.repo, head, workspace / 'incoming'))
            base_registry = cs.tracked_json(self.repo, manifest['base'], cb.REGISTRY)
            submitted = cs.tracked_json(self.repo, head, cb.REGISTRY)
            cb.validate_book(submitted)
            if (cb.export(incoming, submitted) != submitted or manifest['revision'] != submitted['revision']
                    or manifest['changes'] != cb.changes(base_registry, submitted)):
                raise MergeError('Theory manifest or registry disagrees with database')
            b, s = cb.aligned([base, incoming], [base_registry, submitted], submitted)
            fixed_structure(b, s)
            if any(b['data'][t] != s['data'][t] for t in ('code_text', 'annotation')):
                raise MergeError('Theory submission changes coding or annotations')
            cs.git(self.repo, 'worktree', 'add', '-b', f'integration/theory-{identity[:8]}-{uuid.uuid4().hex[:8]}', worktree, master)
            destination = read_project(worktree / cs.PROJECT)
            shared = cs.tracked_json(self.repo, master, cb.REGISTRY)
            if cb.export(destination, shared) != shared:
                raise MergeError('Master database and registry disagree')
            merged, aliases = cb.merge(base_registry, shared, submitted, load_resolutions(resolutions))
            expected = cb.normalize(destination, shared, merged)
            report = dict(codebook_changes=cb.changes(shared, merged),
                          affected_passages=cb.affected(expected, merged, cb.changes(shared, merged)), aliases=aliases)
            cs.save_json(workspace / 'report.json', report)
            candidate = workspace / 'candidate.qda'
            cb.write_snapshot(worktree / cs.PROJECT, expected, candidate)
            print(json.dumps(report, indent=2, ensure_ascii=False))
            print(f'Report and candidate: {workspace}')
            if not cs.confirm('Commit and push this theory revision to origin/master?'):
                return
            cs.clean(self.repo)
            ensure_closed(self.repo / cs.PROJECT)
            ensure_closed(candidate)
            if (cs.fetch_master(self.repo) != master
                    or cs.git(self.repo, 'ls-remote', '--heads', 'origin', 'refs/heads/' + branch).split()[0] != head
                    or read_project(candidate) != expected):
                raise MergeError('Theory inputs changed after preview; publish again')
            writable_database(worktree)
            shutil.copy2(candidate / 'data.qda', worktree / cs.DATABASE)
            cs.save_json(worktree / cb.REGISTRY, merged)
            cs.save_json(worktree / audit_path, dict(version=1, id=identity, branch=branch, submission=head,
                                                   destination=master, published_at=cs.now(), report=report))
            paths = [cs.DATABASE, cb.REGISTRY, audit_path]
            cs.git(worktree, 'add', '--', *paths)
            cs.git(worktree, 'commit', '-m', f'Publish theory revision {identity}', '--', *paths, commit_kind='integration')
            commit = cs.git(worktree, 'rev-parse', 'HEAD')
            cs.git(worktree, 'push', 'origin', f'{commit}:refs/heads/master')
            cs.git(self.repo, 'merge', '--ff-only', commit)
            protect_database(self.repo)
            cs.git(self.repo, 'worktree', 'remove', worktree)
            print(f'Published theory revision as {commit}; existing assignments preserved.')
        except cb.CodebookConflict as error:
            cs.save_json(workspace / 'conflicts.json', error.report)
            print(f'Conflict report: {workspace / "conflicts.json"}')
            raise
        finally:
            if (worktree / cs.DATABASE).exists():
                protect_database(worktree)
            print(f'Theory report workspace: {workspace}')
