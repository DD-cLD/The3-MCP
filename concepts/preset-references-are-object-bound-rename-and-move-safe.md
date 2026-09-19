---
id: preset-references-are-object-bound-rename-and-move-safe
title: "References are OBJECT-bound, not slot- or name-bound: renaming a preset and MOVING it to another slot both leave every reference intact and re-rendering to the new address"
role: programmer
tags: [ma3, presets, pool, references, v2.4, tourshow]
when_to_load: "Before reorganising a pool mid-show-run — renames and Move Preset At are safe for referenced objects; the risk is elsewhere (hand-typed slot numbers, name-lookup scripts, baked content)"
status: active
verified: grandMA3 onPC 2.4.2.2 (Mac), EU tour leg 2026-08
source: "findings/INBOX.md [0819-4cLD] (renames, Dave's point confirmed live) and [0819-6cLD] (ten Move Preset relocations, zero dead refs) 2026-08-19"
supersedes: []
superseded_by: null
---

**Proven both directions on a live tour file:**

- **Rename.** The twelve crowned colour bases were renamed to `cLD <colour>`; a repointed reference still rendered `Preset 4.18` afterwards. **Renames do not break references.**
- **Move.** Ten `Move Preset … At …` relocations (e.g. `68→26`, `65→29`, `51→34`, `83→38`) — **references followed the move**, proven by a song's `SUNSET EDGE` reference re-rendering as `Preset 4.29`. Post-move sweep: **zero dead colour refs**.

**Because the binding is to the object, not to its address or its label.** The same family of truth as the `&apos;`-quoting scope finding (`import-resolver-laws`) and the golden exports that survive stale pool names on GUIDs.

## What this makes safe, and what it does not

**Safe:** pool reorganisation for human legibility. The colour pool went from 81 scattered presets to a contiguous, one-screen working palette with a reserve shelf, mid-tour, with no cue edits — the changeover drill became "walk slots 1-22".

**Not safe:**
- **Hand-typed slot numbers.** Anything a human addressed by slot from muscle memory misses after a move. Dave's own note when utilities moved upstairs: recipes ride the objects fine, fingers do not.
- **Name-lookup scripts.** A rename retargets every by-name resolution — including a macro's own mint-if-missing lookup (`matricks-property-clear-encoding`).
- **Baked content.** Anything that *contains* a value rather than *referring* to one is invisible to a reference scan and unaffected by moves — see `reference-scan-blind-spots-guid-and-baked-content`.

**Relation:** `color-consolidation-crowning` (the surgery this made possible) · `reference-scan-blind-spots-guid-and-baked-content` · `pool-labeling-doctrine-inherited-risk` · `import-resolver-laws`.

History: none — rename behaviour confirmed 2026-08-19, move behaviour proven the same day across ten relocations.
