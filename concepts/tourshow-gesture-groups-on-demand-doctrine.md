---
id: tourshow-gesture-groups-on-demand-doctrine
title: "Bank D gesture groups build ON DEMAND, song by song — never mass-generated; each gets Stored the moment it's actually used"
role: programmer
tags: [tourshow, doctrine]
when_to_load: "Before mass-generating Bank D gesture groups (HALO/SPINE/FRAME/WALL/CANOPY/CORRIDOR/JAB/CURTAIN) up front, or before deciding whether a live/ad-hoc grid sketch needs to become a stored Group"
status: active
source: "findings/INBOX.md, 2026-07-19 [0718-19cLD], Dave ruling; ARTIST_TOURSHOW_GROUP_CONTRACT_v0.1.md"
verified: grandMA3 onPC 2.4.2.2 (Mac)
supersedes: []
superseded_by: null
---

Dave's ruling: the Bank D gesture vocabulary (HALO/SPINE/FRAME/WALL/CANOPY/CORRIDOR/JAB/CURTAIN — see `tourshow-festival-group-theory` for the vocabulary itself) builds **ON DEMAND, song per song** — start with whichever ones a given song actually needs, develop more as the build goes. It is explicitly **NOT** mass-generated up front the way the contract groups are.

**Two-layer model this establishes:** contract groups (spots/washes/pix/JDC/beams by century+scope, see `tourshow-group-contract-v01`) are the **always-there layer** — built once, complete, before any song work starts. Gesture groups are the **story layer** — accumulated incrementally, per-song, as the actual need for a given gesture shows up.

**Storage discipline that follows from this:** live/ad-hoc grid composition (recalling groups or selections, appending, clicking to place the cursor for the next recall — see `grid-cursor-cli-recipe-for-2d-group-layouts`) is fine for **sketching** a gesture shape, but it is exploration only. Recipes bind Selection to a **stored Group object**, so the moment a sketched shape is actually going to be used in a repeatable recipe, it has to be Stored as a Group first — "store whatever we're gonna use." Practical rule: sketch live, then store before it enters a cue. This is why gesture groups get stored **at first real use**, not pre-built and not deferred indefinitely.

Suggested numbering home when a gesture group actually lands: century **7xx**, labeled `cLD GESTURE <name>` (per `tourshow-group-contract-v01`'s open/deferred notes) — not yet allocated as of this session.

**Relation:** the storage discipline here is a consequence of choosing recipe-based programming, not an MA3 technical requirement — see `tourshow-recipe-based-show-style-ruling` for that mode-vs-law distinction.

History: none — ruling stated live 2026-07-19, alongside the group contract design session.
