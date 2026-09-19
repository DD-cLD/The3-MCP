---
id: venue-adapt-macro-pattern
title: "The venue-adaptation kit: mint-if-missing + repoint as a TWO-LINE MACRO, its exact reverse as a twin, the masters treatment as a third — hand surgery at the first venue, one tap by the last"
role: programmer
tags: [ma3, macro, doctrine, festival, kit, v2.4, tourshow]
when_to_load: "When the same desk surgery is about to be performed at a second venue — that is the moment it becomes a macro pair, not the fourth time; also the reference for what a re-runnable adaptation artifact must contain"
status: active
verified: grandMA3 onPC 2.4.2.2 (Mac), EU tour leg 2026-08
source: "findings/INBOX.md [0826-4cLD] (MASTERS TX) · [0828-2cLD] (kit staged) · [0828-3cLD] (maiden run) 2026-08-26→28"
supersedes: []
superseded_by: null
---

## The arc

The same adaptation was performed four times in one week. Venue one was **hand surgery over the wire**. Venue four was **one macro tap**. The kit that closed that gap:

| Macro | Job |
|---|---|
| `cLD MASTERS TX` | the masters migration sweep — one Lua line wrapping the generalised repoint, Printf reports the count. Re-fireable on **any future file**. |
| `cLD MX 1CELL` | two lines: **mint-if-missing** the flat twins (sources looked up **by name**, not slot) + **repoint** the known cell-geometry lines, per-sequence maps, plate and tube families scoped, Printf counts. |
| `cLD MX RESTORE` | the **exact reverse**, per-sequence so same-target ambiguity resolves. |

## What makes an adaptation artifact trustworthy

- **Mint-if-missing, by name.** Slot contents differ between file lineages; a source that exists in one fork may be absent in another and have to be minted from a different parent. Name lookup plus mint-if-missing survives both.
- **Per-sequence maps in both directions.** Several sources collapse onto one twin, so the reverse is only exact if it is written per sequence.
- **Printf the counts.** A macro that reports "14" when the map says 19 is what caught the label race (`macro-lua-label-race-needs-wait`); a macro that only reports success would have shipped a partial adaptation.
- **A `Wait` between a name-producing line and a name-consuming one.** Learned the hard way on the maiden run; the pool artifact is patched and future-proof.
- **XMLs live in `gma3_library/datapools/macros/`** and are staged import-ready before the file that needs them exists. Import with quoted filenames (`import-file-argument-must-be-quoted`).

## The decision tree the kit serves

When a new venue's plot lands:

- **1-cell strobes/blinders** → tap `MX 1CELL`, done.
- **Real multicell matching the build number** → the file needs **nothing**.
- **Different multicell count** (e.g. 14-cell plates) → mint block twins at the new number and repoint, per `mx-cell-geometry-law`.
- **Odd counts** → census first (`selection-count-probe`), then the same doctrine.
- **Masters treatment** inherits from the base file in any fork; re-fire `MASTERS TX` if the lineage predates it.

**Dave's method law behind all of it:** many-line desk batches ride better as **macro or script artifacts** than as long Lua chains — deliver desk-native and re-runnable wherever a batch repeats (`many-lines-ride-macros-not-lua`).

**Relation:** `mx-cell-geometry-law` · `many-lines-ride-macros-not-lua` · `macro-lua-label-race-needs-wait` · `venue-position-crowning-and-shell` (the position half of the kit) · `macro-ization-doctrine` · `import-file-argument-must-be-quoted`.

History: none — assembled across the last week of the EU leg, 2026-08-26 → 2026-08-28, and proven on its maiden run at the final show.
