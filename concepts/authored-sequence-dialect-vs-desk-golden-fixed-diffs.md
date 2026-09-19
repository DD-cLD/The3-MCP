---
id: authored-sequence-dialect-vs-desk-golden-fixed-diffs
title: "The authored-sequence dialect diverges from the desk-export golden in 3 FIXED, sealed-importable spots — smiths should stop re-flagging them as deviations"
role: programmer
tags: [xml-schema, sequence, smith, dialect, golden]
when_to_load: "Before a smith certification pass flags a sequence-XML as non-golden, or before hand-authoring a sequence to match a desk export byte-for-byte — these 3 spots are known, deliberate, and already proven to import clean"
status: active
source: "BACKLOG.md 2026-08-01 [0801-2cLD]"
verified: grandMA3 onPC 2.4.2.2 (Mac)
supersedes: []
superseded_by: null
---

**The authored-sequence-XML dialect diverges from the desk-export golden in 3 FIXED spots — all sealed importable as of {TOUR} build v.88.** These are known, deliberate divergences, not defects, and a smith certification pass should stop re-flagging them:

1. **`Sequence` element: `SpeedMaster` set AFTER `SpeedScale`** in attribute order (the emitter's position, desk-proven by the SONG_C import + live readback `SpeedMaster=Speed1`).
2. **No `Name` attribute on `OffCue`/`CueZero` parts** — the kit idiom; every shipped song has imported clean this way. An export-back adds a `Name`; it is not an import requirement.
3. **`StandardRecipe`: `MAtricks=` written BEFORE `Selection=`** in attribute order.

**Consequence:** any smith packet or manual review comparing an authored sequence byte-for-byte against a desk-export golden should treat these three positions as an accepted, sealed variant of the dialect — not as evidence the authored file is wrong.

**Relation:** `tourshow-seq1310-build-record` (documents spots 1 and 2 as smith flags on that specific build, both closed with no edits — this concept consolidates that pattern as a standing dialect fact rather than a per-build note). `export-sequence-xml-schema` (the general Sequence/Cue/Part/StandardRecipe schema this dialect sits inside — see also its amendment on a fully NAME-less Part, a related but distinct schema-completeness fact). `smith-packet-must-stage-multi-part-golden` (why a smith needs a real multi-part golden to judge dialect facts like these against in the first place).
