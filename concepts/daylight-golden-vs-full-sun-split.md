---
id: daylight-golden-vs-full-sun-split
title: "\"Daylight\" splits into two build targets: GOLDEN hour (warm boards get free amplification) vs FULL SUN (only whites+key+geometry+movement read) — build delta layers against FULL SUN, relax at golden"
role: design
tags: [tourshow]
when_to_load: "Before building a daylight delta layer for a specific EU festival show — check which of the two daylight sub-conditions (golden vs full sun) that show actually falls into"
status: active
source: "findings/INBOX.md, 2026-07-10 (ARTIST_TOURSHOW_DAYLIGHT_AUDIT_v0.1.md)"
verified: grandMA3 onPC 2.4.2.2 (Mac)
supersedes: []
superseded_by: null
---

**The daylight audit splits "daylight" into two distinct build targets**, since they demand different treatment:

- **GOLDEN** (CPH/Oslo/{FESTIVAL}) — warm boards get **free amplification** from golden-hour light; existing warm-palette treatments mostly just work.
- **FULL SUN** (three full-sun {FESTIVAL} dates) — only **whites + key + geometry + movement** actually read against full sun; saturated color and subtlety are wasted.

**Build rule:** build delta layers **against FULL SUN** (the harder, more restrictive condition) and **relax at golden** — i.e. design for the worst case, let the easier case inherit.

**EP ({FESTIVAL}) self-solves:** the saturate gate opens **exactly as the invariant closer block arrives (~20:15)** — meaning EP's own schedule naturally transitions into saturated-color-safe conditions right when the closer block (which wants saturated color) needs it, without requiring a bespoke delta layer for that show.

Cross-reference: `tourshow-eu-sun-and-venue-ledger` (the per-show sun ledger this split is built from), `tourshow-daylight-design-vocabulary` (the operative vocabulary, of which "saturate fields = dusk-and-after" is the rule this split refines), `daylight-audit-board-findings` (which boards need FULL SUN-targeted delta layers first).

History: none — split proposed and recorded same session, 2026-07-10.
