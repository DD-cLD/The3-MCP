---
metadata_version: "1.0"
doc_id: ma3-song-build-runbook
title: "SONG BUILD RUNBOOK v0.2 — the desk session"
owner: DaveDibb
version: "v0.2.1"
status: active
created_at: 2026-08-03
supersedes: SONG_BUILD_RUNBOOK_v0.1.md
session: "[0803-2cLD]"
tags: [tier-1, ma3, runbook, tourshow, desk]
notes: |
  v0.2 folds everything the lock session bought: the figure-reuse lookup, the
  retired JDC openers, the STB (W)+(R) surface, the split fire/cutover steps,
  and the boot-profile ruling. Written to be the ONLY document a console build
  session needs open beside the per-song prework sheets.
---

# SONG BUILD RUNBOOK v0.2

**Scope:** one song, start to heard. Everything below the line is proven — this is
translation, never invention.

> **SKILLS (08-05):** the per-phase protocol ships as installable skills —
> `ma3-run-session` (boot · rhythm · exit gate), `ma3-phaser-workup` (§1's figure
> work in full depth), `ma3-desk-session` (§4–§6 live-desk law). Installed, they
> load on trigger; this runbook stays the one-page map.

## 0 — BOOT (console profile)

Boot per **`ma3-run-session`** (lean, 08-05 context-focus ruling): MEMORY core →
latest state pair → session-type card(s) (`CARD_AUTHORING` + `CARD_DESK`,
`CARD_TIMECODE` only on cutover) → this runbook. **SPINE stays OFF the boot** —
depth is pulled per phase via `concept_lookup`; the show packet rides the first
song's prework. **If a session starts as analysis and turns toward the desk,
RE-ARM before the first write.**

## 1 — PREWORK (file-side, no console)

1. Open the song's two sheets in `generated/prework_batch/`:
   **`PREWORK_<seq>_<song>.csv`** (every line: cue, {LD} group, crosswalked
   target, century part, resolved cLD ref) and **`FIGURES_<seq>_<song>.csv`**.
2. **⭐ Read the FIGURES sheet before minting anything.** Each content hash is
   marked **COPY SOURCE KNOWN — mint per-song by copying (zero decode)** or
   **NEW CONTENT — decode needed, mint per-song**. **Every song mints its OWN
   copies at `21.<century>20`; cross-song binds are outlawed**
   (`tourshow-authoring-contract-v01`, Dave 08-03). Copying the named source and
   setting the gear at the site is the default; only NEW CONTENT rows cost a decode.
3. ⚠ The figure hash is **MAIN-SEQUENCE-ONLY**. Once the song's aux export exists,
   re-run `generated/figure_hash/figure_hash2.py` before trusting the copy-source call.
4. Dry-run the submap. Any `?UNMAPPED?` or `no preset row` in the PREWORK sheet is
   a **ruling owed** — park it in the ledger, do not improvise at the desk.

## 2 — EMIT

- Parts-per-century. Part-attr order clones the desk golden **byte-for-byte**
  (`SpeedScale` between `MAgic` and `Mode`, on EVERY part incl. part 0).
- **`ET.fromstring` gate is mandatory** on every emitted file — lint does not check
  well-formedness.
- **R1 is live:** `JDC_OPENERS_RETIRED = True`. New songs emit **no** master lines.
  The reconciliation identity's `+2 JDC gate-openers` term is **+0**.
- Speed ships **UNBAKED**. Gears are Speed Scale at the desk.
- Reconciliation identity, per song, must resolve with **zero residual**:
  `{LD} lines − HELD − law-drops + QX40-STB expansion (+0 openers) = cLD lines`.

## 3 — CERTIFY

Dispatch the sequence smith. **Stage a MULTI-PART golden** —
`generated/staging_song-d_0731/cld_ns_1310_census.xml`, a TRUE raw console
export (Guid=337 · PresetData=101 · DependencyExport=100) — plus the song's
`gb_sNN00.xml`; a single-part golden cannot attest SpeedScale or SpeedMaster.
⚠ `cld_song-b_seq_v2.xml` is NOT a desk export (0 Guid / 0 PresetData) — never
golden again. ⚠ Export-backs carry **cooked PresetData**: the census file is
attribute-order/serialization authority ONLY — never re-import it. Blockers stop
the build; PASS-WITH-FLAGS is fine if every flag is a deliberate delta.

## 4 — DEPLOY + IMPORT  ⛔ console starts here

1. **"Desk clear?" callout and Dave's clear-to-fire. PER BATCH, not per session** —
   clearance expires the moment the operator re-engages. Announce
   **"starting writes" / "writes done"**.
2. sha-verify every file container → `generated/` → `gma3_library`.
3. **`SaveShow '<name>' /NoConfirmation` checkpoint BEFORE the import.** Full form,
   name and flag, single quotes inside a Lua long bracket.
4. `Import Sequence <slot> '<bare-name>' /NoConfirmation`.
5. **Export-back BINDING census** — count by NAME, never by slot; a slot-form
   counter silently reads zero. A clean import proves nothing below the structure
   layer.

## 5 — PREVIZ

Rail to the song BPM. Apply the Speed Scale gear list. Judge shape and timing —
**not JDC1 output**, whose visualization is structurally untrustworthy; the DMX
viewer or the real unit is the readback truth.

## 6 — TC CUTOVER — **LAST, on Dave's word, its own step**

⛔ **Never fold the cutover into the import chain.** Deleting a TC-targeted sequence
eats the track's events; target MOVES preserve them, deletes do not. {LD}'s
sequences are export-for-inspection-only and are the rollback state — TC resting on
them during a build is a feature.

- `Assign Sequence <seq> At Timecode <tc>.1.<N>` — the dot-index **EXCLUDES the
  Marker track**, so `.1.1` is the main.
- **Target by track CONTENT, never by assumption** — the SONG_D kick pair was
  reversed against seq numbering.
- Verify on the `ObjectList` dot-address; a cached `:Children()` handle reads stale.
- Census **Target AND per-track EVENT COUNT**. A target-only census reads healthy on
  an event-emptied track.

## 7 — HEARD, THEN WRAP

Dave confirms under timecode + audio. Capture findings to `findings/INBOX.md` as
they land. **The librarian is a session-exit GATE, not a nicety** — fire it, then
regenerate `SPINE.md` and the indexes.

---

## CARRIED INTO EVERY BUILD

- **STB:** every `JDC1 US [STB]` use needs a **(W)** white and an **(R)** release
  (R3). The expansion is **value-dependent** — content expands 1→4, `Dimmer.0` stays
  1→1. Per-site map: `generated/desk_pack/STB_CORRECTION_SHEET.csv`.
- **Pass 1 excludes Groups 51 and 60–64.** Her key and backlight are pass 2,
  "{ARTIST} time", once the background is painted.
- **Corrections are DEFERRED** to the end-of-build circle-back, logged with method.
  Nothing gets fixed mid-run.
- **No rulings in the run.** Anything wanting a decision goes to the ledger and the
  song moves on.
