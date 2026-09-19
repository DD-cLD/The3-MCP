---
id: tc-cutover-last-and-delete-eats-events-doctrine
title: "⛔ TC cutover is the LAST act of a build — deleting a TC-targeted sequence eats the track's events; park on {LD}'s, never delete a live-targeted sequence"
role: programmer
tags: [ma3, timecode, sequences, doctrine, v2.4]
when_to_load: "Before deleting, re-importing, or otherwise structurally rebuilding ANY sequence that is currently TC-targeted — and when sequencing a song's build steps, to confirm TC cutover is scheduled LAST rather than folded into the first import chain"
status: active
source: "findings/INBOX.md [0731-2cLD] 2026-07-31 (SONG_B TC 102 token-loss incident + Dave's ruling; SONG_C's same-session application); wraps/2026-07-31-song-b-heard-song-c-built.md (Rulings banked + Paid for sections)"
verified: grandMA3 onPC 2.4.2.2 (Mac)
supersedes: []
superseded_by: null
---

**The incident (SONG_B, 2026-07-31):** TC 102 was cut over onto `cLD SONG_B` during the FIRST import chain. All subsequent editing churn (a strict-mode pass, figure placements, a full v2 delete+rebuild) then happened on a sequence that was already TC-targeted — that is what armed the failure. The v2 rebuild's `Delete 1110` dangled the TC track, and the button-press/Go events bound to the now-dead object were lost. Dave re-entered events and destinations by hand at the desk.

**Mechanism — target MOVES preserve events; target DELETES do not.** `tc-track-target-cutover`'s events-survive-target-moves law covers moves only. A DELETE on the target object drops whatever the track pointed at, and the events bound to that dead object go with it. The post-swap readback that caught this checked TARGETS ONLY — the pointer read healthy while the event lane underneath was empty.

**Corollary, same session — deleting the TC OBJECT itself is safe, the inverse case:** the TC pool object's `Name` attribute (e.g. "SONG_B") rides the XML and survives Delete+Import — the song macro's name-based `Go Timecode '<song>'` call stays intact. **Events live in the TC object; a sequence Target is just a pointer into it** — deleting the pointer's destination loses events, deleting the TC object that holds the events does not.

**Standing order (Dave, ruled):**
1. **{LD}'s sequences are EXPORT-FOR-INSPECTION ONLY — never deleted, never edited.** TC resting on them during a build is a FEATURE, not neglect: they are a complete, working rollback state.
2. **TC cutover fires ONCE, at the very end** — after import + census + Dave's desk pass + any rebuild cycles are fully settled, never folded into the first import chain.
3. **Post-cutover tune-backs stay LINE-level via live `Assign`** (delete-free). "Park the track" — point TC back to {LD}'s original, do the structural work, point it back to ours — survives only as an emergency fallback for a post-cutover structural rebuild that should never happen in the first place.

**Why parking works:** pointer moves preserve events in BOTH directions, and while parked on {LD}'s, TC still drives a COMPLETE working version of the song — the show is never dark mid-surgery (Law Zero applied to the build process itself).

**Census consequence:** TC readback census must count **Target AND per-track EVENT COUNT, always** — a target-only census is not sufficient evidence the track is intact.

**Reapplied the same session (SONG_C):** TC 103 stayed parked on {LD}'s through the entire build — "TC 103 cutover NOT done — parked for Dave previz per cutover-last law." The doctrine held on the very next song.

**Runbook consequence (Dave, owed):** split the runbook's fire-chain step and the cutover step explicitly — never compress into one batch. The miss was pipeline momentum overriding gate discipline, the same circuit-breaker shape as other paid-for lessons in this corpus.

**Relation:** `tc-xml-event-surgery-lane` for the proven surgical-edit alternative when a post-cutover fix is genuinely unavoidable. `tc-track-target-cutover` (existing concept, not staged this run — cLD should fold this doctrine's move-vs-delete distinction into its body on next direct edit).
