"""Rank QualCoder texts against research questions with local E5 embeddings."""
import argparse
from collections import defaultdict
import importlib.metadata
import json
from pathlib import Path
import random
import sqlite3
import sys
import tempfile

from prefilter_common import (DEFAULT_OUTPUT, DEFAULT_PROJECT, ROOT, PrefilterError, digest,
                              document_metadata, duplicate_groups, load_corpus, output_directory,
                              write_csv, write_json)
from prefilter_embeddings import (ALGORITHM, global_embedding, input_length, load_queries, make_chunks,
                                  normalize, score_document)


def save_vectors(path, **arrays):
    import numpy as np
    if path.is_symlink():
        raise PrefilterError(f'Refusing to overwrite symlink: {path}')
    with tempfile.TemporaryDirectory(dir=path.parent) as temporary:
        candidate = Path(temporary) / 'vectors.npz'
        np.savez_compressed(candidate, **arrays)
        candidate.replace(path)


def ranked_rows(documents, results, rqs):
    rows = []
    groups = duplicate_groups(documents)
    for doc in documents:
        scores = results.get(doc['sha256'], {})
        best = max(scores, key=lambda rq: scores[rq]['score']) if scores else ''
        row = dict(document_id=doc['id'], entity=doc['entity'], name=doc['name'], role=doc['role'],
                   paths='; '.join(p.get('path', '') for p in doc['provenance']),
                   sha256=doc['sha256'], representative_id=groups[doc['sha256']][0]['id'],
                   occurrences=len(groups[doc['sha256']]), characters=len(doc['text']),
                   status='empty' if doc['empty'] else 'scored',
                   max_score=scores[best]['score'] if best else '', best_rq=best)
        for rq in rqs:
            identity = rq['id']
            item = scores.get(identity, {})
            row[f'{identity}_score'] = item.get('score', '')
            row[f'{identity}_query'] = item.get('query_id', '')
            row[f'{identity}_passage_score'] = item.get('passage_score', '')
            row[f'{identity}_passage_query'] = item.get('passage_query_id', '')
            row[f'{identity}_passage_start'] = item.get('start', '')
            row[f'{identity}_passage_end'] = item.get('end', '')
            row[f'{identity}_passage'] = item.get('excerpt', '')
        rows.append(row)
    rows.sort(key=lambda r: (r['max_score'] == '', -r['max_score'] if r['max_score'] != '' else 0, r['document_id']))
    for index, row in enumerate(rows, 1):
        row['rank'] = index if row['status'] == 'scored' else ''
    for rq in rqs:
        identity = rq['id']
        ordered = sorted((r for r in rows if r['status'] == 'scored'),
                         key=lambda r: (-r[f'{identity}_score'], r['document_id']))
        for index, row in enumerate(ordered, 1):
            row[f'{identity}_rank'] = index
        for row in rows:
            row.setdefault(f'{identity}_rank', '')
    return rows


def annotation_sample(documents, rows, rqs, size=60, seed=42):
    """Sample unique contents across role, length and baseline ranking strata."""
    by_id = {d['id']: d for d in documents}
    unique = [r for r in rows if r['status'] == 'scored' and r['document_id'] == r['representative_id']]
    if not unique:
        return [], []
    lengths = sorted(r['characters'] for r in unique)
    low, high = lengths[len(lengths) // 3], lengths[2 * len(lengths) // 3]
    buckets = defaultdict(list)
    for index, row in enumerate(unique):
        length = 'short' if row['characters'] <= low else 'medium' if row['characters'] <= high else 'long'
        band = ('high', 'middle', 'low')[min(2, 3 * index // len(unique))]
        buckets[(row['role'], length, band)].append(row)
    rng = random.Random(seed)
    keys = sorted(buckets)
    for bucket in buckets.values():
        rng.shuffle(bucket)
    rng.shuffle(keys)
    selected = []
    while len(selected) < min(size, len(unique)):
        for key in keys:
            if buckets[key] and len(selected) < min(size, len(unique)):
                selected.append((key, buckets[key].pop()))
    rng.shuffle(selected)
    labels, texts = [], []
    for index, (stratum, row) in enumerate(selected):
        label = {k: row[k] for k in ['document_id', 'sha256', 'entity', 'name', 'role']}
        label.update(split='evaluation' if index % 3 == 0 else 'tuning',
                     length_band=stratum[1], baseline_rank_band=stratum[2], notes='')
        for rq in rqs:
            label[f'{rq["id"]}_label'] = ''
        labels.append(label)
        doc = by_id[row['document_id']]
        # Source text is available without viewing model scores, to reduce anchoring.
        texts.append(dict(document_id=doc['id'], entity=doc['entity'], name=doc['name'],
                          sha256=doc['sha256'], text=doc['text'], provenance=doc['provenance']))
    return labels, texts


def run(args):
    import numpy as np
    from sentence_transformers import SentenceTransformer

    config, rqs = load_queries(args.protocol, args.queries, args.query_mode)
    documents, excluded = load_corpus(args.project)
    if args.limit:
        documents = documents[:args.limit]
    groups = duplicate_groups(documents)
    output = output_directory(args.output_dir, args.project, (args.protocol, args.queries))
    cache = output_directory(args.cache_dir or output / 'cache', args.project, (args.protocol, args.queries))
    versions = {package: importlib.metadata.version(package)
                for package in ['sentence-transformers', 'transformers', 'torch', 'numpy']}
    print(f'Loading {config["model"]} at {config["revision"]} on {args.device} (local files: {not args.allow_download})', flush=True)
    model = SentenceTransformer(config['model'], revision=config['revision'], device=args.device,
                                local_files_only=not args.allow_download, trust_remote_code=False)
    max_length = model.max_seq_length
    if not 16 <= args.chunk_tokens <= max_length or not 0 <= args.overlap_tokens < args.chunk_tokens // 2:
        raise PrefilterError(f'Use 16 <= chunk-tokens <= {max_length}, with overlap-tokens < half the window')
    settings = dict(algorithm=ALGORITHM, model=config['model'], revision=config['revision'],
                    document_prefix=config['document_prefix'], chunk_tokens=args.chunk_tokens,
                    overlap_tokens=args.overlap_tokens, max_length=max_length, heading_max_tokens=32,
                    heading_context=True, aggregation='normalize(weighted_mean(normalized_blocks))',
                    weights='new source content tokens; artificial heading context excluded',
                    device=args.device, batch_size=args.batch_size, packages=versions)
    queries = [config['query_prefix'] + q['text'] for rq in rqs for q in rq['queries']]
    if any(input_length(model.tokenizer, q) > max_length for q in queries):
        raise PrefilterError('A semantic query exceeds the model input limit')
    query_key = digest(dict(model=config['model'], revision=config['revision'], queries=queries,
                            algorithm=ALGORITHM, packages=versions, device=args.device, batch_size=args.batch_size))
    query_path = cache / f'queries-{query_key}.npz'
    if query_path.exists():
        with np.load(query_path, allow_pickle=False) as stored:
            query_vectors = normalize(stored['vectors'])
        if query_vectors.shape != (len(queries), model.get_sentence_embedding_dimension()):
            raise PrefilterError(f'Invalid query cache: {query_path}')
    else:
        query_vectors = normalize(model.encode(queries, batch_size=args.batch_size, normalize_embeddings=True,
                                               show_progress_bar=False, prompt=''))
        save_vectors(query_path, vectors=query_vectors)
    results, vectors, chunk_counts = {}, {}, {}
    hits, total_chunks = 0, 0
    unique = [members[0] for members in groups.values() if not members[0]['empty']]
    for index, doc in enumerate(sorted(unique, key=lambda d: d['id']), 1):
        key = digest(dict(text_sha256=doc['sha256'], settings=settings))
        path = cache / f'document-{key}.npz'
        chunks = make_chunks(doc['text'], model.tokenizer, args.chunk_tokens, args.overlap_tokens,
                             config['document_prefix'], max_length)
        chunks = [chunk for chunk in chunks if chunk['weight'] > 0]
        if not chunks:
            raise PrefilterError(f'Source {doc["id"]} has no encodable content tokens')
        cache_hit = path.exists()
        if cache_hit:
            with np.load(path, allow_pickle=False) as stored:
                block_vectors = normalize(stored['blocks'])
                vector = normalize(stored['global_vector'])
                if (block_vectors.shape != (len(chunks), query_vectors.shape[1])
                        or vector.shape != (query_vectors.shape[1],)
                        or not np.array_equal(stored['starts'], [c['start'] for c in chunks])
                        or not np.array_equal(stored['ends'], [c['end'] for c in chunks])):
                    raise PrefilterError(f'Invalid document cache: {path}')
            hits += 1
        else:
            block_vectors = normalize(model.encode([c['input'] for c in chunks], batch_size=args.batch_size,
                                                   normalize_embeddings=True, show_progress_bar=False, prompt=''))
            vector = global_embedding(block_vectors, [c['weight'] for c in chunks])
            save_vectors(path, blocks=block_vectors, global_vector=vector,
                         starts=np.array([c['start'] for c in chunks]), ends=np.array([c['end'] for c in chunks]))
        scores = score_document(vector, block_vectors, query_vectors, rqs)
        for item in scores.values():
            chunk = chunks[item.pop('passage_index')]
            item.update(start=chunk['start'], end=chunk['end'], title=chunk['title'],
                        excerpt=doc['text'][chunk['start']:chunk['end']])
        results[doc['sha256']], vectors[doc['sha256']] = scores, vector
        chunk_counts[doc['sha256']] = len(chunks)
        total_chunks += len(chunks)
        print(f'[{index}/{len(unique)}] source {doc["id"]}: {len(chunks)} blocks{", cached" if cache_hit else ""}', flush=True)

    rows = ranked_rows(documents, results, rqs)
    base_fields = ['rank', 'document_id', 'entity', 'name', 'role', 'paths', 'sha256', 'representative_id',
                   'occurrences', 'characters', 'status', 'max_score', 'best_rq']
    rq_fields = [f'{rq["id"]}_{suffix}' for rq in rqs for suffix in
                 ['rank', 'score', 'query', 'passage_score', 'passage_query', 'passage_start', 'passage_end', 'passage']]
    fields = base_fields + rq_fields
    write_csv(output / 'scores.csv', rows, fields)
    for rq in rqs:
        write_csv(output / f'ranking-{rq["id"]}.csv', sorted(rows, key=lambda r: (
            r[f'{rq["id"]}_rank'] == '', r[f'{rq["id"]}_rank'] or len(rows) + 1)), fields)
    scored = [doc for doc in documents if not doc['empty']]
    matrix = np.stack([vectors[d['sha256']] for d in scored]) if scored else np.empty((0, query_vectors.shape[1]), dtype=np.float32)
    save_vectors(output / 'embeddings.npz', document_ids=np.array([d['id'] for d in scored], dtype=np.int64),
                 document_vectors=matrix, query_vectors=query_vectors,
                 query_ids=np.array([f'{rq["id"]}/{q["id"]}' for rq in rqs for q in rq['queries']]))
    labels, texts = annotation_sample(documents, rows, rqs)
    # Never overwrite human annotations when refreshing a run.
    if not (output / 'annotation.csv').exists():
        label_fields = ['document_id', 'sha256', 'entity', 'name', 'role', 'split', 'length_band',
                        'baseline_rank_band', 'notes'] + [f'{rq["id"]}_label' for rq in rqs]
        write_csv(output / 'annotation.csv', labels, label_fields)
        write_json(output / 'annotation-texts.json', texts)
    manifest = dict(version=1, settings=settings, query_mode=args.query_mode, rqs=rqs,
                    protocol_sha256=digest(args.protocol.read_text(encoding='utf-8')),
                    query_config_sha256=digest(config), query_cache_key=query_key,
                    corpus_sha256=digest([document_metadata(d) for d in documents]),
                    documents=[document_metadata(d) for d in documents], excluded_sources=excluded,
                    counts=dict(documents=len(documents), scored=len(scored), unique_scored=len(unique),
                                chunks=total_chunks, document_cache_hits=hits),
                    chunk_counts=chunk_counts, sample=dict(seed=42, requested=60, available=len(labels)),
                    interpretation='Semantic proximity, not a relevance probability or an exclusion decision')
    write_json(output / 'manifest.json', manifest)
    print(f'Results: {output} ({len(scored)} scored documents, {hits} cached unique texts)')
    return manifest


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--project', type=Path, default=DEFAULT_PROJECT)
    parser.add_argument('--protocol', type=Path, default=ROOT / 'protocol.md')
    parser.add_argument('--queries', type=Path, default=Path(__file__).with_name('prefilter_queries.json'))
    parser.add_argument('--output-dir', type=Path, default=DEFAULT_OUTPUT)
    parser.add_argument('--cache-dir', type=Path)
    parser.add_argument('--query-mode', choices=['expanded', 'original'], default='expanded')
    parser.add_argument('--chunk-tokens', type=int, default=256)
    parser.add_argument('--overlap-tokens', type=int, default=0)
    parser.add_argument('--device', default='cpu')
    parser.add_argument('--batch-size', type=int, default=16)
    parser.add_argument('--allow-download', action='store_true', help='Allow model download if not cached')
    parser.add_argument('--limit', type=int, help='Process only the first N text sources, for a smoke test')
    args = parser.parse_args()
    if args.batch_size < 1 or (args.limit is not None and args.limit < 1):
        parser.error('batch-size and limit must be positive')
    try:
        run(args)
    except (PrefilterError, OSError, sqlite3.Error, ImportError, ValueError, KeyError, RuntimeError) as exc:
        parser.exit(2, f'RQ similarity: {exc}\n')


if __name__ == '__main__':
    main()
