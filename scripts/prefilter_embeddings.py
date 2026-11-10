"""Token-aware segmentation and vector mathematics, independent of the CLI."""
from bisect import bisect_right
import json
import re

from prefilter_common import PrefilterError

ALGORITHM = 'prefilter-global-v1'


def load_queries(protocol, config_path, mode):
    questions = {}
    for line in protocol.read_text(encoding='utf-8').splitlines():
        match = re.match(r'^\s*-\s+\*\*(RQ\d+)\.\*\*\s*(.*?)\s*$', line)
        if match:
            identity, text = match.groups()
            if identity in questions or not text.strip():
                raise PrefilterError(f'Empty or repeated scientific question: {identity}')
            questions[identity] = text
    config = json.loads(config_path.read_text(encoding='utf-8'))
    if not isinstance(config, dict) or config.get('version') != 1:
        raise PrefilterError('Unsupported query configuration version')
    if (not isinstance(config.get('model'), str) or not config['model'].strip()
            or not isinstance(config.get('revision'), str) or not re.fullmatch(r'[a-f0-9]{40}', config['revision'])):
        raise PrefilterError('Specify a model and its fixed 40-character commit revision')
    for name in ('query_prefix', 'document_prefix'):
        if not isinstance(config.get(name), str):
            raise PrefilterError(f'Missing {name}')
    rqs, seen = [], set()
    if not isinstance(config.get('rqs'), list):
        raise PrefilterError('The query configuration must contain an rqs list')
    for rq in config['rqs']:
        if not isinstance(rq, dict) or not isinstance(rq.get('queries'), list):
            raise PrefilterError('Each RQ must contain an ID and a queries list')
        identity = rq.get('id')
        if not isinstance(identity, str) or identity not in questions or identity in seen:
            raise PrefilterError(f'Missing or repeated RQ in protocol/configuration: {identity}')
        seen.add(identity)
        queries, names = [], set()
        for query in rq.get('queries', []):
            if (not isinstance(query, dict) or not isinstance(query.get('id'), str) or not query['id'].strip() or query['id'] in names
                    or not isinstance(query.get('text'), str) or not query['text'].strip()):
                raise PrefilterError(f'{identity}: empty or repeated semantic query')
            names.add(query['id'])
            queries.append(dict(id=query['id'], text=query['text']))
        if not queries:
            raise PrefilterError(f'{identity}: no semantic queries')
        if mode == 'original':
            queries = [dict(id='original', text=re.sub(r'[*`]', '', questions[identity]))]
        rqs.append(dict(id=identity, scientific_question=questions[identity], queries=queries))
    if not rqs or set(questions) != seen:
        raise PrefilterError('Protocol and query configuration must contain the same nonempty set of RQ IDs')
    return config, rqs


def token_ids(tokenizer, text):
    return tokenizer(text, add_special_tokens=False, truncation=False, verbose=False)['input_ids']


def input_length(tokenizer, text):
    return len(tokenizer(text, add_special_tokens=True, truncation=False, verbose=False)['input_ids'])


def sections(text):
    """Partition the original text, retaining its immediate Markdown section title."""
    start, position, title, fence = 0, 0, '', None
    for line in text.splitlines(keepends=True):
        fence_match = re.match(r'^ {0,3}(`{3,}|~{3,})', line)
        if fence_match:
            mark = fence_match[1]
            if fence is None:
                fence = mark
            elif mark[0] == fence[0] and len(mark) >= len(fence):
                fence = None
        if fence is None and (heading := re.match(r'^ {0,3}#{1,6}\s+(.+?)\s*#*\s*$', line)):
            if position > start:
                yield start, position, title
            start, title = position, heading[1]
        position += len(line)
    if position > start:
        yield start, position, title


def make_chunks(text, tokenizer, chunk_tokens=256, overlap=0, prefix='passage: ', max_length=512):
    if not 16 <= chunk_tokens <= max_length:
        raise PrefilterError(f'chunk-tokens must be between 16 and the model limit ({max_length})')
    if not 0 <= overlap < chunk_tokens // 2:
        raise PrefilterError('overlap-tokens must be nonnegative and less than half the chunk size')
    chunks = []
    for section_start, section_end, title in sections(text):
        section = text[section_start:section_end]
        # Limit artificial context only; the complete source heading remains in the text.
        if title:
            title = tokenizer.decode(token_ids(tokenizer, title)[:32], skip_special_tokens=True)
        context = f'{title}\n\n' if title else ''
        lead = prefix + context
        available = chunk_tokens - input_length(tokenizer, lead) - 4
        if available < 1:
            # Very small experimental windows leave no room for added heading context.
            context, lead = '', prefix
            available = chunk_tokens - input_length(tokenizer, lead) - 4
        if available < 1:
            raise PrefilterError('The passage prefix leaves no room for source text')
        tokens = tokenizer(section, add_special_tokens=False, return_offsets_mapping=True,
                           truncation=False, verbose=False)
        offsets = tokens['offset_mapping']
        ends = [pair[1] for pair in offsets]
        boundaries = [m.end() for m in re.finditer(r'\n[ \t]*\n', section)] + [len(section)]
        start, covered_end = 0, 0
        while start < len(section):
            token_start = bisect_right(ends, start)
            token_end = min(len(offsets), token_start + available)
            if token_end == len(offsets):
                end = len(section)
            else:
                end = offsets[token_end - 1][1]
            choices = [b for b in boundaries if max(start, covered_end) < b <= end]
            if choices:
                end = choices[-1]
            while end > start and input_length(tokenizer, lead + section[start:end]) > chunk_tokens:
                earlier = [pair[0] for pair in offsets[token_start:token_end] if start < pair[0] < end]
                end = max(earlier) if earlier else start
            if end <= max(start, covered_end):
                raise PrefilterError('Cannot segment source text within the requested token window')
            content = section[start:end]
            weight = len(token_ids(tokenizer, section[max(start, covered_end):end]))
            chunks.append(dict(start=section_start + start, end=section_start + end,
                               title=title, input=lead + content, weight=weight))
            covered_end = end
            if end == len(section):
                break
            if overlap:
                local_offsets = tokenizer(content, add_special_tokens=False, return_offsets_mapping=True,
                                          truncation=False, verbose=False)['offset_mapping']
                rewind = local_offsets[max(1, len(local_offsets) - overlap)][0] if len(local_offsets) > 1 else len(content)
                start += max(1, rewind)
            else:
                start = end
    return chunks


def normalize(vectors):
    import numpy as np
    vectors = np.asarray(vectors, dtype=np.float32)
    if not np.isfinite(vectors).all():
        raise PrefilterError('Embedding contains non-finite values')
    norms = np.linalg.norm(vectors, axis=-1, keepdims=True)
    if (norms <= 1e-12).any():
        raise PrefilterError('Cannot normalize a zero embedding')
    return vectors / norms


def global_embedding(vectors, weights):
    import numpy as np
    vectors = normalize(vectors)
    weights = np.asarray(weights, dtype=np.float64)
    if weights.shape != (len(vectors),) or (weights < 0).any() or weights.sum() <= 0:
        raise PrefilterError('Invalid content-token weights')
    return normalize(np.average(vectors, axis=0, weights=weights))


def score_document(global_vector, block_vectors, query_vectors, rqs):
    import numpy as np
    global_scores = np.clip(normalize(query_vectors) @ normalize(global_vector), -1, 1)
    local_scores = np.clip(normalize(block_vectors) @ normalize(query_vectors).T, -1, 1)
    results, offset = {}, 0
    for rq in rqs:
        count = len(rq['queries'])
        best_query = int(np.argmax(global_scores[offset:offset + count]))
        block, query = np.unravel_index(np.argmax(local_scores[:, offset:offset + count]),
                                      local_scores[:, offset:offset + count].shape)
        results[rq['id']] = dict(score=float(global_scores[offset + best_query]),
                                 query_id=rq['queries'][best_query]['id'],
                                 passage_score=float(local_scores[block, offset + query]),
                                 passage_query_id=rq['queries'][query]['id'], passage_index=int(block))
        offset += count
    return results
