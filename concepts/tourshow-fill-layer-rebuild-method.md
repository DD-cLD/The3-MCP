---
id: tourshow-fill-layer-rebuild-method
title: "{LD} fill-layer anatomy decoded + our portable rebuild method — proven end-to-end on SONG_T, generalizes per-song to all 18 remaining"
role: programmer
tags: [tourshow, festival, fills, timecode, phaser, sequence]
when_to_load: "Before decoding a {LD} fill/bump layer or rebuilding any of the remaining 18 songs' fill/aux sequences — the cue anatomy, the tempo-gear speed decode, the portable-artifact rebuild steps, and the per-song generalization table"
status: active
source: "findings/INBOX.md [0729cLD] 2026-07-29, live 2.4.2.2 + file reads (gb_fill1/gb_fill2 exports, 19 TC exports); wraps/2026-07-29-song-t-complete-fills-cutover-prework.md"
verified: grandMA3 onPC 2.4.2.2 (Mac)
supersedes: []
superseded_by: null
---

**Portability doctrine (Dave):** {LD}'s fill layers work on our rig but not necessarily every future tour rig. **Record each fill's design INTENT as the durable artifact, then re-point the GROUP per stop for best effect** — fills get re-filled (re-grouped), never re-authored, at each new venue.

## {LD}'s fill anatomy, decoded (from the `gb_fill1`/`gb_fill2` exports)

**FILL 1 (Seq 1501):** cues `OffCue(Release=Yes)` / `CueZero` / `1 [Full]` / `2 [0/Fill 1]` / `3 [0]`, all `TrigType=Follow` — the TC's 1-2-1-2 alternation is a Full/0 bump. Binds: `Strike M [RGB] (Grid) (Fest)` ×2 + `(Lin)` ×1 + `WASH FEST [RGB] (Grid)` ×2; Values: `Dimmer.Full` / `Dimmer.0` ×2 / `Phaser.Dim_PWM_THIN#2` / `Phaser.Fill 1`.

**FILL 2 (Seq 1502):** single cue `1 [Fill 2]` (Temp-fired); binds `Strike M [RGB] Fest` Grid+Lin; Values `Phaser.Dim_PWM_THIN#8` / `Phaser.Fill 2`.

**Both fills:** `XShuffle 5` (F1) / `7` (F2), `ShuffleMode=Auto`, `PhaseFromX 0` → `PhaseToX 360`, Speed fixed-point **`38867217`** = 2.3166 Hz = **139 BPM exactly** — tempo-locked and baked in {LD}'s file. **Ours ride the Sequence Speed override (set to BPM) instead of the baked value** — Dave's ruling. Cooked `PresetData` rides along in the export (7/3 blocks) — strip it per the recipe-only doctrine (`recipe-output-precedence-and-cooking-doctrine`).

**Fill target CONFIRMED:** Dave's belief that the fills hit "STRIKE M FEST RGB" — originally flagged `[VERIFY]` (name-only, and Strike M labels have a JDC1-liar precedent, see `inherited-file-membership-is-ground-truth`) — is now **CONFIRMED** by a `GROUP_TRUTH` membership cross-check (Strike M [RGB] (Grid) (Fest) = Color Strike M ×336 subs, truthful at the group layer; the liars are specifically the US/DS/SW Strike M groups) and by the fill decode itself. Dave's "full setting" (from the MAtricks note below) resolves to the `[Full]` cue.

**⚑ Name-bind hazard:** {LD}'s own preset pool carries silent duplicate-suffix presets — `Dim_PWM_THIN#2` / `Dim_PWM_THIN#8` — the same MA3 silent-`#2` auto-suffix behavior documented in `cld-sandbox-and-namespace`. **Slot-address these, never name-reference them, in any XML we author** that touches {LD}'s pool.

**Fill MAtricks note (Dave):** {LD}'s fill MAtricks carry SHUFFLE settings plus a "full setting" — now decoded as the `[Full]` cue above. Ours take speed from the Sequence Speed override rather than the baked value.

## Speed/gears decode — {LD}'s tempo palette has THREE gears, not one

**Fill wrappers carry `SpeedFromX="139.00 BPM"`** (the standing recipe on the wrapper SR, easy to miss on a first extraction pass). **Forte (All)'s line carries `SpeedFromX="34.75 BPM"` = 139/4.** Combined with the existing `Intro 1/1 Spot Dim` decode (0.2896 Hz = 139/8, an 8-beat/2-bar cycle — see `tourshow-authoring-contract-v01`): **{LD}'s speed palette is tempo ÷1, ÷4, ÷8** — three gears, not a single constant.

**Dave's ruling:** all main-list phasers need slowing, via the per-cue-part **Speed Scale** setting, with **Sequence Override set to BPM**. **Refinement (this session): ÷8 is one of {LD}'s three gears, not the only one — per-figure judgment applies rather than a blanket ÷8.** Check which gear a given figure actually used before choosing the Speed Scale divisor for its cLD replacement. Ours ship speed-unbaked in all cases; the Sequence Speed override (BPM) is the desk knob that supplies tempo.

## The rebuild method — proven end-to-end on SONG_T (Seq 1511/1512)

1. **Decode** {LD}'s fill export(s) for cue/bind/spread/speed anatomy (above).
2. **Author** small, portable artifacts referencing cLD objects only — this build used **5 files**: `cld_ow_fill_burst`/`shimmer`/`rivale_bump` (presets, for `21.1525`/`26`/`27`) + `cld_fill1_seq`/`cld_fill2_seq` (for Seq `1511`/`1512`).
3. **Smith-certify before deploy:** burst = PASS; rivale_bump = PASS, attr-exact vs the golden `Dim_Sin_Bump`; the rest = PASS-WITH-FLAGS, all flags deliberate deltas (`UET=No` vs the golden's `Yes`; `Note=139` added per the 1510 precedent; speed shipped unbaked per Dave's override ruling; shimmer's `GridPos=0` vs the golden's `2^64-1` sentinel).
4. **Byte-exact deploy, verified:** 5/5 sha256 match across container → `generated/` → `gma3_library` datapools.
5. **Checkpoint, then import:** `v.39` pre-import checkpoint → `Import Preset` 21.1525/1526/1527 + `Import Sequence` 1511/1512 (all OK, 31-66ms) → **object-level census EXACT**: preset names clean (no silent `#2`), 1511 binds `Group 201 × Preset 1.5` / `1.15+21.1525 × Group 416` / `1.15`, 1512 binds `21.1526 × Group 416`, names `cLD FILL 1`/`cLD FILL 2` → **v.40 on disk** (113,320,505 B, 20:27).
6. **Set the Sequence Speed override (BPM)** on 1511/1512 (desk step, Dave).
7. **Re-point TC 106 tracks 2/3 `Target`** → 1511/1512, using the Target-change cutover mechanic (`tc-track-target-cutover`).

**Import dialect confirmed clean in this same build:** SR-level spread attrs (`XShuffle`/`XBlock`/`PhaseFromX`/`PhaseToX`) authored as plain attributes directly on the cue-part `StandardRecipe` import correctly and read back exact via `:Get` (`XShuffle=5`/`7`, `XBlock=7`, Phase `0→360` all exact) — the flattened lane (spatial attrs on the cue line, instead of {LD}'s wrapper-preset pattern) is proven; wrapper presets are unnecessary for spread/shuffle. Full mechanical detail in `import-resolver-laws`, which this build's import census extends.

## Milestones (proof the method holds)

- **FILL IMPORT CHAIN LANDED, CENSUS 100%** (above, v.40).
- **AIR-PIX BATCH LANDED VIA LIVE ASSIGN LANE:** 7 lines created on existing empty `P3 PIX` parts, census 7/7 exact, `SaveShow v.41` **on disk** (113,394,086 B, 21:39) — see `assign-cli-recipe-line-grammar` for the CLI mechanic this used.
- **FILLS LIVE UNDER TC:** all three TC 106 tracks re-targeted to cLD's sequences, running complete at v.40 — see `tc-track-target-cutover`.
- **FILLS CONFIRMED BY EAR** (Dave, at the desk): SONG_T played back complete with both fill layers — Dave's words: the fill sequences are what make the song complete. **SONG_T = DONE AND HEARD, v.41.**

**Live bump buttons (forward-looking design ask, not yet built):** Dave wants a few bump executors he can ride live by hand, as a manual-ride layer alongside the TC-fired bump lane — see the extension in `tc-bump-button-architecture`.

## Per-song aux architecture — this method generalizes to all 18 remaining songs

**Decoded from the 19 TC exports on disk (zero console):** per-song aux layers are **per-song sequences** — names carry the song (e.g. `'Kick 1 (SONG_B)'`) — and **sequence number = exec object + 1** (song-t-verified, consistent with the exec/seq relationship in `tc-track-target-cutover`).

**Aux counts per song:** SONG_A 8 · SONG_Q 6 · SONG_E 5 · SONG_H/SONG_B/SONG_D/SONG_L/SONG_M 4 · SONG_O 5 · SONG_C 3 · SONG_J/SONG_N/SONG_F 2 · SONG_I/SONG_K 1 · **SONG_G/SONG_R/SONG_P 0 (main-only, no aux layer)**.

**Main sequence numbers for the 18 remaining songs:** 1000, 1100, 1200, 1300, 1400, 1600, 1700, 1800, 1900, 2000, 2100, 2200, 2300, 2400, 2500, 2600, 2700, 2800.

**The fill/bump rebuild method above = the SONG_T fill method, applied per song.**

**Relation:** `tc-track-target-cutover` (the TC-side half of putting a rebuilt fill under timecode) · `tourshow-seq1510-build-record` (the SONG_T build this fill layer completed) · `tourshow-authoring-contract-v01` (the phaser-figure spec-read posture this speed decode follows) · `import-resolver-laws` (the general import resolver families the SR spread-attr proof extends) · `assign-cli-recipe-line-grammar` (the Assign-creates-lines mechanic used for the air-pix batch) · `inherited-file-membership-is-ground-truth` (the labels-lie doctrine the Strike M Fest confirmation corroborates).

History: none — anatomy decoded, method executed, and generalization stated in one session, 2026-07-29.
