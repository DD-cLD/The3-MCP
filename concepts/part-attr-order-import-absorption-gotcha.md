---
id: part-attr-order-import-absorption-gotcha
title: "⛔ Multi-part cue-part attribute ORDER is not free-form on import — SpeedScale out of desk-export order absorbs the cue's first content part into part 0, silently"
role: programmer
tags: [ma3, xml-schema, sequences, recipes, import, v2.4]
when_to_load: "Before hand-authoring or generating ANY multi-part sequence-cue XML for import (parts-per-century or any other multi-part cue shape) — the Part element's attribute order must clone the desk-export order byte-for-byte, especially SpeedScale's position"
status: active
source: "findings/INBOX.md [0731-2cLD] 2026-07-31, SONG_C seq 1210 build (song-c_emit.py); wraps/2026-07-31-song-b-heard-song-c-built.md 'Paid for' §1"
verified: grandMA3 onPC 2.4.2.2 (Mac)
supersedes: []
superseded_by: null
---

**Paid-for lesson (cost one delete+reimport):** a hand-authored multi-part cue's `Part` attributes must follow the **DESK EXPORT ORDER** — `SpeedScale` sits BETWEEN `MAgic` and `Mode`, on EVERY part, including part 0 / OffCue / CueZero.

**Failure mode:** appending `SpeedScale` AFTER `CueInFade` (instead of between `MAgic` and `Mode`) made the MA3 importer **absorb each cue's FIRST content part into part 0** — 33 `StandardRecipe` lines silently moved, part 1 (P1 SPOTS) emptied — while later parts in the same cue survived untouched. Import echoed clean; only a per-part StandardRecipe census against the source sheet caught the miscount.

**Fix / standing emit rule:** clone the golden export's part-attr order **byte-for-byte**. A second census after the reorder confirmed clean with the golden order restored.

**Scope:** this is a MULTI-PART-cue-specific hazard — a single-part golden cannot attest it, because a single-part golden has no second part to absorb into. See `smith-packet-must-stage-multi-part-golden` for the consequence this has for what a smith dispatch packet must stage.

**Relation:** `sequence-xml-ordered-header-law` (existing concept, not staged this run) — same failure family one level up, at the cue-header level: children 1+2 must be OffCue+CueZero or content cue 1 maps INTO OffCue on import. This concept is the equivalent law one level down, at the Part-attribute level. `export-sequence-xml-schema` for the general Part/StandardRecipe export shape this order-law constrains (see this run's `updates/`). `parts-per-century-emit-pattern-and-et-gate` for the sequence architecture this gotcha was paid for while building.
