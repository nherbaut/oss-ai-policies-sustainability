<div class="col-12 col-md-9 col-xl-8 ps-md-5" role="main">

1.  [Documentation](/docs/)
2.  [Getting Started](/docs/guide/)
3.  Pull Request Process

<div class="td-content">

# Pull Request Process

<div class="lead">

Explains the process and best practices for submitting a pull request to
the Kubernetes project and its associated sub-repositories. It should
serve as a reference for all contributors, and be useful especially to
new or infrequent submitters.

</div>

This doc explains the process and best practices for submitting a pull
request to the
<a href="https://github.com/kubernetes/kubernetes" target="_blank"
rel="noopener">Kubernetes project</a> and its associated
sub-repositories. It should serve as a reference for all contributors,
and be useful especially to new and infrequent submitters.

- [Before You Submit a Pull Request](#before-you-submit-a-pull-request)
  - [Run Local Verifications](#run-local-verifications)
- [The Pull Request Submit Process](#the-pull-request-submit-process)
  - [Marking Unfinished Pull
    Requests](#marking-unfinished-pull-requests)
  - [Pull Requests and the Release
    Cycle](#pull-requests-and-the-release-cycle)
  - [Comment Commands Reference](#comment-commands-reference)
  - [Automation](#automation)
  - [How the e2e Tests Work](#how-the-e2e-tests-work)
- [Why was my pull request closed?](#why-was-my-pull-request-closed)
- [Why is my pull request not getting
  reviewed?](#why-is-my-pull-request-not-getting-reviewed)
- [Best Practices for Faster
  Reviews](#best-practices-for-faster-reviews)
  - [Familiarize yourself with project
    conventions](#familiarize-yourself-with-project-conventions)
  - [Is the feature wanted? File a Kubernetes Enhancement
    Proposal](#is-the-feature-wanted-file-a-kubernetes-enhancement-proposal)
  - [KISS, YAGNI, MVP, etc.](#kiss-yagni-mvp-etc)
  - [Smaller Is Better: Small Commits, Small Pull
    Requests](#smaller-is-better-small-commits-small-pull-requests)
  - [Open a Different Pull Request for Fixes and Generic
    Features](#open-a-different-pull-request-for-fixes-and-generic-features)
  - [Don’t Open Pull Requests That Span the Whole
    Repository](#dont-open-pull-requests-that-span-the-whole-repository)
  - [Comments Matter](#comments-matter)
  - [Test](#test)
  - [Squashing](#squashing)
  - [Commit Message Guidelines](#commit-message-guidelines)
  - [It’s OK to Push Back](#its-ok-to-push-back)
  - [Common Sense and Courtesy](#common-sense-and-courtesy)
  - [Trivial Edits](#trivial-edits)
  - [Large or Automatic Edits](#large-or-automatic-edits)
  - [Fixing Linter Issues](#fixing-linter-issues)
  - [AI Guidance](#ai-guidance)
- [The Testing and Merge Workflow](#the-testing-and-merge-workflow)
  - [More About `Ok-To-Test`](#more-about-ok-to-test)

# Before You Submit a Pull Request<a href="#before-you-submit-a-pull-request" class="td-heading-self-link"
aria-label="Heading self-link"></a>

This guide is for contributors who already have a pull request to
submit. If you’re looking for information on setting up your developer
environment and creating code to contribute to Kubernetes, see the <a
href="https://github.com/kubernetes/community/blob/main/contributors/devel/development.md"
target="_blank" rel="noopener">development guide</a>.

First-time contributors should head to the [Contributor
Guide](/docs/guide) to get started.

**Make sure your pull request adheres to our best practices. These
include following project conventions, making small pull requests, and
commenting thoroughly. Please read the more detailed section on [Best
Practices for Faster Reviews](#best-practices-for-faster-reviews) at the
end of this doc.**

## Run Local Verifications<a href="#run-local-verifications" class="td-heading-self-link"
aria-label="Heading self-link"></a>

You can run these local verifications before you submit your pull
request to predict the pass or fail of continuous integration.

- Run and pass `make verify` (can take 30-40 minutes)
- Run and pass `make test`
- Run and pass `make test-integration`

# The Pull Request Submit Process<a href="#the-pull-request-submit-process" class="td-heading-self-link"
aria-label="Heading self-link"></a>

Merging a pull request requires the following steps to be completed
before the pull request will be merged automatically.

- <a href="https://help.github.com/articles/about-pull-requests/"
  target="_blank" rel="noopener">Open a pull request</a>
  - *For kubernetes/kubernetes repository only:* Add [release
    notes](/docs/guide/release-notes) if needed.
- Follow the EasyCLA steps to
  <a href="https://git.k8s.io/community/CLA.md" target="_blank"
  rel="noopener">sign the CLA</a> (prerequisite)
- Pass all e2e tests
- Get all necessary approvals from reviewers and code owners

## Marking Unfinished Pull Requests<a href="#marking-unfinished-pull-requests" class="td-heading-self-link"
aria-label="Heading self-link"></a>

If you want to solicit reviews before the implementation of your pull
request is complete, you should hold your pull request to ensure that
Tide does not pick it up and attempt to merge it. There are two methods
to achieve this:

1.  You may add the `/hold` or `/hold cancel` comment commands
2.  You may add or remove a `WIP` or `[WIP]` prefix to your pull request
    title

The GitHub robots will add and remove the `do-not-merge/hold` label as
you use the comment commands and the `do-not-merge/work-in-progress`
label as you edit your title. While either label is present, your pull
request will not be considered for merging.

## Pull Requests and the Release Cycle<a href="#pull-requests-and-the-release-cycle"
class="td-heading-self-link" aria-label="Heading self-link"></a>

If a pull request has been reviewed but held or not approved, it might
be due to the current phase in the <a
href="https://github.com/kubernetes/community/blob/main/contributors/devel/sig-release/release.md"
target="_blank" rel="noopener">Release Cycle</a>. Occasionally, a SIG
may freeze their own code base when working towards a specific feature
or goal that could impact other development. During this time, your pull
request could remain unmerged while their release work is completed.

If you feel your pull request is in this state, contact the appropriate
<a href="https://git.k8s.io/community/sig-list.md" target="_blank"
rel="noopener">SIG</a> or
<a href="https://git.k8s.io/sig-release" target="_blank"
rel="noopener">SIG-Release</a> for clarification.

Check the [The Testing and Merge
Workflow](#the-testing-and-merge-workflow) at the end of this document
if you’re interested in the details on how exactly the automation
processes pull requests.

## Comment Commands Reference<a href="#comment-commands-reference" class="td-heading-self-link"
aria-label="Heading self-link"></a>

<a href="https://go.k8s.io/bot-commands" target="_blank"
rel="noopener">The commands doc</a> contains a reference for all comment
commands.

## Automation<a href="#automation" class="td-heading-self-link"
aria-label="Heading self-link"></a>

The Kubernetes developer community uses a variety of automation to
manage pull requests. This automation is described in detail <a
href="https://github.com/kubernetes/community/blob/main/contributors/devel/automation.md"
target="_blank" rel="noopener">in the automation doc</a>.

## How the e2e Tests Work<a href="#how-the-e2e-tests-work" class="td-heading-self-link"
aria-label="Heading self-link"></a>

The end-to-end tests will post the status results to the pull request.
If an e2e test fails, `@k8s-ci-robot` will comment on the pull request
with the test history and the comment-command to re-run that test. e.g.

> The following tests failed, say /retest to rerun them all.

# Why was my pull request closed?<a href="#why-was-my-pull-request-closed" class="td-heading-self-link"
aria-label="Heading self-link"></a>

Pull requests older than 90 days will be closed. Exceptions can be made
for pull requests that have active review comments, or that are awaiting
other dependent pull requests. Closed pull requests are easy to
recreate, and little work is lost by closing a pull request that
subsequently needs to be reopened. We want to limit the total number of
pull requests in flight to:

- Maintain a clean project
- Remove old pull requests that would be difficult to rebase as the
  underlying code has changed over time
- Encourage code velocity

# Why is my pull request not getting reviewed?<a href="#why-is-my-pull-request-not-getting-reviewed"
class="td-heading-self-link" aria-label="Heading self-link"></a>

A few factors affect how long your pull request might wait for review.

If it’s the last few weeks of a milestone, we need to reduce churn and
stabilize.

Or, it could be related to best practices. One common issue is that the
pull request is too big to review. Let’s say you’ve touched 39 files and
have 8657 insertions. When your would-be reviewers pull up the diffs,
they run away - this pull request is going to take 4 hours to review and
they don’t have 4 hours right now. They’ll get to it later, just as soon
as they have more free time (ha!).

There is a detailed rundown of best practices, including how to avoid
too-lengthy pull requests, in the next section.

But, if you’ve already followed the best practices and you still aren’t
getting any pull request love, here are some things you can do to move
the process along:

- Make sure that your pull request has an assigned reviewer (assignee in
  GitHub). If not, reply to the pull request comment stream asking for a
  reviewer to be assigned. This is done via a
  <a href="https://prow.k8s.io/command-help" target="_blank"
  rel="noopener">bot command</a> (the bot may have suggestions for this)
  and looks like this: `/assign @username`.

- Ping the assignee (@username) on the pull request comment stream, and
  ask for an estimate of when they can get to the review.

- Ping the assignee on
  <a href="http://slack.kubernetes.io" target="_blank"
  rel="noopener">Slack</a>. Remember that a person’s GitHub username
  might not be the same as their Slack username.

- Ping the assignee by email (many of us have publicly available email
  addresses).

- If you’re a member of the organization ping the
  <a href="https://github.com/orgs/kubernetes/teams" target="_blank"
  rel="noopener">team</a> (via @team-name) that works in the area you’re
  submitting code to.

- If you have fixed all the issues from a review, and you haven’t heard
  back, you should ping the assignee on the comment stream with a
  “please take another look” (`PTAL`) or similar comment indicating that
  you are ready for another review.

- If you still don’t hear back, post a link to the pull request in the
  `#pr-reviews` channel on Slack to find additional reviewers.

Read on to learn more about how to get faster reviews by following best
practices.

# Best Practices for Faster Reviews<a href="#best-practices-for-faster-reviews"
class="td-heading-self-link" aria-label="Heading self-link"></a>

Most of this section is not specific to Kubernetes, but it’s good to
keep these best practices in mind when you’re making a pull request.

You’ve just had a brilliant idea on how to make Kubernetes better. Let’s
call that idea Feature-X. Feature-X is not even that complicated. You
have a pretty good idea of how to implement it. You jump in and
implement it, fixing a bunch of stuff along the way. You send your pull
request - this is awesome! And it sits. And sits. A week goes by and
nobody reviews it. Finally, someone offers a few comments, which you fix
up and wait for more review. And you wait. Another week or two go by.
This is horrible.

Let’s talk about best practices so your pull request gets reviewed
quickly.

## Familiarize yourself with project conventions<a href="#familiarize-yourself-with-project-conventions"
class="td-heading-self-link" aria-label="Heading self-link"></a>

- <a
  href="https://github.com/kubernetes/community/blob/main/contributors/devel/development.md"
  target="_blank" rel="noopener">Development guide</a>
- [Coding conventions](/docs/guide/coding-convention)
- <a
  href="https://github.com/kubernetes/community/blob/main/contributors/devel/sig-architecture/api-conventions.md"
  target="_blank" rel="noopener">API conventions</a>
- <a
  href="https://github.com/kubernetes/community/blob/main/contributors/devel/sig-cli/kubectl-conventions.md"
  target="_blank" rel="noopener">Kubectl conventions</a>

## Is the feature wanted? File a Kubernetes Enhancement Proposal<a href="#is-the-feature-wanted-file-a-kubernetes-enhancement-proposal"
class="td-heading-self-link" aria-label="Heading self-link"></a>

Are you sure Feature-X is something the Kubernetes team wants or will
accept? Is it implemented to fit with other changes in flight? Are you
willing to bet a few days or weeks of work on it?

It’s better to get confirmation beforehand.

When you want to make a large or otherwise significant change, you
should follow the <a
href="https://github.com/kubernetes/enhancements/blob/master/keps/sig-architecture/0000-kep-process/README.md"
target="_blank" rel="noopener">Kubernetes Enhancement Proposal
process</a>.

Even for small changes, it is often a good idea to gather feedback on an
issue you filed, or even simply ask in the appropriate SIG’s Slack
channel to invite discussion and feedback from code owners. Here’s a
<a href="https://github.com/kubernetes/community/blob/main/sig-list.md"
target="_blank" rel="noopener">list of SIGs</a>, this includes their
public meetings.

## KISS, YAGNI, MVP, etc.<a href="#kiss-yagni-mvp-etc" class="td-heading-self-link"
aria-label="Heading self-link"></a>

Sometimes we need to remind each other of core tenets of software
design - Keep It Simple, You Aren’t Gonna Need It, Minimum Viable
Product, and so on. Adding a feature “because we might need it later” is
antithetical to software that ships. Add the things you need NOW and
(ideally) leave room for things you might need later - but don’t
implement them now.

## Smaller Is Better: Small Commits, Small Pull Requests<a href="#smaller-is-better-small-commits-small-pull-requests"
class="td-heading-self-link" aria-label="Heading self-link"></a>

Small commits and small pull requests get reviewed faster and are more
likely to be correct than big ones.

Attention is a scarce resource. If your pull request takes 60 minutes to
review, the reviewer’s eye for detail is not as keen in the last 30
minutes as it was in the first. It might not get reviewed at all if it
requires a large continuous block of time from the reviewer.

**Breaking up commits**

Break up your pull request into multiple commits, at logical break
points.

Making a series of discrete commits is a powerful way to express the
evolution of an idea or the different ideas that make up a single
feature. Strive to group logically distinct ideas into separate commits.

For example, if you found that Feature-X needed some prefactoring to fit
in, make a commit that JUST does that prefactoring. Then make a new
commit for Feature-X.

Strike a balance with the number of commits. A pull request with 25
commits is still very cumbersome to review, so use your best judgment.

**Breaking up Pull Requests**

Or, going back to our prefactoring example, you could also fork a new
branch, do the prefactoring there and send a pull request for that. If
you can extract whole ideas from your pull request and send those as
pull requests of their own, you can avoid the painful problem of
continually rebasing.

Kubernetes is a fast-moving codebase - lock in your changes ASAP with
your small pull request, and make merges be someone else’s problem.

Multiple small pull requests are often better than multiple commits.
Don’t worry about flooding us with pull requests. We’d rather have 100
small,obvious pull requests than 10 unreviewable monoliths.

We want every pull request to be useful on its own, so use your best
judgment on what should be a pull request vs. a commit.

As a rule of thumb, if your pull request is directly related to
Feature-X and nothing else, it should probably be part of the Feature-X
pull request. If you can explain why you are doing seemingly no-op work
(“it makes the Feature-X change easier, I promise”) we’ll probably be OK
with it. If you can imagine someone finding value independently of
Feature-X, try it as a pull request. (Do not link pull requests by `#`
in a commit description, because GitHub creates lots of spam. Instead,
reference other pull requests via the pull request your commit is in.)

## Open a Different Pull Request for Fixes and Generic Features<a href="#open-a-different-pull-request-for-fixes-and-generic-features"
class="td-heading-self-link" aria-label="Heading self-link"></a>

**Put changes that are unrelated to your feature into a different pull
request.**

Often, as you are implementing Feature-X, you will find bad comments,
poorly named functions, bad structure, weak type-safety, etc.

You absolutely should fix those things (or at least file issues,
please) - but not in the same pull request as your feature. Otherwise,
your diff will have way too many changes, and your reviewer won’t see
the forest for the trees.

**Look for opportunities to pull out generic features.**

For example, if you find yourself touching a lot of modules, think about
the dependencies you are introducing between packages. Can some of what
you’re doing be made more generic and moved up and out of the Feature-X
package? Do you need to use a function or type from an otherwise
unrelated package? If so, promote! We have places for hosting more
generic code.

Likewise, if Feature-X is similar in form to Feature-W which was checked
in last month, and you’re duplicating some tricky stuff from Feature-W,
consider prefactoring the core logic out and using it in both Feature-W
and Feature-X. (Do that in its own commit or pull request, please.)

## Don’t Open Pull Requests That Span the Whole Repository<a href="#dont-open-pull-requests-that-span-the-whole-repository"
class="td-heading-self-link" aria-label="Heading self-link"></a>

Often a new contributor will find some problem that exists in many
places across the main `kubernetes/kubernetes` repository, and file a PR
to fix it everywhere at once. Maybe there’s a cool new function in the
latest golang release that everyone ought to be using, or a
recently-deprecated function that ought to be replaced with calls to its
replacement. Sometimes a contributor will run a linter or security
scanner across the code to find problems, or fix a particular spelling
mistake in comments or variable names. (It’s “deprecated”, not
“depreciated”!)

The problem with this approach is that different parts of
`kubernetes/kubernetes` are maintained by different SIGs, and so changes
to those different parts require approvals from different people. A PR
containing 20 one-line changes scattered across the repository could end
up needing 5 or 10 approvals or more before it can be merged. (While
there are a handful of people who can approve changes across large
portions of the repository, those are generally the people who are the
most busy and hardest to get reviews from, especially when you’re a new
contributor with no connections within the community yet.)

The effort required to review such sweeping changes might not be worth
it, see [“large or automatic edits”](#large-or-automatic-edits) below.

If you really want to try to get such a PR merged, your best bet is to
break up the PR into separate PRs for each SIG whose code it touches.
You can look at the `OWNERS` files in a directory (or its parent
directory) to see who owns that code, and then group the changes
together accordingly (e.g., with one PR touching files in
`cmd/kube-proxy` and `pkg/util/iptables`, which are owned by SIG
Network, and another PR touching files in `pkg/kubelet` and
`pkg/controller/nodelifecycle`, which are owned by SIG Node.)

## Comments Matter<a href="#comments-matter" class="td-heading-self-link"
aria-label="Heading self-link"></a>

In your code, if someone might not understand why you did something (or
you won’t remember why later), comment it. Many code-review comments are
about this exact issue.

If you think there’s something pretty obvious that we could follow up
on, add a TODO.

Read up on <a href="https://blog.golang.org/godoc-documenting-go-code"
target="_blank" rel="noopener">GoDoc</a> - follow those general rules
for comments.

## Test<a href="#test" class="td-heading-self-link"
aria-label="Heading self-link"></a>

Nothing is more frustrating than starting a review, only to find that
the tests are inadequate or absent. Very few pull requests can touch the
code and NOT touch tests.

If you don’t know how to test Feature-X, please ask! We’ll be happy to
help you design things for easy testing or to suggest appropriate test
cases.

## Squashing<a href="#squashing" class="td-heading-self-link"
aria-label="Heading self-link"></a>

Your reviewer has finally sent you feedback on Feature-X.

Make the fixups, and don’t squash yet. Put them in a new commit, and
re-push. That way your reviewer can look at the new commit on its own,
which is much faster than starting over.

We might still ask you to clean up your commits at the very end for the
sake of a more readable history, but don’t do this until asked:
typically at the point where the pull request would otherwise be tagged
`LGTM`.

Each commit should have a good title line (\<70 characters) and include
an additional description paragraph describing in more detail the change
intended.

For more information, see [squash
commits](/docs/guide/github-workflow#squash-commits).

**General squashing guidelines:**

- Sausage =\> squash

Do squash when there are several commits to fix bugs in the original
commit(s), address reviewer feedback, etc. Really we only want to see
the end state, and commit message for the whole pull request.

- Layers =\> don’t squash

Don’t squash when there are independent changes layered to achieve a
single goal. For instance, writing a code munger could be one commit,
applying it could be another, and adding a precommit check could be a
third. One could argue they should be separate pull requests, but
there’s really no way to test/review the munger without seeing it
applied, and there needs to be a precommit check to ensure the munged
output doesn’t immediately get out of date.

**Note**: you can also use the `tide/merge-method-squash` label on your
PR to let the bot handle squashing *all* commits, which can be done by
commenting `/label tide/merge-method-squash`. As opposed to squashing by
hand, this will prevent removal of the `lgtm` label (if already applied)
and re-run of the CI tests. Although, if this label is used, please know
the following:

- All commit messages will be squashed and combined and the final commit
  message will be a combination of all commit messages according to how
  GitHub generates the <a
  href="https://docs.github.com/en/pull-requests/collaborating-with-pull-requests/incorporating-changes-from-a-pull-request/about-pull-request-merges#merge-message-for-a-squash-merge"
  target="_blank" rel="noopener">message for a squash merge</a>, for
  example, if this is the lifecycle of your PR:

  ```
  # commit 1
  Original commit msg

  Some useful information
  Some more useful information
  ```

  ```
  # commit 2
  Address review comments
  ```

  ```
  # commit 3
  Fix test
  ```

  After applying the label, if the PR is merged, the final commit
  message will end up being:

  ```
  Title of your PR (#PR-number)

  * Original commit msg

  Some useful information
  Some more useful information

  * Address review comments

  * Fix test
  ```

  Since commit messages are meant to be a record of the “why” and “what”
  of your changes, having messages like “Address review comments” in the
  final commit message adds no real value in terms of communicating the
  “what"s and “why"s of your change. Please see [Commit Message
  Guidelines](#commit-message-guidelines) for more details on writing
  better commit messages.

  Using this label can help when squashing by hand is considered too
  challenging or not worth the extra effort. It can also speed up
  merging because squashing by hand implies getting another LGTM from a
  reviewer and re-run of the CI tests.

## Commit Message Guidelines<a href="#commit-message-guidelines" class="td-heading-self-link"
aria-label="Heading self-link"></a>

PR comments are not represented in the commit history. Commits and their
commit messages are the *“permanent record”* of the changes being done
in your PR and their commit messages should accurately describe both
*what* and *why* it is being done.

Commit messages are comprised of two parts; the subject and the body.

The subject is the first line of the commit message and is often the
only part that is needed for small or trivial changes. Those may be done
as “one liners” with the `git commit -m` or the `--message` flag, but
only if the what and especially why can be fully described in that few
words.

The commit message body is the portion of text below the subject when
you run `git commit` without the `-m` flag which will open the commit
message for editing in your <a
href="https://help.github.com/en/github/using-git/associating-text-editors-with-git"
target="_blank" rel="noopener">preferred editor</a>. Typing a few
further sentences of clarification is a useful investment in time both
for your reviews and overall later project maintenance.

```
This is the commit message subject

Any text here is the commit message body
Some text
Some more text
...

# Please enter the commit message for your changes. Lines starting
# with '#' will be ignored, and an empty message aborts the commit.
#
# On branch example
# Changes to be committed:
#   ...
#
```

Use these guidelines below to help craft a well formatted commit
message. These can be largely attributed to the previous work of
<a href="https://chris.beams.io/" target="_blank" rel="noopener">Chris
Beams</a>,
<a href="https://tpo.pe/" target="_blank" rel="noopener">Tim Pope</a>,
<a href="https://scottchacon.com/" target="_blank" rel="noopener">Scott
Chacon</a> and
<a href="https://ben.straub.cc/" target="_blank" rel="noopener">Ben
Straub</a>.

- [Try to keep the subject line to 50 characters or less; do not exceed
  72
  characters](#try-to-keep-the-subject-line-to-50-characters-or-less-do-not-exceed-72-characters)
- [The first word in the commit message subject should be capitalized
  unless it starts with a lowercase symbol or other
  identifier](#the-first-word-in-the-commit-message-subject-should-be-capitalized-unless-it-starts-with-a-lowercase-symbol-or-other-identifier)
- [Do not end the commit message subject with a
  period](#do-not-end-the-commit-message-subject-with-a-period)
- [Use imperative mood in your commit message
  subject](#use-imperative-mood-in-your-commit-message-subject)
- [Add a single blank line before the commit message
  body](#add-a-single-blank-line-before-the-commit-message-body)
- [Wrap the commit message body at 72
  characters](#wrap-the-commit-message-body-at-72-characters)
- [Do not use GitHub keywords or (@)mentions within your commit
  message](#do-not-use-github-keywords-or-mentions-within-your-commit-message)
- [Use the commit message body to explain the *what* and *why* of the
  commit](#use-the-commit-message-body-to-explain-the-what-and-why-of-the-commit)

### Try to keep the subject line to 50 characters or less; do not exceed 72 characters<a
href="#try-to-keep-the-subject-line-to-50-characters-or-less-do-not-exceed-72-characters"
class="td-heading-self-link" aria-label="Heading self-link"></a>

The 50 character limit for the commit message subject line acts as a
focus to keep the message summary as concise as possible. It should be
just enough to describe what is being done.

The hard limit of 72 characters is to align with the max body size. When
viewing the history of a repository with `git log`, git will pad the
body text with additional blank spaces. Wrapping the width at 72
characters ensures the body text will be centered and easily viewable on
an 80-column terminal.

#### Providing additional context<a href="#providing-additional-context" class="td-heading-self-link"
aria-label="Heading self-link"></a>

You can provide additional context with fewer characters by prefixing
your commit message with the
<a href="https://github.com/kubernetes/kubernetes/labels?q=kind"
target="_blank" rel="noopener">kind</a> or
<a href="https://github.com/kubernetes/kubernetes/labels?q=area"
target="_blank" rel="noopener">area</a> that your PR is impacting. These
are commonly used labels that other members of the Kubernetes community
will understand.

**Examples:**

- `cleanup: remove unused portion of script foo`
- `deprecation: add notice for bar feature removal in future release`
- `etcd: update default server to 3.4.7`
- `kube-proxy: add a test case for HostnameOverride`

These can serve as a good subject before expanding further on the what
and why within the commit message body.

### The first word in the commit message subject should be capitalized unless it starts with a lowercase symbol or other identifier<a
href="#the-first-word-in-the-commit-message-subject-should-be-capitalized-unless-it-starts-with-a-lowercase-symbol-or-other-identifier"
class="td-heading-self-link" aria-label="Heading self-link"></a>

The commit message subject is like an abbreviated sentence. The first
word should be capitalized unless the message begins with symbol,
acronym or other identifier such as
<a href="https://github.com/kubernetes/kubernetes/labels?q=kind"
target="_blank" rel="noopener">kind</a> or
<a href="https://github.com/kubernetes/kubernetes/labels?q=area"
target="_blank" rel="noopener">area</a> that would regularly be
lowercase.

### Do not end the commit message subject with a period<a href="#do-not-end-the-commit-message-subject-with-a-period"
class="td-heading-self-link" aria-label="Heading self-link"></a>

This is primary intended to serve as a space saving measure, but also
aids in driving the subject line to be as short and concise as possible.

### Use imperative mood in your commit message subject<a href="#use-imperative-mood-in-your-commit-message-subject"
class="td-heading-self-link" aria-label="Heading self-link"></a>

Imperative mood can be be thought of as a *“giving a command”*; it is a
**present-tense** statement that explicitly describes what is being
done.

**Good Examples:**

- Fix x error in y
- Add foo to bar
- Revert commit “baz”
- Update pull request guidelines

**Bad Examples**

- Fixed x error in y
- Added foo to bar
- Reverting bad commit “baz”
- Updating the pull request guidelines
- Fixing more things

A general guideline from
<a href="https://chris.beams.io/" target="_blank" rel="noopener">Chris
Beams</a> on forming an imperative commit subject is it should complete
this sentence:

```
If applied, this commit will <your subject line here>
```

**Examples:**

- *If applied, this commit will* **Fix x error in y**
- *If applied, this commit will* **Add foo to bar**
- *If applied, this commit will* **Revert commit “baz”**
- *If applied, this commit will* **Update the pull request guidelines**

### Add a single blank line before the commit message body<a href="#add-a-single-blank-line-before-the-commit-message-body"
class="td-heading-self-link" aria-label="Heading self-link"></a>

Git uses the blank line to determine which portion of the commit message
is the subject and body. Text preceding the blank line is the subject,
and text following is considered the body.

### Wrap the commit message body at 72 characters<a href="#wrap-the-commit-message-body-at-72-characters"
class="td-heading-self-link" aria-label="Heading self-link"></a>

The default column width for git is 80 characters. Git will pad the text
of the message body with an additional 4 spaces when viewing the git
log. This would leave you with 76 available spaces for text, however the
text would be “lop-sided”. To center the text for better viewing, the
other side is artificially padded with the same amount of spaces,
resulting in 72 usable characters per line. Think of them as the margins
in a word doc.

### Do not use GitHub keywords or (@)mentions within your commit message<a
href="#do-not-use-github-keywords-or-mentions-within-your-commit-message"
class="td-heading-self-link" aria-label="Heading self-link"></a>

#### GitHub Keywords<a href="#github-keywords" class="td-heading-self-link"
aria-label="Heading self-link"></a>

Using
<a href="https://help.github.com/articles/closing-issues-using-keywords"
target="_blank" rel="noopener">GitHub keywords</a> followed by a
`#<issue number>` reference within your commit message will
automatically apply the `do-not-merge/invalid-commit-message` label to
your PR preventing it from being merged.

<a href="https://help.github.com/articles/closing-issues-using-keywords"
target="_blank" rel="noopener">GitHub keywords</a> in a PR to close
issues is considered a convenience item, but can have unexpected
side-effects *when used in a commit message*; often closing something
they shouldn’t.

**Blocked Keywords:**

- close
- closes
- closed
- fix
- fixes
- fixed
- resolve
- resolves
- resolved

#### (@)Mentions<a href="#mentions" class="td-heading-self-link"
aria-label="Heading self-link"></a>

(@)mentions within the commit message will send a notification to that
user, and will continually do so each time the PR is updated.

### Use the commit message body to explain the *what* and *why* of the commit<a
href="#use-the-commit-message-body-to-explain-the-what-and-why-of-the-commit"
class="td-heading-self-link" aria-label="Heading self-link"></a>

Commits and their commit messages are the *“permanent record”* of the
changes being done in your PR. Describing why something has changed and
what effects it may have. You are providing context to both your
reviewer and the next person that has to touch your code.

If something is resolving a bug, or is in response to a specific issue,
you can link to it as a reference with the message body itself. These
sorts of breadcrumbs become essential when tracking down future bugs or
regressions and further help explain the *“why”* the commit was made.

**Additional Resources:**

- <a href="https://chris.beams.io/posts/git-commit/" target="_blank"
  rel="noopener">How to Write a Git Commit Message - Chris Beams</a>
- <a
  href="https://git-scm.com/book/en/v2/Distributed-Git-Contributing-to-a-Project"
  target="_blank" rel="noopener">Distributed Git - Contributing to a
  Project (Commit Guidelines)</a>
- <a href="https://preslav.me/2015/02/21/what-s-with-the-50-72-rule/"
  target="_blank" rel="noopener">What’s with the 50/72 rule? - Preslav
  Rachev</a>
- <a
  href="https://tbaggery.com/2008/04/19/a-note-about-git-commit-messages.html"
  target="_blank" rel="noopener">A Note About Git Commit Messages - Tim
  Pope</a>

## It’s OK to Push Back<a href="#its-ok-to-push-back" class="td-heading-self-link"
aria-label="Heading self-link"></a>

Sometimes reviewers make mistakes. It’s OK to push back on changes your
reviewer requested. If you have a good reason for doing something a
certain way, you are absolutely allowed to debate the merits of a
requested change. Both the reviewer and reviewee should strive to
discuss these issues in a polite and respectful manner.

You might be overruled, but you might also prevail. We’re pretty
reasonable people.

Another phenomenon of open-source projects (where anyone can comment on
any issue) is the dog-pile - your pull request gets so many comments
from so many people it becomes hard to follow. In this situation, you
can ask the primary reviewer (assignee) whether they want you to fork a
new pull request to clear out all the comments. You don’t HAVE to fix
every issue raised by every person who feels like commenting, but you
should answer reasonable comments with an explanation.

## Common Sense and Courtesy<a href="#common-sense-and-courtesy" class="td-heading-self-link"
aria-label="Heading self-link"></a>

No document can take the place of common sense and good taste. Use your
best judgment, while you put a bit of thought into how your work can be
made easier to review. If you do these things your pull requests will
get merged with less friction.

## Trivial Edits<a href="#trivial-edits" class="td-heading-self-link"
aria-label="Heading self-link"></a>

Each incoming Pull Request needs to be reviewed, checked, and then
merged.

While automation helps with this, each contribution also has an
engineering cost. Therefore it is appreciated if you do NOT make trivial
edits and fixes, but instead focus on giving the entire file a review.

If you find one grammatical or spelling error, it is likely there are
more in that file, you can really make your Pull Request count by
checking the formatting, checking for broken links, and fixing errors
and then submitting all the fixes at once to that file.

**Some questions to consider:**

- Can the file be improved further?
- Does the trivial edit greatly improve the quality of the content?

## Large or Automatic Edits<a href="#large-or-automatic-edits" class="td-heading-self-link"
aria-label="Heading self-link"></a>

Some tools make it very easy to create large and/or automatic Pull
Requests, for example:

- global search/replace
- linters which automatically correct issues (see also next section)
- AI tools (large language models, assistants, etc) which generate code
  or documentation

To make it easier for reviewers to handle such Pull Requests, please
explain how it was generated in the “Special notes for your reviewer”
section of the Pull Request description. Reviewers may then be able to
reproduce those steps (search/replace, linters) or can start the review
with the right expectations (AI tools). Also consider the section about
[splitting up Pull
Requests](#dont-open-pull-requests-that-span-the-whole-repository)
above.

Even with such tools it is still your responsibility as submitter of a
Pull Request to ensure that the change is correct (to the best of your
knowledge), and that making the change improves the project enough to
justify the cost that is needed to review and merge the Pull Request
(see previous section). If unsure, create a Draft Pull Request and ask
for guidance.

Please understand that reviewers may decide to close a Pull Request with
a reference to this documentation if they come to the conclusion that
the difficulty of properly reviewing the Pull Request outweighs the
benefit that the Pull Request provides.

## AI Guidance<a href="#ai-guidance" class="td-heading-self-link"
aria-label="Heading self-link"></a>

Using AI tools to help write your PR is acceptable, but as the author,
you are responsible for understanding every change. If you used AI tools
in preparing your PR, you must disclose this in the description of your
PR. For example, including “This PR was written in part with the
assistance of generative AI,” in the PR description is sufficient.

Listing AI tooling as a co-author, co-signing commits using an AI tool,
or using the `assisted-by`, `co-developed` or similar commit trailer is
not allowed.

All contributions must follow the [contributions
policies](/docs/guide/contributing) and use commit messages that align
with [the policy](#commit-message-guidelines).

[Large AI generated](#large-or-automatic-edits) PRs and AI generated
commit messages are not allowed.

Do not leave the first review of AI generated changes to the reviewers.
Verify the changes (code review, testing, etc.) before submitting your
PR. Reviewers may ask questions about your AI-assisted code, and if you
cannot explain why a change was made, the PR will be closed.

When responding to review comments, you must do so without relying on AI
tools. Reviewers want to engage directly with you, not with generated
responses. If you do not engage directly with reviewers, the PR will be
closed.

## Fixing Linter Issues<a href="#fixing-linter-issues" class="td-heading-self-link"
aria-label="Heading self-link"></a>

Kubernetes has a set of linter checks. Some of those must pass in the
entire code base, some must pass in new or modified code, and some are
merely hints to developers how to improve their code.

Please do not create Pull Requests for issues found by linters without
first reaching out to maintainers on the `#code-organization`
<a href="http://slack.kubernetes.io" target="_blank"
rel="noopener">Slack</a> channel to determine whether there is
sufficient interest in fixing such issues.

When it was discussed, make sure to include people who gave the
preliminary approval of this work as well as the link to the discussion
on Slack or GitHub issue into the PR description. This is a good example
to follow:

> /area code-organization
>
> This PR fixes linter rules discussed in the Slack
> <a href="https://kubernetes.slack.com/archives/Foo/Bar" target="_blank"
> rel="noopener">https://kubernetes.slack.com/archives/Foo/Bar</a>.
> Preliminary agreement to address those issues were given by @GHHandle1
> and @GHHandle2.
>
> /assign @GHHandle1 /assign @GHHandle2
>
> This PR fixes issues in the package: pkg/kubelet
>
> Related PRs for other packages:
>
> - github.com/link-to-other-PR1
> - github.com/link-to-other-PR2

It does not matter whether the linter is enabled in Kubernetes or not:

- If a linter *is* enabled in <a
  href="https://github.com/kubernetes/kubernetes/blob/master/hack/golangci.yaml"
  target="_blank" rel="noopener">golangci.yaml</a>, then it has already
  been determined that sweeping changes in the existing code aren’t
  necessary or just are not worth the cost (e.g. causing rebases of
  other Pull Requests or obscuring authorship).
- If a linter *is not* enabled, then it might not be important enough.
- If the check is performed by third party tools which are not
  integrated in the Kubernetes CI or proprietary, file a bug or start a
  discussion about it first.

Such Pull Requests are often large and thus hard to review. When the
linter enforces some opinion or policy, then this is not necessarily
something that applies to Kubernetes. Kubernetes uses the formatting
rules enforced by Go. Stricter rules like specific usage of
<a href="https://golangci-lint.run/usage/linters/#whitespace"
target="_blank" rel="noopener">whitespace</a> or using
<a href="https://golangci-lint.run/usage/linters/#usestdlibvars"
target="_blank" rel="noopener">standard library constants</a> are
opinionated and not worth the cost of introducing them now.

Linters worth considering are those which actually improve code
correctness, for example by warning about suspicious code like calling a
function and then not checking the error result.

# The Testing and Merge Workflow<a href="#the-testing-and-merge-workflow" class="td-heading-self-link"
aria-label="Heading self-link"></a>

The Kubernetes merge workflow uses labels, applied by
<a href="https://prow.k8s.io/command-help" target="_blank"
rel="noopener">commands</a> via comments. These will trigger actions on
your pull request. Different Kubernetes repositories may require
different labels on the path to approval. A generic explanation of how
labels are used in pull requests can be found
[here](/docs/guide/owners#code-review-using-owners-files). The pull
request bot will also automatically apply and/or suggest labels.

*Example:* To apply a SIG label, you would type in a comment:

```
/sig apps
```

*NOTE: For pull requests that are in progress but not ready for review,
prefix the pull request title with `WIP` or `[WIP]` and track any
remaining TODOs in a checklist in the pull request description.*

Here’s the process the pull request goes through on its way from
submission to merging:

1.  Make the pull request

2.  `@k8s-ci-robot` assigns reviewers

3.  If you’re **not** a member of the Kubernetes organization, a
    Reviewer/Kubernetes Member checks that the pull request is safe to
    test. If so, they comment `/ok-to-test`. Pull requests by Kubernetes
    organization <a
    href="https://github.com/kubernetes/community/blob/main/community-membership.md"
    target="_blank" rel="noopener">members</a> do not need this step.
    Now the pull request is considered to be trusted, and the pre-submit
    tests will run:

    1.  Automatic tests run. See the current list of tests at this <a
        href="https://prow.k8s.io/?repo=kubernetes%2Fkubernetes&amp;type=presubmit"
        target="_blank" rel="noopener">link</a>
    2.  If tests fail, resolve issues by pushing edits to your pull
        request branch
    3.  If the failure is a flake, anyone on trusted pull requests can
        comment `/retest` to rerun failed tests

4.  Reviewer suggests edits

5.  Push edits to your pull request branch

6.  Repeat the prior two steps as needed until the reviewer(s) add
    `/lgtm` label. The `/lgtm` label, when applied by someone listed as
    a `reviewer` in the corresponding project `OWNERS` file, is a signal
    that the code has passed review from one or more trusted reviewers
    for that project

7.  (Optional) Some reviewers prefer that you squash commits at this
    step

8.  Follow the bot suggestions to assign an OWNER who will add the
    `/approve` label to the pull request. The `/approve` label, when
    applied by someone listed as an `approver` in the corresponding
    project `OWNERS`, is a signal that the code has passed final review
    and is ready to be automatically merged

The behavior of Prow is configurable across projects. You should be
aware of the following configurable behaviors.

- If you are listed as an `/approver` in the `OWNERS` file, an implicit
  `/approve` can be applied to your pull request. This can result in a
  merge being triggered by a `/lgtm` label. This is the configured
  behavior in many projects, including `kubernetes/kubernetes`. You can
  remove the implicit `/approve` with `/approve cancel`
- `/lgtm` can be configured so that from someone listed as both a
  `reviewer` and an `approver` will cause both labels to be applied. For
  `kubernetes/kubernetes` and many other projects this is *not* the
  default behavior, and `/lgtm` is decoupled from `/approve`

Once the tests pass, and the reviewer adds the `lgtm` and `approved`
labels, the pull request enters the final merge pool. The merge pool is
needed to make sure no incompatible changes have been introduced by
other pull requests since the tests were last run on your pull request.

<a href="https://sigs.k8s.io/prow/cmd/tide" target="_blank"
rel="noopener">Tide</a> will manage the merge pool automatically. It
uses GitHub queries to select PRs into “tide pools”, runs as many in a
batch as it can (“tide comes in”), and merges them (“tide goes out”).

1.  The pull request enters the
    <a href="https://prow.k8s.io/tide" target="_blank" rel="noopener">merge
    pool</a> if the merge criteria are met. The
    <a href="https://prow.k8s.io/pr" target="_blank" rel="noopener">PR
    dashboard</a> shows the difference between your PR’s state and the
    merge criteria so that you can easily see all criteria that are not
    being met and address them.
2.  If tests fail, resolve issues by pushing edits to your pull request
    branch
3.  If the failure is a flake, anyone can comment `/retest` if the pull
    request is trusted
4.  If tests pass, Tide automatically merges the pull request

That’s the last step. Your pull request is now merged.

## More About `Ok-To-Test`<a href="#more-about-ok-to-test" class="td-heading-self-link"
aria-label="Heading self-link"></a>

- The ok-to-test label is applied by org members to PRs from external
  contributors, it signals that the PR can be tested.
- For a Contributor, an `ok-to-test` label means the regular CI tests
  will be run for their PR.
- For the reviewer or the member, labelling the PR with `ok-to-test` it
  means a lot more:
  - They need to take care if the PR is not a wastage of our `CI/CD`
    resources.
  - Is the PR worth testing or does it need more changes before going
    through the `CI/CD` process?
  - Is the PR getting used to run malicious code to misuse our resources
    ?
- An `ok-to-test` label may reduce the workload and smoothens the
  contributors experience as they can know if there is any failing test.
  If there is, you can fix the test and they don’t have to wait for a
  long time to get a review from `maintainer/assignee`.
- There are various other factors on which labelling of `ok-to-test`
  depends :
  - Size of PR :
    - If the PR is of `size/S` or `size/M` which is just to fix a
      grammatical error or spelling mistake, the reviewer can trigger
      the `CI/CD` without having a second thought.
    - If the PR is of `size/XXL` which aims at adding a new feature, a
      new API endpoint or any new substantial feature. There needs to
      other conventions & process to be followed regarding the change
      made. Hence, it may have a slight delay to get labelled with
      `ok-to-test`.
  - Other org members who are not assigned to the following PR may also
    label `ok-to-test` , if the change is small.
  - If the PR is labelled with `cncf-cla: no`, then it is better to wait
    before labelling `ok-to-test`.
  - PRs with tag `do-not-merge/hold` or `needs-rebase` should make the
    appropriate changes before the PR can be labelled `ok-to-test`.
  - PRs created by mistake without to meaningful change of code should
    not be labelled `ok-to-test` and closed.

<div class="d-print-none">

## Feedback

Was this page helpful?

Yes

No

</div>

  
  

</div>

</div>
