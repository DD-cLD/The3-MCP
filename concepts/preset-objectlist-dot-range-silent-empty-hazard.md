---
id: preset-objectlist-dot-range-silent-empty-hazard
title: "ObjectList('Preset X.Y Thru X.Z') returns EMPTY silently even when occupied — census presets via PresetPools:Ptr(pool) walk with nil guard instead"
role: programmer
tags: [ma3, lua, objectlist, presets, v2.4]
when_to_load: "Before using ObjectList with a dotted Preset range (e.g. 'Preset 4.59 Thru 4.62') to census or verify preset pool contents — dot-form preset ranges are unreliable in ObjectList even when the slots are genuinely occupied"
status: active
source: "findings/INBOX.md [0731-2cLD] 2026-07-31 (SONG_C colour-pool census); wraps/2026-07-31-song-b-heard-song-c-built.md 'Paid for' §4"
verified: grandMA3 onPC 2.4.2.2 (Mac)
supersedes: []
superseded_by: null
---

**Read-lane hazard (corroborated a second/third time, on SONG_C):** `ObjectList('Preset 4.59 Thru 4.62')` returns an **EMPTY list, silently** — no error — even though all four slots are occupied. Dot-form Preset ranges are unreliable in `ObjectList`.

**Scope of the hazard, refined this session:** this is specific to **Preset** dot-ranges. **Sequence / Timecode / MAtricks `ObjectList` ranges are fine** — do not over-generalize the caution to every pool type.

**Correct census method for presets:** walk `DataPool().PresetPools:Ptr(pool)` directly, with a **nil guard** — `Ptr(i)` can return `nil` mid-iteration and will throw if not guarded.

**Relation to existing corpus:** this corroborates and extends `objectlist-thru-vs-wildcard-gotcha` (existing concept, not staged this run — its documented case was `Preset 22.1 Thru 22.46`; this session's `4.59 Thru 4.62` is a second live data point on a different pool). cLD should consider folding this file's scope-refinement (only Preset ranges affected) and its pool-walk alternative into that concept's body directly at next edit, since its body wasn't staged for a merge this run.
