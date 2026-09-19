---
id: tourshow-dimmer-preset-ladder
title: "Dimmer preset ladder is fully mapped and CLOSED: Full=1.5 · 75=1.7 · 50=1.9 · 30=1.10 · 20=1.11 · 10=1.13 · 0=1.15 — descending, and NOT contiguous"
role: programmer
tags: [tourshow, dimmer, presets, slots, stock-library, v2.4]
when_to_load: "Before referencing any dimmer-level preset by slot in a recipe bind or authored XML — numeric preset NAMES parse as slot indexes, so these must be addressed by the slot numbers below, never by typing the numeral as a name"
status: active
source: "live console read 2026-07-31 [0731cLD] on EXAMPLE_SHOW gov bal_cLD; closes the open ruling in tourshow-crosswalk-prework-alias-gap"
verified: grandMA3 onPC 2.4.2.2 (Mac)
supersedes: []
superseded_by: null
---

Read live off pool 1 on 2026-07-31:

| Level | Slot |
|---|---|
| Full | **1.5** |
| 75 | **1.7** |
| 50 | **1.9** |
| 30 | **1.10** |
| 20 | **1.11** |
| 10 | **1.13** |
| 0 | **1.15** |

**Descending, with gaps** — the slot number does not encode the level and the spacing is irregular. Do not extrapolate a missing rung; read it.

**This closes the standing "Dimmer '20'/'30' slots" ruling** carried as owed in `tourshow-crosswalk-prework-alias-gap` and flagged UNKNOWN in `CROSSWALK_CHEAT_SHEET_v0.1.md`. It needed a console read, not a Dave decision — worth noting as a class: some "owed rulings" are just unread facts, and sorting those out of the queue is cheap.

**Why slot-addressing is mandatory here:** several of these presets are *named* bare numerals, and a numeric name in a `Preset=`/`Values=` bind path **parses as a SLOT INDEX, not a name** — so `Dimmer.0` resolves to slot 0 (nil), not to the preset named "0". See `import-resolver-laws`.
