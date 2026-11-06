[![Budibase](https://res.cloudinary.com/daog6scxm/image/upload/v1696515725/Branding/Assets/Symbol/RGB/Full%20Colour/Budibase_Symbol_RGB_FullColour_cbqvha_1_z5cwq2.svg)](https://www.budibase.com)

# Budibase

### AI Agents that run your operations

Budibase is an open-source operations platform that saves engineers 100s of hours building Agents, Apps and Automations, securely.

### 🤖 🎨 🚀

![Budibase agent ui](https://res.cloudinary.com/daog6scxm/image/upload/v1775572268/github/Agent_preview.jpg)

[![GitHub all releases](https://img.shields.io/github/downloads/Budibase/budibase/total)](https://github.com/Budibase/budibase/releases) [![GitHub release (latest by date)](https://img.shields.io/github/v/release/Budibase/budibase)](https://github.com/Budibase/budibase/releases) [![Follow @budibase](https://img.shields.io/twitter/follow/budibase?style=social)](https://twitter.com/intent/follow?screen_name=budibase) ![Code of conduct](https://img.shields.io/badge/Contributor%20Covenant-v2.0%20adopted-ff69b4.svg) [![](https://codecov.io/gh/Budibase/budibase/graph/badge.svg?token=E8W2ZFXQOH)](https://codecov.io/gh/Budibase/budibase)

### [Get started - we host (Budibase Cloud)](https://account.budibase.app/register)  ·  [Get started - you host (Docker, K8s, DO)](https://docs.budibase.com/docs/hosting-methods)  ·  [Docs](https://docs.budibase.com/docs)  ·  [Feature request](https://github.com/Budibase/budibase/discussions?discussions_q=category%3AIdeas)  ·  [Report a bug](https://github.com/Budibase/budibase/issues)  ·  Support: [Discussions](https://github.com/Budibase/budibase/discussions)

## ✨ Features

### Run your operations on one platform

Handle requests, automate workflows, manage processes, and connect your business systems - without stitching together multiple tools.

Employees ask questions, request approvals, and report issues every day. Budibase agents understand these requests and handle the work automatically.

### Operations your team can run with AI agents

Employees ask questions, request approvals, and report issues every day. Budibase agents understand these requests and handle the work automatically.

![Budibase chat deploy](https://res.cloudinary.com/daog6scxm/image/upload/v1775573887/github/Agent_Chat.jpg)

### Agents that take action

Budibase agents don’t just answer questions. They run workflows across your business - creating records, routing approvals, updating apps, and notifying teams automatically.

![Budibase agent actions](https://res.cloudinary.com/daog6scxm/image/upload/v1775572270/github/Agent_Actions.jpg)

### Connect the tools your business runs on

Integrate with databases, AI models, and business apps so agents and automations can take action across your operations.

### Deploy with confidence and security

Budibase is open-source and is made to scale. With Budibase, you can self-host on your own infrastructure and globally manage users, onboarding, SMTP, apps, groups, theming and more. You can also provide users/groups with a portal and disseminate user management to the group manager.

------------------------------------------------------------------------

## Budibase Public API

As with anything that we build in Budibase, our public API is simple to use, flexible, and introduces new extensibility. To summarize, the Budibase API enables:

- Budibase as a backend
- Interoperability

#### Docs

You can learn more about the Budibase API at the following places:

- [General documentation](https://docs.budibase.com/docs/public-api): Learn how to get your API key, how to use spec, and how to use Postman
- [Interactive API documentation](https://docs.budibase.com/reference/appcreate) : Learn how to interact with the API

## 🏁 Get started

Deploy Budibase using Docker, Kubernetes, and Digital Ocean on your existing infrastructure. Or use Budibase Cloud if you don't need to self-host and would like to get started quickly.

### [Get started with self-hosting Budibase](https://docs.budibase.com/docs/hosting-methods)

- [Docker - single ARM compatible image](https://docs.budibase.com/docs/docker)
- [Docker Compose](https://docs.budibase.com/docs/docker-compose)
- [Kubernetes](https://docs.budibase.com/docs/kubernetes-k8s)
- [Digital Ocean](https://docs.budibase.com/docs/digitalocean)
- [Portainer](https://docs.budibase.com/docs/portainer)

### [Get started with Budibase Cloud](https://budibase.com)

## 🎓 Learning Budibase

The Budibase documentation [lives here](https://docs.budibase.com/docs).  

## 💬 Community

If you have a question or would like to talk with other Budibase users and join our community, please hop over to [Github discussions](https://github.com/Budibase/budibase/discussions)

## ❗ Code of conduct

Budibase is dedicated to providing everyone a welcoming, diverse, and harassment-free experience. We expect everyone in the Budibase community to abide by our [**Code of Conduct**](https://github.com/Budibase/budibase/blob/HEAD/docs/CODE_OF_CONDUCT.md). Please read it.  

## 🙌 Contributing to Budibase

From opening a bug report to creating a pull request: every contribution is appreciated and welcomed. If you're planning to implement a new feature or change the API, please create an issue first. This way, we can ensure your work is not in vain. Environment setup instructions are available [here](https://github.com/Budibase/budibase/tree/HEAD/docs/CONTRIBUTING.md).

### Not Sure Where to Start?

A good place to start contributing is by looking for the [good first issue](https://github.com/Budibase/budibase/labels/good%20first%20issue) tag.

### How the repository is organized

Budibase is a monorepo managed by lerna. Lerna manages the building and publishing of the budibase packages. At a high level, here are the packages that make up Budibase.

- [packages/builder](https://github.com/Budibase/budibase/tree/HEAD/packages/builder) - contains code for the budibase builder client-side svelte application.

- [packages/client](https://github.com/Budibase/budibase/tree/HEAD/packages/client) - A module that runs in the browser responsible for reading JSON definition and creating living, breathing web apps from it.

- [packages/server](https://github.com/Budibase/budibase/tree/HEAD/packages/server) - The budibase server. This Koa app is responsible for serving the JS for the builder and budibase apps, as well as providing the API for interaction with the database and file system.

For more information, see [CONTRIBUTING.md](https://github.com/Budibase/budibase/blob/HEAD/docs/CONTRIBUTING.md)

## 📝 License

Budibase is open-source, licensed as [GPL v3](https://www.gnu.org/licenses/gpl-3.0.en.html). The client and component libraries are licensed as [MPL](https://directory.fsf.org/wiki/License:MPL-2.0) - so the apps you build can be licensed however you like. Budibase paid features are licensed under the [Business Source License](https://github.com/Budibase/budibase/blob/master/packages/pro/license.md),

## ⭐ Stargazers over time

[![Stargazers over time](https://starchart.cc/Budibase/budibase.svg)](https://starchart.cc/Budibase/budibase)

If you are having issues between updates of the builder, please use the guide [here](https://github.com/Budibase/budibase/blob/HEAD/docs/CONTRIBUTING.md#troubleshooting) to clear down your environment.

## Contributors ✨

Thanks goes to these wonderful people ([emoji key](https://allcontributors.org/docs/en/emoji-key)):

[![](https://contrib.rocks/image?repo=Budibase/budibase)](https://github.com/Budibase/budibase/graphs/contributors)

Made with [contrib.rocks](https://contrib.rocks).
