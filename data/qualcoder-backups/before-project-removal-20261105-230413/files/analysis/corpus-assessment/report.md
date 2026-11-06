# Sustainability in the full policy corpus: first-pass assessment

**The corpus can support RQ2 and RQ3, especially an analysis of how AI contribution rules protect human and community capacity. RQ1 needs a separate, consistently reviewed purpose-document collection. The coded evidence does not justify a weak/strong sustainability classification for RQ4.**

This extends the pilot to **all 281 dataset entries**, without sampling by origin. It supplies one case record per entry, **619 exact excerpts**, an inventory of **330 local and supplementary policy/guideline documents**, and **313 supplementary-source retrieval records**. The original CSV's 281 rows and original 32 columns' cell values are preserved. Every entity now has supplementary-source records in the existing `supplementary_material` column.

These are **provisional AI-assisted first-pass annotations**, not an independently validated thematic analysis. Positive interpretations are traceable to text. A case without a positive code is **evidence not established in this pass**, not evidence that the project ignores or rejects sustainability. Purpose-source discovery and passage selection are partly automated; the report does not claim every project website has been exhaustively read.

Start with the [case table](cases.csv), [readable evidence ledger](evidence.md), [evidence CSV](evidence.csv), [coding rules](codebook.md), and [machine-readable counts](summary.json).

## What changed from the pilot

- Included the user's manually retrieved Forgejo policy and contribution guidelines. Their unknown retrieval dates and the unknown contributing-file URL remain unknown; they are not filled from file timestamps or guesses.
- Retrieved official purpose-source candidates across the full dataset, usually a README at the same commit as the policy. Supplemented organization entries with official about/mission pages. Access dates, moving references, commit references, redirects and snapshot hashes are retained.
- Recovered Linux Kernel and PROJ RST files, followed the moved Godot rules page, followed Servo's actual AI-policy link, resolved four local path-only documents, and followed NLnet's explicit HTML refresh to policy version 2.0. The local inputs are preserved.
- Kept failed retrieval attempts alongside successful replacements. Of 313 source records, 308 are successful downloads and five are failed attempts. These are retrieval counts, not counts of unique usable policies. Some downloaded pages are empty or render badly.

**Following references changed the substantive picture.** Servo's dataset document was a contribution guide linking to a separate AI policy. That recovered policy explicitly names energy/water concerns, worker exploitation and reviewer capacity ([C0083–C0085](evidence.md#c0083)). NLnet's local policy file was only a newline: its downloaded HTML contained a refresh redirect rather than the actual policy. Version 2.0 supplies financial rules and a concern about long-term social lock-in ([C0080–C0081](evidence.md#c0080)). A blank extraction could otherwise have become a false negative.

## RQ1: sustainability in stated project purpose

Four reviewed purpose/principles documents explicitly use sustainability language: **W3C, Tauri, Nura/postmarketOS and OpenInfra Foundation**. Seventeen entries have provisionally interpreted dimensions in their purpose/values passages. For example, OpenList explicitly describes resilient long-term governance ([C0196](evidence.md#c0196)); the Python source is the **PSF's** community-oriented mission, whose organization-level scope must remain visible.

The other case statuses are 16 pilot purpose descriptions without an established sustainability commitment, 243 entries with a retrieved source/passage candidate but no affirmative purpose-level code, and one insufficient-purpose case: Halo's retrieved README is predominantly Chinese, outside the protocol's English/French inclusion rule. No translated purpose is invented.

**These are coverage and evidence-assignment categories, not a yes/no distribution of OSS purposes.** A functional description, sponsor appeal, installation instruction or operational energy-saving tip does not by itself establish a project's raison d'être. Automatically selected passages remain visibly labeled candidates in the ledger. Their semantic relevance needs checking before RQ1 can be treated as a completed corpus-wide finding. Several organizations' official mission pages also differ in level from a particular project's README.

Funding and organizational survival are useful context even when they are not purpose statements: Astropy's about page links administrative/fiscal support to sustainability; attrs asks for more sustainable maintenance; scikit-learn discusses grants and sustainability. Those passages are retained as support context and are not automatically counted as explicit sustainability in project purpose.

**What RQ1 can currently support:** documented positive examples and a concrete collection/review procedure. **What it cannot yet support:** the general claim in H1 that sustainability is part of the purpose of OSS projects, or a reliable prevalence estimate from these source candidates.

## RQ2: sustainability in AI policies

| First-pass category | Dataset entries | Interpretation |
| --- | ---: | --- |
| Explicit environmental concern | 7 | W3C, p5.js, EFF, FreeCAD, SFC, Servo and Nura/postmarketOS name environmental concerns. |
| Other explicit sustainability wording in AI-related rules | 5 | Scala, SunPy, Vector, whisper.cpp and Scalar frame long-term use, maintenance or reviews as sustainable. |
| Concrete implicit concerns, provisionally mapped to sustainability | 97 | The text identifies human capacity, learning, trust, community continuity, maintainability or other specific concerns. |
| Relevant general context without an established AI-specific sustainability rationale | 4 | Ratatui, PEFT, Wave Terminal and AnythingLLM. |
| No sustainability-specific code established | 168 | AI scope or rules are present, but this pass assigns no affirmative sustainability code. **This is not a finding of absence.** |
| **Total** | **281** | Counts describe this dataset and these coding decisions. |

The first three categories supply affirmative candidate evidence in **109 entries**. Generic testing, disclosure, human responsibility and licensing requirements alone are not sufficient for a sustainability code. The categories are mutually exclusive for case summaries; an individual document may contain several different concerns.

The common rationale is a mismatch between cheap generated submissions and scarce human review. Linux Kernel guidance explicitly calls reviewer bandwidth scarce ([C0082](evidence.md#c0082)); Godot states a goal of reducing review burden while preserving maintainability ([C0157–C0158](evidence.md#c0157)). This gives RQ2 something more precise to study than searching for the word “sustainability.”

**Implication for H2:** “no, or partially” must be operationalized. Separate explicit sustainability framing, explicit environmental acknowledgment, implicit dimension-related concerns and actual measures. Do not collapse 168 uncoded cases into a claim that sustainability is absent.

## RQ3: definitions and characteristics

The evidence more readily supports **concerns, protected resources and governance mechanisms** than formal definitions of sustainability.

| Candidate dimension in AI-related text | Entries with recorded evidence |
| --- | ---: |
| Individual | 94 |
| Social | 42 |
| Technical | 22 |
| Environmental | 7 |
| Economic | 2 |

These counts overlap. They are counts of recorded candidate annotations per entity, not independent policies, exhaustive thematic frequencies or agreement-validated results. General repository guidance and purpose-only evidence are excluded from this table.

Useful lines of analysis include:

- **Capacity protection:** finite reviewer attention, moderation effort, validation work and backlog. Most examples name workload; that does not prove burnout. Unlike workload-only passages, La Suite Docs and pi-mono explicitly mention burnout ([C0096](evidence.md#c0096), [C0159](evidence.md#c0159)).
- **Community renewal:** protecting beginner issues, learning opportunities and paths towards future maintenance. This connects individual skill development with continued community participation; it is more than code correctness.
- **Technical continuity:** explicit long-run support, maintainability and contributor ownership after the initial merge. Generic tests or performance claims receive no automatic sustainability interpretation.
- **Environmental acknowledgment versus action:** documents vary from a brief environmental concern to recommendations or prohibitions. A policy's environmental assertions are reported as its claims, not independently verified scientific facts or measured outcomes.
- **Economic evidence:** Nura/postmarketOS explicitly names self-hosting costs; NLnet excludes AI expenses from grant reimbursement. Other “cost” phrases can mean time or maintenance effort. They are not automatically monetary evidence. CAMEL's maintenance-cost statement therefore receives a technical candidate code without an economic code.

**Implication for H3:** human capacity is prominent among the recorded evidence, but community learning, trust and renewal need a substantial social code family. The current annotations do not establish that technical and individual sustainability dominate all OSS policy discourse. Shared policy language and uneven depth of coding affect apparent frequency.

## RQ4: strong sustainability

All 281 case records retain **insufficient evidence** for weak/strong classification. This means no such classification is justified by the evidence assigned here; it is **not** a claim that a strong framework cannot exist elsewhere or that all policies endorse weak sustainability.

A corpus-wide literal scan found no matches for critical natural capital, natural capital, non-substitutability, weak/strong sustainability, planetary boundaries or ecological ceilings/limits. That search is only a diagnostic: a framework could be expressed without those exact terms. Environmental passages and the W3C-referenced Ethical Web Principles were also considered in the pilot and remain in the ledger.

The distinction matters. An AI ban, a resource-efficiency recommendation, a neutrality claim or no-further-harm language does not, by itself, establish preservation of critical natural capital or non-substitutability. Conversely, silence does not establish the substitution position required for a weak-sustainability classification.

**Implication for H4:** an information gap does not confirm “no.” A defensible text-based question is whether policies articulate commitments consistent with strong sustainability. Whether those commitments actually *lead to* strong-sustainability outcomes needs evidence beyond policy text.

## Data quality, scope and practical limits

The current local corpus contains **308 files and 302 unique byte contents**. Five pairs of nonempty files are byte-identical; a sixth duplicate pair consists only of blank files. A blank pair is an extraction problem, not evidence of policy diffusion. Many other documents adapt common policy families, but near-duplicates have not been exhaustively clustered. Count project applicability separately from independent policy formulations.

The combined policy inventory has 321 documents with available text, four empty extracts, four path-only stubs and one page with a rendering problem. These quality flags remain even when a usable replacement is available. The Google Docs reference in the KDE entry could be downloaded but renders as a browser/error page; it is not used as substantive policy evidence. No translated supplementary policy is constructed from the translator note in another row.

Corpus entries mix software projects, foundations, standards guidance, company-wide LLM-use advice and program-specific rules. In particular:

- W3C's Group Note explicitly lacks endorsement by W3C itself and its Members. It is Advisory Board guidance.
- SFC supplies cross-project recommendations; NLnet supplies grant conditions; KDE's policy is GSoC-specific; Oxide's RFD covers company work, not exclusively OSS contributions.
- Diesel points readers to NLnet for explanation; this does not automatically apply every NLnet grant restriction to every Diesel contribution.
- The Python purpose source is a PSF mission. Its connection to a particular software project requires explicit scope handling.
- Scala 2 adopts Scala 3's policy by reference. Nura's official about page documents continuity with the dataset label postmarketOS.

Retrieved web sources are from 5 November 2026. Pinned repository references are retained where available; unversioned webpages and moving branches may differ in time from original extracts. Original collection dates and full adoption histories are not inferred. The report does not establish theoretical saturation, policy compliance, actual sustainability effects, a second coder or inter-rater agreement.

## What to do before treating this as the formal review

1. Adjudicate inclusion and units for foundations, company guidance, program rules and adopted policy chains.
2. Independently review the case table and coded passages, plus uncoded and screening-negative material. Unselected search hits are not automatically rejected as irrelevant.
3. Validate purpose-passage selection systematically. Use a defined mission/about/README search order and record when available material is not a purpose statement.
4. Agree the distinction between concern, definition and measure, and the boundaries of individual, social, economic and technical codes. Retain uncertainty rather than force weak/strong labels.
5. Expand the evidence collection only where those checks identify missing sources. Keep supplementary-source records in the original CSV and leave original metadata unchanged.

`protocol.md` has not been modified. The results establish a documented whole-dataset starting point and concrete evidence for refining the research design, while keeping unsupported conclusions out of the findings.

## Reproduce and validate

From the repository root:

```sh
python3 analysis/corpus-assessment/prepare.py
python3 analysis/corpus-assessment/build_results.py
python3 analysis/corpus-assessment/validate.py
```

Preparation inventories documents and extracts candidate paragraphs. Positive judgments come from [annotations.py](annotations.py) and explicitly retained pilot evidence, not from keyword matches. [candidate-review.csv](candidate-review.csv) records which hits support annotations and which are not used as positive evidence. A hit's non-selection is not a semantic finding of absence.

The builder creates case and evidence tables, freezes the quoted documents, and merges source records into the CSV without changing original cells. The validator is read-only and checks row/column preservation, case/evidence references, literal excerpts and line ranges, snapshot hashes and all source attachments. `collect_sources.py` resumes official downloads when network access is available; it does not overwrite the original extracted documents. The pilot directory remains a historical artifact and should not be regenerated against the updated Forgejo inputs.
