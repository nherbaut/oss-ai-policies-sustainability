Menu

Expand

Light mode

Dark mode

Auto light/dark, in light mode

Auto light/dark, in dark mode

[Skip to content](#furo-main-content)

[Docs Home](/)

Categories

[User documentation](https://wiki.postmarketos.org/) [Policies and Processes](https://docs.nura.eco/policies-and-processes/index.html) [PMCR](https://docs.nura.eco/pmcr/main/index.html)

Projects in pmOS

[pmaports](https://docs.nura.eco/pmaports/main/index.html) [pmbootstrap](https://docs.nura.eco/pmbootstrap/main/index.html) [mrtest](https://docs.nura.eco/mrhlpr/main/usage.html#mrtest) [mrhlpr](https://docs.nura.eco/mrhlpr/main/usage.html#mrhlpr) [docs.nura.eco](https://docs.nura.eco/dne/index.html) [BPO](https://docs.nura.eco/bpo/main/index.html) [hardware-ci](https://docs.nura.eco/hardware-ci/index.html) [phone-harness](https://docs.nura.eco/phone-harness/main/index.html) [mobile-config-firefox](https://docs.nura.eco/mobile-config-firefox/main/index.html)

Policies and Processes

![Nura Logo](../_static/logo.svg)

Policies and Processes

- [Development](../development.html)☒
  - [How to Register on Our GitLab Instance](gitlab.html)
  - [AI Policy](#)
  - [Code Review / Merge](code-review-and-merge.html)
  - [Project Maintainers](project-maintainers.html)
  - [Triaging](triaging.html)
- [Community](../community.html)☐
  - [Code of Conduct](../community/code-of-conduct.html)☐
    - [Community Spaces](../community/code-of-conduct/community-spaces.html)
    - [Transparency reports](../community/code-of-conduct/transparency-reports.html)
  - [Hosted Mainline Communities](../community/soc-communities.html)
- [Governance](../governance.html)☐
  - [Conflict of Interest Policy](../governance/conflict-of-interest.html)
  - [Groups and Teams](../governance/groups-and-teams.html)☐
    - [Board of Directors](../governance/groups-and-teams/board-of-directors.html)
    - [The Membership](../governance/groups-and-teams/the-membership.html)
    - [Code of Conduct Team](../governance/groups-and-teams/coc-team.html)
    - [Finance Team](../governance/groups-and-teams/finance-team.html)
    - [Social Media Team](../governance/groups-and-teams/social-media-team.html)
  - [Team Meetings](../governance/team-meetings.html)☐
    - [Meeting Notes](../governance/team-meetings/meeting-notes.html)
    - [Code of Procedures for Deliberative Assemblies](../governance/team-meetings/code-of-procedures.html)
  - [Finances](../governance/finances.html)☐
    - [Contract Policy](../governance/finances/contracts.html)
    - [Projects](../governance/finances/projects.html)
    - [Expenditure Policy](../governance/finances/expenditures.html)
    - [Yearly Budgets and Updates](../governance/finances/yearly-budget-and-updates.html)
    - [Contributor Support Programme](../governance/finances/contributor-support-programme.html)
  - [Employment](../governance/employment.html)☐
    - [Recruitment and Hiring Policy](../governance/employment/hiring-policy.html)
  - [Association Statutes](../governance/statutes.html)☐
    - [Chapter I: Name - Registered Office – Duration](../governance/statutes/chapter-1-name-registered-office-duration.html)
    - [Chapter II: Goal – Activities](../governance/statutes/chapter-2-goal-activities.html)
    - [Chapter III: Members](../governance/statutes/chapter-3-members.html)
    - [Chapter IV: Membership fees](../governance/statutes/chapter-4-membership-fees.html)
    - [Chapter V: General Assembly](../governance/statutes/chapter-5-general-assembly.html)
    - [Chapter VI: Board of Directors](../governance/statutes/chapter-6-board-of-directors.html)
    - [Chapter VII: Miscellaneous Provisions](../governance/statutes/chapter-7-misc-provisions.html)
    - [OTHER PROVISIONS](../governance/statutes/chapter-7-misc-provisions.html#other-provisions)
- [Events](../events.html)☐
  - [Organized by Nura](../events/organized-by-nura.html)☐
    - [Sponsoring](../events/organized-by-nura/sponsoring.html)
  - [Representing Nura](../events/representing-nura.html)

[Back to top](#)

[Edit this page](https://gitlab.postmarketos.org/postmarketOS/docs.nura.eco/-/blob/main/docs/policies-and-processes/development/ai-policy.md "Edit this page")

# AI Policy

Important

We forbid the use of generative AI tools in Nura.

The following is not allowed in Nura:

- Submitting contributions fully or in part created by generative AI tools to Nura.

- Recommending generative AI tools to other community members for solving problems in the Nura space.

If somebody keeps on violating these rules, we may escalate the situation according to the [Code of Conduct Enforcement Guidelines](../community/code-of-conduct.html#coc-enforcement-guidelines) with warnings and temporary/permanent bans.

## Reasoning

AI tools have several ethical issues. They require an unreasonable amount of energy[^1] and water[^2] to build and operate, their models are built in part with heavily exploited workers in unacceptable working conditions[^3], usually without consent from or compensation for creators of the source material[^4] and oftentimes causing DDoS attacks against FOSS infrastructure in the process[^5] (which in turn force the deployment of challenge-based protections and increase cost and complexity of self-hosting for everybody[^6]). Furthermore, they are being used to undermine labor and justify layoffs[^7]. These are harms that we do not want to perpetuate, even if only indirectly.

Additionally, authors making use of generative AI tools oftentimes increase the maintainer burden and cause further problems by not ensuring the following:

- Understanding completely how the code in their contribution works.

- Describing the change accurately in the commit message.

- Testing the contribution and ensuring it works as described.

- Making sure their patches are unlikely to introduce bugs, especially security bugs.

- Not violating copyright (such as software licenses, creative commons or any other).

------------------------------------------------------------------------

\[[1](#id1)\]

*“After pledging to slash its greenhouse gas emissions, Microsoft’s climate pollution has grown by 30 percent as the company prioritizes AI.”* — [The Verge](https://www.theverge.com/2024/5/15/24157496/microsoft-ai-carbon-footprint-greenhouse-gas-emissions-grow-climate-pledge), 2024-05-15

\[[2](#id2)\]

*“Over the past 12 years, 16 data centers have been approved in Santiago’s metropolitan area. Most use millions of liters of water annually to keep computers from overheating. Chile is in the midst of a drought, expected to last until 2040.”* — [Rest of World](https://restofworld.org/2024/data-centers-environmental-issues/), 2024-05-31

\[[3](#id3)\]

*“OpenAI Used Kenyan Workers on Less Than \$2 Per Hour to Make ChatGPT Less Toxic”* — [TIME](https://time.com/6247678/openai-chatgpt-kenya-workers/), 2023-01-18

\[[4](#id4)\]

*“Amid the rise of generative AI, creators, artists and media rights holders have been forced to reckon with the unlicensed use of their copyrighted material to train AI models without consent or compensation.”* — [Variety](https://variety.com/vip-special-reports/ai-training-consent-content-licensing-special-report-1236307878/), 2025-03-03

\[[5](#id5)\]

*“When one of these botnets goes nuts, the result is indistinguishable from a distributed denial-of-service (DDOS) attack — it is a distributed denial-of-service attack. Should anybody be in doubt about the moral integrity of the people running these systems, a look at the techniques they use should make the situation abundantly clear.*” — [LWN.net](https://lwn.net/Articles/1008897/), 2025-02-14

\[[6](#id6)\]

Including our infrastructure. As of writing (2025-09), [Anubis](https://anubis.techaro.lol/) is being used by the Nura GitLab instance and wiki as well as [many other sites](https://anubis.techaro.lol/docs/user/known-instances/) and Alpine’s GitLab is protected by [go-away](https://git.gammaspectra.live/git/go-away) to fight off scrapers. Many other websites have adopted similar restrictions.

\[[7](#id7)\]

*“Since the rise of generative AI, many have feared the toll it would take on the livelihood of human workers. Now CEOs are admitting AI’s impact and layoffs are starting to ramp up.”* — [Forbes](https://www.forbes.com/sites/richardnieva/2025/07/17/ai-tech-layoffs/), 2025-07-17

Next

Code Review / Merge

Previous

How to Register on Our GitLab Instance

Copyright © 2026 Nura contributors

Made with [Sphinx](https://www.sphinx-doc.org/) and [@pradyunsg](https://pradyunsg.me)'s [Furo](https://github.com/pradyunsg/furo)

On this page

- [AI Policy](#)
  - [Reasoning](#reasoning)

[^1]:

[^2]:

[^3]:

[^4]:

[^5]:

[^6]:

[^7]:
