---
id: probe-called-unreliable-is-not-evidence
title: "A probe you have just called unreliable is not evidence — fix it or drop it, never keep it in play as a supporting hint"
role: operational-live
tags: [process, paid-for-lesson, debugging, probe, tourshow]
when_to_load: "Before using a probe or script's output as supporting evidence for a decision after you have already flagged that same output as looking wrong — the moment a probe result reads as suspect, stop treating any part of it as signal until it is fixed or replaced"
status: active
source: "findings/INBOX.md [0805cLD] 2026-08-05, SONG_L composite-split inversion (phaser smith BLOCKER catch)"
verified: grandMA3 onPC 2.4.2.2 (Mac)
supersedes: []
superseded_by: null
---

**Paid-for process rule, worth more than the bug that produced it.** A probe bug manufactured
a false premise, and cLD built on it AFTER already noticing the probe was unreliable.

`dg_pop_shape.py` printed fixture IDs through a `[:6]` string slice, so `13301` silently
truncated to `1301`. Separately, its inner `sub.iter()` grabbed the FIRST `StandardRecipe`
found in a subtree rather than the correct one, so it attributed both shapes of BOTH Dream
Girl composites to `JDC1 US [RGB]`. **cLD saw the output looked wrong** ("only found ONE
population per figure" — a composite has more than one) **and said so — and then still used
the same probe's output as a supporting signal for the population→shape split it was building.**
The resulting split was backwards: the `Verse 1/2` composite's SINE assignment was inverted, 6
of 23 phaser lines wrong, caught only by the phaser smith cross-checking against {LD}'s own
fixture-ID cover. Full incident: `tourshow-seq2210-song-l-build-record`.

**The rule: once a probe's output has been called unreliable, it is not evidence any more —
not weak evidence, not a "consistent with" data point. Fix the probe or drop the result
entirely. Do not keep it in play as a supporting hint for the same decision it already failed
to make correctly.**

## The method that should have been used instead

The population→shape join is available in-file and cheap, with zero inference: each figure's
own subtree carries `Preset/StandardRecipe/DependencyExport/Dependency/Group/SelectionData/Item`
(the exact fixture roster per population) alongside `Preset/PresetData/Phaser@ID` (the
per-fixture shape). Join the roster against the shape and population→shape falls out directly
— the standing method for every future composite; never infer it from ID prefixes or MAtricks
shape. This method, and the composite-handling doctrine it serves, now live in
`parts-per-century-emit-pattern-and-et-gate`.

**Relation:** `tourshow-seq2210-song-l-build-record` (the build this was paid for on),
`empty-census-deserves-selector-suspicion` (sibling discipline — that concept is about
trusting a ZERO; this one is about trusting a probe you have already flagged as buggy, for ANY
value it returns).
