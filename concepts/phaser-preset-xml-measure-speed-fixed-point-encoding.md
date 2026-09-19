---
id: phaser-preset-xml-measure-speed-fixed-point-encoding
title: "Baked-phaser preset XML: Measure and Speed are 2^24 fixed-point ints — stored = value × 16777216; 16777216 alone = literal 1 (default), not a None sentinel"
role: programmer
tags: [ma3, recipes, xml-schema, v2.4, measures]
when_to_load: "Before reading or hand-authoring a baked-phaser preset's Measure or Speed attribute values in exported/imported XML — the fixed-point encoding, ground-truthed by export-diff"
status: active
source: "findings/INBOX.md, 2026-07-17 [0717-2cLD], export-diff ground truth (Edit→Measure 2→Update→re-export diff)"
verified: grandMA3 onPC 2.4.2.2 (Mac)
supersedes: []
superseded_by: null
---

**Pinned encoding (export-diff ground truth, zero guessing):** in a baked-phaser preset's XML, the `Measure` and `Speed` attributes are **2^24 fixed-point integers**: `stored = value × 16777216`.

- `Measure 2` at the CLI/encoder → XML value **`33554432`** (2 × 16777216).
- The ubiquitous **`16777216`** seen on default/untouched entries is **literal `1`** (the default value), **NOT** a "None"/unset sentinel — this **corrects an earlier reading** that treated 16777216 as a default/none marker.

**Method (repeatable for future fixed-point questions):** `Edit Preset x` → set the value on the console (`Measure 2`) → `Update` → re-export the preset → diff against the pre-edit export. This ground-truths encoding without guessing at the math.

Cross-reference: `recipe-xml-schema` for the sibling **recipe**-dialect XML shape (display-string phase values, not fixed-point ints — the two dialects diverge here); `measure-layer-math` for what a Measure value means musically at runtime (this concept only covers its on-disk encoding); `phaser-preset-update-after-edit-rewrite-behavior` for what else changes in the XML when an Edit→Update round-trip happens.

**Second data point, corroborated 2026-07-21:** the `cLD SONG_G BREATHE` phaser preset (`21.123`, Measure 4 = one bar) encoded as `Measure="67108864"` — exactly `4 × 16777216`, confirming the `stored = value × 16777216` formula on a second concrete value (the first was `Measure 2 → 33554432`, 2026-07-17). See `baked-phaser-preset-xml-schema` for the full worked breathe-preset example this value comes from.

History: created 2026-07-17, correcting an earlier same-session reading that had flagged the 16777216 sentinel as [VERIFY]/possibly-None — resolved via export-diff. Extended 2026-07-21: second data point corroborates the formula — Measure 4 (one bar) = 67108864, from the cLD SONG_G BREATHE phaser preset build.
