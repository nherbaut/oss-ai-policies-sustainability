![Text changing depending on mode. Light: 'So light!' Dark: 'So dark!'](https://github.com/atuinsh/atuin/assets/53315310/08bc86d4-a781-4aaa-8d7e-478ae6bcd129)

*magical shell history*

------------------------------------------------------------------------

[![](https://img.shields.io/github/actions/workflow/status/atuinsh/atuin/rust.yml?style=flat-square)](https://github.com/atuinsh/atuin/actions?query=workflow%3ARust) [![](https://img.shields.io/crates/v/atuin.svg?style=flat-square)](https://crates.io/crates/atuin) [![](https://img.shields.io/crates/d/atuin.svg?style=flat-square)](https://crates.io/crates/atuin) [![](https://img.shields.io/crates/l/atuin.svg?style=flat-square)](https://github.com/atuinsh/atuin/blob/main/LICENSE) [![](https://img.shields.io/discord/954121165239115808)](https://discord.gg/Fq8bJSKPHh) [![](https://img.shields.io/mastodon/follow/109944632283122560?domain=https%3A%2F%2Fhachyderm.io&style=social)](https://hachyderm.io/@atuin) [![](https://img.shields.io/twitter/follow/atuinsh?style=social)](https://twitter.com/atuinsh)

[English](./README.md) \| [简体中文](./docs-i18n/zh-CN/README.md)

Atuin replaces your existing shell history with a SQLite database, and records additional context for your commands. Additionally, it provides optional and *fully encrypted* synchronisation of your history between machines, via an Atuin server.

![animated](demo.gif)

*exit code, duration, time and command shown*

As well as the search UI, it can do things like this:

    # search for all successful `make` commands, recorded after 3pm yesterday
    atuin search --exit 0 --after "yesterday 3pm" make

You may use either the server I host, or host your own! Or just don't use sync at all. As all history sync is encrypted, I couldn't access your data even if I wanted to. And I **really** don't want to.

## Features

- rebind `ctrl-r` and `up` (configurable) to a full screen history search UI
- store shell history in a sqlite database
- back up and sync **encrypted** shell history
- the same history across terminals, across sessions, and across machines
- log exit code, cwd, hostname, session, command duration, etc
- calculate statistics such as "most used command"
- old history file is not replaced
- quick-jump to previous items with Alt-&lt;num\>
- switch filter modes via ctrl-r; search history just from the current session, directory, or globally
- enter to execute a command, tab to edit

## Documentation

- [Quickstart](#quickstart)
- [Install](https://docs.atuin.sh/guide/installation/)
- [Setting up sync](https://docs.atuin.sh/guide/sync/)
- [Import history](https://docs.atuin.sh/guide/import/)
- [Basic usage](https://docs.atuin.sh/guide/basic-usage/)

## Supported Shells

- zsh
- bash
- fish
- nushell
- xonsh
- powershell (tier 2 support)

## Community

### Forum

Atuin has a community forum, please ask here for help and support: \<https://forum.atuin.sh/\>

### IRC

We're also available via \#atuin on libera.chat

### Discord

Atuin also has a community Discord, available [here](https://discord.gg/jR3tfchVvW)

# Quickstart

This will sign you up for the Atuin Cloud sync server. Everything is end-to-end encrypted, so your secrets are safe!

Read the [docs](https://docs.atuin.sh) for an offline setup, self-hosted server, and more.

    curl --proto '=https' --tlsv1.2 -LsSf https://setup.atuin.sh | sh

    atuin register -u <USERNAME> -e <EMAIL>
    atuin import auto
    atuin sync

Then restart your shell!

> \[!NOTE\]
>
> **For Bash users**: The above sets up `bash-preexec` for necessary hooks, but `bash-preexec` has limitations. For details, please see the [Bash](https://docs.atuin.sh/guide/installation/#installing-the-shell-plugin) section of the shell plugin documentation.

# Security

If you find any security issues, we'd appreciate it if you could alert \<ellie@atuin.sh\>

# Related projects

- [Catpuccin for Atuin](https://github.com/catppuccin/atuin)
- [eshell-atuin](https://github.com/SqrtMinusOne/eshell-atuin)
- [mob (tiny creatures in your terminal)](https://github.com/bboynton97/mob)

Please open a PR for any others!

# Contributors

[![](https://contrib.rocks/image?repo=atuinsh/atuin&max=300)](https://github.com/atuinsh/atuin/graphs/contributors)

Made with [contrib.rocks](https://contrib.rocks).
