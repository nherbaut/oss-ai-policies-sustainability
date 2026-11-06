# Readable Markdown in QualCoder

Applied on 2026-11-06: **297 documents cleaned**, **302 unchanged**, and **one
coded document preserved** (Astropy, containing four coded passages). No
conversion failures or unresolved HTML-remnant warnings were reported. The
large size reduction in Jellyfin's overview was reviewed: substantive text is
retained and embedded image payloads are removed. The full backup is
`data/qualcoder-backups/coding-before-markdown-cleanup-20261106-005740-320852.qda`.

`scripts/clean_qualcoder.py` converts HTML-heavy working documents in the existing
QualCoder project into Markdown. Original corpus files remain unchanged. The
converter retains source IDs, names, provenance, case membership, the codebook,
and existing coding. It never imports new documents or recreates removed cases.

The converter uses Pandoc with Beautiful Soup (`beautifulsoup4`, `lxml`) and
`markdown-it-py`. It removes HTML layout, scripts, styles, comments, decorative
SVG markup, and embedded image payloads. Image descriptions and SVG text are
retained. Headings, paragraphs, lists, links, code examples, and ordinary tables
remain readable Markdown. Complex layout tables become paragraphs when necessary
to retain their text. Hidden policy text and navigation text are preserved.

Documents with coding, annotations, audio/video references, partial case links,
or positional bookmarks are skipped. Their text and offsets remain unchanged.
Conversions that lose visible words or produce empty output are rejected and
listed as failures; other documents can still be converted. A large reduction
in file size is flagged for review, since image payloads can dominate file size.

Preview without changing any files:

```sh
python3 -B scripts/clean_qualcoder.py
```

To save a preview report, add `--report /tmp/qualcoder-cleanup-preview.json`.
Close the project in QualCoder before applying:

```sh
python3 -B scripts/clean_qualcoder.py --apply
```

Application creates a full backup under `data/qualcoder-backups/`, updates the
database text and matching project document copies, and adjusts full-document
case-link lengths. It checks the entire database against the backup, allowing
only those intended edits. Exceptions roll back the transaction and restore
changed document copies. After an interrupted process or power failure, restore
the complete backup project rather than mixing database and document versions.

The application report is saved as `qualcoder-cleanup.json` alongside this file.
Source memos record the converter version and original/converted hashes. A
repeat run recognizes these records and leaves already converted sources alone.
Unexpected edits to converted text require review. The document importer also
recognizes this provenance and retains cleaned text and correct case ranges;
it still independently considers new or changed corpus inputs, so a future
import preview can legitimately report unrelated additions.

Verification tests:

```sh
python3 -B -m unittest discover -s scripts/tests -v
```
