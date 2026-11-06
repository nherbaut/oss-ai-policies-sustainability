# `wasmtime`

**A standalone runtime for [WebAssembly](https://webassembly.org/)**

**A [Bytecode Alliance](https://bytecodealliance.org/) project**

[![build status](https://github.com/bytecodealliance/wasmtime/workflows/CI/badge.svg)](https://github.com/bytecodealliance/wasmtime/actions?query=workflow%3ACI) [![zulip chat](https://img.shields.io/badge/zulip-join_chat-brightgreen.svg)](https://bytecodealliance.zulipchat.com/#narrow/stream/217126-wasmtime) ![supported rustc stable](https://img.shields.io/badge/rustc-stable+-green.svg) [![Documentation Status](https://docs.rs/wasmtime/badge.svg)](https://docs.rs/wasmtime)

### [Guide](https://bytecodealliance.github.io/wasmtime/)  \|  [Contributing](https://bytecodealliance.github.io/wasmtime/contributing.html)  \|  [Website](https://wasmtime.dev/)  \|  [Chat](https://bytecodealliance.zulipchat.com/#narrow/stream/217126-wasmtime)

## Installation

The Wasmtime CLI can be installed on Linux and macOS (locally) with a small install script:

``` console
curl https://wasmtime.dev/install.sh -sSf | bash
```

This script installs into `$WASMTIME_HOME` (defaults to `$HOME/.wasmtime`), and executable is placed in `$WASMTIME_HOME/bin`.

After running the install script above, follow the on-screen instructions.

Windows or otherwise interested users can download installers and binaries directly from the [GitHub Releases](https://github.com/bytecodealliance/wasmtime/releases) page.

For additional installation options, refer to the [online book CLI installation page](https://docs.wasmtime.dev/cli-install.html).

Documentation on Wasmtime's currently supported versions can be found [in the online book documentation](https://docs.wasmtime.dev/stability-release.html#current-versions).

## Example

If you've got the [Rust compiler installed](https://www.rust-lang.org/tools/install) then you can take some Rust source code:

``` rust
fn main() {
    println!("Hello, world!");
}
```

and compile it into a WebAssembly component with:

``` console
rustup target add wasm32-wasip2
rustc hello.rs --target wasm32-wasip2
```

Once compiled, you can run your component:

``` console
wasmtime hello.wasm
```

You should see the following output:

``` text
Hello, world!
```

(Note: make sure you installed Rust using the [`rustup`](https://rustup.rs) method in the official instructions above, and do not have a copy of the Rust toolchain installed on your system in some other way as well (e.g. the system package manager). Otherwise, the `rustup target add...` command may not install the target for the correct copy of Rust.)

## Features

- **Fast**. Wasmtime is built on the optimizing [Cranelift](https://cranelift.dev/) code generator to quickly generate high-quality machine code either at runtime or ahead-of-time. Wasmtime is optimized for efficient instantiation, low-overhead calls between the embedder and wasm, and scalability of concurrent instances.

- **[Secure](https://docs.wasmtime.dev/security.html)**. Wasmtime's development is strongly focused on correctness and security. Building on top of Rust's runtime safety guarantees, each Wasmtime feature goes through careful review and consideration via an [RFC process](https://github.com/bytecodealliance/rfcs). Once features are designed and implemented, they undergo 24/7 fuzzing donated by [Google's OSS Fuzz](https://google.github.io/oss-fuzz/). As features stabilize they become part of a [release](https://docs.wasmtime.dev/stability-release.html), and when things go wrong we have a well-defined [security policy](https://bytecodealliance.org/security) in place to quickly mitigate and patch any issues. We follow best practices for defense-in-depth and integrate protections and mitigations for issues like Spectre. Finally, we're working to push the state-of-the-art by collaborating with academic researchers to formally verify critical parts of Wasmtime and Cranelift.

- **[Configurable](https://docs.rs/wasmtime/latest/wasmtime/struct.Config.html)**. Wasmtime uses sensible defaults, but can also be configured to provide more fine-grained control over things like CPU and memory consumption. Whether you want to run Wasmtime in a tiny environment or on massive servers with many concurrent instances, we've got you covered.

- **[WASI](https://docs.rs/wasmtime-wasi/latest/wasmtime_wasi/)**. Wasmtime supports a rich set of APIs for interacting with the host environment through the [WASI standard](https://wasi.dev).

- **[Standards Compliant](https://docs.wasmtime.dev/stability-tiers.html)**. Wasmtime passes the [official WebAssembly test suite](https://github.com/WebAssembly/testsuite), implements the [official C API of wasm](https://github.com/WebAssembly/wasm-c-api), and implements [future proposals to WebAssembly](https://github.com/WebAssembly/proposals) as well. Wasmtime developers are intimately engaged with the WebAssembly standards process all along the way too.

## Language Support

You can use Wasmtime from a variety of different languages through embeddings of the implementation.

Languages supported by the Bytecode Alliance:

- **[Rust](https://bytecodealliance.github.io/wasmtime/lang-rust.html)** - the [`wasmtime` crate](https://crates.io/crates/wasmtime)
- **[C](https://bytecodealliance.github.io/wasmtime/lang-c.html)** - the [`wasm.h`, `wasi.h`, and `wasmtime.h` headers](https://bytecodealliance.github.io/wasmtime/c-api/), [CMake](crates/c-api/CMakeLists.txt)
- **C++** - the [`wasmtime.hh` header](https://bytecodealliance.github.io/wasmtime/c-api/)
- **[Python](https://bytecodealliance.github.io/wasmtime/lang-python.html)** - the [`wasmtime` PyPI package](https://pypi.org/project/wasmtime/)
- **[.NET](https://bytecodealliance.github.io/wasmtime/lang-dotnet.html)** - the [`Wasmtime` NuGet package](https://www.nuget.org/packages/Wasmtime)
- **[Go](https://bytecodealliance.github.io/wasmtime/lang-go.html)** - the [`wasmtime-go` repository](https://pkg.go.dev/github.com/bytecodealliance/wasmtime-go)
- **[Ruby](https://bytecodealliance.github.io/wasmtime/lang-ruby.html)** - the [`wasmtime` gem](https://rubygems.org/gems/wasmtime)

Languages supported by the community:

- **[Elixir](https://docs.wasmtime.dev/lang-elixir.html)** - the [`wasmex` hex package](https://hex.pm/packages/wasmex)
- **Perl** - the [`Wasm` Perl package's `Wasm::Wasmtime`](https://metacpan.org/pod/Wasm::Wasmtime)

## Documentation

[📚 Read the Wasmtime guide here! 📚](https://bytecodealliance.github.io/wasmtime)

The [wasmtime guide](https://bytecodealliance.github.io/wasmtime) is the best starting point to learn about what Wasmtime can do for you or help answer your questions about Wasmtime. If you're curious in contributing to Wasmtime, [it can also help you do that](https://bytecodealliance.github.io/wasmtime/contributing.html)!

------------------------------------------------------------------------

It's Wasmtime.
