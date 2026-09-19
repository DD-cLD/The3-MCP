---
id: save-disk-verify-mtime-delta
title: "⛔ RITUAL LAW: a checkpoint is not a checkpoint until the .show file's mtime AND size move — and MA3 stamps ~9h behind shell TZ, so verify by DELTA against sibling files, never by wall clock"
role: programmer
tags: [ma3, saveshow, ritual, v2.4, tourshow]
when_to_load: "After EVERY save, checkpoint or seal — before telling anyone the show is safe, before any surgery that relies on a rollback point, and before reading a .show file's timestamp as a wall clock"
status: active
verified: grandMA3 onPC 2.4.2.2 (Mac), EU tour leg 2026-08
source: "findings/INBOX.md [0819-4cLD] 2026-08-19 (the phantom-checkpoint reckoning) + [0819-5/6cLD], [0822-1cLD], [0826-2/3/4cLD], [0828-1/3cLD] — applied on every seal across the EU leg"
supersedes: []
superseded_by: null
---

**The law, born out of the phantom-checkpoint reckoning** (`saveshow-enumerate-headless-cancel-class`): **the command echo is not the save. The file on disk is the save.**

## The check

1. List the shows directory: `gma3_2.4.2/shared/shows/`.
2. The target `.show` must be the **newest** file there **and** its **mtime and size must both have moved** since the previous listing. A size-only match with an unchanged mtime, or the reverse, is a failed save.
3. **Read the DELTA, not the clock.** MA3's stamps run roughly **nine hours behind the shell timezone** — the absolute time on a freshly written file will look wrong. Compare it against its *sibling* files in the same directory; the newest-relative position is the signal.

## Receipts across the leg

Every seal on the EU tour was taken this way and named in the log: `v1.4` (128.9 MB) · `v1.42` · `v1.43` · `v1.44` · `EXAMPLE_SHOW {FESTIVAL} .36` · `EXAMPLE_SHOW {FESTIVAL} .51` (125 MB) → `.52` → `.53` (125.8 MB, 02:01 skew stamp) · `EXAMPLE_SHOW use fOR bASE v2.2` (129 MB) · `EXAMPLE_SHOW {FESTIVAL} .24` · `EXAMPLE_SHOW {FESTIVAL} .22` · `EXAMPLE_SHOW {FESTIVAL} {STAGE} .22`. Not one of these was reported as sealed on an echo alone.

**Naming pattern (Dave's ruling, [0819-5]):** the file lineage gets a version pattern and cLD's saves extend it — `v1.4x` on the base file, `.NN` on each venue fork. Dave's own hand-saves interleave cleanly with the pattern; per-fork lineages supersede the base pattern inside that fork.

**The habit is also the insurance.** Twice in one day the export-and-verify habit was what made a rollback survivable: a hash-diff proved a reloaded older file already carried the road's colour tweaks (all 81 presets byte-identical), so nothing had to be reconstructed. See `color-consolidation-crowning`.

**Relation:** `saveshow-enumerate-headless-cancel-class` (why the ritual exists) · `saveshow-discipline-and-mcp-tier` (the shows-dir path and the reachability caveat for the tool that lists it) · `operators-eyes-are-the-census-of-record`.

History: none — ruled and immediately made standing, 2026-08-19; applied on every subsequent seal through the end of the EU leg.
