---
id: export-plus-python-bulk-lane
title: "The standing heavy-audit lane: gated full export → Mac-side python matcher → COUNTS ONLY back into context — never bulk XML through the wire or the window"
role: programmer
tags: [ma3, census, method, mcp, v2.4, tourshow]
when_to_load: "Before any show-wide census, master scan, reference sweep or before/after diff — this is the lane, and it is cheaper and safer than every wire-side alternative"
status: active
verified: grandMA3 onPC 2.4.2.2 (Mac), EU tour leg 2026-08
source: "findings/INBOX.md [0826-1cLD] through [0828-3cLD] 2026-08-26→28 — the method behind every venue adaptation of the EU leg"
supersedes: []
superseded_by: null
---

**The pattern, in three moves:**

1. **Gated full export.** `Export Sequence 1 Thru "…"` (Tier-2 gated) fans the whole live pool out to disk — one file per sequence, name-derived (`export-sequence-writes-per-name-files`) — then **disk-verify the batch** by mtime delta (`save-disk-verify-mtime-delta`).
2. **Mac-side python matcher.** Parse the batch locally. This is where the real analysis happens: master-instance scans, cell-geometry offender hunts, before/after diffs, reference resolution.
3. **Counts only into context.** The matcher prints totals, per-song rollups and short offender lists. Bodies never enter the window.

**Why it wins.** It is immune to the round-trip's scale limits (`split-and-guard-per-sequence-walk-law`), immune to the 1800-char transport cap, immune to console recook storms (`wire-timeout-vs-console-busy`), and it leaves a **repeatable artifact on disk** — every venue adaptation this leg re-ran an earlier matcher rather than rebuilding one.

**Attested runs:** the 190-file {FESTIVAL} export and master scan · the QX40 master blast-radius recompile (70 rows / 20 sequences) · the post-surgery rescan (master-kind rows 294 → 240, QX40 dotless 69 → 15) · the cell-geometry offender sweeps at {FESTIVAL} (18 lines), {FESTIVAL} (19) and {FESTIVAL} · every "still-broken = 0" verification of the leg.

**Scripts banked (in their staging folders):** `schema_probe.py`, `master_scan.py`, `master_scan2.py`, `mark_cell_check.py`, `phaser_recheck.py`, `ltc_confirm.py`.

**Relation:** `split-and-guard-per-sequence-walk-law` (when the wire *can* do it) · `export-sequence-writes-per-name-files` · `tourshow-context-health-never-read-bulk-xml-rule` (why counts only) · `many-lines-ride-macros-not-lua` (the write-side counterpart).

History: none — consolidated from the practice that ran the whole EU tour leg, 2026-08-26 → 2026-08-28.
