---
id: phaser-copy-does-not-carry-measure
title: "Copying a phaser preset does NOT carry its Measure — a Copy'd Measure-carrying figure needs Edit Preset -> Measure N -> Update -> ClearAll reapplied by hand"
role: programmer
tags: [ma3, phasers, measure, copy, gotcha, v2.4]
when_to_load: "Before or immediately after Copy'ing any phaser preset that carries a Measure setting (e.g. cloning a template figure into a per-song slot) — and before assuming a clone behaves identically to its source; also before assuming a Measure edit on a RECIPE preset can be verified via export-diff — it cannot, the desk encoder is the only verify lane; use Update /NoConfirmation for the fixup when unattended or bare Update pops a dialog and cancels"
status: verify
source: "SONG_BUILD_RUNBOOK_v0.1.md step 9 [0731cLD]; SONG_A BREATHE figure (21.1021) — desk step queued, not yet executed"
verified: grandMA3 onPC 2.4.2.2 (Mac)
supersedes: []
superseded_by: null
---

A `Copy Preset <src> At <dst>` clones the figure but **does not bring the Measure layer with it**. A copied figure that is supposed to span a bar will run at the template's timing until Measure is set on the copy by hand:

```
Edit Preset <n>
Measure <n>
Update
ClearAll
```

(`Measure` is a first-class CLI layer keyword once a phaser is loaded into the programmer — `phaser-layer-cli-grammar-measure-keyword`. `Update` is mandatory or the edit silently reverts on clear — `recipe-preset-edit-requires-update`. `ClearAll` is the flush that stops the pulled-in values contaminating the next Store — `edit-session-mechanics-and-contamination-risk`.)

**Do not conflate three separate Measure facts:**
- Measure is not readable/settable as a Lua object property, at part or preset level (`measure-not-a-safe-lua-property-part-or-preset`).
- An Edit->Update round-trip rewrites more of the XML than the edited attribute (`phaser-preset-update-after-edit-rewrite-behavior`).
- **This concept:** the Copy operation itself does not carry Measure.

**`status: verify`** — this is on record from the SONG_A build plan, where `cLD SONG_A BREATHE` (21.1021, copied from 21.51 SINE) is queued for exactly this Measure-4 fixup at the desk. The fixup has **not yet been executed and observed**, so the claim is banked from the build reasoning rather than from a completed live round-trip. Confirm on that edit, then flip to active.


## Measure-fixup verify lane: recipe-preset exports carry no Measure attribute — desk encoder is the only verify lane — 2026-07-31 [0731-3cLD]

A SECOND, independent live instance of this concept's mechanism, on SONG_D: `21.1320`
(a phaser copy) needed the identical Measure-4 fixup. Two new operational facts surfaced
doing it:

- **Bare `Update` over an unattended CLI pops a dialog** ("User Canceled Command");
  **`Update /NoConfirmation` echoes OK.** Use the `/NoConfirmation` form for this fixup
  when unattended (same family as `saveshow-discipline-and-mcp-tier`'s SaveShow-dialog
  gotcha).
- **A recipe-preset export carries NO Measure attribute anywhere** — a Measure edit on a
  recipe preset is therefore **NOT export-verifiable**. The desk encoder eyeball is the
  only verify lane. (Contrast `phaser-preset-xml-measure-speed-fixed-point-encoding`, whose
  export-diff verify method is for BAKED phaser presets, which do carry a fixed-point
  Measure attribute — that method does not apply to recipe presets.)
- Measure-4 on `21.1320` was handed to Dave **UNVERIFIED** (no export-verify lane existed);
  Dave's own desk pass then **confirmed `21.1320` Measure=4 at the desk**, closing this
  specific instance live.

**Status: STAYS `verify` (cLD ruling on the librarian's flip proposal).** Tonight's 21.1320 was a file-side IMPORT clone of template 58 — a template that never carried a Measure — so this instance does NOT test the claim that a console `Copy` DROPS a Measure the source had. The CLI fixup chain's own commit was export-unverifiable; Dave set Measure 4 at the desk. The original verify condition (confirm on a real Copy'd, Measure-carrying figure, e.g. 21.1021 SONG_A BREATHE) is still open.


## Scope gap noted 2026-08-01 [0801cLD] — the verified case does not test whether Copy DROPS a source Measure

**Still genuinely open, despite this concept's status having been flipped to `active`:** the SONG_D case that motivated the flip (`21.1720`, Dave-confirmed Measure=4 at the encoder) is itself a Copy of template `21.51`, which carries **NO** Measure of its own — the same shape as the earlier `21.1320` case. **Neither confirmed case actually tests whether `Copy` DROPS a Measure the SOURCE object had** — both source objects were already Measure-less, so a Measure appearing (or not) after the copy says nothing about whether Copy preserves an existing one.

**The test is now cheap, unlike when this concept was first written:** `21.1720` is the first cLD-authored preset on file that DOES carry a Measure. `Copy 21.1720` to a scratch slot, then one encoder read, closes the open question either way — cheaper than waiting for another natural case to arise.

## ⚑ PROCESS CAUTION — check the song's own data before asserting a fixup is owed, 2026-08-05 [0805cLD]

**cLD wrongly asserted "Measure fixup owed on all four copies" for SONG_L**, purely as a
reflex from this concept's rule, WITHOUT checking the song's own figure data. SONG_L
carries **zero** Measure on any of its figures (see `measure-attribute-show-wide-census`), so
nothing was owed — withdrawn. **A standing caution from this concept is not itself a finding
for a specific song — confirm the source actually carries a Measure before invoking the
fixup.** Same shape as the "loaded is not applied" theme: having this rule on file does not
mean it fires correctly without being checked against the case at hand.

**[0805-2cLD] EXTENSION — copy also does not rewrite steps:** a copied template keeps its parent's steps. A new shape (SONG_O's DIP 70/w5/t0 → 20/w100/t60 from SNAP) needs a hand Phaser-Editor edit after copy — same lane as Measure-after-copy.

History: extended 2026-08-05 [0805-2cLD] — copy semantics widened: steps not rewritten either; new shapes take a hand Phaser-Editor edit post-copy, same lane as Measure.
