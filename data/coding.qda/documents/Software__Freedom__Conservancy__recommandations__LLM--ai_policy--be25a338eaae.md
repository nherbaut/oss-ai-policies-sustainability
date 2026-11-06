[![Software Freedom Conservancy](/static/img/conservancy-header-logo.322da8acaa91.svg)](/)

Toggle navigation menu

- [News](/news/)
  - ### Press Releases

  - ### Press

  - ### Blog

  - ### Vizio Lawsuit in the News

  - ### Our Issues in the News
- [About](/about/)
  - ### Sponsors

  - ### Sustainers

  - ### Board of Directors

  - ### Staff

  - ### Evaluation Committee

  - ### Outside Counsel, et alia

  - ### Transparency

  - ### Contact
- [Our Work](/activities)
  - ### Copyleft Compliance

    We defend & uphold the rights enshrined in copyleft licenses.

  - ### Impact Litigation

    We defend the legal rights of software users in Court when needed.

  - ### LLM-Gen-AI in FOSS

    We help FOSS contributors navigate this ongoing conundrum.

  - ### FOSSY

    Our annual community-oriented conference.

  - ### Outreachy

    Internships for those who face under­representation, systemic bias, or discrimination in tech.

  - ### Hiring

    SFC is hiring!
- [Tools](#)
  - ### Member Projects

    We provide non-profit infrastructure and services to our members creating Free/Libre and Open Source Software.

  - ### Use The Source

    Our tool for evaluating the source code candidates companies must provide for GPLed software.

  - ### OpenWrt One

    We designed and built the first ever wireless Internet router designed with software freedom and right to repair in mind.
- [Learn](/learn)
  - ### The Corresponding Source

    A bi-weekly oggcast about legal, policy, and many other issues in the Free, Libre, and Open Source Software (FLOSS) world. 

  - ### Glossary of Terms

    A list of terms you might be unfamiliar with but occur frequently in our work.

  - ### FAQ About the Vizio Lawsuit

    Your most frequently asked questions about the Vizio lawsuit, answered in one place.
- [Donate](/sustainer/)

[![Software Freedom Conservancy](/static/img/conservancy-header-logo.322da8acaa91.svg)](/)

Close navigation menu

- [News](/news/)
  - ### Press Releases

  - ### Press

  - ### Blog

  - ### Vizio Lawsuit in the News

  - ### Our Issues in the News
- [About](/about/)
  - ### Sponsors

  - ### Sustainers

  - ### Board of Directors

  - ### Staff

  - ### Evaluation Committee

  - ### Outside Counsel, et alia

  - ### Transparency

  - ### Contact
- [Our Work](/activities)
  - ### Copyleft Compliance

    We defend & uphold the rights enshrined in copyleft licenses.

  - ### Impact Litigation

    We defend the legal rights of software users in Court when needed.

  - ### LLM-Gen-AI in FOSS

    We help FOSS contributors navigate this ongoing conundrum.

  - ### FOSSY

    Our annual community-oriented conference.

  - ### Outreachy

    Internships for those who face under­representation, systemic bias, or discrimination in tech.

  - ### Hiring

    SFC is hiring!
- [Tools](/tools)
  - ### Member Projects

    We provide non-profit infrastructure and services to our members creating Free/Libre and Open Source Software.

  - ### Use The Source

    Our tool for evaluating the source code candidates companies must provide for GPLed software.

  - ### OpenWrt One

    We designed and built the first ever wireless Internet router designed with software freedom and right to repair in mind.
- [Learn](/learn)
  - ### The Corresponding Source

    A bi-weekly oggcast about legal, policy, and many other issues in the Free, Libre, and Open Source Software (FLOSS) world. 

  - ### Glossary of Terms

    A list of terms you might be unfamiliar with but occur frequently in our work.

  - ### FAQ About the Vizio Lawsuit

    Your most frequently asked questions about the Vizio lawsuit, answered in one place.
- [Donate](/sustainer/)

# Recommendations When Using LLM-backed Generative AI Systems for FOSS Contributions

### Preamble

The entire community of computer users, which quickly approaches every human, faces the growing conundrum of generative artificial intelligence systems backed by Large Language Models (“LLM-gen-AI”)[^1]. Software freedom activists face particularly difficult challenges in this regard; these LLM-gen-AI systems have been applied in earnest to the endeavors of software creation and modification.

We cannot sufficiently mitigate this tricky problem with merely one statement or a few blog posts. In 2022, Software Freedom Conservancy began our journey on this particular issue when our policy fellow, Bradley M. Kühn, published [If Software is My Copilot, Who Programmed My Software?](https://sfconservancy.org/blog/2022/feb/03/github-copilot-copyleft-gpl/). In the last year, that journey grew in complexity and urgency when some of SFC’s member projects and supporters began to regularly request moral and ethical guidance on these matters. SFC spent these months in almost-daily internal discussions about the plethora of dilemmas presented by LLM-gen-AI systems.

In 2024, [SFC published an aspirational statement](https://sfconservancy.org/news/2024/oct/25/aspirational-on-llm-generative-ai-programming/), a thought experiment rather than a definition. We now make urgent recommendations to those ordered by their employers to use LLM-gen-AI code assistants to contribute to Free and Open Source Software (“FOSS”).

Some FOSS project leaders have taken a zero-tolerance approach to any LLM-gen-AI contributions to their projects. We support leaders who make such decisions. FOSS project leaders deserve our sympathy and understanding regarding the voluminous onslaught of new contributions. Patch evaluation has always required careful analysis (after all, humans write bad code too). Now, that analysis demand (reasonably) feels daunting to maintainers. Everyone should respect their decisions.

Nevertheless, we cannot and must not ignore the many FOSS contributors who decide to explore these tools for the betterment of FOSS. Software freedom activism only succeeds when we admit that we are at least decades away from universal software freedom. Proprietary systems will continue to exist; there is a real danger they will continue to leapfrog FOSS. We should resist the use of proprietary systems, which include the most popular LLM-gen-AI systems, but we should also remain willing ([as we always have](https://sfconservancy.org/blog/2026/jun/02/ethical-use-proprietary-develop-free-software-foss/)) to utilize such systems when they can advance software freedom.

After much study, consideration, collaboration, and consultation with many FOSS leaders, SFC formulated the following recommendations for FOSS contributors who have decided to use LLM-gen-AI systems to augment their FOSS work. We expect to update these recommendations periodically. These are not mandates, demands, conclusions, nor definitions; rather, they are best practices that we have formulated after careful study of the undeniable reality that some FOSS contributors do want to use these LLM-gen-AI systems.

In the months following the announcement of these recommendations, SFC plans an ongoing engagement campaign, including documents, online tutorials, public Q&As, and other community engagement, on these matters. SFC does not make these recommendations in isolation; rather, we offer sustained assistance to the community, particularly to FOSS projects working with proprietary LLM-gen-AI systems.

The long term goal of software freedom is to eliminate the harm of proprietary technology. While we work toward that greater goal, we should seek to mitigate the harms that we cannot immediately eliminate. These recommendations aim to abate the damage of these systems, and also consider how these tools might counter-intuitively *help* us advance FOSS.

## Recommendations

These recommendations are listed in order of our view of their relative importance (most important first).

1.  **The FOSS community should support, not just tolerate, those who outright reject LLM-gen-AI systems.** There are many intersecting ethical and moral issues regarding these systems, many of which are not currently fully understood. Anyone who chooses to avoid them deserves our support and assistance.

2.  **Every FOSS contributor deserves self-determination regarding LLM-gen-AI.** No one should be *required* to use these systems under duress. We make special note here of the increasing reports from technology workers who have been ordered by their management (often under penalty of termination) to use these systems for all their work: FOSS and proprietary. Such mandates are unconscionable and we call on the industry to make use of LLM-gen-AI fully optional, and adopt non-discrimination policies regarding those who opt out.

3.  **FOSS projects should not shun contributors who choose to use LLM-gen-AI systems.** Even FOSS projects that have chosen a zero-tolerance policy should make an effort to welcome contributors who submit a contribution that includes content or who received assistance from an LLM-gen-AI system. Such contributions should be treated no differently than a technically inadequate “first patch”: such submitters should be welcomed to the community and receive a gentle (albeit perhaps form language) response thanking them for their interest and explaining gently why the project will not accept their contribution.

4.  **Before submission, FOSS Contributors must invest substantial time reviewing LLM-gen-AI -assisted and/or -generated contributions.** Such contributions need curation. Contributors should acquire an in-depth understanding of their contribution. FOSS processes yield software systems that are resilient, highly maintainable, and contributor-friendly. Human contributors engage with FOSS projects (even as volunteers) because of the enjoyment and satisfaction available in FOSS projects. **LLM-gen-AI contributions could erode the best aspects of FOSS if an unsolicited onslaught of unvetted, prompt-generated contributions become commonplace.**

5.  **Full disclosure of how and when an LLM-gen-AI system was utilized to assist in creation of a contribution is a moral imperative.** FOSS project leaders cannot make good decisions about LLM-gen-AI policy if they cannot survey which contributions were assisted, and how much they are assisted. Part of the contribution process should (at least) include a disclosure of what LLM-gen-AI system was used, its version (as these system change over time), and a brief description of how the system assisted the contributor. This information should be included in a machine-readable format in commit logs.

6.  **Contributors should only submit “unattended”[^2] LLM-gen-AI contributions in an area explicitly designated for such. If none exists, such contributions should be assumed unwelcome.** FOSS maintainers are often volunteers, or permitted to work only a limited amount of time on their upstream projects. Maintainers’ time is precious, and is best used in human-to-human interactions with new and existing human contributors. New contributors should respect existing decisions about “unattended” LLM-gen-AI. Maintainers should think carefully about the types of unattended LLM-gen-AI contributions that may be useful. We encourage project leaders to flexibly and regularly (but also slowly and deliberately) consider policy changes on unattended contributions when new contributors present new ideas.

7.  **LLM-gen-AI users should keep detailed and accurate records of their interaction and save those meta-artifacts for posterity.** LLM-gen-AI systems excel at automation of users’ logs of prompts, notes, and other written details of the interaction that led to the creation of an artifact. FOSS contributors should keep such meta-artifacts, and *regardless of license* they should be archived as if they are part of the Corresponding Source for the contribution. (In the coming weeks, SFC will publish tutorials and templates to assist in automating this important process.)

8.  **Avoid jumping to conclusions about the legal significance of generated contributions and whether they are “copyright-washing-machines that ruin copyleft”.** There remain many unanswered legal questions, and experts are actively working on solutions. SFC will publish more on this issue in the coming months.

9.  **Inputs impact the licensing of the artifacts**. The question of licensing obligations for material passed through the process called “training” remains undecided. Nevertheless, most LLM-gen-AI sessions don’t begin *only* with a prompt. By contrast, most commonly, the user points the LLM-gen-AI at a codebase and receives its assistance to generate a patch for that codebase. If that codebase is under a copyleft license, your changes *must* be licensed under the project’s license, due to both copyright and contractual terms of that license.

10. **“Copyleft Everything” remains the best viable and safest approach** Certainly those who want to release FOSS under non-copyleft licenses have more to worry about when using these tools. It’s apparent that every widely used LLM-gen-AI was trained on much well-known copylefted code. Courts need years to deliver guidance on many relevant legal questions. In the meantime, *nothing* stops you from using a copyleft license for the work you generate, particularly a license that is widely compatible with other copyleft licenses. SFC will make its staff time available to the [copyleft-next](https://next.copyleft.org) project to eventually offer a license that is widely compatible with other copylefts and extremely suitable as a copyleft for LLM-gen-AI outputs.

11. **When LLM-gen-AI systems (including proprietary ones) can massively accelerate FOSS improvements, use of such tools is an appropriate strategic compromise**. Most FOSS developers are not experts in the area of creation and training of LLM-gen-AI systems. Those developers should feel comfortable making the strategic choice to use LLM-gen-AI systems in these cases.

    We detest using proprietary tools and we are never comfortable recommending them. Yet [for nearly fifty years, FOSS contributors have used proprietary tools](https://sfconservancy.org/blog/2026/jun/02/ethical-use-proprietary-develop-free-software-foss/) to create and advance software freedom. *Writing* proprietary systems is undoubtedly an anti-social act that we all should avoid. *Using* proprietary systems, particularly when they can forward FOSS, is a highly fact-dependent tactical decision.

    **Warning**: do take great care to fully understand the implications of any proprietary license. SFC will publish in the coming weeks some guidance on how to approach such analysis.

12. **Those with skills and interest in making FOSS-friendlier LLM-gen-AI systems should do so as a matter of high priority**. While no system meets the (currently) [Impossible Dream of our aspirational system](https://sfconservancy.org/news/2024/oct/25/aspirational-on-llm-generative-ai-programming/), there are obvious avenues of pursuit that will make progress in that direction. SFC will highlight on our blog in the coming months individuals working in these directions.

13. **Do not overuse LLM-gen-AI, or allow your skills to atrophy**. In our discussions with the FOSS community about LLM-gen-AI, there seems to be one universal conclusion: the systems are most effective and help the most when a very experienced FOSS developer sits at the prompting helm. LLM-gen-AI systems should *complement* existing skills and tools, not *replace* them. Developers should remain *curious* about why software acts the way it does, and this curiosity should extend to the LLM-gen-AI outputs — and even the system itself.

14. **Think carefully about your usage**. As software technologists, we have for decades made complex choices regarding resource consumption vs. convenience. The advent of CI, as just one example, led to massive increases in computing time, while at the same time simplified contribution workflows. As individual FOSS developers, we are unlikely to change the bad behavior of these proprietary software companies who are either focusing on the creation of, or mandating the excessive use of, LLM-gen-AI.

    There are hundreds of intersectional issues of societal significance and social justice that are touched by these technologies, including the environmental impact of the development and use of these systems. Our focus and expertise centers on the implications for software; here we assess user freedom and add our ideas to the overall social conversations about how this technology should be used, controlled, and distributed in the context of FOSS. On matters unrelated to software freedom, we defer to experts that focus on environmental and other intersectional issues.

    In our experience, FOSS contributors are historically much more mindful and concerned about how their actions impact others than developers of proprietary software and systems. Bring that mindfulness to your use of LLM-gen-AI. As just two examples:

    - don’t run to an LLM-gen-AI immediately for every problem,

    - pay attention to the LLM-gen-AI when it is clearly doing useless processing, and quickly redirect it to something more useful.

### The Road Ahead

Most new technologies have some adverse outcomes. We must carefully recognize and mitigate them. Social justice movements (including the software freedom and software right-to-repair movements) succeed when well-intentioned individuals act sustainably and consistently to bring needed change. In FOSS, those individuals constantly invent and improve new technologies that respect users’ rights and freedoms.

The recommendations above are a start. We’re ready for revision and further explanation as facts change. Our community has successfully deployed our unique acumen, and will again to shift this current imbalance of power. We must creatively act as we always have; the FOSS community excels at strategems that counteract proprietary software with ingenuity.

SFC walks with you on this multi-generational journey to universal software freedom and rights.  
Expect (but embrace) the trepidation as we take this next step together now. SFC’s goal is steadfast: empower consumers and users to advance and exercise software freedom, and their right to software repair. Remember these strategies have worked and **will continue to work** when we remain vigilant, mindful, and focused.

#### Acknowledgments

Software Freedom Conservancy publishes this statement after months of internal deliberation and discussions with a group of volunteers, including John Sullivan, Stefano Zacchiroli, and many anonymous contributors. The statement was drafted by SFC in collaboration with that group.

#### Footnotes

[¹](#return-which-systems) These Recommendations are made specifically for systems (most of which are currently proprietary), such as Claude Code, Copilot CLI, Antigravity, and OpenCode. These systems utilize an LLM to generate textual artifacts that assist software project contributors. There is no known shorthand for referring to these systems, so we refer to them here as “LLM-gen-AI” to remind the reader throughout that these recommendations are not necessarily intended to apply to other forms of AI nor other uses of LLMs

[^3]

By “unattended”, we mean prompt-generated contributions that received no further human vetting.

## What We Do

- [The Corresponding Source](/casts/the-corresponding-source/)
- [Copyleft Compliance](/copyleft-compliance/)
- [Vizio Lawsuit](/copyleft-compliance/vizio.html)
- [Facing LLM-gen-AI in FOSS](/llm-gen-ai/)
- [Past Impact Litigation](/copyleft-compliance/past-lawsuits.html#past)
- [*Give Up GitHub!*](https://GiveUpGitHub.org/)
- [Member Projects](/projects/)
- [Outreachy](https://outreachy.org)
- [Use The Source](/usethesource/)
- [FOSSY](https://fossy.us)
- [OpenWrt One](/activities/openwrt-one.html)
- [Awards](/activities/awards.html)

## Facing LLM-gen-AI in FOSS

- [Recommendations When Using LLM-backed Generative AI Systems for FOSS Contributions](/llm-gen-ai/llm-backed-generative-ai-recommendations.html)
- [Aspirational Statement on FOSS LLM-gen-AI](/llm-gen-ai/aspirational-statement-on-llm-generative-ai-for-programming.html)
- More to come …

[![Software Freedom Conservancy](/static/img/conservancy-header-logo.322da8acaa91.svg)](/)

- [Main Page](/)
- [Contact](/about/)
- [Sponsors](/sponsors/)
- [RSS Feed](/feeds/omnibus/)
- [Donate](/sustainer/)

Software Freedom Conservancy is a 501(c)(3) non-profit charity.

[Privacy Policy](/privacy-policy/) last updated 22 December 2020.

This page and its contents are licensed under a [Creative Commons Attribution-Share Alike 4.0 International License](https://creativecommons.org/licenses/by-sa/4.0).

[![Creative Commons Attribution-Share Alike 4.0 International License](/static/img/creative-commons-footer-icons.42c681015296.svg)](https://creativecommons.org/licenses/by-sa/4.0)

[^1]:

[^2]:

[^3]:
