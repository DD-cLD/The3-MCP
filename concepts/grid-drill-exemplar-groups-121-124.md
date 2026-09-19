---
id: grid-drill-exemplar-groups-121-124
title: "Groups 121-124 — the four canonical grid-drill exemplars (flat plane, proportional, paired-mirrored, bounce)"
role: programmer
tags: [ma3, grid, matricks, v2.4, exemplar]
when_to_load: "When you need a worked, verified example of a grid alignment technique (flat one-wide plane, proportional spread, paired mirroring, or the bounce pattern) to copy or extend"
status: active
source: "findings/INBOX.md, 2026-07-14, live-verified drill session; wraps/2026-07-14-3drig-mirror-doctrine-grid-drills.md"
verified: grandMA3 onPC 2.4.2.2 (Mac)
supersedes: []
superseded_by: null
---

The 2026-07-14 grid-drill session built four canonical two-part alignment Groups, all saved live in show **cLD_SANDBOX_v0.8**, each demonstrating a different alignment technique end to end (CLI build → `Store Group` → recall round-trip verified):

- **Group 121 "cLD SPOTS 1WIDE"** — a flat 48-wide single-row plane. Built from a bare `Fixture A Thru B` with no grid-cursor calls at all: a linear Thru selection auto-fills one X row in FID order. The simplest possible case — grid-cursor placement is only needed once the shape stops being a single line.
- **Group 122 "cLD DS WING ALIGN"** — proportional spread: 12 spots at step 4 and 16 wings at step 3, sharing one ~46-column window, with coincidence columns every 12. Kept as the worked density-gap exemplar for `alignment-pairing-vs-proportional-doctrine` — this is what proportional spread looks like when it's the right call.
- **Group 123 "cLD DS WING PAIRED16"** — the paired-and-mirrored exemplar. Wings (FID 149-164) fill row y=1, columns 0-15, in one Thru auto-fill; spots (FID 101-112) sit on row y=0, individually cursor-placed to skip columns 3/7/11/15. Originally built flat/unmirrored, then hand-rebuilt by Dave live into a mirrored triplet pattern — see `grid-mirror-symmetry-doctrine` — and stored over the original via `Store /Overwrite`.
- **Group 124 "cLD DS WING BOUNCE"** — the bounce pattern: wings on even columns 0-30, spots filling the odd-column gaps with 3 mirrored drops at columns 7/15/23. Full mechanism in `grid-bounce-pattern`.

All four round-trip verified and readable on-screen at their respective auto-fit zoom levels (Group 124 confirmed readable at 31 columns). Together they form the complete 2026-07-14 grid-drill arc — Dave's "four canonical two-part alignments": **auto-fill row → proportional spread → paired-mirrored → bounce**.

Building recipes (chases/effects fired against these Groups) was deliberately parked for a later session — see `multi-instance-grid-frontier` and the wrap's open threads for what comes next. (That later session arrived 2026-07-16 — see `worked-strobe-figure-tap-tap-kill` and the phaser/recipe concepts for what got built on top of these Groups.)

**Census confirmed 2026-07-16** (live, same numbering block, during the phaser/recipe session): the names above match exactly what a live group census found that night, plus the surrounding range — **125-127 are empty** (unused), and **128-130 are a JDC set**. 128-130 were used that same session for the tap-tap-tap-kill figure's Sequence 104 build: cue 1 taps on 130, cue 2 hit uses 129×FX White + 130×Strobe, cue 3 kill uses 128×Dimmer-0 — see `worked-strobe-figure-tap-tap-kill`.

History: none — all four built and verified live 2026-07-14, session `[0714-2cLD]3DRig-MirrorDoctrine-GridDrills`. 2026-07-16: live census confirmed the same names and extended the picture — 125-127 empty, 128-130 a JDC set, both put to use the same session.
