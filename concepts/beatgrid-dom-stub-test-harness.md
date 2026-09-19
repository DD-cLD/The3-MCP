---
id: beatgrid-dom-stub-test-harness
title: "DOM-stub headless harness pattern for single-file browser tools — node + Proxy element stubs run the whole script, no browser needed"
role: tools
tags: [process, beatgrid]
when_to_load: "Before writing or extending headless tests for a single-file browser tool (HTML+JS, no build step) — reuse this harness shape rather than reinventing DOM stubbing"
status: active
source: "findings/INBOX.md 2026-07-06 + wrap 2026-07-07-beatgrid04-festival-tc"
verified: grandMA3 onPC 2.4.2.2 (Mac)
supersedes: []
superseded_by: null
---

**node + Proxy element stubs** run beatgrid's **entire script headless** — 43 assertions including async paths, no real browser needed.

**Gotchas:**
- `querySelectorAll` stub must **return elements** — some call sites destructure the result, and a stub that doesn't return real elements breaks those call sites.
- **Test object refs go stale across undo** — re-find objects (e.g. `S.events`) after an undo rather than holding a reference taken before it.
- **`OfflineAudioContext` needs a pass-through stub** for the async audio-analysis paths to run at all under node.

**Status (updated 2026-07-07): PROMOTED — the `/tmp` rebuild cycle ends.** The harness now lives permanently at `beatgrid/Meta/harness/run_asserts.js`. Assertion count grew across the promotion session: **27 green at promotion** → **37 green** after the snap-checkbox focus-bug fix added guard-matrix coverage (see `beatgrid-keydown-guard-scoped-to-text-entry`) → **45 green** by session end per the session wrap, including a real-loader session round-trip. A **vm const/let scope shim trick** is documented in-file. **`autoscan_proto.py` lives alongside it** as a numpy tuning bench for the autoScan/BPM work (see `beatgrid-bpm-estimator-octave-fix`), with constants kept mirrored between the Python bench and the JS implementation.

History: none — built and used same session, 2026-07-06. 2026-07-07: promoted permanently to `beatgrid/Meta/harness/run_asserts.js` (ending the /tmp rebuild cycle); assertion count grew 27→37→45 across the session; vm const/let scope shim + autoscan_proto.py numpy-bench pairing noted.
