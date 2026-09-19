---
id: gears-delivery-is-a-list-cld-does-not-set-speed-scale
title: "Gears delivery ruling: cLD delivers a list of cues + Speed Scale at end of session — Dave applies it at the desk; cLD does not set Speed Scale itself"
role: operational-live
tags: [process, speed-scale, delivery, tourshow, ruling]
when_to_load: "Before deciding whether to issue Speed Scale Set commands at the console for a song's gears, or when a build session is wrapping up and gears are still owed — the standing division of labor is a delivered list, not a console write"
status: active
source: "findings/INBOX.md [0805cLD] 2026-08-05 (Dave, ruling)"
verified: grandMA3 onPC 2.4.2.2 (Mac)
supersedes: []
superseded_by: null
---

**RULED (Dave):** cLD delivers a list of cues + Speed Scale values at the end of each build
session; **Dave applies them at the desk. cLD does not set Speed Scale.**

This is the standing division of labor for the gear/Speed-Scale half of a song's build,
distinct from the mechanical work cLD does own outright (binding phasers, MAtricks, emitting
the sequence). See `tourshow-speed-architecture-standing-ruling` for where the gear NUMBER
comes from (the wrapper `SpeedFromX` ÷ song BPM, read directly off each Phaser Preset) and
`tourshow-seq2210-song-l-build-record` for a worked delivery
(`SONG-L_SPEED_SCALE_0805.md`, 20 parts).

**Relation:** `tourshow-speed-architecture-standing-ruling` (the formula this list is built
from), `state-the-scope-with-the-count` (state PARTS and LINES both when reporting a gear
count — the delivered list is scoped to PARTS, since Speed Scale is a per-part knob).
