"""Preview or explicitly reset QualCoder coding and import the sourced taxonomy.

--apply --reset-coded-data creates a full backup, verifies a separate candidate,
then atomically replaces the database. It never commits or changes Git guards.
"""
import argparse
from contextlib import closing
from copy import deepcopy
from datetime import datetime, timezone
import hashlib
import json
import os
from pathlib import Path
import shutil
import sqlite3
import stat
import sys
import tempfile
import uuid
from zipfile import ZipFile

from merge_qualcoder import MergeError, ensure_closed, read_project
from export_coding_taxonomy import reference_memo

ROOT = Path(__file__).resolve().parents[1]
RESET = ('code_text', 'code_image', 'code_av', 'annotation', 'code_name', 'code_cat')
DIMENSIONS = {
    'Environmental': ('#9CCC65', 'Ressources physiques, énergie, émissions et écosystèmes.'),
    'Technical': ('#90CAF9', 'Évolution, durée de vie, maintenance, complexité et sécurité du logiciel.'),
    'Social': ('#CE93D8', 'Accès, équité, inclusion et effets sur les relations et les communautés.'),
    'Economic': ('#FFCC80', 'Viabilité et répartition des coûts, ressources et valeurs économiques.'),
    'Individual': ('#80CBC4', 'Santé, apprentissage, vie privée, sécurité et capacité d’agir des personnes.'),
}
GUIDE_MARKER = '\n\n[Taxonomy source excerpts]\n'


def sha(path):
    return hashlib.sha256(Path(path).read_bytes()).hexdigest()


def load_taxonomy(path):
    taxonomy = json.loads(Path(path).read_text(encoding='utf-8'))
    if taxonomy.get('version') != 1:
        raise MergeError('Unsupported taxonomy version')
    categories = taxonomy['categories']
    if (len(categories) != 25 or len({c['id'] for c in categories}) != 25
            or len({c['raw_label'] for c in categories}) != 25
            or {c['dimension'] for c in categories} != set(DIMENSIONS)):
        raise MergeError('Expected 25 unique taxonomy categories across five dimensions')
    for code in categories:
        expected = 'provisional_literature_extension' if code['dimension'] == 'Individual' else 'source_authored'
        if code['status'] != expected or not code['operational_definition'] or not code['coding_guidance']:
            raise MergeError('Invalid category status or missing operational guidance')
    archive = ROOT / taxonomy['source_archive']
    if sha(archive) != taxonomy['source_archive_sha256']:
        raise MergeError('The handoff archive differs from the recorded source')
    with ZipFile(archive) as source:
        for name, entry in taxonomy['sources'].items():
            if hashlib.sha256(source.read(entry['archive_member'])).hexdigest() != entry['sha256']:
                raise MergeError(f'Source checksum mismatch: {name}')
    return taxonomy


def global_guide(taxonomy):
    return '\n\n'.join(reference_memo(taxonomy, dimension=d) for d in taxonomy['dimension_excerpts'])


def code_memo(code, taxonomy):
    return reference_memo(taxonomy, code=code)


def expected_data(before, taxonomy, timestamp):
    data = deepcopy(before['data'])
    if any(rows for table, rows in data.items() if table == 'graph' or table.startswith('gr_')):
        raise MergeError('Analytical graphs exist; resolve their code/coding references before resetting the codebook')
    for table in RESET:
        data[table] = []
    owner = data['project'][0]['codername'] or 'Taxonomy import'
    guide = global_guide(taxonomy)
    project = data['project'][0]
    project['memo'] = (project.get('memo') or '').split(GUIDE_MARKER)[0] + GUIDE_MARKER + guide
    project['recently_used_codes'] = None
    for catid, (dimension, (_, description)) in enumerate(DIMENSIONS.items(), 1):
        data['code_cat'].append(dict(catid=catid, name=dimension, owner=owner, date=timestamp,
                                     memo=reference_memo(taxonomy, dimension=dimension), supercatid=None))
    ids = {row['name']: row['catid'] for row in data['code_cat']}
    for cid, code in enumerate(taxonomy['categories'], 1):
        data['code_name'].append(dict(cid=cid, name=code['raw_label'], memo=code_memo(code, taxonomy),
                                     catid=ids[code['dimension']], owner=owner, date=timestamp,
                                     color=DIMENSIONS[code['dimension']][0], supercid=None))
    return data


def check_candidate(snapshot, before, expected):
    if snapshot['schema'] != before['schema'] or snapshot['files'] != before['files']:
        raise MergeError('Schema or project files changed unexpectedly')
    if snapshot['data'] != expected:
        raise MergeError('Candidate database differs from the exact expected reset')


def reset_project(project, taxonomy_path, backup_root, apply=False):
    project = Path(project)
    if project.is_symlink() or (project / 'data.qda').is_symlink():
        raise MergeError('Refusing a symlinked QualCoder project or database')
    project, backup_root = project.resolve(), Path(backup_root).resolve()
    if backup_root.is_relative_to(project):
        raise MergeError('Backup directory must be outside the project')
    if (project.parent.parent / 'coding/codebook.json').exists():
        raise MergeError('A shared UUID codebook registry exists; coordinate its replacement before resetting')
    if project == ROOT / 'data/coding.qda':
        from coding_guards import state
        if state(ROOT).get('active'):
            raise MergeError('An active coding session must be closed before this maintenance reset')
    ensure_closed(project)
    if any((project / f'data.qda{suffix}').exists() for suffix in ('-wal', '-shm', '-journal')):
        raise MergeError('SQLite sidecar files exist; close/checkpoint the project before atomic replacement')
    taxonomy = load_taxonomy(taxonomy_path)
    before = read_project(project)
    timestamp = datetime.now(timezone.utc).strftime('%Y-%m-%d %H:%M:%S')
    expected = expected_data(before, taxonomy, timestamp)
    report = dict(version=1, applied=False, project=str(project), timestamp_utc=timestamp,
                  taxonomy=str(Path(taxonomy_path).resolve()), taxonomy_sha256=sha(taxonomy_path),
                  removed={t: len(before['data'][t]) for t in RESET},
                  imported=dict(dimensions=5, codes=25, source_authored=20, provisional_individual=5),
                  preserved=dict(documents=len(before['data']['source']), cases=len(before['data']['cases'])))
    if not apply:
        return report
    backup_root.mkdir(parents=True, exist_ok=True)
    stamp = datetime.now(timezone.utc).strftime('%Y%m%d-%H%M%S') + '-' + uuid.uuid4().hex[:8]
    backup = backup_root / f'coding-before-taxonomy-reset-{stamp}.qda'
    mode = stat.S_IMODE((project / 'data.qda').stat().st_mode)
    shutil.copytree(project, backup, ignore=shutil.ignore_patterns('data.qda-wal', 'data.qda-shm', 'data.qda-journal'))
    backup_db = backup / 'data.qda'
    backup_db.chmod(mode | stat.S_IWUSR)
    try:
        with closing(sqlite3.connect((project / 'data.qda').as_uri() + '?mode=ro', uri=True)) as source, \
                closing(sqlite3.connect(backup_db)) as saved:
            source.backup(saved)
    finally:
        backup_db.chmod(mode)
    if read_project(backup) != before:
        raise MergeError(f'Project changed during backup; retained backup at {backup}')
    report['backup'] = str(backup)
    with tempfile.TemporaryDirectory(prefix='taxonomy-candidate-') as temporary:
        candidate = Path(temporary) / 'coding.qda'
        shutil.copytree(backup, candidate)
        database = candidate / 'data.qda'
        database.chmod(mode | stat.S_IWUSR)
        with closing(sqlite3.connect(database)) as conn, conn:
            conn.execute('BEGIN IMMEDIATE')
            for table in RESET:
                conn.execute(f'DELETE FROM "{table}"')
            for table in ('code_cat', 'code_name'):
                for row in expected[table]:
                    columns = ','.join(f'"{key}"' for key in row)
                    placeholders = ','.join('?' for _ in row)
                    conn.execute(f'INSERT INTO "{table}" ({columns}) VALUES ({placeholders})', tuple(row.values()))
            conn.execute('UPDATE project SET memo=?,recently_used_codes=?',
                         (expected['project'][0]['memo'], expected['project'][0]['recently_used_codes']))
            if conn.execute('PRAGMA integrity_check').fetchone()[0] != 'ok' or conn.execute('PRAGMA foreign_key_check').fetchall():
                raise MergeError('Candidate SQLite integrity/reference check failed')
        check_candidate(read_project(candidate), before, expected)
        ensure_closed(project)
        if any((project / f'data.qda{suffix}').exists() for suffix in ('-wal', '-shm', '-journal')):
            raise MergeError(f'SQLite sidecars appeared during preparation; backup retained at {backup}')
        if read_project(project) != before:
            raise MergeError(f'Live project changed during preparation; backup retained at {backup}')
        # Publish a verified closed database on the same filesystem, preserving protections.
        fd, staging_name = tempfile.mkstemp(prefix='.taxonomy-reset-', dir=project)
        os.close(fd)
        staging = Path(staging_name)
        try:
            shutil.copy2(database, staging)
            staging.chmod(mode)
            os.replace(staging, project / 'data.qda')
        finally:
            staging.unlink(missing_ok=True)
    check_candidate(read_project(project), before, expected)
    report['applied'] = True
    report['database_after_sha256'] = sha(project / 'data.qda')
    report_path = backup_root / f'coding-before-taxonomy-reset-{stamp}-report.json'
    report_path.write_text(json.dumps(report, indent=2, ensure_ascii=False) + '\n', encoding='utf-8')
    report['report'] = str(report_path)
    return report


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--project', type=Path, default=ROOT / 'data/coding.qda')
    parser.add_argument('--taxonomy', type=Path, default=ROOT / 'coding/taxonomy.json')
    parser.add_argument('--backup-root', type=Path, default=ROOT / 'data/qualcoder-backups')
    parser.add_argument('--apply', action='store_true')
    parser.add_argument('--reset-coded-data', action='store_true')
    args = parser.parse_args()
    if args.apply and not args.reset_coded_data:
        parser.error('--apply requires --reset-coded-data: this deletes all existing coding and annotations')
    try:
        report = reset_project(args.project, args.taxonomy, args.backup_root, args.apply)
    except (MergeError, OSError, ValueError, sqlite3.Error, KeyError) as exc:
        parser.exit(2, f'Taxonomy import stopped: {exc}\n')
    print(json.dumps(report, indent=2, ensure_ascii=False))


if __name__ == '__main__':
    main()
