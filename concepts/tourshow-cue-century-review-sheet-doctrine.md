---
id: tourshow-cue-century-review-sheet-doctrine
title: "The cue×century review sheet is the TASTE verification layer machine checks cannot provide — and dropping it once the line got fast is what let the wash defect through"
role: operational-live
tags: [review-gate, qc, process, tourshow]
when_to_load: "Before shipping any song without producing its cue x century review sheet, or when tempted to skip a review step because the build line is running fast — this is a named, mandatory gate, not an optional nicety"
status: active
source: "BACKLOG.md 2026-08-01 [0801-2cLD], 2026-08-03 [0803-1cLD]"
verified: grandMA3 onPC 2.4.2.2 (Mac)
supersedes: []
superseded_by: null
---

**⭐ NEW DELIVERABLE, RULED (Dave) — PER-SONG CUE-TO-CUE SHEET, CENTURIES AS COLUMNS.** One spreadsheet per song: rows = cues in order, columns = the century parts (P1 SPOTS · P2 WASHES · P4 JDC · P5 BEAMS · P6 RIVALE · P7 PLINE · P8 QX40), cells = what that fixture family does at that cue. Purpose, in Dave's words: *"see what fixtures do, what's the next thing that they do, real easy, all in one spot"* and *"it'll be really easy for me to pull out anything that looks anomalous, or that is gonna look weird on stage — I'll know immediately if I see it."*

## Why it matters: the console shows the data, not the SHAPE

Dave: *"if I see them together, it's kinda hard to read it the way the MA has it, but when we lay it on a spreadsheet, I can see it right away."* **MA3's own sheet view makes this hard to read; the console shows the data, it does not show the shape.** The grid is the shape.

**This sheet is a different verification CLASS from everything else in the toolkit.** Census/lint/smith prove COUNTS and DIALECT — they cannot prove a look makes sense. The grid puts the whole song in front of Dave's eye so **TASTE can verify what mechanics cannot.** Exactly the idea-file design/programmer boundary (`idea-file-design-programmer-boundary-doctrine`) applied to review: the machine certifies structure, the designer certifies sense. **It is also the instrument that would have caught the missing-washes defect** — an empty P2 WASHES column against populated neighbours is unmissable on a grid and invisible in a passing census.

**Build note (cheap — the machinery already exists):** every shipped song's export-back census already parses cue -> part -> SR binds; the grid is a pivot of data already being extracted, emitted as xlsx. No new console contact needed for songs already on disk.

## ⛔⛔ The dropped-practice lesson, second instance of the same failure shape

**This review sheet was a practice we dropped once the build line got fast, and that is exactly what let the wash defect through.** Dave: *"We were doing that sheet, and we just started flowing... we get a couple of good ones, hit the turbo boost, and then it bit us."* Ruling: **get back to the basics even though the line is faster** — speed is precisely what makes the basic step feel skippable, and skipping it is what costs.

**Evidence, straight off the staging folders — the curve is unmistakable:** SONG_B (song 2) = **FOUR** sheet revisions (`SOURCE_PHASER_SHEET` v0.1-v0.4) · SONG_C (song 3) = **ONE** (v0.1; its v0.2 sat on the owed-docs list across three consecutive state files and never came back) · SONG_D, SONG_E, SONG_G, SONG_H, SONG_I, SONG_J = **ZERO**. The practice died exactly where the line started shipping whole songs per session. **A carried-forever owed-doc line is the visible fossil of a practice dying** — treat any doc that survives three rehydrations unactioned as a dropped practice, not a backlog item.

**Standing failure mode, now named — "pipeline momentum overrides gate discipline."** Two instances: the SONG_B TC cutover folded into the first import chain (see `tc-cutover-last-and-delete-eats-events-doctrine`, which names it), and this review-sheet drop. Both cost real rework. **This is no longer an incident shape — it is a standing failure mode of a line that works well: the better the line runs, the more expendable its slowest gate looks.**

**The absence-is-invisible corollary:** running two full songs with census + smith + export-back and never producing the review sheet triggered no failure of any kind — no lint fails, no census disagrees, nothing errors. **The absence of a step you have stopped doing is invisible.** That is why it needs to be a NAMED gate in the runbook rather than a habit, and why a dropped practice can only be caught by an inventory of what a build SHOULD emit, never by checking whether the build passed.

## Delivered — first instance (2026-08-03)

**`SONG-J_RECIPES` 1_SOURCE / 2_cLD / 3_MELD** (`generated/staging_song-j_0801/recipe_sheets/`, with a 4-file generator kit). **Pass 1** = the two sides separately, one row per StandardRecipe line. **Pass 2** = Dave's format exactly — alternating {LD}/cLD rows per CUE #, a (Group, Value, MX) triplet per century across P1..P8. **The generator is song-agnostic; the next song is a path change.**

**Join key, proven safe:** join on the **cue NUMBER**, never on position — SONG_J is 46 cues both sides with identical `No` AND `Name`, nameless cue 28 included, and the console renders `7.1` as `'7.001'` on BOTH files so the stripped string matches without normalisation.

**⭐ PREWORK RULING PROPOSED, awaiting Dave's ratify — the recipe-sheet generator serves THREE modes, not one:**
1. **PREWORK** = pass-1 {LD} book + CROSSWALK tab, generated before any build — strictly more than the existing `crosswalk_prep` markdown (per-line rather than summarised, target and century resolved per line so unmapped groups show as blanks, MX signature per POPULATION, figure and colour inventory).
2. **POST-BUILD GATE** = the meld + RECONCILE + MX CROSSWALK (see `reconciliation-identity-per-song-verification-method`).
3. **THIRD MODE, new as of 08-03** = re-pull and re-meld AFTER Dave has worked the file at the desk — the only artifact that shows what he changed and what is left.

Same generator serves all three; only the input paths move. **This 3-mode framework is a proposal, not yet Dave-ratified** — do not treat it as settled process until he confirms.

## Tooling gotcha paid on the generator (2026-08-03)

**`openpyxl` writes formulas with NO cached value** — a rebuilt workbook reads back **blank for every computed cell**, and a formula-ERROR check still reports 0 errors, because blank is not an error. Caught only by verifying computed VALUES against the Python source of truth (same shape as "a clean Import proves nothing below the structure layer"). **Fix adopted:** the build script now runs recalc itself and asserts on the result — never leave recalc to a separate manual step.

**Note — the wash defect itself is an open Dave-owned action item (some songs' wash content landed on a beam target and was then hand-deleted as an apparent duplicate), not yet filed as its own concept: Dave explicitly said not to investigate it this session. It is the motivating incident for this doctrine, not a fact this doctrine's body asserts.**

**Relation:** `reconciliation-identity-per-song-verification-method` (the sibling crosswalk-completeness sheet/check — that one verifies counts-and-causes, this one verifies taste-and-shape). `tourshow-recipe-line-redundancy-taxonomy` (the "delete-thinking-it's-a-duplicate" failure mode directly adjacent to the wash-defect shape). `tc-cutover-last-and-delete-eats-events-doctrine` (the first instance of the "pipeline momentum overrides gate discipline" failure mode this run names as a pattern).
