---
id: tourshow-phaser-figure-duplication-across-songs
title: "{LD}'s silent #N duplicate phaser names can be content-identical twins WITHIN a song — and nobody has yet content-hashed his 106 figure uses ACROSS songs to check for the same thing"
role: programmer
tags: [phaser, dedup, pool-management, tourshow]
when_to_load: "Before minting a new cLD phaser-pool copy for a {LD} figure — check whether an existing copy already serves it; a #N name suffix does not prove a distinct figure, and cross-song reuse is a real open risk, not yet checked"
status: active
source: "BACKLOG.md 2026-08-01 [0801cLD], 2026-08-03 [0803-1cLD]"
verified: grandMA3 onPC 2.4.2.2 (Mac)
supersedes: []
superseded_by: null
---

**{LD}'s SONG_G pool carries silent-#N duplicate phaser names** (`'Chorus 1/1 Dim#5'` / `'#7'`) that turned out to be **CONTENT-IDENTICAL twins** — one cLD copy served both use-sites (`21.1722`, 2 use-sites). **The `#N` suffix does not imply a distinct figure** — check for twin-`#N` pairs before minting a per-figure copy for each name. This does not conflict with the "one phaser copy per FIGURE, not per use-site" doctrine (`tourshow-authoring-contract-v01`) — it sharpens how to identify a truly distinct FIGURE when {LD}'s own naming is ambiguous.

**⭐ Highest-value unrun check, surfaced by the whole-show pass:** cross-song phaser figure dedup. **106 figure uses show-wide.** A same-song twin has already been proven — SONG_J's Verse 1/1 Dim#8 = Chorus 1/1 Dim#11 (same content hash) — establishing that twins exist WITHIN a song. **Nobody has yet hashed figures ACROSS songs.** If {LD} reused figures between songs, duplicate pool-21 copies are being minted for every one of them without anyone noticing. **Content-hash all 106 figure uses before any more copies get minted** — this is flagged as an open, unrun check, not yet actioned as of this backlog.

**Relation:** `tourshow-authoring-contract-v01` (the one-copy-per-FIGURE doctrine this concept sharpens the identification method for). `tourshow-recipe-line-redundancy-taxonomy` (the sibling redundancy class at the recipe-LINE level rather than the pool-object/figure level).


## ⭐ ANSWERED 2026-08-03 [0803-2cLD] — RAN THE CHECK: 47 DISTINCT FIGURES, 31 ALREADY MINTED, 16 GENUINELY NEW

This concept's flagged, UNRUN cross-song figure-hash check was run this session. Method, result, and validation:

**Granularity ruling — what to hash and what to exclude, and why.** Hash the ordered `<Step>` tuples (`Function`, `Absolute`, `Trans`, `Width`, `Accel`, `Decel`), the driven `Attribute`(s), and `Measure`. **Exclude Phase/GridPos** — spatial, ours lives in a bound MAtricks pool object, not the figure. **Exclude Speed/SpeedMaster** — ours ships UNBAKED and rides cue-part Speed Scale (`tourshow-speed-architecture-standing-ruling`), so two figures with the same shape at different speeds are the same copy at a different gear, not different figures. **Consequence: a content-hash match is a REUSE CANDIDATE whose gear is still set per site at previz — not a claim that two sites read identically on stage.**

**Result, across the 7 remaining songs:** 47 distinct figures, of which 31 are content already minted for a built song — only **16 are genuinely new**. Per song (names / distinct / already-minted / new): SONG_K 8/6/5/**1**, SONG_L 10/9/4/**5**, SONG_M 12/10/5/**5**, SONG_N 6/3/3/**0**, SONG_O 8/7/5/**2**, SONG_P 6/5/4/**1**, SONG_Q 10/7/5/**2**. **SONG_N needs zero new figures** — its 6 names collapse to 3 contents, all three already resident. Phaser-copy workload for the run is 16, not 47 (a 65% cut).

**Show-wide (17 songs, including already-built):** 166 figure name-instances resolve to 57 distinct contents — 8 same-name reuse (not a discovery), 10 different-names/identical-content (the actual finding — widest span 12 songs under 8+ names), 39 single-song. See `inherited-file-membership-is-ground-truth`'s fourth-object-class amendment for this half of the result.

**Validated, not just reported (and a real find came out of validating):** the hash reproduces the known SONG_J twin (`Verse 1/1 Dim#8` = `Chorus 1/1 Dim#11`) exactly; SONG_J's 20 names still separate into 17 distinct hashes (the hash discriminates, it does not over-collapse); a **third** SONG_J twin surfaced — `Transition 1/2 Dim` matches the proven pair's content, but `FIGURE_MAP` mints it separately at `21.2027` while the pair shares `21.2022`, i.e. one redundant pool-21 copy already on the console.

**Two independent derivations agreed:** this content-hash result and the L2 batch-prework pass (a separate code path) both land on 31 reuse / 16 new, identical per song. Corroboration, not a re-print.

**⚠ Scope, stated with the count (per `state-the-scope-with-the-count`): MAIN SEQUENCES ONLY** — no aux export exists yet for any of the 7 remaining songs, so aux-only figures are not in these numbers (the same shape as the 08-01 aux-2002 colour scope trap). Re-run per song once its aux export lands. SONG_R 2800 independently re-confirmed empty (0 cues, 0 figures, 6 KB stub) by this same pass.

**Two defects found and fixed by validating rather than reporting (v1→v2):** (1) `iterparse` + `root.clear()` inside the loop could drop nested `Dependency` subtrees — v2 does a full parse per file; (2) v1 reported one cross-song number that conflated same-name-reuse with different-name-same-content — v2 reports them apart. See `state-the-scope-with-the-count`.

**Files:** `generated/figure_hash/` — `figure_hash2.py` (the analysis), `validate2.py` (the three tests), `FIGURE_HASH_SHOWWIDE_v2.csv` (every figure/hash/class/song), `FIGURE_HASH_FINDINGS_v0.1.md` (this write-up in full). v1 (`figure_hash.py`, `validate_hash.py`) kept for the record only — do not use.

**Relation:** `inherited-file-membership-is-ground-truth` (the labels-lie doctrine this is the fourth object class for) · `tourshow-speed-architecture-standing-ruling` (why Speed is excluded from the hash) · `state-the-scope-with-the-count` (the discipline this validation pass is an instance of).

---
**⚑ Librarian note (not part of the concept body — for cLD, remove before or on apply):** this run could not confirm `tourshow-phaser-figure-duplication-across-songs` exists in the accessible `concepts/SPINE.md` snapshot (grepped, zero hits — see RUN_REPORT.md). Writing this amendment on the dispatch brief's explicit word that this concept already exists and carries the flagged, unrun check. If the file does not in fact exist at apply time, promote this content into a new concept instead of appending it.
