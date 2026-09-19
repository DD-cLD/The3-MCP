---
id: matricks-pool-reusability-and-block-structure
title: "MAtricks pool objects are grid-agnostic and reusable; the 30-look block structure convention"
role: programmer
tags: [ma3, coachella]
when_to_load: "When porting MAtricks pool objects to a different rig/grid, or when orienting to the Coachella pool-numbering convention (MAtricks/Sequences/Executors all run 1-30/201-230)"
status: active
source: "MEMORY §Patterns We Use, 2026-04-01"
verified: grandMA3 onPC 2.4.2.2 (Mac)
supersedes: []
superseded_by: null
---

**MAtricks pool objects are grid-agnostic** — they are reusable on any rig, provided phase is recalculated for the new grid's fixture count/geometry (see `phase-math-formulas`). A pool object built for one rig's N does not silently work on another rig without recomputing N-dependent phase values.

**30-look block structure** (Coachella-specific numbering convention): **MAtricks 1–30, Sequences 1–30, Executors 201–230** — a fixed 1:1:1 mapping across the three pool types for the 30 looks in the show.

## ⭐ THE SET IS NOW LIVE IN THE BUILD FILE — and its portability is proven

**Dave imported the 30 Coachella Spectra Tower MAtricks to pool 111-140** (2026-07-28), inside
the cLD namespace alongside the 101-104 Full/Half/2-Wing/Quarter block. **They bind to a cue
recipe by `Assign` alone.**

**The "recalculate phase for the new grid" caveat above does NOT bite this set.** Operator
evidence (Dave): *"I've used the same MAtricks on several different shows with several fixture
groups big and small and honestly they all translated well with no adjusting on the phase
settings."* That is stronger than a value-read — it exercises the stored value AND how the
console applies it across differing N. A count-computed literal could not have translated
cleanly; translating with zero adjustment means the values are generic.

**Consequence: adopt wholesale, no genericizing pass.** These are the reference implementation
of `no-baked-n-portable-phaser-doctrine` and the spatial half of
`tourshow-authoring-contract-v01`.
History: none — stable since 2026-04-01. Updated 2026-07-28 [0727-2cLD]: the Coachella 30 are live at pool 111-140 and their portability is confirmed by multi-show operator evidence, so this concept's phase-recalculation caveat does not apply to them.
