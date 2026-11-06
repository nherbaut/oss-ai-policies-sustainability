The **LLVM** Compiler Infrastructure ![](img/LLVMWyvernSmall.png)

**Site Map:**

[Overview](/)  
[Features](/Features.html)  
[Documentation](/docs/)  
[Command Guide](/docs/CommandGuide/)  
[FAQ](/docs/FAQ.html)  
[Publications](/pubs/)  
[LLVM Projects](/ProjectsWithLLVM/)  
[Open Projects](/OpenProjects.html)  
[LLVM Users](/Users.html)  
[Bug tracker](https://github.com/llvm/llvm-project/issues/)  
[LLVM Logo](/Logo.html)  
[Blog](http://blog.llvm.org/)  
[Meetings](/devmtg/)  
[LLVM Foundation](//foundation.llvm.org)  

**Download!**

Download now: [**LLVM 23.1.5**](https://releases.llvm.org/)  
[All Releases](/releases/)  
[APT Packages](https://apt.llvm.org/)  
[RPM Snapshots](https://copr.fedorainfracloud.org/coprs/g/fedora-llvm-team/llvm-snapshots/)  
[Pre-releases](https://prereleases.llvm.org/)  

View the open-source  
[**license**](/releases/14.0.0/LICENSE.TXT)

**Search this Site**

**Useful Links**

Forums  
[LLVM Discourse](https://discourse.llvm.org/)  

Mailing Lists:  
[Commits List](https://lists.llvm.org/cgi-bin/mailman/listinfo)  

Discord (Real-time Chat):  
[Discord](https://discord.gg/xS7Z362)  

Calendar:  
[LLVM Community Calendar](https://calendar.google.com/calendar/u/0/embed?src=calendar@llvm.org)  

Dev. Resources:  
[doxygen](/doxygen/)  
[Sources (GitHub)](https://github.com/llvm/llvm-project/)  
[Code Review](https://reviews.llvm.org)  
[Blog](http://blog.llvm.org/)  
[Bug tracker](https://github.com/llvm/llvm-project/issues/)  
[Buildbot](https://lab.llvm.org/buildbot/)  
[Green Dragon](http://green.lab.llvm.org/)  
[LNT](http://lnt.llvm.org/)  
[Scan-build](/reports/scan-build/)  
[llvm-cov](https://lab.llvm.org/coverage/coverage-reports/index.html)  
[Compile-time tracker](https://llvm-compile-time-tracker.com/)  

**Release Emails**

23.1.5: [Nov 2026](https://discourse.llvm.org/t/llvm-23-1-5-released/92716) 23.1.4: [Oct 2026](https://discourse.llvm.org/t/llvm-23-1-4-released/92564) 23.1.3: [Oct 2026](https://discourse.llvm.org/t/llvm-23-1-3-released/92432) 23.1.2: [Sep 2026](https://discourse.llvm.org/t/lvm-23-1-2-released/91895) 23.1.1: [Sep 2026](https://discourse.llvm.org/t/llvm-23-1-1-released/91760) 23.1.0: [Aug 2026](https://discourse.llvm.org/t/llvm-23-1-0-released/91654) 22.1.8: [Jun 2026](https://discourse.llvm.org/t/llvm-22-1-8-released/91084) 22.1.7: [Jun 2026](https://discourse.llvm.org/t/llvm-22-1-7-released/90961) 22.1.6: [May 2026](https://discourse.llvm.org/t/llvm-22-1-6-released/90838/3) 22.1.5: [May 2026](https://discourse.llvm.org/t/llvm-22-1-5-released/90734) 22.1.4: [Apr 2026](https://discourse.llvm.org/t/llvm-22-1-3-released/90467) 22.1.3: [Apr 2026](https://discourse.llvm.org/t/llvm-22-1-3-released/90467) 22.1.2: [Mar 2026](https://discourse.llvm.org/t/llvm-22-1-2-released/90308) 22.1.1: [Mar 2026](https://discourse.llvm.org/t/llvm-22-1-1-released/90150) 22.1.0: [Feb 2026](https://discourse.llvm.org/t/llvm-22-1-0-released/89950/2) [All Announcements](https://discourse.llvm.org/c/announce/46)  

Maintained by the  
[llvm-admin team](mailto:llvm-admin@lists.llvm.org)

LLVM Overview

The LLVM Project is a collection of modular and reusable compiler and toolchain technologies. Despite its name, LLVM has little to do with traditional virtual machines. The name "LLVM" itself is not an acronym; it is the full name of the project.

LLVM began as a [research project](pubs/2004-01-30-CGO-LLVM.html) at the [University of Illinois](https://cs.illinois.edu/), with the goal of providing a modern, SSA-based compilation strategy capable of supporting both static and dynamic compilation of arbitrary programming languages. Since then, LLVM has grown to be an umbrella project consisting of a number of subprojects, many of which are being used in production by a wide variety of [commercial and open source](Users.html) projects as well as being widely used in [academic research](pubs/). Code in the LLVM project is licensed under the ["Apache 2.0 License with LLVM exceptions"](docs/DeveloperPolicy.html#new-llvm-project-license-framework)

The primary sub-projects of LLVM are:

1.  The **LLVM Core** libraries provide a modern source- and target-independent [optimizer](docs/Passes.html), along with [code generation support](docs/CodeGenerator.html) for many popular CPUs (as well as some less common ones!) These libraries are built around a [well specified](docs/LangRef.html) code representation known as the LLVM intermediate representation ("LLVM IR"). The LLVM Core libraries are [well documented](docs/), and it is particularly easy to invent your own language (or port an existing compiler) to use [LLVM as an optimizer and code generator](docs/tutorial/).

2.  **[Clang](https://clang.llvm.org)** is an "LLVM native" C/C++/Objective-C compiler, which aims to deliver amazingly fast compiles, extremely useful [error and warning messages](https://clang.llvm.org/diagnostics.html) and to provide a platform for building great source level tools. The [Clang Static Analyzer](https://clang-analyzer.llvm.org/) and [clang-tidy](https://clang.llvm.org/extra/clang-tidy/) are tools that automatically find bugs in your code, and are great examples of the sort of tools that can be built using the Clang frontend as a library to parse C/C++ code.

3.  **[Flang](https://flang.llvm.org)** is a modern Fortran compiler with an associated runtime, which aims to generate high-performance code, and support Fortran 2023 and all official Fortran standards going back to Fortran 77, including a number of widely-used [extensions](https://flang.llvm.org/docs/Extensions.html). Flang supports [OpenMP](https://flang.llvm.org/docs/OpenMPSupport.html) for both CPUs and GPUs.

4.  The **[LLDB](https://lldb.llvm.org)** project builds on libraries provided by LLVM and Clang to provide a great native debugger. It uses the Clang ASTs and expression parser, LLVM JIT, LLVM disassembler, etc so that it provides an experience that "just works". It is also blazing fast and much more memory efficient than GDB at loading symbols.

5.  The **[libc++](https://libcxx.llvm.org)** and **[libc++ ABI](https://libcxxabi.llvm.org)** projects provide a standard conformant and high-performance implementation of the C++ Standard Library, including full support for C++11 and C++14.

6.  The **[libc](https://libc.llvm.org)** project provides a high-performance, standards-conformant implementation of the C Standard Library, fully integrated with LLVM. It delivers optimized performance and comprehensive support for modern C standards, ensuring a reliable and efficient foundation for C applications.

7.  The **[compiler-rt](https://compiler-rt.llvm.org)** project provides highly tuned implementations of the low-level code generator support routines like "`__fixunsdfdi`" and other calls generated when a target doesn't have a short sequence of native instructions to implement a core IR operation. It also provides implementations of run-time libraries for dynamic testing tools such as [AddressSanitizer](https://clang.llvm.org/docs/AddressSanitizer.html), [ThreadSanitizer](https://clang.llvm.org/docs/ThreadSanitizer.html), [MemorySanitizer](https://clang.llvm.org/docs/MemorySanitizer.html), and [DataFlowSanitizer](https://clang.llvm.org/docs/DataFlowSanitizer.html).

8.  The **[MLIR](https://mlir.llvm.org)** subproject is a novel approach to building reusable and extensible compiler infrastructure. MLIR aims to address software fragmentation, improve compilation for heterogeneous hardware, significantly reduce the cost of building domain specific compilers, and aid in connecting existing compilers together.

9.  The **[OpenMP](https://openmp.llvm.org)** subproject provides an [OpenMP](https://openmp.org) runtime for use with the OpenMP implementation in Clang and Flang.

10. The **[polly](https://polly.llvm.org/)** project implements a suite of cache-locality optimizations as well as auto-parallelism and vectorization using a polyhedral model.

11. The **[libclc](https://libclc.llvm.org/)** project aims to implement the OpenCL standard library.

12. The **[klee](https://klee.llvm.org)** project implements a "symbolic virtual machine" which uses a theorem prover to try to evaluate all dynamic paths through a program in an effort to find bugs and to prove properties of functions. A major feature of klee is that it can produce a testcase in the event that it detects a bug.

13. The **[LLD](https://lld.llvm.org/)** project is a new linker. That is a drop-in replacement for system linkers and runs much faster.

14. The **[BOLT](https://github.com/llvm/llvm-project/tree/main/bolt)** project is a post-link optimizer. It achieves the improvements by optimizing application's code layout based on execution profile gathered by sampling profiler.

In addition to official subprojects of LLVM, there are a broad variety of other projects that [use components of LLVM for various tasks](/ProjectsWithLLVM/). Through these external projects you can use LLVM to compile Ruby, Python, Haskell, Rust, D, PHP, Pure, Lua, Julia, and a number of other languages. A major strength of LLVM is its versatility, flexibility, and reusability, which is why it is being used for such a wide variety of different tasks: everything from doing light-weight JIT compiles of embedded languages like Lua to compiling Fortran code for massive super computers.

As much as everything else, LLVM has a broad and friendly community of people who are interested in building great low-level tools. If you are interested in [getting involved](https://llvm.org/docs/GettingInvolved.html), a good first place is to skim the [LLVM Blog](https://blog.llvm.org) and join [LLVM Discourse](https://discourse.llvm.org). For information on how to send in a patch, get commit access, and copyright and license topics, please see [the LLVM Developer Policy](docs/DeveloperPolicy.html).

Latest LLVM Release!

**3 November 2026**: LLVM 23.1.5 is now [**available for download**](releases/)! LLVM is publicly available under an open source [License](releases/23.1.0/LICENSE.TXT). Also, you might want to check out [**the new features**](docs/ReleaseNotes.html#whatsnew) in Git that will appear in the next LLVM release. If you want them early, [download LLVM](releases/) through anonymous Git.

Upcoming Events

[October 26-28](/devmtg/2026-10/) 2026 US LLVM  

ACM Software System Award!

LLVM has been awarded the **2012 ACM Software System Award**! This award is given by ACM to *one* software system worldwide every year. LLVM is [in highly distinguished company](https://awards.acm.org/software-system/award-recipients)! Click on any of the individual recipients' names on that page for the detailed citation describing the award.

Upcoming Releases

**LLVM Release Schedule:**

- 23.1.x
  - Tue Jul 14th, 2026: release/23.x branch
  - Fri Jul 17th, 2026: 23.1.0-rc1 was released
  - Tue Jul 28th, 2026: 23.1.0-rc2 was released
  - Tue Aug 12th, 2026: 23.1.0-rc3 was released
  - Tue Aug 25th, 2026: 23.1.0 was released
  - Tue Sep 8th, 2026: 23.1.1 was released
  - Tue Sep 22nd, 2026: 23.1.2 was released
  - Tue Oct 6th, 2026: 23.1.3 was released
  - Tue Oct 20th, 2026: 23.1.4 was released
  - Tue Nov 3rd, 2026: 23.1.5 was released
  - Tue Nov 17th, 2026: 23.1.6
  - Tue Dec 1st, 2026: 23.1.7
  - Tue Dec 15th, 2026: 23.1.8
  - Tue Dec 29th, 2026: 23.1.9 (if necessary)

Developer Meetings

Upcoming:

- [October 26-28, 2026](/devmtg/2026-10/)

Proceedings from past meetings:

- [April 13-15, 2026](/devmtg/2026-04/)
- [October 27-29, 2025](/devmtg/2025-10/)
- [June 10, 2025](/devmtg/2025-06/)
- [April 14-16, 2025](/devmtg/2025-04/)
- [October 22-24, 2024](/devmtg/2024-10/)
- [April 10-11, 2024](/devmtg/2024-04/)
- [October 9-11, 2023](/devmtg/2023-10/)
- [May 10-11, 2023](/devmtg/2023-05/)
- [November 8-9, 2022](/devmtg/2022-11/)
- [May 10-11, 2022](/devmtg/2022-05/)
- [November 16-19, 2021](/devmtg/2021-11/)
- [October 6-8, 2020](/devmtg/2020-09/)
- [October 22-23, 2019](/devmtg/2019-10/)
- [April 8-9, 2019](/devmtg/2019-04/)
- [October 17-18, 2018](/devmtg/2018-10/)
- [April 16-17, 2018](/devmtg/2018-04/)
- [October 18-19, 2017](/devmtg/2017-10/)
- [March 27-28, 2017](/devmtg/2017-03/)
- [November 3-4, 2016](/devmtg/2016-11/)
- [March 17-18, 2016](/devmtg/2016-03/)
- [October 29-30, 2015](/devmtg/2015-10/)
- [April 13-14, 2015](/devmtg/2015-04/)
- [October 28-29, 2014](/devmtg/2014-10/)
- [April 7-8, 2014](/devmtg/2014-04/)
- [Nov 6-7, 2013](/devmtg/2013-11/)
- [April 29-30, 2013](/devmtg/2013-04/)
- [November 7-8, 2012](/devmtg/2012-11/)
- [April 12, 2012](/devmtg/2012-04-12/)
- [November 18, 2011](/devmtg/2011-11/)
- [September 2011](/devmtg/2011-09-16/)
- [November 2010](/devmtg/2010-11/)
- [October 2009](/devmtg/2009-10/)
- [August 2008](/devmtg/2008-08/)
- [May 2007](/devmtg/2007-05/)
