---
id: color-consolidation-crowning
title: "⛔ Colour consolidation law: CROWN the current-stage-truth variant into the base slot BEFORE repointing — repoint every reference first, delete LAST, and save before anything. Skipping the crown snaps the whole show to stale base looks."
role: programmer
tags: [ma3, doctrine, presets, color, v2.4, tourshow]
when_to_load: "Before folding a sprawl of per-song preset mints back into one shared version per family — the ORDER is the whole lesson, and the no-crowning variant was executed and rolled back the same day"
status: active
verified: grandMA3 onPC 2.4.2.2 (Mac), EU tour leg 2026-08
source: "findings/INBOX.md [0819-1cLD] (plan + ruling) · [0819-2cLD] (no-crowning run) · [0819-3cLD] (Dave caught it, rollback, crowned re-run) · [0819-5cLD] (colour-phaser recheck) 2026-08-19"
supersedes: []
superseded_by: null
---

## Why consolidate at all

Per-song colour mints make a **changeover impossible**: tuning a venue means touching fifty presets instead of one family. The inherited file already contained the intended workflow — a `COLOR_UPDATE` sequence whose cues touch each base colour — and the per-song mint habit had broken that model. Consolidation restores it. Dave's ruling: **one shared version per colour family**.

## The law, in order

1. **SaveShow first.** "A save is better than being careful."
2. **CROWN** — per family, copy the **current-stage-truth** variant (the one Dave has actually tuned) **into the base slot**. Re-Label afterwards: `Copy Preset /o /nc` carries the **source's Name**.
3. **REPOINT** every reference to the survivors.
4. **VERIFY** zero refs remain to the doomed slots. Test-fire.
5. **DELETE LAST.**
6. **SaveShow.**

## The paid-for proof that step 2 is not optional

Round one ran **as-is, no crowning**, on Dave's go. It was mechanically perfect — **407 recipe lines repointed**, per-slot counts matching the scan exactly, zero remaining refs to all 43 doomed slots, 43 deleted, pool 81 → 39. And it **snapped every song to the inherited base looks**, because the bases still held the *original* programmer's content while the tour's look lived in the mints that had just died into them. Dave saw it immediately — *"didn't see you were using the {LD} colors too — now I understand the crowning"* — reloaded, and the run was done again **crowned**: 12 bases crowned from the highest-live-use variants, then the same 407-line sweep, verify, delete, seal.

**The rollback was survivable only because of the export habit.** A hash-diff of the reloaded older file against the pre-surgery pool export showed **all 81 presets byte-identical** — the road's colour tweaks were already in the older file, and nothing had to be reconstructed. Baseline exports saved the day twice in one day.

**What a census cannot see, and must be flagged:** non-colour desk edits made after the reloaded version was cut (cue timing, position tweaks from show notes) are invisible to any file-side check. Only the operator knows (`operators-eyes-are-the-census-of-record`).

## After the fold

- **Legibility is part of the deliverable.** The survivors were renamed with a `cLD` prefix and later relocated into a contiguous, one-screen working palette with a reserve shelf — safe because references are object-bound (`preset-references-are-object-bound-rename-and-move-safe`). The changeover drill became "walk the working palette."
- **Colour-phasers owe the same fold.** Phasers never bound the colour pool **by reference at all** — but their **baked step content** did owe the consolidation, which no reference scan could see (`reference-scan-blind-spots-guid-and-baked-content`). Dave rebuilt nine on the crowned bases and folded seven; verification then ran 4/4 clean, including a full recipe scan showing **233 distinct phaser slots referenced, all resolving, zero dangling**.

**Relation:** `venue-position-crowning-and-shell` (the same crowning move in the position pool) · `preset-references-are-object-bound-rename-and-move-safe` · `reference-scan-blind-spots-guid-and-baked-content` · `pool-discipline-stock-vs-custom` · `save-disk-verify-mtime-delta`.

History: none — planned, mis-run, rolled back and re-run correctly inside one day, 2026-08-19.
