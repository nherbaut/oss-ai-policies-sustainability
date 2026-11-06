"""Reproduce the local corpus audit and deterministic pilot selection (stdlib only)."""
import csv
import hashlib
import json
import re
from collections import Counter, defaultdict
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
OUT = Path(__file__).resolve().parent
DATASET = ROOT / 'data/281/dataset1-multiple-ai-policies.csv'
FIELDS = [(9, 'ai_policy'), (10, 'contributing'), (11, 'agent'), (13, 'other_policy')]
ENVIRONMENTAL = re.compile(
    r'\b(environmental|ecological|carbon footprint|greenhouse|climate|water use|'
    r'energy consumption|energy and water|energy costs)\b', re.I)
SUSTAINABILITY = re.compile(r'\bsustainab\w*\b', re.I)


def digest(value):
    return hashlib.sha256(value).hexdigest()


def run():
    with DATASET.open(newline='', encoding='utf-8-sig') as f:
        table = list(csv.reader(f))
    header, rows = table[0], table[1:]
    assert len(rows) == 281 and len({r[0] for r in rows}) == 281
    # Positional access preserves the source's repeated "doc excerpt" headers.
    original_width = 32
    baseline = digest(json.dumps([header[:original_width]] +
                      [r[:original_width] for r in rows], ensure_ascii=False).encode())
    assert baseline == json.loads((OUT / 'baseline.json').read_text())['original_cells_sha256'], 'Original dataset cells changed since this pilot was frozen.'
    groups = defaultdict(list)
    inventory, missing, hashes, selected = [], [], defaultdict(list), []
    for number, row in enumerate(rows, 2):
        entity = row[0].strip()
        files = sorted((ROOT / 'data/281/policies' / entity).glob('*.md'))
        content = '\n'.join(p.read_text() for p in files)
        group = ('environmental' if ENVIRONMENTAL.search(content) else
                 'other_explicit_sustainability' if SUSTAINABILITY.search(content)
                 else 'no_explicit_sustainability')
        groups[group].append(entity)
        for index, kind in FIELDS:
            if row[index].strip() and not any(p.stem == kind for p in files):
                missing.append({'entity': entity, 'type': kind, 'source_cell': row[index]})
        for p in files:
            text = p.read_text()
            rel = str(p.relative_to(ROOT))
            sha = digest(p.read_bytes())
            hashes[sha].append(rel)
            inventory.append({'entity': entity, 'csv_row': number, 'path': rel,
                              'document_type': p.stem, 'bytes': p.stat().st_size,
                              'lines': len(text.splitlines()), 'sha256': sha,
                              'screening_group': group,
                              'possible_bot_challenge': bool(re.search(
                                  r'Cookie monster!|Making sure you.re not a bot|'
                                  r'Access Denied|Just a moment\.\.\.', text, re.I))})
    for group in ('environmental', 'other_explicit_sustainability', 'no_explicit_sustainability'):
        selected.extend(groups[group][:8])
    for row in rows:
        if len(selected) == 24:
            break
        if row[0] not in selected:
            selected.append(row[0])
    group_for = {entity: group for group, entities in groups.items() for entity in entities}
    sample = [{'entity': entity, 'screening_group': group_for[entity],
               'files': [x['path'] for x in inventory if x['entity'] == entity]}
              for entity in selected]
    report = {
        'dataset_entries': len(rows), 'original_columns': original_width,
        'original_cells_sha256': baseline,
        'documents': len(inventory),
        'entities_with_documents': len({x['entity'] for x in inventory}),
        'entities_without_documents': [r[0] for r in rows if not any(x['entity'] == r[0] for x in inventory)],
        'document_types': dict(Counter(x['document_type'] for x in inventory)),
        'screening_counts': {g: len(v) for g, v in groups.items()},
        'screening_patterns': {'environmental': ENVIRONMENTAL.pattern, 'sustainability': SUSTAINABILITY.pattern},
        'missing_linked_documents': missing,
        'exact_duplicate_groups': [v for v in hashes.values() if len(v) > 1],
        'possible_bot_challenges': [x['path'] for x in inventory if x['possible_bot_challenge']],
        'pilot_screening_counts': dict(Counter(x['screening_group'] for x in sample)),
        'pilot_documents': sum(len(x['files']) for x in sample),
    }
    (OUT / 'audit.json').write_text(json.dumps(report, indent=2, ensure_ascii=False) + '\n')
    (OUT / 'sample.json').write_text(json.dumps(sample, indent=2, ensure_ascii=False) + '\n')
    with (OUT / 'inventory.csv').open('w', newline='') as f:
        w = csv.DictWriter(f, fieldnames=list(inventory[0]), lineterminator='\n'); w.writeheader(); w.writerows(inventory)
    print(json.dumps({k: v for k, v in report.items() if k not in
                     ('missing_linked_documents', 'exact_duplicate_groups')}, indent=2))


if __name__ == '__main__':
    run()
