<div class="docMainContainer_TBSr" role="main">

<div class="container padding-top--md padding-bottom--lg">

<div class="row">

<div class="col docItemCol_VOVn">

<div class="docItemContainer_Djhp">

- <a href="/" class="breadcrumbs__link" aria-label="Home page"><img
  src="data:image/svg+xml;base64,PHN2ZyB2aWV3Ym94PSIwIDAgMjQgMjQiIGNsYXNzPSJicmVhZGNydW1iSG9tZUljb25fWU5GVCI+PHBhdGggZD0iTTEwIDE5di01aDR2NWMwIC41NS40NSAxIDEgMWgzYy41NSAwIDEtLjQ1IDEtMXYtN2gxLjdjLjQ2IDAgLjY4LS41Ny4zMy0uODdMMTIuNjcgMy42Yy0uMzgtLjM0LS45Ni0uMzQtMS4zNCAwbC04LjM2IDcuNTNjLS4zNC4zLS4xMy44Ny4zMy44N0g1djdjMCAuNTUuNDUgMSAxIDFoM2MuNTUgMCAxLS40NSAxLTF6IiBmaWxsPSJjdXJyZW50Q29sb3IiIC8+PC9zdmc+"
  class="breadcrumbHomeIcon_YNFT" /></a>
- <a href="/docs/general/contributing/"
  class="breadcrumbs__link"><span>Contributing</span></a>
- <span class="breadcrumbs__link">LLM/"AI" Policies</span>

<div class="tocCollapsible_ETCw theme-doc-toc-mobile tocMobile_ITEo">

On this page

</div>

<div class="theme-doc-markdown markdown">

<div>

# Jellyfin LLM/"AI" Development Policy

</div>

The rise of LLMs as a useful development tool over the last year or so
has been significant. The power and flexibility of tools like Claude
Code and ChatGPT have given a lot of functionality both to experienced
developers and new developers alike. But there are trade-offs.

The Jellyfin project has, from day one, had a major focus on code
quality - readability, simplicity, conciseness. This is a mostly manual
effort driven by a dedicated team of individuals, and is motivated by a
desire to fix the code Jellyfin is based off of which, without beating a
dead horse too much, was extremely fragile, spaghettified, and prone to
over-engineered complexity.

We are seeing a precipitous rise in contributors using AI within the
Jellyfin ecosystem, both in the server and for clients, as well as a
rise in criticism and concern about LLMs generally. At this time we are
writing this policy to address exactly what we expect and desire with
respect to contributions and interactions within our community that may
use LLMs. These rules apply to all of our official projects and
community spaces.

## General Guidelines<a href="#general-guidelines" class="hash-link"
aria-label="Direct link to General Guidelines" translate="no"
title="Direct link to General Guidelines">​</a>

1.  LLM output is **expressly prohibited** for any direct communication,
    including the following:

    - issues or comments
    - feature requests or comments
    - pull request bodies or comments
    - forum/chat/etc. posts or comments

    In short, if you are posting **any** of those things, the output
    must be your own words, explanation, description, etc., not a
    verbatim dump of an LLM's output. We expect you to understand what
    you're posting. Violating this rule will result in closure/deletion
    of the offending item(s).

    An exception will be made for **LLM-assisted translations** if you
    are having trouble accurately conveying your intent in English.
    Please explicitly note this ("I have translated this from MyLanguage
    with an LLM") and, if possible, post in your original language as
    well.

2.  LLM code contributions are subject to more granularity below, but
    the general principle is that "pure 'vibe coding' will be rejected"
    and "you are responsible for what you commit". We will review in
    that vein. If the **code looks terrible**, it will be **rejected as
    such**.

## LLM Code Contributions to Official Projects<a href="#llm-code-contributions-to-official-projects" class="hash-link"
aria-label="Direct link to LLM Code Contributions to Official Projects"
translate="no"
title="Direct link to LLM Code Contributions to Official Projects">​</a>

The use of LLMs for code is controversial and open to much
interpretation. These guidelines are our best effort attempt to ensure
that knowledgeable developers who seek to use these tools as a
legitimate aid are not overly-hindered, while also preventing an ongoing
flood of slop contributions that violate our core ethos above. These
apply to **all official Jellyfin projects**.

1.  Contributions should be **concise and focused**. If the PR claims to
    target X, and is also touching unrelated Y and Z, it will be
    rejected. This includes incidental changes to unrelated
    functionality, a hallmark of poorly-worded or too-general prompts.
    Similarly, a large PR must be **broken into multiple small,
    manageable commits** for review and history purposes.
2.  Formatting and quality **standards must be upheld**. Excessive
    unhelpful comments, spaghetti code, spaces on empty lines, etc. will
    be interpreted as pure LLM output and rejected; you must **clean up
    the mess** before submitting. Also **do not commit LLM metafiles**
    (e.g. `.claude` configs) or any other editor-created non-code files.
3.  You must **review the output** and be able to **explain** in the PR
    body - **without** LLM output as noted above - **what is being
    changed and why**. Your PR body (and, if applicable, commit bodies)
    should be providing context to other developers about why a change
    was made, and if your name is on it, we want **your** words and
    explanations, not an LLM's. If **you can't explain** what the LLM
    did, we are **not interested** in the change.
4.  The changes must be **tested**. The code should build and run
    correctly, or it will be rejected. You should also **explicitly test
    the functionality being modified**.
5.  You must be able and willing to **handle review feedback** and
    implement the suggested change(s) as required. What this means in
    practice is, if you do not know what has been changed or why (see
    \#3), and thus can't implement suggested changes or discuss them
    **yourself**, then we are **not interested** in the change. Just
    dumping reviewer feedback into an LLM and expecting what comes out
    to be "good enough", is not.
6.  **Features or refactors** require **an in-depth level of
    understanding** about what is being changed and why. It is obvious
    to our reviewers when changes are made without the developer making
    them understanding what is happening. These will be rejected. And as
    noted in \#1, the PR must **contain multiple discrete commits**.
    *We* will squash commits as deemed appropriate after review. Large
    changes must also follow our other development policies (discussion,
    review, implementation, testing process).
7.  The **final discretion always lies with the reviewers**. If your PR
    is not capable of being reasonably reviewed, for any reason
    (over-complexity, size, squashed commits, etc.) it will be rejected,
    and this goes just as much for non-LLM-assisted PRs as it does for
    LLM-assisted PRs. You will be asked to split such a PR up into
    multiple PRs that each present a focused, concise set of changes
    instead.

The golden rule is this: **do not just let an LLM loose on the codebase
with a vague vibe prompt and then commit the results as-is**. This is
lazy development, will **always** result in a **poor-quality
contribution** from our perspective, and we are not at all interested in
such slop. **Make an effort** or please do not bother. And again, you
are free to use LLMs to **assist** you, but not as the sole source of
code changes.

## LLM-generated Tools, Clients, etc. Shared in the Community<a href="#llm-generated-tools-clients-etc-shared-in-the-community"
class="hash-link"
aria-label="Direct link to LLM-generated Tools, Clients, etc. Shared in the Community"
translate="no"
title="Direct link to LLM-generated Tools, Clients, etc. Shared in the Community">​</a>

You are of course free to do whatever you wish for your own non-official
projects. However, we will be enforcing the following rules for any
**sharing of such projects within our communities**.

1.  Any primarily-LLM-developed projects should be **clearly marked as
    such**. It is up to users to decide if this is acceptable to them or
    not. If you used an LLM for secondary assistance (e.g. docs,
    formatting, etc.) in an obvious way, we would err towards disclosure
    as well.
2.  You **must** respect and follow licenses. If you are basing your
    project off of existing code, **following its license is not
    optional**. You must **credit existing contributors in full** for
    **all contributions**. Do not **mangle the Git history**, and do not
    **commit pending 3rd party changes as your own** (i.e. by copying
    the code and then committing it). Doing so will result in, not just
    rejection, but a ban from our organization and community. We have a
    **zero tolerance policy** for code theft and bad-faith attribution
    attempts.
3.  For members of the community, **do not report** LLM-generated tools,
    clients, etc. **on that basis alone**, and do not engage in anti-LLM
    "witch hunts". As mentioned above, this is **permitted** and it is
    your choice whether to "support" said tool/client/etc. or not.
4.  We, the moderators, are not going to play "LLM police" about 3rd
    party projects by nitpicking to try to "find LLM contributions" that
    otherwise follow our rules here; this is tedious and a waste of our
    time and effort. What this means in practice is that rule \#1 is up
    to the author, and rule \#3 must be interpreted in that vein. If you
    **only suspect** a tool is LLM-generated and violates rule \#1, then
    downvote/ignore it and move on. **Only if** we see **blatant
    breaking of rule \#1** we will enforce it, but again we will not be
    going through code line by line playing the "was this LLM
    generated?" game. Rule \#2 will always be enforced regardless of
    LLM-ness or not.

</div>

<div class="row margin-top--sm theme-doc-footer-edit-meta-row">

<div class="col noPrint_WFHX">

<a
href="https://github.com/jellyfin/jellyfin.org/edit/master/docs/general/contributing/llm-policies.md"
class="theme-edit-this-page" target="_blank"
rel="noopener noreferrer"><img
src="data:image/svg+xml;base64,PHN2ZyBmaWxsPSJjdXJyZW50Q29sb3IiIGhlaWdodD0iMjAiIHdpZHRoPSIyMCIgdmlld2JveD0iMCAwIDQwIDQwIiBjbGFzcz0iaWNvbkVkaXRfWjlTdyIgYXJpYS1oaWRkZW49InRydWUiPjxnPjxwYXRoIGQ9Im0zNC41IDExLjdsLTMgMy4xLTYuMy02LjMgMy4xLTNxMC41LTAuNSAxLjItMC41dDEuMSAwLjVsMy45IDMuOXEwLjUgMC40IDAuNSAxLjF0LTAuNSAxLjJ6IG0tMjkuNSAxNy4xbDE4LjQtMTguNSA2LjMgNi4zLTE4LjQgMTguNGgtNi4zdi02LjJ6IiAvPjwvZz48L3N2Zz4="
class="iconEdit_Z9Sw" />Edit this page</a>

</div>

<div class="col lastUpdated_JAkA">

</div>

</div>

<a href="/docs/general/contributing/issues"
class="pagination-nav__link pagination-nav__link--prev"></a>

<div class="pagination-nav__sublabel">

Previous

</div>

<div class="pagination-nav__label">

Reporting Issues

</div>

<a href="/docs/general/contributing/release-procedure"
class="pagination-nav__link pagination-nav__link--next"></a>

<div class="pagination-nav__sublabel">

Next

</div>

<div class="pagination-nav__label">

Releases

</div>

</div>

</div>

<div class="col col--3">

<div class="tableOfContents_bqdL thin-scrollbar theme-doc-toc-desktop">

- <a href="#general-guidelines"
  class="table-of-contents__link toc-highlight">General Guidelines</a>
- <a href="#llm-code-contributions-to-official-projects"
  class="table-of-contents__link toc-highlight">LLM Code Contributions to
  Official Projects</a>
- <a href="#llm-generated-tools-clients-etc-shared-in-the-community"
  class="table-of-contents__link toc-highlight">LLM-generated Tools,
  Clients, etc. Shared in the Community</a>

</div>

</div>

</div>

</div>

</div>
