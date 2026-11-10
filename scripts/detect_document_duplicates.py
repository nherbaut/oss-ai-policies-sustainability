"""Find exactly equal texts in a QualCoder project, without changing the project."""
import argparse
import sqlite3
import sys

from prefilter_common import (DEFAULT_OUTPUT, DEFAULT_PROJECT, PrefilterError, document_metadata,
                              duplicate_groups, load_corpus, output_directory, write_csv, write_json)


def export_duplicates(project, output_dir):
    documents, excluded = load_corpus(project)
    groups = duplicate_groups(documents)
    output = output_directory(output_dir, project)
    report = dict(version=1, comparison='Exact equality of stored text; SHA-256 of UTF-8, no normalization',
                  documents=len(documents), unique_texts=len(groups),
                  duplicate_groups=[], empty_documents=[], excluded_sources=excluded)
    rows = []
    for sha, members in groups.items():
        representative = members[0]['id']
        if len(members) > 1:
            report['duplicate_groups'].append(dict(sha256=sha, representative_id=representative,
                                                   empty=members[0]['empty'],
                                                   members=[document_metadata(d) for d in members]))
        for doc in members:
            if doc['empty']:
                report['empty_documents'].append(document_metadata(doc))
            rows.append(dict(document_id=doc['id'], entity=doc['entity'], name=doc['name'],
                             paths='; '.join(p.get('path', '') for p in doc['provenance']),
                             sha256=sha, duplicate_group=sha if len(members) > 1 else '',
                             representative_id=representative, occurrences=len(members), empty=doc['empty']))
    rows.sort(key=lambda r: r['document_id'])
    write_json(output / 'duplicates.json', report)
    write_csv(output / 'duplicates.csv', rows,
              ['document_id', 'entity', 'name', 'paths', 'sha256', 'duplicate_group',
               'representative_id', 'occurrences', 'empty'])
    return report


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--project', default=DEFAULT_PROJECT)
    parser.add_argument('--output-dir', default=DEFAULT_OUTPUT)
    args = parser.parse_args()
    try:
        report = export_duplicates(args.project, args.output_dir)
    except (PrefilterError, OSError, sqlite3.Error) as exc:
        parser.exit(2, f'Duplicate detection: {exc}\n')
    print(f'{report["documents"]} documents, {report["unique_texts"]} unique texts, '
          f'{len(report["duplicate_groups"])} duplicate groups, {len(report["empty_documents"])} empty documents.\n'
          f'Reports: {args.output_dir}')


if __name__ == '__main__':
    main()
