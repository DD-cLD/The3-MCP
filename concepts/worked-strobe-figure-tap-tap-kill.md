---
id: worked-strobe-figure-tap-tap-kill
title: "The tap-tap-kill figure — quarter-note beam pops, then full-plate strobe, then an outside-in delayed kill inside one beat"
role: design
tags: [ma3, doctrine, effect, strobe, tourshow, jdc1, acme]
when_to_load: "When building a beam/plate strobe cue arc — this is Dave's worked three-part reference figure (pops, full strobe, delayed kill)"
status: active
source: "findings/INBOX.md, 2026-07-15, Dave dictated live (recipe arc)"
verified: grandMA3 onPC 2.4.2.2 (Mac)
supersedes: []
superseded_by: null
---

Dave's worked reference figure for a strobe cue arc, built on `replay-portable-strobe-doctrine`, in three beats:

1. Quarter-note controlled beam pops via the two-state strobe phaser — Dave's shorthand for the feel is "tap tap tap."
2. The strobe opens and all plates jump to full intensity.
3. A delayed-intensity kill sweeps the plates down to zero from the outside in, landing the whole sweep inside a single quarter beat.

The kill's delay spread across the row is itself a named choice: **two-wing** (the usual pick), **no-wing** (no delay spread, everything drops together), or **multi-wing** (more than two delay zones). This spread can be scoped per beam, per fixture, or per group — same three-beat shape, different grain.

This figure was actually realized tonight as Sequence 101's Cue 2 ("PLATES OUT-IN"), which Dave ratified enthusiastically on sight. The cue's mechanical implementation (recipe/MAtricks embedding syntax, exact delay values) is tracked as its own concept in this run's console-mechanics shard — not duplicated here; this file captures the figure as a reusable design pattern, illustrated with {TOUR}'s beam/plate vocabulary but meant to travel per `replay-portable-strobe-doctrine`.

**Second live realization, 2026-07-16 — Sequence 104 "cLD TAPTAP" (v0.15), built on the phaser/recipe system:** a fuller three-cue build of essentially the same shape, this time authored as phaser recipes on the JDC drill groups (128/129/130 — see `grid-drill-exemplar-groups-121-124`'s 2026-07-16 census note):
- **Cue 1 (TAPS):** PhaserRecipe on Group 130 using the Strobe SHAPE, with Speed overridden 600→60BPM (the override broke only the Speed property's shape-link bracket; curve/width stayed linked) + NShot 3 — three quarter-note taps then auto-stop. Live-verified.
- **Cue 2 (HIT):** Group 129 × FX White + Group 130 × Strobe shape running at its native, un-overridden speed (`<600BPM>`).
- **Cue 3 (KILL):** Group 128 × Dimmer-0 + a recipe-line MAtricks delayed sweep (`Delay From X 0` → `Delay To X 1`, a directional delay sweep across X).

Run end-to-end via `Go+` ×3. This is the same conceptual three-beat figure (taps, then full/hit, then delayed kill) as the 2026-07-15 Sequence 101 Cue 2 realization above, now built on the newer recipe system across three separate cues instead of one, and on the JDC group set rather than the original beam/plate groups.

History: none — dictated live 2026-07-15 and built same session as Sequence 101 Cue 2. 2026-07-16: second live realization built and run as Sequence 104 "cLD TAPTAP" (v0.15), a fuller three-cue recipe-based version of the same figure on the JDC group set — see body.
