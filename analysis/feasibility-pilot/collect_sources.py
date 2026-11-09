"""Collect official supplementary sources; never overwrite local policy extracts.

Network access is required. Writes snapshots and a manifest, but does not edit
the dataset. The reviewed source records are attached by build_results.py.
"""
import csv
import hashlib
import json
import re
import subprocess
from concurrent.futures import ThreadPoolExecutor
from datetime import datetime, timezone
from pathlib import Path
from urllib.request import Request, urlopen

HERE = Path(__file__).resolve().parent
ROOT = HERE.parents[1]
PURPOSE_PAGES = {
    'W3C': 'https://www.w3.org/mission/',
    'EFF': 'https://www.eff.org/about',
    'Software Freedom Conservancy (recommandations LLM)': 'https://sfconservancy.org/about/',
    'postmarketOS': 'https://postmarketos.org/about/',
    'SunPy': 'https://sunpy.org/about/',
    'Forgejo': 'https://forgejo.org/',
}
EXTRA_SOURCES = [
    {'id': '01-ethical-principles', 'entity': 'W3C', 'title': 'Ethical Web Principles: sustainability',
     'url': 'https://www.w3.org/TR/ethical-web-principles/#sustainable',
     'role': 'referenced_framework', 'version': None, 'relevant_rqs': ['RQ3', 'RQ4']},
    {'id': '03-contribution-rules', 'entity': 'EFF', 'title': 'Coding with EFF',
     'url': 'https://www.eff.org/about/opportunities/volunteer/coding-with-eff',
     'role': 'additional_contribution_policy', 'version': None, 'relevant_rqs': ['RQ2', 'RQ3', 'RQ4']},
    {'id': '06-purpose-followup', 'entity': 'postmarketOS', 'title': 'About postmarketOS (redirect target)',
     'url': 'https://wiki.nura.eco/wiki/About_postmarketOS',
     'role': 'purpose_statement_candidate', 'version': None, 'relevant_rqs': ['RQ1']},
    {'id': '21-policy-raw', 'entity': 'Forgejo', 'title': 'Forgejo governance AI Agreement (raw endpoint)',
     'url': 'https://codeberg.org/forgejo/governance/raw/branch/main/AIAgreement.md',
     'role': 'additional_policy_retrieval', 'version': 'main', 'relevant_rqs': ['RQ2', 'RQ3', 'RQ4']},
]


def raw_url(url):
    return re.sub(r'^https://github.com/([^/]+)/([^/]+)/blob/',
                  r'https://raw.githubusercontent.com/\1/\2/', url)


def fetch(task):
    record = dict(task)
    record['accessed_at'] = datetime.now(timezone.utc).isoformat()
    destination = HERE / 'sources' / record['id']
    try:
        req = Request(raw_url(record['url']), headers={'User-Agent': 'Research feasibility pilot (Python urllib)'})
        with urlopen(req, timeout=35) as response:
            data = response.read()
            record['resolved_url'] = response.geturl()
            media_type = response.headers.get_content_type()
        record['sha256'] = hashlib.sha256(data).hexdigest()
        is_html = media_type == 'text/html' or data.lstrip().lower().startswith(b'<!doctype html')
        raw_path = destination.with_suffix('.html' if is_html else '.raw.md')
        raw_path.write_bytes(data)
        if is_html:
            result = subprocess.run(['pandoc', '-f', 'html', '-t', 'gfm', '--wrap=none'],
                                    input=data, capture_output=True, check=True)
            text = result.stdout.decode()
        else:
            text = data.decode('utf-8-sig')
        destination.with_suffix('.md').write_text(text)
        record['snapshot'] = str(destination.with_suffix('.md').relative_to(ROOT))
        record['raw_snapshot'] = str(raw_path.relative_to(ROOT))
        record['status'] = 'downloaded'
        if re.search(r'Cookie monster!|Making sure you.re not a bot|Access Denied|Just a moment\.\.\.', text, re.I):
            record['status'] = 'possible_bot_challenge'
        if record['role'] == 'original_policy_verification' and 'local_path' in record:
            local = (ROOT / record['local_path']).read_text()
            record['local_bytes_identical'] = local == text
    except Exception as exc:
        record['status'] = 'unavailable'
        record['error'] = f'{type(exc).__name__}: {exc}'
    return record


def main():
    (HERE / 'sources').mkdir(exist_ok=True)
    with (ROOT / 'data/281/dataset1-multiple-ai-policies.csv').open(newline='', encoding='utf-8-sig') as f:
        table = list(csv.reader(f))
    rows = {r[0]: r for r in table[1:]}
    sample = json.loads((HERE / 'sample.json').read_text())
    tasks = []
    for entity_number, item in enumerate(sample, 1):
        entity = item['entity']; row = rows[entity]
        version = None
        for index, kind in [(9, 'ai_policy'), (10, 'contributing'), (11, 'agent'), (13, 'other_policy')]:
            url = row[index].strip()
            if not url:
                continue
            match = re.match(r'https://github.com/([^/]+)/([^/]+)/blob/([^/]+)/', url)
            if match and match.group(3) not in ('main', 'master') and version is None:
                version = match.group(3)
            tasks.append({'id': f'{entity_number:02d}-{kind}', 'entity': entity,
                          'role': 'original_policy_verification', 'title': f'{entity}: {kind}',
                          'url': url, 'version': match.group(3) if match else None,
                          'relevant_rqs': ['RQ2', 'RQ3', 'RQ4'],
                          'local_path': f'data/281/policies/{entity}/{kind}.md'})
        if entity in PURPOSE_PAGES:
            url = PURPOSE_PAGES[entity]; title = f'{entity}: official about/mission page'
            version = None
        else:
            assert '/' in entity
            url = f'https://github.com/{entity}/blob/{version or "HEAD"}/README.md'
            title = f'{entity}: repository README'
        tasks.append({'id': f'{entity_number:02d}-purpose', 'entity': entity,
                      'role': 'purpose_statement_candidate', 'title': title,
                      'url': url, 'version': version, 'relevant_rqs': ['RQ1']})
    tasks.extend(EXTRA_SOURCES)
    manifest = HERE / 'source-manifest.json'
    previous = {r['id']: r for r in json.loads(manifest.read_text())} if manifest.exists() else {}
    # Resume collection without changing already downloaded snapshots.
    pending = [t for t in tasks if t['id'] not in previous or previous[t['id']]['status'] == 'unavailable']
    with ThreadPoolExecutor(max_workers=6) as pool:
        previous.update({r['id']: r for r in pool.map(fetch, pending)})
    records = [previous[t['id']] for t in tasks]
    (HERE / 'source-manifest.json').write_text(json.dumps(records, indent=2, ensure_ascii=False) + '\n')
    for record in records:
        print(record['id'], record['status'], record.get('error', ''))
    if records and all(r['status'] == 'unavailable' for r in records):
        raise SystemExit('All fetches failed; check network access before interpreting availability.')


if __name__ == '__main__':
    main()
