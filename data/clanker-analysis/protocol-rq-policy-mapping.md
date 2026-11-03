# Mapping of OSS AI policies to the ICT4S 2027 protocol RQ1–RQ4

Date: 2026-11-03
Research questions: `protocol.md` ("Sustainability in the AI Policies of Open Source Projects: A Grey Literature Review").
Corpus: `policies/` (92 files; 87 substantive policies, after excluding the pointer or template-only files xarray `AI_POLICY.md.47`, beeware `ai-policy.md` and `ai-policy.md.1`, scala2 `LLM_POLICY.md.2`, and the agent-instruction file xonsh `CLAUDE.md`). Verbatim forks are listed in the companion report `rq-policy-mapping.md`, section 0. Under the protocol's exclusion rule they are counted once. Counts below are given in files and are indicative, not the output of the double-coded procedure.

Coding: Karlskrona dimensions (individual, social, economic, environmental, technical) plus one inductive code, **legal**, which recurs in the corpus and has no Karlskrona counterpart.

## 1. Summary

| RQ | Hypothesis | Observation on this corpus | Verdict |
|---|---|---|---|
| RQ1: sustainability in the stated purpose of projects | H1: yes, or partially | The corpus contains no README, mission statement or charter. Some policies include purpose-like statements; one of them (FreeCAD) links purpose and sustainability. | Not testable with this corpus |
| RQ2: sustainability in AI policies | H2: no, or only partially | 7 of 87 policies use the word "sustain(able)". About 4 mention the environment, 1 substantively. Sustainability concerns without the term (maintainability, burnout, mentoring) are widespread. | H2 supported ("partially") |
| RQ3: dimensions and definitions addressed | H3: mostly technical and individual, centred on the maintainer | Individual, technical and economic codes (maintainer workload, review budget, code quality) dominate. The social dimension (mentoring, community, trust) is also frequent. Environmental: about 4 files. Legal (copyright, licence, DCO): frequent. | H3 supported, with a strong social component |
| RQ4: frameworks leading to strong sustainability | H4: no | No policy treats critical natural capital. Threshold ("non-negotiable") language exists, but only for technical and legal properties. The cost/benefit rules found are compensatory (weak) logic. | H4 supported |

## 2. RQ1: sustainability in the stated purpose

The corpus holds AI policies only, so RQ1 cannot be answered from it: the protocol requires README, mission statements, manifestos and charters. The following policies contain purpose-like statements, which may serve as pilot codes:

- `AI_POLICY.md.24` (FreeCAD/FreeCAD): "FreeCAD is a community driven project, and would not exist without the people who helped to shape it" / "FreeCAD is made by humans and for humans, and we believe that it is important for it to stay like that." The same document "raises awareness of fully open and frugal AI". This is the only file where purpose and sustainability are linked.
- `AI_POLICY.md.60` (tinyauthapp/tinyauth): "Tinyauth is developed by humans, for humans".
- `AI_POLICY.md.41` (nibzard/awesome-agentic-patterns): "This repository is community-first, pattern-first, and non-promotional."
- `AI_POLICY.md.52` (quarkusio/quarkus): "keeping Quarkus collaborative, human-driven, and focused on quality."
- `AI_POLICY.md.21` (EnterpriseDB/barman): "trusted by organizations of all sizes for over 15 years".
- `AI_CONTRIBUTION_POLICY.md` (apache/fory): "a performance-critical foundational serialization framework".
- `AI_POLICY.md.33` (kiali/kiali): "committed to maintaining high standards of code quality, community engagement, and open source principles".

Testing RQ1 requires collecting the README files of the repositories listed in `dataset2-dedicated-ai-policies.csv`.

## 3. RQ2: is sustainability addressed in AI policies?

### 3.1 Explicit use of "sustain(able)" (7 files)

- `AI_POLICY.md.28` (go-git): "keeps provenance clear for the project's long-term health"; "the CNCF community's evolving norms on sustainable AI-assisted open source development."
- `AI_POLICY.md.64` (vectordotdev/vector): "It's about keeping contributions high-quality and reviews sustainable for a small team".
- `AI_POLICY.md.9` (Beyond-All-Reason): "ensure that collaboration remains productive and sustainable."
- `LLM_POLICY.md.1` (scala/scala3): "We want to ensure this potential is used responsibly and remains sustainable in the long term."
- `AI_Policy.md` (PennyLane): "Passing maintainer feedback to an LLM doesn't help anyone grow, and does not sustain our community." / "those who are doing the work of sustaining the project."
- `AI_USAGE_POLICY.md.5` (simdjson): "does not sustain our community."
- `ai_policy.md.2` (RIOT-OS/RIOT): "Reviewing changes from new contributors is part of growing the next generation of contributors and sustaining the project. [...] recruiting new maintainers helps sustain the project over the long term."

None of these files defines the term. In every case "sustainable" refers to the project or community, never to the environment.

### 3.2 Sustainability concerns without the term (implicit sustainability)

These cases fall under the protocol's threat "Implicit sustainability".

- Long-term maintainability: `AI_USAGE_POLICY.md.2` (openvino: "ensure long-term maintainability of the project"), `AI_POLICY.md.21` (Barman: "You are responsible for the long-term maintenance of that code"), `AI_CONTRIBUTION_POLICY.md` (Fory: "a quality and maintainability gate"), `AI_POLICY.md.38` (modelcontextprotocol: "generating code or changes that cannot be reasonably maintained or evolved").
- Ecosystem health: `AI_POLICY.md.31` (huggingface/lerobot: "a healthy open-source ecosystem"), `AI_POLICY.md.50`/`.32`/`.46`/`.49` (attrs family: "poisoning the open source ecosystem that was precarious even before the arrival of LLM tools"), `AI_POLICY.md.52` (Quarkus: "a healthy and productive community"), `AI_POLICY.md.33` (Kiali: section "Community and Project Health").

### 3.3 Policies with no sustainability content

Short disclosure-only policies have no sustainability content in any dimension: `AI_POLICY.md.61`/`.62` (Textualize rich/textual), `AI_POLICY.md.8` (toad), `AI_POLICY.md.66` (difftastic), `AI_POLICY.md.68` (zrythm, legal only), `AI-POLICY.md` (Azahar, legal only), `AI_POLICY.md.16`/`.17` (ClickHouse).

## 4. RQ3: which dimensions and definitions?

### 4.1 Individual (maintainer wellbeing; contributor competence)

Maintainer-centred (the H3 core):
- `AI_POLICY.md.50` (attrs) and derivatives: "extremely demoralizing and has already burned out many good maintainers."
- `AI_POLICY.md.21` (Barman): "To protect the quality of the project and the sanity of its maintainers".
- `AI_POLICY.md.26` (Ghostty) and about 18 derivatives: "we have to have strict rules to protect maintainers."
- `AI_POLICY.md.25` (arcane): "maintainers who volunteer their time"; `AI_POLICY.md.58` (starship): "This project is maintained by volunteers. This policy exists to keep review burden reasonable."

Contributor-centred (learning):
- `AI_POLICY.md.5` (AnkiDroid): "Ensure contributors can contribute without AI assistance."
- `AI_POLICY.md.30` (Hatchet), `AI_POLICY.md.58` (Starship), `AI_Policy.md` (PennyLane), `ai_policy.md.2` (RIOT), `AI_POLICY.md.19` (DokuWiki): "good first issue" reserved for human learning.
- `AI_USAGE_POLICY.md.3` (p5.js), `.1` (JabRef), `AI_USAGE_POLICY.md` (Debezium): "LLMs often provide incorrect or incomplete answers, and they may create a false sense of understanding."
- `AI_POLICY.md.64` (Vector): "Spending time in the actual source [...] is what builds the real intuition".

### 4.2 Technical

- `AI_POLICY.md.28` (go-git): "Correctness, compatibility with the reference Git implementation, and long-term maintainability are non-negotiable properties of the project."
- `AI_CONTRIBUTION_POLICY.md` (Fory): additional checks for protocol and performance-critical paths.
- `AI_POLICY.md.34` (kornia): "You must use existing `kornia` utilities and never reinvent the wheel".
- `AI_POLICY.md.35` (leptos): "Every change is a possible bug. [...] There is no value in churn for the sake of churn".
- `LLM_POLICY.md` (podman): "Podman has always prioritized code quality (readability, simplicity, and conciseness)".
- `AI_POLICY.md.16`/`.17` (ClickHouse): "Prefer using AI for improving the code base, such as removing and simplifying code, improving the build speed".

### 4.3 Economic (scarce review capacity treated as a budget; compensation)

- `AI_POLICY.md.29` (gradle): "This policy protects our limited review budget, allowing us to invest our attention wisely."
- `AI_Policy.md` (PennyLane), `ai_policy.md.2` (RIOT): "Our golden rule is that a contribution should be worth more to the project than the time it takes to review it."; definition of "extractive contributions" quoting Eghbal: "the marginal cost of reviewing and merging that contribution is greater than the marginal benefit to the project's producers."
- `AI_POLICY.md.14` (CEF): "Contributions should provide more value to the project than the review effort they require."
- `AI_USAGE_POLICY.md.4` (Atlantis): "contributors are limited to 8 open PRs at any given time."
- `ai-policy.md.2` (eslint): "ESLint does not provide compensation [...] for contributions created primarily by AI."

### 4.4 Social (community, mentoring, trust, human communication)

- `AI_POLICY.md.24` (FreeCAD): "we value the interaction with the contributor and the community building as much as the improvement to FreeCAD"; "societal: exploiting workers for content moderation, affecting the learning process".
- `AI_POLICY.md.5` (AnkiDroid): "Ensure mentors are mentoring people, not AI output."
- `AI_POLICY.md.29` (Gradle): "The value of a contribution is not only in the code it delivers, but in the knowledge shared and the community relationships built along the way."
- `ai-usage-policy.md` (actualbudget/actual): "the conversation around a change is where most of the value of code review lives."
- `AI_POLICY.md.7` (avian): "This is a human community".
- `AI_USAGE_POLICY.md.3` (p5.js) and derivatives: "learning to code and contributing to open source are deeply human endeavors that requires curiosity, slowness, and community."
- `AI_POLICY.md.24` (FreeCAD), equity: "privilege: only large organizations can effectively train and operate high-performance LLMs, limited accessibility to the technology for the unprivileged".

### 4.5 Environmental (about 4 files)

- `AI_POLICY.md.24` (FreeCAD), substantive: "environmental: land use, carbon footprint, and water use for cooling of large data centers"; "raise awareness of alternatives [...] frugal AI initiatives and fully open source AI models such as Apertus that is trained on fully open data in a carbon-neutral and water-neutral data center." The concern carries no obligation: "many of these concerns are outside of the influence of the FreeCAD project".
- `AI_USAGE_POLICY.md.1` (JabRef), `AI_USAGE_POLICY.md.3` (p5.js), `AI_USAGE_POLICY.md` (Debezium), mention only: "There are also ethical and legal considerations around authorship, licensing, and environmental impact."

### 4.6 Inductive code: legal

Present in a large share of the corpus: copyright, licence compatibility, provenance, DCO. Representative passages:
- `AI_POLICY.md.45` (PowerDNS): code contributions using AI are banned because "there is no way to know whether the AI has been trained on code compatible with the GPL version 2 licence".
- `AI_POLICY.md.50` (attrs): "We cannot risk the copyright status of this project."
- `AI_POLICY.md.68` (zrythm): "Only humans can legally certify the Developer Certificate of Origin".

### 4.7 Reading against H3

- H3 is supported: the dominant concern is maintainer workload and code quality (individual + technical), expressed as review cost (economic).
- The social dimension is more frequent than H3 states: mentoring, the contributor pipeline and human communication form a recurring theme, mostly in LLVM-, attrs- and p5.js-derived texts.
- Environmental concern is marginal: about 4 of 87 files, and 1 with content.
- The legal dimension is frequent and is not covered by the Karlskrona grid, so the coding scheme should include it as an inductive code.

## 5. RQ4: do these definitions lead to strong sustainability?

### 5.1 No treatment of critical natural capital

No policy sets an ecological limit, a resource budget, or an obligation tied to environmental impact. The only environmental provision (FreeCAD) is informative, and its proposed remedy rests on neutrality claims ("carbon-neutral and water-neutral"). That is a compensation logic, not a preserved-capital threshold.

### 5.2 Threshold logic exists, but for non-natural capital

- `AI_POLICY.md.28` (go-git): "non-negotiable properties" (correctness, compatibility, maintainability).
- `AI_POLICY.md.21` (Barman): "This makes human understanding and accountability non-negotiable."
- `LLM_POLICY.md.1` (scala3): "The following rules are non-negotiable".
- `AI_POLICY.md.45` (PowerDNS): outright ban on AI-generated code (legal capital).

Each of these statements is structurally a strong-sustainability rule (some capital cannot be traded), but each applies to technical, human or legal capital, never to natural capital.

### 5.3 Compensatory (weak) logic is explicit

- PennyLane and RIOT ("worth more to the project than the time it takes to review it") and CEF ("more value [...] than the review effort") define acceptability as a net balance between benefit and maintainer cost. This logic is substitutable and compensatory.

### 5.4 Interdependencies between dimensions

A few policies state a link between dimensions, all between productivity (technical/economic) and maintainer capacity (individual/social):
- `AI_POLICY.md.29` (Gradle): "There is a fundamental asymmetry [...] AI tools make it easy to generate and submit large amounts of code, but they do not make it equally faster for us to review it."
- `ai_policy.md.2` (RIOT): "While new tools enable more development, it shifts effort from the implementor to the reviewer".
- `AI_POLICY.md.49` (pip): "LLM generated content is generally easier for you to produce, but harder for others to read, review or interpret."

FreeCAD lists five concern areas (privilege, environmental, copyright, societal, open source projects) but does not relate them. No policy relates any dimension to the environmental one.

### 5.5 Verdict

H4 is supported: no policy provides a framework that leads to strong sustainability as the protocol defines it (critical natural capital must be preserved).

## 6. Implications for the protocol

1. RQ1 requires a separate collection of purpose statements; the current `policies/` folder cannot answer it.
2. The coding scheme needs an inductive **legal** code. It may also need a distinction between **maintainer-individual** and **contributor-individual** (learning) codes, because both are frequent and serve different arguments under H3.
3. The strong/weak classification should record threshold rules on non-natural capital (section 5.2) separately, otherwise they will be coded as "strong" by structure.
4. Applying the protocol's verbatim-fork exclusion rule substantially reduces the effective corpus size, because of the Ghostty, uv/ripgrep, LLVM, attrs and p5.js lineages.
