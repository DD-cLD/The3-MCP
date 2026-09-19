---
doc_id: case-study-song-m-build
title: "Case study — one song, cold start to heard-under-timecode, in one session"
status: active
verified: grandMA3 onPC 2.4.2.2 (Mac), MCP bridge, safety mode `rehearsal`
source: "Banked build record of the session, every figure verified live at the time; names mapped per the release placeholders table (README)"
---

# CASE STUDY — SONG_M: cold start → heard under timecode, one session

**What this is.** The full arc of one song rebuilt from an inherited showfile onto a role-based,
recipe-driven build, with the real numbers. It is the worked example for every law in
`playbook/` and most of `concepts/`. **Read the numbers — they carry the mechanism.**

**Who did what.** The human ruled taste, gears, timecode, and every clearance. The AI executed
reads, arithmetic, emission, certification, hash chains, imports, binds, and every census.
🔴 NOTHING FIRED WITHOUT A WRITTEN BATCH SPEC AND THE HUMAN'S WORD; NOTHING WAS TRUSTED ON ITS ECHO.
That division is the method, not a caveat on it (§9).

---

## 1 · Frame

| item | value |
|---|---|
| Board state at start | 6 of 19 songs heard. SONG_M = the largest remaining build |
| Inherited main | seq 2300 — 230 recipe lines, 29 cues, 30 phaser bind sites |
| Inherited aux | 2301–2304 (Kick 1, Snare 1, Snare 2, Kick 2) — edited IN PLACE by the human pre-build; TC aux tracks stay on them; no new aux minted |
| Target | new main at seq 2310 |
| Rig | onPC 2.4.2.2 (Mac), MCP bridge, safety mode `rehearsal` |
| Why this song is the exemplar | most figure-complex of the 19: 12 wrapper names, 4 leaf shapes, XY drive, an embed-vs-cooked conflict — every pattern fires once |

## 2 · Bring-up census — by name, before anything fires

| object | state |
|---|---|
| Seq 2310 | EMPTY · seq 2300 present + 4 aux, by name |
| Preset pool 21 | source figures 21.2300–2307 (8, by name) · mint block 21.2320+ EMPTY |
| MAtricks pool | 100–195 occupied (prior songs) → this song mints from 196 |
| Phaser templates (live) | 21.51 SINE (copy-only) · 52 LINEAR (copy-only) · 53 RAMP UP · 54 RAMP DOWN · 55 SNAP · 56 TRAPEZE · 57 CHASE · 58 SINE ½ · 59 LINEAR ½ · 60 RAMP UP ½ |

Law applied: `empty-census-deserves-selector-suspicion` · `state-the-scope-with-the-count`.

## 3 · Embed read — 12 wrappers → 4 leaf shapes

Source: the inherited sequence export, 17.7 MB XML. The source LD binds **no** MAtricks pool
objects; all per-population spread lives inline on *wrapper* StandardRecipes inside each
phaser preset's `DependencyExport` embed (`source-matricks-wrapper-recipe-encoding`).

**12 wrapper figure names collapse to 4 leaf shapes** via embedded `Preset=` indirection.
Wrappers carry ALL per-population MX (XWings/XGroup/XBlock/XShuffle · PhaseFrom/To X·Y ·
SpeedFromX/Y).

| leaf | steps (`?`/`*` stripped) | classified | mint source |
|---|---|---|---|
| sine-bump dimmer | 100 w25 t100 → 0 w100 t25 | BUMP | ← template 21.58 |
| ramp-minus dimmer | ~0-width spike @100 → fade to 0; Measure raw 67108864 = 4×2²⁴ | RAMP DOWN | ← 21.54 (+ Measure 4, human's hand) |
| square dimmer | 0↔100, Trans 0 both steps, Measure 4 | SNAP | ← 21.55 (+ Measure 4, human's hand) |
| 20×20 relative P/T circle | SELECTIVE — 25 per-fixture rows, relative values | copy-only content | ← a prior song's OWN mint at 21.1921 — never the imported original (21.245) |

Three catches, each a standing law now:

| catch | what happened | law |
|---|---|---|
| **The Y-catch** | chorus figure drives X **and** Y (SpeedFromY 58.5 BPM, PhaseY 0→90°) on all 3 RGB populations. An X-only read ships a flat chorus. | "CHECK Y EVERY TIME" — `source-figures-are-recipe-presets-spread-read-law` |
| Embed vs cooked row | embeds said 58.5 BPM; cooked residue said 117 on 9 sites | **embeds rule** (standing since two builds prior); human previz-approved at Div2 |
| Join law | embed population "Spots + BEAM (Grid)" and site group "Spots + Beam [Sym]" are the same population | join by **crosswalked target**, never by the source's group-name string — `inherited-file-membership-is-ground-truth` |

Measure encoding: `phaser-preset-xml-measure-speed-fixed-point-encoding`. Copy does not carry Measure: `phaser-copy-does-not-carry-measure`.

## 4 · Mint plan → desk

**Shapes:** 21.2320 BUMP ← 58 · 2321 RAMP DN ← 54 · 2322 SNAP/PWM ← 55 · 2323 PTC CIRCLE ← 21.1921.
Copy + Label in one gated expression, name-readback inline.

**MAtricks 196–209: all 14 minted fresh, ZERO reuse — and the zero was earned, not assumed:**

| step | result |
|---|---|
| live census of 100–195 first | no exact literal match on any want |
| one candidate (145) | sat on the lying-names ledger → excluded on principle |
| near-matches that were NOT matches | X-only variants of XY wants (188, 194, 163) · sign difference (176 = X+360 vs want X−360) · mirror variance (186) |

MX property schema was **live-dumped off an existing object**: 96 properties; recipe attrs map 1:1
(XWINGS/XGROUP/XBLOCK/XSHUFFLE/PHASEFROM–TO X·Y/PHASERTRANSFORM/XINVW). Copy-and-tweak via Lua
`:Set()`, full-property readback in the same expression. Phase fields read negatives honestly
(`PX0.0to-360.0`); the u32 wraparound lie is integer-shift-scoped.

**Checkpoints:** SaveShow v.128 pre-mints → v.129 post-mints, each disk-verified
(`GetPath(Enums.PathType.Showfiles)` + `io.popen ls` — the shows dir is not reachable by a
filesystem tool over the bridge; this lane replaced it). `saveshow-discipline-and-mcp-tier` ·
`save-disk-verify-mtime-delta`.

**Tier discipline:** every Store / Copy / SaveShow / Import / Export = Tier-2 confirm gate on the
EXACT wrapped command; Go+ = Tier-3. Grant → resend, per the batch spec the human cleared in
writing. `playbook/console-hard-rules.md`.

## 5 · Emit → certify → import

**Reconciliation identity** (`tourshow-two-pass-build-method`):

```
230 source lines − 1 HELD (spot-colour line on a group with no rostered fixture class)
                 − 0 law-drops + 0 STB expansion (1 off-line site only) + 0 openers
                 = 229 emitted · residual ZERO
```

Per-part census matched the prework sheet digit-for-digit: P1 18 · P2 9 · P4 48 · P5 51 · P6 6 · P7 52 · P8 45.

Colours: two per-song palette slots, 23 + 16 bind sites. The human approved the blue by watching
previz — the decision was presented as a stated default, then cleared.

**Certify:** attr-for-attr serialization against the **heard sibling** (the previous song's
shipped file) across Sequence / Cue / Part / StandardRecipe — zero mine-only signatures.
Golden law: export-backs carry cooked PresetData = serialization authority only, never re-import
(`import-resolver-laws`).

**Deploy:** sha256 identical at every hop (build container → synced drive → `gma3_library`).
Import echoed OK — **the echo proved nothing.** Export-back census BY NAME at bind scope:

| object | census |
|---|---|
| StandardRecipes | 229/229 |
| BUMP binds | 20/20 |
| PWM binds | 6/6 |
| RAMP DN binds | 3/3 |
| CIRCLE binds | 1/1 |
| Strict lines | 13/13 |
| colour A / colour B | 23/23 · 16/16 |

Emit lane: `kit/cld_songbuild.py` (the mechanical half; taste stays with the human — see its docstring).

## 6 · The macro bind lane — "the macro is less tool calls" (human's ruling)

| step | detail |
|---|---|
| authoring | 30 MX binds as **Macro 120** — one `Lua "…"` handle-assign line per bind; indexes computed from the authored file's structure (cue / part / StandardRecipe child order) |
| why Lua, not CLI | plain-CLI `Assign … At` had failed on a prior song; Lua handle `:Set('MAtricks','Default.MAtricks.N')` is the proven form (`recipe-line-cli-addressing-and-list-readback`) |
| test-first | ordinal-1 bind fired alone via `send_lua` and read back **before** the other 29 were authored into the macro |
| import → **line-readback diff** | all 30 command strings read back off the console, sha-compared to authored — EXACT — then and only then Go+ |
| bind census | **30/30, zero fails**, walked object-by-object |
| economics | 3 gate cycles vs ~10 chunked-Lua sends. Residual asset: any re-import of 2310 rebinds with one Go+ |

Race hazard on macro label lines: `macro-lua-label-race-needs-wait`.

## 7 · Timecode cutover + verify — the human's hand, the AI's census

- The human cut the main himself (2300 → 2310 at track .1.1); aux stayed on his edited-in-place 2301–2304.
- Census at **true event depth** — Track → TimeRange → CmdSubTrack → **CmdEvent**:
  main → 2310, 25 events · aux → 2301 / 2302 / 2303 / 2304 with 180 / 158 / 190 / 344.
  Target-only reads lie on an event-emptied track; **the count is the verify** (`tc-track-target-cutover`).
- Lua truths banked en route: cue `:Get('No')` returns ×1000 fixed-point (cue 6 = 6000) · a
  property returning ZERO values breaks bare `tostring()` — guard every read as `tostring((…))`.
- Desk sealed v.133. **Song 7 of 19 heard. Elapsed: one session, cold start to heard-under-timecode.**

## 8 · The clearance protocol that wrapped every write batch

1. Written batch spec (objects, numbers, exact commands) → human clears in writing.
2. Tier-2 confirm gate fires on the EXACT wrapped command → grant → resend.
3. Readback by name in the same expression (never trust the echo).
4. SaveShow checkpoint, disk-verified, before and after each mint batch.
5. Announce brackets around the batch in the log.

## 9 · Division of labor — the authority boundaries

| **the human ruled** | **the AI executed** |
|---|---|
| taste · the blue · gears at the rail (117 hypothesis; the one unattested-gear want on cue 2.1 flagged, his call) | reads (embed, cooked, live pool) · the arithmetic · the crosswalk join |
| Measure hand-edits on 2321 / 2322 | emission · certification against the heard sibling · sha chains |
| the timecode cut | imports · the 30 binds · every census, at the depth where the truth lives |
| every batch clearance · previz judgment (watched and approved) | nothing fired without his word; nothing trusted on its echo |

That is the method: **language and judgment on one side of the pass, mechanism and verification
on the other, and a written gate between them.**

---
*Placeholders: `SONG_M` = the song · source LD = `{LD}` in the concepts · see README §Placeholders.*
