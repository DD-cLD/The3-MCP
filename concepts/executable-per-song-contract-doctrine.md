---
id: executable-per-song-contract-doctrine
title: "Executable, closed per-song contract doctrine (Codex ADOPT): zero pick-at-desk; verify via a vertical-slice audition (SET + hardest cue + one gesture) before fanning out; a circuit-breaker gate re-fires the review whenever a silent failure or workaround occurs"
role: operational-live
tags: [doctrine, process, tourshow, external-review]
when_to_load: "Before treating a song's idea-file/build package as 'done' and ready for desk import — check it against the closed-contract + vertical-slice + circuit-breaker tests below first"
status: active
source: "wraps/2026-07-21-external-review-and-method-direction.md [0721-3cLD] — Codex (GPT max) review of the cld_maker_sandbox/REVIEW clean-room, Dave ADOPT decision"
verified: grandMA3 onPC 2.4.2.2 (Mac)
supersedes: []
superseded_by: null
---

**The big idea (Codex, ADOPTED by Dave):** the SONG_G first-pass miss wasn't a lack-of-knowledge problem — it was a lack of an **EXECUTABLE, CLOSED per-song contract**. A build package is not ready for desk time unless it requires **zero "pick at desk"** decisions — every WHO/WHAT/HOW/level choice is already resolved in the authored deliverable, so console time really is pure translation (see `idea-file-design-programmer-boundary-doctrine`). This diagnoses the SONG_G miss more precisely than "the doctrine wasn't loaded" — the doctrine WAS loaded (`recipe-lane-end-to-end-verified`, `v24-phaser-model`) and still didn't get applied, because nothing forced the plan to be a closed, checkable artifact before programming started.

**VERTICAL SLICE + AUDITION (Codex sharpening):** before fanning a build out to every cue, build and fire a minimal vertical slice first — **SET cue + the hardest cue + one representative gesture** — and audition it on the desk. **A clean IMPORT is not the same as programming success**; only firing and looking at the slice proves the contract actually translates to a good look. This generalizes `review-plan-gate-precedes-programming-doctrine`'s "plan for the hardest moment first" heuristic into a concrete verification step.

**AUDITION TUNE-BACK (Codex sharpening):** because the build is a clean-rebuild-onto-a-keeper (see `clean-authoring-and-persistence-doctrine`), any desk edits made during the audition must **round-trip back into the authored contract** — a look tuned live at the desk and never folded back into the source deliverable is a look that will be lost or contradicted on the next rebuild.

**CIRCUIT BREAKER (Codex sharpening — names the real SONG_G failure mode):** the gate must **RE-FIRE mid-session** after ANY silent failure or workaround — this is what actually derailed the SONG_G first pass: one hard blocker (the `ColorAdd` silent-empty-preset trap, see `baked-phaser-preset-xml-schema`) tunneled the session into "just make it import" mode, and the review→plan gate never re-triggered to pull it back out. A circuit breaker means: the moment a workaround gets improvised to get past a blocker, STOP and re-run the review/plan check before continuing, rather than letting "just make it work" become the session's new mode.

**Scope caution (Dave, same session):** take the THINKING from this review, not a 4-document hash-ceremony — keep the actual process to a 2-page plan + checklist. The point is a closed, verifiable contract, not more paperwork.

**Relation:** `review-plan-gate-precedes-programming-doctrine` — the original, narrower "load doctrine before programming" gate this review sharpens into a testable contract + circuit breaker. `idea-file-design-programmer-boundary-doctrine` — the idea-file this contract is the executable, closed version of. `external-cross-vendor-review-lane-pattern` — the review mechanism (Codex clean-room) that produced this finding.

History: none — Codex review run and ADOPT decision made in one session, 2026-07-21 [0721-3cLD]; full review at `cld_maker_sandbox/REVIEW/FINDINGS_LOCAL.md`.
