# Whole-corpus first-pass coding rules

This extends the [pilot codebook](../feasibility-pilot/codebook.md). Those operational definitions remain the starting point. This is a provisional AI-assisted assessment with no independent human coder or agreement statistics.

## Units, scope and evidence

- The case unit is each of the 281 dataset entities. An entity is not necessarily a software project: it can be a foundation, company or specific contribution program.
- The evidence unit is a literal passage, with its original path, line range, content hash, source URL where known and a frozen copy. No missing statement, retrieval date, authority or intention is invented.
- The file roles `ai_policy`, `contributing`, `agent` and `other_policy` are download-slot labels. Their actual scope must be read from the document.
- General contribution guidance, product-feature requirements, purpose statements and AI-specific rules remain separate scopes. A symlink/path stub, empty file or browser challenge is not a policy.
- An entity may have several applicable policy documents. Shared text and adoption-by-reference are not independent observations of policy creation.

## RQ1: purpose status

| Case status | Meaning |
| --- | --- |
| `explicit_sustainability` | A reviewed purpose/principles passage explicitly frames sustainability. This can concern organizational continuity rather than the environment. |
| `interpreted_dimension` | A reviewed stated purpose/value supports a provisional dimension mapping, explained in its evidence record. |
| `purpose_only` | Retained pilot passage describes purpose without establishing sustainability. It is not a project-wide negative finding. |
| `source_available_no_positive_purpose_code` | An official source/passage candidate is available; this first pass assigns no affirmative purpose-level sustainability code. Automatic candidate selection still needs semantic review. |
| `insufficient_purpose_evidence` | No meaningful eligible purpose passage established. Do not infer or silently translate a purpose. |

Functional descriptions, funding appeals, installation guidance, news and operational recommendations must not automatically become mission evidence. The purpose-source procedure is not yet an exhaustive crawl of every project's website. Organization-level missions must retain their level when attached to a project-related dataset row.

## RQ2: AI-related sustainability evidence

Use the first applicable case status:

1. `explicit_environmental_concern`: AI-related text explicitly names environmental concerns.
2. `explicit_sustainability_ai`: other explicit sustainability wording appears in AI-related rules/rationale.
3. `implicit_concern_ai`: recorded passages name specific concerns provisionally mapped to dimensions.
4. `general_context_only`: relevant evidence is general guidance rather than an established AI-specific sustainability rationale.
5. `no_sustainability_specific_code_established`: AI scope/rules are present, but no positive sustainability interpretation is assigned here.
6. `insufficient_policy_evidence`: substantive AI-policy scope cannot be established from usable material.

These are case-summary categories, not a binary classifier of whether a project cares about sustainability. A scope excerpt confirms AI-related material exists; it does not turn generic accountability, quality or licensing into sustainability evidence.

## RQ3: candidate dimensions

| Dimension | Required textual basis | Boundary |
| --- | --- | --- |
| Individual | Attention, workload, fatigue, skill development, learning or explicit privacy/autonomy values. | Workload alone does not establish burnout. |
| Social | Community continuity, participation, fairness, trust, labor conditions or stated freedoms. | A social-network product category alone does not qualify. |
| Technical | Maintainability, long-run support, resilience or infrastructure continuity. | Tests, speed and correctness alone are insufficient. Maintenance checks are weaker candidates than an explicit longevity rationale. |
| Environmental | Explicit environmental effects or physical-resource concerns. | A maintainer's “energy” or efficient code alone is not environmental evidence. |
| Economic | Financial costs, reimbursement, funding or livelihoods explicitly supported by text. | Time/value metaphors and maintenance “costs” without monetary context are not automatically financial. |

Multiple dimensions may apply. Every mapping remains provisional and must state its basis. Distinguish concerns, rules/measures and rationales from formal definitions/frameworks. AI-specific counts exclude purpose-only and general-guideline evidence.

## RQ4: strength and uncertainty

Use the protocol's capital/substitutability definitions. Weak or strong classification requires direct supporting passages and an explicit rationale. Neither an AI ban nor environmental awareness proves strong sustainability; missing information does not prove weak sustainability. `insufficient_evidence` means no classification is established by this pass, not that a framework cannot exist elsewhere.

Literal framework-term screening is diagnostic only. It cannot establish semantic absence or practical sustainability outcomes.

## Automation and independent review

`prepare.py` extracts candidate paragraphs using headings and thematic patterns. `annotations.py` contains the affirmative analytical choices. The builder also retains applicable pilot annotations and creates visibly marked source/scope candidates. Keyword hits never become positive dimension codes automatically.

All 281 entries receive a case record; not every sentence receives exhaustive semantic adjudication. Candidate non-selection means “not used as positive evidence,” not “reviewed and proven irrelevant.” Source availability and passage selection must not be reported as a completed purpose-level thematic review.

Before publication, independent reviewers should check positive codes and screening-negative/uncoded material, validate source scope and purpose selection, resolve uncertain mappings, and then calculate agreement if appropriate. No second-coder results, adoption history, saturation or missing evidence are fabricated.
