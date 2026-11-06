# QualCoder document import

Project: `data/coding.qda` (QualCoder 4.0, database schema v17).

Imported **602 substantive documents**, grouped into **281 cases** named exactly as the dataset's project/entity labels. Each source is linked to its case over its entire text. The documents include the extracted policies, contribution/agent guidelines and supplementary official research sources.

The existing rqlite contribution guide was reused, retaining its source ID, name and text. The other 601 sources are new. Identical text within one project is imported once, with all input paths and source references retained in the document memo. Identical policies from different projects remain in their respective project cases.

New document filenames identify the project and document role. Original Markdown/text is retained so excerpts and character offsets can be matched exactly. Source memos record paths, URLs, versions and retrieval dates where available; unknown provenance remains unknown. Existing thematic codes, coded passages, annotations, journals, coder names and project settings are preserved.

Sixteen unusable input/retrieval records were skipped: four empty texts, six path-only stubs, five failed retrieval attempts and one rendering/error page. Available substantive replacements are imported separately. The detailed source/case mapping and exclusions are in [qualcoder-import.json](qualcoder-import.json).

A complete pre-import project backup is stored at:

`data/qualcoder-backups/coding-before-import-20261105-221955-046085.qda`

It can be opened as a separate QualCoder project. Its database contains the original one document and no cases.

Validation checked database integrity, all 602 text/file copies, the 281 cases, all full-document links, absence of orphan or cross-project links, preservation of existing coding/settings, and the original source against the backup. A repeated import preview reports zero changes.

To preview a future import from the repository root:

```sh
python3 -B scripts/import_qualcoder.py
```

To apply it, close the project in QualCoder and run:

```sh
python3 -B scripts/import_qualcoder.py --apply
```

The importer creates another backup before changes and reuses existing documents/case links. It imports documents and cases, not the assessment's provisional thematic coding.
