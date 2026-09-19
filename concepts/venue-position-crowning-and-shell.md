---
id: venue-position-crowning-and-shell
title: "Venue position adaptation (Dave's design): take the venue's position set WHOLE and CROWN it into the tour's slots, then SHELL the tour's own pan ingredient — references are object-bound, so restore = re-crown + reverse the map"
role: programmer
tags: [ma3, doctrine, positions, presets, festival, v2.4, tourshow]
when_to_load: "Before adapting a show to a house rig's positions on a festival changeover — this is the system that replaces pointing fixtures by hand, and it is show-proven with ZERO pre-show rig time"
status: active
verified: grandMA3 onPC 2.4.2.2 (Mac), EU tour leg 2026-08
source: "findings/INBOX.md [0821-1cLD] (Dave's design, correcting a tilt-strip draft) · [0821-2cLD] (crown mapping) · [0822-1cLD] (executed: 7 crowns + 39-ref shell sweep, sealed) · [0822-3cLD] (show result) 2026-08-21→22"
supersedes: []
superseded_by: null
---

## The problem it solves

A festival changeover buys ~25 minutes, of which maybe **five** reach the rig. Washes and spots barely get pointed. Editing cues per venue is impossible; so is re-teaching positions fixture by fixture.

## Dave's design, in four moves

1. **Take the venue's position set WHOLE** — pan *and* tilt. It is a different rig; **their positions are the truth**. Do not synthesise.
2. **CROWN the venue positions into our own preset slots.** One cue ingredient then delivers the full correct position, and **zero cues are edited.**
3. **SILENCE our pan ingredient.** Repoint every cue/recipe reference to our pan presets at **one blank SHELL** (`empty-preset-mint-clear-then-store`). The lines stay, the references stay valid, the touring pan stops arguing with the house rig's geometry.
4. **Leave our pan presets untouched in their slots.** Tour-mode restore = reverse the repoint + re-crown from the baseline export.

## The executed run (receipts)

- **Baseline first:** full pool-2 export (1.3 MB) — **this is the tour restore source** — plus a disk-verified checkpoint.
- **7 crowns:** venue `89→69 · 91→70 · 92→71 · 93→72 · 94→73 · 95→74 · 96→75`, names restored after copy (Copy carries the source's Name).
- **Shell:** `Preset 2.199 'PAN SHELL'` minted empty; **39 references swept** from the three tour pan presets across every main sequence. **The sweep map IS the restore map** and was recorded verbatim, per sequence and per cue.
- **Verify:** zero refs remain to the pan presets; the pan presets themselves intact in their slots; sealed and disk-verified.
- **Result:** the show pointed right with **no rig time at all**. Dave: "Smashed it, with no pre show rig time it was clocked at success."

## Standing notes

- **Record the sweep map as you sweep.** Restore is only exact if the reverse is unambiguous; a per-sequence map resolves same-target ambiguity (the same discipline the venue MX kit needed, `mx-cell-geometry-law`).
- **Full-position shapes carrying old-rig pan can still fight the house.** source-era position presets with pan baked in remained live and referenced — flagged for Dave's eye, with the same shell treatment available in one sweep if they argue.
- **The toggle is the end state:** a FESTIVAL/TOUR macro pair running the saved sweeps in each direction — the same shape the MX kit reached (`venue-adapt-macro-pattern`).

**Relation:** `empty-preset-mint-clear-then-store` · `preset-references-are-object-bound-rename-and-move-safe` (why crowning and shelling are safe) · `color-consolidation-crowning` (the crowning pattern's first home) · `venue-adapt-macro-pattern` · `mm-shell-empty-preset-armor`.

History: none — designed 2026-08-21, executed and show-proven 2026-08-22.
