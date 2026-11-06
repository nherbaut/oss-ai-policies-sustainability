<div id="content" role="main">

<div class="slogan alt-background">

<div class="container slogan-message">

<div style="max-width:790px;margin:10px 0;padding:0 5px">

<div id="slogan">

Zig is a general-purpose programming language and toolchain for maintaining **robust**, **optimal** and **reusable** software.

</div>

</div>

</div>

</div>

<div class="container" style="display:flex;flex-direction:row;flex-wrap:wrap;padding:30px 0 20px; justify-content:space-between;">

<div class="features">

<div>

<div id="features">

## ⚡ A Simple Language

Focus on debugging your application rather than debugging your programming language knowledge.

- No hidden control flow.
- No hidden memory allocations.
- No preprocessor, no macros.

## ⚡ Comptime

A fresh approach to metaprogramming based on compile-time code execution and lazy evaluation.

- Call any function at compile-time.
- Manipulate types as values without runtime overhead.
- Comptime emulates the target architecture.

## ⚡ Maintain it with Zig

Incrementally improve your C/C++/Zig codebase.

- Use Zig as a zero-dependency, drop-in C/C++ compiler that supports cross-compilation out-of-the-box.
- Leverage `zig build` to create a consistent development environment across all platforms.
- Add a Zig compilation unit to C/C++ projects, exposing the rich standard library to your C/C++ code.

</div>

</div>

<div style="display:flex;flex-direction:row;flex-wrap:wrap;justify-content:center">

<div>

# <a href="intro/overview/" class="button" style="display:inline">Full overview</a>

</div>

<div style="margin-left:5px">

# <a href="intro/samples/" class="button" style="display:inline">More code samples</a>

</div>

</div>

</div>

<div class="codesample">

<figure>
<pre><code>const std = @import(&quot;std&quot;);
const parseInt = std.fmt.parseInt;

test &quot;parse integers&quot; {
    const input = &quot;123 67 89,99&quot;;
    const gpa = std.testing.allocator;

    var list: std.ArrayList(u32) = .empty;
    // Ensure the list is freed at scope exit.
    // Try commenting out this line!
    defer list.deinit(gpa);

    var it = std.mem.tokenizeAny(u8, input, &quot; ,&quot;);
    while (it.next()) |num| {
        const n = try parseInt(u32, num, 10);
        try list.append(gpa, n);
    }

    const expected = [_]u32{ 123, 67, 89, 99 };

    for (expected, list.items) |exp, actual| {
        try std.testing.expectEqual(exp, actual);
    }
}</code></pre>
<figcaption>index.zig</figcaption>
</figure>

<figure>
<pre><code>$ zig test index.zig
1/1 index.test.parse integers...OK
All 1 tests passed.</code></pre>
<figcaption>Shell</figcaption>
</figure>

</div>

</div>

<div class="alt-background">

<div class="container" style="display:flex;flex-direction:column;justify-content:center;text-align:center;padding:20px 0">

<div id="community" class="section-title">

# [Community](#community)

</div>

<div class="container" style="display:flex;flex-direction:row;flex-wrap:wrap;justify-content:center">

<div style="width:25%">

<img src="/ziggy.svg" style="max-height:200px" />

</div>

<div class="community-message">

<div>

<div id="decentralized">

## [The Zig community is decentralized](#decentralized)

Anyone is free to start and maintain their own space for the community to gather.  
There is no concept of “official” or “unofficial”, however, each gathering place has its own moderators and rules.

</div>

</div>

<div>

# <a href="/community" class="button" style="display:inline">See all Communities</a>

</div>

</div>

</div>

<div style="height: 50px;">

</div>

<div class="container" style="display:flex;flex-direction:row;flex-wrap:wrap;justify-content:center">

<div class="main-development-message">

<div id="main-development">

## [Main development](#main-development)

The Zig repository can be found at <https://codeberg.org/ziglang/zig>, where we also host the issue tracker and discuss proposals.  
Contributors are expected to follow Zig’s [Code of Conduct](/code-of-conduct/).

</div>

</div>

<div style="width:40%">

<img src="/zero.svg" style="max-height:200px" />

</div>

</div>

</div>

</div>

<div class="container" style="display:flex;flex-direction:column;justify-content:center;text-align:center;padding:20px 0">

<div>

<div id="zsf" class="section-title">

# [Zig Software Foundation](#zsf)

## The ZSF is a 501(c)(3) non-profit corporation.

The Zig Software Foundation is a non-profit corporation founded in 2020 by Andrew Kelley, the creator of Zig, with the goal of supporting the development of the language. Currently, the ZSF is able to offer paid work at competitive rates to a small number of core contributors. We hope to be able to extend this offer to more core contributors in the future.

The Zig Software Foundation is sustained by donations.

</div>

</div>

# <a href="/zsf/" class="button" style="display: inline">Learn More</a>

</div>

<div class="alt-background" style="padding:20px 0">

<div class="container">

<div id="sponsors" class="section-title">

# [Sponsors](#sponsors)

</div>

<div>

<div id="corporate-sponsors">

## [Corporate Sponsors](#corporate-sponsors)

The following companies are providing direct financial support to the Zig Software foundation.

</div>

</div>

<div class="monetary-logos">

![](/sponsors/tb-logo-black.png) <a href="https://blacksmith.sh/" class="span2" rel="noopener nofollow" target="_blank"></a>

![](/sponsors/Blacksmith_Logo.svg) <a href="https://zml.ai" class="span2" rel="noopener nofollow" target="_blank"></a>

![](/sponsors/zml.svg)

![](/sponsors/SILARES_HORIZONTAL_LOGO_BLACK.png) <a href="https://synadia.com/" class="span2 synadia" rel="noopener nofollow" target="_blank"></a>

![](/sponsors/Synadia_Logo.svg)

</div>

</div>

</div>

</div>
