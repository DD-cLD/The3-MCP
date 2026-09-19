---
card: TIMECODE
version: "0.1"
created_at: 2026-07-24
scope: "Timecode authoring and TC desk sessions — the LAST step, its own session (Dave's ruling)"
not_scope: "Song content authoring (CARD_AUTHORING) · general console contact (CARD_DESK)"
---

# CARD — TIMECODE

**Why this is its own card:** TC is separable in time. Per Dave's ruling, timecode is
**not part of the content-import step** — it is the last step and gets its own desk
session, at least for song #1. Nothing here is needed while building song content.

Every line is a place the console accepts your work and silently fires the wrong thing.

---

## ⛔ THE ONE THAT LOOKS RIGHT AND ISN'T

**`CueDestination` is COSMETIC display text.** The console does not read it at import —
it re-resolves from the executor's *current* cue 1 (which is why stale labels from
prior executor contents show up). **Firing is driven by `ValCueDestination`** plus the
numeric address. A label that reads correctly proves nothing.
`export-timecode-tc-event-xml-schema`

---

## THE XML CHAIN

`Timecode` → `TrackGroup` → `MarkerTrack` + `Track` → `TimeRange` → `CmdSubTrack` → `CmdEvent` → `RealtimeCmd`

- `Track` targets a sequence: `Target="ShowData.DataPools.Default.Sequences.<N or name>"`
- `TimeRange` takes `Duration="To End"`
- `CmdEvent` carries `Name="Go+"|"Off"`, `Time=<decimal seconds>`, `CueDestination=<label>`
- `RealtimeCmd` carries `Type="Key"`, `Object="13.13.0.5.<exec>"`, `ExecToken="Go+"|"Off"`, **`ValCueDestination="0.5.<exec>.<cue × 1000>"`**
- Faders ride a parallel `FaderSubTrack` → `FaderEvent(ExecToken="FaderMaster" ValFaderValue="NN.NN%")`
- Timecode object attrs: `TCSlot=-1`, `Cursor`/`Duration`, `LoopMode`, `Goto="as Go"`, `PlaybackandRecord="All Events"`

`export-timecode-tc-event-xml-schema`

## ADDRESSING

- **Cue number is encoded ×1000** in `ValCueDestination` — the same scaling as a cue's internal `.no`. Cue 5 → `5000`. `export-timecode-tc-event-xml-schema` · `cue-display-number-vs-no-addressing-gotcha`
- A `CmdEvent` with **no** `ValCueDestination` imports as a plain sequential `Go+` — perfectly fine for a linear cue list, and simpler. `export-timecode-tc-event-xml-schema`

## TIME FORMAT & DROP-FRAME MATH

- `Time` is a **decimal-seconds string** — `"5.383"`, or `"1m05.183"` past a minute. Decimal seconds is **frame-rate agnostic**, which is why it is the safe authoring unit. `export-timecode-tc-event-xml-schema`
- **29.97 DF is the exact fraction `30000/1001`, never a float.** A float approximation silently drifts off true time. `df-2997-drop-frame-timecode-math-and-rate-switch`
- Keep all TC arithmetic in **integer frame space**: `03:29:53;22 + 42.8s = 03:30:36;15` (DF) vs `03:30:36:16` (30 NDF). The two differ — pick the rate before you compute. `df-2997-drop-frame-timecode-math-and-rate-switch`
- A console rate-switch recalculates automatically — no re-entry, no re-export needed. `df-2997-drop-frame-timecode-math-and-rate-switch`

## SHORT-FORM / TOUR BOUNCES

- Address post-seam short-bounce cues on the **LONG-FORM timeline** (`file t + audio cut width`, frame-round **once**) — never file-TC + the LTC track's frame-rounded jump. The re-encode rounding costs ±1 frame and forks the address between bounces. One sheet then stays valid on both. `tourshow-days-show-edit-map`
- Convert with `(QCaller long-form TC − tcStart) at 30fps`. Session `startSec` is **file-local** — a naive `tcStart + startSec` fires post-splice cues early. `tourshow-days-show-edit-map` *(show record — not included)*

## BUMPS

- A rhythm/flash gesture better timed on a button gets built as a **bump on a button executor** — but **the button push is still entered into the TC list as an event**. One reusable bump fired many times beats a thousand cues. `tc-bump-button-architecture` · `tourshow-playback-architecture-doctrine`

## CUTOVER — WHEN AND HOW

- **TC cutover is the LAST act of a build — never folded into the first import chain.** {LD}'s sequences are EXPORT-FOR-INSPECTION ONLY (never deleted, never edited) and are the standing park spot for any post-cutover structural edit: point TC back to theirs, do the work, point it back — the show is never dark mid-surgery. `tc-cutover-last-and-delete-eats-events-doctrine`
- **Deleting a TC-targeted sequence EATS the track's events — target MOVES preserve, target DELETES don't.** Readback must count Target AND per-track EVENT COUNT, always; a target-only census reads healthy on an event-emptied track. `tc-cutover-last-and-delete-eats-events-doctrine`
- **A third TC authoring lane exists beside CLI-Assign and desk-typing: byte-surgical span-editing of an exported TC file** (Export → edit one Track element's span → SaveShow checkpoint → Delete+Import → export-back event-count census). Use for post-cutover TC edits and for Go+→Temp conversions. `tc-xml-event-surgery-lane`
- **Bump/drum-roll events are `Temp` + `Temp(Release)` pairs (~0.3s apart), never a latching `Go+`.** `tc-temp-release-pair-dialect`

## ⚑ VERIFY

- Read back after import: a clean import echo proves nothing about `ValCueDestination`.
- Confirm the target executor's cue 1 is what you expect **before** trusting any displayed `CueDestination` label.
