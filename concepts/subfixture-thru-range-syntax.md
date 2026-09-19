---
id: subfixture-thru-range-syntax
title: "Sub-range Thru syntax settled: continuation at the deepest addressed level; multi-fixture ranges distribute the sub-range per fixture; verified through three levels (JDC plate/tube branches)"
role: programmer
tags: [ma3, cli, subfixture, v2.4, doc-correction]
when_to_load: "Before writing any CLI Fixture selection that reaches into subfixtures via dot notation (`301.1 Thru 16` style), especially across a multi-fixture range — also check `subfixture-down-up-cli-navigation-and-grid-stacking` for how the result lands on the grid"
status: active
source: "findings/INBOX.md, 2026-07-15, console live 2.4.2.2"
verified: grandMA3 onPC 2.4.2.2 (Mac)
supersedes: []
superseded_by: null
---

**Settled rule (live 2.4.2.2):** the `Thru` operand continues at the **deepest addressed level of its left operand**.

- `Fixture 301.1 Thru 16` → subs 1–16 of fixture 301, spread on the grid, **16 Selected** ✔ (left side is sub-qualified — `.1` — so the bare `16` on the right continues at sub level).
- `Fixture 301.1 Thru 301.16` → **Illegal object** ✘ (fully-qualified fixture.sub on BOTH ends fails at sub level).
- `Fixture 301 Thru 301.16` → selects **ONLY the .16 endpoint** (left side is fixture-level/bare, so it does not extend a sub-range the way the first form does).

**Repo manual error (3rd confirmed this session):** the manual's CommandLine sample `Fixture 1.1 Thru 1.6` is **wrong** — it matches the fully-qualified-both-ends pattern above, which is Illegal live.

**Multi-fixture sub-range distribution:** `Fixture 301 Thru 312.33 Thru 48` selects subs **33–48 of EACH fixture** in the 301–312 range — the dot-qualifier applies **per-fixture across the range**, not just to the range's endpoint. Probed on 2 fixtures → exactly 32 selected (16 subs × 2 fixtures), confirming the per-fixture read. This also explains the earlier "endpoint-only" result above: `301 Thru 301.16` only has ONE fixture in its range (301 itself), so "per-fixture across the range" collapses to a single sub.

**Three-level dot addressing verified (2026-07-21, JDC1 branches):** the deepest-level-continuation rule holds at level 3. `Fixture 401 Thru 464.1.1 Thru 12` selects plate-pixel subs `.1.1`–`.1.12` of EACH JDC1 401–464 = **768** (export Size=768, items addressed `401.1.1`, IDType 0). The left operand `.1.1` sets the level, so the bare `Thru 12` continues at the **3rd** level, and the multi-fixture range distributes per fixture exactly as it does at level 2. Working forms: JDC PLATES = `401 Thru 464.1.1 Thru 12`, JDC TUBES = `401 Thru 464.2.1 Thru 12`. The corpus had only two-level (pixel-line) confirmation before this.

**Compact-pack corollary:** an explicit sub-range selection made this way, with **no** `Grid X/Y` cursor calls guiding it, **compact-packs onto one row in selection order** — it does not spread itself across a 2D shape on its own. Pairing the same dot-range selections WITH `Grid X/Y` cursor moves (see `grid-cursor-cli-recipe-for-2d-group-layouts`) lands each sub-range block at its own specified cell instead — both lanes were verified the same session. A `GS`-stored sub-grid layout (see `gridstore-keyword-and-fixture-type-write`) does **not** apply here either — the stored layout only engages on `Down`-expansion, not on explicit dot-range Thru selections.

**Dave ratified this as the primary lane (2026-07-15):** direct dot-range entry (`Fixture 301 Thru 312.33 Thru 48 ; Store Group x`) is the primary method for building section Groups on multi-instance fixtures — faster and more direct than composing every block through Grid-cursor moves. It composes cleanly with Grid-cursor placement (above) when a 2D shape beyond one packed row is wanted.

History: none — syntax settled and multi-fixture behavior probed live in one session, 2026-07-15 (an earlier same-day hypothesis that fully-qualified `Fixture 301.1 Thru 301.16` might work was tested and found Illegal, folded into the settled rule above rather than kept as a separate entry). Extended 2026-07-21: the same continuation rule verified at THREE levels on the JDC1 plate/tube branches (`401 Thru 464.1.1 Thru 12` → 768).
