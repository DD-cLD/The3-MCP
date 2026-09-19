---
id: export-timecode-tc-event-xml-schema
title: "Export Timecode XML schema — Timecode>TrackGroup>Track (targets a Sequence)>TimeRange>CmdSubTrack/FaderSubTrack events; Time is a decimal-seconds string"
role: programmer
tags: [ma3, xml-schema, timecode, v2.4]
when_to_load: "Before reading, generating, or hand-authoring a TC-event XML file (Export Timecode) — e.g. cLD MAker's TC-event export or any file-side bump-lane generation — the full element/attribute shape and the beatgrid-startSec bridge"
status: active
source: "findings/INBOX.md, 2026-07-17 [0717-3cLD], console live 2.4.2.2 — Export Timecode, incidental capture (was open homework per tc-bump-button-architecture + NEXT_ACTIONS)"
verified: grandMA3 onPC 2.4.2.2 (Mac)
supersedes: []
superseded_by: null
---

**Schema tree:**

```
GMA3
 > Timecode (Cursor Duration LoopMode LoopCount TCSlot AutoStop SwitchOff Goto
             PlaybackandRecord TimeDisplayFormat FrameReadout RestartOption)
    > TrackGroup
       > <MarkerTrack>
       > <Track Target="ShowData.DataPools.Default.Sequences.102">
          > TimeRange (Duration="To End")
             > <CmdSubTrack>
                > <CmdEvent Name="Go+"|"Off" Time="5.383" CueDestination="cLD CHASE GAPS">
                   > <RealtimeCmd Type="Key" Object="13.13.0.5.101" ExecToken="Go+" ValCueDestination="0.5.101.1000">
             > <FaderSubTrack>
                > <FaderEvent Name="Fader(Master)" Time="12.783">
                   > <RealtimeCmd Type="Fader" ValFaderValue="100.00%" ValEncoderResolution="167772">
```

**Time format:** a decimal-seconds string (e.g. `"5.383"`), or `"1m05.183"` once past one minute.

**Semantics:**
- A `<Track>` TARGETS a sequence via the same dotted full-path convention as recipe bind-slot refs (see `export-sequence-xml-schema`).
- `<CmdEvent>`s fire `Go+`/`Off` at a given `Time` into a named cue (`CueDestination`).
- `<FaderEvent>`s ride master level at a given `Time`.

**THE BRIDGE:** a beatgrid moment's `startSec` (see `beatgrid-session-json-schema-conventions`) maps DIRECTLY onto a `CmdEvent`'s `Time` attribute — cLD MAker can generate a whole TC track file-side straight from a treatment timeline, with no manual TC recording step.

**Relation:** this CRACKS the "TC-event XML schema" homework left open in `tc-bump-button-architecture` — that concept's bump-executor design can now be authored directly rather than only recorded. Reserved as a v1.1 seam in `cld-maker-identity-rename-and-scope` (schema now fully captured, so unblocked whenever it's picked up).

**Corroboration (2026-07-18):** the decimal-seconds `Time` format was confirmed rate-agnostic in practice — switching a show's TC frame rate from 30fps to 29.97 drop makes the console recalculate its own display without touching this XML's `Time` values (no re-entry, no re-export). See `df-2997-drop-frame-timecode-math-and-rate-switch` for the full DF math this corroborates.

**Corroboration + two new mechanics (2026-07-21, [0721-2cLD]):** the full schema was **hand-authored file-side from scratch** (no console export as a starting point) for `cLD SONG_G TC` (Timecode 2) — 9 cue-fire `CmdEvent`s + 6 slide-pop events — and **imported clean**, a fourth proof point for `xml-file-side-authoring-import-lane-proven` (now on the timecode dialect). Two mechanics confirmed live:
- A `CmdEvent` **WITHOUT** `ValCueDestination` imports as a **plain sequential Go+** (fine for a linear cue list — no explicit cue targeting needed).
- **`CueDestination` is COSMETIC ONLY** — a display label, not read at import. The console **re-resolves the actual fire target from the executor's live current-cue** plus the numeric `ValCueDestination`; imported events showed stale labels (`"PLATE MASTERS FULL"`, `"cLD CHASE GAPS"`) left over from whatever that executor last held, while firing still hit the correct numeric address. Never trust the `CueDestination` string when reading an imported TC file — read `ValCueDestination`.

**Addressing formula, generalized:** `Object="13.13.0.5.<exec>"` and `ValCueDestination="0.5.<exec>.<cue × 1000>"` — the cue number is encoded ×1000 (cue 1 → `1000`, matching the original worked example `0.5.101.1000` above).

History: created 2026-07-17 from an incidental Export Timecode capture during the same live-desk session that cracked `export-sequence-xml-schema` — closes a homework item that had been open since 2026-07-16. Extended 2026-07-18: rate-agnosticism corroborated against live 29.97 drop-frame rate-switch behavior. Extended 2026-07-21: hand-authored from scratch and imported clean (cLD SONG_G TC) — fourth dialect proof for `xml-file-side-authoring-import-lane-proven`; confirmed CmdEvent-without-ValCueDestination falls back to plain sequential Go+; confirmed CueDestination is a cosmetic label only (console re-resolves from live executor state); generalized the ValCueDestination cue×1000 addressing formula.
