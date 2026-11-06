[![CI](https://github.com/scalar/scalar/actions/workflows/ci.yml/badge.svg)](https://github.com/scalar/scalar/actions/workflows/ci.yml) [![Contributors](https://img.shields.io/github/contributors/scalar/scalar)](https://github.com/scalar/scalar/graphs/contributors) [![GitHub License](https://img.shields.io/github/license/scalar/scalar)](https://github.com/scalar/scalar/blob/main/LICENSE) [![Twitter](https://img.shields.io/twitter/follow/scalar)](https://x.com/scalar) [![Discord](https://img.shields.io/discord/1135330207960678410?style=flat&color=5865F2)](https://discord.gg/scalar)

# 

Scalar

[![Scalar API Reference](https://github.com/user-attachments/assets/9b639f2d-0204-4b15-b918-158072a9afa5#gh-light-mode-only)](https://docs.scalar.com/swagger-editor) [![Scalar API client](https://github.com/user-attachments/assets/b391b82f-d993-4e97-8a17-1c3c7ccbb19b#gh-light-mode-only)](https://scalar.com/download)

![](https://github.com/user-attachments/assets/3a24fc5c-5d3c-4be4-8b9e-399bd49e4fb7#gh-light-mode-only) ![](https://github.com/user-attachments/assets/76f123ae-f458-409f-84d3-b9ad14fd3fb2#gh-dark-mode-only)

### Interactive API Reference from OpenAPI/Swagger

└ Renders OpenAPI/Swagger documents  
└ Comes with an API testing tool  
└ Doesn't look like 2011  
└ Generates code examples for many languages & frameworks  
└ Integrates with your favorite framework  
└ [Try Demo](https://docs.scalar.com/swagger-editor)

![](https://github.com/user-attachments/assets/7d7e7ba7-2b02-49f3-abcd-b24c566a3c16#gh-light-mode-only) ![](https://github.com/user-attachments/assets/341bfb1d-5cb0-4ec6-89eb-4b1dcc07eeb7#gh-dark-mode-only)

![](https://github.com/user-attachments/assets/d9f90c51-82d4-4948-9365-658ccc7d78c4#gh-light-mode-only) ![](https://github.com/user-attachments/assets/e7c2023e-dfbc-428c-bc85-c06d8a6e4b67#gh-dark-mode-only)

### An offline-first API Client built for OpenAPI

└ Free and open-source  
└ First-class OpenAPI/Swagger support  
└ Integrates with dozens of API Frameworks (Elysia, Hono, FastAPI, etc)  
└ Syncs with your favorite server framework (Watch Mode)  
└ Has environment variables, dynamic parameters and everything  
└ [Try It in the Browser](https://client.scalar.com/) └ [Download (Windows, MacOS, Linux)](https://scalar.com/download)  

![](https://github.com/user-attachments/assets/7d7e7ba7-2b02-49f3-abcd-b24c566a3c16#gh-light-mode-only) ![](https://github.com/user-attachments/assets/341bfb1d-5cb0-4ec6-89eb-4b1dcc07eeb7#gh-dark-mode-only)

### Trusted by:

![Scalar API client](https://github.com/user-attachments/assets/73dcef95-fc4f-4111-bb09-f3ce37453a81#gh-light-mode-only) ![Scalar API client](https://github.com/user-attachments/assets/1da6b904-34be-4760-b535-0dd2160e6d12#gh-light-mode-only)

### Quickstart

All you need is a single HTML file to create an amazing API reference:

``` html
<!doctype html>
<html>
  <head>
    <title>Scalar API Reference</title>
    <meta charset="utf-8" />
    <meta
      name="viewport"
      content="width=device-width, initial-scale=1" />
  </head>

  <body>
    <div id="app"></div>

    <!-- Load the Script -->
    <script src="https://cdn.jsdelivr.net/npm/@scalar/api-reference"></script>

    <!-- Initialize the Scalar API Reference -->
    <script>
      Scalar.createApiReference('#app', {
        // The URL of the OpenAPI/Swagger document
        url: 'https://registry.scalar.com/@scalar/apis/galaxy?format=json',
        // Avoid CORS issues
        proxyUrl: 'https://proxy.scalar.com',
      })
    </script>
  </body>
</html>
```

> Need a Custom Header? Check out this example: https://codepen.io/scalarorg/pen/VwOXqam

And there's an ever-growing list of plugins and integrations:

### Integrations

- [HTML/JS API](https://scalar.com/products/api-references/integrations/html-js) (works everywhere)
- [.NET ASP.NET Core](https://scalar.com/products/api-references/integrations/aspnetcore/integration)
- [Aspire](https://scalar.com/products/api-references/integrations/aspire)
- [AdonisJS](https://scalar.com/products/api-references/integrations/adonisjs)
- [Astro](https://scalar.com/products/api-references/integrations/astro)
- [Django Ninja](https://scalar.com/products/api-references/integrations/django-ninja)
- [Django](https://scalar.com/products/api-references/integrations/django)
- [Docker](https://scalar.com/products/api-references/integrations/docker)
- [Docusaurus](https://scalar.com/products/api-references/integrations/docusaurus)
- [Elixir](https://scalar.com/products/api-references/integrations/elixir)
- [Express](https://scalar.com/products/api-references/integrations/express)
- [FastAPI](https://scalar.com/products/api-references/integrations/fastapi)
- [Fastify](https://scalar.com/products/api-references/integrations/fastify)
- [Flask](https://scalar.com/products/api-references/integrations/flask)
- [Go](https://scalar.com/products/api-references/integrations/go)
- [Hapi](https://scalar.com/products/api-references/integrations/hapi)
- [Hono](https://scalar.com/products/api-references/integrations/hono)
- [Laravel Scribe](https://scalar.com/products/api-references/integrations/laravel-scribe)
- [Laravel](https://scalar.com/products/api-references/integrations/laravel)
- [Micronaut](https://scalar.com/products/api-references/integrations/micronaut)
- [NestJS](https://scalar.com/products/api-references/integrations/nestjs)
- [Next.js](https://scalar.com/products/api-references/integrations/nextjs)
- [Nuxt](https://scalar.com/products/api-references/integrations/nuxt)
- [Python](https://scalar.com/products/api-references/integrations/python)
- [React](https://scalar.com/products/api-references/integrations/react)
- [Ruby on Rails](https://scalar.com/products/api-references/integrations/ruby-on-rails)
- [Rust](https://scalar.com/products/api-references/integrations/rust)
- [Spring Boot](https://scalar.com/products/api-references/integrations/spring-boot)
- [SvelteKit](https://scalar.com/products/api-references/integrations/sveltekit)
- [Ts.ED](https://scalar.com/products/api-references/integrations/tsed)
- [Vue.js](https://scalar.com/products/api-references/integrations/vue)

### Built-in Support

The following frameworks have chosen Scalar API Reference as their default OpenAPI documentation UI, recognizing its developer-friendly features and modern design:

- [Effect](https://scalar.com/products/api-references/integrations/effect)
- [ElysiaJS](https://scalar.com/products/api-references/integrations/elysiajs)
- [HappyX](https://github.com/HapticX/happyx)
- [Litestar](https://docs.litestar.dev/latest/usage/openapi/ui_plugins.html)
- [Nitro](https://scalar.com/products/api-references/integrations/nitro)
- [oRPC](https://orpc.unnoq.com/docs/openapi/plugins/openapi-reference)
- [Platformatic](https://scalar.com/products/api-references/integrations/platformatic)
- [Spry](https://scalar.com/products/api-references/integrations/spry)

### Managed Hosting

We're offering a free and paid managed hosting on the edge, too:

- Write your API documentation and publish API references (free)
- `YOUR_NAME_HERE.apidocumentation.com` subdomain and SSL (free)
- [GitHub Sync](https://scalar.com/products/docs/github-sync)
- Write free-form documentation
- Collaborate with your team
- Use any domain

Ready? [Create your Scalar Account](https://scalar.com)

### Documentation

Topic

Description

[Configuration](https://scalar.com/products/api-references/configuration)

The universal configuration object

[Themes](https://scalar.com/products/api-references/themes)

Predefined themes, layouts & styling

[OpenAPI](https://scalar.com/products/api-references/openapi)

OpenAPI specification extensions

[Markdown](https://scalar.com/products/api-references/markdown)

Supported Markdown syntax

[Plugins](https://scalar.com/products/api-references/plugins)

Extend the functionality

### Projects

Project

Description

[Scalar API Reference](https://scalar.com/products/api-references/getting-started)

Self-hosted API Reference

[Scalar API Client](https://scalar.com/download)

Postman alternative

[Agent Scalar](https://scalar.com/products/agent/getting-started)

Chat with your API

[Scalar Registry](https://scalar.com/products/registry/getting-started)

Manage OpenAPI documents

[Scalar Docs](https://scalar.com/products/docs/getting-started)

Hosted documentation

[Scalar Docs Starter](https://github.com/scalar/starter)

Starter template for Scalar Docs

[Scalar SDKs](https://scalar.com/products/sdks/getting-started)

SDK generation

[Scalar CLI](https://scalar.com/tools/cli/getting-started)

Command-line interface

[Scalar Mock Server](https://scalar.com/tools/mock-server/getting-started)

Mock APIs from OpenAPI documents

[Scalar Galaxy](packages/galaxy/README.md)

Our OpenAPI Example

[Scalar Editor](https://editor.scalar.com/)

OpenAPI Online Editor

[Scalar OpenAPI Parser](packages/openapi-parser/README.md)

Parse OpenAPI documents

[Scalar OpenAPI to Markdown](packages/openapi-to-markdown/README.md)

OpenAPI \> Markdown/HTML

[Scalar OpenAPI Upgrader](packages/openapi-upgrader/README.md)

Upgrade OpenAPI documents

[Scalar Void Server](packages/void-server/README.md)

HTTP Request Mirror

### Community

We are API nerds. You too? Let's chat on Discord: \<https://discord.gg/scalar\>

### Contributions

Contributions are welcome! Read the [`CONTRIBUTING`](CONTRIBUTING.md) guide.

**Top 10 Contributors (April 2025)**

![](https://github.com/user-attachments/assets/8c10d2aa-9eb4-4818-9ca2-625cfed5ca08#gh-light-mode-only) ![](https://github.com/user-attachments/assets/50b9b042-107e-4167-9c7f-94497f85d2e0#gh-dark-mode-only)

**Top Contributors (All Time)**

[![hanspagel](https://avatars.githubusercontent.com/u/1577992?v=4)  
_(**hanspagel**)](https://github.com/hanspagel)

[![xC0dex](https://avatars.githubusercontent.com/u/22918366?v=4)  
_(**xC0dex**)](https://github.com/xC0dex)

[![amritk](https://avatars.githubusercontent.com/u/2039539?v=4)  
_(**amritk**)](https://github.com/amritk)

[![antlio](https://avatars.githubusercontent.com/u/14966155?v=4)  
_(**antlio**)](https://github.com/antlio)

[![hwkr](https://avatars.githubusercontent.com/u/6374090?v=4)  
_(**hwkr**)](https://github.com/hwkr)

[![marclave](https://avatars.githubusercontent.com/u/6176314?v=4)  
_(**marclave**)](https://github.com/marclave)

[![DemonHa](https://avatars.githubusercontent.com/u/91160178?v=4)  
_(**DemonHa**)](https://github.com/DemonHa)

[![cameronrohani](https://avatars.githubusercontent.com/u/6201407?v=4)  
_(**cameronrohani**)](https://github.com/cameronrohani)

[![geoffgscott](https://avatars.githubusercontent.com/u/59206100?v=4)  
_(**geoffgscott**)](https://github.com/geoffgscott)

[![marcalexiei](https://avatars.githubusercontent.com/u/24919330?v=4)  
_(**marcalexiei**)](https://github.com/marcalexiei)

[![tmastrom](https://avatars.githubusercontent.com/u/36525329?v=4)  
_(**tmastrom**)](https://github.com/tmastrom)

[![inyourtime](https://avatars.githubusercontent.com/u/66111030?v=4)  
_(**inyourtime**)](https://github.com/inyourtime)

[![liamdscalar](https://avatars.githubusercontent.com/u/225425944?v=4)  
_(**liamdscalar**)](https://github.com/liamdscalar)

[![bgrcs](https://avatars.githubusercontent.com/u/18078763?v=4)  
_(**bgrcs**)](https://github.com/bgrcs)

[![AbdelhamidKhald](https://avatars.githubusercontent.com/u/140171792?v=4)  
_(**AbdelhamidKhald**)](https://github.com/AbdelhamidKhald)

[![gevann](https://avatars.githubusercontent.com/u/6427337?v=4)  
_(**gevann**)](https://github.com/gevann)

[![alonfaraj](https://avatars.githubusercontent.com/u/15960497?v=4)  
_(**alonfaraj**)](https://github.com/alonfaraj)

[![federicobond](https://avatars.githubusercontent.com/u/138426?v=4)  
_(**federicobond**)](https://github.com/federicobond)

[![ahmedrangel](https://avatars.githubusercontent.com/u/50090595?v=4)  
_(**ahmedrangel**)](https://github.com/ahmedrangel)

[![matthyk](https://avatars.githubusercontent.com/u/53833818?v=4)  
_(**matthyk**)](https://github.com/matthyk)

[![Amorim33](https://avatars.githubusercontent.com/u/42624869?v=4)  
_(**Amorim33**)](https://github.com/Amorim33)

[![wilhelmer](https://avatars.githubusercontent.com/u/2234833?v=4)  
_(**wilhelmer**)](https://github.com/wilhelmer)

[![baywet](https://avatars.githubusercontent.com/u/7905502?v=4)  
_(**baywet**)](https://github.com/baywet)

[![YagUber](https://avatars.githubusercontent.com/u/20715993?v=4)  
_(**YagUber**)](https://github.com/YagUber)

[![Mason-Little](https://avatars.githubusercontent.com/u/105008441?v=4)  
_(**Mason-Little**)](https://github.com/Mason-Little)

[![ivanagas](https://avatars.githubusercontent.com/u/34755028?v=4)  
_(**ivanagas**)](https://github.com/ivanagas)

[![Edgaraszs](https://avatars.githubusercontent.com/u/55696268?v=4)  
_(**Edgaraszs**)](https://github.com/Edgaraszs)

[![adjsky](https://avatars.githubusercontent.com/u/49305219?v=4)  
_(**adjsky**)](https://github.com/adjsky)

[![RemcoGoy](https://avatars.githubusercontent.com/u/34539109?v=4)  
_(**RemcoGoy**)](https://github.com/RemcoGoy)

[![mpminardi](https://avatars.githubusercontent.com/u/8587567?v=4)  
_(**mpminardi**)](https://github.com/mpminardi)

[![mcollina](https://avatars.githubusercontent.com/u/52195?v=4)  
_(**mcollina**)](https://github.com/mcollina)

[![TheVaan](https://avatars.githubusercontent.com/u/1108485?v=4)  
_(**TheVaan**)](https://github.com/TheVaan)

[![cobyfrombrooklyn-bot](https://avatars.githubusercontent.com/u/262706804?v=4)  
_(**cobyfrombrooklyn-bot**)](https://github.com/cobyfrombrooklyn-bot)

[![si-net](https://avatars.githubusercontent.com/u/25386895?v=4)  
_(**si-net**)](https://github.com/si-net)

[![paulomorgado](https://avatars.githubusercontent.com/u/470455?v=4)  
_(**paulomorgado**)](https://github.com/paulomorgado)

[![nsychev](https://avatars.githubusercontent.com/u/11004619?v=4)  
_(**nsychev**)](https://github.com/nsychev)

[![Mohib834](https://avatars.githubusercontent.com/u/47316464?v=4)  
_(**Mohib834**)](https://github.com/Mohib834)

[![lc-soft](https://avatars.githubusercontent.com/u/1730073?v=4)  
_(**lc-soft**)](https://github.com/lc-soft)

[![fuma-nama](https://avatars.githubusercontent.com/u/76240755?v=4)  
_(**fuma-nama**)](https://github.com/fuma-nama)

[![ATREAY](https://avatars.githubusercontent.com/u/66585295?v=4)  
_(**ATREAY**)](https://github.com/ATREAY)

[![SimonVadier](https://avatars.githubusercontent.com/u/97546195?v=4)  
_(**SimonVadier**)](https://github.com/SimonVadier)

[![ledgersteve](https://avatars.githubusercontent.com/u/90449376?v=4)  
_(**ledgersteve**)](https://github.com/ledgersteve)

[![timheuer](https://avatars.githubusercontent.com/u/4821?v=4)  
_(**timheuer**)](https://github.com/timheuer)

[![wilcoschoneveld](https://avatars.githubusercontent.com/u/3064588?v=4)  
_(**wilcoschoneveld**)](https://github.com/wilcoschoneveld)

[![ykdojo](https://avatars.githubusercontent.com/u/1811651?v=4)  
_(**ykdojo**)](https://github.com/ykdojo)

[![x-delfino](https://avatars.githubusercontent.com/u/67192579?v=4)  
_(**x-delfino**)](https://github.com/x-delfino)

[![horpto](https://avatars.githubusercontent.com/u/7109350?v=4)  
_(**horpto**)](https://github.com/horpto)

[![jpjpjp](https://avatars.githubusercontent.com/u/4774656?v=4)  
_(**jpjpjp**)](https://github.com/jpjpjp)

[![trusta](https://avatars.githubusercontent.com/u/7666444?v=4)  
_(**trusta**)](https://github.com/trusta)

[![hex0id](https://avatars.githubusercontent.com/u/5276261?v=4)  
_(**hex0id**)](https://github.com/hex0id)

[![yshrsmz](https://avatars.githubusercontent.com/u/654889?v=4)  
_(**yshrsmz**)](https://github.com/yshrsmz)

[![soulchild](https://avatars.githubusercontent.com/u/59642?v=4)  
_(**soulchild**)](https://github.com/soulchild)

[![SebastianBienert](https://avatars.githubusercontent.com/u/17458785?v=4)  
_(**SebastianBienert**)](https://github.com/SebastianBienert)

[![cyphercodes](https://avatars.githubusercontent.com/u/7407177?v=4)  
_(**cyphercodes**)](https://github.com/cyphercodes)

[![PrinceManfred](https://avatars.githubusercontent.com/u/777963?v=4)  
_(**PrinceManfred**)](https://github.com/PrinceManfred)

[![mouhannad-sh](https://avatars.githubusercontent.com/u/18495740?v=4)  
_(**mouhannad-sh**)](https://github.com/mouhannad-sh)

[![mason-at-pieces](https://avatars.githubusercontent.com/u/123421085?v=4)  
_(**mason-at-pieces**)](https://github.com/mason-at-pieces)

[![luc122c](https://avatars.githubusercontent.com/u/7257092?v=4)  
_(**luc122c**)](https://github.com/luc122c)

[![luke-hagar-sp](https://avatars.githubusercontent.com/u/193985956?v=4)  
_(**luke-hagar-sp**)](https://github.com/luke-hagar-sp)

[![handrews](https://avatars.githubusercontent.com/u/2358015?v=4)  
_(**handrews**)](https://github.com/handrews)

[![gsmcdonald](https://avatars.githubusercontent.com/u/36003378?v=4)  
_(**gsmcdonald**)](https://github.com/gsmcdonald)

[![Duncanma](https://avatars.githubusercontent.com/u/18338424?v=4)  
_(**Duncanma**)](https://github.com/Duncanma)

[![WDaan](https://avatars.githubusercontent.com/u/25707052?v=4)  
_(**WDaan**)](https://github.com/WDaan)

[![STP5940](https://avatars.githubusercontent.com/u/21144303?v=4)  
_(**STP5940**)](https://github.com/STP5940)

[![mirismaili](https://avatars.githubusercontent.com/u/15800189?v=4)  
_(**mirismaili**)](https://github.com/mirismaili)

[![rmp135](https://avatars.githubusercontent.com/u/3882803?v=4)  
_(**rmp135**)](https://github.com/rmp135)

[![roryschadler](https://avatars.githubusercontent.com/u/48921090?v=4)  
_(**roryschadler**)](https://github.com/roryschadler)

[![rpmccarter](https://avatars.githubusercontent.com/u/63772591?v=4)  
_(**rpmccarter**)](https://github.com/rpmccarter)

[![hrynevychroman](https://avatars.githubusercontent.com/u/82209198?v=4)  
_(**hrynevychroman**)](https://github.com/hrynevychroman)

[![rbange](https://avatars.githubusercontent.com/u/13252574?v=4)  
_(**rbange**)](https://github.com/rbange)

[![rcollas](https://avatars.githubusercontent.com/u/80286021?v=4)  
_(**rcollas**)](https://github.com/rcollas)

[![bobheadxi](https://avatars.githubusercontent.com/u/23356519?v=4)  
_(**bobheadxi**)](https://github.com/bobheadxi)

[![captainsafia](https://avatars.githubusercontent.com/u/1857993?v=4)  
_(**captainsafia**)](https://github.com/captainsafia)

[![realsama](https://avatars.githubusercontent.com/u/46403284?v=4)  
_(**realsama**)](https://github.com/realsama)

[![ventocis](https://avatars.githubusercontent.com/u/36198345?v=4)  
_(**ventocis**)](https://github.com/ventocis)

[![SamyPesse](https://avatars.githubusercontent.com/u/845425?v=4)  
_(**SamyPesse**)](https://github.com/SamyPesse)

[![SergioChan](https://avatars.githubusercontent.com/u/10103766?v=4)  
_(**SergioChan**)](https://github.com/SergioChan)

[![medz](https://avatars.githubusercontent.com/u/5564821?v=4)  
_(**medz**)](https://github.com/medz)

[![dotfortun](https://avatars.githubusercontent.com/u/11822957?v=4)  
_(**dotfortun**)](https://github.com/dotfortun)

[![smoores-dev](https://avatars.githubusercontent.com/u/5354254?v=4)  
_(**smoores-dev**)](https://github.com/smoores-dev)

[![Chinlinlee](https://avatars.githubusercontent.com/u/49154622?v=4)  
_(**Chinlinlee**)](https://github.com/Chinlinlee)

[![tinchoz49](https://avatars.githubusercontent.com/u/819446?v=4)  
_(**tinchoz49**)](https://github.com/tinchoz49)

[![MatteoH2O1999](https://avatars.githubusercontent.com/u/82184604?v=4)  
_(**MatteoH2O1999**)](https://github.com/MatteoH2O1999)

[![maxehmookau](https://avatars.githubusercontent.com/u/690977?v=4)  
_(**maxehmookau**)](https://github.com/maxehmookau)

[![MaxBreida](https://avatars.githubusercontent.com/u/18685579?v=4)  
_(**MaxBreida**)](https://github.com/MaxBreida)

[![mvt147](https://avatars.githubusercontent.com/u/9066177?v=4)  
_(**mvt147**)](https://github.com/mvt147)

[![michielbdejong](https://avatars.githubusercontent.com/u/408412?v=4)  
_(**michielbdejong**)](https://github.com/michielbdejong)

[![1571min](https://avatars.githubusercontent.com/u/44085183?v=4)  
_(**1571min**)](https://github.com/1571min)

[![malinbranduse](https://avatars.githubusercontent.com/u/22645119?v=4)  
_(**malinbranduse**)](https://github.com/malinbranduse)

[![Lazialize](https://avatars.githubusercontent.com/u/3455147?v=4)  
_(**Lazialize**)](https://github.com/Lazialize)

[![Olexandr88](https://avatars.githubusercontent.com/u/93856062?v=4)  
_(**Olexandr88**)](https://github.com/Olexandr88)

[![pat-s](https://avatars.githubusercontent.com/u/8430564?v=4)  
_(**pat-s**)](https://github.com/pat-s)

[![pkucmus](https://avatars.githubusercontent.com/u/6347418?v=4)  
_(**pkucmus**)](https://github.com/pkucmus)

[![petercinibulk](https://avatars.githubusercontent.com/u/29611892?v=4)  
_(**petercinibulk**)](https://github.com/petercinibulk)

[![petvas](https://avatars.githubusercontent.com/u/8041694?v=4)  
_(**petvas**)](https://github.com/petvas)

[![philsturgeon](https://avatars.githubusercontent.com/u/67381?v=4)  
_(**philsturgeon**)](https://github.com/philsturgeon)

[![pdjohntony](https://avatars.githubusercontent.com/u/6294702?v=4)  
_(**pdjohntony**)](https://github.com/pdjohntony)

[![Fjandin](https://avatars.githubusercontent.com/u/167869?v=4)  
_(**Fjandin**)](https://github.com/Fjandin)

[![rhuanbarreto](https://avatars.githubusercontent.com/u/283004?v=4)  
_(**rhuanbarreto**)](https://github.com/rhuanbarreto)

[![rickihastings](https://avatars.githubusercontent.com/u/45660?v=4)  
_(**rickihastings**)](https://github.com/rickihastings)

[![robert-dean](https://avatars.githubusercontent.com/u/99672719?v=4)  
_(**robert-dean**)](https://github.com/robert-dean)

[![bsdayo](https://avatars.githubusercontent.com/u/41754841?v=4)  
_(**bsdayo**)](https://github.com/bsdayo)

[![WilliamBonvini](https://avatars.githubusercontent.com/u/37834150?v=4)  
_(**WilliamBonvini**)](https://github.com/WilliamBonvini)

[![danwithabox](https://avatars.githubusercontent.com/u/144792741?v=4)  
_(**danwithabox**)](https://github.com/danwithabox)

[![demingongo](https://avatars.githubusercontent.com/u/24739500?v=4)  
_(**demingongo**)](https://github.com/demingongo)

[![FotieMConstant](https://avatars.githubusercontent.com/u/42372656?v=4)  
_(**FotieMConstant**)](https://github.com/FotieMConstant)

[![ga1az](https://avatars.githubusercontent.com/u/75758899?v=4)  
_(**ga1az**)](https://github.com/ga1az)

[![g-airey](https://avatars.githubusercontent.com/u/35547338?v=4)  
_(**g-airey**)](https://github.com/g-airey)

[![gary5](https://avatars.githubusercontent.com/u/7246502?v=4)  
_(**gary5**)](https://github.com/gary5)

[![kwaichanz](https://avatars.githubusercontent.com/u/36059761?v=4)  
_(**kwaichanz**)](https://github.com/kwaichanz)

[![milksense](https://avatars.githubusercontent.com/u/29128703?v=4)  
_(**milksense**)](https://github.com/milksense)

[![o-az](https://avatars.githubusercontent.com/u/23618431?v=4)  
_(**o-az**)](https://github.com/o-az)

[![omerp-explorium](https://avatars.githubusercontent.com/u/93073822?v=4)  
_(**omerp-explorium**)](https://github.com/omerp-explorium)

[![stefanprobst](https://avatars.githubusercontent.com/u/20753323?v=4)  
_(**stefanprobst**)](https://github.com/stefanprobst)

[![dunklesToast](https://avatars.githubusercontent.com/u/17279485?v=4)  
_(**dunklesToast**)](https://github.com/dunklesToast)

[![tsiwek-piwik](https://avatars.githubusercontent.com/u/117373332?v=4)  
_(**tsiwek-piwik**)](https://github.com/tsiwek-piwik)

[![dinwwwh](https://avatars.githubusercontent.com/u/64189902?v=4)  
_(**dinwwwh**)](https://github.com/dinwwwh)

[![zgcalebp](https://avatars.githubusercontent.com/u/142928130?v=4)  
_(**zgcalebp**)](https://github.com/zgcalebp)

[![Huliiiiii](https://avatars.githubusercontent.com/u/134658521?v=4)  
_(**Huliiiiii**)](https://github.com/Huliiiiii)

[![soGit](https://avatars.githubusercontent.com/u/10682798?v=4)  
_(**soGit**)](https://github.com/soGit)

[![sinh117801](https://avatars.githubusercontent.com/u/43696715?v=4)  
_(**sinh117801**)](https://github.com/sinh117801)

[![stratosblue](https://avatars.githubusercontent.com/u/20887303?v=4)  
_(**stratosblue**)](https://github.com/stratosblue)

[![yokeTH](https://avatars.githubusercontent.com/u/66236295?v=4)  
_(**yokeTH**)](https://github.com/yokeTH)

[![Thiago-Mausbach](https://avatars.githubusercontent.com/u/80917439?v=4)  
_(**Thiago-Mausbach**)](https://github.com/Thiago-Mausbach)

[![thibaultleouay](https://avatars.githubusercontent.com/u/13894054?v=4)  
_(**thibaultleouay**)](https://github.com/thibaultleouay)

[![thijskok](https://avatars.githubusercontent.com/u/1344550?v=4)  
_(**thijskok**)](https://github.com/thijskok)

[![TomzBench](https://avatars.githubusercontent.com/u/20780378?v=4)  
_(**TomzBench**)](https://github.com/TomzBench)

[![rektdeckard](https://avatars.githubusercontent.com/u/26732044?v=4)  
_(**rektdeckard**)](https://github.com/rektdeckard)

[![Courtcircuits](https://avatars.githubusercontent.com/u/90451752?v=4)  
_(**Courtcircuits**)](https://github.com/Courtcircuits)

[![mveselov-stack-wizard](https://avatars.githubusercontent.com/u/117447605?v=4)  
_(**mveselov-stack-wizard**)](https://github.com/mveselov-stack-wizard)

[![Mai0313](https://avatars.githubusercontent.com/u/21039366?v=4)  
_(**Mai0313**)](https://github.com/Mai0313)

[![Ma-ve](https://avatars.githubusercontent.com/u/11227996?v=4)  
_(**Ma-ve**)](https://github.com/Ma-ve)

[![WesleySkeen](https://avatars.githubusercontent.com/u/2134761?v=4)  
_(**WesleySkeen**)](https://github.com/WesleySkeen)

[![rotciw](https://avatars.githubusercontent.com/u/21119564?v=4)  
_(**rotciw**)](https://github.com/rotciw)

[![Wolf-Syndrome](https://avatars.githubusercontent.com/u/44598104?v=4)  
_(**Wolf-Syndrome**)](https://github.com/Wolf-Syndrome)

[![rolldeep-stepmerrily](https://avatars.githubusercontent.com/u/98504913?v=4)  
_(**rolldeep-stepmerrily**)](https://github.com/rolldeep-stepmerrily)

[![zakaria-shahen](https://avatars.githubusercontent.com/u/35308232?v=4)  
_(**zakaria-shahen**)](https://github.com/zakaria-shahen)

[![bingbeann](https://avatars.githubusercontent.com/u/110380613?v=4)  
_(**bingbeann**)](https://github.com/bingbeann)

[![abdulamite](https://avatars.githubusercontent.com/u/7246246?v=4)  
_(**abdulamite**)](https://github.com/abdulamite)

[![foxfriends](https://avatars.githubusercontent.com/u/6126521?v=4)  
_(**foxfriends**)](https://github.com/foxfriends)

[![carstenlebek](https://avatars.githubusercontent.com/u/59960385?v=4)  
_(**carstenlebek**)](https://github.com/carstenlebek)

[![chadwhitacre](https://avatars.githubusercontent.com/u/134455?v=4)  
_(**chadwhitacre**)](https://github.com/chadwhitacre)

[![chrislearn](https://avatars.githubusercontent.com/u/5874864?v=4)  
_(**chrislearn**)](https://github.com/chrislearn)

[![jensenbox](https://avatars.githubusercontent.com/u/189265?v=4)  
_(**jensenbox**)](https://github.com/jensenbox)

[![ClanEver](https://avatars.githubusercontent.com/u/73160783?v=4)  
_(**ClanEver**)](https://github.com/ClanEver)

[![damiansan239](https://avatars.githubusercontent.com/u/42095620?v=4)  
_(**damiansan239**)](https://github.com/damiansan239)

[![danjohnson95](https://avatars.githubusercontent.com/u/6871504?v=4)  
_(**danjohnson95**)](https://github.com/danjohnson95)

[![danp](https://avatars.githubusercontent.com/u/2182?v=4)  
_(**danp**)](https://github.com/danp)

[![darekaze](https://avatars.githubusercontent.com/u/32747549?v=4)  
_(**darekaze**)](https://github.com/darekaze)

[![DavidNiessen](https://avatars.githubusercontent.com/u/68539499?v=4)  
_(**DavidNiessen**)](https://github.com/DavidNiessen)

[![delputnam](https://avatars.githubusercontent.com/u/1379730?v=4)  
_(**delputnam**)](https://github.com/delputnam)

[![lundibundi](https://avatars.githubusercontent.com/u/9109612?v=4)  
_(**lundibundi**)](https://github.com/lundibundi)

[![untiny](https://avatars.githubusercontent.com/u/29054492?v=4)  
_(**untiny**)](https://github.com/untiny)

[![diegolopes](https://avatars.githubusercontent.com/u/27782408?v=4)  
_(**diegolopes**)](https://github.com/diegolopes)

[![DmitriiKhudiakov](https://avatars.githubusercontent.com/u/148915384?v=4)  
_(**DmitriiKhudiakov**)](https://github.com/DmitriiKhudiakov)

[![elliotnash](https://avatars.githubusercontent.com/u/53949099?v=4)  
_(**elliotnash**)](https://github.com/elliotnash)

[![elliott-with-the-longest-name-on-github](https://avatars.githubusercontent.com/u/76245373?v=4)  
_(**elliott-with-the-longest-name-on-github**)](https://github.com/elliott-with-the-longest-name-on-github)

[![emmanuel-ferdman](https://avatars.githubusercontent.com/u/35470921?v=4)  
_(**emmanuel-ferdman**)](https://github.com/emmanuel-ferdman)

[![MathurAditya724](https://avatars.githubusercontent.com/u/57684218?v=4)  
_(**MathurAditya724**)](https://github.com/MathurAditya724)

[![ahmadi-akbar](https://avatars.githubusercontent.com/u/48069695?v=4)  
_(**ahmadi-akbar**)](https://github.com/ahmadi-akbar)

[![slash686](https://avatars.githubusercontent.com/u/4161770?v=4)  
_(**slash686**)](https://github.com/slash686)

[![alewin](https://avatars.githubusercontent.com/u/980844?v=4)  
_(**alewin**)](https://github.com/alewin)

[![gizero](https://avatars.githubusercontent.com/u/1544064?v=4)  
_(**gizero**)](https://github.com/gizero)

[![sigpwned](https://avatars.githubusercontent.com/u/1236302?v=4)  
_(**sigpwned**)](https://github.com/sigpwned)

[![arashsheyda](https://avatars.githubusercontent.com/u/38922203?v=4)  
_(**arashsheyda**)](https://github.com/arashsheyda)

[![thisisarko](https://avatars.githubusercontent.com/u/169167507?v=4)  
_(**thisisarko**)](https://github.com/thisisarko)

[![arthurfiorette](https://avatars.githubusercontent.com/u/47537704?v=4)  
_(**arthurfiorette**)](https://github.com/arthurfiorette)

[![zsilbi](https://avatars.githubusercontent.com/u/3886658?v=4)  
_(**zsilbi**)](https://github.com/zsilbi)

[![saithis](https://avatars.githubusercontent.com/u/1547453?v=4)  
_(**saithis**)](https://github.com/saithis)

[![BenJeau](https://avatars.githubusercontent.com/u/22248828?v=4)  
_(**BenJeau**)](https://github.com/BenJeau)

[![bdpiprava](https://avatars.githubusercontent.com/u/7871209?v=4)  
_(**bdpiprava**)](https://github.com/bdpiprava)

[![Borisich](https://avatars.githubusercontent.com/u/18186889?v=4)  
_(**Borisich**)](https://github.com/Borisich)

[![bmanth60](https://avatars.githubusercontent.com/u/5578150?v=4)  
_(**bmanth60**)](https://github.com/bmanth60)

[![brianheineman](https://avatars.githubusercontent.com/u/3210678?v=4)  
_(**brianheineman**)](https://github.com/brianheineman)

[![brunogrcsada](https://avatars.githubusercontent.com/u/54673205?v=4)  
_(**brunogrcsada**)](https://github.com/brunogrcsada)

[![Smyrcu](https://avatars.githubusercontent.com/u/42031920?v=4)  
_(**Smyrcu**)](https://github.com/Smyrcu)

[![cactysman](https://avatars.githubusercontent.com/u/5056880?v=4)  
_(**cactysman**)](https://github.com/cactysman)

[![froggy1014](https://avatars.githubusercontent.com/u/76844856?v=4)  
_(**froggy1014**)](https://github.com/froggy1014)

[![jan-krueger](https://avatars.githubusercontent.com/u/3315137?v=4)  
_(**jan-krueger**)](https://github.com/jan-krueger)

[![Tholdrim](https://avatars.githubusercontent.com/u/38507238?v=4)  
_(**Tholdrim**)](https://github.com/Tholdrim)

[![Jefwillems](https://avatars.githubusercontent.com/u/10141933?v=4)  
_(**Jefwillems**)](https://github.com/Jefwillems)

[![jqwn](https://avatars.githubusercontent.com/u/14569?v=4)  
_(**jqwn**)](https://github.com/jqwn)

[![Jannchie](https://avatars.githubusercontent.com/u/29743310?v=4)  
_(**Jannchie**)](https://github.com/Jannchie)

[![jonataw](https://avatars.githubusercontent.com/u/29772763?v=4)  
_(**jonataw**)](https://github.com/jonataw)

[![IHIutch](https://avatars.githubusercontent.com/u/20825047?v=4)  
_(**IHIutch**)](https://github.com/IHIutch)

[![jlnslv](https://avatars.githubusercontent.com/u/323004?v=4)  
_(**jlnslv**)](https://github.com/jlnslv)

[![kaigritun](https://avatars.githubusercontent.com/u/258667664?v=4)  
_(**kaigritun**)](https://github.com/kaigritun)

[![KevSlashNull](https://avatars.githubusercontent.com/u/28510368?v=4)  
_(**KevSlashNull**)](https://github.com/KevSlashNull)

[![kou029w](https://avatars.githubusercontent.com/u/1730234?v=4)  
_(**kou029w**)](https://github.com/kou029w)

[![krcm0209](https://avatars.githubusercontent.com/u/17315774?v=4)  
_(**krcm0209**)](https://github.com/krcm0209)

[![kyllian](https://avatars.githubusercontent.com/u/5831233?v=4)  
_(**kyllian**)](https://github.com/kyllian)

[![sanscontext](https://avatars.githubusercontent.com/u/17016388?v=4)  
_(**sanscontext**)](https://github.com/sanscontext)

[![ShadiestGoat](https://avatars.githubusercontent.com/u/48590492?v=4)  
_(**ShadiestGoat**)](https://github.com/ShadiestGoat)

[![da411d](https://avatars.githubusercontent.com/u/12462454?v=4)  
_(**da411d**)](https://github.com/da411d)

[![marikaner](https://avatars.githubusercontent.com/u/868536?v=4)  
_(**marikaner**)](https://github.com/marikaner)

[![MarioGK](https://avatars.githubusercontent.com/u/8379079?v=4)  
_(**MarioGK**)](https://github.com/MarioGK)

[![not-my-profile](https://avatars.githubusercontent.com/u/73739153?v=4)  
_(**not-my-profile**)](https://github.com/not-my-profile)

[![facus26](https://avatars.githubusercontent.com/u/18079059?v=4)  
_(**facus26**)](https://github.com/facus26)

[![filiabel](https://avatars.githubusercontent.com/u/25987724?v=4)  
_(**filiabel**)](https://github.com/filiabel)

[![flovouin](https://avatars.githubusercontent.com/u/5155149?v=4)  
_(**flovouin**)](https://github.com/flovouin)

[![Fdawgs](https://avatars.githubusercontent.com/u/43814140?v=4)  
_(**Fdawgs**)](https://github.com/Fdawgs)

[![fredrik-aschehoug](https://avatars.githubusercontent.com/u/15358786?v=4)  
_(**fredrik-aschehoug**)](https://github.com/fredrik-aschehoug)

[![silkfire](https://avatars.githubusercontent.com/u/1554615?v=4)  
_(**silkfire**)](https://github.com/silkfire)

[![galah92](https://avatars.githubusercontent.com/u/14138433?v=4)  
_(**galah92**)](https://github.com/galah92)

[![GreyXor](https://avatars.githubusercontent.com/u/79602273?v=4)  
_(**GreyXor**)](https://github.com/GreyXor)

[![255kb](https://avatars.githubusercontent.com/u/7489814?v=4)  
_(**255kb**)](https://github.com/255kb)

[![Hamidrzash](https://avatars.githubusercontent.com/u/69453538?v=4)  
_(**Hamidrzash**)](https://github.com/Hamidrzash)

[![HelgeSverre](https://avatars.githubusercontent.com/u/1089652?v=4)  
_(**HelgeSverre**)](https://github.com/HelgeSverre)

[![CJHwong](https://avatars.githubusercontent.com/u/906057?v=4)  
_(**CJHwong**)](https://github.com/CJHwong)

[![hpmouton](https://avatars.githubusercontent.com/u/61012928?v=4)  
_(**hpmouton**)](https://github.com/hpmouton)

[![iagobalmeida](https://avatars.githubusercontent.com/u/35234046?v=4)  
_(**iagobalmeida**)](https://github.com/iagobalmeida)

[![IceyWu](https://avatars.githubusercontent.com/u/66096254?v=4)  
_(**IceyWu**)](https://github.com/IceyWu)

[![eltociear](https://avatars.githubusercontent.com/u/22633385?v=4)  
_(**eltociear**)](https://github.com/eltociear)

[![tltsutltsu](https://avatars.githubusercontent.com/u/83283675?v=4)  
_(**tltsutltsu**)](https://github.com/tltsutltsu)

[![kevinand11](https://avatars.githubusercontent.com/u/48160414?v=4)  
_(**kevinand11**)](https://github.com/kevinand11)

[![JacobCoffee](https://avatars.githubusercontent.com/u/45884264?v=4)  
_(**JacobCoffee**)](https://github.com/JacobCoffee)
