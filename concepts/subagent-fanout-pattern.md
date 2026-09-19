---
id: subagent-fanout-pattern
title: "Subagent fan-out for bulk processing keeps main context lean — cheap models process, Fable thinks"
role: operational-meta
tags: [process]
when_to_load: "When facing a bulk/parallelizable processing task (visual analysis, description writing, measurement) that would otherwise bloat the main session's context"
status: active
source: "MEMORY §{TOUR} — direction-package intake + Law 0 — Paid-for lessons (0702-3), 2026-07-02 third session; refined by findings/INBOX.md librarian-bootstrap-run entry, 2026-07-04"
verified: grandMA3 onPC 2.4.2.2 (Mac)
supersedes: []
superseded_by: null
---

**Dave-endorsed pattern:** fan out bulk visual/description work to parallel Sonnet subagents (e.g. hex color measurement via PIL) rather than doing it inline in the main session. This keeps main context lean.

General framing: **cheap models for processing, Fable (the thinking model) for thinking** — this generalizes the same split the Librarian protocol itself uses (see `LIBRARIAN.md`'s capture/curate split: cheap model restructures, thinking model designs/verifies).

This is an **evergreen process pattern**, not tourshow-specific, even though it was first articulated during {TOUR} work — tagged accordingly (no era tag).

**Measured, not just asserted (2026-07-04):** the librarian bootstrap run gave this pattern its first hard numbers. A Sonnet subagent digested all of MEMORY.md (494 lines) into 60 atomic concept files + `concepts/INDEX.md` in ~11 min / ~145k tokens / 85 tool calls — the "cheap model processes" half held up at full scale. But the "Fable thinks" half turned out to be doing real work, not ceremony: Fable's verification pass caught 4 filing issues the subagent's own self-check missed (misfiled evergreen concepts filed under a historical/era section, duplicate index cross-refs, an empty placeholder section, and a v0.1/v0.2 supersede call the subagent hadn't resolved). **Corollary: the thinking-model verify step is load-bearing, not ceremony** — don't skip it to save time on fan-out runs, even when the cheap-model output looks clean.

History: none — recorded 2026-07-02 (third session); refined 2026-07-04 with bootstrap-run metrics and the verify-checklist corollary.
