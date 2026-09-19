---
id: tc-temp-release-pair-dialect
title: "TC bump/drum-roll events are Temp + Temp(Release) pairs, never a latching Go+ — two coexisting event-XML forms, both fire"
role: programmer
tags: [ma3, timecode, xml-schema, v2.4]
when_to_load: "Before authoring or repairing any bump/flash/drum-roll TC event by hand or by XML surgery — the press/release event pair shape, the attribute differences between the two coexisting event forms, and the time-format switch past 60 seconds"
status: active
source: "findings/INBOX.md [0731-2cLD] 2026-07-31, TC event dialect facts from cld_tc102_inspect track 5 (SONG_B drum-roll repair); wraps/2026-07-31-song-b-heard-song-c-built.md"
verified: grandMA3 onPC 2.4.2.2 (Mac)
supersedes: []
superseded_by: null
---

**Ruling (Dave):** drum-roll/bump TC events are **`Temp` + `Temp(Release)` pairs, ~0.3s apart, NEVER a latching `Go+`.** This restores `tc-bump-button-architecture` doctrine — a desk hand-repair had used quick `Go+` entries instead and needed converting back.

**Press event:** `RealtimeCmd` `ExecToken="Temp"` `Status="On"`.

**Release event:** `Name="Temp(Release)"`, `RealtimeCmd` `Status="Off"` `ExecToken="Temp"` — a **sparse desk-typed form**: no `Object=` / `ValCueDestination=` needed, `Time=` offset +0.3s from the press.

**Two event forms coexist in the same TC file, and both fire:**
- RECORDED/full form: `Object=` + `ValCueDestination=` + `UserProfile`/`User` set, `IsRealtime=1`.
- DESK-TYPED sparse form: no `Object`/`ValCue`, `User=0`, `IsRealtime=0` — resolves via the track rather than its own address.

**A `Go+` → `Temp` conversion must flip BOTH the `Name` attribute AND `ExecToken`** — changing only one does not produce a working Temp event.

**Time format:** times over 60s use the minute-prefixed attribute form `"1m42.333"`, not raw seconds.

**Exec-object addressing note:** exec object number = seq number − 1 (e.g. exec object 1113 = seq 1114 − 1) — the same seq-minus-1 law seen elsewhere in the corpus, confirmed again on a TC exec/track read.

**Verify queued (Dave, explicit) — CLI TC-event creation/type-flip on a SCRATCH timecode is UNPROVEN mechanics.** Kept off the live repaired TC this session (the repair used the XML-surgery lane instead); needs proving before this dialect can be authored directly at the CLI for the remaining songs.

**Relation:** `tc-xml-event-surgery-lane` for the proven method used to convert Go+ entries to Temp pairs by file surgery. `tc-bump-button-architecture` (existing concept, not staged this run) for the base bump-vs-cue-count doctrine this session re-confirms after a desk repair briefly contradicted it.
