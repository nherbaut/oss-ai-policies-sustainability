Toggle the table of contents

# About Nura

- [Page](/wiki/About_Nura "View the content page [c]")
- [Discussion](/index.php?title=Talk:About_Nura&action=edit&redlink=1 "Discussion about the content page (page does not exist) [t]")

English

- [Read](/wiki/About_Nura)
- [View source](/index.php?title=About_Nura&action=edit "This page is protected. You can view its source [e]")
- [View history](/index.php?title=About_Nura&action=history "Past revisions of this page [h]")

Tools

Tools

move to sidebar

hide

Actions

- [Read](/wiki/About_Nura)
- [View source](/index.php?title=About_Nura&action=edit)
- [View history](/index.php?title=About_Nura&action=history)

General

- [What links here](/wiki/Special:WhatLinksHere/About_Nura "A list of all wiki pages that link here [j]")
- [Related changes](/wiki/Special:RecentChangesLinked/About_Nura "Recent changes in pages linked from this page [k]")
- [Special pages](/wiki/Special:SpecialPages "A list of all special pages [q]")
- [Printable version](javascript:print(); "Printable version of this page [p]")
- [Permanent link](/index.php?title=About_Nura&oldid=107221 "Permanent link to this revision of this page")
- [Page information](/index.php?title=About_Nura&action=info "More information about this page")
- [Cargo data](/index.php?title=About_Nura&action=pagevalues)

Appearance

move to sidebar

hide

From Nura Wiki

(Redirected from [About postmarketOS](/index.php?title=About_postmarketOS&redirect=no "About postmarketOS"))

[Nura](https://nura.eco/) extends the [free and open source](https://en.wikipedia.org/wiki/Free_software) operating system [Alpine Linux](https://alpinelinux.org/about/) to run on smartphones and other mobile devices. Alpine is a security-oriented, light-weight Linux distribution based on [musl libc](https://musl.libc.org/) and [BusyBox](https://busybox.net/).

Currently, Nura is for Linux enthusiasts. In the long term, Nura shall empower ordinary people to be in control of their phone (and not the other way around).

Until 27 September 2026, Nura was called postmarketOS.

## Status

Nura is for Linux enthusiasts. The more complete [device ports](/wiki/Devices "Devices") (mostly aarch64 devices in main and community categories) are capable of running modern mobile interfaces [Phosh](/wiki/Phosh "Phosh"), [Plasma Mobile](/wiki/Plasma_Mobile "Plasma Mobile") and [Sxmo](/wiki/Sxmo "Sxmo").

Other interfaces and devices are either for testing or serve a special purpose. For example, because of its hardware keyboard, one can use the classic [N900](/wiki/Nokia_N900_(nokia-n900) "Nokia N900 (nokia-n900)") with [i3wm](/wiki/I3wm "I3wm").

## Principles

Decisions related to development of Nura are done with the following principles in mind.

### Developer facing

#### Easy to modify

Nura should be easy to modify and it should be easy to contribute the changes back.

Examples:

- All packages in one [pmaports.git](/wiki/Pmaports.git "Pmaports.git") repository
- Simple packaging format [APKBUILD](https://wiki.alpinelinux.org/wiki/APKBUILD_Reference)
- [pmbootstrap](/wiki/Pmbootstrap "Pmbootstrap") makes it easy to:
  - Create a custom installation
  - Cross compile packages
  - Build packages from local source tree
  - Create foreign arch chroots
  - Reset the chroots to start over
- It's easy to enable SSH
- Lots of CI scripts assist in contributing changes back

#### Sustainable and maintainable

Nura should have maintainable code and packages. When patching software to fix builds or to fit our needs, we attempt to upstream everything that makes sense. [Device specific](/wiki/Device_specific_package "Device specific package") code and configuration should be minimal.

Devices in the [main category](/wiki/Device_categorization "Device categorization") must use a [(close to) mainline](/wiki/(Close_to)_Mainline "(Close to) Mainline") kernel.

Related:

- [Guidelines for packaging patches](/wiki/Create_a_package#Guidelines_for_packaging_patches "Create a package")

#### Minimal base

It must be possible to install a minimal version of Nura.

Use case example:

- Mainlining a new device with a minimal rootfs

#### Infrastructure

The infrastructure of Nura should consist of free and open source software.

### User facing

#### Polished

Apps should make sense together and not give conflicting instructions. Broken features shall be disabled.

Examples:

- [pmaports!1449](https://gitlab.postmarketos.org/postmarketOS/pmaports/-/merge_requests/1449#note_385456592%7C): first run screen of GNOME software disabled
- [pmaports!1443](https://gitlab.nura.eco/nura/pmaports/-/merge_requests/1443): broken "logout" button in Phosh hidden

#### Avoid distractions

User interfaces and apps should aid users in their workflows, and not distract them.

["How Technology is Hijacking Your Mind"](https://medium.com/thrive-global/how-technology-hijacks-peoples-minds-from-a-magician-and-google-s-design-ethicist-56d62ef5edf3) is an excellent article on this topic, illustrating how this is a problem with current mainstream smartphone OS and apps. Examples for distractions:

- Advertising
- Notifications for unimportant events
- "Recommendations" to try out specific features
- Autoplay of next videos

#### Prefer free software services

Integrations with services that run on proprietary software, or provide proprietary software, should not be enabled by default or recommended. But it should still be easy to enable them if the user desires (by having them behind an "additional providers" button or similar). If we have no means to test if integration with a proprietary service is working or not, we shall disable it.

Examples for proprietary services:

- Flatpak + Flathub
- YouTube

Related issues:

- [pmaports#725](https://gitlab.nura.eco/nura/pmaports/-/work_items/725): gnome-online-accounts: hide / disable proprietary services

#### Reliable

Updates should not break Nura on the [stable channel](https://nura.eco/blog/2020/05/31/three-years/#stable-release-channel). Long term, it would be great to allow users to recover from failed updates.

Related issues:

- [pmaports#492](https://gitlab.nura.eco/nura/pmaports/-/work_items/492): make it possible to roll back upgrades

#### Privacy friendly

##### Encryption

The user's data should be protected with encryption unless they explicitly choose to use an unencrypted communication channel. Full disk encryption has been implemented since day one in Nura.

Long term, we should push towards integrating and preferring end-to-end encrypted communication.

Related issues:

- [pmaports#726](https://gitlab.nura.eco/nura/pmaports/-/work_items/726): Integrate EteSync into Phosh / Plasma Mobile on Nura

##### Security

Nura should use state-of-the-art security to protect the user's data from malicious input, such as websites or PDF documents.

Related issues:

- [pmaports#1596](https://gitlab.nura.eco/nura/pmaports/-/work_items/1596): privilege separation

##### Avoid tracking

Long term, it should be hard to fingerprint the user and collect data about them when they use Nura. (Currently we have merely changed the user-agents to something more generic.)

Related issues:

- [pmaports#727](https://gitlab.nura.eco/nura/pmaports/-/work_items/727): Phosh: bluetooth is always re-enabled after boot

#### No vendor lock-in

In Nura, we aim to build generic software solutions (programs, apps, ...), which can be adapted by other distributions if they choose to do so. Branding should be optional and sane patches to make our software work better on other systems should be accepted.

This benefits the user, as it is easier for them to switch between distributions. Also it makes development easier, because instead of each project developing their own solution for certain problems, we can work together.

Examples:

- osk-sdl
- mobile-config-firefox
- on-device installer (distro-agnostic components now live upstream, Nura specific branding is in a separate repository called postmarketos-ondev)
- megapixels

Retrieved from "[https://wiki.nura.eco/index.php?title=About_Nura&oldid=107221](https://wiki.nura.eco/index.php?title=About_Nura&oldid=107221)"
