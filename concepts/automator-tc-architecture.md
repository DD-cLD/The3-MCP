---
id: automator-tc-architecture
title: "The show-run automator decoded: LTC → a 24h timecode canvas of half-hour blocks by show position → a token-named cue whose CMD fires the song macro → one shared SongStart macro. TC TIME IS SONG IDENTITY, and there is nothing resident."
role: programmer
tags: [ma3, timecode, showcontrol, plugin, macro, v2.4, tourshow]
when_to_load: "Before touching any part of an inherited hands-off show-run chain — adding a song, correcting an offset, adding a per-song action; the whole chain is native objects and the single touchpoint is one macro line"
status: active
verified: grandMA3 onPC 2.4.2.2 (Mac), EU tour leg 2026-08
source: "findings/INBOX.md [0808-4cLD] (the decode, all Tier-1 reads + one gated census) · [0808-5cLD] · [0808-9cLD] · [0808-10cLD] (Dave verified end-to-end under real Art-Net TC) · [0812-2cLD] (Dave's edits censused) 2026-08-08→12"
supersedes: []
superseded_by: null
---

## The chain (no plugin runs at showtime)

```
LTC slot 1
  → Timecode 1 'Automator'   — 24h canvas, ONE track, one Go+ event per song
    → Sequence 1 'AUTOMATOR' cue N — cues NAMED the song tokens, in SHOW ORDER, empty parts
      → part-0 CMD `Go+ Macro "<token>"`   (COMMANDENABLED = 1)
        → the song macro
          → the shared SongStart macro
            → the show-control toolbox call
```

**Every link is a native object.** Timing authority is 100% native TC + CMD. See `plugin-code-runs-at-showfile-load` for why the Lua toolbox in the last link is a subroutine, not a service.

## The lattice: TC time is song identity

Events sit on **half-hour blocks by show position** — event *N* ≈ (N−1) × 30 min, trimmed a few seconds early on some songs to the actual LTC start of that song's playback file. Each **per-song TC show's `OffsetTCSlot` is that song's REAL LTC start**, and it must agree with the automator event that fires it. Verified to the frame against decoded playback WAVs.

**The blocks continue past the live set by song number** — which meant a song added later had its slot predetermined by the scheme rather than chosen (the pilot's provisional value turned out to be the scheme's own answer). **When adding a song: add the automator event at its block, add the token-named cue with its CMD, cut the playback to that base, set the TC show's offset to match.**

## The song macro pattern, and the single touchpoint

Each song macro is three lines: set the `selectedsong` global to the token, set `bpm`, then call the **shared `SongStart` macro**. That shared macro is **one line of Lua**.

**⇒ One line added to the shared macro gives EVERY song a new per-song action, with zero per-song edits.** That is how the blocking-card swap and the video clip-connect were added — a second line calling one toolbox function that reads the `selectedsong` global and does both (`appearance-image-swap-blocking-cards`, `resolume-dmx-one-hot-clip-select`).

**Design call worth carrying:** the per-song action rides the **shared macro**, not eighteen mark cues. Mark-cue CMDs are orphaned by sequence renames; the macro lane is rename-immune (`name-token-single-holder-cutover-law`). Trade-off: a **manually-fired** mark cue will not pull the per-song action — the mark-lane CMD pass is a five-minute option once renames settle, if wanted.

## Field-leak gotcha in the offsets

One TC show's `OffsetTCSlot` carried an odd value that mismatched its own automator event — and **a second show carried the identical odd value**. Two shows sharing one wrong number is a **store-time field leak from a template**, not a design choice; the template TC show was found carrying exactly that value. **Measure the offset from the playback file's own LTC rather than inheriting it**, and suspect any two shows that agree on an odd number.

## Verification standard

The chain was proven **end-to-end under real Art-Net timecode**, hands-off, and then ran **live in a show**: TC in → automator → song macro → toolbox → page/sequence/mark/BPM + blocking card + video clip. Census after every edit at **CmdSubTrack depth** — targets by name, event counts exact — never on the echo.

**Relation:** `plugin-code-runs-at-showfile-load` · `timecode-assertprevevents-and-goto-seam-controls` (the seam knobs on these TC shows) · `tc-slot-enum-internal-default` · `name-token-single-holder-cutover-law` · `export-timecode-tc-event-xml-schema` · `tourshow-playback-architecture-doctrine`.

History: none — decoded 2026-08-08 by read-only census, extended and verified in show conditions through 2026-08-19.
