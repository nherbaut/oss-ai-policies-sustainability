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
  branch must be at its recorded starting commit or latest authorized synchronization checkpoint.
- Finishing returns to master and restores read-only permissions. Checkout and
  merge hooks reapply permissions after manual branch switches and pulls.
- Commits containing `data/coding.qda/data.qda` on master are rejected. Ordinary
  tooling/documentation commits on master remain allowed.
- Manual commits on coding branches are rejected, including empty commits. Use
  `make coding-finish` or `make coding-sync`. The finish, synchronization, and integration programs authorize only their
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
make coding-sync  # after shared theory changes (once the registry is initialized)
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
text, source/document memos, cases, attributes, journals, graphs, or another coder's
records. After the codebook registry is initialized, you may also create codes and
categories attributed to yourself and refine your own new concepts, including
their hierarchy and definitions. Existing shared concepts are maintained through
the theory workflow below. Before initialization, codes and categories remain
frozen. Media/transcript coding is outside this merger's scope. Routine bookmarks, the selected coder, display settings, and filters
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
case structure, unauthorized shared-codebook changes, or unsupported analytical
tables also stop integration.
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

## Inductive coding and shared theory

The shared codebook uses `coding/codebook.json` to associate permanent UUIDs with
QualCoder codes/categories. SQLite IDs are local identifiers and can collide
across branches; synchronization and integration translate them by UUID, including
code/category references in coding and graphs. The SQLite schema and native
UTF-16 passage offsets stay unchanged. Names never establish identity on their own.

### Enable once at a clean boundary

First finish and integrate outstanding legacy sessions in every clone. Remove
published coding branches from the remote after integration. From a clean master
matching origin/master, with no active session:

```sh
make coding-setup
make coding-codebook-init
git add coding/codebook.json
git commit -m "Initialize shared codebook identities"
git push origin master
```

Initialization writes only the registry; it preserves every existing coded
passage and leaves the database unchanged. It refuses outstanding local legacy
jobs or remote coding branches. Coordinate with other coders: a legacy active
session in another clone cannot be discovered if it was never pushed. New
sessions use the new protocol only after the registry has been committed and
published. This implementation does not initialize the research project for you.

### Work inductively on a coding branch

Use `make coding-start` as usual. Add codes/categories in QualCoder under your
confirmed coder name. You can rename, redefine, recolor, or reorganize those new
concepts; you cannot edit/delete existing shared concepts or another coder's
records. Remove an unused local proposal if it is no longer needed. Codebook
proposals are shown at completion, in the commit, in the notification PR, and in
its full session manifest. Integration accepts proposals into the shared registry.
That advances the shared revision for other active sessions.

### Incorporate new shared theory explicitly

Keep QualCoder closed and run:

```sh
make coding-sync
```

Synchronization fetches origin/master and imports its **codebook only**. It keeps
your local codebook proposals and coding, without importing other coders' new
passages. A preview lists theory changes and your affected passages. Definitions
are reported for interpretation; assignments are not automatically recoded and no
review acknowledgement is required. After your confirmation it writes a backup,
updates the database/registry/progress manifest, and makes an authorized sync
commit on the existing coding branch. The original baseline stays recorded; the
new checkpoint is used by the guards. Running sync again when current makes no
commit. Do not Git-merge or rebase master into an active session.

Completion checks the latest shared revision and asks you to synchronize if it
changed. Once a session is completed, further theory updates are handled by the
maintainer during integration: the report shows affected submitted passages and
preserves their assignments, without requiring the coder to reopen the session.

An interrupted sync before its commit restores the verified backup on the next
sync/finish command, provided the files have not since changed. An interruption
after the commit recovers the checkpoint from its committed progress manifest.
If recovery finds additional edits, it stops and points to the backup rather than
overwriting them. Reports and backups remain under `.git/qualcoder/sync-*`.

### Publish new theory as a maintainer

Prepare theory manually on a separate maintenance branch, with no coding session:

```sh
git switch master
git pull --ff-only
git switch -c maintenance/new-theory
chmod u+w data/coding.qda/data.qda
# Edit only the codebook in QualCoder, then close it.
make coding-codebook-register
git add data/coding.qda/data.qda coding/codebook.json coding/theory/
git commit -m "Register new theory"
git push -u origin maintenance/new-theory
git switch master
make coding-theory-publish BRANCH=maintenance/new-theory
```

Registration records new UUIDs and a theory manifest; it validates that documents,
cases, coding, annotations, and other analytical content are unchanged. Re-run
registration after refining your maintenance work and before committing it.
Use a fresh branch for each published revision. Publication compares the theory
branch with its base and the latest master, builds a candidate in an isolated
worktree, and previews changed concepts and affected master passages. Confirm to
commit/push the semantic result and its audit in `coding/theory-revisions/`.
Existing master coding is preserved. A rejected push requires a new preview;
rerunning an already published snapshot is harmless. Master remains read-only
and its database commit guard stays enabled.

Maintainers can add, rename, redefine, recolor, and reorganize shared concepts.
Deleting or merging shared codes/categories is deliberately unsupported. Two
maintainers changing the same field differently produces a conflict; refine the
maintenance branch, register it again, and retry. Disjoint field edits can merge.

### Decide conflicts between independently created concepts

Independent same-name codes/categories stop sync or integration even if their
definitions match. The printed `conflicts.json` includes the current destination
revision and the proposal UUIDs. Copy it outside the repository and replace its
`choices` list with explicit decisions, for example:

```json
{
  "revision": "CURRENT_DESTINATION_REVISION_FROM_REPORT",
  "choices": [
    {"entity": "LOCAL_PROPOSAL_UUID", "action": "adopt-shared", "target": "SHARED_UUID"}
  ]
}
```

Adoption reassigns references to the chosen shared concept. To keep a distinct
concept, use `{"entity":"LOCAL_PROPOSAL_UUID","action":"rename-local","name":"Distinct name"}`.
Never edit UUIDs to force equivalence. Resolutions target the exact destination
revision; stale files are rejected. Run the applicable command again:

```sh
make coding-sync RESOLUTIONS=/tmp/decisions.json
make coding-integrate BRANCH=coding/alice/SESSION_BRANCH RESOLUTIONS=/tmp/decisions.json
make coding-theory-publish BRANCH=maintenance/new-theory RESOLUTIONS=/tmp/decisions.json
```

These decisions apply to incoming new concepts. Shared-field conflicts require
refinement on the maintenance branch. If adoption would collapse multiple coding
records onto one identity, review those passages first; the program rejects that
case instead of discarding a record.

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
Text identity must remain stable through the coding round. The standalone legacy
merger also requires unchanged code IDs and a frozen codebook; use the session
commands for codebook-aware merges.
QualCoder's native text offsets use UTF-16 units. The merger verifies selected
text against both UTF-16 and legacy Python code-point offsets, preserving the
stored positions unchanged. Annotation previews prefer native UTF-16 when both
interpretations are possible, since annotations contain no selected-text field.

## Sourced sustainability taxonomy

`coding/taxonomy.json` records the 20 source-authored categories from Roy et al.
(2026, DOI `10.1145/3786148.3788620`) and five **provisional** individual categories.
Raw labels and metrics follow the source image. Workbook definitions retain their
own labels and exact cell locations; differences and contradictions are explicit.
Operational definitions and coding guidance for OSS/GenAI are researcher proposals,
not quotations or empirically observed effects. The individual extension still
needs verification against the original literature.

`scripts/import_sustainability_taxonomy.py` imports five dimension categories and
25 codes with English verbatim source excerpts and citations in their memos.
The project memo contains excerpts defining the five sustainability dimensions.
Researcher adaptations, coding guidance and source metrics are retained in
`coding/taxonomy.json`.

Preview is read-only:

```sh
python3 -B scripts/import_sustainability_taxonomy.py
```

For an explicitly authorized **complete reset** with QualCoder closed:

```sh
python3 -B scripts/import_sustainability_taxonomy.py --apply --reset-coded-data
```

This deletes all existing text/media coding, annotations and codebook entries.
It preserves corpus text, document/case provenance, case links and coder records.
It creates a complete project backup and audit report in the ignored
`data/qualcoder-backups/`, verifies a separate candidate against every expected
table, then replaces only the database and preserves its permissions. Analytical
graphs or an initialized shared UUID registry require separate reconciliation;
the reset refuses to leave those references inconsistent. The tool does not
initialize the shared registry, modify Git guards, commit or push. Existing
master database commit guards still apply.

## Static coding explorer

Generate a standalone, read-only explorer of the current checkout's coding:

```sh
make coding-site
python3 -m http.server 8000 --directory dist/coding-site
```

Open <http://localhost:8000>. The English interface includes searchable documents,
the code/category tree and memos, filters by code and coder, highlighted source
text, overlapping interpretations, coding memos, importance flags, and annotations.
Selecting a code filters that exact code; the code tree counts all coded passages
in the snapshot. Documents without coding remain visible unless filtered out.
Text is displayed verbatim, including Markdown, to preserve coding positions.
UTF-16 positions and historical code-point positions are validated against the
stored excerpts. Media files, journals, and application settings are not exported.

The output is `dist/coding-site/` (ignored by Git). Python 3.10+ is the only build
dependency; no packages, network, backend, or CDN are needed. All document text,
coder names, document/code memos, and annotations are included in this export.
Rerun the target to refresh the snapshot; the QualCoder project is never modified.
Invalid references or text positions stop generation with an explicit error.
The exporter supports custom locations:

```sh
python3 -B scripts/build_coding_site.py --project data/coding.qda --output /tmp/coding-site
```

### GitHub Pages deployment

The workflow `.github/workflows/coding-site-pages.yml` tests and rebuilds the site
from the committed QualCoder database, then publishes `dist/coding-site/` as a
GitHub Pages artifact. Generated files, including `.nojekyll` and `.coding-site`,
stay ignored by Git; only the generator, web assets, and workflow are versioned.
Relative asset URLs work under a repository subpath.

In the repository's **Settings → Pages → Build and deployment → Source**, select
**GitHub Actions** once. Commit and push the site sources and workflow to `master`.
Changes to the database, generator, assets, exporter tests, or build workflow then
trigger deployment automatically. You can also select **Deploy coding explorer
to GitHub Pages → Run workflow** in the Actions tab, with the `master` branch.
Manual runs on other branches are skipped. No personal token is needed: the
deployment job uses `GITHUB_TOKEN` and GitHub's OIDC permissions.

The published URL appears in the workflow's `github-pages` environment. Only the
generated site directory is uploaded, including the exported corpus text, coder
names, memos, and annotations. `make coding-site` itself remains a local build.
See [GitHub's custom Pages workflow documentation](https://docs.github.com/en/pages/getting-started-with-github-pages/using-custom-workflows-with-github-pages).

## Tests

```sh
make coding-test
```

The collaboration tests create small project fixtures and local bare Git
remotes, and mock all GitHub operations. They do not publish real PRs, alter the
research database, or start a real coding session.
The Action tests require Node.js 18+ locally and execute the exact inline workflow
script against mocked GitHub APIs. Node.js is not needed on coders' machines.

## Export the taxonomy for a paper

Run `make coding-taxonomy-export` to export the current QualCoder categories,
codes and complete memos to `coding/exports/taxonomy.md` and `taxonomy.json`,
with a companion `refs.bib`. The command also refreshes the marked taxonomy
section in `protocol.md`. The export reads a consistent SQLite snapshot.

With QualCoder closed, `make coding-taxonomy-references` refreshes the source excerpts and citations
in the existing taxonomy memos, saves a database backup and regenerates the
exports. Future imports use the same excerpt format. Record a supporting
reference and source location for each new code or category, or its inductive
origin and supporting corpus passages. Repository instructions in `AGENTS.md`
apply this requirement to future taxonomy work.

The taxonomy exporter also produces `coding/exports/taxonomy.svg` for vector
publication, `taxonomy.png` for previews and the protocol, and editable Graphviz
source in `taxonomy.dot`. Graphviz (`dot`) must be installed. The figure captions cite the sources through `refs.bib` and identify the
individual-level categories as provisional. Regenerate all formats with `make coding-taxonomy-export`.

Taxonomy memos contain English verbatim source excerpts followed by citations and
source locations. Researcher interpretations and provisional status are recorded
in `coding/taxonomy.json`. For the five provisional individual-level codes, the
current verified excerpts are category labels from the supplied literature survey.
