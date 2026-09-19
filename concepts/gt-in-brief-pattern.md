---
id: gt-in-brief-pattern
title: "GT-in-brief pattern: pre-compute octave-disambiguated grid + sections + transients and ship them IN the brief — 7/7 exact grids, zero octave errors"
role: tools
tags: [process, beatgrid]
when_to_load: "When designing a brief/handoff for a parallel or fleet build that depends on audio analysis (BPM grid, sections, transients) — decide whether to pre-compute ground truth centrally or let each builder re-derive it"
status: active
source: "findings/INBOX.md 2026-07-08"
verified: grandMA3 onPC 2.4.2.2 (Mac)
supersedes: []
superseded_by: null
---

**Pattern:** for the overnight fleet run (6 Bird's Eye songs), a "foreman" pass pre-computed **octave-disambiguated grid + sections + transients** for each song and shipped that ground truth directly inside each builder's brief, with an explicit instruction not to re-derive tempo. Result: **7/7 builds landed exact grids, zero octave errors** — every builder used `grid_final` verbatim, even where the contrast table was ambiguous (see `bpm-ambiguous-margin-policy`).

**Why this matters:** the run-1 bake-off's A-builder failure class (mis-picking an octave under time/tool pressure) is **closed by construction** once tempo is no longer something a builder is asked to derive — it's handed to them as measured fact. This reframes the builder's job: **pre-compute machine truth centrally, let each builder do the human/judgment layer** (section identity, palette, device placement, Impact placement) on top of a fact they don't have to re-earn.

**Generalization:** this is the same shape as `subagent-fanout-pattern`'s cheap-model/thinking-model split, applied one level more specifically — for any fan-out build where a shared, error-prone measurement underlies every worker's output, compute that measurement once, verify it once, and distribute it as ground truth rather than trusting N independent re-derivations to agree.

History: none — pattern validated same session across all 6 fleet-batch builds, 2026-07-08.
