"""Compare prefilter runs on a fixed, completely human-labelled sample."""
import argparse
import csv
import json
from pathlib import Path

from prefilter_common import DEFAULT_OUTPUT, PrefilterError, write_json

LABELS = {'useful', 'not_useful', 'uncertain'}


def evaluate(annotations, runs, budgets):
    with Path(annotations).open(encoding='utf-8', newline='') as stream:
        labels = list(csv.DictReader(stream))
    if not labels:
        raise PrefilterError('No human annotations supplied')
    if not budgets or any(b < 1 for b in budgets):
        raise PrefilterError('Reading budgets must be positive')
    manifests = [json.loads((Path(run) / 'manifest.json').read_text(encoding='utf-8')) for run in runs]
    reference = manifests[0]
    rq_ids = [rq['id'] for rq in reference['rqs']]
    seen = set()
    for row in labels:
        if row['sha256'] in seen:
            raise PrefilterError('Annotate each unique text once; duplicate contents cannot be split or counted twice')
        seen.add(row['sha256'])
        if row.get('split') not in ('tuning', 'evaluation'):
            raise PrefilterError('Each annotation needs a tuning or evaluation split')
        for rq in rq_ids:
            if row.get(f'{rq}_label') not in LABELS:
                raise PrefilterError(f'Complete every label with useful, not_useful or uncertain: source {row.get("document_id")}, {rq}')
    output = dict(version=1, interpretation='Metrics within the labelled sample only; not population recall estimates', runs=[])
    for run, manifest in zip(runs, manifests):
        if (manifest['corpus_sha256'] != reference['corpus_sha256']
                or manifest['protocol_sha256'] != reference['protocol_sha256']
                or [r['id'] for r in manifest['rqs']] != rq_ids):
            raise PrefilterError('Runs must use the same corpus and scientific research questions')
        sources = {str(d['id']): d['sha256'] for d in manifest['documents']}
        with (Path(run) / 'scores.csv').open(encoding='utf-8', newline='') as stream:
            scores = {r['sha256']: r for r in csv.DictReader(stream) if r['status'] == 'scored'}
        for row in labels:
            if sources.get(row['document_id']) != row['sha256'] or row['sha256'] not in scores:
                raise PrefilterError('Annotations are stale or refer to documents not scored in this run')
        metrics = []
        for split in ('tuning', 'evaluation'):
            subset = [r for r in labels if r['split'] == split]
            for rq in rq_ids:
                judged = [r for r in subset if r[f'{rq}_label'] != 'uncertain']
                ordered = sorted(judged, key=lambda r: (-float(scores[r['sha256']][f'{rq}_score']), int(r['document_id'])))
                positives = sum(r[f'{rq}_label'] == 'useful' for r in judged)
                for budget in sorted(set(budgets)):
                    retrieved = ordered[:budget]
                    hits = sum(r[f'{rq}_label'] == 'useful' for r in retrieved)
                    metrics.append(dict(split=split, rq=rq, budget=budget, judged=len(judged),
                                        uncertain=len(subset) - len(judged), positives=positives,
                                        retrieved=len(retrieved), useful_retrieved=hits,
                                        precision=hits / len(retrieved) if retrieved else None,
                                        recall=hits / positives if positives else None))
        output['runs'].append(dict(path=str(run), settings=manifest['settings'],
                                   query_mode=manifest['query_mode'], metrics=metrics))
    return output


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--annotations', type=Path, required=True)
    parser.add_argument('--runs', type=Path, nargs='+', required=True)
    parser.add_argument('--budgets', type=int, nargs='+', default=[5, 10])
    parser.add_argument('--output', type=Path, default=DEFAULT_OUTPUT / 'evaluation.json')
    args = parser.parse_args()
    try:
        report = evaluate(args.annotations, args.runs, args.budgets)
        protected = [args.annotations.resolve()] + [
            (run / name).resolve() for run in args.runs for name in
            ('manifest.json', 'scores.csv', 'annotation.csv', 'annotation-texts.json')]
        if (args.output.suffix != '.json' or args.output.resolve() in protected
                or any(p.suffix == '.qda' for p in args.output.resolve().parents)):
            raise PrefilterError('Use a distinct JSON output outside any QualCoder project')
        args.output.parent.mkdir(parents=True, exist_ok=True)
        write_json(args.output, report)
    except (PrefilterError, OSError, ValueError, KeyError) as exc:
        parser.exit(2, f'Prefilter evaluation: {exc}\n')
    print(f'Evaluation written to {args.output}; no metrics were inferred from unlabelled documents.')


if __name__ == '__main__':
    main()
