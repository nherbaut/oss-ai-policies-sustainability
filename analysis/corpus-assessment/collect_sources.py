"""Resume official purpose-source collection and repair missing policy retrievals.

Downloads supplementary material only; does not change the source corpus or CSV.
Run from the repository root. Requires Pandoc for HTML and RST conversion.
"""
import csv
import hashlib
import json
import re
import subprocess
import posixpath
from concurrent.futures import ThreadPoolExecutor, as_completed
from datetime import datetime, timezone
from pathlib import Path
from urllib.error import HTTPError
from urllib.request import Request, urlopen

HERE = Path(__file__).resolve().parent
ROOT = HERE.parents[1]
DATASET = ROOT / 'data/281/dataset1-multiple-ai-policies.csv'
MANIFEST = HERE / 'source-manifest.json'
ABOUT = {
    'Kubernetes': 'https://kubernetes.io/', 'Jellyfin': 'https://jellyfin.org/',
    'NLnet': 'https://nlnet.nl/foundation/', 'OpenInfra Foundation': 'https://openinfra.org/about/',
    'Linux Kernel': 'https://github.com/torvalds/linux/blob/master/README',
    'OpenSSL': 'https://openssl-library.org/about/',
    'PROJ (OSGeo)': 'https://github.com/OSGeo/PROJ/blob/master/README.md',
    'LLVM': 'https://llvm.org/', 'NLnet Labs': 'https://nlnetlabs.nl/about/',
    'pip-tools': 'https://github.com/jazzband/pip-tools/blob/main/README.md',
    'Matplotlib': 'https://matplotlib.org/stable/project/mission.html',
    'Astropy': 'https://www.astropy.org/about.html',
    'Oxide Computer (RFD 576)': 'https://oxide.computer/company',
    'Castle Game Engine': 'https://castle-engine.io/',
    'Python (devguide)': 'https://www.python.org/psf/mission/',
    'python-attrs': 'https://github.com/python-attrs/attrs/blob/main/README.md',
    'scikit-learn': 'https://scikit-learn.org/stable/about.html',
    'Apache Software Foundation': 'https://www.apache.org/foundation/',
    'Godot': 'https://godotengine.org/', 'Servo': 'https://servo.org/',
    'Teamtype': 'https://github.com/teamtype/teamtype/blob/main/README.md',
    'Zig': 'https://ziglang.org/', 'Gentoo': 'https://www.gentoo.org/get-started/about/',
    'KDE (page GSoC)': 'https://kde.org/community/whatiskde/',
    'Flathub': 'https://flathub.org/about',
    'FastAPI': 'https://github.com/fastapi/fastapi/blob/master/README.md',
    'QEMU': 'https://www.qemu.org/', 'OpenJDK': 'https://openjdk.org/',
    'AFNix': 'https://www.afnix.fr/', 'Linux Foundation': 'https://www.linuxfoundation.org/about',
}
FOLLOWUPS = [
    ('085', 'dolphin-emu/dolphin', 'purpose_statement_candidate', 'https://dolphin-emu.org/docs/faq/'),
    ('107', 'Oxide Computer (RFD 576)', 'purpose_statement_candidate', 'https://oxide.computer/'),
    ('182', 'Godot', 'supplementary_policy', 'https://contributing.godotengine.org/en/latest/development/contribution_rules.html#ai-assisted-contributions'),
    ('228', 'm2team/nanazip', 'purpose_statement_candidate', 'https://github.com/m2team/nanazip/blob/7551b164cb178f1b5b14e01969e5d16215bce275/ReadMe.md'),
    ('274', 'AFNix', 'purpose_statement_candidate', 'https://afnix.fr/'),
    ('196', 'Servo', 'supplementary_policy', 'https://book.servo.org/policy/ai-usage.html'),
    ('039', 'Linux Kernel', 'supplementary_policy', 'https://github.com/torvalds/linux/blob/master/Documentation/process/generated-content.rst'),
    ('037', 'NLnet', 'supplementary_policy', 'https://nlnet.nl/foundation/policies/generativeAI/2.0/'),
    ('016', 'diesel-rs/diesel', 'supplementary_policy', 'https://nlnet.nl/foundation/policies/generativeAI/2.0/'),
    ('121', 'directus/directus', 'purpose_statement_candidate', 'https://github.com/directus/directus/blob/240b801568b4cd99676dc69adc22682800215654/directus/readme.md'),
    ('137', 'biomejs/biome', 'purpose_statement_candidate', 'https://github.com/biomejs/biome/blob/b3b12b3fe390feabbd9ba097922d6c7e56823406/packages/@biomejs/biome/README.md'),
    ('100', 'caldis/mos', 'purpose_statement_candidate', 'https://github.com/caldis/mos/blob/5dfb2363331cf63f529fdafa27962c41f91feff4/README.enUS.md'),
]


def now(): return datetime.now(timezone.utc).isoformat()


def raw_url(url):
    return re.sub(r'^https://github.com/([^/]+)/([^/]+)/blob/', r'https://raw.githubusercontent.com/\1/\2/', url)


def fetch(task):
    record = dict(task, accessed_at=now())
    nlnet_url = 'https://nlnet.nl/foundation/policies/generativeAI/2.0/'
    shared_policy = 'data/281/policies/diesel-rs/diesel/other_policy.md'
    if task['url'].rstrip('/') in (nlnet_url.rstrip('/'), nlnet_url.rsplit('/2.0/', 1)[0]):
        data = (ROOT / shared_policy).read_bytes()
        if not data.strip():
            raise ValueError('Shared NLnet policy is empty: ' + shared_policy)
        record.update(url=nlnet_url, resolved_url=nlnet_url, version='2.0',
                      status='downloaded', snapshot=shared_policy,
                      raw_snapshot=shared_policy, sha256=hashlib.sha256(data).hexdigest(),
                      attempts=[], notes='Shared foundation policy retained under Diesel; reused across project associations.')
        return record
    attempts = []
    candidates = task.get('candidate_urls', [task['url']])
    for url in candidates:
        try:
            req = Request(raw_url(url), headers={'User-Agent': 'OSS sustainability research source collection'})
            with urlopen(req, timeout=30) as response:
                data = response.read(); media = response.headers.get_content_type()
                record['resolved_url'] = response.geturl()
            record['url'] = url
            is_html = media == 'text/html' or data.lstrip().lower().startswith(b'<!doctype html')
            is_rst = url.split('?', 1)[0].endswith('.rst')
            dest = HERE / 'sources' / record['id']
            raw = dest.with_suffix('.html' if is_html else '.rst' if is_rst else '.raw.md')
            raw.write_bytes(data)
            if is_html or is_rst:
                text = subprocess.run(['pandoc', '-f', 'html' if is_html else 'rst', '-t', 'gfm', '--wrap=none'],
                                      input=data, capture_output=True, check=True).stdout.decode()
            else:
                text = data.decode('utf-8-sig')
            dest.with_suffix('.md').write_text(text)
            record.update(status='downloaded', snapshot=str(dest.with_suffix('.md').relative_to(ROOT)),
                          raw_snapshot=str(raw.relative_to(ROOT)), sha256=hashlib.sha256(data).hexdigest())
            if re.search(r'Cookie monster!|Making sure you.re not a bot|Access Denied|Just a moment\.\.\.|Checking your browser|Enable JavaScript and cookies to continue', text, re.I):
                record['status'] = 'possible_bot_challenge'
            record['attempts'] = attempts
            return record
        except Exception as exc:
            attempts.append({'url': url, 'error': f'{type(exc).__name__}: {exc}', 'accessed_at': now()})
            if not isinstance(exc, HTTPError) or exc.code != 404:
                break
    record.update(status='unavailable', attempts=attempts)
    return record


def tasks_and_reuse():
    with DATASET.open(newline='', encoding='utf-8-sig') as f: table = list(csv.reader(f))
    pilot = json.loads((ROOT / 'analysis/feasibility-pilot/source-manifest.json').read_text())
    tasks, reused = [], []
    for n, row in enumerate(table[1:], 1):
        entity = row[0]
        purposes = [s for s in pilot if s['entity'] == entity and s['role'] == 'purpose_statement_candidate'
                    and s['status'] == 'downloaded' and s['id'] != '06-purpose']
        if purposes:
            for source in purposes:
                reused.append(dict(source, reused_from_pilot=True))
        else:
            version = None
            for cell in (row[9], row[10], row[11], row[13]):
                m = re.search(r'https://github.com/([^/]+/[^/]+)/blob/([^/]+)/', cell)
                if m and m[1].lower() == entity.lower():
                    version = m[2]; break
            if entity in ABOUT:
                url = ABOUT[entity]; candidates = [url]
            elif '/' in entity:
                base = f'https://github.com/{entity}/blob/{version or "HEAD"}/'
                candidates = [base + name for name in ('README.md', 'README.rst', 'readme.md', 'README')]
                url = candidates[0]
            else:
                raise ValueError(f'No official purpose source configured for {entity}')
            tasks.append({'id': f'corpus-{n:03d}-purpose', 'entity': entity,
                          'role': 'purpose_statement_candidate', 'title': entity + ': official purpose/README candidate',
                          'url': url, 'candidate_urls': candidates, 'version': version,
                          'relevant_rqs': ['RQ1']})
        # Fetch each actual URL separately when a source cell contains several URLs.
        for index, kind in [(9, 'ai_policy'), (10, 'contributing'), (11, 'agent'), (13, 'other_policy')]:
            existing = ROOT / 'data/281/policies' / entity / (kind + '.md')
            stub = existing.read_text().strip() if existing.is_file() else ''
            is_stub = bool(re.fullmatch(r'[.\w/-]+\.(md|rst)', stub))
            if existing.is_file() and stub and not is_stub: continue
            for j, url in enumerate(re.findall(r'https?://[^\s]+', row[index]), 1):
                url = url.rstrip('),')
                original_url = url
                if is_stub:
                    link = re.match(r'(https://github.com/[^/]+/[^/]+/blob/[^/]+/)(.+)',url)
                    if link:
                        url = link[1] + posixpath.normpath(posixpath.join(posixpath.dirname(link[2]),stub))
                m = re.search(r'/blob/([^/]+)/', url)
                tasks.append({'id': f'corpus-{n:03d}-{kind}-{j}', 'entity': entity,
                              'role': 'supplementary_policy', 'title': f'{entity}: missing {kind} source {j}',
                              'url': url, 'version': m[1] if m else None,
                              'original_stub_url': original_url if is_stub else None,
                              'relevant_rqs': ['RQ2', 'RQ3', 'RQ4']})
    # Framework and actual EFF rules were reviewed in the pilot; preserve those sources.
    reused.extend(s for s in pilot if s['id'] in ('01-ethical-principles', '03-contribution-rules'))
    for number, entity, role, url in FOLLOWUPS:
        tasks.append({'id': f'corpus-{number}-followup', 'entity': entity, 'role': role,
                      'title': entity + ': official follow-up after failed source retrieval',
                      'url': url, 'version': re.search(r'/blob/([^/]+)/',url)[1] if re.search(r'/blob/([^/]+)/',url) else None,
                      'relevant_rqs': ['RQ1'] if role == 'purpose_statement_candidate' else ['RQ2','RQ3','RQ4']})
    return tasks, reused


def main():
    (HERE / 'sources').mkdir(exist_ok=True)
    tasks, reused = tasks_and_reuse()
    saved = {s['id']: s for s in json.loads(MANIFEST.read_text())} if MANIFEST.exists() else {}
    saved.update({s['id']: s for s in reused})
    for task in tasks:
        if task['id'] in saved and task.get('version') and not saved[task['id']].get('version'):
            saved[task['id']]['version']=task['version']
    pending = [t for t in tasks if t['id'] not in saved or
               (saved[t['id']]['status'] == 'unavailable' and any(
                   'Name or service not known' in a.get('error', '') for a in saved[t['id']].get('attempts', [])))]
    with ThreadPoolExecutor(max_workers=8) as pool:
        futures = [pool.submit(fetch, task) for task in pending]
        for count, future in enumerate(as_completed(futures), 1):
            source = future.result(); saved[source['id']] = source
            MANIFEST.write_text(json.dumps(sorted(saved.values(), key=lambda s:s['id']), indent=2, ensure_ascii=False) + '\n')
            if count % 20 == 0 or source['status'] != 'downloaded':
                print(f'{count}/{len(pending)} {source["id"]}: {source["status"]}', flush=True)
    MANIFEST.write_text(json.dumps(sorted(saved.values(), key=lambda s:s['id']), indent=2, ensure_ascii=False) + '\n')
    from collections import Counter
    print(dict(Counter(s['status'] for s in saved.values())), flush=True)


if __name__ == '__main__': main()
