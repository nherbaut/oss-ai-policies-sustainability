# Taxonomy provenance

Whenever adding or refining a QualCoder code or category, write its memo in English using only verbatim excerpts from verified references, followed by citations and exact source locations. Store researcher interpretations, operational guidance, rationale and provisional status separately in taxonomy metadata. For inductive additions, use supporting English corpus excerpts with their provenance. When only a category label is verified, quote that label and identify its source rather than inventing a definition.

Cite Becker et al. (2015), `becker2015sustainability`, for the five high-level sustainability dimensions. Cite Roy et al. (2026), `roy2026taxonomy`, for the twenty categories drawn from that taxonomy. Preserve the provisional provenance of the five individual-level categories.

Keep bibliographic records in `refs.bib`, taxonomy metadata in `coding/taxonomy.json`, and live QualCoder memos consistent. After taxonomy changes, run `make coding-taxonomy-export` to regenerate the publication export and the marked taxonomy section in `protocol.md`. Preserve surrounding protocol text and existing coding records.
