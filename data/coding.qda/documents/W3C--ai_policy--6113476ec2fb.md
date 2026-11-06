[![W3C](https://www.w3.org/StyleSheets/TR/2021/logos/W3C)](https://www.w3.org/)

# Use of Large Language Models in Standards Work

[W3C Group Note](https://www.w3.org/standards/types#NOTE) 24 March 2026

More details about this document

This version:  
[https://www.w3.org/TR/2026/NOTE-llms-standards-20260324/](https://www.w3.org/TR/2026/NOTE-llms-standards-20260324/)

Latest published version:  
\<https://www.w3.org/TR/llms-standards/\>

Latest editor's draft:  
\<https://w3c.github.io/AB-public/position-statements/llms-standards/\>

History:  
\<https://www.w3.org/standards/history/llms-standards/\>

[Commit history](https://github.com/w3c/ab-public/commits/)

Editors:  
[Hidde de Vries](mailto:hidde@hiddedevries.nl) (Logius)

[Elena Lape](mailto:elena@holopin.io) (Holopin)

Feedback:  
[GitHub w3c/ab-public](https://github.com/w3c/ab-public/) ([pull requests](https://github.com/w3c/ab-public/pulls/), [new issue](https://github.com/w3c/ab-public/issues/new/choose), [open issues](https://github.com/w3c/ab-public/issues/))

[Copyright](https://www.w3.org/policies/#copyright) © 2026 [World Wide Web Consortium](https://www.w3.org/). W3C^(®) [liability](https://www.w3.org/policies/#Legal_Disclaimer), [trademark](https://www.w3.org/policies/#W3C_Trademarks) and [document use](https://www.w3.org/copyright/document-license/ "W3C Document License") rules apply.

------------------------------------------------------------------------

## Abstract

As Large Language Models (LLMs) become increasingly synonymous with “AI”, and are used by people within our community, we want to highlight considerations around different ways in which LLMs can be useful or problematic when it comes to leveraging them in standards work at W3C.

## Status of This Document

*This section describes the status of this document at the time of its publication. A list of current W3C publications and the latest revision of this technical report can be found in the [W3C standards and drafts index](https://www.w3.org/TR/).*

This document summarizes the Advisory Board’s current thinking, as of 24 March 2026. New initiatives by the W3C Team on [AI & the Web](https://www.w3.org/reports/ai-web-impact/), various AI-related Working Groups such as the [WebML WG](https://www.w3.org/groups/wg/webmachinelearning/) and [GPU for the Web WG](https://www.w3.org/groups/wg/gpu/), and the [Web & AI Interest Group](https://www.w3.org/groups/ig/webai/) show that this conversation is timely.

This document was published by the [Advisory Board](https://www.w3.org/groups/other/ab) as a Group Note using the [Note track](https://www.w3.org/policies/process/20250818/#recs-and-notes).

This Group Note is endorsed by the [Advisory Board](https://www.w3.org/groups/other/ab), but is not endorsed by W3C itself nor its Members.

The [W3C Patent Policy](https://www.w3.org/policies/patent-policy/) does not carry any licensing requirements or commitments on this document.

This document is governed by the [18 August 2025 W3C Process Document](https://www.w3.org/policies/process/20250818/).

## Table of Contents

1.  [Abstract](#abstract)
2.  [Status of This Document](#sotd)
3.  [1. Where Benefits May Outweigh Risks](#where-benefits-may-outweigh-risks)
    1.  [1.1 Demos, Tests and Examples](#demos-tests-and-examples)
    2.  [1.2 Interrogate, Spellcheck, Edit Standards](#interrogate-spellcheck-edit-standards)
    3.  [1.3 Brainstorming Names](#brainstorming-names)
4.  [2. Where Risks May Outweigh Benefits](#where-risks-may-outweigh-benefits)
5.  [3. Combining Accountability with Best Practices](#combining-accountability-with-best-practices)

## 1. Where Benefits May Outweigh Risks

So far, LLMs have shown to benefit the standards process in several ways:

### 1.1 Demos, Tests and Examples

When paired with deep domain expertise, LLM coding assistants can help to build proof-of-concept level demos or write tests of specific web platform features. The ability to quickly generate and show a group many examples during a meeting helps verify concepts faster, reduces manual effort, and makes discussions more productive.

### 1.2 Interrogate, Spellcheck, Edit Standards

In addition to basic spellchecking, and editing, which are especially facilitative for our international community, LLMs can be used to ask questions about web standards to identify problems, gaps, and possibilities to improve.

### 1.3 Brainstorming Names

New standards work often needs new names. Those names should be easy to understand while still fitting platform conventions and avoiding conflicts with existing terms. Because LLMs are trained on a very large sample of human language, they're a great tool to use when trying to come up with human friendly names for novel concepts.

## 2. Where Risks May Outweigh Benefits

In some cases, there are serious risks.

First, there is a possibility of copyright infringement. As LLMs may be trained on copyrighted materials, even well-meaning contributions could create associated liability.

There could also be security risks. Providing Member Confidential information to LLMs could result in data leakage (we suggest particular caution with free products).

Sometimes there’s subtle incorrectness. LLM-generated text and code may contain subtle falsehoods, which are hard to spot and difficult to debug.

If a specification concerns something that does not yet exist, like [the decade-old debate of defining what the scope of a “view” is](https://hidde.blog/views/), LLMs are unlikely to be helpful, as they’re often trained on stale data that doesn’t necessarily incorporate the most recent discussions, especially if they took place over email or meetings.

Verbosity is a possible issue too. At W3C, we’ve always exchanged lengthy arguments, but if we automate writing them we could end up with more text that is less intentional and less meaningful. This can result in “second-hand burdening” that can thwart our community’s effectiveness.

W3C has a long tradition of scribing discussions manually. It lets us take a step back, and reflect on and interpret how a room understood a discussion. Fully outsourcing this to LLMs risks losing that tradition, and introduces risks of misattribution, biased attribution, factual incorrectness, and increase of minute length with irrelevancies.

Lastly, there is a climate impact. Production and usage of LLMs has a climate footprint (including energy and water use) that is disproportionately high, when compared to the production and usage of alternatives, such as manually writing text. As the web platform is built with [commitment to sustainability in mind](https://www.w3.org/TR/ethical-web-principles/#sustainable), it is worth considering this in the tools we use while developing the platform’s standards.

## 3. Combining Accountability with Best Practices

Ultimately, each individual is responsible for their own output. Whether or not an LLM is used is a matter of personal choice — the work produced remains the responsibility of the person behind it.

When LLMs are used, we suggest implementing these guardrails:

- **Check before sharing**: thoroughly check all content for correctness, and ensure no unintended information has been included, and that any content attributed to a person, for instance in minutes, reflects what they actually said.
- **Clearly label LLM output**: when content is primarily output from an LLM, label it as such. This helps collaborators evaluate the content. For instance, introduce output with “I got the following from an AI:”.
- **Assume full responsibility for the content**: when content is (partially) output from an LLM, it is upon the person sharing the content to take responsibility for it.
- **Prefer smaller and more task-specific models over large and general-purpose models**: smaller models usually use less energy.
- **Embrace thoughtful discussions**: avoid using LLMs instead of deliberation. For instance, in asynchronous discussions, writing can help the thought process, while generating replies with an LLM would sidestep that process.

[↑](#title)
