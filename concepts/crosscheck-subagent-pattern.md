---
id: crosscheck-subagent-pattern
title: "Cross-check subagent (independent, read-only, concepts-as-ground-truth) catches what a green test suite doesn't — keep for Tier-2+ MCP work"
role: operational-live
tags: [process, mcp]
when_to_load: "Before calling Tier-2+ MCP safety/gating work done on the strength of a green test suite alone — especially install/write-path tools and classifier changes"
status: active
source: "findings/INBOX.md, 2026-07-05 + 2026-07-06; wrap 2026-07-05-install-plugin-crosscheck + wrap 2026-07-07-beatgrid04-festival-tc"
verified: grandMA3 onPC 2.4.2.2 (Mac)
supersedes: []
superseded_by: null
---

**Pattern:** at Dave's call, dispatch an independent Fable subagent — read-only, using the project's concept corpus as ground truth — to review completed Tier-2+ MCP work as a second look, separate from the implementing session and separate from unit tests.

**Measured result (2026-07-05):** reviewing `install_plugin` + hook-lifecycle work that already had a 67-green unit test suite, the cross-check subagent caught **1 blocker + 2 majors** the suite had not surfaced:
- Blocker: GPDF classified Tier 1 and would pass `send_lua` ungated even in `dry_run` (see `gpdf-console-killer`'s enforcement update).
- Major: custom XML unvalidated/unbound from the confirm_gate hash.
- Major: verify false-positive on occupied plugin-pool slots (see `plugin-import-verify-name-match`).
- (Plus 5 minors, all fixed same session.)

All 8 findings were fixed in the same session the review ran; suite grew 49 → 80 tests, still green.

**Takeaway:** a green unit-test suite proves the code does what the tests assert — it does not prove the tests asserted the right things. An independent reviewer with no stake in the implementation and no access to "it already passed" as an anchor is positioned to catch classifier-routing gaps and validation-binding gaps that the implementing session's own tests were blind to.

**Keep this pattern for Tier-2+ MCP work** — i.e., anything touching write-capable tools, the classifier, or confirm_gate. The reviewer in this run also produced an 8-item attended console-verify list as a side effect, carried forward via the session's NEXT_ACTIONS rather than filed as concepts (process/procedural, not a banked fact).

**2nd data point (2026-07-05, restart-gate-021-ship, server 0.2.1 diff):** an independent Fable reviewer on a **96-green diff** returned **0 blockers, 1 major, 6 minors**. The major: the new `manual_lookup` grep-fallback (added to close the SaveShow index-coverage gap — see `manual-index-vocabulary-is-curated`) would have served **CHANGELOG/HANDOFF meta-docs as manual hits** — an epistemic leak in the fact-verification channel (a lookup meant to answer "what does the manual say" could return project process-doc text instead, undetectable as such to a caller). The major + 4 of the 6 minors were fixed in the same block; the remaining 2 minors were documented as designed. **Still 2-for-2:** both runs of this pattern (2026-07-05 install_plugin review at 67→80 green, and this run at 96 green) found real, non-blocker issues a green suite alone did not surface — the pattern keeps paying on Tier-2-adjacent MCP work specifically, not just Tier-2 write paths.

**3rd data point (2026-07-06, beatgrid 0.4 diff — Color-Sync + Stem-Sections, 43-assertion-green headless suite):** an independent Fable reviewer returned **0 blockers / 4 majors / 9 minors**. Majors: undo-scope gaps (mutations made without `snap()`), undo-stack memory bloat (dataURLs living inside snapshots — see `beatgrid-undo-side-cache-pattern`), modal re-entrancy via global shortcuts, `esc()` coverage gaps on session-controlled strings. All majors + most minors fixed same session. **Pattern now 3-for-3** — and notably this run was not MCP-tier work at all (a single-file browser tool, beatgrid.html), so the pattern's value isn't confined to Tier-2+ MCP write-paths: a green 43-assertion headless suite had the same class of blind spots the two MCP runs had.

History: none — first exercise of this pattern with measured results, 2026-07-05. (An earlier, related data point — the librarian bootstrap run's Fable verification pass catching 4 filing issues a subagent's self-check missed, 2026-07-04 — lives in `subagent-fanout-pattern`; that concept is about the cheap-model/thinking-model split for bulk processing generally, this one is specifically about post-hoc adversarial review of Tier-2+ MCP safety work. Related, not merged — different retrieval triggers.) 2026-07-05, same day: 2nd data point recorded (96-green diff, 0 blockers/1 major/6 minors) — pattern held on a second, independent review later the same session. 2026-07-06: 3rd data point recorded (beatgrid 0.4 diff, 43-green suite, 0 blockers/4 majors/9 minors) — pattern held on non-MCP browser-tool code.
