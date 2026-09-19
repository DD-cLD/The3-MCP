---
id: source-timing-is-the-tempo-grid
title: "{LD}'s SONG_T timing layer is a pure 139-BPM beat grid — 15 part-0 CueInFades all beat-locked (2/4/8/16 beats), riding only the >> travel cues; TrigTime never used"
role: programmer
tags: [tourshow, festival, song-t, timing, source]
when_to_load: "Before reading or reverse-engineering {LD}'s SONG_T (or any {FESTIVAL} song's) fade timing — the whole timing layer decodes to round beat counts at the song BPM, not arbitrary seconds, and only rides the >> travel cues"
status: active
source: "findings/INBOX.md [0728cLD] 2026-07-28, decoded from Sequence 1500 export at 139 BPM; wraps/2026-07-28-song-t-full-build-and-resolver-laws.md"
verified: grandMA3 onPC 2.4.2.2 (Mac)
supersedes: []
superseded_by: null
---

**{LD}'s entire SONG_T timing layer is 15 part-0 `CueInFade` values, and every one of them is beat-locked to the song's 139 BPM** — not a hand-typed seconds value:

| Seconds | Beats @ 139 BPM |
|---|---|
| 0.863 | 2 |
| 1.727 | 4 |
| 3.453 | 8 |
| 6.906 | 16 |

(6.906 rides the intro travel cues 2.1/3.1.) **`Mark` fades in at a flat 2.0s; `OffCue` releases at a flat 3.0s** — the two structural bookends are the exceptions to the beat-lock, timed in plain seconds instead.

**Cue 26.1 is dual-layer:** `CueInFade` (intensity) = 1.73s while `Preset4Fade` (color) = 3.45s — **color lags intensity by exactly one beat-doubling** (1.73 ≈ 4 beats, 3.45 ≈ 8 beats).

**Fades ride ONLY the `>>` travel cues** — a third independent confirmation of the phrase-envelope split (named cue = the look/chord, `>>` cue = the movement/voice-leading; see `cue-structure-is-tonal-harmony`). The named section cues themselves carry no fade of their own.

**`TrigTime` is absent everywhere in this song** — every cue is a bare `Follow`, firing on completion of what precedes it, never on a timed trigger.

**Parts do NOT inherit the part-0 fade automatically** — the part-0 `CueInFade` must be (re-)applied to every part explicitly on any regeneration/rebuild; it is not a cue-level default that cascades.

**Method note:** this is a spec-read for starting values, the same posture `tourshow-authoring-contract-v01` rules for {LD}'s phasers (read for the musical figure, then re-author) — round-trip the beat math against the target song's own BPM rather than copying the raw seconds.

**Relation:** `source-spread-is-one-full-wave` is the spatial half of the same six-phaser/timing decode; `tourshow-seq1510-build-record` is the build this timing layer was authored into.

## Corroborated on the AUX layer, 2026-08-05 [0805cLD]

SONG_L's aux release fades are beat-locked the same way: OffCue fades read **0.536/0.540**
(= 1 beat at 112 BPM, 60/112 = 0.5357) and **1.070/1.071** (= 2 beats), kept VERBATIM from
{LD} rather than recomputed. Same law as the main-sequence timing layer this concept
documents, now confirmed on an aux for the first time — see
`tourshow-seq2210-song-l-build-record`.

History: none — decoded in one pass, 2026-07-28, from the Sequence 1500 (SONG_T) export.
