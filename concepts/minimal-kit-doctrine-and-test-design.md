---
id: minimal-kit-doctrine-and-test-design
title: "Minimal-kit doctrine — find the LEAST information functionally needed to program; knowledge lives in two homes (minimum rides at authoring time, full library stands behind the certification gate)"
role: operational-meta
tags: [context, method, authoring, bakeoff]
when_to_load: "Before deciding what to load into an authoring context or a dispatch packet; when arguing about how much process a build actually needs"
status: verify
source: "findings/INBOX.md 2026-07-23 [0723-2cLD] (MINIMAL-KIT DOCTRINE TEST, Dave ruling — 'a new truth in AI')"
verified: grandMA3 onPC 2.4.2.2 (Mac)
supersedes: []
superseded_by: null
---

**DAVE'S RULING (called "a new truth in AI"):** find the **LEAST** information functionally needed to program — MCP use, MA3 dialects, process steps — and reduce the process to its smallest possible shape. Feed the creative document and let model intelligence work. **Excess process noise at authoring time may do more harm than good.** And critically: **RUN THE TEST, don't assume.**

**ARCHITECTURAL PRINCIPLE NAMED:** knowledge lives in **two homes** — the **MINIMUM rides at authoring time**; the **FULL library stands behind the certification gate**. Deliverable-at-the-boundary is what makes this safe: even a badly-armed authoring pass cannot reach the console without passing a verify dispatch that *does* carry the full library.

**THE FLOOR IS NON-ZERO BUT CARD-SIZED.** ⛔ console-killers and silent-failure dialect rules are **empirical, not derivable** — no amount of model capability reconstructs the fact that `Thru 4.105` is Illegal while `Thru 105` is OK, or that a raw quote silently truncates a macro import. So the minimum is not zero. The hypothesis is that it is **card-sized rather than manifest-sized** — and that is a hypothesis to test, not to assume.

**TEST DESIGN (cLD, per the bakeoff pattern).** One bounded ground-truth task — candidate: the SONG_E floor-cell life phaser. Three clean-room arms, same model class, same output contract:

- **Arm A** — creative doc + one-page dialect CARD + one golden exemplar
- **Arm B** — creative doc + the current full smith manifest
- **Arm C** — bare: creative doc + golden only

**ALL arms certified by the same verify-smith before any desk contact.** Judged blind on: certification blocker count · import-worthiness · phase-math correctness · token cost · creative-translation quality.

**IF CARDS WIN:** cards become the default dispatch payload, briefs slim to v0.2, and concept bodies retreat to a verify/rescue layer.

**POSITION PRINCIPLE, regardless of arm outcome:** the creative document stays **freshest in the authoring context**; the kit stays **small and upfront**.

**SEQUENCING:** partition run first (the spine must separate before it can be compressed), card distillation rides that pass, bake-off before the next real authoring dispatch.

**⚠ TENSION TO HOLD (2026-07-24):** the minimal-kit hypothesis and the load-the-whole-spine ruling pull in opposite directions and both are live. They are reconcilable because they answer different questions — the spine is about what a session **has access to** (cheap inside a 1M window), the card is about what is **in the foreground of attention** (where less is genuinely more). Corpus = reference; card = foreground. The counter-evidence that keeps this honest is the SONG_G recipe miss, where doctrine was **LOADED and still did not apply** — proving that access alone is insufficient and foreground matters independently.

History: ruled 2026-07-23 [0723-2cLD]; reconciled against the spine ruling 2026-07-24 [0724cLD]. Status stays `verify` until the three-arm test actually runs.
