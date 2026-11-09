"""Local orchestration for coding-session.sh; no shell evaluation of user input."""
import argparse
from contextlib import closing, contextmanager
from datetime import datetime, timezone
import fcntl
import hashlib
import io
import json
import os
from pathlib import Path
import re
import shutil
import sqlite3
import subprocess
import tarfile
import tempfile
import unicodedata
import uuid

from merge_qualcoder import MergeError, ensure_closed, plan_merge, read_project, write_candidate

PROJECT = 'data/coding.qda'
DATABASE = PROJECT + '/data.qda'
VERSION = 1


def now():
    return datetime.now(timezone.utc).isoformat()


def run(args, cwd, check=True, binary=False):
    result = subprocess.run(args, cwd=cwd, capture_output=True, text=not binary)
    if check and result.returncode:
        error = result.stderr.decode(errors='replace') if binary else result.stderr
        raise MergeError(f'{args[0]} {args[1]} failed: {error.strip()}')
    return result


def git(repo, *args, check=True):
    return run(['git', *map(str, args)], repo, check=check).stdout.strip()


def dirty_paths(repo):
    result = set()
    for args in [('diff', '--name-only', '--no-renames', '-z'),
                 ('diff', '--cached', '--name-only', '--no-renames', '-z'),
                 ('ls-files', '--others', '--exclude-standard', '-z')]:
        result.update(p for p in run(['git', *args], repo).stdout.split('\0') if p)
    return result


def clean(repo):
    paths = dirty_paths(repo)
    if paths:
        raise MergeError('Resolve unrelated/uncommitted work first:\n' + '\n'.join(sorted(paths)))


def confirm(message):
    return input(message + ' [y/N] ').strip().lower() in ('y', 'yes')


def save_json(path, value):
    path.parent.mkdir(parents=True, exist_ok=True)
    staging = path.with_name(path.name + '.tmp')
    staging.write_text(json.dumps(value, indent=2, ensure_ascii=False) + '\n')
    os.replace(staging, path)


def extract_project(repo, commit, target):
    archive = run(['git', 'archive', '--format=tar', commit, '--', PROJECT], repo, binary=True).stdout
    with tarfile.open(fileobj=io.BytesIO(archive)) as tar:
        for member in tar:
            relative = Path(member.name)
            if relative.is_absolute() or '..' in relative.parts:
                raise MergeError('Unsafe path in committed project')
            if not relative.is_relative_to(PROJECT):
                if member.isdir() and Path(PROJECT).is_relative_to(relative):
                    continue  # git archive includes the parent "data/" entry.
                raise MergeError('Unexpected path in committed project')
            path = target / relative
            if member.isdir():
                path.mkdir(parents=True, exist_ok=True)
            elif member.isfile():
                path.parent.mkdir(parents=True, exist_ok=True)
                path.write_bytes(tar.extractfile(member).read())
            else:
                raise MergeError('Project snapshots must contain only regular files and directories')
    return target / PROJECT


def tracked_json(repo, commit, path, optional=False):
    result = run(['git', 'show', f'{commit}:{path}'], repo, check=False)
    if result.returncode and optional:
        return None
    if result.returncode:
        raise MergeError(f'Missing committed metadata: {path}')
    return json.loads(result.stdout)


def ancestor(repo, older, newer):
    if run(['git', 'merge-base', '--is-ancestor', older, newer], repo, check=False).returncode:
        raise MergeError('The recorded base/local master is not an ancestor; do not rebase or Git-merge the database')


def fetch_master(repo):
    git(repo, 'fetch', 'origin', 'refs/heads/master:refs/remotes/origin/master')
    return git(repo, 'rev-parse', 'refs/remotes/origin/master')


def check_manifest(manifest):
    if (manifest.get('version') != VERSION or manifest.get('project') != PROJECT
            or not re.fullmatch(r'[a-f0-9]{32}', manifest.get('id', ''))
            or not re.fullmatch(r'[a-f0-9]{40,64}', manifest.get('base', ''))
            or not manifest.get('branch', '').startswith('coding/')
            or not manifest.get('coder', '').strip()
            or manifest['coder'].strip().lower() == 'default'):
        raise MergeError('Invalid coding-session manifest')


def validate_submission(repo, session, head, temporary):
    check_manifest(session)
    ancestor(repo, session['base'], head)
    path = f'coding/sessions/{session["id"]}.json'
    changed = set(p for p in run(['git', 'diff', '--name-only', '--no-renames', '-z', session['base'], head], repo).stdout.split('\0') if p)
    if not changed <= {DATABASE, path} or path not in changed:
        raise MergeError('Submission changes files outside its database and session manifest')
    stored = tracked_json(repo, head, path)
    if stored != session:
        raise MergeError('Session manifest does not match the submitted snapshot')
    base = extract_project(repo, session['base'], temporary / 'base')
    submitted = extract_project(repo, head, temporary / 'submission')
    report = plan_merge(read_project(base), read_project(base), read_project(submitted), session['coder'])
    if report['conflicts'] or report['summary'] != session['summary']:
        raise MergeError('Submission differs from its validated completion summary')
    return base, submitted, report


class Workflow:
    def __init__(self, repo):
        self.repo = Path(git(repo, 'rev-parse', '--show-toplevel')).resolve()
        self.local = Path(git(self.repo, 'rev-parse', '--absolute-git-dir')) / 'qualcoder'
        self.local.mkdir(exist_ok=True)
        self.state_path = self.local / 'state.json'
        self.state = json.loads(self.state_path.read_text()) if self.state_path.exists() else {'active': None, 'completed': []}

    def save(self):
        save_json(self.state_path, self.state)

    def branch(self):
        return git(self.repo, 'symbolic-ref', '--short', 'HEAD')

    def require_master(self):
        if self.state.get('active'):
            raise MergeError('A coding session is active; complete it first')
        if self.branch() != 'master':
            raise MergeError('Run this command from master')
        clean(self.repo)
        ensure_closed(self.repo / PROJECT)

    def start(self):
        self.require_master()
        remote = fetch_master(self.repo)
        ancestor(self.repo, 'master', remote)
        git(self.repo, 'merge', '--ff-only', remote)
        snapshot = read_project(self.repo / PROJECT)
        suggested = self.state.get('preferred_coder') or snapshot['data']['project'][0]['codername']
        if not suggested or suggested.lower() == 'default':
            suggested = ''
        coder = input(f'Coder name{f" [{suggested}]" if suggested else ""}: ').strip() or suggested
        if not coder or coder.lower() == 'default' or any(ord(c) < 32 for c in coder):
            raise MergeError('Enter a nonempty coder name other than default')
        slug = re.sub(r'[^a-z0-9]+', '-', unicodedata.normalize('NFKD', coder).encode('ascii', 'ignore').decode().lower()).strip('-') or 'coder'
        identity = uuid.uuid4().hex
        branch = f'coding/{slug[:40]}/{datetime.now(timezone.utc):%Y%m%d-%H%M%S}-{identity[:8]}'
        session = dict(version=VERSION, id=identity, coder=coder, branch=branch,
                       base=git(self.repo, 'rev-parse', 'HEAD'), project=PROJECT, started_at=now(), phase='active')
        # Persist recovery state before any project mutation.
        git(self.repo, 'switch', '-c', branch)
        self.state.update(active=session, preferred_coder=coder)
        self.save()
        with closing(sqlite3.connect(self.repo / DATABASE)) as conn, conn:
            conn.execute('UPDATE project SET codername=?', (coder,))
            conn.execute('INSERT OR IGNORE INTO coder_names(name,visibility) VALUES (?,1)', (coder,))
        print(f'Session: {identity}\nBranch: {branch}\nOpen: {self.repo / PROJECT}\nIn QualCoder Settings, verify the current coder is {coder!r}.')

    def finish(self):
        session = self.state.get('active')
        if not session:
            print('No coding session is active.')
            return
        if self.branch() != session['branch']:
            raise MergeError(f'Resume the session branch first: {session["branch"]}')
        ensure_closed(self.repo / PROJECT)
        manifest_path = f'coding/sessions/{session["id"]}.json'
        head = git(self.repo, 'rev-parse', 'HEAD')
        # A crash after commit but before the local state update is recoverable.
        if session['phase'] == 'committing' and head != session['base']:
            manifest = tracked_json(self.repo, head, manifest_path)
            with tempfile.TemporaryDirectory(dir=self.local) as temp:
                validate_submission(self.repo, manifest, head, Path(temp))
            clean(self.repo)
        else:
            if head != session['base']:
                raise MergeError('Unexpected commits on the session branch; do not amend or rebase sessions')
            unrelated = dirty_paths(self.repo) - {DATABASE, manifest_path}
            if unrelated:
                raise MergeError('Unrelated work will not be committed; resolve it first:\n' + '\n'.join(sorted(unrelated)))
            with tempfile.TemporaryDirectory(dir=self.local) as temp:
                base = extract_project(self.repo, session['base'], Path(temp))
                report = plan_merge(read_project(base), read_project(base), read_project(self.repo / PROJECT), session['coder'])
            print(json.dumps(report, indent=2, ensure_ascii=False))
            print('Files to commit:\n' + DATABASE + '\n' + manifest_path)
            if not confirm('Commit and complete this coding session?'):
                print('Session remains active; nothing was committed.')
                return
            # Validate again after the prompt, preventing stale approval.
            ensure_closed(self.repo / PROJECT)
            with tempfile.TemporaryDirectory(dir=self.local) as temp:
                base = extract_project(self.repo, session['base'], Path(temp))
                fresh = plan_merge(read_project(base), read_project(base), read_project(self.repo / PROJECT), session['coder'])
            if fresh != report or dirty_paths(self.repo) - {DATABASE, manifest_path}:
                raise MergeError('Work changed after preview; review completion again')
            manifest = {k: v for k, v in session.items() if k != 'phase'}
            manifest.update(completed_at=now(), summary=report['summary'])
            save_json(self.repo / manifest_path, manifest)
            session['phase'] = 'committing'
            self.save()
            git(self.repo, 'add', '--', DATABASE, manifest_path)
            git(self.repo, 'commit', '-m', f'Coding session: {session["coder"]} ({session["id"][:8]})', '--', DATABASE, manifest_path)
            head = git(self.repo, 'rev-parse', 'HEAD')
            with tempfile.TemporaryDirectory(dir=self.local) as temp:
                validate_submission(self.repo, manifest, head, Path(temp))
        completed = dict(manifest, head=head)
        self.state['completed'] = [s for s in self.state['completed'] if s['id'] != completed['id']] + [completed]
        # Record completion before switching. If switching fails, no work is lost.
        self.state['active'] = None
        self.save()
        git(self.repo, 'switch', 'master')
        print(f'Completed {completed["id"]}; snapshot {head}. Returned to master.')

    def select_completed(self, identity):
        sessions = self.state.get('completed', [])
        if identity:
            sessions = [s for s in sessions if s['id'] == identity]
        if not sessions:
            raise MergeError('No matching completed session')
        if len(sessions) > 1:
            for index, s in enumerate(sessions, 1):
                print(f'{index}. {s["coder"]}: {s["id"]} ({s["completed_at"]})')
            selection = input('Session number: ').strip()
            if not selection.isdigit() or not 1 <= int(selection) <= len(sessions):
                raise MergeError('Invalid session selection')
            return sessions[int(selection) - 1]
        return sessions[0]

    def gh(self, *args):
        return run(['gh', *map(str, args)], self.repo).stdout.strip()

    def request_merge(self, identity):
        completed = self.select_completed(identity)
        head = git(self.repo, 'rev-parse', completed['branch'])
        if head != completed['head']:
            raise MergeError('Completed session was amended; submit the original immutable snapshot')
        manifest = tracked_json(self.repo, head, f'coding/sessions/{completed["id"]}.json')
        with tempfile.TemporaryDirectory(dir=self.local) as temp:
            validate_submission(self.repo, manifest, head, Path(temp))
        # Refuse dirty submitted branches even if completion was previously valid.
        if self.branch() == completed['branch']:
            clean(self.repo)
        git(self.repo, 'push', '--set-upstream', 'origin', completed['branch'])
        print(f'Published coding branch: {completed["branch"]}\nSnapshot: {head}')
        print('GitHub Actions will create or update its draft notification PR when enabled. No local gh CLI is required.')
        print(f'Maintainer can also integrate directly:\nmake coding-integrate BRANCH={completed["branch"]}')

    def comment_notification(self, number, identity, head, commit):
        info = json.loads(self.gh('pr', 'view', number, '--json', 'state,headRefOid,comments'))
        if info['headRefOid'] != head:
            raise MergeError('Coding was integrated, but the PR head changed; notification was not modified')
        if info['state'] == 'CLOSED':
            return False
        marker = f'<!-- qualcoder-integrated:{identity}:{head} -->'
        if not any(marker in c['body'] for c in info.get('comments', [])):
            with tempfile.TemporaryDirectory(dir=self.local) as temp:
                body = Path(temp) / 'comment.md'
                body.write_text(f'Integrated programmatically in commit {commit}. Coder attribution was retained.\n\n{marker}\n')
                self.gh('pr', 'comment', number, '--body-file', body)
        return True

    def close_notification(self, number, identity, head, commit):
        if not self.comment_notification(number, identity, head, commit):
            print(f'Already integrated as {commit}; notification is closed.')
            return
        self.gh('pr', 'close', number)
        print(f'Integrated as {commit}; notification PR #{number} closed.')

    def notify_branch_integration(self, branch, identity, head, commit):
        if shutil.which('gh') is None:
            print('gh is unavailable; no PR comment was posted. Coding integration is complete.')
            return
        try:
            prs = json.loads(self.gh('pr', 'list', '--state', 'open', '--head', branch,
                                     '--base', 'master', '--json', 'number,headRefOid,body'))
            matched = False
            for pr in prs:
                marker = re.search(r'<!-- qualcoder-session-v1: (\{[^\n]*\}) -->', pr.get('body') or '')
                if not marker or pr.get('headRefOid') != head:
                    continue
                snapshot = json.loads(marker[1])
                if snapshot.get('id') != identity or snapshot.get('head') != head:
                    continue
                if self.comment_notification(pr['number'], identity, head, commit):
                    print(f'Integration recorded in PR #{pr["number"]}; the notification remains open.')
                    matched = True
            if not matched:
                print('No matching open notification PR was found. Coding integration is complete.')
        except (MergeError, OSError, ValueError, KeyError, TypeError) as error:
            print(f'Coding integration is complete, but the PR comment could not be posted: {error}')
            print(f'Retry make coding-integrate BRANCH={branch}; existing coding will not be duplicated.')

    def integrate(self, number=None, branch=None):
        self.require_master()
        if (number is None) == (branch is None):
            raise MergeError('Choose either a PR number or --branch coding/...')
        if branch is not None:
            if not branch.startswith('coding/'):
                raise MergeError('Expected a coding/... session branch')
            git(self.repo, 'check-ref-format', 'refs/heads/' + branch)
            ref = 'refs/qualcoder/branches/' + hashlib.sha256(branch.encode()).hexdigest()
            git(self.repo, 'fetch', 'origin', f'refs/heads/{branch}:{ref}')
            head = git(self.repo, 'rev-parse', ref)
            paths = run(['git', 'ls-tree', '-r', '--name-only', '-z', head, '--', 'coding/sessions'], self.repo).stdout.split('\0')
            manifests = [tracked_json(self.repo, head, p) for p in paths if re.fullmatch(r'coding/sessions/[a-f0-9]{32}\.json', p)]
            matches = [m for m in manifests if m.get('branch') == branch]
            if len(matches) != 1:
                raise MergeError('Expected exactly one completed session manifest for this branch')
            manifest = matches[0]
            check_manifest(manifest)
            master = fetch_master(self.repo)
            ancestor(self.repo, 'master', master)
            self.integrate_snapshot(None, branch, head, manifest, master)
            return
        if shutil.which('gh') is None:
            raise MergeError('gh is required for PR numbers; use make coding-integrate BRANCH=coding/... without gh')
        info = json.loads(self.gh('pr', 'view', number, '--json', 'state,isDraft,isCrossRepository,headRefName,headRefOid,baseRefName,body'))
        if info.get('isCrossRepository') or info['baseRefName'] != 'master' or not info['headRefName'].startswith('coding/'):
            raise MergeError('Expected a same-repository coding notification targeting master')
        marker = re.search(r'<!-- qualcoder-session-v1: (\{[^\n]*\}) -->', info['body'])
        if not marker:
            raise MergeError('PR has no coding-session snapshot marker')
        submission = json.loads(marker[1])
        identity, head = submission['id'], submission['head']
        if not re.fullmatch(r'[a-f0-9]{32}', identity) or not re.fullmatch(r'[a-f0-9]{40,64}', head) or head != info['headRefOid']:
            raise MergeError('PR snapshot changed after submission')
        master = fetch_master(self.repo)
        ancestor(self.repo, 'master', master)
        audit_path = f'coding/merges/{identity}.json'
        previous = tracked_json(self.repo, master, audit_path, optional=True)
        if previous:
            if previous['submission'] != head:
                raise MergeError('Session ID was already integrated from another snapshot')
            commit = git(self.repo, 'log', '-1', '--format=%H', master, '--', audit_path)
            self.close_notification(number, identity, head, commit)
            return
        if info['state'] != 'OPEN' or not info['isDraft']:
            raise MergeError('New integrations require an open draft notification PR')
        git(self.repo, 'check-ref-format', 'refs/heads/' + info['headRefName'])
        git(self.repo, 'fetch', 'origin', f'refs/heads/{info["headRefName"]}:refs/qualcoder/pr/{number}')
        if git(self.repo, 'rev-parse', f'refs/qualcoder/pr/{number}') != head:
            raise MergeError('PR head changed during fetch')
        manifest = tracked_json(self.repo, head, f'coding/sessions/{identity}.json')
        if manifest.get('id') != identity or manifest.get('branch') != info['headRefName']:
            raise MergeError('PR branch and manifest disagree')
        self.integrate_snapshot(number, info['headRefName'], head, manifest, master)

    def integrate_snapshot(self, number, branch, head, manifest, master):
        identity = manifest['id']
        audit_path = f'coding/merges/{identity}.json'
        previous = tracked_json(self.repo, master, audit_path, optional=True)
        if previous:
            if previous['submission'] != head:
                raise MergeError('Session ID was already integrated from another snapshot')
            commit = git(self.repo, 'log', '-1', '--format=%H', master, '--', audit_path)
            if number is not None:
                self.close_notification(number, identity, head, commit)
            else:
                print(f'Already integrated as {commit}. No coding was duplicated.')
                self.notify_branch_integration(branch, identity, head, commit)
            return
        ancestor(self.repo, manifest['base'], master)
        workspace = Path(tempfile.mkdtemp(prefix='integration-', dir=self.local))
        worktree = workspace / 'worktree'
        integration_branch = f'integration/{identity[:8]}-{uuid.uuid4().hex[:8]}'
        try:
            base, incoming, _ = validate_submission(self.repo, manifest, head, workspace / 'inputs')
            git(self.repo, 'worktree', 'add', '-b', integration_branch, worktree, master)
            destination = worktree / PROJECT
            report = plan_merge(read_project(base), read_project(destination), read_project(incoming), manifest['coder'])
            save_json(workspace / 'report.json', report)
            print(json.dumps(report, indent=2, ensure_ascii=False))
            if report['conflicts']:
                raise MergeError('Conflicts require review; master was not changed')
            candidate = workspace / 'candidate.qda'
            write_candidate(base, destination, incoming, manifest['coder'], candidate, report)
            candidate_hash = hashlib.sha256((candidate / 'data.qda').read_bytes()).hexdigest()
            print(f'Validated candidate: {candidate}\nReport: {workspace / "report.json"}')
            prompt = 'Commit and push this integration to origin/master'
            if number is not None:
                prompt += ', then close the notification PR'
            elif shutil.which('gh') is not None:
                prompt += ', then comment on its notification PR'
            if not confirm(prompt + '?'):
                print(f'Cancelled; candidate retained at {workspace}. Master is unchanged.')
                return
            clean(self.repo)
            ensure_closed(self.repo / PROJECT)
            ensure_closed(candidate)
            if hashlib.sha256((candidate / 'data.qda').read_bytes()).hexdigest() != candidate_hash:
                raise MergeError('Candidate changed during review; run integration again for a fresh preview')
            # Never accept a different head or destination under an old approval.
            if number is not None:
                current_pr = json.loads(self.gh('pr', 'view', number, '--json', 'headRefOid,state,isDraft'))
                if current_pr['state'] != 'OPEN' or not current_pr['isDraft']:
                    raise MergeError('Notification PR is no longer an open draft; integration stopped')
                current_head = current_pr['headRefOid']
            else:
                current_head = git(self.repo, 'ls-remote', '--exit-code', '--heads', 'origin', 'refs/heads/' + branch).split()[0]
            if fetch_master(self.repo) != master or current_head != head:
                raise MergeError('Remote master or submission advanced; run integration again for a fresh preview')
            shutil.copy2(candidate / 'data.qda', worktree / DATABASE)
            save_json(worktree / audit_path, dict(version=VERSION, id=identity, coder=manifest['coder'],
                                                base=manifest['base'], destination=master, submission=head,
                                                pr=number, branch=branch, integrated_at=now(), report=report))
            git(worktree, 'add', '--', DATABASE, audit_path)
            description = f'notification #{number}' if number is not None else f'branch {branch}'
            git(worktree, 'commit', '-m', f'Integrate coding session {identity} ({description})', '--', DATABASE, audit_path)
            commit = git(worktree, 'rev-parse', 'HEAD')
            git(worktree, 'push', 'origin', f'{commit}:refs/heads/master')
            # A failed push leaves the integration branch/worktree recoverable.
            # Updating the user's clean local master is optional after publication.
            if self.branch() == 'master' and not dirty_paths(self.repo):
                ensure_closed(self.repo / PROJECT)
                git(self.repo, 'merge', '--ff-only', commit)
            if number is not None:
                self.close_notification(number, identity, head, commit)
            else:
                print(f'Integrated branch {branch} as {commit}.')
                self.notify_branch_integration(branch, identity, head, commit)
            git(self.repo, 'worktree', 'remove', worktree)
        except BaseException:
            print(f'Integration workspace retained for recovery: {workspace}')
            raise

    def status(self):
        print(json.dumps(self.state, indent=2, ensure_ascii=False))


@contextmanager
def local_lock(path):
    with path.open('a') as lock:
        try:
            fcntl.flock(lock, fcntl.LOCK_EX | fcntl.LOCK_NB)
        except BlockingIOError:
            raise MergeError('Another session command is already running in this checkout')
        yield


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--repo', type=Path, default=Path.cwd())
    sub = parser.add_subparsers(dest='command', required=True)
    for name in ('start', 'finish', 'status'):
        sub.add_parser(name)
    sub.add_parser('request-merge').add_argument('--session')
    integration = sub.add_parser('integrate')
    integration.add_argument('pr', nargs='?', type=int)
    integration.add_argument('--branch')
    args = parser.parse_args()
    try:
        workflow = Workflow(args.repo)
        with local_lock(workflow.local / 'command.lock'):
            # Reload state after obtaining the lock.
            if workflow.state_path.exists():
                workflow.state = json.loads(workflow.state_path.read_text())
            if args.command == 'request-merge':
                workflow.request_merge(args.session)
            elif args.command == 'integrate':
                if args.pr is not None and args.pr < 1:
                    raise MergeError('PR number must be positive')
                workflow.integrate(args.pr, branch=args.branch)
            else:
                getattr(workflow, args.command)()
        return 0
    except (MergeError, OSError, sqlite3.Error, ValueError, KeyError, TypeError, EOFError, KeyboardInterrupt) as error:
        print(f'Stopped: {error}')
        return 2


if __name__ == '__main__':
    raise SystemExit(main())
