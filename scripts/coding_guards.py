"""Versioned local Git guards and QualCoder database permissions (standard library).

Installed copies live in Git's common directory so checking out an older branch
does not remove the hooks. They are accident prevention, not an access-control
boundary against the owner of the checkout.
"""
import argparse
from contextlib import contextmanager
import hmac
import json
import os
from pathlib import Path
import re
import stat
import subprocess
import sys
import uuid

DATABASE = 'data/coding.qda/data.qda'
TOKEN_ENV = 'QUALCODER_COMMIT_TOKEN'
HOOKS = ('pre-commit', 'pre-merge-commit', 'post-checkout', 'post-merge')


class GuardError(ValueError):
    pass


def git(repo, *args, check=True):
    result = subprocess.run(['git', *args], cwd=repo, text=True, capture_output=True)
    if check and result.returncode:
        raise GuardError(result.stderr.strip())
    return result.stdout.strip()


def git_path(repo, *args):
    value = Path(git(repo, 'rev-parse', *args))
    return (repo / value).resolve() if not value.is_absolute() else value.resolve()


def local_directory(repo):
    return git_path(repo, '--absolute-git-dir') / 'qualcoder'


def common_directory(repo):
    return git_path(repo, '--git-common-dir') / 'qualcoder'


def state(repo):
    path = local_directory(repo) / 'state.json'
    return json.loads(path.read_text()) if path.exists() else {}


def branch(repo):
    return git(repo, 'symbolic-ref', '--quiet', '--short', 'HEAD', check=False)


def ensure_closed(repo):
    result = subprocess.run(['lsof', '-t', str(repo / DATABASE)], capture_output=True, text=True)
    if result.returncode not in (0, 1) or result.stdout.strip():
        raise GuardError('Close QualCoder before changing database permissions, then run make coding-protect.')


def writable_database(repo):
    """Internal write enable for a validated session or integration workspace."""
    path = repo / DATABASE
    if path.is_symlink():
        raise GuardError('Refusing to change permissions on a database symlink')
    path.chmod(stat.S_IMODE(path.stat().st_mode) | stat.S_IWUSR)


def protect_database(repo):
    path = repo / DATABASE
    if not path.exists():
        return  # Worktrees/older branches without a project have nothing to protect.
    if path.is_symlink():
        raise GuardError('Refusing to change permissions on a database symlink')
    active = state(repo).get('active')
    current = branch(repo)
    writable = bool(active and current == active.get('branch') and current.startswith('coding/')
                    and (active.get('phase') in ('committing', 'syncing') or git(repo, 'rev-parse', 'HEAD') == active.get('checkpoint', active.get('base'))))
    previous = stat.S_IMODE(path.stat().st_mode)
    desired = previous & ~0o222
    if writable:
        desired |= stat.S_IWUSR
    if previous == desired:
        return
    try:
        ensure_closed(repo)
    except GuardError:
        if not writable:
            path.chmod(desired)  # Also prevent new writers, even if an old handle exists.
        raise
    path.chmod(desired)


def install(repo):
    """Enable repository-owned hooks without overwriting existing custom hooks."""
    source = repo / '.githooks'
    target = common_directory(repo) / 'hooks'
    configured = git(repo, 'config', '--get', 'core.hooksPath', check=False)
    if configured:
        configured_path = Path(configured)
        configured_path = (repo / configured_path).resolve() if not configured_path.is_absolute() else configured_path.resolve()
        if configured_path != target:
            raise GuardError(f'Existing core.hooksPath={configured!r}; integrate the QualCoder guards with your custom hooks first.')
    else:
        legacy = git_path(repo, '--git-common-dir') / 'hooks'
        custom = [str(legacy / name) for name in HOOKS if (legacy / name).exists() and os.access(legacy / name, os.X_OK)]
        if custom:
            raise GuardError('Existing custom hooks were preserved; integrate them before setup: ' + ', '.join(custom))
    for name in HOOKS:
        if not (source / name).is_file():
            raise GuardError('Guard files are missing; update this checkout before running make coding-setup.')
    helper = common_directory(repo) / 'coding_guards.py'
    payloads = {target / name: (source / name).read_bytes() for name in HOOKS}
    payloads[helper] = Path(__file__).read_bytes()
    needs_install = not configured or any(not p.exists() or p.read_bytes() != content or
                                         (p.parent == target and not os.access(p, os.X_OK))
                                         for p, content in payloads.items())
    if needs_install:
        ensure_closed(repo)
        target.mkdir(parents=True, exist_ok=True)
        for path, content in payloads.items():
            temporary = path.with_name(path.name + '.tmp')
            temporary.write_bytes(content)
            temporary.chmod(0o755 if path.parent == target else 0o644)
            os.replace(temporary, path)
        git(repo, 'config', '--local', 'core.hooksPath', str(target))
    protect_database(repo)


def require_installed(repo):
    """Read-only gate: never installs, repairs, or updates hooks implicitly."""
    message = 'Coding guards are missing, disabled, or outdated. Run make coding-setup before using make coding.'
    target = common_directory(repo) / 'hooks'
    configured = git(repo, 'config', '--get', 'core.hooksPath', check=False)
    if not configured:
        raise GuardError(message)
    configured_path = Path(configured)
    configured_path = (repo / configured_path).resolve() if not configured_path.is_absolute() else configured_path.resolve()
    if configured_path != target:
        raise GuardError(message)
    try:
        for name in HOOKS:
            source, installed = repo / '.githooks' / name, target / name
            if (not installed.is_file() or installed.is_symlink() or not os.access(installed, os.X_OK)
                    or source.read_bytes() != installed.read_bytes()):
                raise GuardError(message)
        helper = common_directory(repo) / 'coding_guards.py'
        if not helper.is_file() or helper.is_symlink() or helper.read_bytes() != Path(__file__).read_bytes():
            raise GuardError(message)
    except OSError as error:
        raise GuardError(message) from error


@contextmanager
def authorize_commit(repo, kind):
    """Authorize only this exact staged tree and branch for one subprocess."""
    if kind not in ('session', 'integration', 'sync'):
        raise GuardError('Unknown commit authorization')
    directory = local_directory(repo) / 'commit-permits'
    directory.mkdir(parents=True, exist_ok=True)
    token = uuid.uuid4().hex
    path = directory / (token + '.json')
    value = dict(token=token, kind=kind, branch=branch(repo), tree=git(repo, 'write-tree'))
    # Exclusive creation prevents accidentally replacing another command's permit.
    with path.open('x') as output:
        json.dump(value, output)
    path.chmod(0o600)
    try:
        yield dict(os.environ, **{TOKEN_ENV: token})
    finally:
        path.unlink(missing_ok=True)


def commit_permit(repo):
    token = os.environ.get(TOKEN_ENV, '')
    if not re.fullmatch(r'[a-f0-9]{32}', token):
        return None
    path = local_directory(repo) / 'commit-permits' / (token + '.json')
    if not path.exists():
        return None
    permit = json.loads(path.read_text())
    if (not hmac.compare_digest(token, permit.get('token', ''))
            or permit.get('branch') != branch(repo) or permit.get('tree') != git(repo, 'write-tree')):
        raise GuardError('Commit authorization does not match this branch and staged content')
    return permit.get('kind')


def check_commit(repo):
    protect_database(repo)
    current = branch(repo)
    paths = set(p for p in git(repo, 'diff', '--cached', '--name-only', '--no-renames', '-z').split('\0') if p)
    if current == 'master' and DATABASE in paths:
        raise GuardError('Database commits on master are blocked. Use make coding-start and make coding-finish; maintainers use make coding-integrate.')
    active = state(repo).get('active')
    if current.startswith('coding/') or (active and active.get('branch') == current):
        permit = commit_permit(repo)
        phase = active.get('phase') if active else None
        if (not active or active.get('branch') != current
                or (phase, permit) not in (('committing', 'session'), ('syncing', 'sync'))):
            raise GuardError('Manual commits on coding session branches are blocked. Use make coding-finish.')
        allowed = {DATABASE, f'coding/sessions/{active["id"]}.json'}
        if permit == 'sync':
            allowed.add('coding/codebook.json')
        if not paths <= allowed:
            raise GuardError('Session commits may contain only their database and session manifest')
    if current.startswith('integration/') and DATABASE in paths and commit_permit(repo) != 'integration':
        raise GuardError('Manual integration database commits are blocked. Use make coding-integrate.')


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--repo', type=Path, default=Path.cwd())
    parser.add_argument('command', choices=('setup', 'protect', 'commit'))
    args = parser.parse_args()
    try:
        repo = Path(git(args.repo, 'rev-parse', '--show-toplevel')).resolve()
        if args.command == 'setup':
            install(repo)
            print('Coding guards enabled. Database is writable only in a valid active session.')
        elif args.command == 'protect':
            protect_database(repo)
        else:
            check_commit(repo)
        return 0
    except (GuardError, OSError, ValueError, KeyError, TypeError) as error:
        print(f'QualCoder guard: {error}', file=sys.stderr)
        return 1


if __name__ == '__main__':
    raise SystemExit(main())
