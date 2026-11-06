[![Oxc logo](https://oxc.rs/oxc-dark.svg)](https://oxc.rs)  

[![MIT licensed](https://img.shields.io/badge/license-MIT-blue.svg)](https://github.com/oxc-project/oxc/blob/main/LICENSE) [![Build Status](https://github.com/oxc-project/oxc/actions/workflows/ci.yml/badge.svg?event=push&branch=main)](https://github.com/oxc-project/oxc/actions/workflows/ci.yml?query=event%3Apush+branch%3Amain) [![Code Coverage](https://codecov.io/gh/oxc-project/oxc/graph/badge.svg?token=FVHEH0BQLJ)](https://codecov.io/gh/oxc-project/oxc) [![CodSpeed Badge](https://img.shields.io/endpoint?url=https://codspeed.io/badge.json)](https://codspeed.io/oxc-project/oxc) [![Sponsors](https://img.shields.io/github/sponsors/Boshen)](https://github.com/sponsors/Boshen)

[![Discord chat](https://img.shields.io/discord/1079625926024900739?logo=discord&label=Discord)](https://discord.gg/9uXCAwqQZW) [![Playground](https://img.shields.io/badge/Playground-blue?color=9BE4E0)](https://playground.oxc.rs/) [![Website](https://img.shields.io/badge/Website-blue)](https://oxc.rs)

## ⚓ Oxc

*/oʊ ɛks siː/*

The Oxidation Compiler is a collection of high-performance tools for JavaScript and TypeScript written in Rust.

Oxc is part of [VoidZero](https://voidzero.dev/)'s vision for a unified, high-performance toolchain for JavaScript. It powers [Rolldown](https://rolldown.rs) ([Vite](https://vite.dev/)'s bundler) and enables the next generation of ultra-fast development tools that work seamlessly together.

For more information, check out our website at [oxc.rs](https://oxc.rs).

_(\* Oxidation is the chemical process that creates rust)

## 🙋 Who's using Oxc?

[Rolldown](https://rolldown.rs) and [Nuxt](https://nuxt.com/) use Oxc for parsing. [Rolldown](https://rolldown.rs) also uses Oxc for transformation and minification. [Nova](https://trynova.dev/), [swc-node](https://github.com/swc-project/swc-node), and [knip](https://github.com/webpro/knip) use [oxc_resolver](https://docs.rs/oxc_resolver) for module resolution. [Preact](https://preactjs.com/), [Shopify](https://shopify.com/), [ByteDance](https://www.bytedance.com/), and [Shopee](https://shopee.com/) use oxlint for linting.

[See more projects using Oxc →](https://oxc.rs/docs/guide/projects.html)

## 🔧 Lint or Format a Codebase

- **Lint**: [Oxlint](https://oxc.rs/docs/guide/usage/linter) — `npx oxlint@latest`
- **Format**: [Oxfmt](https://oxc.rs/docs/guide/usage/formatter) — `npx oxfmt@latest`

## 🧰 Build Tooling on Top of Oxc

- Parse JavaScript and TypeScript: [Parser](https://oxc.rs/docs/guide/usage/parser)
- Transform TypeScript, JSX, and modern JavaScript: [Transformer](https://oxc.rs/docs/guide/usage/transformer)
- Minify JavaScript for production builds: [Minifier](https://oxc.rs/docs/guide/usage/minifier)
- Resolve modules for JavaScript and TypeScript: [Resolver](https://oxc.rs/docs/guide/usage/resolver)

## ✍️ Contribute

Check out some of the [good first issues](https://github.com/oxc-project/oxc/contribute) or ask us on [Discord](https://discord.gg/9uXCAwqQZW).

See [CONTRIBUTING.md](./CONTRIBUTING.md) for guidance, or read the complete [contributing guide on our website →](https://oxc.rs/docs/contribute/introduction.html)

If you are unable to contribute by code, you can still participate by:

- Add a [GitHub Star](https://github.com/oxc-project/oxc/stargazers) to the project
- Join us on [Discord](https://discord.gg/9uXCAwqQZW)
- [Follow me on X](https://x.com/boshen_c) and post about this project

## 📚 Other Resources

- [Troubleshooting](https://oxc.rs/docs/guide/troubleshooting)
- [Benchmarks](https://oxc.rs/docs/guide/benchmarks)
- [Talks and media](https://oxc.rs/docs/guide/media)
- [Team](https://oxc.rs/team)
- [Endorsements](https://oxc.rs/endorsements)
- [Releases](https://github.com/oxc-project/oxc/releases)

## ❤ Who's [Sponsoring Oxc](https://github.com/sponsors/Boshen)?

[![My sponsors](https://raw.githubusercontent.com/Boshen/sponsors/main/sponsors.svg)](https://github.com/sponsors/Boshen)

## 📖 License

Oxc is free and open-source software licensed under the [MIT License](./LICENSE).

Thank you to [namespace.so](https://namespace.so) for powering our CI/CD pipelines with fast, free macOS and Linux runners.

Oxc ports or copies code from other open source projects, their licenses are listed in [**Third-party library licenses**](./THIRD-PARTY-LICENSE).
