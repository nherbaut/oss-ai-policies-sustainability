<div id="main-content" class="bd-main" role="main">

<div class="bd-content">

<div class="bd-article-container">

<div class="bd-header-article d-print-none">

<div class="header-article-items header-article__inner">

<div class="header-article-items__start">

<div class="header-article-item">

- <a href="../index.html" class="nav-link" aria-label="Home"><em></em></a>
- <a href="index.html" class="nav-link">Development</a>
- <span class="ellipsis">Contributing Overview</span>

</div>

</div>

</div>

</div>

<div id="searchbox">

</div>

<div id="contributing-overview" class="section">

<span id="contrib-overview"></span>

# Contributing Overview<a href="#contributing-overview" class="headerlink"
title="Link to this heading">#</a>

<div id="local-git-conventions" class="section">

<span id="git-conventions"></span>

## Local git conventions<a href="#local-git-conventions" class="headerlink"
title="Link to this heading">#</a>

If you are tracking the Arrow source repository locally, here is a
checklist for using <span class="pre">`git`</span>:

- Work off of your **personal fork** of
  <span class="pre">`apache/arrow`</span> and submit pull requests
  “upstream”.

- Keep your fork’s **main branch synced** with
  <span class="pre">`upstream/main`</span>.

- **Develop on branches**, rather than your own “main” branch.

- It does not matter what you call your branch. Some people like to use
  the GitHub issue number as branch name, others use descriptive names.

- **Sync your branch** with <span class="pre">`upstream/main`</span>
  **regularly**, as many commits are merged to main every day.

- It is recommended to use
  <span class="pre">`git`</span>` `<span class="pre">`rebase`</span>
  rather than
  <span class="pre">`git`</span>` `<span class="pre">`merge`</span>.

- In case there are conflicts, and your local commit history has
  multiple commits, you may simplify the conflict resolution process by
  **squashing your local commits into a single commit**. Preserving the
  commit history isn’t as important because when your feature branch is
  merged upstream, a squash happens automatically.

  <span class="sd-summary-text">How to squash local
  commits?</span><span class="sd-summary-state-marker sd-summary-chevron-right"><img
  src="data:image/svg+xml;base64,PHN2ZyB2ZXJzaW9uPSIxLjEiIHdpZHRoPSIxLjVlbSIgaGVpZ2h0PSIxLjVlbSIgY2xhc3M9InNkLW9jdGljb24gc2Qtb2N0aWNvbi1jaGV2cm9uLXJpZ2h0IiB2aWV3Ym94PSIwIDAgMjQgMjQiIGFyaWEtaGlkZGVuPSJ0cnVlIj48cGF0aCBkPSJNOC43MiAxOC43OGEuNzUuNzUgMCAwIDEgMC0xLjA2TDE0LjQ0IDEyIDguNzIgNi4yOGEuNzUxLjc1MSAwIDAgMSAuMDE4LTEuMDQyLjc1MS43NTEgMCAwIDEgMS4wNDItLjAxOGw2LjI1IDYuMjVhLjc1Ljc1IDAgMCAxIDAgMS4wNmwtNi4yNSA2LjI1YS43NS43NSAwIDAgMS0xLjA2IDBaIiAvPjwvc3ZnPg=="
  class="sd-octicon sd-octicon-chevron-right" /></span>

  <div class="sd-summary-content sd-card-body docutils">

  Abort the rebase with:

  <div class="highlight-console notranslate">

  <div class="highlight">

      $ git rebase --abort

  </div>

  </div>

  Following which, the local commits can be squashed interactively by
  running:

  <div class="highlight-console notranslate">

  <div class="highlight">

      $ git rebase --interactive ORIG_HEAD~n

  </div>

  </div>

  Where <span class="pre">`n`</span> is the number of commits you have
  in your local branch. After the squash, you can try the merge again,
  and this time conflict resolution should be relatively
  straightforward.

  Once you have an updated local copy, you can push to your remote repo.
  Note, since your remote repo still holds the old history, you would
  need to do a force push. Most pushes should use
  <span class="pre">`--force-with-lease`</span>:

  <div class="highlight-console notranslate">

  <div class="highlight">

      $ git push --force-with-lease origin branch

  </div>

  </div>

  The option <span class="pre">`--force-with-lease`</span> will fail if
  the remote has commits that are not available locally, for example if
  additional commits have been made by a colleague. By using
  <span class="pre">`--force-with-lease`</span> instead of
  <span class="pre">`--force`</span>, you ensure those commits are not
  overwritten and can fetch those changes if desired.

  </div>

  <span class="sd-summary-text">Setting rebase to be
  default</span><span class="sd-summary-state-marker sd-summary-chevron-right"><img
  src="data:image/svg+xml;base64,PHN2ZyB2ZXJzaW9uPSIxLjEiIHdpZHRoPSIxLjVlbSIgaGVpZ2h0PSIxLjVlbSIgY2xhc3M9InNkLW9jdGljb24gc2Qtb2N0aWNvbi1jaGV2cm9uLXJpZ2h0IiB2aWV3Ym94PSIwIDAgMjQgMjQiIGFyaWEtaGlkZGVuPSJ0cnVlIj48cGF0aCBkPSJNOC43MiAxOC43OGEuNzUuNzUgMCAwIDEgMC0xLjA2TDE0LjQ0IDEyIDguNzIgNi4yOGEuNzUxLjc1MSAwIDAgMSAuMDE4LTEuMDQyLjc1MS43NTEgMCAwIDEgMS4wNDItLjAxOGw2LjI1IDYuMjVhLjc1Ljc1IDAgMCAxIDAgMS4wNmwtNi4yNSA2LjI1YS43NS43NSAwIDAgMS0xLjA2IDBaIiAvPjwvc3ZnPg=="
  class="sd-octicon sd-octicon-chevron-right" /></span>

  <div class="sd-summary-content sd-card-body docutils">

  If you set the following in your repo’s
  <span class="pre">`.git/config`</span>, the
  <span class="pre">`--rebase`</span> option can be omitted from the
  <span class="pre">`git`</span>` `<span class="pre">`pull`</span>
  command, as it is implied by default.

  <div class="highlight-console notranslate">

  <div class="highlight">

      [pull]
            rebase = true

  </div>

  </div>

  </div>

</div>

<div id="pull-request-and-review" class="section">

<span id="id1"></span>

## Pull request and review<a href="#pull-request-and-review" class="headerlink"
title="Link to this heading">#</a>

When contributing a patch, use this list as a checklist of Apache Arrow
workflow:

- Submit the patch as a **GitHub pull request** against the **main
  branch**.

- So that your pull request syncs with the GitHub issue, **prefix your
  pull request title with the GitHub issue id** (ex:
  <a href="https://github.com/apache/arrow/pull/14867"
  class="reference external">GH-14866: [C++] Remove internal GroupBy
  implementation</a>).

- Give the pull request a **clear, brief description**: when the pull
  request is merged, this will be retained in the extended commit
  message.

- Make sure that your code **passes the unit tests**. You can find
  instructions how to run the unit tests for each Arrow component in its
  respective README file.

- In order to improve our code and your review experience, we have
  enabled GitHub Copilot reviews to automate the first pass. Reviewers
  and contributors are encouraged to address valid suggestions; you
  don’t need to respond to every comment, but please don’t ignore them
  either.

Core developers and others with a stake in the part of the project your
change affects will review, request changes, and hopefully indicate
their approval in the end. To make the review process smooth for
everyone, try to

- **Break your work into small, single-purpose patches if possible.**

  It’s much harder to merge in a large change with a lot of disjoint
  features, and particularly if you’re new to the project, smaller
  changes are much easier for maintainers to accept.

- **Add new unit tests for your code.**

- **Follow the style guides** for the part(s) of the project you’re
  modifying.

  Some languages (C++ and Python, for example) run a lint check in
  continuous integration. For all languages, see their respective
  developer documentation and READMEs for style guidance.

- Try to make it look as if the codebase has a single author, and
  emulate any conventions you see, whether or not they are officially
  documented or checked.

When tests are passing and the pull request has been approved by the
interested parties, a <a href="https://arrow.apache.org/committers/"
class="reference external">committer</a> will merge the pull request.
This is done with a **command-line utility that does a squash merge**.

<span class="sd-summary-text">Details on squash
merge</span><span class="sd-summary-state-marker sd-summary-chevron-right"><img
src="data:image/svg+xml;base64,PHN2ZyB2ZXJzaW9uPSIxLjEiIHdpZHRoPSIxLjVlbSIgaGVpZ2h0PSIxLjVlbSIgY2xhc3M9InNkLW9jdGljb24gc2Qtb2N0aWNvbi1jaGV2cm9uLXJpZ2h0IiB2aWV3Ym94PSIwIDAgMjQgMjQiIGFyaWEtaGlkZGVuPSJ0cnVlIj48cGF0aCBkPSJNOC43MiAxOC43OGEuNzUuNzUgMCAwIDEgMC0xLjA2TDE0LjQ0IDEyIDguNzIgNi4yOGEuNzUxLjc1MSAwIDAgMSAuMDE4LTEuMDQyLjc1MS43NTEgMCAwIDEgMS4wNDItLjAxOGw2LjI1IDYuMjVhLjc1Ljc1IDAgMCAxIDAgMS4wNmwtNi4yNSA2LjI1YS43NS43NSAwIDAgMS0xLjA2IDBaIiAvPjwvc3ZnPg=="
class="sd-octicon sd-octicon-chevron-right" /></span>

<div class="sd-summary-content sd-card-body docutils">

A pull request is merged with a squash merge so that all of your commits
will be registered as a single commit to the main branch; this
simplifies the connection between GitHub issues and commits, makes it
easier to bisect history to identify where changes were introduced, and
helps us be able to cherry-pick individual patches onto a maintenance
branch.

Your pull request will appear in the GitHub interface to have been
“merged”. In the commit message of that commit, the merge tool adds the
pull request description, a link back to the pull request, and
attribution to the contributor and any co-authors.

</div>

<div id="ai-generated-code" class="section">

<span id="id2"></span>

### AI-generated code<a href="#ai-generated-code" class="headerlink"
title="Link to this heading">#</a>

We recognise that AI coding assistants are now a regular part of many
developers’ workflows and can improve productivity. Thoughtful use of
these tools can be beneficial, but AI-generated PRs can sometimes lead
to undesirable additional maintainer burden. PRs that appear to be fully
generated by AI with little to no engagement from the author may be
closed without further review.

Human-generated mistakes tend to be easier to spot and reason about, and
code review is intended to be a collaborative learning experience that
benefits both submitter and reviewer. When a PR appears to have been
generated without much engagement from the submitter, reviewers with
access to AI tools could more efficiently generate the code directly,
and since the submitter is not likely to learn from the review process,
their time is more productively spent researching and reporting on the
issue.

We are not opposed to the use of AI tools in generating PRs, but
recommend the following:

- Only submit a PR if you are able to debug and own the changes
  yourself - review all generated code to understand every detail

- Match the style and conventions used in the rest of the codebase,
  including PR titles and descriptions

- Be upfront about AI usage and summarise what was AI-generated

- If there are parts you don’t fully understand, leave comments on your
  own PR explaining what steps you took to verify correctness

- Watch for AI’s tendency to generate overly verbose comments,
  unnecessary test cases, and incorrect fixes

- Break down large PRs into smaller ones to make review easier

- AI agents should never tag or ping maintainers

PR authors are also responsible for disclosing any copyrighted materials
in submitted contributions. See the
<a href="https://www.apache.org/legal/generative-tooling.html"
class="reference external">ASF’s guidance on AI-generated code</a> for
further information on licensing considerations.

</div>

</div>

<div id="experimental-repositories" class="section">

## Experimental repositories<a href="#experimental-repositories" class="headerlink"
title="Link to this heading">#</a>

Apache Arrow has an explicit policy over developing experimental
repositories in the context of <a
href="https://grep.codeconsult.ch/2020/04/07/rules-for-revolutionaries-2000-edition/"
class="reference external">rules for revolutionaries</a>.

The main motivation for this policy is to offer a lightweight mechanism
to conduct experimental work, with the necessary creative freedom,
within the ASF and the Apache Arrow governance model. This policy allows
committers to work on new repositories, as they offer many important
tools to manage it (e.g. github issues, “watch”, “github stars” to
measure overall interest).

<div id="process" class="section">

### Process<a href="#process" class="headerlink" title="Link to this heading">#</a>

- A committer *may* initiate experimental work by creating a separate
  git repository within the Apache Arrow (e.g. via
  <a href="https://selfserve.apache.org/"
  class="reference external">selfserve</a>) and announcing it on the
  mailing list, together with its goals, and a link to the newly created
  repository.

- The committer *must* initiate an email thread with the sole purpose of
  presenting updates to the community about the status of the repo.

- There *must not* be official releases from the repository.

- Any decision to make the experimental repo official in any way,
  whether by merging or migrating, *must* be discussed and voted on in
  the mailing list.

- The committer is responsible for managing issues, documentation, CI of
  the repository, including licensing checks.

- The committer decides when the repository is archived.

</div>

<div id="repository-management" class="section">

### Repository management<a href="#repository-management" class="headerlink"
title="Link to this heading">#</a>

- The repository *must* be under <span class="pre">`apache/`</span>

- The repository’s name *must* be prefixed by
  <span class="pre">`arrow-experimental-`</span>

- The committer has full permissions over the repository (within
  possible in ASF)

- Push / merge permissions *must only* be granted to Apache Arrow
  committers

</div>

<div id="development-process" class="section">

### Development process<a href="#development-process" class="headerlink"
title="Link to this heading">#</a>

- The repository must follow the ASF requirements about 3rd party code.

- The committer decides how to manage issues, PRs, etc.

</div>

<div id="divergences" class="section">

### Divergences<a href="#divergences" class="headerlink"
title="Link to this heading">#</a>

- If any of the “must” above fails to materialize and no correction
  measure is taken by the committer upon request, the PMC *should* take
  ownership and decide what to do.

</div>

</div>

<div id="guidance-for-specific-features" class="section">

<span id="specific-features"></span>

## Guidance for specific features<a href="#guidance-for-specific-features" class="headerlink"
title="Link to this heading">#</a>

From time to time the community has discussions on specific types of
features and improvements that they expect to support. This section
outlines decisions that have been made in this regard.

<div id="endianness" class="section">

### Endianness<a href="#endianness" class="headerlink"
title="Link to this heading">#</a>

The Arrow format allows setting endianness. Due to the popularity of
little endian architectures, most of the implementations assume little
endian by default. There has been some effort to support big endian
platforms as well. Based on a <a
href="https://mail-archives.apache.org/mod_mbox/arrow-dev/202009.mbox/%3cCAK7Z5T--HHhr9Dy43PYhD6m-XoU4qoGwQVLwZsG-kOxXjPTyZA@mail.gmail.com%3e"
class="reference external">mailing-list discussion</a>, the requirements
for a new platform are:

1.  A robust (non-flaky, returning results in a reasonable time)
    Continuous Integration setup.

2.  Benchmarks for performance critical parts of the code to demonstrate
    no regression.

Furthermore, for big-endian support, there are two levels that an
implementation can support:

1.  Native endianness (all Arrow communication happens with processes of
    the same endianness). This includes ancillary functionality such as
    reading and writing various file formats, such as Parquet.

2.  Cross endian support (implementations will do byte reordering when
    appropriate for <a href="../format/Columnar.html#format-ipc"
    class="reference internal"><span class="std std-ref">IPC</span></a>
    and <a href="../format/Flight.html#flight-rpc"
    class="reference internal"><span class="std std-ref">Flight</span></a>
    messages).

The decision on what level to support is based on maintainers’
preferences for complexity and technical risk. In general all
implementations should be open to native endianness support (provided
the CI and performance requirements are met). Cross endianness support
is a question for individual maintainers.

The current implementations aiming for cross endian support are:

1.  C++

Implementations that do not intend to implement cross endian support:

1.  Java

For other libraries, a discussion to gather consensus on the
mailing-list should be had before submitting PRs.

</div>

</div>

</div>

<div class="prev-next-area">

<a href="guide/resources.html" class="left-prev"
title="previous page"><em></em></a>

<div class="prev-next-info">

previous

Additional information and resources

</div>

<a href="reviewing.html" class="right-next" title="next page"></a>

<div class="prev-next-info">

next

Reviewing contributions

</div>

</div>

</div>

<div id="pst-secondary-sidebar" class="bd-sidebar-secondary bd-toc">

<div class="sidebar-secondary-items sidebar-secondary__inner">

<div class="sidebar-secondary-item">

<div id="pst-page-navigation-heading-2"
class="page-toc tocsection onthispage">

On this page

</div>

- <a href="#local-git-conventions"
  class="reference internal nav-link">Local git conventions</a>
- <a href="#pull-request-and-review"
  class="reference internal nav-link">Pull request and review</a>
  - <a href="#ai-generated-code"
    class="reference internal nav-link">AI-generated code</a>
- <a href="#experimental-repositories"
  class="reference internal nav-link">Experimental repositories</a>
  - <a href="#process" class="reference internal nav-link">Process</a>
  - <a href="#repository-management"
    class="reference internal nav-link">Repository management</a>
  - <a href="#development-process"
    class="reference internal nav-link">Development process</a>
  - <a href="#divergences"
    class="reference internal nav-link">Divergences</a>
- <a href="#guidance-for-specific-features"
  class="reference internal nav-link">Guidance for specific features</a>
  - <a href="#endianness" class="reference internal nav-link">Endianness</a>

</div>

<div class="sidebar-secondary-item">

<div class="tocsection editthispage">

[ Edit on
GitHub](https://github.com/apache/arrow/edit/main/docs/source/developers/overview.rst)

</div>

</div>

</div>

</div>

</div>

</div>
