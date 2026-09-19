---
id: state-the-scope-with-the-count
title: "State the scope with the count — a bare number is not checkable, and the mistake shape recurs at every new count"
role: operational-live
tags: [verification, crosscheck, methodology, tourshow]
when_to_load: "Before reporting, shipping, or acting on ANY headline count or workload number this project produces — recipe counts, figure counts, backlog/INBOX line counts, correction-surface counts. Read this before trusting your own first-pass tally, and before repeating a count you did not personally recompute."
status: active
source: "BACKLOG_pass2.md [0803-2cLD], lines 3, 9, 17, 2026-08-03"
verified: grandMA3 onPC 2.4.2.2 (Mac)
supersedes: []
superseded_by: null
---

**The discipline: state the scope with the count, always.** A bare number ("122", "47 figures", "~85 INBOX lines") is not checkable by anyone reading it later — what was counted, what was deliberately excluded, and why, has to travel with the number or the count silently rots into an unverifiable claim the moment a later session repeats it without rechecking.

**The same mistake shape recurs — it is not learned once, it needs re-applying at every new count.** This session alone produced two further self-caught instances (the source material labels the first of these its own **third instance** of the pattern, implying at least two earlier instances already exist in the corpus — not independently re-sourced by this run; see Relation):

1. **Same-name-reuse conflated with different-name-same-content.** v1 of the cross-song phaser figure-hash reported ONE cross-song number that silently mixed "{LD} reused one object under one name across songs" (not a discovery — already treated as one figure) with "DIFFERENT names, IDENTICAL content" (the actual finding). Caught by validating the output rather than just reporting it; v2 reports the two counts apart. See `tourshow-phaser-figure-duplication-across-songs`.
2. **Figure NAMES counted under a header that read as figure COUNT.** The batch prework's first run labelled a per-song header with the number of figure *names* while the header read as the number of distinct figures. {LD} gives one figure content several names per song, so a name-count overstates the mint workload every time (SONG_K's first pass showed 6 REUSE + 2 NEW against only 6 truly distinct figures). Caught pre-ship, before the CSVs were finalized.

**A third example the same session, same shape, different domain — bookkeeping, not a shipped artifact:** the INBOX backlog was carried forward session to session as "~85 lines" (per `CURRENT_STATE_A0803.1`) or "~55" (per the LOCK plan) — both undercounts, neither rechecked. An actual count of the file found **140** lines. Count the file; don't quote the last state file's estimate.

**A fourth instance, 2026-08-05 — the scope resolved an apparent contradiction rather than being the mistake itself.** SONG_L's gear counts: 23 phaser LINES sit across 20 cue PARTS. cLD first reported "Div2 x15" (the PARTS scope) and the phaser smith separately reported "Div2 x18" (the LINES scope, pre-ruling). **Both were correct at their own scope; neither was the other's error.** Speed Scale is a PART knob, so PARTS is the operative unit for a desk gear list — but the disagreement itself is a reminder that a count mismatch between two honest passes is often a scope disagreement, not a defect. See `tourshow-seq2210-song-l-build-record`.

**The rule, stated for reuse:** before shipping any count — in a findings doc, a CSV header, a state-file estimate, or a run report — state what was included, what was excluded, and whether the number was actually recomputed or just carried forward from the last time someone said it. State the scope alongside the count, every time, not just the first time it's derived.

**Relation:** `tourshow-phaser-figure-duplication-across-songs` (home of the first instance above) · `recipe-layer-is-fixture-agnostic-doctrine` (carries an earlier, 2026-07-27 count-correction — 105 vs. 50 live recipe lines — plausibly one of the earlier instances this session's material numbers itself against, though this run did not independently verify that specific cross-reference).
