---
id: timecode-assertprevevents-and-goto-seam-controls
title: "Timecode seam controls live on the Timecode object: GOTO and ASSERTPREVEVENTS. Fleet law — Assert TRUE on song shows (heals a cut's seam), FALSE on the automator (an assert across a block jump would fire every passed song's CMD chain)."
role: programmer
tags: [ma3, timecode, showrun, v2.4, tourshow]
when_to_load: "Before playing a cut-down/short-version bounce whose LTC jumps forward mid-show, or before setting Assert/Goto on any timecode show — the automator-vs-song split is load-bearing, not cosmetic"
status: active
verified: grandMA3 onPC 2.4.2.2 (Mac), EU tour leg 2026-08
source: "findings/INBOX.md [0808-8cLD] (schema + fleet census) and [0812-2cLD] (Dave's spec, 23 shows set, readback exact) 2026-08-08→12"
supersedes: []
superseded_by: null
---

## Where the knobs are

The Timecode object's property schema (~50 properties) carries the seam controls: **`GOTO`** and **`ASSERTPREVEVENTS`**, alongside `AutoStart` / `AutoStop` / `SwitchOff` / `RestartOption` / `LoopMode` and the record family. **The local manual's CLI reference has nothing on jump/resync behaviour — the desk schema was the source.** Dump the object when the documentation is silent.

## Semantics

- **`AssertPrevEvents = true`** — when the playback pointer crosses events without playing them, their **cumulative state is re-established at the landing point**. An assert, not a machine-gun replay.
- **`false`** — the jump simply continues; skipped events never fire and state stays stale until the next event.

**With name-addressed events, both are survivable** — the first post-cut event re-aims the sequence correctly either way (`automator-tc-architecture`). Assert makes the seam *clean* rather than *eventually* clean.

## ⛔ The fleet split (Dave's spec, set across 23 shows, readback exact)

| Show | AssertPrevEvents |
|---|---|
| **The automator TC show** | **FALSE** |
| **Every song TC show** (including the dead ones, for uniformity) | **TRUE** |

**Why the split is load-bearing:** Assert heals seams **inside** a song. On the **automator**, whose events are half-hour blocks each firing a whole song's CMD chain, an assert across a block jump would **re-establish every passed song cue's state — firing the command chain of songs 1..N**. **Assert inside songs, never across them.**

The automator was found set **TRUE** (drift, or a hand) before the pass. The flip to FALSE was not cosmetic.

**Fleet consistency is itself a finding.** The census before the pass showed shows disagreeing on Assert *and* Loop, with one outlier that also carried a wrong offset — the same show that turned out to have inherited a template's leaked field (`automator-tc-architecture`). **Odd-one-out on one property is worth checking on all of them.**

## What this settled

The short-version plan: **zero new timecode shows, zero retiming.** Cut-down bounces carry their edit in the LTC itself (`beatgrid-tc-carried-cuts-and-seam-gap`), so tuning Assert plus a bench test of a real forward jump is the whole job; per-seam "landing" events are a fallback garnish, likely unneeded.

**Relation:** `automator-tc-architecture` · `beatgrid-tc-carried-cuts-and-seam-gap` · `tc-slot-enum-internal-default` · `df-2997-drop-frame-timecode-math-and-rate-switch` · `tc-cutover-last-and-delete-eats-events-doctrine`.

History: schema and fleet census 2026-08-08; the split ruled and applied across 23 shows 2026-08-12.
