---
id: pool21-block-layout-and-copy-source-law
title: "Pool 21 blocks: <century>00-0N = {LD} originals, <century>20+ = cLD per-song — copy-source slots point at OUR templates, never at {LD}'s composites; figure-hash decode counts over-split on serialization prefixes"
role: programmer
tags: [ma3, v2.4, tourshow, pool21, phaser, copy-source, source, tooling]
when_to_load: "Before minting, copying, or re-pointing anything in preset pool 21; when resolving a FIGURES-sheet 'COPY SOURCE KNOWN' name; when reading figure_hash2.py decode counts."
status: active
source: "findings/INBOX.md 2026-08-05 [0805-2cLD] — live console v2.4.2.2 probes + {LD} {FESTIVAL} export reads + Dave rulings"
verified: grandMA3 onPC 2.4.2.2 (Mac)
supersedes: []
superseded_by: null
---
Block layout (live census): **21.<century>00-0N = {LD}'s imported originals**
(unprefixed names, e.g. 2700-2706, 2500-2504) · **21.<century>20+ = cLD-authored
per-song recipes** (`cLD <SONG> <ROLE>`).

The FIGURES sheets' "COPY SOURCE KNOWN" names resolve to {LD} ORIGINALS, not
cLD objects. **Dave ruling (08-05): copy-source slot references must point at OUR
templates** — BUMP←21.58 SINE 1/2 · RAMP←21.53 RAMP UP · FILLS←21.56 TRAPEZE ·
TRAP←21.56 · DIP←21.55 SNAP. **NEVER copy {LD}'s originals into our recipe
slots**: his carry cell-level Selective rows + group DependencyExport —
re-author-don't-re-point doctrine (`recipe-layer-is-fixture-agnostic-doctrine`).
Complements `tourshow-authoring-contract-v01` (every song mints its own copies
at 21.<century>20; cross-song binds outlawed).

Hasher caveat: `figure_hash2.py` over-splits — it hashes raw step strings
INCLUDING the export's `*`/`?` serialization prefixes, so numerically identical
figures split into distinct hashes (Intro Dim fc45c43b vs 17e3a36e are the same
shape). The prefix is a serialization artifact, not semantics — one figure can
carry BOTH prefixed and unprefixed rows. Direction is safe (understates
copy-source availability) but it inflates decode counts in every run table.

History: none — minted 2026-08-05 [0805-2cLD]; live pool-21 census + Dave's copy-source ruling after the copied-source-originals rollback + figure_hash2.py over-split diagnosis.
