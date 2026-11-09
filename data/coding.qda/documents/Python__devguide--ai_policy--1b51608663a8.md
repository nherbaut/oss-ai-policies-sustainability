Menu

Expand

Light mode

Dark mode

Auto light/dark, in light mode

Auto light/dark, in dark mode

[Skip to content](#furo-main-content)

Python Developer's Guide

![Logo](../../_static/python-logo.svg)

Python Developer's Guide

- [Getting started](../)☒
  - [Quick reference](../quick-reference/)
  - [Setup and building](../setup-building/)
  - [Fixing “easy” issues (and beyond)](../fixing-issues/)
  - [Git bootcamp and cheat sheet](../git-boot-camp/)
  - [Lifecycle of a pull request](../pull-request-lifecycle/)
  - [Where to get help](../getting-help/)
  - [Guidelines for using AI tools](#)
- [Development workflow](../../developer-workflow/)☐
  - [Following Python’s development](../../developer-workflow/communication-channels/)
  - [Changing Python](../../developer-workflow/lang-changes/)
  - [Development cycle](../../developer-workflow/development-cycle/)
  - [Adding to the stdlib](../../developer-workflow/stdlib/)
  - [Standard library extension modules](../../developer-workflow/extension-modules/)
  - [Changing Python’s C API](../../developer-workflow/c-api/)
  - [Changing CPython’s grammar](../../developer-workflow/grammar/)
  - [Porting and platform support](../../developer-workflow/porting/)
- [Issues and triaging](../../triage/)☐
  - [Using the issue tracker](../../triage/issue-tracker/)
  - [Triaging an issue](../../triage/triaging/)
  - [GitHub labels](../../triage/labels/)
  - [Triage Team](../../triage/triage-team/)
- [Documentation](../../documentation/)☐
  - [Getting started](../../documentation/start-documenting/)
  - [Helping with documentation](../../documentation/help-documenting/)
  - [Style guide](../../documentation/style-guide/)
  - [reStructuredText markup](../../documentation/markup/)
  - [Translations](../../documentation/translations/)☐
    - [Translating](../../documentation/translations/translating/)
    - [Coordinating](../../documentation/translations/coordinating/)
  - [Helping with the Developer’s Guide](../../documentation/devguide/)
- [Testing and buildbots](../../testing/)☐
  - [Running and writing tests](../../testing/run-write-tests/)
  - [Silence warnings from the test suite](../../testing/silence-warnings/)
  - [Increase test coverage](../../testing/coverage/)
  - [OSS-Fuzz for CPython](../../testing/oss-fuzz/)
  - [Working with buildbots](../../testing/buildbots/)
  - [New buildbot workers](../../testing/new-buildbot-worker/)
- [Development tools](../../development-tools/)☐
  - [Argument Clinic](../../development-tools/clinic/)☐
    - [Tutorial](../../development-tools/clinic/tutorial/)
    - [How-to guides](../../development-tools/clinic/howto/)
  - [GDB support](../../development-tools/gdb/)
  - [Sanitizers](../../development-tools/sanitizers/)
  - [Tools for tracking compiler warnings](../../development-tools/warnings/)
- [Core team](../../core-team/)☐
  - [Responsibilities](../../core-team/responsibilities/)
  - [Accepting pull requests](../../core-team/committing/)
  - [Experts index](../../core-team/experts/)
  - [Team log](../../core-team/team-log/)
  - [Motivations and affiliations](../../core-team/motivations/)
  - [How to join the core team](../../core-team/join-team/)
  - [Memorialization](../../core-team/memorialization/)
- [Security](../../security/)☐
  - [Security policy](../../security/policy/)
  - [Python Security Response Team (PSRT)](../../security/psrt/)
  - [Software Bill-of-Materials (SBOM)](../../security/sbom/)
- [CPython’s internals](../../internals/)
- [Status of Python versions](../../versions/)

[Back to top](#)

[View this page](https://github.com/python/devguide/blob/main/getting-started/ai-tools.rst?plain=true "View this page")

[Edit this page](https://github.com/python/devguide/edit/main/getting-started/ai-tools.rst "Edit this page")

# Guidelines for using AI tools

The person submitting an issue or PR is responsible for its content, regardless of whether AI tools were used in its creation. Generative AI tools can produce output quickly, but discretion, good judgment, and critical thinking are the foundation of all good contributions. We value good code, concise accurate documentation, and well scoped PRs without unneeded code churn.

## Considerations for success

Authors must review the work done by AI tooling in detail to ensure it actually makes sense before proposing it as a PR or filing it as an issue.

We expect PR authors and those filing issues to be able to explain their proposed changes in their own words.

Disclosure of the use of AI tools in the PR description is appreciated, while not required. Be prepared to explain how the tool was used and what changes it made.

Whether you are using AI tools or not, keep the following principles in mind for the quality of your contribution:

- Consider whether the change is necessary

- Make minimal, focused changes

- Follow existing coding style and patterns

- Write tests that exercise the change

- Keep backwards compatibility with prior releases in mind. Existing tests may be ensuring specific API behaviors are maintained.

Pay close attention to AI generated recommendations for testing changes. Provide input about Python’s testing principles when guiding an AI model. Always review the output before opening a pull request or issue, including proposed PR or issue titles and descriptions.

## Acceptable uses

Some of the acceptable uses of generative AI include:

- Assistance with writing comments, especially in a non-native language

- Gaining understanding of existing code

- Supplementing contributor knowledge for code, tests, and documentation

## Unacceptable uses

Maintainers may close issues and PRs that are not useful or productive, without explanation, regardless of whether AI tools were used or not.

If a contributor repeatedly opens unproductive issues or PRs, they may be blocked from contributing to the project because it is disruptive and disrespectful of the maintainers time.

It is not acceptable to alter or bypass existing tests, or remove desired functionality, in order to make a failing test pass. Such changes are not a real fix.

## How these guidelines are applied

Using AI tools is not a reason on its own for an issue or PR to be labeled or closed. When a maintainer thinks an issue or PR does not follow these guidelines, they may apply one of the following labels. A bot then posts a comment that links to this page.

- [AI-needs-explanation](https://github.com/python/cpython/labels/AI-needs-explanation): the issue or PR stays open. Reply in your own words: explain what the change does or what the issue is about, and describe how you checked that it is correct.

- [AI-guidelines-not-met](https://github.com/python/cpython/labels/AI-guidelines-not-met): the issue or PR is closed. If you think we misunderstood your contribution, reply on the issue or PR. You are welcome to explain your approach or ask questions about these guidelines.

Next

Development workflow

Previous

Where to get help

Copyright © 2011 Python Software Foundation

Made with [Sphinx](https://www.sphinx-doc.org/) and [@pradyunsg](https://pradyunsg.me)'s [Furo](https://github.com/pradyunsg/furo)

Last updated on Oct 28, 2026

On this page

- [Guidelines for using AI tools](#)
  - [Considerations for success](#considerations-for-success)
  - [Acceptable uses](#acceptable-uses)
  - [Unacceptable uses](#unacceptable-uses)
  - [How these guidelines are applied](#how-these-guidelines-are-applied)
