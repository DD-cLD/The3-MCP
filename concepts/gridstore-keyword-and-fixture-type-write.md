---
id: gridstore-keyword-and-fixture-type-write
title: "`GS` (GridStore) bakes the current selection-grid sub-layout INTO THE FIXTURE TYPE — every instance of that type inherits it on Down"
role: programmer
tags: [ma3, cli, gs, subfixture, v2.4]
when_to_load: "Before using GS to save a subfixture grid layout, or when deciding whether a layout needs to live on the fixture TYPE (GS) vs. a single Group (bake-at-Store) — see `gs-multifixture-recall-unreliable` before relying on GS for a multi-fixture build"
status: active
source: "findings/INBOX.md, 2026-07-15, console live 2.4.2.2"
verified: grandMA3 onPC 2.4.2.2 (Mac)
supersedes: []
superseded_by: null
---

**`GS` = short form of the `GridStore` keyword** (confirmed live, 2.4.2.2).

**What it does:** lay out subs on the selection grid (Grid-cursor moves + sub-range selections, per `grid-cursor-cli-recipe-for-2d-group-layouts` / `subfixture-thru-range-syntax`), then fire `GS`. A popup appears, verbatim:

> "Do you want to store the grid positions into the fixture type?" — OK / Cancel

Choosing OK writes the current programmer sub-layout **into the fixture TYPE itself**, not just the selected instances — every fixture of that type inherits the stored layout from then on.

**Propagation confirmed:** after `GS`, selecting the parent fixtures and expanding with `Down` (e.g. `Fixture 301 Thru 312 ; Down`) propagates the stored layout **tiled side-by-side per fixture** — worked example, 12 ACMEs (301–312) → 576 subs laid out as 12 blocks of 16 columns × 3 rows each (equivalently, 192 total columns × 3 rows).

**Typing caveat:** `ShCuts` (console keyboard shortcuts) must be **OFF** to type `GS` in the docked command line — otherwise the two letters risk being intercepted as a shortcut. The Edit Command popup lane is unaffected by this.

**Relationship to other layout-storage lanes:** GS writes to the fixture TYPE (all instances, always-on inheritance via Down). This is a different, stronger-reaching mechanism than baking a layout into a single Group at `Store` time (per-instance, only that Group) — see `grid-cursor-cli-recipe-for-2d-group-layouts`. **Before relying on GS for anything beyond a single fixture, read `gs-multifixture-recall-unreliable`** — multi-fixture Down-recall of a GS-stored layout is not always faithful.

**Not durable across a repatch (2026-07-21):** a GS type-bake does NOT survive a fixture-type repatch. The 2026-07-15 GS bake of the ACME 16-col × 3-row color/beam/color sandwich was **gone** in cLD_SANDBOX_v0.23 — probing `ClearAll ; Fixture 301 ; Down ; Store scratch ; Export` returned all 48 subs stacked at X=0,Y=0 (default parent-cell stacking), i.e. the type had reverted. Most likely the v11 repatch re-imported/reset the ACME FixtureType 4. **Consequence:** GS is not a durable carrier — build the layout FRESH via Grid-cursor baked into Groups (the reliable per-Group lane, see `gs-multifixture-recall-unreliable`). This is a second, independent reason — on top of nondeterministic multi-fixture recall — to prefer Groups over GS for anything that must persist.

History: none — GS keyword, popup text, and single-fixture-type propagation confirmed live in one session, 2026-07-15 (Dave's drill). Extended 2026-07-21: the 2026-07-15 type-bake was found wiped after the v11 repatch — GS bakes are not durable across a repatch.
