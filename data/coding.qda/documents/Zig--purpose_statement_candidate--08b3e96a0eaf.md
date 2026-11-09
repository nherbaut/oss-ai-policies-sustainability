Zig is a general-purpose programming language and toolchain for maintaining **robust**, **optimal** and **reusable** software.

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

# [Full overview](intro/overview/)

# [More code samples](intro/samples/)

    const std = @import("std");
    const parseInt = std.fmt.parseInt;

    test "parse integers" {
        const input = "123 67 89,99";
        const gpa = std.testing.allocator;

        var list: std.ArrayList(u32) = .empty;
        // Ensure the list is freed at scope exit.
        // Try commenting out this line!
        defer list.deinit(gpa);

        var it = std.mem.tokenizeAny(u8, input, " ,");
        while (it.next()) |num| {
            const n = try parseInt(u32, num, 10);
            try list.append(gpa, n);
        }

        const expected = [_]u32{ 123, 67, 89, 99 };

        for (expected, list.items) |exp, actual| {
            try std.testing.expectEqual(exp, actual);
        }
    }

index.zig

    $ zig test index.zig
    1/1 index.test.parse integers...OK
    All 1 tests passed.

Shell

# [Community](#community)

![](/ziggy.svg)

## [The Zig community is decentralized](#decentralized)

Anyone is free to start and maintain their own space for the community to gather.  
There is no concept of “official” or “unofficial”, however, each gathering place has its own moderators and rules.

# [See all Communities](/community)

## [Main development](#main-development)

The Zig repository can be found at \<https://codeberg.org/ziglang/zig\>, where we also host the issue tracker and discuss proposals.  
Contributors are expected to follow Zig’s [Code of Conduct](/code-of-conduct/).

![](/zero.svg)

# [Zig Software Foundation](#zsf)

## The ZSF is a 501(c)(3) non-profit corporation.

The Zig Software Foundation is a non-profit corporation founded in 2020 by Andrew Kelley, the creator of Zig, with the goal of supporting the development of the language. Currently, the ZSF is able to offer paid work at competitive rates to a small number of core contributors. We hope to be able to extend this offer to more core contributors in the future.

The Zig Software Foundation is sustained by donations.

# [Learn More](/zsf/)

# [Sponsors](#sponsors)

## [Corporate Sponsors](#corporate-sponsors)

The following companies are providing direct financial support to the Zig Software foundation.

![](/sponsors/tb-logo-black.png)

![](/sponsors/Blacksmith_Logo.svg)

![](/sponsors/zml.svg)

![](/sponsors/SILARES_HORIZONTAL_LOGO_BLACK.png)

![](/sponsors/Synadia_Logo.svg)
