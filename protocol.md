---
title: "Sustainability in the AI Policies of Open Source Projects: A Grey Literature Review"
subtitle: "Idea note for ICT4S 2027"
author: "NeS team, LaBRI"
date: "October 2026"
---

# Motivation

- Open source software (OSS) projects increasingly rely on generative AI (GenAI): coding agents were adopted by 22--29% of 128,018 GitHub projects within months of their release [@robbes2026agentic].
- Practices are highly diverse: no convention exists, even on what contributors must disclose, and many policy files are revised within months [@hora2026permit].
- Policies are written mostly in reaction to GenAI ("AI slop", review load, licensing), not out of a sustainability agenda [@hora2026permit].
- Sustainability is a *wicked problem* [@rittel1973dilemmas]: its dimensions are interdependent, improving one can degrade another, and no single objective can be optimised.
- We do not know whether, and how, OSS communities frame sustainability when they regulate GenAI.

# Research questions and hypotheses

- **RQ1.** Is sustainability addressed in the stated purpose (*raison d'être*) of open source projects?
    - *H1:* yes, or partially.
- **RQ2.** Is sustainability addressed in the AI policies of open source projects?
    - *H2:* no, or only partially.
- **RQ3.** Which definitions and characteristics of sustainability are addressed in these AI policies?
    - *H3:* mostly technical and individual sustainability, centred on the maintainer (workload, code quality, burnout).
- **RQ4.** Do these definitions provide frameworks leading to strong sustainability?
    - *H4:* no.

# Methodology

We follow the guidelines for multivocal and grey literature reviews of @garousi2019guidelines. AI policies are grey literature (`CONTRIBUTING.md`, `AI_POLICY.md`, governance pages, discussion threads), so a classical systematic literature review does not apply.

## Planning

- Define the review goal and the four RQs above.
- Decide that grey literature is the primary source, because academic work does not yet cover policies produced by communities.
- Complement it with a short academic search to ground the sustainability framework used in the coding scheme.

## Source selection and search

- **Project sample.** Select OSS projects by explicit criteria (for example popularity, foundation membership such as Linux Foundation or Apache, domain diversity), using the corpus of @hora2026permit as a starting point.
- **Policy files.** Collect AI policies from the repositories, project websites, and governance documents.
- **Purpose statements (RQ1).** Collect README, mission statements, manifestos, and charters.
- **Search.** Keyword queries (e.g., "AI policy", "LLM", "Copilot", "generated code") on GitHub code search and web search engines, with snowballing from links and mentions.
- **Stopping criterion.** Stop when new sources no longer add new codes (theoretical saturation).
- **Freezing.** Fix a collection date and archive every document (Software Heritage, Wayback Machine) for reproducibility, since policies change quickly.

## Inclusion and quality assessment

- **Inclusion.** The document states rules or positions on AI-generated contributions or AI tool use in the project.
- **Exclusion.** Duplicates, forks that copy a policy verbatim (counted once), documents not in English or French, and unofficial opinions of individuals.
- **Quality.** Apply the grey literature criteria of @garousi2019guidelines: authority of the producer, methodology, objectivity, date, novelty, and impact.
- Record whether each document is official (merged policy) or a proposal under discussion.

## Data extraction

- Project metadata: size, age, governance, foundation, domain.
- Policy metadata: date, version history, stance (ban, permit with conditions, permit freely), disclosure requirement.
- Verbatim excerpts that mention sustainability or related terms.

## Coding scheme and synthesis

- **Sustainability dimensions.** Deductive codes from the Karlskrona manifesto [@becker2015sustainability]: individual, social, economic, environmental, and technical. Inductive codes are added as they emerge.
- **Strength of sustainability.** Each definition is classified as *weak* (substitutability between natural and other capital) or *strong* (critical natural capital must be preserved) [@neumayer2013weak].
- **Procedure.** Thematic analysis [@braun2006thematic], with two coders on a sample, inter-rater agreement (Cohen's kappa), and disagreements resolved by discussion.
- **Mapping to RQs.**
    - RQ1: presence or absence of sustainability in purpose statements.
    - RQ2: presence or absence of sustainability in AI policies.
    - RQ3: distribution of dimensions and definitions across policies.
    - RQ4: classification of definitions as weak or strong, and analysis of interdependencies between dimensions.

## Threats to validity

- **Selection bias.** Popular projects may not represent the long tail; mitigated by explicit sampling criteria and a stratified sample.
- **Volatility.** Policies change; mitigated by a frozen and archived corpus.
- **Implicit sustainability.** Projects may address sustainability without naming it; mitigated by a broad keyword set and manual reading.
- **Coder subjectivity.** Mitigated by a double-coded sample and agreement metrics.
- **Policy versus practice.** Policies say little about actual behaviour; this is a stated limit of the study.

## Expected contributions

- A map of how OSS communities frame sustainability when regulating GenAI.
- A coding grid of sustainability dimensions that can be reused.
- Recommendations for maintainers, for instance a template sustainability clause for AI policies.

# References {-}

::: {#refs}
:::
