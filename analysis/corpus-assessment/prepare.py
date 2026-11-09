"""Inventory documents and extract review candidates. Patterns do not assign codes."""
import csv
import hashlib
import json
import re
from collections import defaultdict
from pathlib import Path

HERE = Path(__file__).resolve().parent
ROOT = HERE.parents[1]
AI = re.compile(r'\b(AI|LLMs?|large language models?|generative|coding agents?|automation|automated contributions)\b', re.I)
THEMES = re.compile(r'sustainab|environmental|ecolog|carbon footprint|climat|energy.{0,35}(consum|use|water)|water.{0,25}(use|consum)|'
                    r'burnout|burn.out|overwhelm|overload|\bburden\b|workload|review.{0,30}(time|effort|capacity)|'
                    r'(time|effort|resources|attention|bandwidth).{0,35}(limit|scarc|wast|cost|consum)|'
                    r'(limit|scarc|wast|cost|consum).{0,35}(time|effort|resources|attention|bandwidth)|'
                    r'learn|skills?\b|atroph|maintainab|long.term|future maintain|human connection|trust|inclus|fair|exploitat|exploit|'
                    r'maintainer.{0,40}(time|fatigue)|review (load|resources|cycles)|back.and.forth|bottleneck|human collaboration|'
                    r'livelihood|financ|\bcosts?\b|critical natural|substitut|ecological limit|planetary bound', re.I)
HEAD = re.compile(r'^(#{1,6})\s+(.+)')


def sha(data): return hashlib.sha256(data).hexdigest()


def ranges(lines, kind, entity):
    if entity == 'EFF' and kind == 'ai_policy': return [(350, 419)]
    if entity == 'Software Freedom Conservancy (recommandations LLM)': return [(335, 620)]
    if entity == 'postmarketOS': return [(269, 328)]
    if entity == 'SunPy': return [(36, 219)]
    if kind == 'ai_policy': return [(0,len(lines))]
    if entity in ('ggml-org/whisper.cpp', 'ggml-org/llama.cpp') and kind == 'other_policy': return [(0,len(lines))]
    headings = [(i, len(m[1]), m[2]) for i, l in enumerate(lines) if (m := HEAD.match(l))]
    if kind in ('ai_policy', 'other_policy', 'supplementary_policy') and headings and headings[0][0] <= 12 and headings[0][1] == 1 and AI.search(headings[0][2]):
        return [(0,len(lines))]
    found = []
    for i, level, title in headings:
        if not AI.search(title): continue
        end = next((j for j, lev, _ in headings if j > i and lev <= level), len(lines))
        found.append((i, end))
    if not found and kind in ('ai_policy', 'other_policy', 'agent', 'supplementary_policy'):
        return [(0,len(lines))]
    if not found:
        # Paragraph-level candidates only; their scope must be checked during review.
        for i, line in enumerate(lines):
            if AI.search(line): found.append((max(0, i - 2), min(len(lines), i + 4)))
    return found


def main():
    with (ROOT / 'data/281/dataset1-multiple-ai-policies.csv').open(newline='', encoding='utf-8-sig') as f: table = list(csv.reader(f))
    baseline = json.loads((HERE / 'baseline.json').read_text())
    assert sha(json.dumps([r[:32] for r in table], ensure_ascii=False).encode()) == baseline['original_cells_sha256']
    sources = json.loads((HERE / 'source-manifest.json').read_text())
    documents, candidates, groups = [], [], defaultdict(list)
    for number, row in enumerate(table[1:], 1):
        entity = row[0]
        entries = [(str(p.relative_to(ROOT)), p.stem, '', None)
                   for p in sorted((ROOT / 'data/281/policies' / entity).glob('*.md'))]
        entries += [(s['snapshot'], 'supplementary_policy', s['url'], s['id']) for s in sources
                    if s['entity'] == entity and s['role'] == 'supplementary_policy' and s['status'] == 'downloaded']
        for path, kind, url, source_id in entries:
            text = (ROOT / path).read_text(); lines = text.splitlines()
            if not url:
                slot = {'ai_policy': 9, 'contributing': 10, 'agent': 11, 'other_policy': 13}.get(kind)
                url = row[slot] if slot is not None else ''
            doc = {'document_id': f'D{len(documents)+1:04d}', 'entity': entity, 'csv_row': number + 1,
                   'path': path, 'kind': kind, 'source_url': url, 'source_id': source_id,
                   'sha256': sha((ROOT/path).read_bytes()), 'lines': len(lines),
                   'ai_ranges': ranges(lines, kind, entity),
                   'extraction_status': 'possible_bot_challenge' if re.search(r'Cookie monster!|Making sure you.re not a bot|Access Denied|Just a moment\.\.\.', text, re.I) else 'text_available'}
            documents.append(doc); groups[doc['sha256']].append(path)
            allowed = set(i for a,b in doc['ai_ranges'] for i in range(a,b))
            if doc['extraction_status'] != 'text_available': continue
            for match in re.finditer(r'\S[^\n]*(?:\n(?!\s*\n)[^\n]*)*', text):
                start = text[:match.start()].count('\n')
                excerpt = match.group()
                if start not in allowed or not THEMES.search(re.sub(r'\s+', ' ', excerpt)): continue
                if len(excerpt) > 6000: continue
                candidates.append({'candidate_id': f'P{len(candidates)+1:04d}',
                                   'entity': entity, 'document_id': doc['document_id'],
                                   'path': path, 'line_start': start+1,
                                   'line_end': start+excerpt.count('\n')+1,
                                   'excerpt': excerpt})
    (HERE / 'documents.json').write_text(json.dumps(documents, indent=2, ensure_ascii=False)+'\n')
    (HERE / 'candidates.json').write_text(json.dumps(candidates, indent=2, ensure_ascii=False)+'\n')
    (HERE / 'duplicate-groups.json').write_text(json.dumps([v for v in groups.values() if len(v)>1],indent=2)+'\n')
    (HERE / 'baseline.json').write_text(json.dumps(baseline,indent=2)+'\n')
    print(f'{len(documents)} documents; {len(candidates)} candidate paragraphs; {len(set(c["entity"] for c in candidates))} entities with candidates')


if __name__ == '__main__': main()
