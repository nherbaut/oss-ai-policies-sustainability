[![npm version](https://img.shields.io/npm/v/eslint.svg)](https://www.npmjs.com/package/eslint) [![Downloads](https://img.shields.io/npm/dm/eslint.svg)](https://www.npmjs.com/package/eslint) [![Build Status](https://github.com/eslint/eslint/workflows/CI/badge.svg)](https://github.com/eslint/eslint/actions)  
[![Open Collective Backers](https://img.shields.io/opencollective/backers/eslint)](https://opencollective.com/eslint) [![Open Collective Sponsors](https://img.shields.io/opencollective/sponsors/eslint)](https://opencollective.com/eslint)

# ESLint

[Website](https://eslint.org) \| [Configure ESLint](https://eslint.org/docs/latest/use/configure) \| [Rules](https://eslint.org/docs/rules/) \| [Contribute to ESLint](https://eslint.org/docs/latest/contribute) \| [Report Bugs](https://eslint.org/docs/latest/contribute/report-bugs) \| [Code of Conduct](https://eslint.org/conduct) \| [X](https://x.com/geteslint) \| [Discord](https://eslint.org/chat) \| [Mastodon](https://fosstodon.org/@eslint) \| [Bluesky](https://bsky.app/profile/eslint.org)

ESLint is a tool for identifying and reporting on patterns found in ECMAScript/JavaScript code. In many ways, it is similar to JSLint and JSHint with a few exceptions:

- ESLint uses [Espree](https://github.com/eslint/js/tree/main/packages/espree) for JavaScript parsing.
- ESLint uses an AST to evaluate patterns in code.
- ESLint is completely pluggable, every single rule is a plugin and you can add more at runtime.

## Table of Contents

1.  [Installation and Usage](#installation-and-usage)
2.  [Configuration](#configuration)
3.  [Version Support](#version-support)
4.  [Code of Conduct](#code-of-conduct)
5.  [Filing Issues](#filing-issues)
6.  [Frequently Asked Questions](#frequently-asked-questions)
7.  [Releases](#releases)
8.  [Security Policy](#security-policy)
9.  [Semantic Versioning Policy](#semantic-versioning-policy)
10. [ESM Dependencies](#esm-dependencies)
11. [License](#license)
12. [Team](#team)
13. [Sponsors](#sponsors)
14. [Technology Sponsors](#technology-sponsors)

## Installation and Usage

### Prerequisites

To use ESLint, you must have [Node.js](https://nodejs.org/) (`^20.19.0`, `^22.13.0`, or `>=24`) installed and built with SSL and ICU support. (If you are using an official Node.js distribution, both SSL and ICU are always built in.)

If you use ESLint's TypeScript type definitions, TypeScript 5.3 or later is required.

### npm Installation

You can install and configure ESLint using this command:

``` shell
npm init @eslint/config@latest
```

After that, you can run ESLint on any file or directory like this:

``` shell
npx eslint yourfile.js
```

### pnpm Installation

To use ESLint with pnpm, we recommend setting up a `.npmrc` file with at least the following settings:

``` text
auto-install-peers=true
node-linker=hoisted
```

This ensures that pnpm installs dependencies in a way that is more compatible with npm and is less likely to produce errors.

## Configuration

You can configure rules in your `eslint.config.js` files as in this example:

``` js
import { defineConfig } from "eslint/config";

export default defineConfig([
    {
        files: ["**/*.js", "**/*.cjs", "**/*.mjs"],
        rules: {
            "prefer-const": "warn",
            "no-constant-binary-expression": "error",
        },
    },
]);
```

The names `"prefer-const"` and `"no-constant-binary-expression"` are the names of [rules](https://eslint.org/docs/rules) in ESLint. The first value is the error level of the rule and can be one of these values:

- `"off"` or `0` - turn the rule off
- `"warn"` or `1` - turn the rule on as a warning (doesn't affect exit code)
- `"error"` or `2` - turn the rule on as an error (exit code will be 1)

The three error levels allow you fine-grained control over how ESLint applies rules (for more configuration options and details, see the [configuration docs](https://eslint.org/docs/latest/use/configure)).

## Version Support

The ESLint team provides ongoing support for the current version and six months of limited support for the previous version. Limited support includes critical bug fixes, security issues, and compatibility issues only.

ESLint offers commercial support for both current and previous versions through our partners, [Tidelift](https://tidelift.com/funding/github/npm/eslint) and [HeroDevs](https://www.herodevs.com/support/eslint-nes?utm_source=ESLintWebsite&utm_medium=ESLintWebsite&utm_campaign=ESLintNES&utm_id=ESLintNES).

See [Version Support](https://eslint.org/version-support) for more details.

## Code of Conduct

ESLint adheres to the [OpenJS Foundation Code of Conduct](https://eslint.org/conduct).

## Filing Issues

Before filing an issue, please be sure to read the guidelines for what you're reporting:

- [Bug Report](https://eslint.org/docs/latest/contribute/report-bugs)
- [Propose a New Rule](https://eslint.org/docs/latest/contribute/propose-new-rule)
- [Proposing a Rule Change](https://eslint.org/docs/latest/contribute/propose-rule-change)
- [Request a Change](https://eslint.org/docs/latest/contribute/request-change)

## Frequently Asked Questions

### Does ESLint support JSX?

Yes, ESLint natively supports parsing JSX syntax (this must be enabled in [configuration](https://eslint.org/docs/latest/use/configure)). Please note that supporting JSX syntax *is not* the same as supporting React. React applies specific semantics to JSX syntax that ESLint doesn't recognize. We recommend using [eslint-plugin-react](https://www.npmjs.com/package/eslint-plugin-react) if you are using React and want React semantics.

### Does Prettier replace ESLint?

No, ESLint and Prettier have different jobs: ESLint is a linter (looking for problematic patterns) and Prettier is a code formatter. Using both tools is common, refer to [Prettier's documentation](https://prettier.io/docs/en/install#eslint-and-other-linters) to learn how to configure them to work well with each other.

### What ECMAScript versions does ESLint support?

ESLint has full support for ECMAScript 3, 5, and every year from 2015 up until the most recent stage 4 specification (the default). You can set your desired ECMAScript syntax and other settings (like global variables) through [configuration](https://eslint.org/docs/latest/use/configure).

### What about experimental features?

ESLint's parser only officially supports the latest final ECMAScript standard. We will make changes to core rules in order to avoid crashes on stage 3 ECMAScript syntax proposals (as long as they are implemented using the correct experimental ESTree syntax). We may make changes to core rules to better work with language extensions (such as JSX, Flow, and TypeScript) on a case-by-case basis.

In other cases (including if rules need to warn on more or fewer cases due to new syntax, rather than just not crashing), we recommend you use other parsers and/or rule plugins. If you are using Babel, you can use [@babel/eslint-parser](https://www.npmjs.com/package/@babel/eslint-parser) and [@babel/eslint-plugin](https://www.npmjs.com/package/@babel/eslint-plugin) to use any option available in Babel.

Once a language feature has been adopted into the ECMAScript standard (stage 4 according to the [TC39 process](https://tc39.github.io/process-document/)), we will accept issues and pull requests related to the new feature, subject to our [contributing guidelines](https://eslint.org/docs/latest/contribute). Until then, please use the appropriate parser and plugin(s) for your experimental feature.

### Which Node.js versions does ESLint support?

ESLint updates the supported Node.js versions with each major release of ESLint. At that time, ESLint's supported Node.js versions are updated to be:

1.  The most recent maintenance release of Node.js
2.  The lowest minor version of the Node.js LTS release that includes the features the ESLint team wants to use.
3.  The Node.js Current release

ESLint is also expected to work with Node.js versions released after the Node.js Current release.

Refer to the [Quick Start Guide](https://eslint.org/docs/latest/use/getting-started#prerequisites) for the officially supported Node.js versions for a given ESLint release.

### Where to ask for help?

Open a [discussion](https://github.com/eslint/eslint/discussions) or stop by our [Discord server](https://eslint.org/chat).

### Why doesn't ESLint lock dependency versions?

Lock files like `package-lock.json` are helpful for deployed applications. They ensure that dependencies are consistent between environments and across deployments.

Packages like `eslint` that get published to the npm registry do not include lock files. `npm install eslint` as a user will respect version constraints in ESLint's `package.json`. ESLint and its dependencies will be included in the user's lock file if one exists, but ESLint's own lock file would not be used.

We intentionally don't lock dependency versions so that we have the latest compatible dependency versions in development and CI that our users get when installing ESLint in a project.

The Twilio blog has a [deeper dive](https://www.twilio.com/blog/lockfiles-nodejs) to learn more.

## Releases

We have scheduled releases every two weeks on Friday or Saturday. You can follow a [release issue](https://github.com/eslint/eslint/issues?q=is%3Aopen+is%3Aissue+label%3Arelease) for updates about the scheduling of any particular release.

## Security Policy

ESLint takes security seriously. We work hard to ensure that ESLint is safe for everyone and that security issues are addressed quickly and responsibly. Read the full [security policy](https://github.com/eslint/.github/blob/master/SECURITY.md).

## Semantic Versioning Policy

ESLint follows [semantic versioning](https://semver.org). However, due to the nature of ESLint as a code quality tool, it's not always clear when a minor or major version bump occurs. To help clarify this for everyone, we've defined the following semantic versioning policy for ESLint:

- Patch release (intended to not break your lint build)
  - A bug fix in a rule that results in ESLint reporting fewer linting errors.
  - A bug fix to the CLI or core (including formatters).
  - Improvements to documentation.
  - Non-user-facing changes such as refactoring code, adding, deleting, or modifying tests, and increasing test coverage.
  - Re-releasing after a failed release (i.e., publishing a release that doesn't work for anyone).
- Minor release (might break your lint build)
  - A bug fix that results in ESLint reporting more linting errors (e.g., fixing false negatives in a core rule, or linting additional files that were previously incorrectly skipped).
  - A new rule is created.
  - A new option to an existing rule that does not result in ESLint reporting more linting errors by default.
  - A new addition to an existing rule to support a newly-added language feature (within the last 12 months) that will result in ESLint reporting more linting errors by default.
  - An existing rule is deprecated.
  - A new CLI capability is created.
  - New capabilities to the public API are added (new classes, new methods, new arguments to existing methods, etc.).
  - A new formatter is created.
  - `eslint:recommended` is updated and will result in strictly fewer linting errors (e.g., rule removals).
- Major release (likely to break your lint build)
  - `eslint:recommended` is updated and may result in new linting errors (e.g., rule additions, most rule option updates).
  - A new option to an existing rule that results in ESLint reporting more linting errors by default.
  - An existing formatter is removed.
  - Part of the public API is removed or changed in an incompatible way. The public API includes:
    - Rule schemas
    - Configuration schema
    - Command-line options
    - Node.js API
    - Rule, formatter, parser, plugin APIs

According to our policy, any minor update may report more linting errors than the previous release (ex: from a bug fix). As such, we recommend using the tilde (`~`) in `package.json` e.g. `"eslint": "~3.1.0"` to guarantee the results of your builds.

## ESM Dependencies

Since ESLint is a CommonJS package, there are restrictions on which ESM-only packages can be used as dependencies.

Packages that are controlled by the ESLint team and have no external dependencies can be safely loaded synchronously using [`require(esm)`](https://nodejs.org/api/modules.html#loading-ecmascript-modules-using-require) and therefore used in any contexts.

For external packages, we don't use `require(esm)` because a package could add a top-level `await` and thus break ESLint. We can use an external ESM-only package only in case it is needed only in asynchronous code, in which case it can be loaded using dynamic `import()`.

These policies don't apply to packages intended for our own usage only, such as `eslint-config-eslint`.

## License

MIT License

Copyright OpenJS Foundation and other contributors, \<www.openjsf.org\>

Permission is hereby granted, free of charge, to any person obtaining a copy of this software and associated documentation files (the "Software"), to deal in the Software without restriction, including without limitation the rights to use, copy, modify, merge, publish, distribute, sublicense, and/or sell copies of the Software, and to permit persons to whom the Software is furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM, OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE SOFTWARE.

## Team

These folks keep the project moving and are resources for help.

### Technical Steering Committee (TSC)

The people who manage releases, review feature requests, and meet regularly to ensure ESLint is properly maintained.

[![Nicholas C. Zakas's Avatar](https://github.com/nzakas.png?s=75)  
Nicholas C. Zakas](https://github.com/nzakas)

[![Francesco Trotta's Avatar](https://github.com/fasttime.png?s=75)  
Francesco Trotta](https://github.com/fasttime)

[![Milos Djermanovic's Avatar](https://github.com/mdjermanovic.png?s=75)  
Milos Djermanovic](https://github.com/mdjermanovic)

### Reviewers

The people who review and implement new features.

[![唯然's Avatar](https://github.com/aladdin-add.png?s=75)  
唯然](https://github.com/aladdin-add)

[![Nitin Kumar's Avatar](https://github.com/snitin315.png?s=75)  
Nitin Kumar](https://github.com/snitin315)

### Committers

The people who review and fix bugs and help triage issues.

[![fnx's Avatar](https://github.com/DMartens.png?s=75)  
fnx](https://github.com/DMartens)

[![Josh Goldberg ✨'s Avatar](https://github.com/JoshuaKGoldberg.png?s=75)  
Josh Goldberg ✨](https://github.com/JoshuaKGoldberg)

[![Sweta Tanwar's Avatar](https://github.com/SwetaTanwar.png?s=75)  
Sweta Tanwar](https://github.com/SwetaTanwar)

[![Tanuj Kanti's Avatar](https://github.com/Tanujkanti4441.png?s=75)  
Tanuj Kanti](https://github.com/Tanujkanti4441)

[![lumir's Avatar](https://github.com/lumirlumir.png?s=75)  
lumir](https://github.com/lumirlumir)

[![Pixel's Avatar](https://github.com/Pixel998.png?s=75)  
Pixel](https://github.com/Pixel998)

### Website Team

Team members who focus specifically on eslint.org

[![Amaresh S M's Avatar](https://github.com/amareshsm.png?s=75)  
Amaresh S M](https://github.com/amareshsm)

[![Harish's Avatar](https://github.com/harish-sethuraman.png?s=75)  
Harish](https://github.com/harish-sethuraman)

[![Percy Ma's Avatar](https://github.com/kecrily.png?s=75)  
Percy Ma](https://github.com/kecrily)

## Sponsors

The following companies, organizations, and individuals support ESLint's ongoing maintenance and development. [Become a Sponsor](https://eslint.org/donate) to get your logo on our READMEs and [website](https://eslint.org/sponsors).

### Platinum Sponsors

[![Automattic](https://images.opencollective.com/automattic/d0ef3e1/logo.png)](https://automattic.com)

### Gold Sponsors

[![Qlty Software](https://images.opencollective.com/qltysh/33d157d/logo.png)](https://qlty.sh/) [![Shopify](https://avatars.githubusercontent.com/u/8085)](https://shopify.engineering/) [![CodeRabbit](https://avatars.githubusercontent.com/u/132028505)](https://www.coderabbit.ai/?utm_source=cr_org&utm_medium=github)

### Silver Sponsors

[![Vite](https://images.opencollective.com/vite/d472863/logo.png)](https://vite.dev/) [![Liftoff](https://images.opencollective.com/liftoff/2d6c3b6/logo.png)](https://liftoff.io/) [![StackBlitz](https://avatars.githubusercontent.com/u/28635252)](https://stackblitz.com)

### Bronze Sponsors

[![Cybozu](https://images.opencollective.com/cybozu/933e46d/logo.png)](https://cybozu.co.jp/) [![SAP](https://avatars.githubusercontent.com/u/2531208)](https://opensource.sap.com) [![Syntax](https://github.com/syntaxfm.png)](https://syntax.fm) [![Icons8](https://images.opencollective.com/icons8/7fa1641/logo.png)](https://icons8.com/) [![Discord](https://images.opencollective.com/discordapp/f9645d9/logo.png)](https://discord.com) [![GitBook](https://avatars.githubusercontent.com/u/7111340)](https://www.gitbook.com) [![Citadel AI](https://avatars.githubusercontent.com/u/75781367)](https://citadel-ai.com)

### Technology Sponsors

Technology sponsors allow us to use their products and services for free as part of a contribution to the open source ecosystem and our work.

[![Netlify](https://raw.githubusercontent.com/eslint/eslint.org/main/src/assets/images/techsponsors/netlify-icon.svg)](https://netlify.com) [![Algolia](https://raw.githubusercontent.com/eslint/eslint.org/main/src/assets/images/techsponsors/algolia-icon.svg)](https://algolia.com) [![1Password](https://raw.githubusercontent.com/eslint/eslint.org/main/src/assets/images/techsponsors/1password-icon.svg)](https://1password.com)
