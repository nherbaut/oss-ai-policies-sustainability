"""Read-only validation of corpus results, excerpts, snapshots and CSV preservation."""
import csv
import hashlib
import json
from pathlib import Path

HERE=Path(__file__).resolve().parent
ROOT=HERE.parents[1]


def sha(data):return hashlib.sha256(data).hexdigest()


def csv_dict(path):
    with path.open(newline='',encoding='utf-8-sig') as f:return list(csv.DictReader(f))


def main():
    dataset=ROOT/'data/281/dataset1-multiple-ai-policies.csv'
    with dataset.open(newline='',encoding='utf-8-sig') as f:table=list(csv.reader(f))
    baseline=json.loads((HERE/'baseline.json').read_text())
    expected=baseline['dataset_entries']
    assert len(table)==expected+1 and len({r[0] for r in table[1:]})==expected
    assert all(len(r)==len(table[0]) for r in table)
    assert sha(json.dumps([r[:32] for r in table],ensure_ascii=False).encode())==baseline['original_cells_sha256']
    cases=csv_dict(HERE/'cases.csv');evidence=csv_dict(HERE/'evidence.csv')
    assert len(cases)==expected and {c['entity'] for c in cases}=={r[0] for r in table[1:]}
    by_id={e['evidence_id']:e for e in evidence};assert len(by_id)==len(evidence)
    for c in cases:
        for field in ('rq1_evidence_ids','rq2_evidence_ids'):
            for identifier in filter(None,c[field].split(';')):
                assert identifier in by_id and by_id[identifier]['entity']==c['entity']
        assert c['rq2_evidence_ids'] or c['rq2_status']=='insufficient_policy_evidence'
        if c['rq2_status'] in ('implicit_concern_ai','explicit_environmental_concern','explicit_sustainability_ai'):
            assert c['rq3_ai_dimension_candidates']
        assert c['rq4_classification']=='insufficient_evidence'
    for e in evidence:
        path=ROOT/e['source_path'];frozen=ROOT/e['frozen_path']
        assert sha(path.read_bytes())==e['source_sha256']==sha(frozen.read_bytes())
        text=path.read_text();start=int(e['line_start']);end=int(e['line_end'])
        assert e['excerpt'] and e['excerpt'] in '\n'.join(text.splitlines()[start-1:end])
    sources=json.loads((HERE/'source-manifest.json').read_text())
    col=table[0].index('supplementary_material')
    attached={r[0]:json.loads(r[col]) for r in table[1:]}
    assert all(attached.values())
    for s in sources:
        assert any(r.get('url')==s['url'] and r.get('version')==s.get('version') for r in attached[s['entity']])
        if s.get('raw_snapshot'):assert sha((ROOT/s['raw_snapshot']).read_bytes())==s['sha256']
    summary=json.loads((HERE/'summary.json').read_text())
    assert summary['entities']==len(cases) and summary['evidence_rows']==len(evidence)
    assert sum(summary['rq1_counts'].values())==expected==sum(summary['rq2_counts'].values())
    for entity in ('Forgejo',):
        assert any(r.get('role')=='user_supplied_policy' for r in attached[entity])
    print(f'PASS: {len(cases)} cases, {len(evidence)} exact excerpts and frozen copies, {len(sources)} source records; all original CSV cells preserved.')


if __name__=='__main__':main()
