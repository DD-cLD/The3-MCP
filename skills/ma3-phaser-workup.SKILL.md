---
name: ma3-phaser-workup
description: The {TOUR} per-song phaser chain — read {LD}'s figures (X AND Y, unfiltered), pool-block census, copy-source via content hash with per-song minting, Speed Scale gears, MAtricks spread. Use whenever a song's phasers are read, minted, gauged, or bound. Triggers on phaser, figure, pool 21, FIGURES sheet, decode, copy source, Speed Scale, gear, MAtricks, MX, spread, X and Y.
---

# MA3 Phaser Workup — read → copy → gears → MX

The chain that eats sessions when a detail slips (Dave, 08-05: "the toughest part
each time — missing the details in the phasers, X and Y, MAtricks"). Each step
below is a historical miss, inverted. Dialect + math arming for any XML authoring
is **ma3-phaser-gate** — invoke it before writing phaser XML. Paths relative to
`WORKING/`.

## 1 — READ ({LD}'s export)

- Start from `generated/prework_batch/FIGURES_<seq>_<song>.csv` +
  `decode_phasers()` (in `generated/songbuild/cld_songbuild.py`).
- **Dump driven Attributes UNFILTERED** — X, Y, Z, Phase, Speed, per figure.
  **CHECK Y EVERY TIME**: the recurring miss is an X-only read on a figure that
  also drives Y (a pan+tilt circle read as a pan sine).
- A Selective row set at **cell-level dot-IDs** = fixture references baked in —
  that preset cannot be re-pointed by swapping the group; it must be re-authored
  (paid for on SONG_A's Synth Swell).
- Phase span / GridPos are informational only — **our phase rides MAtricks,
  never baked**.
- `*`/`?`-prefixed fixed-point values appear in some exports — strip before
  arithmetic (08-01 guard, already in the kit).

## 2 — COPY (mint per-song; a known source = zero decode)

- **Every song mints its OWN copies at `21.<century>20+`** — cross-song binds are
  outlawed (`tourshow-authoring-contract-v01`, Dave 08-03).
- Sheet status **COPY SOURCE KNOWN** → `Copy Preset 21.<src> At 21.<dst>` +
  `Label` (inner quotes `&quot;`-escaped). Zero decode.
- Sheet status **NEW CONTENT** → decode steps/width/trans from the export and
  author per **ma3-phaser-gate**.
- The hash matches step tuples + Attribute + Measure and EXCLUDES Phase (rides
  MAtricks) and Speed (unbaked) — a match is the same SHAPE; gear and spread are
  still set per site.
- Templates **21.51/52 are COPY-ONLY on console** (no file-side XML exists).
- **Census the POOL BLOCK, not just sequence refs.** Two censuses, labeled:
  what exists at `21.<century>20+` (catches orphan copies and non-Dimmer
  figures — the 21.2402 lesson) and what the sequence actually binds
  (bind-site census). A count without its scope is a defect.

## 3 — GEARS (Speed)

- Speed ships **UNBAKED** — tempo is Speed Scale at the cue part
  (`tourshow-speed-architecture-standing-ruling`). Never bake {LD}'s BPM.
- `decode_phasers()` reports his baked BPM; convert against the song BPM.
- **Attested gear tokens: One · Div2 · Div4 · Div16 · ×2** (×2 attested by Dave
  08-05 — entered directly on Speed Scale). Div8 remains
  UNATTESTED — wanting one goes on the desk list for Dave, never invented.
- Fade math regenerates per song from BPM (`beats_to_seconds`) — never copy
  another song's literal seconds.

## 4 — MX (MAtricks)

- Spread lives in the **bound MAtricks object**; phase formulas are LITERAL —
  full spread = `360 − 360/N` (CARD_AUTHORING → PHASE MATH block, verbatim;
  never encoder-bar values in pool-stored objects).
- **Block counts for N: QX40 = 5 · JDC1 = 12 · PLINE = 16.** Fractional spread
  values are legitimate outputs, not errors.
- Reuse an existing MAtricks slot only on **EXACT literal match** (101 Full
  Spread / 102 Half Spread). Anything else mints at **171+**, and only after a
  **LIVE re-census** of the pool — slots move between sessions; any sheet's slot
  map is stale by definition.
- Wrapper presets are per-POPULATION, matched by the **crosswalked cLD TARGET**
  (submap), never by {LD}'s grouping.

## 5 — PROVE

- Reconciliation identity per song at zero residual; lint + `ET.fromstring` on
  every emitted file.
- After the song's aux exports land, re-run `generated/figure_hash/figure_hash2.py`
  before trusting any copy-source call on the next song.
