# Provisional coding guide

This guide operationalizes the questions and five dimensions already named in `protocol.md`. It does not claim to validate the underlying theoretical framework. This is an AI-assisted, single-analyst pilot, with no independent human coding or agreement measurement.

## Unit and evidence requirements

The sampling unit is a dataset entity; the coding unit is a passage in a document. An entity can have several documents and several dimensions. Foundation recommendations, project policies, advisory notes and general repository guidelines retain their separate roles. A policy adopted by reference is one policy chain, not two independent observations.

Every interpretation requires an exact excerpt, source path, line range, applicable RQ, scope and rationale. `evidence.csv` preserves literal text, including source wrapping and Markdown. `evidence.md` offers a readable rendering. Labels describe the passage, not independently verified real-world effects.

Read the surrounding subsection before coding. Exclude navigation, related articles, footers, links whose text is unrelated to the policy, and bot challenges. General contribution guidance must not be silently counted as AI-policy evidence. Retrieved source filenames such as `other_policy.md` do not establish the original document's role.

## RQ1: project purpose

Use mission, about, introductory purpose and stated organizational principles. A README's installation advice, CI tips, sponsor links and generic legal disclaimer do not establish its raison d'être. A purpose-like statement inside an AI policy may be recorded separately, with its location made explicit.

| Status | Rule |
| --- | --- |
| `explicit_sustainability` | The purpose/principles passage explicitly uses sustainability language. Record which concern it describes; the word alone is not an environmental commitment. |
| `interpreted_dimension` | Stated purpose or values support a specific dimension, with the mapping explicitly identified as analyst interpretation. |
| `purpose_only` | A functional purpose is available, but the selected purpose passages do not establish a sustainability commitment. This does not mean the project has no such commitment elsewhere. |
| Source unavailable / insufficient evidence | Use when meaningful purpose material cannot be obtained; do not substitute imagined intentions or infer them from the project's subject area. |

## RQ2: sustainability in AI policy

The mutually exclusive case-level statuses below make environmental acknowledgment, sustainability wording and analytical inference distinguishable. When several apply, use the first applicable status in this table; retain all supporting passages in the ledger.

| Status | Rule |
| --- | --- |
| `explicit_environmental_concern` | The AI-related text explicitly names environmental impacts or resource concerns. It need not use the word sustainability. |
| `explicit_sustainability_ai` | The AI-related subsection explicitly uses sustainability language about a stated concern. |
| `implicit_concern_ai` | An AI-related rationale explicitly protects finite human capacity, learning, community continuity or maintainability. Calling this sustainability is an analyst interpretation. |
| `general_context_only` | Relevant concerns are in general guidance; the AI subsection does not establish a sufficiently specific sustainability rationale. |
| `generic_rules_only` | Generic quality, disclosure, accountability or legal requirements are available, but do not establish a sustainability-specific rationale in the reviewed AI text. |

Unusable or unavailable policies must remain missing evidence. Forgejo has a usable supplementary retrieval in this pilot; its local bot challenge remains unusable.

## RQ3: dimensions and definitions

| Dimension | Candidate textual evidence | Do not infer from |
| --- | --- | --- |
| Individual | Finite attention, reviewer overload, skill preservation, learning and explicitly identified personal workload. | Accountability alone; workload as proof of clinical burnout. |
| Social | Community trust, fairness, inclusion, human relationships, labor conditions, newcomer participation and future-maintainer development. | A product merely being a social network; every human-in-the-loop rule. |
| Economic | Explicit costs, financial viability or livelihoods. | Every licensing restriction, review-time statement, or value/cost metaphor. |
| Environmental | Energy, water, emissions, land, ecological harm, waste or explicit environmental concern. | Solar physics, the Carbon programming-language name, or fast execution alone. |
| Technical | Maintainability, ongoing support, resilience and continuity of software or infrastructure. | Every test, correctness requirement, performance claim, or security feature alone. |

Allow multiple dimensions when the excerpt supports them; explain each mapping. General-guideline and purpose codes are excluded from AI-specific dimension counts. The purpose-like statement embedded in Mastodon's policy remains included as policy evidence and is separately labeled.

Distinguish a **concern**, a **rule/measure**, a **rationale**, and a **definition/framework**. The pilot establishes candidate concerns more readily than formal definitions. Legal provenance, disclosure and human accountability may be recorded as separate policy themes without forcing them into a sustainability dimension. Unknown or ambiguous meanings remain unclassified.

## RQ4: strength of sustainability

The protocol defines weak sustainability through substitutability between natural and other capital, and strong sustainability through preservation of critical natural capital. Look for direct textual support for those commitments, ecological constraints and the treatment of trade-offs.

- Assign **strong** only when the reviewed framework establishes the relevant preservation/non-substitutability commitment. Record the supporting passage and reasoning.
- Assign **weak** only when the text supports the relevant substitution position. Efficiency or technological optimism alone is insufficient.
- Assign **insufficient evidence** when neither interpretation can be substantiated. A ban on AI, an environmental concern, a neutrality claim or an absence of sustainability vocabulary establishes neither category.

Normative no-further-harm language may be a framework indicator worth discussing, but must not be promoted into an unsupported claim of a complete strong-sustainability framework. A policy's stated aim does not establish its practical outcomes.

## Review and reproducibility

Reviewers should independently check the evidence selection and interpretation, including cases labeled generic or implicit. Agree the final codebook before calculating agreement. Resolve disagreements explicitly; do not fabricate a second coder or agreement statistics.

The screening patterns and deterministic sample are stored in `audit.py`, `audit.json` and `sample.json`. Screening finds candidates, not semantic classifications. It intentionally remains simple and is vulnerable to synonyms, languages, boilerplate and ordering effects. No-hit cases are read for implicit themes. The pilot cannot establish theoretical saturation or population prevalence.
