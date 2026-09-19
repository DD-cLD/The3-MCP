---
id: tourshow-speed-architecture-standing-ruling
title: "Standing speed architecture: every cLD sequence rides the BPM Speed Master, gears come from the DIVIDE function in Cue Speed Scale, and NOTHING carries speed on Effects or MAtricks at play time"
role: programmer
tags: [tourshow, speed, tempo, doctrine, matricks, phasers, v2.4]
when_to_load: "Before setting ANY speed or tempo value — on a sequence, a cue-part Speed Scale, an effect/phaser preset, or a MAtricks — this is the standing division of responsibility and it supersedes per-song improvisation"
status: active
source: "findings/INBOX.md [0730cLD] 2026-07-30 (Dave, dictated standing ruling); applied on SONG_A; extended findings/INBOX.md [0803-3cLD] 2026-08-04 (weighted notation: Speed Scale = wrapper SpeedFromX ÷ BPM, wrapper path pinned)"
verified: grandMA3 onPC 2.4.2.2 (Mac)
supersedes: []
superseded_by: null
---

**Dave's ruling, standing across the show:**

1. **Every cLD sequence is set to the BPM SPEED MASTER.**
2. **Gears ride the DIVIDE function in Cue Speed Scale** — per cue part, at the desk.
3. **No special speed settings on Effects/phaser presets, and no MAtricks speed binds at play time.** Our MAtricks binds carry **phase/spread only**.

**Our presets therefore ship speed-UNBAKED, always.** Speed is a desk knob, not authored content — which is also what makes the content portable, since a baked rate is as rig-specific as a baked phase.

## Where the gear number comes from

Read it off {LD}'s own baked speeds during the phaser spec-read: his figures decode to clean divisions of the song tempo, and that division IS the Speed Scale plan. SONG_A decoded to **119.0** (÷1) and **59.5** (÷2) — his design intent, recovered rather than guessed. The aux Synth Swell decoded to **238 = ×2**.

**Watch for a cue that mixes gears.** SONG_A's chorus fired wave lines at ÷1 alongside a rivale line at ÷2. If Speed Scale is one knob per cue part, a mixed-gear cue cannot be split there — either accept the dominant gear or give the odd line its own part.

**Generalises `tourshow-fill-layer-rebuild-method`'s narrower SONG_T note** ("ours ride the Sequence Speed override set to BPM") from a per-build detail into standing doctrine for every song.


## ⭐ SCOPE NARROWED 2026-08-01 [0801-2cLD] — MAtricks DO carry speed for 2D figures whose X:Y speed RATIO is the figure

The standing rule in this concept's body ("no MAtricks speed binds at play time... our MAtricks binds carry phase/spread only") is narrowed for one deliberate case. **Dave ruled: for a 2D figure where the X:Y SPEED RATIO is itself the figure, author a SPECIAL MAtricks carrying BOTH X and Y speed.** This extends the standing rule rather than replacing it — it applies only when the ratio between axes is load-bearing, not as a general license to bake speed onto MAtricks.

**Dialect proven, no desk golden needed — settled empirically:** no MAtricks XML exemplar existed anywhere in the corpus carrying any Speed attribute before this (zero on our 6 MX goldens, zero in {LD}'s sequence exports). Rather than guess, one MAtricks was set with X+Y speed at the desk, exported, and read back: **live property dump on `MX 157` confirmed `SpeedFromX` / `SpeedToX` / `SpeedFromY` / `SpeedToY` (plus the Z pair)**, alongside `FadeFrom`/`To` and `DelayFrom`/`To` per axis — casing follows the `PhaseFromX` convention. **`MX 168` then proved the authored dialect accepts Speed AFTER the Phase block**: imported and read back `SpeedFromX=240.0 SpeedFromY=60.0` exact. {LD}'s own desk order leads each axis triple WITH Speed (`SpeedFromX, PhaseFromX, PhaseToX, SpeedFromY, ...`) on his `StandardRecipe` wrappers — that order is **NOT required** on a MAtricks pool object; Speed-after-Phase is proven to work there.

**Scope shrank on inspection — only ONE of three candidate 2D figures actually needed a real ratio.** Breakdown 2/1 bakes X=120 Y=120 (1:1 — both axes at rail, so a plain 2D phase MX + a per-part Speed Scale reproduces it with no special object needed) and Swell Dim#4 bakes Y=`'Stop'` with `PhaseY 0->0` (Y entirely inert = the figure is X-only). **Only Swell Dim#3 needs real ratios** (X:Y = 2:1 on Strike M, 4:1 on the Lin/CL populations). **Check whether a ratio is actually real before minting a speed-carrying MAtricks object** — most candidates resolve to the existing phase-only + Speed Scale pattern.

## Where the gear number comes from — a third gear family added, 2026-08-01 [0801-2cLD]

**SONG_I's 270 BPM against a 135 rail is DOUBLE TIME** (Dave confirmed) -> **Speed Scale ×2**, a MULTIPLY gear — the existing "SONG_A Synth-Swell" ÷2 precedent generalizes into a full multiply lane, not just divide. Half of SONG_I's phaser energy runs double-time; it is that song's dominant gear, not an outlier. **⚠ The ×2 gear's serialization TOKEN is UNATTESTED in the corpus** — only `One`/`Div2`/`Div4`/`Div16` have ever been seen in a desk export. Pin the multiply-family spelling via a scratch export before any emitter bakes a double-time gear into authored XML.

## Where the gear number comes from — the exact formula and wrapper path, 2026-08-04 [0803-3cLD]

**CONSTRAINING (G=0.7).** Speed Scale is a **Part attribute, set per cue**; its value is
**{LD}'s wrapper `SpeedFromX` ÷ the song's BPM.** The wrapper StandardRecipe this divides
lives at **`Part/DependencyExport/Dependency/Preset/StandardRecipe`** — the same per-population
wrapper pattern documented in `source-matricks-wrapper-recipe-encoding`, read here for its
SPEED axis rather than its spread axis. This is the concrete mechanism behind "read it off
{LD}'s own baked speeds" above: divide the wrapper's `SpeedFromX` by BPM and the result is
the gear (÷1, ÷2, ×2, …) to set in Cue Speed Scale.

## Working lane confirmed, 2026-08-05 [0805cLD] — read `SpeedFrom` directly off the Phaser Preset

**Dave, ruling on practice:** the Speed Scale multiple comes **directly from `SpeedFrom` in
each Phaser Preset.** This sharpens the wrapper-path formula immediately above
(`SpeedFromX ÷ BPM`, read at `Part/DependencyExport/Dependency/Preset/StandardRecipe`) — the
**per-preset `SpeedFrom` read is the working lane** in practice, not a distinct mechanism.

**[0805-2cLD] CORRECTION — x2 IS an attested Speed Scale token** (Dave 08-05, enters speed scales directly). The prior "Div8 and x2 UNATTESTED" narrows to **Div8 only**. Attested ladder: Div16 · Div4 · Div2 · One · x2.

History: corrected 2026-08-05 [0805-2cLD] — x2 attested by Dave; prior unattested pair narrowed to Div8 only.
