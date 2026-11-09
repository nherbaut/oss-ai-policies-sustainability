"""Build the evidence tables, attach sources to the dataset, and validate provenance.

Annotations below are provisional analyst judgments, not automatic classifications.
Run after audit.py and collect_sources.py. No network access is needed.
"""
import csv
import hashlib
import json
from collections import Counter
from pathlib import Path

HERE = Path(__file__).resolve().parent
ROOT = HERE.parents[1]
DATASET = ROOT / 'data/281/dataset1-multiple-ai-policies.csv'
SAMPLE = json.loads((HERE / 'sample.json').read_text())
SOURCES = json.loads((HERE / 'source-manifest.json').read_text())
SOURCE_BY_ID = {s['id']: s for s in SOURCES}
EVIDENCE = []


def add(number, document, excerpt, rqs, dimensions, basis, rationale, scope='AI policy', uncertainty='Provisional single-analyst interpretation; independent review required.'):
    entity = SAMPLE[number - 1]['entity']
    if document.startswith('@'):
        source = SOURCE_BY_ID[document[1:]]
        assert source['entity'] == entity and source['status'] == 'downloaded'
        path = source['snapshot']; url = source['url']; source_id = source['id']
        version = source.get('version') or 'Unversioned webpage; see retrieval timestamp and snapshot hash'
    else:
        path = f'data/281/policies/{entity}/{document}.md'
        source = SOURCE_BY_ID.get(f'{number:02d}-{document}')
        url = source['url'] if source else ''
        source_id = 'local-snapshot'
        version = (source.get('version') if source else None) or 'Local extraction date not recorded'
    content = (ROOT / path).read_text()
    assert excerpt in content, f'Excerpt not found: {entity}, {document}, {excerpt!r}'
    start = content.index(excerpt)
    EVIDENCE.append({
        'evidence_id': f'E{len(EVIDENCE) + 1:03d}', 'entity': entity,
        'rqs': ';'.join(rqs), 'scope': scope, 'basis': basis,
        'dimensions': ';'.join(dimensions), 'excerpt': excerpt,
        'source_path': path, 'line_start': content[:start].count('\n') + 1,
        'line_end': content[:start + len(excerpt)].count('\n') + 1,
        'source_url': url, 'source_id': source_id, 'version': version,
        'rationale': rationale, 'uncertainty': uncertainty,
    })


def annotations():
    # Local documents are the primary evidence for policy coding.
    add(1, 'ai_policy', 'Lastly, there is a climate impact. Production and usage of LLMs has a\nclimate footprint (including energy and water use)', ['RQ2', 'RQ3'], ['environmental'], 'explicit_concern', 'Names climate, energy and water impacts; no impact magnitude is independently validated.')
    add(1, 'ai_policy', 'more text that is less intentional and less meaningful. This can result\nin “second-hand burdening” that can thwart our community’s\neffectiveness.', ['RQ3'], ['social'], 'interpreted_dimension', 'Connects generated communication to community effectiveness.')
    add(1, 'ai_policy', 'This Group Note is endorsed by the [Advisory\nBoard](https://www.w3.org/groups/other/ab), but is not endorsed by\n<span class="abbr" title="World Wide Web Consortium">W3C</span> itself\nnor its Members.', ['RQ2'], [], 'document_status', 'Advisory Board guidance, not a W3C-wide binding contribution policy.', uncertainty='Explicit document status.')
    add(1, 'ai_policy', '**Prefer smaller and more task-specific models over large and\n  general-purpose models**: smaller models usually use less energy.', ['RQ3', 'RQ4'], ['environmental'], 'explicit_measure', 'Efficiency-oriented recommendation; no ecological ceiling or non-substitutability requirement is stated in this passage.')
    add(2, 'ai_policy', 'There are also ethical and legal considerations around authorship, licensing, and environmental impact.', ['RQ2', 'RQ3'], ['environmental'], 'explicit_concern', 'Environmental impact is acknowledged without definition or operational environmental requirement.')
    add(2, 'ai_policy', 'We believe that learning to code and contributing to open source are deeply human endeavors that requires curiosity, slowness, and community.', ['RQ3'], ['individual', 'social'], 'interpreted_dimension', 'Protects learning and community participation; dimensions are analytical labels, not definitions supplied by the policy.')
    add(3, 'ai_policy', 'makes LLM-generated code exhausting to review, especially with smaller,\nless resourced teams.', ['RQ2', 'RQ3'], ['individual'], 'interpreted_dimension', 'States review exhaustion and limited team resources; this is a blog explanation linking to the actual contribution rules.')
    add(3, 'ai_policy', '[climatic](https://www.technologyreview.com/2025/05/20/1116327/ai-energy-usage-climate-footprint-big-tech/)\nconcerns for many.', ['RQ2', 'RQ3'], ['environmental'], 'explicit_concern', 'Explicit climate concern in the article body, not the unrelated news/sidebar content.')
    add(3, '@03-contribution-rules', 'that experience is not being built.', ['RQ3'], ['individual', 'social'], 'interpreted_dimension', 'In the AI policy section, this refers to lost contributor experience when AI writes code and interacts with reviewers.', scope='Supplementary contribution policy', uncertainty='Interpretation depends on the immediately preceding sentence; see source section Policy Regarding AI-Assisted Contributions.')
    add(4, 'ai_policy', '- **environmental:** land use, carbon footprint, and water use for cooling of large data centers', ['RQ2', 'RQ3'], ['environmental'], 'explicit_concern', 'Specifies land, carbon and water impacts.')
    add(4, 'ai_policy', '- **societal:** exploiting workers for content moderation, affecting the learning process', ['RQ3'], ['social', 'individual'], 'interpreted_dimension', 'Names worker exploitation and learning impacts; these support social and individual codes.')
    add(4, 'ai_policy', 'We want to help the contributor improve their skills and learn how their input can cause real change.', ['RQ3'], ['individual'], 'explicit_measure', 'States a contributor development goal.')
    add(4, 'ai_policy', 'Examples are frugal AI initiatives and fully open source AI models such as Apertus that is trained on fully open data in a carbon-neutral and water-neutral data center.', ['RQ3', 'RQ4'], ['environmental'], 'explicit_measure', 'Raises awareness of alternatives; does not establish ecological limits or verify the claimed neutrality.')
    add(5, 'ai_policy', 'including\n    the environmental impact of the development and use of these\n    systems.', ['RQ2', 'RQ3'], ['environmental'], 'explicit_concern', 'Acknowledges environmental impact in recommendations for FOSS, not a binding rule for every project.')
    add(5, 'ai_policy', '**Do not overuse LLM-gen-AI, or allow your skills to atrophy**.', ['RQ3'], ['individual'], 'explicit_measure', 'Directly addresses skill preservation.')
    add(5, 'ai_policy', 'FOSS processes yield\n    software systems that are resilient, highly maintainable, and\n    contributor-friendly.', ['RQ3'], ['technical', 'social'], 'interpreted_dimension', 'Links contribution processes to maintainability and contributor experience.')
    add(5, 'ai_policy', 'On matters\n    unrelated to software freedom, we defer to experts that focus on\n    environmental and other intersectional issues.', ['RQ4'], [], 'explicit_scope_limit', 'Acknowledges environmental expertise outside the document’s focus; does not supply a strong-sustainability framework.')
    add(6, 'ai_policy', 'They require an unreasonable\namount of energy[^1] and water[^2] to build and operate', ['RQ2', 'RQ3'], ['environmental'], 'explicit_concern', 'Policy claims excessive energy and water use; the pilot does not independently validate that claim.')
    add(6, 'ai_policy', 'their models\nare built in part with heavily exploited workers in unacceptable working\nconditions', ['RQ3'], ['social'], 'explicit_concern', 'Policy states labor exploitation concerns.')
    add(6, 'ai_policy', 'increase cost and\ncomplexity of self-hosting for everybody', ['RQ3'], ['economic', 'technical'], 'interpreted_dimension', 'Explicit costs and infrastructure complexity support economic and technical candidate codes; no financial measurement is provided.')
    add(6, 'ai_policy', 'These are harms\nthat we do not want to perpetuate, even if only indirectly.', ['RQ3', 'RQ4'], ['environmental', 'social'], 'explicit_rationale', 'Refusal of the preceding harms informs the ban, but the reviewed text does not define critical natural capital or non-substitutability.')
    add(6, 'ai_policy', 'We forbid the use of generative AI tools in Nura.', ['RQ2'], [], 'document_scope', 'The dataset label is postmarketOS; the document itself names Nura. The supplementary about page explicitly connects the names.', uncertainty='Project-name continuity is documented online; original extraction date remains unknown.')
    add(7, 'other_policy', 'We want to ensure this potential is used responsibly and remains sustainable in the long term.', ['RQ2', 'RQ3'], [], 'explicit_sustainability', 'Explicit long-term framing without a formal sustainability definition.')
    add(7, 'other_policy', 'preserving code correctness while\nkeeping the maintainers’ workload manageable.', ['RQ3'], ['technical', 'individual'], 'interpreted_dimension', 'Places code quality and maintainer workload alongside explicit long-term framing; workload is not evidence of burnout.')
    add(7, 'other_policy', 'We also care about maintainability,', ['RQ3'], ['technical'], 'explicit_concern', 'Names maintainability rather than correctness alone.')
    add(8, 'ai_policy', 'Transparency supports trust, effective collaboration, and\nsustainable maintenance.', ['RQ2', 'RQ3'], ['social', 'technical'], 'explicit_sustainability', 'Connects transparency to trust, collaboration and maintenance.')
    add(8, 'ai_policy', 'respect the time, expertise, and long-term responsibilities of both\ncontributors and maintainers.', ['RQ3'], ['individual'], 'interpreted_dimension', 'Recognizes finite time and long-term maintenance responsibilities.')
    add(9, 'ai_policy', "It's about keeping contributions high-quality and reviews sustainable for a small team maintaining a popular open source project that receives a lot of PRs.", ['RQ2', 'RQ3'], ['individual'], 'explicit_sustainability', 'Explicitly frames reviewer capacity as a sustainability concern.')
    add(9, 'ai_policy', 'Spending time in the actual source, following the logic yourself, and running things locally is what builds the real intuition you\'ll need to contribute confidently.', ['RQ3'], ['individual'], 'interpreted_dimension', 'Addresses contributor learning and skill development.')
    add(10, 'contributing', 'diagnosing issues without clear reproduction steps is extremely time-consuming and simply not sustainable.', ['RQ2'], [], 'explicit_general_guidance', 'This is in Issue Reporting Guidelines, outside AI Tool Policy; do not count it as explicit sustainability in AI rules.', scope='General contribution guidance')
    add(10, 'contributing', 'It is unfair for other contributors and the reviewers to spend much of the time dealing with this, hence these rules:', ['RQ2', 'RQ3'], ['individual', 'social'], 'interpreted_dimension', 'Within AI Tool Policy, explicitly identifies time costs and fairness; sustainability is an interpretation here.')
    add(11, 'other_policy', 'This policy exists to ensure that maintainers can sustainably manage the project without being overwhelmed by low-quality submissions.', ['RQ2', 'RQ3'], ['individual'], 'explicit_sustainability', 'Directly connects sustainability and maintainer overload.')
    add(11, 'other_policy', '**A pull request represents a long-term commitment.** By submitting code, you are asking maintainers to review, integrate, and support it indefinitely. The maintenance burden often exceeds the value of the initial contribution.', ['RQ3'], ['individual', 'technical'], 'interpreted_dimension', 'Explicitly describes maintenance after initial acceptance and a burden/value trade-off; this is not measured economic valuation.')
    add(12, 'contributing', 'Review bandwidth is limited.', ['RQ2', 'RQ3'], ['individual'], 'interpreted_dimension', 'General contribution context about solo-maintainer capacity; not an AI-specific sustainability statement.', scope='General contribution guidance')
    add(12, 'contributing', 'AI-assisted contributions are welcome, but PRs must reflect clear understanding of context, existing patterns, and project direction.', ['RQ2'], [], 'generic_quality_rule', 'An AI rule is present, but the general sustainability closing sentence cannot establish an explicit AI-specific sustainability rationale.')
    add(12, 'contributing', 'Clear expectations help keep the project moving quickly and sustainably.', ['RQ2'], [], 'explicit_general_guidance', 'General closing statement, not a separate AI sustainability requirement.', scope='General contribution guidance')
    add(13, 'contributing', 'To keep reviews healthy and sustainable:', ['RQ2', 'RQ3'], ['individual'], 'explicit_sustainability', 'Within AI assisted coding, explicitly frames review sustainability.')
    add(13, 'contributing', 'Add tests for regressions, issues, and new features. If it is not tested, it will likely break soon.', ['RQ3'], ['technical'], 'interpreted_dimension', 'Within the sustainability-framed AI subsection, explicitly links testing to future breakage.')
    add(14, 'contributing', '**Quality**: AI-generated content should meet the same quality standards as human-written content.', ['RQ2'], [], 'generic_quality_rule', 'Quality rule alone is insufficient to establish a sustainability definition or long-term commitment.')
    add(14, 'contributing', 'We prioritize maintaining backwards compatibility and minimizing disruption to users:', ['RQ3'], ['technical'], 'interpreted_dimension', 'Clear technical continuity concern in general guidelines, outside the AI subsection.', scope='General contribution guidance')
    add(15, 'ai_policy', 'the primary bottleneck in this, and any other mature project, is the need for a responsible human being to read and think through the huge volumes of code and text being directed at it.', ['RQ2', 'RQ3'], ['individual'], 'interpreted_dimension', 'Makes finite human attention a concrete policy rationale without using the word sustainability.')
    add(15, 'ai_policy', '**Every change is a possible bug.**', ['RQ3'], [], 'generic_quality_rule', 'Risk of defects is stated; no independent technical-sustainability code is assigned from this sentence alone.')
    add(16, 'contributing', "The goal is to keep Keycloak's code consistent and high-quality while respecting reviewers' limited time.", ['RQ2', 'RQ3'], ['individual'], 'interpreted_dimension', 'AI subsection explicitly addresses limited reviewer time.')
    add(17, 'contributing', "These measures help reduce maintenance burden and keep the team's work efficient.", ['RQ2', 'RQ3'], ['individual'], 'interpreted_dimension', 'AI subsection links moderation rules to maintenance burden.')
    add(18, 'ai_policy', "adds value, and does not waste the community's time.", ['RQ2', 'RQ3'], ['social'], 'interpreted_dimension', 'Collective time and value are policy concerns; no formal sustainability definition is provided.')
    add(19, 'other_policy', 'It is important that the software has a high standard of quality and maintainability, with careful thought given to changes that affect production deployments.', ['RQ2', 'RQ3'], ['technical'], 'interpreted_dimension', 'Explicit maintainability and deployed-system continuity support a technical code.')
    add(19, 'other_policy', 'There are a small number of people on the Mastodon core team, and we seek to use our time and resources effectively.', ['RQ3'], ['individual'], 'interpreted_dimension', 'Explicit finite team resources.')
    add(19, 'other_policy', 'Our project is fundamentally about authentic human connection and communication.', ['RQ1', 'RQ3'], ['social'], 'interpreted_dimension', 'A purpose-like statement inside an AI policy connects project values and policy rationale; corroborating purpose sources are still needed.', scope='Project-purpose statement embedded in AI policy')
    add(20, 'ai_policy', 'this provides an opportunity for newcomers to learn the codebase. Using AI to author the code for you annihilates this benefit.', ['RQ2', 'RQ3'], ['individual', 'social'], 'interpreted_dimension', 'Protects learning opportunities for newcomers; community reproduction is an interpretation, not the wording of a formal definition.')
    add(21, 'ai_policy', 'Cookie monster!', ['RQ2'], [], 'unusable_extraction', 'Local document is a bot challenge; no policy conclusion is drawn from it.', scope='Extraction artifact', uncertainty='Unusable as policy evidence.')
    add(21, '@21-policy-raw', 'due to legal uncertainties.', ['RQ2'], [], 'explicit_legal_rationale', 'Recovered official policy names a legal rationale. Legal caution is not automatically economic or strong sustainability.', scope='Supplementary governance policy', uncertainty='Retrieved from a moving main branch; original extraction date and version unknown.')
    add(22, 'ai_policy', 'low-quality, AI-generated contributions that waste maintainer time.', ['RQ2', 'RQ3'], ['individual'], 'interpreted_dimension', 'Concrete reviewer-time rationale without sustainability terminology.')
    add(23, 'contributing', 'Everyone who submits a contribution to Nix is responsible for it, regardless of the use of automated tooling.', ['RQ2'], [], 'generic_accountability_rule', 'Accountability is explicit; no sustainability-specific rationale is inferred from this rule alone.')
    add(24, 'other_policy', 'These issues exist to create a learning path for new contributors who will become future maintainers.', ['RQ2', 'RQ3'], ['individual', 'social'], 'interpreted_dimension', 'Explicitly links newcomer learning to future maintenance capacity.')
    add(24, 'other_policy', 'A contribution that costs reviewers more time than it returns value to the project is extractive and will be closed,', ['RQ3'], ['individual'], 'interpreted_dimension', 'Time/value trade-off is explicit, but is not itself a monetary or natural-capital substitution claim.')
    # Purpose excerpts are selected from actual purpose/principles passages.
    purpose = [
        (1, '01-purpose', 'technology needs to be developed sustainably, striving for balance between economic growth, social well-being and environmental protections.', ['environmental', 'social', 'economic'], 'explicit_sustainability', 'Mission explicitly integrates sustainability dimensions.'),
        (2, '02-purpose', 'p5.js is built and organized to prioritize [accessibility, inclusivity, community, and joy](https://p5js.org/community).', ['social'], 'interpreted_dimension', 'Explicit community/inclusion priorities; social sustainability is an analytical mapping.'),
        (3, '03-purpose', "EFF's mission is to ensure that technology supports freedom, justice, and innovation for all people of the world.", ['social'], 'interpreted_dimension', 'Mission names rights and justice, without a formal sustainability definition.'),
        (4, '04-purpose', 'FreeCAD is an open-source parametric 3D \nmodeler made primarily to design real-life objects of any size.', [], 'purpose_only', 'Functional purpose; sustainability not found in this purpose passage.'),
        (5, '05-purpose', 'Our mission is to ensure the right to repair, improve and reinstall software.', ['social', 'technical'], 'interpreted_dimension', 'Rights and ongoing ability to modify software are potential social/technical themes; not an environmental commitment by implication.'),
        (6, '06-purpose-followup', 'Sustainable and maintainable', ['technical'], 'explicit_sustainability', 'Principles heading is followed by maintainable-code, upstreaming and minimal device-specific-code guidance; no hardware longevity claim is invented.'),
        (7, '07-purpose', 'This is the home of the [Scala 2](https://www.scala-lang.org)\nstandard library, compiler, and language spec.', [], 'purpose_only', 'Functional introduction. Later CI energy advice is not the stated purpose.'),
        (8, '08-purpose', 'It aims to be a comprehensive data analysis environment that allows researchers within the field of solar physics to carry out their tasks with the minimal effort.', [], 'purpose_only', 'Scientific software purpose; solar physics does not imply an environmental sustainability mission.'),
        (9, '09-purpose', 'Reduce total observability costs.', ['economic'], 'interpreted_dimension', 'Stated use case about economic costs; not an explicit sustainability definition.'),
        (10, '10-purpose', 'Tauri aims to be a sustainable collective based on principles that guide sustainable free and open software communities.', ['social'], 'explicit_sustainability', 'Explicit organizational/community continuity goal.'),
        (11, '11-purpose', "High-performance inference of [OpenAI's Whisper](https://github.com/openai/whisper) automatic speech recognition (ASR) model:", [], 'purpose_only', 'Performance and product functionality alone do not establish sustainability.'),
        (12, '12-purpose', 'Wave is an open-source, AI-integrated terminal for macOS, Linux, and Windows.', [], 'purpose_only', 'Product description; sustainability not found in this purpose passage.'),
        (13, '13-purpose', 'Interactive API Reference from OpenAPI/Swagger', [], 'purpose_only', 'Product heading, not a sustainability commitment.'),
        (14, '14-purpose', 'is a Rust crate for cooking up terminal user interfaces', [], 'purpose_only', 'Functional description, not a sustainability mission.'),
        (15, '15-purpose', 'Leptos is a full-stack, isomorphic Rust web framework leveraging fine-grained reactivity to build declarative user interfaces.', [], 'purpose_only', 'Functional description, not a sustainability mission.'),
        (16, '16-purpose', 'Add authentication to applications and secure services with minimum effort.', [], 'purpose_only', 'Security functionality alone is not coded as sustainability.'),
        (17, '17-purpose', 'Build bulletproof UI components faster', [], 'purpose_only', 'Product slogan; no sustainability commitment established.'),
        (18, '18-purpose', 'Bitcoin Core connects to the Bitcoin peer-to-peer network to download and fully\nvalidate blocks and transactions.', [], 'purpose_only', 'Functional purpose; no external assumptions about Bitcoin energy use are introduced.'),
        (19, '19-purpose', 'Mastodon is a **free, open-source social network server**', [], 'purpose_only', 'A social-network product category alone is not a social sustainability commitment; compare the purpose-like statement in its policy.'),
        (20, '20-purpose', 'rust-analyzer is a language server that provides IDE functionality for\nwriting Rust programs.', [], 'purpose_only', 'Functional description; sustainability not found in this purpose passage.'),
        (21, '21-purpose', 'Brought to you by an inclusive community', ['social'], 'interpreted_dimension', 'Community inclusion is stated; social sustainability remains an analytical interpretation.'),
        (22, '22-purpose', 'PostHog is an all-in-one, open source platform for building successful products', [], 'purpose_only', 'Product purpose; no sustainability commitment established.'),
        (23, '23-purpose', 'Nix is a powerful package manager for Linux and other Unix systems that makes package\nmanagement reliable and reproducible.', [], 'purpose_only', 'Reliability and reproducibility alone are not treated as a sustainability definition.'),
        (24, '24-purpose', '**A safe home for all your data.**', [], 'purpose_only', 'Data-hosting purpose; no sustainability commitment established.'),
    ]
    for number, source, excerpt, dimensions, basis, rationale in purpose:
        add(number, '@' + source, excerpt, ['RQ1'], dimensions, basis, rationale, scope='Purpose/principles passage')
    add(1, '@01-ethical-principles', 'We will endeavor not to do further harm to the environment when we introduce new technologies to the web', ['RQ3', 'RQ4'], ['environmental'], 'explicit_framework_principle', 'Normative no-further-harm language in a framework referenced by the AI note; insufficient to assert a full non-substitutability framework.', scope='Referenced ethical framework')


POLICY_JUDGMENTS = [
    ('explicit_environmental_concern', 'Advisory Board Group Note; explicit sustainability and environmental recommendations; not endorsed by W3C itself or its Members.'),
    ('explicit_environmental_concern', 'Environmental concern plus learning/community rationale; no operational environmental limit found.'),
    ('explicit_environmental_concern', 'Dataset document is a policy-explanation blog post; supplementary contribution rules address experience-building and human review.'),
    ('explicit_environmental_concern', 'Environmental/social concerns and frugal-AI awareness; no critical-natural-capital definition found.'),
    ('explicit_environmental_concern', 'Cross-project recommendations, not a binding project-specific policy; environmental expertise explicitly deferred.'),
    ('explicit_environmental_concern', 'Dataset entity postmarketOS now names Nura in policy and official about page; keep original label and record documented continuity.'),
    ('explicit_sustainability_ai', 'Scala 2 explicitly adopts Scala 3 policy; two documents are one applicable policy chain, not independent observations.'),
    ('explicit_sustainability_ai', 'Trust, contributor effort and long-term maintenance responsibilities are linked.'),
    ('explicit_sustainability_ai', 'Small-team review sustainability and contributor learning are explicit concerns.'),
    ('implicit_concern_ai', 'Explicit sustainability phrase is in general issue-reporting guidance; AI subsection separately addresses reviewer time and fairness.'),
    ('explicit_sustainability_ai', 'Detailed rules are in a file named AGENTS.md at source, saved as other_policy.md; sustained maintenance is an explicit rationale.'),
    ('general_context_only', 'Explicit sustainability and scarce review bandwidth occur in general guidelines; the AI rule requires understanding and alignment.'),
    ('explicit_sustainability_ai', 'AI subsection explicitly connects sustainable reviews with bounded PRs and regression testing.'),
    ('generic_rules_only', 'AI rules address quality/licensing; backwards compatibility is in general guidelines, so no AI-specific sustainability rationale is assigned.'),
    ('implicit_concern_ai', 'Human attention bottleneck is stated, without sustainability terminology.'),
    ('implicit_concern_ai', 'AI subsection explicitly names reviewers’ limited time.'),
    ('implicit_concern_ai', 'AI measures explicitly aim to reduce maintenance burden.'),
    ('implicit_concern_ai', 'Community time is named, without a sustainability definition.'),
    ('implicit_concern_ai', 'Maintainability, finite team capacity and human connection are explicit concerns without sustainability terminology.'),
    ('implicit_concern_ai', 'AI restriction protects newcomer learning opportunities.'),
    ('generic_rules_only', 'Local extraction unusable; recovered official policy supplies legal/accountability rationale, with no sustainability-specific claim established.'),
    ('implicit_concern_ai', 'Explicit rationale protects maintainer time.'),
    ('generic_rules_only', 'Human accountability and disclosure rules do not, by themselves, establish sustainability intent.'),
    ('implicit_concern_ai', 'Reviewer time and learning paths for future maintainers are explicit concerns.'),
]


def write_csv(path, rows):
    with path.open('w', newline='', encoding='utf-8') as f:
        writer = csv.DictWriter(f, fieldnames=list(rows[0]), lineterminator='\n'); writer.writeheader(); writer.writerows(rows)


def main():
    annotations()
    write_csv(HERE / 'evidence.csv', EVIDENCE)
    cases = []
    for i, item in enumerate(SAMPLE):
        entity = item['entity']; ev = [e for e in EVIDENCE if e['entity'] == entity]
        purposes = [e for e in ev if e['scope'] == 'Purpose/principles passage']
        assert len(purposes) == 1
        purpose = purposes[0]
        policy = [e for e in ev if e['scope'] in ('AI policy', 'Supplementary contribution policy', 'Supplementary governance policy', 'Project-purpose statement embedded in AI policy')]
        cases.append({
            'entity': entity, 'screening_group': item['screening_group'],
            'rq1_purpose_passage_status': purpose['basis'],
            'rq1_evidence_ids': ';'.join(e['evidence_id'] for e in ev if 'RQ1' in e['rqs']),
            'rq2_ai_status': POLICY_JUDGMENTS[i][0],
            'rq3_ai_dimension_candidates': ';'.join(sorted({d for e in policy for d in e['dimensions'].split(';') if d})),
            'rq4_classification': 'insufficient_evidence',
            'rq4_reason': 'No explicit critical-natural-capital/non-substitutability framework established in reviewed policy text; neither weak nor strong is assigned.',
            'evidence_ids': ';'.join(e['evidence_id'] for e in ev),
            'notes': POLICY_JUDGMENTS[i][1],
        })
    write_csv(HERE / 'cases.csv', cases)
    readable = ['# Pilot evidence ledger', '',
                'Exact excerpts and provisional interpretations. The CSV is the machine-readable equivalent.', '']
    for ev in EVIDENCE:
        readable.extend([f"## {ev['evidence_id']}", '',
                         f"**{ev['entity']}** — {ev['rqs']}; {ev['scope']}; {ev['basis']}", '',
                         '> ' + ev['excerpt'].replace('\n', '\n> '), '',
                         f"Source: [{ev['source_path']}, lines {ev['line_start']}–{ev['line_end']}](<../../{ev['source_path']}#L{ev['line_start']}>).", '',
                         f"Candidate dimensions: {ev['dimensions'] or 'none assigned'}. {ev['rationale']}", '',
                         f"Uncertainty: {ev['uncertainty']}", ''])
    (HERE / 'evidence.md').write_text('\n'.join(readable))
    with DATASET.open(newline='', encoding='utf-8-sig') as f:
        table = list(csv.reader(f))
    baseline = json.loads((HERE / 'baseline.json').read_text())['original_cells_sha256']
    original = [r[:32] for r in table]
    assert hashlib.sha256(json.dumps(original, ensure_ascii=False).encode()).hexdigest() == baseline
    if 'supplementary_material' not in table[0]:
        table[0].append('supplementary_material')
        for row in table[1:]: row.append('[]')
    column = table[0].index('supplementary_material')
    for row in table[1:]:
        records = json.loads(row[column] or '[]')
        for source in SOURCES:
            if source['entity'] != row[0]: continue
            # Include successful sources and unusable retrieval attempts explicitly.
            record = {k: source.get(k) for k in ('id', 'title', 'role', 'url', 'resolved_url',
                       'accessed_at', 'version', 'relevant_rqs', 'status', 'snapshot', 'raw_snapshot', 'sha256')}
            record['used_as_evidence'] = any(e['source_id'] == source['id'] for e in EVIDENCE)
            if source['id'] == '06-purpose':
                record['notes'] = 'Redirect notice only; substantive purpose source is 06-purpose-followup.'
            elif source['id'] == '21-ai_policy':
                record['notes'] = 'Bot challenge, not policy text; recovered policy is 21-policy-raw.'
            elif source['role'] == 'original_policy_verification':
                record['notes'] = ('Byte-identical to local extract.' if source.get('local_bytes_identical')
                                   else 'Not byte-identical; HTML conversion/wrapping may differ. This alone is not evidence of substantive policy change.')
            records = [r for r in records if (r.get('url'), r.get('version')) != (record['url'], record['version'])]
            records.append(record)
        row[column] = json.dumps(records, ensure_ascii=False, separators=(',', ':'))
    assert [r[:32] for r in table] == original
    assert len(table) == 282 and len({r[0] for r in table[1:]}) == 281
    # Write only when content changes, with original CSV dialect and existing cells retained.
    import io
    buffer = io.StringIO(newline=''); csv.writer(buffer, lineterminator='\n').writerows(table)
    updated = buffer.getvalue().encode('utf-8')
    if DATASET.read_bytes() != updated: DATASET.write_bytes(updated)
    summary = {
        'pilot_entities': len(cases), 'evidence_rows': len(EVIDENCE),
        'rq1_purpose_passage_counts': dict(Counter(c['rq1_purpose_passage_status'] for c in cases)),
        'rq2_status_counts': dict(Counter(c['rq2_ai_status'] for c in cases)),
        'rq3_entity_counts_by_candidate_dimension': dict(Counter(d for c in cases for d in c['rq3_ai_dimension_candidates'].split(';') if d)),
        'rq4_classification_counts': dict(Counter(c['rq4_classification'] for c in cases)),
        'supplementary_retrieval_records': len(SOURCES),
        'retrieval_status_counts': dict(Counter(s['status'] for s in SOURCES)),
        'original_cells_sha256': baseline,
    }
    (HERE / 'summary.json').write_text(json.dumps(summary, indent=2) + '\n')
    validate()
    print(json.dumps(summary, indent=2))


def validate():
    with DATASET.open(newline='', encoding='utf-8-sig') as f: table = list(csv.reader(f))
    assert len(table) == 282 and all(len(r) == len(table[0]) for r in table)
    digest = hashlib.sha256(json.dumps([r[:32] for r in table], ensure_ascii=False).encode()).hexdigest()
    assert digest == json.loads((HERE / 'baseline.json').read_text())['original_cells_sha256']
    for source in SOURCES:
        if 'raw_snapshot' in source:
            assert hashlib.sha256((ROOT / source['raw_snapshot']).read_bytes()).hexdigest() == source['sha256']
    column = table[0].index('supplementary_material')
    attached = {r[0]: json.loads(r[column]) for r in table[1:]}
    for source in SOURCES:
        assert any(r['id'] == source['id'] for r in attached[source['entity']])
    for ev in EVIDENCE:
        content = (ROOT / ev['source_path']).read_text()
        assert ev['excerpt'] in content
        lines = content.splitlines()
        context = '\n'.join(lines[ev['line_start'] - 1:ev['line_end']])
        assert ev['excerpt'] in context
        if ev['source_id'] != 'local-snapshot':
            assert any(r['id'] == ev['source_id'] and r['used_as_evidence'] for r in attached[ev['entity']])
    assert len(SAMPLE) == 24


if __name__ == '__main__':
    main()
