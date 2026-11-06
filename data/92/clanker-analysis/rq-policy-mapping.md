# Mapping of OSS AI policies to SUSTAIN-OSS RQ1–RQ4

Date: 2026-11-03
Source corpus: `policies/` (92 files, GitHub HTML pages saved with `.md` names; text extracted from the embedded file content). Each file is cited by its local name and the repository given in its `og:url`.

## 0. Corpus notes

- 87 files contain a substantive AI policy. Five do not:
  - `AI_POLICY.md.47` (pydata/xarray): pointer only (`doc/contribute/ai-policy.md`).
  - `ai-policy.md`, `ai-policy.md.1` (beeware/briefcase, beeware/toga): template include only.
  - `LLM_POLICY.md.2` (scala/scala): defers to scala3.
  - `CLAUDE.md` (xonsh/xonsh): agent instructions, not a contribution policy; one relevant line is cited under RQ1.
- Duplicates or near-duplicates: ClickHouse ×2 (`.16`, `.17`); rust-analyzer ×2 (`.54`, `.55`); rich/textual (`.61`, `.62`); echo/cloudstream (`.12`, `AI-POLICY.md.1`); attrs/structlog/requests/pip (`.50`, `.32`, `.46`, `.49`); p5.js/JabRef/Debezium (`AI_USAGE_POLICY.md.3`, `.1`, `AI_USAGE_POLICY.md`); LLVM-derived PennyLane/RIOT/simdjson.
- Template lineage is visible in the texts: Ghostty → about 18 derivatives (13 with explicit attribution); uv → ripgrep → bitcoin, duckdb, regex, rust-analyzer, wemake; LLVM → PennyLane, RIOT, simdjson, difftastic; Jellyfin → Podman; Forgejo → FlorisBoard; CloudNativePG → Barman.

## 1. Summary

| RQ / H | Coverage in corpus | Strongest files |
|---|---|---|
| RQ1 / H1 (adoption, participation, knowledge, resources) | Partial. Participation shifts (drive-by, one-off, abandoned PRs) and the contributor-to-maintainer pipeline are described. Resource use beyond code: none. | RIOT, Gradle, Spock, DokuWiki, Kiali, Ghostty family, Atlantis |
| RQ2 / H2 (responsibility, trust, learning, belonging) | Strong. This is the dominant content of the corpus. H2's mechanism (reasoning must stay visible and discussable) appears directly in many texts. | Fory, PyTorch, Actual, pip, Vector, ripgrep family, AnkiDroid, PennyLane/RIOT, FreeCAD, Gradle |
| RQ3 / H3 (cross-dimension trade-offs, strong-sustainability limits) | Weak. Social/individual/technical trade-offs (review asymmetry, burnout) are stated. Environmental impact: 4 files, of which 1 substantive. Proprietary-model dependence and token cost: no provision. | FreeCAD, JabRef/p5.js/Debezium, Gradle, RIOT, PowerDNS |
| RQ4 / H4 (RAI-pattern governance, revision, legitimacy) | Partial. Evidence of reactive origin, informal pattern diffusion, context adaptation and some revision clauses. No reference to Responsible-AI patterns, no preset evaluation criteria. | Fory, Atlantis, FreeCAD, leptos, Gradle, PennyLane, Redot |

No RQ is entirely without matching content. The following sub-components have no matching provision in any file:

1. RQ1: resource use beyond code (energy, compute, token spending).
2. H3: absolute resource demand; dependence on proprietary models; rising token prices.
3. RQ4/H4: any reference to Responsible-AI pattern catalogues; any criteria by which the policy itself is assessed.
4. Problem statement item [11] (agents reusing OSS without visiting projects): no policy addresses outbound reuse of the project by agents.

## 2. RQ1 / H1 — Adoption and participation

H1 predicts more peripheral, one-off contributions and less sustained engagement.

### 2.1 Pipeline from contributor to maintainer (direct match to H1)

`ai_policy.md.2` (RIOT-OS/RIOT):
> "Prior to the advent of LLMs, open-source project maintainers would often review any and all changes sent to the project simply because posting a change for review was a sign of interest from a potential long-term contributor. While new tools enable more development, it shifts effort from the implementor to the reviewer [...]"
> "Reviewing changes from new contributors is part of growing the next generation of contributors and sustaining the project. [...] growing our contributor base and recruiting new maintainers helps sustain the project over the long term."

`AI_POLICY.md.29` (gradle/gradle):
> "Low-effort submissions—where code is generated, submitted, and abandoned—waste our limited review capacity."
> "A relationship, not a transaction. [...] We hope contributors will learn from the review process, stay engaged, and continue helping us build Gradle."

`AI_POLICY.md.57` (spockframework/spock): same wording ("Submissions that are generated, posted, and then abandoned").

`LLM_POLICY.md.1` (scala/scala3):
> "Do not open pull requests without the intention of answering code reviews and pushing it to its completion."

### 2.2 Increase of peripheral / drive-by contributions

`AI_POLICY.md.19` (dokuwiki/dokuwiki):
> "Drive-by AI contributions are not welcome. If you are a first-time contributor it is expected that you will explain your motivation [...] We want contributions to be driven by people who actually use DokuWiki and care about the project, not by people who are just looking for an easy way to get a contribution on their GitHub profile."

`AI_POLICY.md.33` (kiali/kiali), prohibited practice "Gaming the System":
> "Creating artificial contribution velocity through bulk AI-generated submissions"; "Submitting low-quality or redundant contributions to inflate metrics"; "Using AI to simulate community engagement or discussions"

`AI_POLICY.md.26` (ghostty-org/ghostty) and derivatives (`.1`, `.4`, `.27`, `.30`, `.42`, `.39`):
> "Drive-by pull requests that do not reference an accepted issue will be closed."

`AI_POLICY.md.35` (leptos-rs/leptos):
> "It is much more helpful for you to spend your time, energy, and attention filtering, reviewing, and testing AI output from 1 PR than using AI to blast out 10 drive-by PRs."

`AI_POLICY.md.52` (quarkusio/quarkus):
> "recent patterns of use have led to increased moderation burden, low-value contributions, and reduced community signal."

`AI_USAGE_POLICY.md.4` (runatlantis/atlantis), a quantitative cap:
> "To avoid maintainer overload, contributors are limited to 8 open PRs at any given time."

Also: `ai-contribution-policy.md` (Graphite: "ever-increasing flood of low-quality PRs"), `AI_POLICY.md.28` (go-git: "A flood of low-effort PRs exhausts maintainer attention"), `AI_POLICY.md.21` (Barman: "'low-effort' or 'random' contributions").

### 2.3 Core/periphery asymmetry in the rules themselves

Several policies apply rules only to outside contributors, which formalises a core/periphery split relevant to H1.

`AI_POLICY.md.26` (Ghostty) and derivatives:
> "These rules apply only to outside contributions to Ghostty. Maintainers are exempt from these rules and may use AI tools at their discretion; they've proven themselves trustworthy to apply good judgment."

`AI_POLICY.md.5` (ankidroid/Anki-Android):
> "Before you have 3 merged pull requests, you may not use any AI tools to produce contributions for AnkiDroid."

`AI_POLICY.md.24` (FreeCAD/FreeCAD):
> "PRs from outside the Developers group will be marked as 'Unverified' [...] After several successful contributions we will add new contributors to the groups"

### 2.4 Adoption by maintainers (adoption measurement)

`AI_POLICY.md.26` (Ghostty): "Ghostty is written with plenty of AI assistance". `AI_POLICY.md.44` (PostHog): "PostHog is built with plenty of AI assistance." `AI_POLICY.md.60` (tinyauth) and `AI_USAGE_POLICY.md.4` (Atlantis) list the AI tools used by maintainers (CodeRabbit, Dosu, Copilot, Claude). `AI_POLICY.md.28` (go-git): "The same disclosure and ownership expectations apply to maintainer-authored commits."

### 2.5 Disclosure as a measurement instrument (relevant to WP1 "declared" use)

`AI_POLICY.md.29` (Gradle):
> "we ask because information about AI tool use helps us evaluate their impact, build new best practices, and adjust existing processes."

`AI_Policy.md` (PennyLane) and `ai_policy.md.2` (RIOT), stating a limit:
> "Our policy on labelling is intended to facilitate reviews, and not to track which parts of [the project] are generated."

`AI_POLICY.md.64` (vectordotdev/vector):
> "We'd also love if you could like or dislike each AI comment. [...] it genuinely helps us understand whether the tool is pulling its weight."

Machine-readable traces: `Assisted-by:` trailers (CEF, Barman, go-git, FreeCAD, Kiali, AnkiDroid, PennyLane, RIOT, zrythm, Atlantis, awesome-agentic-patterns); `CLAUDE.md` (xonsh): "place them in a `test_<topic>_llm.py` file"; `AI_POLICY.md.67` (Zeek): AI-generated Pcaps must be listed in `Traces/README`; `ai_policy.md` (Chromium): prompts may be added to `//agents/prompts/eval`. Counter-case: `AI_POLICY.md.17` (ClickHouse): "You don't have to disclose your usage of AI."

### 2.6 Knowledge

`AI_POLICY.md.64` (Vector):
> "there's still no substitute for some good old-fashioned reading. Spending time in the actual source, following the logic yourself, and running things locally is what builds the real intuition you'll need to contribute confidently."

`AI_USAGE_POLICY.md.1` (JabRef), and p5.js, Debezium:
> "we ask that you only do so assistively (like a reference or tutor) and not generatively (having the tool write code for you)." / "LLMs often provide incorrect or incomplete answers, and they may create a false sense of understanding."

### 2.7 Gap

No file contains a provision on resource use beyond code (compute, energy, token budgets). "Resource" appears only as maintainer review time.

## 3. RQ2 / H2 — Responsibility, trust, learning, belonging

### 3.1 Visibility of reasoning (direct match to the H2 mechanism)

`AI_CONTRIBUTION_POLICY.md` (apache/fory):
> "The following MUST be human-authored [...]: Review responses; Design rationale and tradeoff discussion; Risk analysis and production impact explanation"

`AI_POLICY.md.51` (pytorch/pytorch):
> "Other users' comments+questions are requests for your understanding, reasoning, and judgment. Unreviewed AI output shifts the burden of verification onto the other party and can make discussions slower, noisier, or misleading."

`ai-usage-policy.md` (actualbudget/actual):
> "the conversation around a change is where most of the value of code review lives. If that conversation is between an AI on one side and a human on the other, it stops being useful."

`AI_POLICY.md.49` (pypa/pip):
> "code reviews are a social process and are not intended to catch bugs in PRs created by an LLM. If you submit a pull request, we expect you to engage with reviewers and learn from the review, not simply update the prompt that generated the PR and regenerate the code."

`AI_POLICY.md.64` (Vector):
> "GitHub discussions (issues, PR descriptions, review threads) are how our community thinks together."

`AI_POLICY.md.13` (BurntSushi/ripgrep) and derivatives (`.10`, `.15`, `.20`, `.53`, `.54`, `.55`, `.65`):
> "If you wish to include context from an interaction with AI in your comments, it must be in a quote block [...] and disclosed as such. It must be accompanied by human commentary explaining the relevance and implications of the context."

`AI_POLICY.md.41` (awesome-agentic-patterns): "You must not use AI to outsource your reasoning to reviewers". `AI_POLICY.md.22` (f3d): "Never let it think or talk for you". `AI_POLICY.md.35` (leptos): "Knowledge is cheap, wisdom is expensive." `ai-contribution-policy.md` (Graphite): "A detailed, human-written description must accompany every line of material that you did not personally write [...] It should justify why each line is correct".

Making the private model exchange public: `LLM_POLICY.md.1` (scala3): "If LLM-based tools were used extensively in a contribution, attaching prompt history in a comment is considered a useful aid for code reviewers." `ai_policy.md` (Chromium): "If a single prompt to a tool [...] was used to create the CL then the prompt may be included in the CL description."

Counter-positions: `AI_POLICY.md.64` (Vector): "if a response is thoughtful and on point, does it matter whether a human wrote every word? We don't think so." `AI_CONTRIBUTION_POLICY.md` (Fory): "Contributors are NOT required to disclose model names, provider names, private prompts, or internal workflow details."

### 3.2 Responsibility

`AI_POLICY.md.13` (ripgrep):
> "the project maintainers remain responsible for any code that is published as part of a release. Contributors are expected to be responsible for any code they publish."

`AI_POLICY.md.21` (Barman): "You are responsible for the long-term maintenance of that code." / "'The AI generated it' is never an acceptable answer to a reviewer's question."

`AI_POLICY.md.19` (DokuWiki): "Each commit must have a responsible human author attached. Refrain from 'co-authored-by' or similar tags that attribute the contribution to an AI."

`AI_POLICY.md.68` (zrythm): "AI agents MUST NOT add `Signed-off-by` tags. Only humans can legally certify the Developer Certificate of Origin."

`ai_policy.md` (Chromium): "Any account that sends for review CLs which are not actually understood by the human behind the account is at risk of losing their committer status."

`AI_USAGE_POLICY.md.1` (JabRef): "Large language models (LLMs) make mistakes and cannot be held accountable for their outputs."

Attribution conflict: `AI_POLICY.md.50`/`.32`/`.46`/`.49` (attrs family) forbid LLM co-author tags; `AI_USAGE_POLICY.md.4` (Atlantis) accepts `Co-authored-by: Claude`.

### 3.3 Trust

`AI_POLICY.md.28` (go-git): "Disclosure is not a penalty — it is trust infrastructure."
`AI_POLICY.md.3` (ag2ai/ag2): "we just need to be able to trust that a human stands behind it."
`AI_POLICY.md.57` (Spock): "The value of a contribution lies not only in the code it delivers, but in the understanding shared and the trust built along the way."
`AI_POLICY.md.36` (letta): automated checks, with exemption for "trusted contributors".
`AI_POLICY.md.39` (Loop): "we may try to verify that you are a human contributor through specific questions."
`AI_POLICY.md.7` (avian): "Exhibiting multiple clear signs of LLM output is a red flag, but please do not start witch hunts."

### 3.4 Learning and mentoring

`AI_POLICY.md.5` (AnkiDroid):
> "AI generated contributions are nullifying our mentorship efforts by consuming guidance meant for humans and shifting the responsibility of ensuring correctness onto our code reviewers." / "Ensure mentors are mentoring people, not AI output."

`AI_Policy.md` (PennyLane), `AI_USAGE_POLICY.md.5` (simdjson), `ai_policy.md.2` (RIOT):
> "Passing maintainer feedback to an LLM doesn't help anyone grow, and does not sustain our community."

`AI_POLICY.md.50` (attrs) and derivatives: "This dynamic is especially pernicious because it poisons the well for mentoring new contributors which we are committed to."

Good-first-issue reservation: `AI_POLICY.md.30` (Hatchet: "intended for new contributors to learn the codebase, and are thus wasted if AI solves them"), `AI_POLICY.md.58` (Starship), `AI_Policy.md` (PennyLane: "squanders the learning opportunity"), `ai_policy.md.2` (RIOT), `AI_POLICY.md.19` (DokuWiki), `AI_POLICY.md.41` (awesome-agentic-patterns).

`AI_USAGE_POLICY.md.3` (p5.js), JabRef, Debezium: "learning to code and contributing to open source are deeply human endeavors that requires curiosity, slowness, and community."

### 3.5 Belonging

`AI_POLICY.md.24` (FreeCAD): "With each contribution we value the interaction with the contributor and the community building as much as the improvement to FreeCAD." / "This policy acknowledges the harmful sides of AI with respect to communities".
`AI_POLICY.md.29` (Gradle): "The value of a contribution is not only in the code it delivers, but in the knowledge shared and the community relationships built along the way."
`AI_POLICY.md.7` (avian): "This is a human community, and we do not tolerate or wish to interact with raw LLM output."
`AI_POLICY.md.26` (Ghostty): "It is a boundary point at which people interact with each other and the work done."
`ai-policy.md.2` (ESLint), economic dimension of belonging: "ESLint does not provide compensation [...] for contributions created primarily by AI."

## 4. RQ3 / H3 — Trade-offs and non-negotiable limits

### 4.1 Environmental dimension

`AI_POLICY.md.24` (FreeCAD) is the only file with a substantive environmental provision:
> "environmental: land use, carbon footprint, and water use for cooling of large data centers"
> "privilege: only large organizations can effectively train and operate high-performance LLMs, limited accessibility to the technology for the unprivileged [...]"
> "FreeCAD as a project wants to raise awareness of alternatives to the large LLMs that can only be trained by large organizations. Examples are frugal AI initiatives and fully open source AI models such as Apertus that is trained on fully open data in a carbon-neutral and water-neutral data center."

The provision is awareness-raising; it contains no requirement. FreeCAD states: "many of these concerns are outside of the influence of the FreeCAD project".

`AI_USAGE_POLICY.md.1` (JabRef), `AI_USAGE_POLICY.md.3` (p5.js), `AI_USAGE_POLICY.md` (Debezium), mention only:
> "There are also ethical and legal considerations around authorship, licensing, and environmental impact."

`AI_POLICY.md.35` (leptos): "serious concerns about the ethics and the effects of generative AI", without specification.

### 4.2 Productivity versus other dimensions (social, individual, technical)

`AI_POLICY.md.29` (Gradle):
> "There is a fundamental asymmetry between submitting a contribution and reviewing one: AI tools make it easy to generate and submit large amounts of code, but they do not make it equally faster for us to review it."

`AI_POLICY.md.49` (pip): "LLM generated content is generally easier for you to produce, but harder for others to read, review or interpret. Prioritising your time over that of others is contrary to the project's code of conduct."

`AI_POLICY.md.50` (attrs family): "Having to wade through plausible-looking-but-low-quality pull requests [...] is extremely demoralizing and has already burned out many good maintainers." / "poisoning the open source ecosystem that was precarious even before the arrival of LLM tools."

`AI_Policy.md` (PennyLane), `ai_policy.md.2` (RIOT): "Our golden rule is that a contribution should be worth more to the project than the time it takes to review it." (an explicit cost/benefit criterion). `AI_POLICY.md.14` (CEF): "Contributions should provide more value to the project than the review effort they require."

`AI_POLICY.md.42` (Polars): "Poor usage of AI can generate tremendous amounts of low-quality code and 'slop' PRs, which can have a net-negative effect on the maintenance of Polars."

PennyLane and RIOT cite the METR study on experienced OSS developer productivity as a justification.

### 4.3 Non-negotiable limits (language of strong sustainability, applied to non-ecological capital)

`AI_POLICY.md.21` (Barman): "This makes human understanding and accountability non-negotiable."
`AI_POLICY.md.28` (go-git): "Correctness, compatibility with the reference Git implementation, and long-term maintainability are non-negotiable properties of the project."
`LLM_POLICY.md.1` (scala3): "The following rules are non-negotiable".
`AI_POLICY.md.45` (PowerDNS), a hard limit on the legal dimension: "The use of AI tools for code contributions is not allowed. The rationale behind this is that there is no way to know whether the AI has been trained on code compatible with the GPL version 2 licence".
`AI_POLICY.md.50` (attrs family): "We cannot risk the copyright status of this project."

### 4.4 Dependence on providers

No provision addresses dependence on proprietary models, token prices, or cost of access. The only provider-related clauses are legal: `AI_POLICY.md.21` (Barman: "does not violate the terms of service of the AI provider"), `AI_POLICY.md.28` (go-git), `AI_POLICY.md.33` (Kiali), `AI_USAGE_POLICY.md.4` (Atlantis), `AI_POLICY.md.68` (zrythm: "AI tool terms must not restrict output usage"). `AI_USAGE_POLICY.md.1` (JabRef) recommends "AI tools trained on JabRef data, such as DeepWiki", a tool-choice recommendation. FreeCAD's "privilege" item (4.1) is the only statement about concentration of model ownership.

### 4.5 Gap relative to H3

No file links productivity gains to absolute resource demand, and no file states a trade-off that productivity assessments would miss. H3 has no direct match.

## 5. RQ4 / H4 — Governance framework, revision, legitimacy

### 5.1 Reactive origin (premise of H4)

`AI_POLICY.md.42` (Polars): "We have established these rules [...] because we have experienced an increasing number of low-quality pull requests".
`AI_POLICY.md.26` (Ghostty): "until either the people get better, the AI gets better, or both, we have to have strict rules to protect maintainers."
`AI_POLICY.md.9` (Beyond-All-Reason): "The restrictions outlined above exist due to repeated misuse of AI".
`ai-contribution-policy.md` (Graphite): "it has become necessary to set some strict rules against low-effort PRs."

### 5.2 Explicit choice among configurations

`AI_POLICY.md.35` (leptos) states three options and the reason for the choice:
> "1. Ban all outside contributions and issues 2. Ban AI-generated contributions and issues (and spend time and energy trying to identify them) 3. Allow contributions of any kind, with clear guidelines" / "I don't think it's productive to incentivize secrecy around whether AI tools were used or not."

`AI_POLICY.md.2` (Redot): "We do not believe [...] that a blanket ban on generative AI is productive or remotely enforceable."

`AI_POLICY.md.24` (FreeCAD), values-based framing closest to an envelope: "This document outlines the core project values regarding the technology and acts as the compass that should guide us in decisions concerning AI."

### 5.3 Context adaptation

`AI_POLICY.md.21` (Barman): "Backup tooling has a unique risk profile: incorrect behavior may go undetected until a disaster recovery scenario".
`AI_CONTRIBUTION_POLICY.md` (Fory): additional required checks for protocol and performance-critical paths.
`AI_POLICY.md.40` (nasa/fprime): "Human judgment on safety-critical decisions".
`AI_POLICY.md.54` (rust-analyzer): "Due to the foundational nature of our projects, we require a human in the loop".
`AI_POLICY.md.34` (Kornia): implementations "must be based on an existing library reference".

Negative evidence of adaptation: `AI_POLICY.md.1` (Pennyw0rth/NetExec) still reads "The Ghostty project has strict rules for AI usage" and "These rules apply only to outside contributions to Ghostty", i.e. the template was adopted without adaptation.

### 5.4 Revision mechanisms

`AI_USAGE_POLICY.md.4` (Atlantis):
> "This policy will be reviewed and updated as needed to reflect: Changes in AI tooling [...]; Legal or regulatory developments; Maintainer and reviewer experience together with community feedback; Evolution of CNCF and industry best practices"

`AI_POLICY.md.10` (bitcoin): "Questions or proposed changes to this policy can be discussed in bitcoin-core/meta."
`AI_POLICY.md.6` (pre-commit-terraform): "This policy is intentionally minimal and open to refinement."
`AI_POLICY.md.2` (Redot): "This policy may be updated over time as AI tooling, legal guidance, and community standards evolve."
`AI_USAGE_POLICY.md.1` (JabRef): "may have to change our policies as AI tools evolve. We welcome feedback".
Versioning or dating: Kornia (`.34`, v1.0), awesome-agentic-patterns (`.41`, v1.0, adopted 2026-03-11), Azahar (`AI-POLICY.md`, effective 20 March 2026), PowerDNS (`.45`, last update 15 September 2025).

### 5.5 Legitimacy and process

`AI_CONTRIBUTION_POLICY.md` (Fory):
> "Any long-term contribution restrictions MUST follow Apache project governance and community process, and SHOULD be documented with clear rationale."

Alignment with external frameworks: Kiali (`.33`), go-git (`.28`), Barman (`.21`), Atlantis (`AI_USAGE_POLICY.md.4`) reference Linux Foundation / CNCF guidance. Fory (`AI_CONTRIBUTION_POLICY.md`) and OpenVINO (`AI_USAGE_POLICY.md.2`) give precedence to existing project or foundation governance in case of conflict.

### 5.6 Affordability of enforcement

`AI_USAGE_POLICY.md.2` (openvino): "This policy is not based on AI detection. Enforcement is based on observed contribution quality, reviewer confidence, and adherence to project rules."
`AI_Policy.md` (PennyLane): canned response and an `extractive` label "to help other reviewers prioritize their review time."
`AI_POLICY.md.7` (avian): "No LLM-generated commits [...] This is automatically enforced by a CI check."
`AI_POLICY.md.36` (letta): non-compliant issues "automatically closed and locked".
`AI_USAGE_POLICY.md.1` (JabRef): `AGENTS.md` instructs agents "to act more like guides than code generators", with the stated limit "Agents may ignore it".
`AI_POLICY.md.34` (Kornia): enforcement delegated to AI reviewers via `.github/copilot-instructions.md`.

### 5.7 Gap relative to H4

No file references Responsible-AI pattern catalogues, defines criteria for assessing the policy itself, or evaluates its effects. Atlantis (5.4) and Gradle ("adjust existing processes") are the closest to a revision loop driven by observation.
