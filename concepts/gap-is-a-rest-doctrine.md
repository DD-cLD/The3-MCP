---
id: gap-is-a-rest-doctrine
title: "A gap on the grid time-map plays as silence — mirrored/bounce gaps are authored rests, not just spacing"
role: programmer
tags: [ma3, doctrine, grid, matricks, v2.4]
when_to_load: "When placing gaps or dropped cells in a grid build — treat the gap as a deliberate musical rest, not leftover space"
status: active
source: "findings/INBOX.md, 2026-07-15, Dave dictated live"
verified: grandMA3 onPC 2.4.2.2 (Mac)
supersedes: []
superseded_by: null
---

Design reframe that follows directly from `grid-is-a-time-map-doctrine`: if a shared grid column is a moment in time, an EMPTY cell in that column is a moment with no stage output — silence. A gap on the grid doesn't just skip a fixture, it plays as a rest.

This reframes every gap pattern already in active use: the mirrored gaps of `grid-mirror-symmetry-doctrine` and the alternating drops of `grid-bounce-pattern` aren't just ways to make an uneven fixture count look tidy — under this doctrine they're **authored rests**, placed on purpose for musical effect, the same way a composer places a rest in a score.

The reframe follows Dave's operator confirmation that empty cells really are respected by MAtricks and phasing (Next steps into gaps produce no stage output that beat, and phase math uses the full grid extent including gaps, not just occupied-cell count). That mechanical verification is tracked in `matricks-phase-distribution-on-gappy-grids-open-question` — **live 100% CONFIRMED 2026-07-16** (Dave, attended, live on Group 124's bounce grid, 2.4.2.2: a gap CONSUMES A BEAT in phaser traversal), corroborated the same session by a structural test (Chase recipe on Group 124 ran single-cell/AdaptiveWidth, honoring the sparse grid with no compaction — positional jumps consistent with gap columns passing dark). This file remains scoped to the design meaning of the result, not the underlying mechanism — but the mechanism itself is now fully closed too, not just this doctrine's framing of it.

Practical consequence: when composing a mirrored or bounce gap layout, the gap placement deserves the same intentionality as the occupied cells — where the rest lands is a musical decision.

History: dictated live 2026-07-15, closing out the open mechanical question from 2026-07-14 (design reframe stated as doctrine ahead of the final live mechanical confirm). 2026-07-16: the queued live 100% confirmation ran (Group 124 bounce grid, Dave attended) — gap-consumes-a-beat confirmed mechanically, not just as operator knowledge; doctrine unchanged, now standing on fully confirmed footing.
