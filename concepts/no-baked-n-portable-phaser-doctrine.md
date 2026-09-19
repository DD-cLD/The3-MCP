---
id: no-baked-n-portable-phaser-doctrine
title: "NO BAKED N in travelling content — stock MAtricks + generic phase ranges (0-360 / 0-180) + AdaptiveMeasure/AdaptiveWidth, never a phase literal computed for a specific fixture count"
role: programmer
tags: [tourshow, doctrine, portability, phasers, matricks, phase-math]
when_to_load: "Before authoring ANY phaser, MAtricks value or recipe that has to survive landing on a different rig — this is the one thing that genuinely breaks across rigs, and it is the requirement the fixture-agnostic recipe doctrine depends on"
status: active
source: "Dave ruling 2026-07-27 [0727cLD], refining the resolution question raised by the 19 JDC1 -> 7 LEDJ Q40 upstage swap"
verified: grandMA3 onPC 2.4.2.2 (Mac)
supersedes: []
superseded_by: null
---

**Dave's ruling.** Differing pixel counts across rigs are fine. **A MAtricks carrying a
phase literal computed for a specific N is not** — that is the single thing that actually
breaks when content lands on a different rig.

## The worked example

A phase stored for **N=228 cells** is `360 − 360/228` = **358.4°**. Recalled on **7 floods**,
the seven land at 0 / 59.7 / … / 358.4 — putting the last fixture **1.6° off the first**, a
visible collision at the wrap. The correct value for N=7 would have been **308.6°**.

So `360 − 360/N` is **MORE correct on a known N and BRITTLE everywhere else** — the wrong
trade for a show that lands on a different house rig nightly.

## The portable phaser shape

1. **Stock MAtricks pool object** (`tourshow-stock-matricks-pool-inventory` — pool 1-30,
   Reset/Phase/Block/Group/Wing families).
2. **Generic phase range** — `0-360` for a full spread, `0-180` where
   `Direction=Alternate` (bounce doubles the traversal, per `stock-measures-grammar-census`).
   **`PhaseToX=360` is safe: the engine normalises it as one full lap with endpoints
   excluded** — Dave confirmed, resolving `recipe-phase-endpoint-convention`.
3. **`AdaptiveMeasure` + `AdaptiveWidth`**, which per `v24-phaser-model` auto-calculate
   timing and width **from the current selection grid** rather than from stored numbers.
4. **Grid coordinates live in the GROUP**, which the contract already bakes at Store time.

**Net: no N appears anywhere in the recipe**, and the same phaser recomputes itself for 7
fixtures or 228. The adaptive layers are the built-in answer to cross-rig scaling and should
be standard on all travelling content.

## What is NOT superseded

**Keep `360 − 360/N` for locking a KNOWN rig.** `phase-math-formulas` remains correct for
MAtricks **pool storage**, where phase is a literal manual value the console does not
compute (`mtricks-phase-vs-encoder-phase`). Two surfaces, two computation paths, two
different questions — the literal formula for a fixed rig, generic ranges for anything that
travels.

## ⭐ The reference implementation — what "done right" looks like

**Dave's 30 Coachella Spectra Tower MAtricks (imported to pool 111-140) are the positive
exemplar of this doctrine.** Operator evidence, 2026-07-28: *"I've used the same MAtricks on
several different shows with several fixture groups big and small and honestly they all
translated well with no adjusting on the phase settings."* They bind to a cue recipe by
`Assign` alone.

**Why that is proof rather than anecdote:** a phase literal computed for a specific N
**cannot** translate cleanly to a different N — it collides at the wrap or leaves a hole
(see the worked example above). Translating across several shows and several group sizes
with **zero** phase adjustment is only possible if the stored values are generic. And it is a
stronger test than reading a value off one slot, because it exercises the whole chain — the
stored value *and* how the console applies it across differing fixture counts.

**Practical consequence:** adopt the set wholesale, no genericizing pass. And any MAtricks
authored from here should look like these — this is the standard the doctrine points at.

## Why this doctrine is load-bearing

`recipe-layer-is-fixture-agnostic-doctrine` explicitly REQUIRES this to hold. `Group x Preset`
absorbs rig and fixture-type differences, but a baked phase literal smuggles a fixture count
back into the content layer and defeats the whole scheme. First live test: 19 upstage JDC1
replaced by 7 LEDJ Q40 — **phaser resolution degrades gracefully** (a fine chase across 228
cells is a coarse one across 7 floods; same recipe, still correct, reads differently). **The
cut hits the FILL layer, not the CONTENT layer.**

History: ruled by Dave 2026-07-27; filed 2026-07-27 [0727-2cLD], closing the librarian
debt flagged at that session's boot (the fixture-agnostic doctrine had been citing this
concept before it existed). Updated 2026-07-28: gained a positive exemplar — the Coachella 30 (MAtricks 111-140), proven portable across multiple shows and fixture counts with no phase adjustment, promoting the concept from a cautionary rule to one with a reference implementation.
