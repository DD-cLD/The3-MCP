---
id: design-lock-vs-build-evidence-authority-precedence
title: "When a design lock and the shipped build disagree, ask which one has more INFORMATION behind it, not which one is older — a lock is a hypothesis with a date on it, the build is evidence"
role: operational-live
tags: [process, doctrine, authority, tourshow]
when_to_load: "Before flagging a build's output as 'drift' from a written design lock/ruling — check whether the lock predates evidence the build was made with; the newer, more-informed artifact may be the one that should update the rule"
status: active
source: "BACKLOG.md 2026-08-03 [0803-1cLD]"
verified: grandMA3 onPC 2.4.2.2 (Mac)
supersedes: []
superseded_by: null
---

**Standing lesson, generalises well beyond the colour case it was paid for on:** when a design lock and the shipped output disagree, **ask which one has more INFORMATION behind it, not which one is older.**

**The paid-for instance:** a per-song colour census was flagged as "drift" from a written palette-lock rule (the rule said retune a small fixed set of global anchor presets; the build had instead grown many more per-song presets). The lock was written off an early transcription; the output was built against ten songs of real screen content. Reading "output != lock" as drift was wrong — it was **LEARNING**. See `tourshow-palette-and-groove-v2` for the concrete colour-authority ruling this produced.

**The general rule: a lock is a hypothesis with a date on it; the build is evidence.** When they disagree, the newer artifact built with more real information is the one that should usually win — the older document should be updated to match, not the other way around.

**This is the INVERSE failure to the dropped-review-sheet lesson** (`tourshow-cue-century-review-sheet-doctrine`): there, an existing PRACTICE should have held and got dropped in error. Here, an existing RULE should have moved and was instead defended as though the build were violating it. Both are failures of not re-checking a standing artifact's currency at the moment it collides with new information — one where the old thing was right and got abandoned, one where the old thing was wrong and got defended.

**Relation:** `tourshow-palette-and-groove-v2` (the concrete colour-authority ruling this lesson produced). `tourshow-cue-century-review-sheet-doctrine` (the inverse-shaped failure this lesson is explicitly paired against).
