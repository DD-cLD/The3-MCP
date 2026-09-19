---
id: cue-structure-is-tonal-harmony
title: "The cue structure IS tonal harmony — Mark/SET is HOME (the tonic), section cues are the departure, the song resolves back to nothing, and bumps are ornaments that must resolve into the line"
role: programmer
tags: [tourshow, doctrine, design-frame, cues, structure, taste]
when_to_load: "Before structuring, ordering or judging ANY song's cue list — and any time you are unsure whether a proposed cue, bump or movement is tasteful. This is the frame Dave supplied specifically so the programmer can check its own proposals against something rather than guess."
status: active
source: "Dave, dictated 2026-07-27 [0727-2cLD], offered explicitly as a bridge into knowledge cLD already holds; corroborated the same session against the SONG_T sequence export"
verified: grandMA3 onPC 2.4.2.2 (Mac)
supersedes: []
superseded_by: null
---

**Dave's framing, given deliberately as a bridge.** Concert lighting programming is a
hand-to-hand trade craft that is barely written down; tonal harmony is one of the most
thoroughly documented bodies of knowledge in existence. Dave routed around the thin spot
through the thick one: **read the cue structure as harmonic motion.**

## The mapping

| Music | Show |
|---|---|
| **Tonic / home** | the **Mark / SET cue** — the referent everything else is heard against |
| Departure, rising tension | the section cues stepping away from home |
| Pre-dominant (the build) | Prechorus-class cues — tension that *wants* to resolve |
| Voice-leading between chords | the **`>>` decimal cues** — how each line travels |
| Ornament / riff / fill | the **bump buttons** — surface events, never structure |
| Final resolution | the Outro/Blackout return — back to nothing, back to home |

**Why home matters mechanically:** without a clearly established tonic, movement away does
not read as movement — it reads as noise. The SET cue is what makes every later departure
legible.

## It explains a mechanic we already had

`tc-bump-button-architecture` rules that bumps exit via **Release, never Off**, so the channel
falls back to whatever the main sequence holds underneath. Under this frame that IS the
ornamentation rule: **an ornament that does not resolve back into the line is not an ornament,
it is noise.** Release *is* "return to the structural voice." The mechanic was banked first,
without the why; the why was music theory all along.

## Three consequences that fall out

1. **Tension must be WITHHELD to be spendable.** Maximum dissonance in bar two leaves nowhere
   to go. This is the intensity budget of
   `tourshow-go-wild-pair-intensity-budget-and-release-matricks-doctrine` restated — and it
   shows the principle runs at SET level too: the go-wild pair exists so the two songs that
   should peak still can.
2. **The return home should be recognisable but NOT identical.** A final tonic is the same
   chord meaning something different for what preceded it. An Outro is **home with history**,
   not a re-fire of the Mark cue.
3. **Start the movement EARLY — anacrusis.** Begin a move *before* the cue it is meant to land
   on, so the change arrives into an already-travelling gesture instead of starting one. The
   hit lands *into* motion. This is the operational form of Dave's **"tension wants motion, not
   just a level."** It also appears one layer down in the position vocabulary — a pan fan is the
   approach, the tilt is the landing (`festival-position-preset-stacking-and-tilt-ladder`).

## Confirmed by the inherited file's own data

Two checks nobody set up to pass, run against the SONG_T export:

- **Phaser placement.** 5 of the 6 distinct phasers sit on `>>` movement cues; the single
  exception rides cue 6 **Prechorus** — the pre-dominant. The one named cue that gets a phaser
  is exactly the one whose musical job is building tension. **Tension wants motion, not a level.**
- **The tonic bracket is visible in the line counts.** Cue 1 `Mark` is the heaviest cue in the
  song at **26 recipe lines**; cue 27.1 `>>` (the Blackout movement) is second at **16**. Home
  and the return to home are the two largest cues.

## ⚠ Scope — this does NOT promote the programmer to designer

`idea-file-design-programmer-boundary-doctrine` stands unchanged: the design side carries
music, story and "what good looks like"; the programmer carries the full mechanical toolkit and
**decides nothing**. What this frame buys is **structural literacy, not authority** — read the
shape being built, stop proposing things that fight the arc, and flag when a MECHANICAL choice
would break it (a bump that Offs instead of Releases; a build that spends its loudest
vocabulary before the chorus it is meant to set up). **Use it to check proposals, never to
originate intent.**

History: none — given by Dave 2026-07-27 and corroborated the same session against the SONG_T
export.
