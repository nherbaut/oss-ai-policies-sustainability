[![Dolphin Emulator](https://dolphin-emu.org/m/static/img/logo.72ba8e6312af.png)](/)

- [Download](/download/)
- [Blog](/blog/)
- [Screenshots](/media/)
- [FAQ](/docs/faq/)
- [Guides](/docs/guides/)
- [Compatibility](/compat/)
- [Community ](#)
  - [Discord](https://discord.dolphin-emu.org/)
  - [Forum](https://forums.dolphin-emu.org/)
  - [Wiki](https://wiki.dolphin-emu.org/)
  - [GitHub](https://github.com/dolphin-emu/dolphin)

&nbsp;

- 

  English
  - 

    Asturianu

  - 

    Bahasa Melayu

  - 

    Català

  - 

    Česky

  - 

    Cymraeg

  - 

    Dansk

  - 

    Deutsch

  - 

    Español

  - 

    Ελληνικά

  - 

    Français

  - 

    Galego

  - 

    Italiano

  - 

    Magyar

  - 

    Nederlands

  - 

    Norsk (Bokmål)

  - 

    Polski

  - 

    Português

  - 

    Português (Brasil)

  - 

    Русский

  - 

    Svenska

  - 

    Türkçe

  - 

    中文(中国)

  - 

    日本語

  - 

    한국어

- About Dolphin
- [What is Dolphin?](#what-dolphin)
- [Dolphin's License](#what-dolphins-license)
- [Who Made Dolphin?](#who-made-dolphin)
- Hardware and system requirements
- [Operating Systems](#what-operating-systems-are-supported)
- [CPU](#which-cpu-should-i-use)
- [GPU](#which-gpu-do-i-need)
- [RAM](#how-much-ram-do-i-need-run-dolphin)
- Installation issues
- [Which version?](#which-version-dolphin-should-i-download)
- [VCdll missing](#program-cant-start-because-vcdll-is-missing)
- [XINPUT_3.dll not found](#application-has-failed-start-because-xinput1_3dll-)
- [Error 0xc000007b](#application-was-unable-start-correctly-0xc000007b)
- Configuration issues
- [Laptop/GPU is slower than it should be](#my-laptop-new-gpu-not-performing-well-it-should)
- [Second GC pad not working](#i-configured-bindings-second-gc-pad-it-does-not-wo)
- Common issues
- [Audio Stuttering](#my-audio-stuttering)
- [Game issues](#game-x-does-not-run-correctly)
- [Graphics menu makes games faster?](#dolphin-speeds-when-i-open-graphics-menu)
- Dolphin development
- [Building Dolphin](#how-can-i-build-dolphin-my-computer)
- [Following development](#what-best-way-follow-development-progress)
- [Suggesting improvements](#ive-got-idea-make-dolphin-better-how-should-i-tell)
- Miscellaneous
- [Why not use more cores](#couldnt-dolphin-use-more-my-cpu-cores-go-faster)
- [Why does Dolphin require so much power](#why-do-i-need-such-powerful-computer-emulate-old-c)
- [Downloading game ISOs/ROMs](#where-can-i-download-game-isosroms)
- [Supported Dump Formats](#what-dump-formats-are-supported-dolphin)

# About Dolphin

### What is Dolphin?

Dolphin is a GameCube and Wii emulator with high compatibility across the majority of titles for both platforms. It was first developed as closed source in 2003, and as open source since 2008.

### What is Dolphin's License?

When Dolphin went open-source in 2008, it was released under the GPLv2 license. However it has since been [relicensed to GPLv2+](https://dolphin-emu.org/blog/2015/05/25/relicensing-dolphin/). According to the license, you may use Dolphin and its source code for any purpose, but distributing Dolphin requires that the source code be released and attribution given. For more details, see the [license document](https://github.com/dolphin-emu/dolphin/tree/master/LICENSES).

### Who Made Dolphin?

Over 200 people have worked hard over the years to create Dolphin. The list of contributors can be found [on GitHub](https://github.com/dolphin-emu/dolphin/graphs/contributors).

Dolphin is not affiliated with Nintendo in any way.

# Hardware and system requirements

### What operating systems are supported?

Dolphin is a cross-platform emulator that runs on Windows (10 and newer), Linux, macOS (11.0 Big Sur and up), and Android (7.0 and above). Other Unix-like systems (such as FreeBSD) may work but are not officially supported. Operating systems are required to be 64-bit to run Dolphin.

### Which CPU should I use?

Dolphin is a dual core application that relies upon IPC (Instructions Per Clock) and clockspeed for performance. Additional cores will not make Dolphin go any faster, though an "extra" core that Dolphin isn’t using may help slightly by keeping background tasks from using the same cores as Dolphin.

Accordingly, the perfect CPU for Dolphin has high IPC, a high clock rate, and *four* cores or more. With four cores, Dolphin has two cores for the main emulation threads, a third core for other tasks, and another core for the operating system and background tasks to run without taking resources from the emulator.

Newer processors are generally better than older ones, thanks to the increased IPC that comes with newer architectures.

- **Intel**: Dolphin cares about frequency rather than core count, so within a given generation, mid-tier processors with fewer cores will act more or less the same as high-tier processors with more cores. Newer generations will give higher performance per clock, and K series processors will allow for overclocking to gain extra performance. Be wary of U and Y series processors, as their reduced clockspeeds often struggle with Dolphin's workload.

- **AMD**: Dolphin is not cache bound so it does not benefit much from X3D, and it doesn't use a lot of cores so Dolphin doesn't benefit from high core count CPUs either. Threadripper will work fine of course but a mid-tier Ryzen 5 of the same generation will technically outperform it. When buying Ryzen CPUs with Dolphin in mind, focus on frequency, and try to get as new as possible CPU for the best IPC.

For more details, such as specific CPU recommendations, CPU comparisons, or what hardware you should purchase to get playable speeds on a specific game, please ask on our [Hardware Forum](https://forums.dolphin-emu.org/Forum-hardware) **before purchasing**.

**Note**: For more information regarding CPU performance, please check out [this handy benchmark](https://docs.google.com/spreadsheet/ccc?key=0AkEUvobPn_DcdEo2aEhhdUpnU01tYUtNM3ZVX2d6SkE&usp=sharing) that contains results from tons of users. It's important to remember that Dolphin is a console emulator with tons of optimizations and features. But, in the end, it does what the game instructs it to do. [Some](https://wiki.dolphin-emu.org/index.php?title=Crazy_Taxi) games only use features that are easy to emulate, and thus will run full-speed on just about any computer that supports Dolphin. Meanwhile, [others](https://wiki.dolphin-emu.org/index.php?title=The_Last_Story) struggle to run full speed at all times on even the most powerful of processors.

### Which GPU do I need?

Choosing a GPU for Dolphin is a fairly simple task. The more powerful the graphics card, the more pixels and enhancements you can throw at it before you’ll see slowdown. However, the biggest thing to watch for is making sure the GPU supports DirectX11.1 and OpenGL 4.4. Dolphin emulates a console that functions very differently from a traditional PC, and uses the latest D3D and OGL features to reduce overhead. If you do not have those extensions, performance will suffer.

- **NVIDIA**: Any modern mid-range or better NVIDIA GPU will be able to play Dolphin in HD resolutions with [Ubershaders](https://dolphin-emu.org/blog/2017/07/30/ubershaders/) quite well. Old (10+ years) and/or low end GPUs may struggle, and are not recommended.

- **AMD**: Any modern mid-range or better AMD GPU will perform well in Dolphin with Ubershaders. AMD generally favors D3D over OpenGL, so we recommend D3D for these GPUs. Old (10+ years) and/or low end GPUs may struggle, and are not recommended.

- **Intel**: Iris Pro iGPUs will handle Dolphin well in D3D in Windows, though there are driver issues with the other graphics backends on that OS. A full fledged discrete graphics card is still highly recommended. IGPs older than the HD4000 are not supported.

### How much RAM do I need to run Dolphin?

2GB or more is recommended. RAM speed or the amount of RAM generally has no effect on emulation speed.

# Installation issues

### Which version of Dolphin should I download?

The latest beta version of Dolphin is a good choice to start with: our betas are well tested and should give a reliable experience. Development versions have the latest fixes and optimizations, but their constantly changing nature means that little testing has been done on them and unknown bugs may appear. Choose dev builds if you want to be on the bleeding edge of new features, and/or want to help with Dolphin's development.

Our buildbot provides each revision of Dolphin in four variants on the main site:

- **Windows x64** for 64-bit x86 Windows operating systems
- **Windows ARM64** for 64-bit ARM Windows operating systems
- **macOS** for 64-bit macOS computers, ARM or x86
- **Android** APKs for 64-bit Android

We no longer distribute Linux builds on our website, requiring users to build from source. Please see our [Building Dolphin on Linux](https://dolphin-emu.org/docs/guides/building-dolphin-linux/) guide for instructions.

Dolphin [does not support 32-bit operating systems](https://dolphin-emu.org/blog/2014/05/19/obituary-32bit/). To check if your version of Windows is compatible with 64-bit applications, open the Start Menu, right click on *Computer* and select the *Properties* option. A window should appear, showing "64-bit operating system" as the *System type* if your Windows version can run Dolphin x64. If you are running a 32-bit operating system, you should upgrade to a 64-bit version to better utilize the abilities of your hardware.

On Android, Dolphin also requires 64-bit (ARMv8 AArch64). To see if your Android phone has the necessary requirements, simply run the APK, and Dolphin will alert you.

Do note that sometimes various revisions may not have built correctly for all OSes, and some builds are missing. If this occurs, it will be fixed in a short time.

### "This program can't start because VC\_.dll is missing"

Dolphin now uses Visual Studio C++ 2022 on Windows. Windows users must have the latest Visual C++ 2015, 2017, 2019, and 2022 runtime installed in order to use Dolphin. If you ever encounter a MSVCP\_\_.dll or vcruntime\_\_.dll error, please download the latest Visual C++ runtime version from [Microsoft's website](https://aka.ms/vs/17/release/vc_redist.x64.exe).

Also, remember to extract Dolphin's files from the archive to a folder on your computer instead of running Dolphin directly from inside the archive.

### "This application has failed to start because XINPUT1_3.dll was not found"

Update and/or repair DirectX or reinstall the [Xbox 360 Controller Drivers](https://www.microsoft.com/accessories/en-ca/d/xbox-360-controller-for-windows).

### "The application was unable to start correctly (0xc000007b)"

When people see one of the error messages about vcomp100.dll or xinput1_3.dll missing they often download 32-bit builds of these files from the internet and expect them to work fine with 64-bit applications.

If you're suffering from this issue, make sure to delete any manually downloaded DLL files which are stored in your system paths and in the path where the Dolphin binary is stored and reinstall them with the proper runtime installers instead. Refer to the two questions above for further information.

# Configuration issues

### My Laptop / New GPU is not performing as well as it should

Laptops and modern GPUs use a variety of tricks to reduce their power consumption and overall temperature. Underclocking, reducing voltages, using integrated instead of discrete graphics, etc. Sometimes these tricks get in the way of Dolphin, and the system needs a little help to use its maximum capabilities with the emulator. Use the links below for assistance.

- [Windows](https://forums.dolphin-emu.org/Thread-laptop-performance-guide)
- [Linux](https://www.linux.org/threads/nvidia-optimus-on-linux.8873/)

### I configured the bindings for the second GC pad but it does not work

Make sure that the emulated GameCube port 2 is configured as a Standard Controller in the GameCube tab of the main configuration window. If the pad still does not work, check that your game can actually use a second GameCube controller.

# Common issues

### My audio is stuttering!

Sometimes when you're running a game you may run into occasions where Dolphin is unable to run full-speed. Because the emulated console isn't running full-speed, it doesn't output as much audio as Dolphin needs. As such there end up being gaps in the audio, commonly referred to as *audio stuttering* by users.

This is not actually an audio issue, but a performance issue. Audio stuttering can be avoided by running Dolphin full-speed, or, in the latest development builds, activating time-stretched audio. Time-stretched audio will "stretch" the currently output audio over the gaps, allowing the game to sound more natural at the cost of some audio latency.

### Game "X" does not run correctly

Even with a decade of work, Dolphin isn't a perfect emulator. This means you may encounter various issues that range from minor sound or graphics defects to game breaking errors and crashes. In order to provide users with as much information as possible, the Dolphin website hosts a [wiki](https://wiki.dolphin-emu.org/) with thousands of pages dedicated to games and various features of the emulator. Game Specific pages often list problems a game has, solutions, and what settings are needed to make it run as accurately as possible.

If you find a bug in a game that isn't listed on the Wiki, please checkout the [issue tracker](https://bugs.dolphin-emu.org/projects/emulator/issues) and see if it is reported there. If it isn't, feel free to report the bug you found so that the developers are aware of the issue. Be aware, one of the rules you must follow before reporting an issue is make sure the issue isn't already fixed on the latest development version.

### Dolphin speeds up when I open the graphics menu?

Dolphin is configured to run as fast as possible by default. However, for some games, that will cause a lot of problems, and they need more accurate and more demanding settings to run properly. For user convenience, many games have had these settings preconfigured in the "GameINI", a file with custom settings for each game.

**Note: The below is only relevant to Dolphin versions before [5.0-4171](https://dolphin-emu.org/blog/2017/07/01/dolphin-progress-report-june-2017/#50-4171-videoconfig-port-to-layered-configuration-system-by-merrymage)**

By opening the graphics menu, you are overriding the GameINI default settings and instead using the settings within the graphics menu, which will be the global defaults or whatever you last set them to. If you are playing a game that needs accurate but demanding settings, opening the graphics menu will disable those settings and result in a speed up. However, you will then be subject to the glitches and problems the GameINI settings were protecting you from.

See the [Dolphin Wiki](https://wiki.dolphin-emu.org/) for details on what games needs which settings to run correctly and why.

# Dolphin development

### How can I build Dolphin on my computer?

The build instructions are available on GitHub:

- [Windows build instructions](https://github.com/dolphin-emu/dolphin#building-for-windows)
- [Linux/macOS build instructions](https://github.com/dolphin-emu/dolphin#building-for-linux-and-macos)

### What is the best way to follow the development progress?

Builds are compiled for every development version of Dolphin and are available on the [download page](http://dolphin-emu.org/download/).

All of the Git commits are also available on [GitHub](https://github.com/dolphin-emu/dolphin/) where you can comment on changes and view new [pull requests](https://github.com/dolphin-emu/dolphin/pulls) to get a jump on upcoming features.

### I've got an idea to make Dolphin better, how should I tell the devs about it?

Most of the Dolphin developers read the ["Development discussion" forum](http://forums.dolphin-emu.org/Forum-development-discussion). Posting a thread there might be a good idea to get some feedback from developers but also from users.

Dolphin developers also communicate via IRC, which is better for instant discussion than a forum. Join us on `#dolphin-emu @ irc.libera.chat`.

Even if your idea is very good, note that developers are doing their work on Dolphin on their free time and don't necessarily have the time to implement everything people suggest. If you can, implementing a first draft of your idea might be a good way to get developers attention.

# Miscellaneous

### Couldn't Dolphin use more of my CPU cores to go faster?

CPUs do not work that way.

Every core on a CPU runs in parallel. Two tasks can run very well in parallel if they don't need to communicate often or to run at the exact same speed. For example, compressing files can be run on separate cores because compressing one file and compressing another file are two completely independent tasks, which do not need to communicate.

In Dolphin, the only demanding tasks that can run well in parallel are the CPU, the GPU and the DSP. Breaking up any of these tasks into smaller tasks just to run it on more cores is very likely to make the program slower. That's why Dolphin only runs on 3 cores and won't use all of your 4 or 6 cores CPU.

### Why do I need such a powerful computer to emulate an old console?

While it's true the GameCube and Wii hardware is a lot slower than what you need to emulate the console using Dolphin, the hardware found in these consoles is also very different from what you can find in a gaming PC. For example:

- Instead of an Intel or AMD x86 CPU, GameCube and Wii use an [IBM PowerPC](http://en.wikipedia.org/wiki/Gekko_(microprocessor)) CPU. Games are programmed for this CPU: when emulating, every basic instruction a game runs needs to be translated to something a PC can execute. Depending on the instruction, this can take from 2x to 100x clock cycles, which explains why you need more than a 486MHz CPU to emulate a GameCube.

- The RAM in these consoles is [SRAM](http://en.wikipedia.org/wiki/Static_random_access_memory), smaller but faster than the [SDRAM](http://en.wikipedia.org/wiki/SDRAM) used in a PC. It is also shared between CPU and GPU, which makes operations like texture uploads (CPU memory to GPU memory) or framebuffer copies (GPU memory to CPU memory) a lot less demanding than they are on a PC.

- The GPU is not using shaders: every graphics effect and every computation done by the game is executed directly by the hardware without an intermediate programming language. This does not match how a PC GPU works at all. Dolphin uses shaders on the PC GPU to translate what the GC GPU can do directly in hardware, causing it to run a lot slower.

- A PC runs an operating system in order to be able to run several programs at the same time. A GameCube or a Wii does not have the same requirement and can directly execute things on the hardware without going through the operating system, making a lot of communication between chips faster.

This list is not exhaustive but should give you a good idea of what exactly makes emulation require a powerful computer.

### Where can I download game ISOs/ROMs?

Short answer: You don't. Buy games and dump them with a Wii.

Long answer: Downloading commercial games is illegal and thus strongly frowned upon by the Dolphin developers. To prevent legal issues, this includes gray areas like downloading games which you purchased earlier. You don't necessarily need to own a gaming console by yourself because you can buy a game disc and dump them with a friend's console. On the other hand, copying a friend's game dump is considered illegal again.

For dumping games with a Wii, you'll want to install the homebrew channel and run an application like [CleanRip](http://wiibrew.org/wiki/CleanRip).

### What dump formats are supported by Dolphin?

Dolphin supports playing games dumped in the following formats:

- GCM/ISO (uncompressed dumps, should be 1.4GB for GameCube games and 4.7GB for Wii games)
- GCZ \*
- CISO
- WBFS
- WIA \*
- NFS (Wii games purchased from the Wii U eShop)
- [RVZ](https://dolphin-emu.org/blog/2020/07/05/dolphin-progress-report-may-and-june-2020/#50-12188-support-for-rvz-and-wia-disc-formats-by-josjuice) \*

Note that WBFS and CISO are lossy compression formats: they remove some of the unused information stored on the discs to make files smaller. If you wish to compress your dumps to save space, we recommend RVZ.

\* Dolphin can be used to compress your games to this format

© Dolphin Emulator Project - [Website Source Code](https://github.com/dolphin-emu/www) - [Privacy Policy](/docs/privacy/) [Mastodon verification](https://social.dolphin-emu.org/@dolphin)
