English \| [简体中文](translations/README.zh.md) \| [繁體中文](translations/README.zht.md) \| [한국어](translations/README.ko.md) \| [Deutsch](translations/README.de.md) \| [Español](translations/README.es.md) \| [Français](translations/README.fr.md) \| [Italiano](translations/README.it.md) \| [Dansk](translations/README.da.md) \| [日本語](translations/README.ja.md) \| [Polski](translations/README.pl.md) \| [Русский](translations/README.ru.md) \| [Bosanski](translations/README.bs.md) \| [العربية](translations/README.ar.md) \| [Norsk](translations/README.no.md) \| [Português (Brasil)](translations/README.br.md) \| [ไทย](translations/README.th.md) \| [Türkçe](translations/README.tr.md) \| [Українська](translations/README.uk.md) \| [বাংলা](translations/README.bn.md) \| [Ελληνικά](translations/README.gr.md) \| [Tiếng Việt](translations/README.vi.md)

[![Kilo Code logo](https://github.com/user-attachments/assets/bdb0c174-b9fd-40ad-a47b-f3aab9b54e8d)](https://kilo.ai)

The open source coding agent for building with AI in VS Code, JetBrains, or the CLI.

[![VS Code Marketplace](https://raster.shields.io/badge/VS_Code_Marketplace-007ACC?style=flat&logo=visualstudiocode&logoColor=white)](https://marketplace.visualstudio.com/items?itemName=kilocode.Kilo-Code) [![npm](https://raster.shields.io/npm/v/@kilocode/cli?style=flat)](https://www.npmjs.com/package/@kilocode/cli) [![X (Twitter)](https://raster.shields.io/badge/kilocode-000000?style=flat&logo=x&logoColor=white)](https://x.com/kilocode) [![Blog](https://raster.shields.io/badge/Blog-555?style=flat&logo=substack&logoColor=white)](https://blog.kilo.ai) [![Discord](https://raster.shields.io/badge/Join%20Discord-5865F2?style=flat&logo=discord&logoColor=white)](https://kilo.ai/discord) [![Reddit](https://raster.shields.io/badge/Join%20r%2Fkilocode-D84315?style=flat&logo=reddit&logoColor=white)](https://www.reddit.com/r/kilocode/)

![Kilo-in-VS-Code-and-CLI](https://github.com/user-attachments/assets/0536ca59-ed81-4512-9e05-d186187a1b52)

Kilo-in-VS-Code-and-CLI

------------------------------------------------------------------------

Kilo Code is an AI coding agent that meets you everywhere you work: [VS Code](https://kilo.ai/landing/vs-code), [JetBrains](https://kilo.ai/features/jetbrains-native), and the [CLI](https://kilo.ai/cli). It's open source with open pricing. You pick from 500+ models, switch between them mid-task, and pay the model provider's rate with zero markup. No API keys required to start.

### Installation

Pick where you want to run Kilo.

**VS Code**

Install the [Kilo Code extension](vscode:extension/kilocode.kilo-code) directly, or grab it from the [VS Code Marketplace](https://marketplace.visualstudio.com/items?itemName=kilocode.Kilo-Code). Create an account and you'll have access to 500+ models including GPT-5.5, Claude Opus 4.7, Claude Sonnet 4.6, and Gemini 3.1 Pro Preview, all at provider pricing.

**CLI**

``` bash
# npm
npm install -g @kilocode/cli

# curl
curl -fsSL https://kilo.ai/cli/install | bash

# pnpm
pnpm add -g @kilocode/cli

# bun
bun add -g @kilocode/cli

# Homebrew (macOS / Linux)
brew install Kilo-Org/tap/kilo

# Arch Linux (AUR)
paru -S kilo-bin
```

Then run `kilo` in any project directory to start.

**JetBrains**

Install the [Kilo Code plugin](https://plugins.jetbrains.com/plugin/28350-kilo-code) from the JetBrains Marketplace, or search "Kilo Code" in `Settings → Plugins` inside any JetBrains IDE.

**Cloud Agent**

Run Kilo from the web, no local machine needed, at [app.kilo.ai/cloud](https://app.kilo.ai/cloud).

**Code Reviews**

Set up automated AI code reviews on your pull requests at [app.kilo.ai/code-reviews](https://app.kilo.ai/code-reviews).

**KiloClaw**

Spin up your always-on AI agent at [app.kilo.ai/claw](https://app.kilo.ai/claw).

Install the CLI from GitHub Releases (binaries)

Download the latest binary from the [Releases page](https://github.com/Kilo-Org/kilocode/releases).

| Platform              | Asset                     |
|-----------------------|---------------------------|
| Windows (most PCs)    | `kilo-windows-x64.zip`    |
| macOS (Apple Silicon) | `kilo-darwin-arm64.zip`   |
| macOS (Intel)         | `kilo-darwin-x64.zip`     |
| Linux x64             | `kilo-linux-x64.tar.gz`   |
| Linux ARM             | `kilo-linux-arm64.tar.gz` |

Notes: `x64-baseline` is a compatibility build for older CPUs without AVX. `musl` is the statically linked build for Alpine or minimal Docker images without glibc. `kilo-vscode-*.vsix` is the VS Code extension package, not the CLI. `Source code` archives are for building from source.

### Agents

Kilo ships with specialized agents you switch between depending on the task. You can also build your own custom agents.

- **Code** - The default. Implements and edits code from natural language.
- **Plan** - Designs architecture and writes implementation plans before any code gets written.
- **Ask** - Answers questions about your codebase without touching any files.
- **Debug** - Troubleshoots and traces issues.
- **Review** - Reviews your changes and surfaces issues across performance, security, style, and test coverage.

Learn more about [agents and custom agents](https://kilo.ai/docs/code-with-ai/agents/using-agents).

### What it does

- **Code generation** from natural language, across multiple files.
- **Inline autocomplete** with ghost-text suggestions and tab to accept.
- **Self-checking** so the agent reviews and corrects its own work.
- **Terminal and browser control** to run commands and automate the web.
- **MCP marketplace** to find and wire up MCP servers that extend what the agent can do.
- **500+ models** with mid-task switching, so you can match latency, cost, and reasoning to the job.

### Autonomous Mode (CI/CD)

Run `kilo run` with `--auto` for fully autonomous operation with no prompts, built for CI/CD pipelines:

``` bash
kilo run --auto "run tests and fix any failures"
```

`--auto` disables all permission prompts and lets the agent execute any action without confirmation. Only use it in trusted environments.

### Documentation

For configuration and everything else, [head over to the docs](https://kilo.ai/docs).

### Contributing

Contributions are welcome from developers, writers, and everyone in between. Start with the [Contributing Guide](/CONTRIBUTING.md) for environment setup, coding standards, and how to open a pull request. See [RELEASING.md](RELEASING.md) for the VS Code extension and CLI release process, and [packages/kilo-jetbrains/RELEASING.md](packages/kilo-jetbrains/RELEASING.md) for the JetBrains plugin.

Please review our [Code of Conduct](/CODE_OF_CONDUCT.md) before getting involved.

### License

MIT. You're free to use, modify, and distribute this code, including commercially, as long as you keep the attribution and license notices. See [License](/LICENSE).

### FAQ

Where did Kilo CLI come from?

Kilo CLI is a fork of [OpenCode](https://github.com/anomalyco/opencode), enhanced to work within the Kilo agentic engineering platform.

------------------------------------------------------------------------

**Join the community** [Discord](https://kilo.ai/discord) \| [X](https://x.com/kilocode) \| [Reddit](https://www.reddit.com/r/kilocode/)
