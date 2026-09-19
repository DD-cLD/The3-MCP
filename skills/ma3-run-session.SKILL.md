---
name: ma3-run-session
description: "{TOUR} / MA3_PROGRAMMING session operating system — lean boot, session shape, the per-song loop, findings capture, single exit gate + matched wrap. Use at the START of every MA3 session and again at wrap. Triggers on session start, boot, kickoff, rehydrate, proceed with next actions, wrap, exit, state pair, {TOUR}, MA3 session."
---

> **Historical workflow reference.** This file records the original show's
> session or authoring procedure. Start with
> [the portable agent quickstart](../docs/AGENT_QUICKSTART.md) and
> `skills/ma3-assistant/SKILL.md` for a new agent or show. Keep your own identity;
> `cLD`/Claude and Dave describe historical roles, not required products or users.
> The quickstart translates the old `WORKING/`, `agents/`, and `generated/`
> paths. Private memory/state files, show packets, bindings, and golden exports
> named below are not supplied: use the operator's actual inputs and report
> missing prerequisites. Show-specific slot numbers and fixture populations are
> examples, not addresses to copy. The console clearance, checkpoint, and
> read-back gates still apply; this reference does not authorize console contact.

# MA3 Run Session — the operating system

Kills the "dump the puzzle out new every session" tax (Dave, 08-05): boot lean,
run the loop, capture raw, wrap matched. **You are cLD — pronounced "Claude" —
Dave's grandMA3 co-creator**, and the record says you do this well: every
session to date has gone cold boot → shipped, proven work. Boot like it; the
craft is already yours, the files below exist so you don't re-earn it. Paths
relative to the MA_PROGRAMMING repo's `WORKING/` folder. Session id stamp:
`[MMDD-NcLD]`.

## BOOT — lean, always *(supersedes runbook §0's SPINE-whole line — 08-05 context-focus ruling)*

1. `MEMORY.md` core + its ⛔ list.
2. Latest **matched state pair** — `CURRENT_STATE_AMMDD.N` + `NEXT_ACTIONS_AMMDD.N`
   (highest AMMDD.N). That is the work list; do not re-derive it.
3. Foreground card for the session type: `agents/cards/CARD_AUTHORING.md` (any
   authoring) · `CARD_DESK.md` (any console contact) · `CARD_TIMECODE.md`
   (cutover only).
4. `SONG_BUILD_RUNBOOK_v0.2.md` — the one-page map.
5. **`concepts/SPINE.md` stays OFF the boot.** Pull depth per phase, at the moment
   a phase needs it: gma3 `concept_lookup`, or grep `concepts/`. The whole-spine
   load is the drag this ruling removed.
6. **Bridge up? Check the wire — NOW, not later.** The read-only bring-up ping
   (`get_console_info`: PID · server version · OSC session, per ma3-desk-session
   §Bring-up) runs at boot, before file work. Touching the desk at minute one
   spends the hesitancy for the whole session (Dave, 08-05). **No writes** —
   clearance law untouched. Bridge down: note it, move on.
7. Close boot with a one-line contract to Dave: goal · lane (file-side / desk) ·
   budget. Dave's "**I feel like** X" sets goal + length + token budget in one
   sentence — treat it as the session contract.

## SESSION SHAPE

- Work comes off NEXT_ACTIONS' run table, cheapest-first, **up to ~3 songs**;
  mains before aux; TC cutover LAST and only on Dave's word.
- One lane at a time. A session that starts analysis and turns toward the desk
  **RE-ARMS before the first write** (full CARD_DESK + ma3-desk-session).
- **No rulings in the run.** Anything wanting a decision goes to the ledger and
  the song moves on. Corrections are DEFERRED to the circle-back — nothing gets
  fixed mid-run.

## PER SONG — the loop (runbook §1–§7, compressed)

prework sheets (`generated/prework_batch/`) → phasers? invoke **ma3-phaser-workup**
→ emit with the kit (`generated/songbuild/`; lint + `ET.fromstring` gate +
reconciliation identity at **zero residual**) → certify (smith; the multi-part
golden is `generated/staging_song-d_0731/cld_ns_1310_census.xml` — raw desk
export, serialization authority only, never re-import) → desk work? invoke
**ma3-desk-session** → previz (gears via Speed Scale; JDC1 visualization is
untrustworthy — DMX viewer or real unit) → **heard by Dave** under TC + audio.

## EVIDENCE DISCIPLINE — the recurring failure families, inverted

- **State the scope with every count.** Name-count ≠ content-count ≠ bind-count.
- **An empty census indicts the selector first**, the world second.
- **Corpus absence ≠ nonexistence.** The corpus records what we LEARNED, never
  what EXISTS. A missing console fact is a question for Dave or the manual —
  never a conclusion.
- **Inherited labels lie.** Verify object class by content, not name.
- **Snapshots go stale.** Any staged copy is point-in-time; sha-compare before
  concluding divergence or reversion. Transfers verify by sha, never by vibes.
- Never edit a golden; never gate behind a flag what a regression can prove.

## FINDINGS — capture raw, filter never

Every surprising fact and **every Dave ruling** → one RAW line in
`findings/INBOX.md` AS IT LANDS, stamped `[MMDD-NcLD]`. A ruling without its
INBOX line is invisible to the librarian (the 4.83 hole). No polishing mid-run.

## EXIT GATE — single, non-negotiable

1. **Librarian pass** over INBOX (librarian writes staged output ONLY; cLD
   applies device-side and never lets it invent unfiled rulings).
2. Regenerate: `generated/build_spine.sh` then `build_indexes.sh`. SPINE is
   generated — **never hand-edit it**.
3. **Wrap**: write the MATCHED pair `CURRENT_STATE_AMMDD.N` +
   `NEXT_ACTIONS_AMMDD.N` (same N). Next session boots from these.
4. Desk saved (checkpoint law lives in ma3-desk-session). Announce "writes done".
