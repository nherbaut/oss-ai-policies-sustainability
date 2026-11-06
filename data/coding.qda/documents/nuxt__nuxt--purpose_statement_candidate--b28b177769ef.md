[![Nuxt banner](./.github/assets/banner.svg)](https://nuxt.com)

# Nuxt

[![Version](https://npmx.dev/api/registry/badge/version/nuxt)](https://npmx.dev/package/nuxt) [![Downloads](https://npmx.dev/api/registry/badge/downloads/nuxt)](https://npmx.dev/package/nuxt) [![License](https://img.shields.io/github/license/nuxt/nuxt.svg?style=flat&colorA=18181B&colorB=28CF8D)](https://github.com/nuxt/nuxt/blob/main/LICENSE) [![Modules](https://img.shields.io/badge/dynamic/json?url=https://nuxt.com/api/v1/modules&query=$.stats.modules&label=Modules&style=flat&colorA=18181B&colorB=28CF8D)](https://nuxt.com/modules) [![Website](https://img.shields.io/badge/Nuxt%20Docs-18181B?logo=nuxt)](https://nuxt.com) [![Discord](https://img.shields.io/badge/Nuxt%20Discord-18181B?logo=discord)](https://chat.nuxt.dev) [![Nuxt openssf scorecard score](https://api.securityscorecards.dev/projects/github.com/nuxt/nuxt/badge)](https://securityscorecards.dev/viewer/?uri=github.com/nuxt/nuxt) [![Ask DeepWiki](https://deepwiki.com/badge.svg)](https://deepwiki.com/nuxt/nuxt)

Nuxt is a free and open-source framework with an intuitive and extendable way to create type-safe, performant and production-grade full-stack web applications and websites with Vue.js.

It provides a number of features that make it easy to build fast, SEO-friendly, and scalable web applications, including: - Server-side rendering, static site generation, hybrid rendering and edge-side rendering - Automatic routing with code-splitting and pre-fetching - Data fetching and state management - Search engine optimization and defining meta tags - Auto imports of components, composables and utils - TypeScript with zero configuration - Go full-stack with our server/ directory - Extensible with [300+ modules](https://nuxt.com/modules) - Deployment to a variety of [hosting platforms](https://nuxt.com/deploy) - ...[and much more](https://nuxt.com) 🚀

### Table of Contents

- 🚀 [Getting Started](#getting-started)
- 💻 [Vue Development](#vue-development)
- 📖 [Documentation](#documentation)
- 🧩 [Modules](#modules)
- ❤️ [Contribute](#contribute)
- 🏠 [Local Development](#local-development)
- 🛟 [Professional Support](#professional-support)
- 🔗 [Follow Us](#follow-us)
- ⚖️ [License](#license)

------------------------------------------------------------------------

## 🚀 Getting Started

Use the following command to create a new starter project. This will create a starter project with all the necessary files and dependencies:

``` bash
npm create nuxt@latest <my-project>
```

> \[!TIP\] Discover also [nuxt.new](https://nuxt.new): Open a Nuxt starter on CodeSandbox, StackBlitz or locally to get up and running in a few seconds.

## 💻 Vue Development

Simple, intuitive and powerful, Nuxt lets you write Vue components in a way that makes sense. Every repetitive task is automated, so you can focus on writing your full-stack Vue application with confidence.

Example of an `app.vue`:

``` vue
<script setup lang="ts">
useSeoMeta({
  title: 'Meet Nuxt',
  description: 'The Intuitive Vue Framework.',
})
</script>

<template>
  <div id="app">
    <AppHeader />
    <NuxtPage />
    <AppFooter />
  </div>
</template>

<style scoped>
#app {
  background-color: #020420;
  color: #00DC82;
}
</style>
```

## 📖 Documentation

We highly recommend you take a look at the [Nuxt documentation](https://nuxt.com/docs) to level up. It’s a great resource for learning more about the framework. It covers everything from getting started to advanced topics.

## 🧩 Modules

Discover our [list of modules](https://nuxt.com/modules) to supercharge your Nuxt project, created by the Nuxt team and community.

## ❤️ Contribute

We invite you to contribute and help improve Nuxt 💚

Here are a few ways you can get involved: - **Reporting Bugs:** If you come across any bugs or issues, please check out the [reporting bugs guide](https://nuxt.com/docs/4.x/community/reporting-bugs) to learn how to submit a bug report. - **Suggestions:** Have ideas to enhance Nuxt? We'd love to hear them! Check out the [contribution guide](https://nuxt.com/docs/4.x/community/contribution) to share your suggestions. - **Questions:** If you have questions or need assistance, the [getting help guide](https://nuxt.com/docs/4.x/community/getting-help) provides resources to help you out.

## 🏠 Local Development

Follow the docs to [Set Up Your Local Development Environment](https://nuxt.com/docs/4.x/community/framework-contribution#setup) to contribute to the framework and documentation.

## 🛟 Professional Support

- Technical audit & consulting: [Nuxt Experts](https://nuxt.com/enterprise/support)
- Custom development & more: [Nuxt Agencies Partners](https://nuxt.com/enterprise/agencies)

## 🔗 Follow Us

[![Discord](./.github/assets/discord.svg)](https://go.nuxt.com/discord)  [![Twitter](./.github/assets/twitter.svg)](https://go.nuxt.com/x)  [![GitHub](./.github/assets/github.svg)](https://go.nuxt.com/github)  [![Bluesky](./.github/assets/bluesky.svg)](https://go.nuxt.com/bluesky)

## ⚖️ License

[MIT](https://github.com/nuxt/nuxt/blob/main/LICENSE)
