# Can these policies support the protocol's research questions?

**Yes, particularly RQ2 and RQ3. RQ1 requires supplementary purpose documents, and RQ4 currently supports an assessment of textual evidence rather than a justified weak/strong classification.** This pilot supplies concrete examples and identifies methodological decisions needed before a formal review. It does not test the hypotheses or estimate prevalence across OSS.

The findings below come from a provisional AI-assisted analytical pass, not independent human coding. Every excerpt and interpretation is available in the [evidence ledger](evidence.md), its [CSV equivalent](evidence.csv), and the [24 case assessments](cases.csv). Missing information has not been filled with assumptions.

## Corpus, sampling and source quality

The local audit found **281 dataset entries, 307 documents and 278 entities with at least one downloaded document**. Document types are 66 `ai_policy.md`, 204 `contributing.md`, 29 `other_policy.md` and eight `agent.md`. These names describe download slots, not necessarily the source's actual document type. See the [inventory](inventory.csv) and [audit details](audit.json).

The audit identifies six pairs of byte-identical documents: 301 unique file contents among 307 files. For example, the Apache Kafka supplementary policy duplicates the Apache Software Foundation document, and the uv and Ruff supplementary policies duplicate each other. Count a shared policy text separately from the number of projects to which it applies. The full audit lists every pair; near-duplicates were not systematically clustered.

Ten populated source slots lack corresponding local files. One of these contains a translator's note rather than a retrievable URL, and some others contain multiple URLs or explanatory text. They therefore do not represent ten independently verified missing policies. Linux Kernel, PROJ and Godot have no downloaded documents. The download Makefile rejects unsupported non-Markdown/non-HTML formats and assumes source cells contain a single URL; the absent slots require individual investigation rather than a conclusion that no policy exists. The source CSV also contains repeated `doc excerpt` column names; processing here preserves columns positionally.

Whole-corpus screening found six entities with environmental-term hits and seven with other sustainability-word hits. The pilot includes all 13, the first eight no-hit entities, and the next three remaining entries in CSV order to reach **24 entities and 28 local documents**. Dataset origin was not used. Screening expressions and exact selection are reproducible in [audit.py](audit.py) and [sample.json](sample.json). These are search results, not counts of sustainability-aware policies across the dataset. Sampling deliberately favors positive examples and depends on CSV order.

The 24 cases cover W3C, p5.js, EFF, FreeCAD, Software Freedom Conservancy, postmarketOS, Scala, SunPy, Vector, Tauri, whisper.cpp, Wave Terminal, Scalar, Ratatui, Leptos, Keycloak, Storybook, Bitcoin Core, Mastodon, rust-analyzer, Forgejo, PostHog, Nix and Nextcloud. Close reading focused on AI-related sections and their rationales, with general guidance and webpage boilerplate kept separate. Purpose review focused on introductory purpose, mission and principles passages; it was not an exhaustive search of every project webpage.

Official source collection on **5 November 2026** produced 56 retrieval records: 55 downloads and one bot challenge. One successful download is only a redirect notice; it supplies no substantive purpose evidence. Raw responses, converted text, access timestamps, versions where available, resolved URLs and hashes are retained in [source-manifest.json](source-manifest.json) and `sources/`. All 56 records, including unsuccessful substantive retrievals, are attached to the corresponding existing dataset rows in the new `supplementary_material` column. The 281 entries and their original 32 columns' cell values are preserved. Unselected entities have `[]` in the new column.

Important source distinctions:

- **Forgejo:** the local file contains a bot challenge, not a policy ([E050](evidence.md#e050)). The official raw endpoint supplies a policy with an explicit legal rationale ([E051](evidence.md#e051)). No conclusion is drawn from the bot page.
- **postmarketOS/Nura:** the supplied URL resolves to Nura documentation, and the supplementary about page explicitly states that Nura was called postmarketOS until 27 September 2026. Preserve the dataset's original label and document this continuity rather than inventing a project mismatch or silently renaming the row. The first about-page response was a redirect notice; its linked wiki page supplies the substantive text. See sources `06-ai_policy`, `06-purpose` and `06-purpose-followup` in the manifest.
- **W3C:** the document says it is endorsed by the Advisory Board, but not W3C itself or its Members ([E003](evidence.md#e003)). Treat it as advisory standards-work guidance rather than a binding OSS contribution policy.
- **EFF and SFC:** EFF's dataset document is a blog explanation linking to actual contribution rules; these rules were collected separately. SFC's document is cross-project recommendations. Neither should be silently counted as an individual project's merged repository policy.
- **Scala and whisper.cpp:** Scala 2 adopts Scala 3's policy by reference; whisper.cpp's detailed rules originate in `AGENTS.md`, saved locally as `other_policy.md`. Follow document roles and adoption links rather than filenames.

Pinned GitHub sources match the local text byte-for-byte in the checked pilot cases. Unversioned HTML sources are not byte-identical after different conversions; that alone establishes no substantive change. The original local extraction date was not recorded. A repository snapshot proves the text at that commit, but this pilot does not independently establish adoption history, author authority or a formal grey-literature quality score for every case.

## RQ1: sustainability in the stated purpose of projects

**Feasible with supplementary material; the policy collection alone is insufficient for a systematic answer.** Three reviewed purpose/principles documents explicitly use sustainability language:

- W3C's mission links sustainable technology development to economic growth, social well-being and environmental protection ([E056](evidence.md#e056)).
- Tauri's README states an aim to be a sustainable collective ([E065](evidence.md#e065)).
- The Nura/postmarketOS about page includes a sustainable-and-maintainable principle, explained through code, packages and upstreaming ([E061](evidence.md#e061)). This is not, by itself, evidence of an environmental mission.

Five other selected purpose passages provide candidate dimensional evidence without explicitly defining sustainability: p5.js prioritizes accessibility and community ([E057](evidence.md#e057)); EFF names freedom and justice ([E058](evidence.md#e058)); SFC names rights to repair and modify software ([E060](evidence.md#e060)); Vector lists cost reduction ([E064](evidence.md#e064)); Forgejo names an inclusive community ([E076](evidence.md#e076)). These remain analytical mappings, not statements that those projects call their missions sustainable.

The remaining 16 selected purpose passages describe functionality without establishing sustainability commitments. This means **not found in the reviewed purpose passages**, not “the project has no sustainability purpose.” For example, SunPy's solar-physics focus does not itself imply environmental sustainability, and Bitcoin Core's purpose cannot be supplemented with assumptions about its energy impacts.

Mastodon's AI policy also contains a purpose-like statement about authentic human connection ([E048](evidence.md#e048)). That is useful evidence of a connection between values and policy, but its location must remain explicit. Conversely, Scala's README includes later CI energy-saving advice; this is operational guidance, not automatically its stated purpose.

**Implication for H1:** positive examples exist, but the pilot does not establish that sustainability is generally part of OSS purpose. Define what qualifies as a purpose statement and distinguish explicit sustainability from interpreted dimensions before testing this hypothesis.

## RQ2: sustainability in AI policies

**Feasible, provided explicit language and implicit concerns are analyzed separately.** The mutually exclusive pilot categories are:

| Reviewed AI-text category | Entities, out of 24 | Meaning |
| --- | ---: | --- |
| Explicit environmental concern | 6 | W3C, p5.js, EFF, FreeCAD, SFC and Nura/postmarketOS acknowledge environmental concerns. |
| Other explicit sustainability language in AI rules | 5 | Scala, SunPy, Vector, whisper.cpp and Scalar explicitly frame long-term use, maintenance or reviews as sustainable. |
| Concrete AI-related concerns, interpreted as sustainability | 9 | Tauri, Leptos, Keycloak, Storybook, Bitcoin Core, Mastodon, rust-analyzer, PostHog and Nextcloud name relevant concerns without sustainability wording. |
| Relevant general context, without an established AI-specific sustainability rationale | 1 | Wave Terminal. |
| Generic quality, accountability or legal rules without an established sustainability-specific rationale | 3 | Ratatui, Forgejo and Nix. |

These categories are defined in the [codebook](codebook.md). They are descriptions of this purposive sample and do not imply that the remaining cases lack sustainability concerns elsewhere.

Vector directly frames review sustainability around a small team's capacity ([E028](evidence.md#e028)); SunPy links transparency to trust and sustainable maintenance ([E026](evidence.md#e026)); whisper.cpp links sustainable management to avoiding overload ([E032](evidence.md#e032)). FreeCAD explicitly names land, carbon and water impacts ([E010](evidence.md#e010)). These examples are enough to show that a keyword-only finding of “sustainability absent” would be unsafe.

Scope matters. Tauri's explicit sustainability sentence concerns ordinary issue reporting, while its AI subsection separately addresses unfair review-time costs ([E030–E031](evidence.md#e030)). Wave's sustainability statement closes general contribution guidance ([E034–E036](evidence.md#e034)). Neither should become an explicit AI-policy sustainability statement merely because it appears in the same file.

**Implication for H2:** the proposed “no, or partially” hypothesis needs a stated meaning of “partially.” Separate explicit framing, concrete implicit concerns and operational measures; this pilot cannot estimate how common each is.

## RQ3: definitions and characteristics of sustainability

**Feasible for concerns, dimensions and mechanisms; less clearly feasible for formal definitions.** Most recorded passages describe things to protect or rules to follow rather than define sustainability itself.

| Candidate dimension in reviewed AI-related text | Pilot entities with recorded evidence | Examples |
| --- | ---: | --- |
| Individual | 17 | Reviewer attention, workload and contributor learning. |
| Social | 12 | Community effectiveness, fairness, human connection, labor conditions and newcomer participation. |
| Technical | 7 | Maintainability, continued support, infrastructure complexity and future breakage. |
| Environmental | 6 | Climate, land, water and energy concerns. |
| Economic | 1 | Explicit self-hosting costs in Nura/postmarketOS. |

Counts overlap and are based on the provisional passages recorded in the ledger, not a validated exhaustive coding. They exclude purpose-only and general-guideline evidence, and include Mastodon's purpose-like statement because it is part of the AI-policy rationale. Screening intentionally selected environmental cases, so these numbers cannot establish their relative frequency in the wider corpus.

There is more than code quality here. rust-analyzer protects newcomer learning opportunities ([E049](evidence.md#e049)); Nextcloud explicitly connects learning paths to future maintainers ([E054](evidence.md#e054)); SFC discusses skill atrophy and resilient, maintainable software ([E015–E016](evidence.md#e015)); FreeCAD names worker exploitation ([E011](evidence.md#e011)). These provide possible links between individual development, community continuity and technical maintenance.

Avoid inflating dimensions: a licensing restriction is not automatically economic sustainability, a request to test code is not automatically technical sustainability, and a statement about workload does not prove burnout. Nura/postmarketOS explicitly discusses self-hosting costs ([E020](evidence.md#e020)); the pilot's time/value statements elsewhere do not establish monetary effects.

**Implication for H3:** the examples justify investigating individual and technical concerns, but social concerns also deserve a substantial place. Retain separate codes for learning, community renewal, reviewer capacity and maintainability. Do not turn a pilot with deliberately selected cases into support for the hypothesis that these dimensions dominate generally.

## RQ4: frameworks leading to strong sustainability

**The pilot identifies framework indicators, but does not justify a weak/strong classification for any of the 24 cases.** All cases are marked **insufficient evidence**, rather than weak sustainability. No explicit framework of critical natural capital and non-substitutability was established in the reviewed policy text.

The environmental cases vary meaningfully:

- FreeCAD raises awareness of frugal and open alternatives, including a claimed carbon-/water-neutral example ([E013](evidence.md#e013)). This establishes neither verified neutrality nor an ecological ceiling.
- Nura/postmarketOS refuses to perpetuate the harms it lists ([E021](evidence.md#e021)). This is an explicit normative rationale; an AI ban alone does not establish strong sustainability.
- SFC acknowledges environmental impacts but defers environmental expertise outside its main software-freedom focus ([E017](evidence.md#e017)).
- W3C recommends smaller models ([E004](evidence.md#e004)) and references Ethical Web Principles. That framework includes a no-further-environmental-harm commitment ([E080](evidence.md#e080)). This is a stronger normative indicator than a bare impact mention, but the reviewed material does not establish the protocol's specific non-substitutability framework.

**Implication for H4:** insufficient information is not confirmation of “no.” A text-only study can ask whether documents articulate commitments consistent with strong sustainability. Whether they actually *lead to* strong-sustainability outcomes would require evidence beyond these policies.

## Recommended protocol clarifications and next steps

1. Define explicit sustainability, interpreted sustainability concerns, and no evidence found as separate outcomes. A clear concern is not necessarily a definition, and missing evidence is not a negative position.
2. Keep purpose statements and AI-policy rationales distinct, while allowing an explicitly labeled embedded purpose statement such as Mastodon's. Use a consistent purpose-source search procedure before comparing projects.
3. Decide whether foundation recommendations and standards-work notes belong in the main sample or a contextual comparison. Their scope and authority differ from repository contribution rules.
4. Use project/entity, policy text and passage as separate units. Track adoption-by-reference and duplicates so shared text does not masquerade as independent policy creation.
5. Add “insufficient evidence” to RQ4's classification and distinguish textual commitments from outcomes. Consider asking: “What commitments, if any, are consistent with strong sustainability?”
6. Independently review the pilot evidence and code boundaries, especially generic quality rules, economic coding, and social/individual overlap. No second-coder review or agreement statistic has been performed.
7. Repair the missing/invalid downloads, freeze source versions and dates, then expand coding beyond this pilot. Document language/translation handling and assess grey-literature authority and quality. Do not claim saturation from these 24 cases.

The original `protocol.md` is unchanged. The practical result is a usable starting corpus for RQ2/RQ3, a demonstrated need for purpose-source collection for RQ1, and a concrete reason to make uncertainty and textual evidence central to RQ4.

## Reproducing and checking the artifacts

Run from the repository root:

```sh
python3 analysis/feasibility-pilot/audit.py
python3 analysis/feasibility-pilot/build_results.py
```

The first command regenerates inventory and selection. The second validates literal excerpts and line ranges, snapshot hashes, all supplementary-source attachments, and preservation of the original 32 columns and 281 entries. It rebuilds the annotated tables and idempotently updates only the supplementary column. The [summary](summary.json) contains the reported counts. Both scripts check the fixed original-cell hash in `baseline.json`; they fail if the original dataset cells have changed since this pilot was frozen.

To collect sources again, `collect_sources.py` requires network access and Pandoc. It resumes saved downloads without replacing them, retries unavailable sources, and retains unusable bot responses as such. The source record's `used_as_evidence` flag means a direct ledger quotation; other records can still serve source verification or document an unsuccessful substantive retrieval. Hashes preserve this pilot's snapshots; they are not proof of an external archival deposit.
