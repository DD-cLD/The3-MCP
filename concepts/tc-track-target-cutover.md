---
id: tc-track-target-cutover
title: "⛔ TC cutover = change the TC track's Target — never rename, re-author, or juggle executors; rollback = point Target back"
role: programmer
tags: [ma3, timecode, cutover, v2.4, tourshow]
when_to_load: "Before planning or executing ANY timecode cutover from an inherited/predecessor sequence to your own — change the TC track's Target, don't rename or re-author; also the reference for how a TC track addresses its sequence by name and how its exec-object number relates to the sequence number"
status: active
source: "findings/INBOX.md [0729cLD] 2026-07-29, live 2.4.2.2 (Dave, desk, PROVEN LIVE); wraps/2026-07-29-song-t-complete-fills-cutover-prework.md"
verified: grandMA3 onPC 2.4.2.2 (Mac)
supersedes: []
superseded_by: null
---

**⛔ THE MECHANISM, PROVEN LIVE: a Timecode track drives whatever sequence its `Target` property points at — change the Target, and the whole rename/re-author/executor-juggling problem disappears.** No TC authoring, no renaming objects, no executor gymnastics. Point the track's `Target` at your own sequence and the timecode drives it exactly as it drove the original.

**Live proof (2026-07-29):** Dave changed TC 106 track 1's `Target` from Seq 1500 ({LD}'s SONG_T) to **Seq 1510 (cLD SONG_T)** and watched it run cLD's build with the song — the first light of the tour build. **Rollback = point the Target back to 1500.** Later the same session, all three TC 106 tracks were re-targeted at once — Seq 1510 (main) / 1511 (cLD FILL 1) / 1512 (cLD FILL 2) — and event labels re-resolved live to the new preset names; the show ran complete under TC with every object ours. **cLD can drive this Target change via CLI for the remaining songs** — this is the standing cutover method for the rest of the setlist, not a SONG_T one-off.

**⚠ SUPERSEDES the older "rename-cutover" plan.** Prior sessions (2026-07-27/28) carried an unresolved "TC rename-cutover" method as debt — the assumption was that cutting the timecode over to cLD's sequences would require renaming objects or re-deriving how the TC's addressed executor maps onto a page/exec slot (`13.13.0.5.1499` ↔ "page 106 / exec 115" — see `festival-page-per-song-executor-architecture`). **That whole plan is now dead.** The Target property makes it a one-line change; no rename, no page/exec derivation needed at all. This concept is the definitive record — older records referencing a "rename-cutover" (`tourshow-seq1510-build-record`'s pre-2026-07-29 "What's left," `festival-page-per-song-executor-architecture`'s "rename cutover" language) describe the superseded plan, not what actually shipped.

## TC 106 track identity — three tracks, each targeting a sequence BY NAME

**FILE-SIDE (from `SONG_T.xml`, the TC export):** TC 106 carries THREE tracks, each targeting a sequence **by name**: `SONG_T` → `Sequences.SONG_T` (26 Go+ events, at exec object `13.13.0.5.1499`) · `Fill 1` → `Sequences.Fill 1` (60 Go+ events, at exec object `...1500`) · `Fill 2` → `Sequences.Fill 2` (10 Temp + 10 Temp(Release) pairs, at exec object `...1501`, every `ValCueDestination=0.5.1501.1000` = cue 1). The exec-object triplet (1499/1500/1501) is consecutive.

**DESK-SIDE, CORRECTED AND PINNED LIVE (from the Edit Timecode window):** the track `Target`s are actually **SEQUENCES 1500 `SONG_T` (main) / 1501 `Fill 1` / 1502 `Fill 2`** — the file-side read above found the **exec OBJECTS** (`13.13.0.5.1499/1500/1501`), not the sequence numbers. **Both readings are true simultaneously: exec object = seq number − 1**, now confirmed live for the whole triplet (1499 = 1500−1, 1500 = 1501−1, 1501 = 1502−1). This refines (does not contradict) the "apparent main exec = sequence century − 1 pattern" already on record in `festival-page-per-song-executor-architecture` — that pattern is now an exact, live-confirmed rule for this triplet, not just an apparent one.

**Temp events carry `FromLocalHardwareFader=1`** — recorded hardware presses, corroborating the recorded-bumps model for how {LD}'s fill layer was authored.

**Still genuinely unresolved (unaffected by the cutover mechanism above):** how the exec-object number (`1499`) maps onto a **page/exec-SLOT** (e.g. "page 106, exec 115") is still not derivable from the files — see `festival-page-per-song-executor-architecture`'s open item. **This mapping is now MOOT for cutover purposes** (the Target change doesn't need it), but it remains open for anyone who needs the page/exec-slot number itself for some other reason.

## Milestones (proof the mechanism holds under real use)

- **SONG_T FIRST FIRE:** Seq 1510 ran under TC 106 with the song — first light of the tour build. Look read thin at this point (known causes: phasers ~8x too fast pending the Speed Scale ruling, Forte All→RIVALE not yet bound, Fill 1/Fill 2 layers not yet built, plus the design ask for this song is deliberately low on lights). Crosswalk itself ruled good by Dave at this checkpoint.
- **FILLS LIVE UNDER TC (Dave: "It lands! Send It!!!"):** screenshot-confirmed all three TC 106 tracks re-targeted to cLD's objects — Seq 1510 cLD SONG_T / 1511 cLD FILL 1 / 1512 cLD FILL 2 — event labels re-resolved to cLD's preset names (`[0/cLD OW FILL BURST]`, `[cLD OW FILL SHIMMER]`), running with the song at v.40. Team saying coined this session: **SEND IT.**

**Relation:** `festival-page-per-song-executor-architecture` (the per-page executor architecture and the still-open page/exec-slot mapping) · `tourshow-seq1510-build-record` (the SONG_T build this cutover completed) · `tourshow-fill-layer-rebuild-method` (the fill sequences 1511/1512 this cutover put under TC).



## ⭐ THE CLI LANE, PROVEN 9/9 — 2026-07-31 [0731cLD]

**Grammar:** `Assign Sequence <seq> At Timecode <tc>.1.<N>` re-points dot-track N's `Target`. Landed **9 of 9 tracks** on TC 101 for SONG_A (main + 8 aux) in one batch, every one readback-verified. **This supersedes this file's earlier desk-only framing** — cLD can drive the whole cutover over the wire; it is the standing method for the remaining setlist.

### ⛔ The dot-index EXCLUDES the Marker track

`<tc>.<group>.<N>` addresses the **Nth NON-MARKER track** — i.e. tree-child **N+1**. So `.1.1` is the **main** track and `.1.2` is the first aux, not the reverse. The first SONG_A assign was written to `.1.2` believing it was the main and re-pointed **Snare 1** instead.

**Damage profile is mild, which is exactly what makes it dangerous:** a TC track keeps all of its events when its `Target` moves — only the pointer changes — so the mistake costs one corrective assign and produces a completely clean-looking echo either way. Nothing in the command feedback distinguishes the right track from its neighbour.

### ⚠ A cached `:Children()` handle reads a STALE Target after an Assign

A track's identity (and display name) derives from its target, so the object shifts when the target does. A handle captured before the write reads the **old** target afterwards and reports a successful write as a failure. **Verify on the `ObjectList` dot-address**, never a cached tree handle:

```
ObjectList('Timecode 101.1.1')[1]:Get('Target')
```

Both traps stacked on the same write — a wrong-track assign masked by a stale readback — and only reading back off the dot-address cut through. Census the whole track group in tree order when in doubt; `#tg:Children()` includes the Marker and is the honest count.

History: none — mechanism discovered, proven, and generalized in one session, 2026-07-29. 2026-07-31 [0731cLD] — CLI Assign lane proven 9/9 on TC 101; dot-index-excludes-Marker and cached-handle-staleness traps banked.


## Track TREE order is not sequence-NUMBER order — verify every target by content, never by position — 2026-07-31 [0731-3cLD]

**TC 104 cutover prep (SONG_D, the last act before execution):** the track tree order
is **Marker, main, Snare1, Snare2, KICK2, KICK1** — so by the dot-index law above (tree
excludes Marker, `.1.1`=main), `.1.1`=main→1310, `.1.2`→1311, `.1.3`→1312,
**`.1.4`=Kick2→1314**, **`.1.5`=Kick1→1313**.

**THE KICK PAIR IS REVERSED vs. sequence numbering:** the track tree lists Kick2 BEFORE
Kick1, but the correct targets are Kick2→1314 and Kick1→1313 — the opposite of what walking
the tree in order and assigning sequence numbers sequentially would produce. **Target by
track content, never by assumption** — the same dot-index-position trap this concept's
"EXCLUDES the Marker track" section already warns about, now with a second, independent
failure mode (content order vs. number order diverging) stacked on top of it.

**Live-executed and proven correct:** Dave ran the TC 104 cutover himself at the desk —
Target flips including the reversed kick pair, all correct — tested under timecode + audio,
called SEND IT. Export-back TC 104 census: 5/5 tracks target cLD sequences BY NAME, 393
events intact (17 Go+ / 46+46 / 12+12 / 8+8 / 122+122 Temp pairs), Marker untouched.
