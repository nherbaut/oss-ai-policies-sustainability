# wgpu

![](logo.png)

[![Build Status](https://img.shields.io/github/actions/workflow/status/gfx-rs/wgpu/ci.yml?branch=trunk&logo=github&label=CI)](https://github.com/gfx-rs/wgpu/actions) [![codecov.io](https://img.shields.io/codecov/c/github/gfx-rs/wgpu?logo=codecov&logoColor=fff&label=codecov&token=84qJTesmeS)](https://codecov.io/gh/gfx-rs/wgpu)

`wgpu` is a cross-platform, safe, pure-Rust graphics API. It runs natively on Vulkan, Metal, D3D12, and OpenGL; and on top of WebGL2 and WebGPU on wasm.

The API is based on the [WebGPU standard](https://gpuweb.github.io/gpuweb/), but is a fully native Rust library. It serves as the core of the WebGPU integration in Firefox, Servo, and Deno.

## Getting Started

See our examples online at \<https://wgpu.rs/examples/\>. You can see the Rust sources at [examples](examples) and run them directly with `cargo run --bin wgpu-examples <example>`.

### Learning `wgpu`

If you are new to `wgpu` and graphics programming, we recommend starting with [Learn Wgpu](https://sotrh.github.io/learn-wgpu/).

Additionally, [WebGPU Fundamentals](https://webgpufundamentals.org/) is a tutorial for WebGPU which is very similar to our API, minus differences between Rust and Javascript.

### Wiki

We have a [wiki](https://github.com/gfx-rs/wgpu/wiki) which has information on useful architecture patterns, debugging tips, and more getting started information.

### Need Help? Want to Contribute?

The wgpu community uses Matrix and Discord to discuss.

- [![\#wgpu:matrix.org](https://img.shields.io/static/v1?label=wgpu-devs&message=%23wgpu&color=blueviolet&logo=matrix)](https://matrix.to/#/#wgpu:matrix.org) - discussion of wgpu's development.
- [![\#wgpu-users:matrix.org](https://img.shields.io/static/v1?label=wgpu-users&message=%23wgpu-users&color=blueviolet&logo=matrix)](https://matrix.to/#/#wgpu-users:matrix.org) - discussion of using the library and the surrounding ecosystem.
- [![\#wgpu on the Rust Gamedev Discord](https://img.shields.io/discord/676678179678715904?logo=discord&logoColor=E0E3FF&label=%23wgpu&color=5865F2)](https://discord.gg/X3MYBNXUMJ) - Dedicated support channel on the Rust Gamedev Discord.

### Other Languages

To use wgpu in C or dozens of other languages, look at [wgpu-native](https://github.com/gfx-rs/wgpu-native). These are C bindings to wgpu and has an up-to-date list of libraries bringing support to other languages.

[Learn WebGPU (for C++)](https://eliemichel.github.io/LearnWebGPU/) is a good resource for learning how to use wgpu-native from C++.

## Quick Links

| Docs | Examples | Changelog |
|:--:|:--:|:--:|
| [v30](https://docs.rs/wgpu/) | [v30](https://github.com/gfx-rs/wgpu/tree/v30/examples#readme) | [v30](https://github.com/gfx-rs/wgpu/releases) |
| [`trunk`](https://wgpu.rs/doc/wgpu/) | [`trunk`](https://github.com/gfx-rs/wgpu/tree/trunk/examples#readme) | [`trunk`](https://github.com/gfx-rs/wgpu/blob/trunk/CHANGELOG.md#unreleased) |

Contributors are welcome! See [CONTRIBUTING.md](CONTRIBUTING.md) for more information.

## Supported Platforms

| API    | Windows      | Linux/Android   | macOS/iOS | Web (wasm)  |
|--------|--------------|-----------------|-----------|-------------|
| Vulkan | ✅           | ✅              | 🌋        |             |
| Metal  |              |                 | ✅        |             |
| DX12   | ✅           |                 |           |             |
| OpenGL | 🆗 (GL 3.3+) | 🆗 (GL ES 3.0+) | 📐        | 🆗 (WebGL2) |
| WebGPU |              |                 |           | ✅          |

✅ = First Class Support  
🆗 = Downlevel/Best Effort Support  
📐 = Requires the [ANGLE](https://github.com/gfx-rs/wgpu/wiki/Running-on-ANGLE) translation layer (GL ES 3.0 only). Use the `angle` feature on macOS/iOS. On Windows, `gles` uses WGL by default; build with `cfg(windows_angle)` to use ANGLE instead. 🌋 = Requires the [MoltenVK](https://vulkan.lunarg.com/sdk/home#mac) translation layer  
🛠️ = Unsupported, though open to contributions

## Environment Variables

Testing, examples, and `::from_env()` methods use a standardized set of environment variables to control wgpu's behavior.

- `WGPU_BACKEND` with a comma-separated list of the backends you want to use (`vulkan`, `metal`, `dx12`, or `gl`).
- `WGPU_ADAPTER_NAME` with a case-insensitive substring of the name of the adapter you want to use (ex. `1080` will match `NVIDIA GeForce 1080ti`).
- `WGPU_DX12_COMPILER` with the DX12 shader compiler you wish to use (`dxc`, `static-dxc`, or `fxc`). Note that `dxc` requires `dxcompiler.dll` (min v1.8.2502) to be in the working directory, and `static-dxc` requires the `static-dxc` crate feature to be enabled. Otherwise, it will fall back to `fxc`.

See the [documentation](https://docs.rs/wgpu/latest/wgpu/index.html?search=env) for more environment variables.

When running the CTS, use the variables `DENO_WEBGPU_ADAPTER_NAME`, `DENO_WEBGPU_BACKEND`, `DENO_WEBGPU_POWER_PREFERENCE`, `DENO_WEBGPU_DX12_COMPILER`, and `DENO_WEBGPU_STRICT_COMPLIANCE`.

## Repo Overview

For an overview of all the components in the gfx-rs ecosystem, see [the big picture](./docs/big-picture.png).

## MSRV policy

TL;DR: If you're using `wgpu`, our MSRV is **1.87**. If you're running our tests or examples, our MSRV is **1.93**.

We will avoid bumping the MSRV of `wgpu` without good reason, and such a change is considered breaking.

Specific Details

Due to complex dependants, we have three MSRV policies:

- `wgpu`'s MSRV is **1.87**
- `wgpu-core` (and hence `wgpu-hal`, `naga`, `naga-types` and `wgpu-types`)'s MSRV is **1.87**.
- The rest of the workspace has an MSRV of **1.93**.

It is enforced on CI (in "/.github/workflows/ci.yml") with the `WGPU_MSRV`, `CORE_MSRV`, and `REPO_MSRV` variables, respectively. This version can only be upgraded in breaking releases, though we release a breaking version every three months.

The following rules apply:

- The `wgpu-core` crate should never require an MSRV ahead of Firefox's MSRV for nightly builds, as determined by the value of `MINIMUM_RUST_VERSION` in [`python/mozboot/mozboot/util.py`](https://searchfox.org/mozilla-central/source/python/mozboot/mozboot/util.py).
- The `wgpu` crate should never require an MSRV ahead of Servo's MSRV, as determined by the value of their rust-version declaration in [`Cargo.toml`](https://github.com/servo/servo/blob/main/Cargo.toml#L23)
- The repository MSRV should never require an MSRV higher than `stable - 3`. For example, if stable is at 1.97, the repository MSRV should be no higher than 1.94. This is to allow people who are using a decently-updated OS-provided rust to be able to build our repository. Consider cross checking with [NixOS](https://search.nixos.org/packages?show=rustc), though this is not required.

## Testing and Environment Variables

[Information about testing](./docs/testing.md), including where tests of various kinds live, and how to run the tests.

## Tracking the WebGPU and WGSL draft specifications

The `wgpu` crate is meant to be an idiomatic Rust translation of the [WebGPU API](https://www.w3.org/TR/webgpu/). That specification, along with its shading language, [WGSL](https://gpuweb.github.io/gpuweb/wgsl/), are both still in the "Working Draft" phase, and while the general outlines are stable, details change frequently. Until the specification is stabilized, the `wgpu` crate and the version of WGSL it implements will likely differ from what is specified, as the implementation catches up.

Exactly which WGSL features `wgpu` supports depends on how you are using it:

- When running as native code, `wgpu` uses [Naga](https://github.com/gfx-rs/wgpu/tree/trunk/naga/) to translate WGSL code into the shading language of your platform's native GPU API. Naga is working on catching up to the WGSL specification, with [bugs](https://github.com/gfx-rs/wgpu/issues?q=is%3Aissue%20state%3Aopen%20label%3A%22naga%22) tracking various issues, but there is no concise summary of differences from the specification.

- When running in a web browser (by compilation to WebAssembly) without the `"webgl"` feature enabled, `wgpu` relies on the browser's own WebGPU implementation. WGSL shaders are simply passed through to the browser, so that determines which WGSL features you can use.

- When running in a web browser with `wgpu`'s `"webgl"` feature enabled, `wgpu` uses Naga to translate WGSL programs into GLSL. This uses the same version of Naga as if you were running `wgpu` as native code.
