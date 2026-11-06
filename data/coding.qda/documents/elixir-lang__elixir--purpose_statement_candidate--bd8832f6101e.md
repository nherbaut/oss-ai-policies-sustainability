# ![Elixir logo](https://github.com/elixir-lang/elixir-lang.github.com/raw/main/images/logo/logo.png)

[![CI](https://github.com/elixir-lang/elixir/actions/workflows/ci.yml/badge.svg?branch=main)](https://github.com/elixir-lang/elixir/actions/workflows/ci.yml?query=branch%3Amain) [![OpenSSF Best Practices](https://www.bestpractices.dev/projects/10187/badge)](https://www.bestpractices.dev/projects/10187)

Elixir is a dynamic, functional language designed for building scalable and maintainable applications.

For more about Elixir, installation and documentation, [check Elixir's website](https://elixir-lang.org/).

## Policies

New releases are announced in the [announcement mailing list](https://groups.google.com/group/elixir-lang-ann). You can subscribe by sending an email to \<elixir-lang-ann+subscribe@googlegroups.com\> and replying to the confirmation email.

All security releases [will be tagged with `[security]`](https://groups.google.com/forum/#!searchin/elixir-lang-ann/%5Bsecurity%5D%7Csort:date). For more information, please read our [Security Policy](SECURITY.md).

All interactions in our official communication channels follow our [Code of Conduct](CODE_OF_CONDUCT.md).

All contributions are required to conform to our [Open Source Policy](OPEN_SOURCE_POLICY.md).

## Bug reports

For reporting bugs, [visit our issue tracker](https://github.com/elixir-lang/elixir/issues) and follow the steps for reporting a new issue. **Please disclose security vulnerabilities privately [in our Security page](https://github.com/elixir-lang/elixir/security)**.

All currently open bugs related to Elixir are listed in the issues tracker. The Elixir team uses the issues tracker to focus on *actionable items*, including planned enhancements in the short and medium term. We also do our best to label entries for clarity and to ease collaboration.

Our *actionable item policy* has some important consequences, such as:

- Proposing new features as well as requests for support, help, and guidance must be done in their own spaces, detailed next.

- Issues we have identified to be outside of Elixir's scope, such as an upstream bug, will be closed (and requested to be moved elsewhere if appropriate).

- We actively close unrelated and non-actionable issues to keep the issues tracker tidy. If you believe we got something wrong, drop a comment and we can always reopen the issue.

By keeping the overall issues tracker tidy and organized, the community can easily peek at what is coming in new releases and also get involved by commenting on existing issues and submitting pull requests. Please remember to keep the tone positive and be kind! For more information, see the [Code of Conduct](CODE_OF_CONDUCT.md).

## Discussions, support, and help

For general discussions, support, and help, please use the community spaces [listed on the sidebar of the Elixir website](https://elixir-lang.org/), such as forums, chat platforms, etc, where the wider community will be available to help you.

## Proposing new features

We encourage you to first propose new features in the community spaces listed above. These discussions help refine ideas and gather feedback before submission. Our website also includes [a general outline of the language history and its current development focus](https://elixir-lang.org/development.html).

Once you are ready, you can submit your proposal to the [Elixir Core mailing list](https://groups.google.com/group/elixir-lang-core), either through the web interface or by subscribing to it at \<elixir-lang-core+subscribe@googlegroups.com\>. Remember to include a clear problem description, compare the proposed solution to existing alternatives in the Elixir ecosystem (and in other languages if possible), and consider the potential impact your changes will have on the codebase and community.

Once a proposal is accepted, it will be added to [the issue tracker](https://github.com/elixir-lang/elixir/issues). Features and bug fixes that have already been merged and will be included in the next release are then "closed" and added to the [changelog](CHANGELOG.md) before release.

## Compiling from source

For the many different ways to install Elixir, [see our installation instructions on the website](https://elixir-lang.org/install.html). However, if you want to contribute to Elixir, you will need to compile from source.

First, [install Erlang](https://elixir-lang.org/install.html#installing-erlang). After that, clone this repository to your machine, compile and test it:

``` sh
git clone https://github.com/elixir-lang/elixir.git
cd elixir
make
```

> Note: if you are running on Windows, [this article includes important notes for compiling Elixir from source on Windows](https://github.com/elixir-lang/elixir/wiki/Windows).

In case you want to use this Elixir version as your system version, you need to add the `bin` directory to [your PATH environment variable](https://elixir-lang.org/install.html#setting-path-environment-variable).

When updating the repository, you may want to run `make clean` before recompiling. For deterministic builds, you should set the environment variable `ERL_COMPILER_OPTIONS=deterministic`.

## Contributing

Contributions to Elixir are always welcome! Before you get started, please check out our [CONTRIBUTING.md](CONTRIBUTING.md) file. There you will find detailed guidelines on how to set up your environment, run the test suite, format your code, and submit pull requests.

Note you must disclose the use of coding agents and AI written code in your contributions. See the "Using AI and coding agents" in [CONTRIBUTING.md](CONTRIBUTING.md).

## Development links

- [Elixir Documentation](https://elixir-lang.org/docs.html)
- [Elixir Core Mailing list (development)](https://groups.google.com/group/elixir-lang-core)
- [Announcement mailing list](https://groups.google.com/group/elixir-lang-ann)
- [Code of Conduct](CODE_OF_CONDUCT.md)
- [Issue tracker](https://github.com/elixir-lang/elixir/issues)
- [Changelog](CHANGELOG.md)
- [Security Policy](SECURITY.md)
- **[\#elixir](https://web.libera.chat/#elixir)** on [Libera.Chat](https://libera.chat) IRC

## License

"Elixir" and the Elixir logo are registered trademarks of The Elixir Team.

Elixir source code is released under Apache License 2.0.

Check [LICENSE](LICENSE) file for more information.
