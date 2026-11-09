# Coding together with QualCoder

Use a local session branch for each coding job. A GitHub Action creates or updates
a draft pull request when the completed branch is pushed. The maintainer runs
the merger below. **Do not use GitHub Merge,
rebase session branches, or resolve the SQLite database using ours/theirs.**

Requirements: Bash, Python 3.10+, Git, and `lsof`. The GitHub CLI (`gh`) is optional:
only maintainers using PR numbers need it; publishing and direct branch integration
work without it. The
session commands run on Linux/macOS (or WSL), use `origin/master`, and expect
write access to the same GitHub repository. Configure your Git author name and
email. Maintainers using PR numbers should authenticate `gh`. QualCoder schema v17 is supported.
No additional Python packages are needed for this workflow.

Commit and push the workflow/configuration changes to `origin/master` before the first session: starting
requires a clean checkout on `master`. Keep the project closed while starting,
completing, or integrating a session. Automatic backups and AI chat history stay
local; already-tracked generated files have been removed from tracking, retaining
their local copies. Existing copies remain in Git history.

## Local commit guards and database protection

The hook sources are versioned in `.githooks/`. Git does not enable hooks merely
by cloning a repository. Enable them once in each clone, with QualCoder closed:

```sh
make coding-setup
```

The menu and all session commands refuse to run until setup has completed. They
also reject missing, disabled, changed, or non-executable hooks; run
`make coding-setup` again after updating the guard code or repairing an installation.
They never silently install or repair guards. Setup copies
the managed hooks and their standalone Python helper into Git's local common
directory and sets local `core.hooksPath`. The installed copies continue to work
when switching to older branches that lack the hook source files. No global Git
settings are changed. Existing custom hooks or `core.hooksPath` are preserved:
setup stops rather than replacing them silently.

- The database is **read-only on master**, detached checkouts, completed coding
  branches, and branches without a matching active session.
- Starting or resuming the registered session enables owner write access. Its
  branch must still be at the session's recorded starting commit.
- Finishing returns to master and restores read-only permissions. Checkout and
  merge hooks reapply permissions after manual branch switches and pulls.
- Commits containing `data/coding.qda/data.qda` on master are rejected. Ordinary
  tooling/documentation commits on master remain allowed.
- Manual commits on coding branches are rejected, including empty commits. Use
  `make coding-finish`. The finish and integration programs authorize only their
  exact staged tree and branch for their own commit subprocess; they do not leave
  a global bypass enabled. Integration writes occur in its isolated worktree.

To reapply permissions after an interrupted operation:

```sh
make coding-protect
```

These are accident guards, not an access-control boundary against the checkout's
owner: local hooks can be bypassed and permissions can be changed manually.
**Close QualCoder before switching branches.** A post-checkout hook runs after
Git has switched, and removing write permissions does not revoke an already-open
database handle. If that is detected, close the application and run
`make coding-protect`. Keep GitHub's master protection enabled as the server-side
control. Fast-forward Git merges do not create commits and are not blocked by a
pre-commit hook.

For intentional corpus/codebook maintenance, use a separate maintenance branch
with no active coding session, explicitly enable database writes there with
`chmod u+w data/coding.qda/data.qda`, and follow the maintainer's review process.
Reapply protection afterward. Do not perform that maintenance on master or in a
coder's active session.

### Enable automatic notification PRs

Publish `.github/workflows/coding-session-pr.yml` with this setup. In the repository's
**Settings → Actions → General → Workflow permissions**, enable **Allow GitHub
Actions to create and approve pull requests**. Organization policy can restrict
this setting. The workflow uses `GITHUB_TOKEN` with contents read access and
pull-request write access; it requires no custom secret or local `gh` installation.
See [GitHub's repository Actions settings documentation](https://docs.github.com/en/repositories/managing-your-repositorys-settings-and-features/enabling-features-for-your-repository/managing-github-actions-settings-for-a-repository).

Every push to `coding/**` validates the completed session manifest and changed
paths, then creates a draft PR or refreshes its title, summary, and snapshot SHA.
Existing open notifications are kept as drafts; closed notifications are not
reopened. Already-integrated snapshots are skipped. The workflow reads metadata
through GitHub APIs and never checks out repository files or runs their scripts,
approves a PR, or merges the SQLite database. Full database validation remains
the maintainer program's responsibility.

## Coder commands

Run the interactive menu:

```sh
make coding
```

Or run its individual commands:

```sh
make coding-start
make coding-finish
make coding-request-merge
make coding-status
```

1. **Start** fetches and fast-forwards `master`, asks for your coder name, and
   creates a unique `coding/<name>/<timestamp>-<id>` branch in this checkout. A
   suggested name can be confirmed with Enter; `default` is not accepted. Open
   `data/coding.qda` yourself, and verify your name in QualCoder Settings before
   coding. Existing passages retain their original attribution.
2. **Finish** validates the work and shows the additions, edits, and deletions
   grouped by document and coder. Answer `y` to commit the database and session
   manifest; Enter or `n` leaves the session active. After committing, the script
   returns to `master`. No unrelated files are staged; resolve unrelated work
   separately if it prevents completion.
   The commit message and session manifest list the corpus documents whose coding
   changed, with per-file counts for added, edited, and deleted coding/annotations.
3. **Request merge** checks remote branches and integration audits, offers only
   unpublished completed sessions, and pushes the selected immutable snapshot.
   Already-published or integrated sessions are excluded. An explicit
   `SESSION=SESSION_ID` for one of those sessions reports its status without
   pushing again. Publication status is saved locally and refreshed each time
   this command runs, including sessions created before status tracking existed.
   The Action creates or updates the draft notification PR asynchronously. No local
   GitHub CLI calls are made. The command also prints the branch and a direct
   integration command to share with the maintainer if Actions are unavailable. With
   several completed sessions, select one interactively or use
   `make coding-request-merge SESSION=SESSION_ID`.

Within a session, you may add/edit/delete **your own text coding and
annotations**, including their memos and importance flags. Do not change source
text, source/document memos, cases, attributes, codes, categories, journals,
graphs, or another coder's records. Media/transcript coding is outside version
one. Codebook changes should be agreed and committed on master between coding
rounds. Routine bookmarks, the selected coder, display settings, and filters
can change; integration retains the master's UI state.

You may code different documents/cases or independently code the same passages.
Different coder names preserve overlapping interpretations and independent
agreement. QualCoder's current-coder setting affects which coding is displayed;
switch coders or use its reports when comparing results.

## Maintainer integration

From a clean `master` checkout with no active session:

```sh
make coding-integrate PR=123
```

Or integrate a published session branch directly, with no `gh` dependency:

```sh
make coding-integrate BRANCH=coding/alice/SESSION_BRANCH
```

The menu accepts either a PR number or the full `coding/...` branch name. Branch
mode validates the remote branch's manifest and snapshot, confirms the merge, and
records it in the same integration audit trail. When `gh` is available and
authenticated, it finds the matching open notification and comments with the
integration commit, leaving the PR open. Without `gh`, the coding still integrates.
Rerunning the branch command retries a missing comment without duplicating coding
or existing comments. Close the notification manually afterward, or rerun
integration by PR number when `gh` is available to close it automatically.
Comment failures are reported separately and do not undo a successful integration.

The command checks the PR's recorded snapshot, extracts its common starting
project, and compares it with current remote master. It uses trusted tooling
from your checkout, never scripts from the submission branch. Work happens in a
separate integration worktree under Git's local directory.

Read the report and inspect the candidate project if desired. Close that
candidate before proceeding; any database change during review requires a fresh
preview (including UI changes saved by the application). Answer `y` to commit and push the integration and
its audit record, comment with the integration commit, and close the draft PR.
GitHub will show it as **closed**, not merged; integration is recorded in
`coding/merges/SESSION_ID.json` and the Git commit. Session branch history is not
merged into master. Do not enable auto-merge on notification PRs.

The merger compares logical records rather than independently allocated numeric
IDs. Independent changes are combined, identical changes are coalesced, and
overlapping passages by different coders are retained. It understands deletions
relative to the recorded base; it does not simply union database rows. Different
edits to the same logical record, deletion versus editing, and incompatible
additions by the same coder stop integration for review. Changed document text,
case structure, codebook, or unsupported analytical tables also stop integration.
Deletions that would invalidate graph references are rejected.

New notification PRs show a **Corpus files with coding changes** section, with
links to the document snapshots and per-file change counts. Large lists include
a link to the full manifest to stay within GitHub's PR-description size limit.
The maintainer verifies this file list against the actual database changes.
Older session manifests remain supported; their PRs indicate that a file list
was not recorded rather than guessing one. Integration commit messages also list
the files whose coding was actually changed by the merge.

### Failures and recovery

- No input project is overwritten by the standalone merger. Integration retains
  its candidate, report, and worktree path on cancellation or failure; master is
  unchanged until the explicit integration confirmation and successful push.
- Push/network failure: rerun `request-merge`. The completed branch and committed
  coding remain available. If the push succeeded but the Action failed, check
  repository Actions and rerun the failed job after correcting its settings; an
  up-to-date Git push does not create another push event. Direct branch integration
  remains available even when notification creation fails.
- Interrupted completion: run `status`, return to its recorded session branch
  if necessary, and rerun `finish`. A commit made before the interruption is
  recognized and is not duplicated. If completion succeeded but returning to
  master failed, close QualCoder, resolve unrelated work, and switch to master.
- Master advanced or push was rejected: rerun `make coding-integrate PR=PR_NUMBER`
  (or `make coding-integrate BRANCH=coding/...`) for a fresh
  candidate and confirmation. Do not rebase the binary integration or force-push.
- Integration pushed but PR closure failed: rerun `make coding-integrate PR=PR_NUMBER`. Its audit
  record prevents duplicate coding and lets the notification closure be retried.
- Conflicts or rejected structural changes: inspect the retained JSON report,
  resolve the research decision outside the immutable submitted snapshot, and
  prepare a new session from master. Do not edit the database with a text editor.

The local active/completed-session registry is stored in the checkout's Git
directory under `qualcoder/state.json`; `status` shows its branch and commit IDs.
Committed manifests live in `coding/sessions/` on submission branches. Losing the
local registry does not remove those commits, but the menu will no longer know
which local sessions to offer automatically.

## Standalone merger

For manual review of three closed project directories:

```sh
python3 -B scripts/merge_qualcoder.py \
  --base /tmp/base.qda \
  --destination /tmp/master.qda \
  --submission /tmp/alice.qda \
  --coder Alice \
  --report /tmp/merge-report.json
```

Preview does not modify project data. Add `--apply --output /tmp/merged.qda` to
write a new candidate after validation. Existing output directories are refused.
Exit code 2 indicates a conflict, unsupported change, or validation failure.

The merger verifies matching schemas and frozen project content, exact selected
excerpts, valid character offsets, references, unique records, and SQLite
integrity. It checks the complete candidate database against its expected result.
Text identity and code IDs must remain stable through the coding round.
QualCoder's native text offsets use UTF-16 units. The merger verifies selected
text against both UTF-16 and legacy Python code-point offsets, preserving the
stored positions unchanged. Annotation previews prefer native UTF-16 when both
interpretations are possible, since annotations contain no selected-text field.

## Tests

```sh
make coding-test
```

The collaboration tests create small project fixtures and local bare Git
remotes, and mock all GitHub operations. They do not publish real PRs, alter the
research database, or start a real coding session.
The Action tests require Node.js 18+ locally and execute the exact inline workflow
script against mocked GitHub APIs. Node.js is not needed on coders' machines.
