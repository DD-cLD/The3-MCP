---
id: tourshow-authoring-contract-v01
title: "{TOUR} authoring contract v0.1 — their STRUCTURE, our content: phaser preset = the temporal figure, group = who, MAtricks bound at the SEQUENCE = spatial; one phaser copy per FIGURE (reversed 07-30; was per use-site); cLD-prefixed; ours at 21.<century>20"
role: programmer
tags: [tourshow, festival, doctrine, contract, phasers, matricks, transplant]
when_to_load: "Before authoring ANY {TOUR} cue content — this is the closed contract for what each object is responsible for, where ours are numbered, and what gets copied vs referenced"
status: active
source: "Dave rulings 2026-07-27/28 [0727-2cLD], dictated across the architecture session"
verified: grandMA3 onPC 2.4.2.2 (Mac)
supersedes: []
superseded_by: null
---

**Keep {LD}'s song STRUCTURE. Replace every layer of content.** The cue list shape is
already blocked out and correct; everything inside it becomes ours.

## Responsibility split — four objects, bound at the cue-part recipe line

| Object | Carries | Notes |
|---|---|---|
| **Phaser preset** | the **temporal figure** | a phaser RECIPE (not baked) referencing a **stock Shape** + a **Universal Dimmer preset**. Direction is baked HERE — `PlaybackDirection` does not exist at the cue-part line (`recipe-line-playback-properties`), so the set needs forward AND Alternate variants. |
| **Group** | **who** | ours, per `tourshow-group-contract-v01` |
| **MAtricks** | the **spatial distribution** | **the SEQUENCE references it**, not the phaser. Drawn from a reusable set, overridable case-by-case. |
| **Colour / intensity** | ours | custom colours from video-clip RGB; **universal intensities**, `/Universal` on every store |

Bind lane is proven: `Assign <obj> At Sequence x Cue y Part z`, bare form, routing
**Group→Selection · Preset→Values · MAtricks→MAtricks** (`assign-cli-recipe-line-grammar`).

## The reusable MAtricks set — SOLVED, not to be authored

**Dave's 30 Coachella Spectra Tower MAtricks, imported at pool 111-140.** They bind by `Assign`
alone and are **proven portable across several shows and fixture-group sizes with no phase
adjustment** — see `no-baked-n-portable-phaser-doctrine`, where they are the reference
implementation. Simple phase / wing / group / block variants cover the normal case.

## Phasers — their phaser is a CHECKLIST, not a thing to port

Read {LD}'s per-cue phaser only as the question *"does this cue want a phaser?"* If yes,
author a NEW template phaser and reference ours. **Never reference theirs** — their phasers are
`PresetMode="Global"` but hold per-fixture `Selective` rows with baked phase, so swapping the
group on a recipe line does NOT re-point them.

- **Numbering: ours at `21.<century>20`.** SONG_T → `21.1520` (theirs occupy 1500-1507).
  Generalises across the setlist, since the phaser pool mirrors the sequence century.
- **⚠ ONE PRESET PER USE-SITE — deliberately anti-DRY.** Need the same figure elsewhere? **Copy
  it and reference the copy.** Rationale (Dave): organisation plus local editability — each
  instance stays individually tunable through its own sequence recipe. **Do NOT "optimise" this
  later by consolidating near-identical phasers.** It trades global reuse for the ability to
  tune one moment without touching the others, which is the right trade on a live show.
- **Build a TEMPLATE SET first and copy from it** — DRY at authoring, copies at use.

## Naming — `cLD ` prefix on every cLD-authored preset

Standing law (`cld-sandbox-and-namespace`). Dodges MA3's silent `#2` duplicate-suffix, and
makes provenance readable in a file whose names have lied twice.

## What survives of the decode work

We do NOT port their phasers, so the Selective/baked-N problem never arrives. But a selective
phaser still reads out its **musical spec** — `Intro 1/1 Spot Dim` decodes via the 2^24 fixed
point to 0.2896 Hz = 139/8 = an **8-beat (2-bar) cycle**. **Use the decode as a spec-read for
starting values, not as a port.**

## Status

**CLOSED, 2026-07-28 — every object in the contract is built.** Groups ✓ · colours ✓ (video RGB)
· intensities ✓ (Universal) · MAtricks ✓ (Coachella 30) · positions ✓ (tilt ladder
`festival-position-preset-stacking-and-tilt-ladder` + pan set `2.81-83` Fan/X1/X2) ·
**phaser template set ✓ — 27 templates landed (v.27), the last remaining item, closed
2026-07-28.** See `tourshow-seq1510-build-record` for the build that exercised the completed
contract end to end.


## ⛔ REVERSED 2026-07-30 (Dave) — copy granularity is PER FIGURE, not per use-site

The "ONE PRESET PER USE-SITE — deliberately anti-DRY" rule above is **superseded**. Dave's ruling on the SONG_A build: **one phaser copy per FIGURE**, reused across that figure's use-sites within the song. SONG_A landed **11 copies across 19 use-sites** (`21.1020-1030`).

The old rule's rationale — local editability, tune one moment without touching the others — is preserved as **copy-on-demand**: if a single use-site later needs its own tuning, fork *that* copy at that moment. What is dropped is pre-emptively authoring the cross-product up front.

This also aligns the contract with `compose-at-bind-time-principle`: authoring N copies of one figure before knowing any of them will diverge is pre-multiplying.

Old text kept above for the reasoning, which still stands for the fork case.

## ⭐⭐ FURTHER LOOSENED 2026-08-05 [0805cLD] — a phaser preset is an INGREDIENT; hash count is not object count

**RULED (Dave):** a phaser preset is an **INGREDIENT** — reusable, and usable by MULTIPLE
CUES AT THE SAME TIME. *"We can use the same bump all the way through the show if we
wanted."* **The figure-hash count is NOT the object count — do not mint one object per
content hash.** This loosens the copy-granularity rule further than the 2026-07-30 reversal
above already did: **per-figure was the ceiling, not the floor.** SONG_L ships **5**
objects (`cLD SONG_L PAN SINE` / `SINE` / `BUMP` / `RAMP DOWN` / `COLOR LINEAR`) against **9**
distinct content hashes — full build record: `tourshow-seq2210-song-l-build-record`.

**Companion misread, corrected same session:** the FIGURES sheet's status string
"REUSE-CONTENT — MINT a per-song copy FROM this source (do NOT cross-song bind)" was misread
as "one object per content hash," producing a false 9-object blocker on SONG_L. **The
sheet's REUSE/NEW axis describes where CONTENT came from, not how many OBJECTS to mint** — do
not conflate the two questions.

**Also ruled the same session — composites are SEPARATED, not decomposed:** when one {LD}
preset mixes fixture types/shapes, the parts-per-century explosion already splits by fixture
family, so the composite becomes one part per century with its own bind, never a puzzle to
decompose by hand. Full doctrine and the population→shape join method:
`parts-per-century-emit-pattern-and-et-gate`.

History: extended 2026-07-28 [0728cLD] — Status section updated to CLOSED: the phaser [0728cLD] — Status section updated to CLOSED: the phaser
template set (27 templates, `21.53-73`+`81-86`) and the pan preset set (`2.81-83`) both
landed, completing every object named in the contract.


History: none — ruled by Dave across 2026-07-27/28 [0727-2cLD]. 2026-07-31 [0731cLD] — copy-granularity rule reversed per Dave's 2026-07-30 ruling (per-figure, fork on demand); title updated to match.
