![Shows the banner of Biome, with its logo and the phrase 'Biome - Toolchain of the web'.](https://raw.githubusercontent.com/biomejs/resources/main/svg/slogan-light-transparent.svg)

[![CI on main](https://github.com/biomejs/biome/actions/workflows/main.yml/badge.svg)](https://github.com/biomejs/biome/actions/workflows/main.yml) [![Discord chat](https://badgen.net/discord/online-members/BypW39g6Yc?icon=discord&label=discord&color=60a5fa)](https://biomejs.dev/chat) [![npm version](https://npmx.dev/api/registry/badge/version/@biomejs/biome?color=60a5fa&style=shieldsio&label=%40biomejs%2Fbiome)](https://npmx.dev/package/@biomejs/biome) [![VSCode version](https://img.shields.io/visual-studio-marketplace/v/biomejs.biome?label=Visual%20Studio%20Marketplace&labelColor=374151&color=60a5fa)](https://marketplace.visualstudio.com/items?itemName=biomejs.biome) [![Open VSX version](https://img.shields.io/visual-studio-marketplace/v/biomejs.biome?label=Open%20VSX%20Registry&logo=data:image/svg+xml;base64,PD94bWwgdmVyc2lvbj0iMS4wIiBlbmNvZGluZz0idXRmLTgiPz4KPHN2ZyB2aWV3Qm94PSI0LjYgNSA5Ni4yIDEyMi43IiB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciPgogIDxwYXRoIGQ9Ik0zMCA0NC4yTDUyLjYgNUg3LjN6TTQuNiA4OC41aDQ1LjNMMjcuMiA0OS40em01MSAwbDIyLjYgMzkuMiAyMi42LTM5LjJ6IiBmaWxsPSIjYzE2MGVmIi8+CiAgPHBhdGggZD0iTTUyLjYgNUwzMCA0NC4yaDQ1LjJ6TTI3LjIgNDkuNGwyMi43IDM5LjEgMjIuNi0zOS4xem01MSAwTDU1LjYgODguNWg0NS4yeiIgZmlsbD0iI2E2MGVlNSIvPgo8L3N2Zz4=&labelColor=374151&color=60a5fa)](https://open-vsx.org/extension/biomejs/biome)

[हिन्दी](https://github.com/biomejs/biome/blob/main/packages/%40biomejs/biome/README.hi.md) \| English \| [Español](https://github.com/biomejs/biome/blob/main/packages/%40biomejs/biome/README.es.md) \| [Français](https://github.com/biomejs/biome/blob/main/packages/%40biomejs/biome/README.fr.md) \| [繁體中文](https://github.com/biomejs/biome/blob/main/packages/%40biomejs/biome/README.zh-TW.md) \| [简体中文](https://github.com/biomejs/biome/blob/main/packages/%40biomejs/biome/README.zh-CN.md) \| [日本語](https://github.com/biomejs/biome/blob/main/packages/%40biomejs/biome/README.ja.md) \| [Polski](https://github.com/biomejs/biome/blob/main/packages/%40biomejs/biome/README.pl.md) \| [Português do Brasil](https://github.com/biomejs/biome/blob/main/packages/%40biomejs/biome/README.pt-BR.md) \| [한국어](https://github.com/biomejs/biome/blob/main/packages/%40biomejs/biome/README.kr.md) \| [Русский](https://github.com/biomejs/biome/blob/main/packages/%40biomejs/biome/README.ru.md) \| [Українська](https://github.com/biomejs/biome/blob/main/packages/%40biomejs/biome/README.uk.md)

**Biome** is a performant toolchain for web projects, it aims to provide developer tools to maintain the health of said projects.

**Biome is a [fast formatter](https://github.com/biomejs/benchmark#formatting)** for *JavaScript*, *TypeScript*, *JSX*, *JSON*, *CSS* and *GraphQL* that scores **[97% compatibility with *Prettier*](https://algora.io/challenges/prettier)**.

**Biome is a [performant linter](https://github.com/biomejs/benchmark#linting)** for *JavaScript*, *TypeScript*, *JSX*, *JSON*, *CSS*, and *GraphQL* that features **[more than 500 rules](https://biomejs.dev/linter/javascript/rules/)** from ESLint, typescript-eslint, and [other sources](https://github.com/biomejs/biome/discussions/3). It **outputs detailed and contextualized diagnostics** that help you to improve your code and become a better programmer!

**Biome** is designed from the start to be used [interactively within an editor](https://biomejs.dev/editors/first-party-extensions/). It can format and lint malformed code as you are writing it.

### Installation

``` shell
npm install --save-dev --save-exact @biomejs/biome
```

### Usage

``` shell
# format files
npx @biomejs/biome format --write

# lint files and apply the safe fixes
npx @biomejs/biome lint --write

# run format, lint, etc. and apply the safe fixes
npx @biomejs/biome check --write

# check all files against format, lint, etc. in CI environments
npx @biomejs/biome ci
```

If you want to give Biome a run without installing it, use the [online playground](https://biomejs.dev/playground/), compiled to WebAssembly.

## Documentation

Check out our [homepage](https://biomejs.dev/) to learn more about Biome, or directly head to the [Getting Started guide](https://biomejs.dev/guides/getting-started/) to start using Biome.

## More about Biome

**Biome** has sane defaults and it doesn't require configuration.

**Biome** aims to support [all main languages](https://biomejs.dev/internals/language-support/) of modern web development.

**Biome** [doesn't require Node.js](https://biomejs.dev/guides/manual-installation/) to function.

**Biome** has first-class LSP support, with a sophisticated parser that represents the source text in full fidelity and top-notch error recovery.

**Biome** wants to offer a high-quality *Developer Experience*, with descriptive diagnostics and great performance.

**Biome** unifies functionalities that have previously been separate tools. Building upon a shared base allows us to provide a cohesive experience for processing code, displaying errors, parallelize work, caching, and configuration.

Read more about our [project philosophy](https://biomejs.dev/internals/philosophy/).

**Biome** is [MIT licensed](https://github.com/biomejs/biome/tree/main/LICENSE-MIT) or [Apache 2.0 licensed](https://github.com/biomejs/biome/tree/main/LICENSE-APACHE) and moderated under the [Contributor Covenant Code of Conduct](https://github.com/biomejs/biome/tree/main/CODE_OF_CONDUCT.md).

## Funding

You can fund the project in different ways

### Project sponsorship and funding

You can sponsor or fund the project via [Open collective](https://opencollective.com/biome) or [GitHub sponsors](https://github.com/sponsors/biomejs)

Biome offers a simple sponsorship program that allows companies to get visibility and recognition among various developers.

Biome offers [enterprise support](https://biomejs.dev/enterprise), where Core Contributors can be employed to work on company-focused projects.

## Sponsors

### Platinum Sponsors

|  |
|:--:|
| ![Depot logo](https://depot.dev/assets/brand/1693758816/depot-logo-horizontal-on-light@3x.png) |

### Silver Sponsors

|  |  |
|:--:|:--:|
| [![Lokalise logo](https://avatars.githubusercontent.com/u/14294501?s=200&v=4)](https://lokalise.com/?utm_source=biome&utm_medium=readme) | [![Latitude logo](https://avatars.githubusercontent.com/u/98949449?s=200&v=4)](https://latitude.so/?utm_source=biome&utm_medium=readme) |

### Bronze Sponsors

|  |  |  |  |  |  |  |  |  |  |
|:--:|:--:|:--:|:--:|:--:|:--:|:--:|:--:|:--:|:--:|
| [![Vital logo](https://avatars.githubusercontent.com/u/25357309?s=200)](https://vital.io/?utm_source=biome&utm_medium=readme) | [![CodeRabbit logo](https://avatars.githubusercontent.com/u/132028505?s=200&v=4)](https://coderabbit.ai/?utm_source=biome&utm_medium=readme) | [![Forge42 logo](https://avatars.githubusercontent.com/u/161314831?s=200&v=4)](https://forge42.dev/?utm_source=biome&utm_medium=readme) | [![RStudio logo](https://avatars.githubusercontent.com/u/513560?s=200&v=4)](http://rstudio.org/?utm_source=biome&utm_medium=readme) | [![Pennylane logo](https://avatars.githubusercontent.com/u/57875210?s=200&v=4)](https://pennylane.com/?utm_source=biome&utm_medium=readme) | [![JetBrains logo](https://resources.jetbrains.com/storage/products/company/brand/logos/jetbrains.png)](https://jetbrains.com/?utm_source=biome&utm_medium=readme) | [![EGSTOCK, Inc. logo](https://images.opencollective.com/egstock/b18c836/logo/256.png?height=256)](https://www.egstock.co.jp/?utm_source=biome&utm_medium=readme) | [![Convex logo](https://avatars.githubusercontent.com/u/81530787?s=200&v=4)](https://www.convex.dev/?utm_source=biome&utm_medium=readme) | [![Graphite logo](https://avatars.githubusercontent.com/u/61942612?s=200&v=4)](https://graphite.dev/?utm_source=biome&utm_medium=readme) | [![Kraken Tech logo](https://avatars.githubusercontent.com/u/105941848?s=200&v=4)](https://kraken.tech/?utm_source=biome&utm_medium=readme) |
