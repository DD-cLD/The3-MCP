---
id: export-sequence-writes-per-name-files
title: "'Export Sequence 1 Thru \"file\"' fans out ONE FILE PER SEQUENCE named from the sequence's own name — the filename you give is ignored; freshness-filter the batch by mtime to find your run's output"
role: programmer
tags: [ma3, cli, export, v2.4, census, tourshow]
when_to_load: "Before running a range Export Sequence and expecting a single named file, or when a bulk export appears to have produced nothing under the name you asked for — look for a fan-out of name-derived files instead"
status: active
verified: grandMA3 onPC 2.4.2.2 (Mac), EU tour leg 2026-08
source: "findings/INBOX.md [0826-1cLD] 2026-08-26, {FESTIVAL} — T2-gated 190-file export batch, disk-verified"
supersedes: []
superseded_by: null
---

**A range `Export Sequence` does not write the file you name.** `Export Sequence 1 Thru "<filename>"` walks the range and writes **one XML file per sequence**, each named from **that sequence's own name**, into `gma3_library/datapools/sequences/`. The filename argument is consumed and ignored.

**Receipt:** one gated call produced a **190-file batch** in a single run — the whole live sequence pool of the tour file, exported for Mac-side analysis.

## Consequences

- **Do not census by filename.** The output set is discovered by listing the directory, not by opening the name you typed.
- **Freshness-filter by mtime.** The sequences directory accumulates every past export. The way to isolate *this run's* output is an mtime batch window — and per `save-disk-verify-mtime-delta`, read that window as a **delta** against the directory's other files, because MA3's stamps run ~9h behind shell time.
- This is the front half of the standing heavy-audit lane — see `export-plus-python-bulk-lane`.

**Relation:** `export-plus-python-bulk-lane` (what to do with the batch) · `export-sequence-xml-schema` (what is inside each file) · `save-disk-verify-mtime-delta` (the mtime-skew rule) · `preset-range-export-open-ended-only` (the sibling range-export gotcha in the preset pool).

History: none — observed and used the same session, 2026-08-26.
