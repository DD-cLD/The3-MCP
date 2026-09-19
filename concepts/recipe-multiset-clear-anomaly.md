---
id: recipe-multiset-clear-anomaly
title: "[VERIFY] A multi-pair Set was observed clearing several recipe properties in ONE line (Property \"Selection\" \"\" \"Values\" \"\" \"MAtricks\" \"\" \"Filter\" \"\") — collides with the patch one-prop-per-Set hard rule; per-object-class behavior unconfirmed"
role: programmer
tags: [ma3, cli, recipes, v2.4, verify]
when_to_load: "Before assuming Set chaining behavior is uniform across object classes — a recipe-line multi-pair Set was observed clearing 4 properties in one command, which contradicts the patch-fixture one-prop-per-Set hard rule; confirm which class you're targeting before relying on either behavior"
status: verify
source: "findings/INBOX.md, 2026-07-17 — HegauLigh via forum [0717-1cLD]"
verified: grandMA3 onPC 2.4.2.2 (Mac)
supersedes: []
superseded_by: null
---

**Observed form:** a single `Set` line with multiple `Property "name" value` pairs chained together — `Property "Selection" "" "Values" "" "MAtricks" "" "Filter" ""` — was reported to clear all four recipe-line bind slots (Selection, Values, MAtricks, Filter) in one command (HegauLigh, forum source).

**Collision:** this directly contradicts the hard-verified rule in `patch-set-one-prop-quoted-values` — on **patch fixtures**, chaining multiple property/value pairs onto one `Set` silently drops everything after the first pair. If the recipe-line multi-pair form above is real, `Set` chaining behavior is **not uniform across object classes**: it may work for recipe-line property clears while failing for patch-fixture writes.

**[VERIFY]** — not independently live-tested this session. Open questions:
- Does this multi-pair chaining work for **non-empty** values too, or only for clearing (empty-string) writes?
- Is the difference genuinely per-object-class (recipe line vs. patch fixture), or does it depend on something else (e.g. all-empty-value writes behaving differently from real value writes on either class)?

**Practical stance until resolved:** do not assume multi-pair `Set` chaining works on a recipe line just because this one forum report describes it — verify by readback (`recipe-line-cli-addressing-and-list-readback`'s `List` lane) after any attempt, and default to one-property-per-`Set` (the `patch-set-one-prop-quoted-values` discipline) unless this is specifically retested and confirmed live.

Clears with: a live retest on a recipe line — chain 2+ non-empty property/value pairs in one `Set`, then verify via `List` whether all pairs landed or only the first.

History: none — first captured, 2026-07-17, forum-sourced only; flagged verify immediately due to the direct collision with an existing hard-verified rule for a different object class.
