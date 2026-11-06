Menu

Expand

Light mode

Dark mode

Auto light/dark, in light mode

Auto light/dark, in dark mode

[Skip to content](#furo-main-content)

pip-tools documentation v7.6.3.dev33

[pip-tools documentation v7.6.3.dev33](../)

Contents

- [How-Tos](../how-to/)☐
  - [Customize Compiled Headers](../how-to/customize-compiled-headers/)
  - [Configure Shell Completion](../how-to/configure-completion/)
- [Reference](../reference/)☐
  - [pip-compile](../reference/pip-compile/)
  - [pip-sync](../reference/pip-sync/)
  - [Configuration](../reference/configuration/)
  - [Environment Variables](../reference/environment-variables/)
- [Contributing](#)
- [Changelog](../changelog/)

Private API reference

- [piptools](../pkg/modules/)☐
  - [piptools package](../pkg/piptools/)☐
    - [piptools.\_compat package](../pkg/piptools._compat/)☐
      - [piptools.\_compat.\_click_compat module](../pkg/piptools._compat._click_compat/)
      - [piptools.\_compat.\_tomllib_compat module](../pkg/piptools._compat._tomllib_compat/)
      - [piptools.\_compat.path_compat module](../pkg/piptools._compat.path_compat/)
      - [piptools.\_compat.pip_compat module](../pkg/piptools._compat.pip_compat/)
      - [piptools.\_compat.tempfile_compat module](../pkg/piptools._compat.tempfile_compat/)
    - [piptools.\_internal package](../pkg/piptools._internal/)☐
      - [piptools.\_internal.\_pip_api package](../pkg/piptools._internal._pip_api/)☐
        - [piptools.\_internal.\_pip_api.cli_options module](../pkg/piptools._internal._pip_api.cli_options/)
        - [piptools.\_internal.\_pip_api.command_methods module](../pkg/piptools._internal._pip_api.command_methods/)
        - [piptools.\_internal.\_pip_api.install_requirements module](../pkg/piptools._internal._pip_api.install_requirements/)
        - [piptools.\_internal.\_pip_api.package_finder module](../pkg/piptools._internal._pip_api.package_finder/)
        - [piptools.\_internal.\_pip_api.pip_version module](../pkg/piptools._internal._pip_api.pip_version/)
      - [piptools.\_internal.\_environment_variables module](../pkg/piptools._internal._environment_variables/)
      - [piptools.\_internal.\_subprocess module](../pkg/piptools._internal._subprocess/)
    - [piptools.repositories package](../pkg/piptools.repositories/)☐
      - [piptools.repositories.base module](../pkg/piptools.repositories.base/)
      - [piptools.repositories.local module](../pkg/piptools.repositories.local/)
      - [piptools.repositories.pypi module](../pkg/piptools.repositories.pypi/)
    - [piptools.scripts package](../pkg/piptools.scripts/)☐
      - [piptools.scripts.\_deprecations module](../pkg/piptools.scripts._deprecations/)
      - [piptools.scripts.compile module](../pkg/piptools.scripts.compile/)
      - [piptools.scripts.options module](../pkg/piptools.scripts.options/)
      - [piptools.scripts.sync module](../pkg/piptools.scripts.sync/)
    - [piptools.\_\_main\_\_ module](../pkg/piptools.__main__/)
    - [piptools.build module](../pkg/piptools.build/)
    - [piptools.cache module](../pkg/piptools.cache/)
    - [piptools.exceptions module](../pkg/piptools.exceptions/)
    - [piptools.locations module](../pkg/piptools.locations/)
    - [piptools.logging module](../pkg/piptools.logging/)
    - [piptools.resolver module](../pkg/piptools.resolver/)
    - [piptools.sync module](../pkg/piptools.sync/)
    - [piptools.utils module](../pkg/piptools.utils/)
    - [piptools.writer module](../pkg/piptools.writer/)

[Back to top](#)

[View this page](../_sources/contributing.md.txt "View this page")

# Contributing

Everyone interacting with and contributing to pip-tools is expected to follow the [PSF Code of Conduct](https://github.com/pypa/.github/blob/main/CODE_OF_CONDUCT.md).

## Project Contribution Guidelines

Here are a few additional or emphasized guidelines to follow when contributing to `pip-tools`:

- If you need to have a virtualenv outside of `tox`, it is possible to reuse its configuration to provision it with [tox devenv](https://tox.wiki/en/latest/reference/cli.html#tox-devenv-(d)).

- Always provide tests for your changes and run `tox``-p``all` to make sure they are passing the checks locally.

- Give a clear one-line description in the PR (that the maintainers can add to [CHANGELOG](#./CHANGELOG.md) afterwards).

- Wait for the review of at least one other contributor before merging.

- Before merging, assign the PR to a milestone for a version to help with the release process.

The only exception to those guidelines is for trivial changes, such as documentation corrections or contributions that do not change pip-tools itself.

Contributions following these guidelines are always welcomed, encouraged and appreciated.

### LLM Generated Contributions

Contributors are free to use whatever tools they like, but we have some additional guidance for LLM-assisted contributions.

When interacting in pip-tools spaces (issues, pull requests, matrix, discord, etc.), do not use LLMs to speak for you, except for translation or grammar edits. This includes the creation of changelogs and PR descriptions. Human-to-human communication is foundational to open source communities.

Caution

In extreme cases, low quality PRs may be closed as spam.

#### Responsibility

Remember that you, not the LLM, are responsible for your contributions. Be ready to discuss your changes. Do not submit code you have not reviewed.

Do your best to follow the conventions and standards of the project. Make sure your code really works. Be thoughtful about testing and documentation.

Try to make your code brief, and recognize when less is more.

#### Autonomous Code Submissions

The use of agents which write code and submit pull requests without human review is not permitted.

#### Pull Request Templates

Please do not replace the pull request template, which is part of the maintainers’ process.

### The `good``first``issue` label

The [`good`` ``first`` ``issue` label](https://github.com/pypa/pip-tools/labels/good%20first%20issue%22) is used to designate items which are being left for new contributors. They’re a great way to get onboarded into the project and learn.

Having an LLM resolve one of these issues does not help anyone learn. Therefore, please be considerate of those who may benefit from these opportunities, and refrain from asking an LLM to produce a complete solution.

## Project Release Process

Releases require approval by a member of the [`pip-tools-admins` team](https://github.com/orgs/pypa/teams/pip-tools-admins).

Commands given below may assume that your fork is named `origin` in git remotes and the main repo is named `upstream`.

This is the current release process:

- Create a branch for the release. *e.g., `release/v3.4.0`*.

- Use `towncrier` to update the [CHANGELOG](#./CHANGELOG.md), *e.g., `towncrier``build``--version``v3.4.0`*.

- Push the branch to your fork, *e.g., `git``push``-u``origin``release/v3.4.0`*, and create a pull request.

- Merge the pull request after the changes are approved.

- Make sure that the tests/CI still pass.

- Fetch the latest changes to `main` locally.

- Create an unsigned tag with the release version number prefixed with a `v`, *e.g., `git``tag``-a``v3.4.0``-m``v3.4.0`*, and push it to `upstream`.

- Create a GitHub Release, populated with a copy of the changelog and set to “Create a discussion for this release” in the `Announcements` category. Some of the markdown will need to be reformatted into GFM. The release title and tag should be the newly created tag.

- The [GitHub Release Workflow](https://github.com/pypa/pip-tools/actions/workflows/release.yml) will trigger off of the release to publish to PyPI. A member of the \[`pip-tools-leads` team\] must approve the publication step.

- Once the release to PyPI is confirmed, close the milestone.

- Publish any release notifications, *e.g., pip-tools matrix channel, discuss.python.org, bluesky, mastodon, pypa Discord*.

## Adding Change Notes with PRs

It is important to maintain a changelog to explain to users what changed between versions.

To avoid merge conflicts, we use [Towncrier](https://towncrier.readthedocs.io/en/stable/) to maintain our changelog.

Towncrier uses separate files, “news fragments”, for each pull request. On release, those fragments are compiled into the changelog.

You don’t need to install Towncrier to contribute, you just have to follow some simple rules!

- In your pull request, add a new file into `changelog.d/` with a filename formatted as `$NUMBER.$CATEGORY.md`.

  - The number is the PR number or issue number which your PR addresses.

  - The category is `bugfix`, `feature`, `deprecation`, `breaking`, `doc`, `packaging`, `contrib`, or `misc`. The maintainers may use special categories `highlights` and `afterword`, but regular contributors don’t generally need to.

  - For example, if your PR fixes bug \#404, the change notes should be named `changelog.d/404.bugfix.md`.

- If multiple issues are addressed, create a symlink to the change notes with another issue number in the name. Towncrier will automatically merge files into one entry with multiple links.

- Prefer the simple past or constructions with “now”.

- Include a byline, `--``by``` {user}`github-username` ``

You can preview the changelog by running `tox``run``-e``build-docs` and viewing the changelog in the docs.

### Categories

The categories for change notes are defined as follows.

- `bugfix`: A fix for something we deemed improper or undesired behavior.

- `feature`: A new behavior, such as a new flag or environment variable.

- `deprecation`: A declaration of future removals and breaking changes in behavior.

- `breaking`: A change in behavior which changes or violates established user expectations (e.g., removing a flag or changing output formatting).

- `doc`: Notable updates to the documentation structure or build process.

- `packaging`: Changes in how `pip-tools` itself is packaged and tested which may impact downstreams and redistributors.

- `contrib`: Changes to the contributor experience (e.g., running tests, building the docs, or setting up a development environment).

- `misc`: Changes that don’t fit any of the other categories.

- `highlights`: A prelude to the release notes. Normally filled out by the maintainers with important announcements concerning a `pip-tools` release. It is rendered before the normal change log categories.

  Important

  The file name must not reference a number but be orphan, starting with a `+`.

- `afterword`: A concluding paragraph after the release notes. May be filled out by the maintainers if they want to include additional free-form notes. It is rendered after the normal change log categories.

  Important

  The file name must not reference a number but be orphan, starting with a `+`.

Sometimes it’s not clear which category to use for a change. Do your best and a maintainer can discuss this with you during review.

### Examples

Example bugfix, [`2223.bugfix.md`](https://github.com/pypa/pip-tools/pull/2224):

    Fixed a bug which removed slashes from URLs in `-r` and `-c` in the output
    of `pip-compile` -- by {user}`sirosen`.

Example contributor update, [`2214.contrib.md`](https://github.com/pypa/pip-tools/pull/2214):

    `pip-tools` now tests on and officially supports `pip` version 25.2
    -- by {user}`sirosen`.

### Rationale

When making a change to `pip-tools`, it is important to communicate the differences that end-users will experience in a manner that they can understand.

Details of the change that are primarily of interest only to `pip-tools` developers may be irrelevant to most users, and if so, then those details can be omitted from the change notes. Then, when the maintainers publish a new release, they’ll automatically use these records to compose a change log for the respective version.

We write change notes in the past tense because this suits the users who will be reading these notes. Combined with others, the notes will be a part of the “news digest” telling the readers what **changed** in a specific version of `pip-tools` since the previous version.

This methodology has several benefits, including those covered by the [Towncrier Philosophy](https://towncrier.readthedocs.io/en/stable/#philosophy):

- Change notes separate the user-facing description of changes from the implementation details. Details go into the git history, but users aren’t expected to care about them.

- The release engineer may not have been involved in each issue and pull request. Writing the notes early in the process involves the developers in the best position to write good notes.

- Describing a change can help during code review. The reviewer can better identify which effects of a change were intentional and which were not.

Next

Changelog

Previous

Environment Variables

Copyright © The pip-tools Contributors

Made with [Sphinx](https://www.sphinx-doc.org/) and [@pradyunsg](https://pradyunsg.me)'s [Furo](https://github.com/pradyunsg/furo)

On this page

- [Contributing](#)
  - [Project Contribution Guidelines](#project-contribution-guidelines)
    - [LLM Generated Contributions](#llm-generated-contributions)
      - [Responsibility](#responsibility)
      - [Autonomous Code Submissions](#autonomous-code-submissions)
      - [Pull Request Templates](#pull-request-templates)
    - [The `good`` ``first`` ``issue` label](#the-good-first-issue-label)
  - [Project Release Process](#project-release-process)
  - [Adding Change Notes with PRs](#adding-change-notes-with-prs)
    - [Categories](#categories)
    - [Examples](#examples)
    - [Rationale](#rationale)
