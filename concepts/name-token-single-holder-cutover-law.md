---
id: name-token-single-holder-cutover-law
title: "Name-resolution cutover law: rename the OLD holder AWAY FIRST so a token never has two holders — then converge every addressing lane (name resolution, TC index targets, executor seats) onto the same object per song"
role: programmer
tags: [ma3, doctrine, naming, timecode, cutover, v2.4, tourshow]
when_to_load: "Before swapping which object a by-name lane resolves to — a rebuild taking over an original's token, a sequence replacing another under timecode; the ordering rule is what prevents an ambiguous window"
status: active
verified: grandMA3 onPC 2.4.2.2 (Mac), EU tour leg 2026-08
source: "findings/INBOX.md [0812-1cLD] 2026-08-12 — 14 flips + 3 case-normalisations + a uniform graveyard rename, censused 18/18 single-holder"
supersedes: []
superseded_by: null
---

## The law

**Per token: rename the OLD holder away FIRST, then rename the new one in.** At no point may two objects carry the same token — a by-name resolver has no defined behaviour in that window, and the failure is silent.

Attested execution: **14 song flips**, done old-away-first per song, plus **3 case-normalisations** of names an earlier session had set in a different case, plus the old objects given a **uniform graveyard prefix** (`OLD <token>` ×17) so the retired set is legible at a glance. Census after: **18/18 tokens single-holder.**

## Exact spelling, no case bets

The fire path resolves by **exact token**. A hand-added cue read `In _N_OUT` firing `Go+ Macro "SONG_S"` — both wrong, both fixed to the exact token, both verified by readback (`object-name-assignment-asymmetry-cues-vs-others` for the cue-rename mechanics). **Never bet on case-insensitivity anywhere in a name-resolved chain.** The image pool needed the same treatment for its own match law — one card renamed so the token match ran 18/18 exact.

## Converge every lane, or the cutover isn't done

A song is addressed by **three independent lanes**, and they can disagree silently:

1. **Name resolution** — the plugin chain resolving the token to a sequence;
2. **Timecode index targets** — TC tracks pointing at a sequence by index;
3. **Executor seats** — the per-song page's main executor assignment.

The cutover is structurally complete only when **all three land on the same object per song**. That convergence was done deliberately and censused: name tokens 18/18, executor seats read back per page, TC targets confirmed by name.

**Ordering consequence for build work:** while renames are in flight, **do not write new CMDs into the objects being renamed** — orphan risk. Park that pass until the names settle, then it is five minutes. (This is exactly why the video clip-go was routed through the single shared macro touchpoint instead of eighteen mark cues — see `automator-tc-architecture`.)

**Relation:** `speedmaster-name-token-exact-match-gotcha` · `object-name-assignment-asymmetry-cues-vs-others` · `automator-tc-architecture` · `tc-track-target-cutover` · `tc-cutover-last-and-delete-eats-events-doctrine` · `pool-naming-song-prefix-collision-rule`.

History: none — executed and censused 2026-08-12.
