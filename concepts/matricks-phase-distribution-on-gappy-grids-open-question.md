---
id: matricks-phase-distribution-on-gappy-grids-open-question
title: "CONFIRMED 2026-07-16: MAtricks PHASE distribution respects gaps via ABSOLUTE grid coordinates (same model as XWidth) — a gap consumes a beat, live 100% verified"
role: programmer
tags: [ma3, matricks, phase-math, v2.4]
when_to_load: "Before trusting phase-math formulas on a grid with gaps or a non-zero origin — N = the full grid extent including gaps, not the occupied-cell count; live-confirmed 2026-07-16, no longer an open question (id kept unchanged for stability, see History)"
status: active
source: "findings/INBOX.md, 2026-07-10 (opened) through 2026-07-16 (closed) — console live 2.4.2.2"
verified: grandMA3 onPC 2.4.2.2 (Mac)
supersedes: []
superseded_by: null
---

**RESOLVED 2026-07-16 — id and framing below kept as the historical record of the question; see the confirmation paragraph near the end for the answer.**

**Originally unresolved:** `matricks-xwidth-wraps-on-absolute-grid-x` confirmed that XWidth re-wrap uses each fixture's **absolute** grid X coordinate, mod width — a non-zero grid origin produces uneven, wart-carrying wraps. It was **not yet known** whether MAtricks **PHASE** distribution behaves the same way, or whether it instead **compresses to only the occupied cells**, ignoring gaps/origin offsets. (Answer, confirmed live 2026-07-16: PHASE behaves the same way as XWidth — absolute coordinates, not compression.)

This matters directly for `phase-math-formulas`: those formulas assume a clean `N` (effective fixture count). If Phase uses absolute grid coordinates like Width does, a gappy or offset-origin grid could silently produce the wrong phase spread even when N is computed correctly — the formula's N-based math would need a grid-compression step first.

**Verifies with:** build a phaser on a deliberately offset or gappy grid (non-zero origin, and/or a grid with empty cells between occupied ones) and observe whether the phase values land as if the occupied cells were compressed to a clean 0..N-1 run, or as if the raw grid coordinates (including gaps) were used directly.

**Dave's operator answer (2026-07-15, not yet the live 100% confirm):** per Dave's own operating knowledge, **empty cells ARE respected** by MAtricks phase distribution, the same way they are by XWidth — unoccupied grid cells still count as coordinates (a `Next` step landing in a gap produces no stage output that beat). Reframed as design doctrine: a gap in the grid's time-map is a **rest** — mirrored/bounce gap placements author deliberate rests into a chase. Consequence for `phase-math-formulas`: **N in the phase formulas = the full grid extent including gaps, not the occupied-cell count** — the absolute-coordinate model, not the compress-to-occupied model. This **largely closes** the question above, but Dave was explicit he wants a **live 100% confirmation** before treating it as fully settled — `status` was held at `verify` until that run happened (see the confirmation two paragraphs below: it has now happened, and status is `active`).

**Queued verification test (per the 2026-07-15 wrap):** Group 121 (contiguous, no gaps) as the **control**, Groups 124/128 (gappy layouts) as the **test cases** — fire the same phase distribution and visually confirm the gap-as-rest behavior live before flipping this concept to `active`.

**Live 100% confirmation (2026-07-16, Dave, attended, live on Group 124's bounce grid, 2.4.2.2):** a gap on the grid CONSUMES A BEAT in phaser traversal. Per the session's own framing this CLOSES the queued live confirm above. **Structural corroboration, same session:** a Chase recipe run on Group 124 "cLD DS WING BOUNCE" ran single-cell (AdaptiveWidth), honoring the sparse grid with no compaction — positional jumps were consistent with gap columns passing dark rather than being skipped/re-indexed. That's the structural half of the picture; the rhythm half (a gap consumes a full beat, not just a visual skip) is the live confirmation itself.

Consequence for `phase-math-formulas`, now settled rather than hypothetical: **N in the phase formulas = the full grid extent including gaps, not the occupied-cell count** — confirmed the absolute-coordinate model, not the compress-to-occupied model.

See `gap-is-a-rest-doctrine` for the design-doctrine framing of this same result (a gap in the grid's time-map is a rest), now also on confirmed mechanical footing.

History: none — probe fired as an open question 2026-07-10, not yet tested. 2026-07-15: Dave supplied an operator-knowledge answer (empty cells respected, absolute coords, gap=rest) that appeared to close this question — status intentionally held at `verify` pending Dave's explicit live 100% confirmation; test plan queued (121 control vs. 124/128 test). **2026-07-16: live confirmation ran** on Group 124's bounce grid, attended by Dave — a gap consumes a beat in phaser traversal, corroborated the same session by the structural Chase-on-124 test. Status flipped `verify` → `active`; question answered. Title updated to state the answer (id kept stable per the librarian's no-rename rule).
