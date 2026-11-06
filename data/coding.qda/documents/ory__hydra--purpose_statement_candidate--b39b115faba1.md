# ![Ory Hydra - Open Source OAuth 2 and OpenID Connect server](https://raw.githubusercontent.com/ory/meta/master/static/banners/hydra.svg)

#### [Chat](https://www.ory.com/chat) · [Discussions](https://github.com/ory/hydra/discussions) · [Newsletter](https://www.ory.com/l/sign-up-newsletter) · [Docs](https://www.ory.com/docs/) · [Try Ory Network](https://console.ory.sh/) · [Jobs](https://www.ory.com/jobs/)

Ory Hydra is a hardened, OpenID Certified OAuth 2.0 Server and OpenID Connect Provider optimized for low-latency, high throughput, and low resource consumption. It connects to your existing identity provider through a login and consent app, giving you absolute control over the user interface and experience.

------------------------------------------------------------------------

- [What is Ory Hydra?](#what-is-ory-hydra)
  - [Why Ory Hydra](#why-ory-hydra)
  - [OAuth2 and OpenID Connect: Open Standards](#oauth2-and-openid-connect-open-standards)
  - [OpenID Connect Certified](#openid-connect-certified)
- [Deployment options](#deployment-options)
  - [Use Ory Hydra on the Ory Network](#use-ory-hydra-on-the-ory-network)
  - [Self-host Ory Hydra](#self-host-ory-hydra)
- [Quickstart](#quickstart)
- [Who is using Ory Hydra](#who-is-using-ory-hydra)
- [Ecosystem](#ecosystem)
  - [Ory Kratos: Identity and User Infrastructure and Management](#ory-kratos-identity-and-user-infrastructure-and-management)
  - [Ory Hydra: OAuth2 & OpenID Connect Server](#ory-hydra-oauth2--openid-connect-server)
  - [Ory Oathkeeper: Identity & Access Proxy](#ory-oathkeeper-identity--access-proxy)
  - [Ory Keto: Access Control Policies as a Server](#ory-keto-access-control-policies-as-a-server)
- [Documentation](#documentation)
- [Developing Ory Hydra](#developing-ory-hydra)
- [Security](#security)
  - [Disclosing vulnerabilities](#disclosing-vulnerabilities)
- [Telemetry](#telemetry)
- [Libraries and third-party projects](#libraries-and-third-party-projects)

## What is Ory Hydra?

Ory Hydra is a server implementation of the OAuth 2.0 authorization framework and the OpenID Connect Core 1.0. It follows [cloud architecture best practices](https://www.ory.com/docs/ecosystem/software-architecture-philosophy) and focuses on:

- OAuth 2.0 and OpenID Connect flows
- Token issuance and validation
- Client management
- Consent and login flow orchestration
- JWKS management
- Low latency and high throughput

We recommend starting with the [Ory Hydra introduction docs](https://www.ory.com/docs/hydra) to learn more about its architecture, feature set, and how it compares to other systems.

### Why Ory Hydra

Ory Hydra is designed to:

- Be a standalone OAuth 2.0 and OpenID Connect server without user management
- Connect to any existing identity provider through a login and consent app
- Give you absolute control over the user interface and experience flows
- Work with any authentication endpoint: [Ory Kratos](https://github.com/ory/kratos), [authboss](https://github.com/go-authboss/authboss), [User Frosting](https://www.userfrosting.com/), or your proprietary system
- Scale to large numbers of clients and tokens
- Fit into modern cloud native environments such as Kubernetes and managed platforms

### OAuth2 and OpenID Connect: Open Standards

Ory Hydra implements Open Standards set by the IETF:

- [The OAuth 2.0 Authorization Framework](https://tools.ietf.org/html/rfc6749)
- [OAuth 2.0 Threat Model and Security Considerations](https://tools.ietf.org/html/rfc6819)
- [OAuth 2.0 Token Revocation](https://tools.ietf.org/html/rfc7009)
- [OAuth 2.0 Token Introspection](https://tools.ietf.org/html/rfc7662)
- [OAuth 2.0 for Native Apps](https://tools.ietf.org/html/draft-ietf-oauth-native-apps-10)
- [OAuth 2.0 Dynamic Client Registration Protocol](https://datatracker.ietf.org/doc/html/rfc7591)
- [OAuth 2.0 Dynamic Client Registration Management Protocol](https://datatracker.ietf.org/doc/html/rfc7592)
- [Proof Key for Code Exchange by OAuth Public Clients](https://tools.ietf.org/html/rfc7636)
- [JSON Web Token (JWT) Profile for OAuth 2.0 Client Authentication and Authorization Grants](https://tools.ietf.org/html/rfc7523)

and the OpenID Foundation:

- [OpenID Connect Core 1.0](http://openid.net/specs/openid-connect-core-1_0.html)
- [OpenID Connect Discovery 1.0](https://openid.net/specs/openid-connect-discovery-1_0.html)
- [OpenID Connect Dynamic Client Registration 1.0](https://openid.net/specs/openid-connect-registration-1_0.html)
- [OpenID Connect Front-Channel Logout 1.0](https://openid.net/specs/openid-connect-frontchannel-1_0.html)
- [OpenID Connect Back-Channel Logout 1.0](https://openid.net/specs/openid-connect-backchannel-1_0.html)

### OpenID Connect Certified

Ory Hydra is an OpenID Foundation [certified OpenID Provider (OP)](http://openid.net/certification/#OPs).

![Ory Hydra is a certified OpenID Providier](https://github.com/ory/docs/blob/master/docs/hydra/images/oidc-cert.png)

The following OpenID profiles are certified:

- [Basic OpenID Provider](http://openid.net/specs/openid-connect-core-1_0.html#CodeFlowAuth) (response types `code`)
- [Implicit OpenID Provider](http://openid.net/specs/openid-connect-core-1_0.html#ImplicitFlowAuth) (response types `id_token`, `id_token+token`)
- [Hybrid OpenID Provider](http://openid.net/specs/openid-connect-core-1_0.html#HybridFlowAuth) (response types `code+id_token`, `code+id_token+token`, `code+token`)
- [OpenID Provider Publishing Configuration Information](https://openid.net/specs/openid-connect-discovery-1_0.html)
- [Dynamic OpenID Provider](https://openid.net/specs/openid-connect-registration-1_0.html)

To obtain certification, we deployed the [reference user login and consent app](https://github.com/ory/hydra-login-consent-node) (unmodified) and Ory Hydra v1.0.0.

## Deployment options

You can run Ory Hydra in two main ways:

- As a managed service on the Ory Network
- As a self hosted service under your own control, with or without the Ory Enterprise License

### Use Ory Hydra on the Ory Network

The [Ory Network](https://www.ory.com/cloud) is the fastest way to use Ory services in production. **Ory OAuth2 & OpenID Connect** is powered by the open source Ory Hydra server and is API compatible.

The Ory Network provides:

- OAuth2 and OpenID Connect for single sign on, API access, and machine to machine authorization
- Identity and credential management that scales to billions of users and devices
- Registration, login, and account management flows for passkeys, biometrics, social login, SSO, and multi factor authentication
- Prebuilt login, registration, and account management pages and components
- Low latency permission checks based on the Zanzibar model with the Ory Permission Language
- GDPR friendly storage with data locality and compliance in mind
- Web based Ory Console and Ory CLI for administration and operations
- Cloud native APIs compatible with the open source servers
- Fair, usage based [pricing](https://www.ory.com/pricing)

Sign up for a [free developer account](https://console.ory.sh/registration?utm_source=github&utm_medium=banner&utm_campaign=hydra-readme) to get started.

### Self-host Ory Hydra

You can run Ory Hydra yourself for full control over infrastructure, deployment, and customization.

The [install guide](https://www.ory.com/docs/hydra/install) explains how to:

- Install Hydra on Linux, macOS, Windows, and Docker
- Configure databases such as PostgreSQL, MySQL, and CockroachDB
- Deploy to Kubernetes and other orchestration systems
- Build Hydra from source

This guide uses the open source distribution to get you started without license requirements. It is a great fit for individuals, researchers, hackers, and companies that want to experiment, prototype, or run unimportant workloads without SLAs. You get the full core engine, and you are free to inspect, extend, and build it from source.

If you run Hydra as part of a business-critical system, for example OAuth2 and OpenID Connect for all your users, you should use a commercial agreement to reduce operational and security risk. The **Ory Enterprise License (OEL)** layers on top of self-hosted Hydra and provides:

- Additional enterprise features that are not available in the open source version
- Regular security releases, including CVE patches, with service level agreements
- Support for advanced scaling, multi-tenancy, and complex deployments
- Premium support options with SLAs, direct access to engineers, and onboarding help
- Access to a private Docker registry with frequent and vetted, up-to-date enterprise builds

For guaranteed CVE fixes, current enterprise builds, advanced features, and support in production, you need a valid [Ory Enterprise License](https://www.ory.com/ory-enterprise-license) and access to the Ory Enterprise Docker registry. To learn more, [contact the Ory team](https://www.ory.com/contact/).

## Quickstart

Install the [Ory CLI](https://www.ory.com/docs/guides/cli/installation) and create a new project to try Ory OAuth2 & OpenID Connect.

``` bash
# Install the Ory CLI if you do not have it yet:
bash <(curl https://raw.githubusercontent.com/ory/meta/master/install.sh) -b . ory
sudo mv ./ory /usr/local/bin/

# Sign in or sign up
ory auth

# Create a new project
ory create project --create-workspace "Ory Open Source" --name "GitHub Quickstart" --use-project
```

Try out the OAuth 2.0 Client Credentials flow:

``` bash
ory create oauth2-client \
    --name "Client Credentials Demo" \
    --grant-type client_credentials
# Note the client ID and secret from output

ory perform client-credentials \
    --client-id <your-client-id> \
    --client-secret <your-client-secret>
# Note the access token from output

ory introspect token <your-access-token>
```

Try out the OAuth 2.0 Authorize Code + OpenID Connect flow:

``` bash
ory create oauth2-client \
    --name "Authorize Code with OpenID Connect Demo" \
    --grant-type authorization_code,refresh_token \
    --response-type code \
    --redirect-uri http://127.0.0.1:4446/callback

ory perform authorization-code \
    --client-id <your-client-id> \
    --client-secret <your-client-secret>
```

## Who is using Ory Hydra

The Ory community stands on the shoulders of individuals, companies, and maintainers. The Ory team thanks everyone involved - from submitting bug reports and feature requests, to contributing patches and documentation. The Ory community counts more than 50.000 members and is growing. The Ory stack protects 7.000.000.000+ API requests every day across thousands of companies. None of this would have been possible without each and everyone of you!

The following list represents companies that have accompanied us along the way and that have made outstanding contributions to our ecosystem. *If you think that your company deserves a spot here, reach out to <office@ory.com> now*!

| Name | Logo | Website | Case Study |
|----|:--:|----|----|
| OpenAI | ![OpenAI](https://raw.githubusercontent.com/ory/meta/master/static/adopters/dark/openai.svg) | [openai.com](https://openai.com/) | [OpenAI Case Study](https://www.ory.com/case-studies/openai) |
| Fandom | ![Fandom](https://raw.githubusercontent.com/ory/meta/master/static/adopters/dark/fandom.svg) | [fandom.com](https://www.fandom.com/) | [Fandom Case Study](https://www.ory.com/case-studies/fandom) |
| Lumin | ![Lumin](https://raw.githubusercontent.com/ory/meta/master/static/adopters/dark/lumin.svg) | [luminpdf.com](https://www.luminpdf.com/) | [Lumin Case Study](https://www.ory.com/case-studies/lumin) |
| Sencrop | ![Sencrop](https://raw.githubusercontent.com/ory/meta/master/static/adopters/dark/sencrop.svg) | [sencrop.com](https://sencrop.com/) | [Sencrop Case Study](https://www.ory.com/case-studies/sencrop) |
| OSINT Industries | ![OSINT Industries](https://raw.githubusercontent.com/ory/meta/master/static/adopters/dark/osint.svg) | [osint.industries](https://www.osint.industries/) | [OSINT Industries Case Study](https://www.ory.com/case-studies/osint) |
| HGV | ![HGV](https://raw.githubusercontent.com/ory/meta/master/static/adopters/dark/hgv.svg) | [hgv.it](https://www.hgv.it/) | [HGV Case Study](https://www.ory.com/case-studies/hgv) |
| Maxroll | ![Maxroll](https://raw.githubusercontent.com/ory/meta/master/static/adopters/dark/maxroll.svg) | [maxroll.gg](https://maxroll.gg/) | [Maxroll Case Study](https://www.ory.com/case-studies/maxroll) |
| Zezam | ![Zezam](https://raw.githubusercontent.com/ory/meta/master/static/adopters/dark/zezam.svg) | [zezam.io](https://www.zezam.io/) | [Zezam Case Study](https://www.ory.com/case-studies/zezam) |
| T.RowePrice | ![T.RowePrice](https://raw.githubusercontent.com/ory/meta/master/static/adopters/dark/troweprice.svg) | [troweprice.com](https://www.troweprice.com/) |  |
| Mistral | ![Mistral](https://raw.githubusercontent.com/ory/meta/master/static/adopters/dark/mistral.svg) | [mistral.ai](https://www.mistral.ai/) |  |
| Axel Springer | ![Axel Springer](https://raw.githubusercontent.com/ory/meta/master/static/adopters/dark/axelspringer.svg) | [axelspringer.com](https://www.axelspringer.com/) |  |
| Hemnet | ![Hemnet](https://raw.githubusercontent.com/ory/meta/master/static/adopters/dark/hemnet.svg) | [hemnet.se](https://www.hemnet.se/) |  |
| Cisco | ![Cisco](https://raw.githubusercontent.com/ory/meta/master/static/adopters/dark/cisco.svg) | [cisco.com](https://www.cisco.com/) |  |
| Presidencia de la República Dominicana | ![Presidencia de la República Dominicana](https://raw.githubusercontent.com/ory/meta/master/static/adopters/dark/republica-dominicana.svg) | [presidencia.gob.do](https://www.presidencia.gob.do/) |  |
| Moonpig | ![Moonpig](https://raw.githubusercontent.com/ory/meta/master/static/adopters/dark/moonpig.svg) | [moonpig.com](https://www.moonpig.com/) |  |
| Booster | ![Booster](https://raw.githubusercontent.com/ory/meta/master/static/adopters/dark/booster.svg) | [choosebooster.com](https://www.choosebooster.com/) |  |
| Zaptec | ![Zaptec](https://raw.githubusercontent.com/ory/meta/master/static/adopters/dark/zaptec.svg) | [zaptec.com](https://www.zaptec.com/) |  |
| Klarna | ![Klarna](https://raw.githubusercontent.com/ory/meta/master/static/adopters/dark/klarna.svg) | [klarna.com](https://www.klarna.com/) |  |
| Raspberry PI Foundation | ![Raspberry PI Foundation](https://raw.githubusercontent.com/ory/meta/master/static/adopters/dark/raspi.svg) | [raspberrypi.org](https://www.raspberrypi.org/) |  |
| Tulip | ![Tulip Retail](https://raw.githubusercontent.com/ory/meta/master/static/adopters/dark/tulip.svg) | [tulip.com](https://tulip.com/) |  |
| Hootsuite | ![Hootsuite](https://raw.githubusercontent.com/ory/meta/master/static/adopters/dark/hootsuite.svg) | [hootsuite.com](https://hootsuite.com/) |  |
| Segment | ![Segment](https://raw.githubusercontent.com/ory/meta/master/static/adopters/dark/segment.svg) | [segment.com](https://segment.com/) |  |
| Arduino | ![Arduino](https://raw.githubusercontent.com/ory/meta/master/static/adopters/dark/arduino.svg) | [arduino.cc](https://www.arduino.cc/) |  |
| Sainsbury's | ![Sainsbury's](https://raw.githubusercontent.com/ory/meta/master/static/adopters/dark/sainsburys.svg) | [sainsburys.co.uk](https://www.sainsburys.co.uk/) |  |
| Contraste | ![Contraste](https://raw.githubusercontent.com/ory/meta/master/static/adopters/dark/contraste.svg) | [contraste.com](https://www.contraste.com/en) |  |
| inMusic | ![InMusic](https://raw.githubusercontent.com/ory/meta/master/static/adopters/dark/inmusic.svg) | [inmusicbrands.com](https://inmusicbrands.com/) |  |
| Buhta | ![Buhta](https://raw.githubusercontent.com/ory/meta/master/static/adopters/dark/buhta.svg) | [buhta.com](https://buhta.com/) |  |
| Amplitude | ![amplitude.com](https://raw.githubusercontent.com/ory/meta/master/static/adopters/dark/amplitude.svg) | [amplitude.com](https://amplitude.com/) |  |
| ![TIER IV](https://raw.githubusercontent.com/ory/meta/master/static/adopters/dark/tieriv.svg) | ![Kyma Project](https://raw.githubusercontent.com/ory/meta/master/static/adopters/dark/kyma.svg) | ![Serlo](https://raw.githubusercontent.com/ory/meta/master/static/adopters/dark/serlo.svg) | ![Padis](https://raw.githubusercontent.com/ory/meta/master/static/adopters/dark/padis.svg) |
| ![Cloudbear](https://raw.githubusercontent.com/ory/meta/master/static/adopters/dark/cloudbear.svg) | ![Security Onion Solutions](https://raw.githubusercontent.com/ory/meta/master/static/adopters/dark/securityonion.svg) | ![Factly](https://raw.githubusercontent.com/ory/meta/master/static/adopters/dark/factly.svg) | ![All My Funds](https://raw.githubusercontent.com/ory/meta/master/static/adopters/dark/allmyfunds.svg) |
| ![Nortal](https://raw.githubusercontent.com/ory/meta/master/static/adopters/dark/nortal.svg) | ![OrderMyGear](https://raw.githubusercontent.com/ory/meta/master/static/adopters/dark/ordermygear.svg) | ![R2Devops](https://raw.githubusercontent.com/ory/meta/master/static/adopters/dark/r2devops.svg) | ![Paralus](https://raw.githubusercontent.com/ory/meta/master/static/adopters/dark/paralus.svg) |
| ![dyrector.io](https://raw.githubusercontent.com/ory/meta/master/static/adopters/dark/dyrector_io.svg) | ![pinniped.dev](https://raw.githubusercontent.com/ory/meta/master/static/adopters/dark/pinniped.svg) | ![pvotal.tech](https://raw.githubusercontent.com/ory/meta/master/static/adopters/dark/pvotal.svg) |  |

Many thanks to all individual contributors

[![](https://opencollective.com/ory/contributors.svg?width=890&limit=714&button=false)](https://opencollective.com/ory)

## Ecosystem

We build Ory on several guiding principles when it comes to our architecture design:

- Minimal dependencies
- Runs everywhere
- Scales without effort
- Minimize room for human and network errors

Ory's architecture is designed to run best on a Container Orchestration system such as Kubernetes, CloudFoundry, OpenShift, and similar projects. Binaries are small (5-15MB) and available for all popular processor types (ARM, AMD64, i386) and operating systems (FreeBSD, Linux, macOS, Windows) without system dependencies (Java, Node, Ruby, libxml, ...).

### Ory Kratos: Identity and User Infrastructure and Management

[Ory Kratos](https://github.com/ory/kratos) is an API-first Identity and User Management system that is built according to [cloud architecture best practices](https://www.ory.com/docs/next/ecosystem/software-architecture-philosophy). It implements core use cases that almost every software application needs to deal with: Self-service Login and Registration, Multi-Factor Authentication (MFA/2FA), Account Recovery and Verification, Profile, and Account Management.

### Ory Hydra: OAuth2 & OpenID Connect Server

[Ory Hydra](https://github.com/ory/hydra) is an OpenID Certified™ OAuth2 and OpenID Connect Provider which easily connects to any existing identity system by writing a tiny "bridge" application. It gives absolute control over the user interface and user experience flows.

### Ory Oathkeeper: Identity & Access Proxy

[Ory Oathkeeper](https://github.com/ory/oathkeeper) is a BeyondCorp/Zero Trust Identity & Access Proxy (IAP) with configurable authentication, authorization, and request mutation rules for your web services: Authenticate JWT, Access Tokens, API Keys, mTLS; Check if the contained subject is allowed to perform the request; Encode resulting content into custom headers (`X-User-ID`), JSON Web Tokens and more!

### Ory Keto: Access Control Policies as a Server

[Ory Keto](https://github.com/ory/keto) is a policy decision point. It uses a set of access control policies, similar to AWS IAM Policies, in order to determine whether a subject (user, application, service, car, ...) is authorized to perform a certain action on a resource.

## Documentation

The full Ory Hydra documentation is available at [www.ory.com/docs/hydra](https://www.ory.com/docs/hydra), including:

- [Installation guides](https://www.ory.com/docs/hydra/install)
- [Configuration reference](https://www.ory.com/docs/hydra/reference/configuration)
- [HTTP API documentation](https://www.ory.com/docs/hydra/sdk/api)
- [Security architecture](https://www.ory.com/docs/hydra/security-architecture)
- [Performance benchmarks](https://www.ory.com/docs/performance/hydra)

For upgrading and changelogs, check [releases tab](https://github.com/ory/hydra/releases) and [CHANGELOG.md](./CHANGELOG.md).

## Developing Ory Hydra

See [DEVELOP.md](./DEVELOP.md) for information on:

- Contribution guidelines
- Prerequisites
- Install from source
- Running tests
- Build Docker image
- Preview API documentation

## Security

OAuth2 and OAuth2 related specifications are over 400 written pages. Implementing OAuth2 is easy, getting it right is hard. Ory Hydra is trusted by companies all around the world, has a vibrant community and faces millions of requests in production each day. Read [the security guide](https://www.ory.com/docs/hydra/security-architecture) for more details on cryptography and security concepts.

### Disclosing vulnerabilities

If you think you found a security vulnerability, please refrain from posting it publicly on the forums, the chat, or GitHub. You can find all info for responsible disclosure in our [security.txt](https://www.ory.com/.well-known/security.txt).

## Telemetry

Our services collect summarized, anonymized data that can optionally be turned off. Click [here](https://www.ory.com/docs/ecosystem/sqa) to learn more.

## Libraries and third-party projects

Official:

- [User Login & Consent Example](https://github.com/ory/hydra-login-consent-node)

Community:

- Visit [this document for an overview of community projects and articles](https://www.ory.com/docs/ecosystem/community)

Developer Blog:

- Visit the [Ory Blog](https://www.ory.com/blog/) for guides, tutorials and articles around Ory Hydra and the Ory ecosystem.
