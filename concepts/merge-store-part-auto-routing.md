---
id: merge-store-part-auto-routing
title: "A default-addressed merge routes new fixture data to the part ALREADY CARRYING that fixture's content — you do not choose the part, the fixture's existing home does"
role: programmer
tags: [ma3, cues, parts, store, v2.4, tourshow]
when_to_load: "Before merging values into a multi-part cue without naming a part — the data lands in whichever part already holds that fixture, which is usually right and occasionally surprising"
status: active
verified: grandMA3 onPC 2.4.2.2 (Mac), EU tour leg 2026-08
source: "findings/INBOX.md [0826-3cLD] 2026-08-26, {FESTIVAL} — observed on the masters-surgery write batch"
supersedes: []
superseded_by: null
---

**Behaviour:** on a **default-addressed** (no explicit part) merge-store into a multi-part cue, MA3 routes each fixture's new data **to the part that already carries that fixture's content**. The part choice is made per fixture by existing residency, not by the command.

**Why this is mostly a gift.** Given that part numbers cannot be safely inferred from part names (`part-numbers-are-not-part-labels`), a default-addressed merge is the *safe* write into a multi-part cue: it cannot create a junk part and it preserves the show's part structure.

**Why it occasionally surprises.** Rows written this way can land somewhere the author did not picture, and then survive a later removal sweep aimed at a different part. That is exactly the benign residue noted in `cooked-recipe-rows-immune-to-store-remove` — raw cell rows that landed by auto-routing and outlived the `At Remove` pass, holding the same presets the recipes now cook (duplication, not conflict).

**Working rule:** merge by default address and then **census the parts afterwards** from an export-back; do not assume the part you had in mind is the part that received the data.

**Relation:** `part-numbers-are-not-part-labels` · `store-remove-attribute-scoped` · `cooked-recipe-rows-immune-to-store-remove` · `parts-per-century-emit-pattern-and-et-gate`.

History: none — observed 2026-08-26.
