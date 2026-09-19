---
id: reference-scan-blind-spots-guid-and-baked-content
title: "⛔ A reference scan needs NAME + SLOT + GUID forms — and even a complete one is blind to BAKED CONTENT: objects that CARRY a value rather than REFER to one stay the operator's domain"
role: programmer
tags: [ma3, census, scan, presets, phasers, v2.4, tourshow]
when_to_load: "Before concluding from a scan that nothing references a pool object — check all three reference forms, then ask separately what merely CONTAINS its content, which no reference scan can see"
status: active
verified: grandMA3 onPC 2.4.2.2 (Mac), EU tour leg 2026-08
source: "findings/INBOX.md [0819-5cLD] 2026-08-19 — self-corrected mid-session after the original grep's pattern-blindness was exposed"
supersedes: []
superseded_by: null
---

## Layer one: three reference forms

A scan that matches only literal `Preset 4.x` text is **pattern-blind**. References appear as:

- **name paths** — with the pool's *live* name, which drifts (`import-resolver-laws`);
- **slot forms** — numeric, immune to renames;
- **GUID forms** — how golden exports survive stale pool names.

**A scan must cover all three** before "zero references" means anything.

**Attested:** the original colour-in-phaser grep matched only the name-path form. A GUID cross-reference was then run and returned **still zero** — the phasers genuinely never bound the colour pool by reference. The conclusion happened to survive; the method did not, and was corrected in the log the same session.

## Layer two: the blind spot no scan closes

**Objects that CARRY content rather than REFER to it are invisible to every reference scan.** Colour-phasers were the case in point: their **baked step content** owed the consolidation, and no name/slot/GUID sweep could have seen it, because there was no reference to find. The delete never broke them *mechanically* — what Dave saw was a look, not a link.

**Working heuristic:** anything **named for what it carries** (a "deep blue" phaser, a "cool white" figure) is a candidate for baked content and belongs on the operator's list, not the scanner's. Instruments confirm; eyes find (`operators-eyes-are-the-census-of-record`).

## What a complete verification looked like afterwards

Four checks, all passing: fresh pool export with **zero dead colour-name refs** · **zero valueless phasers** (empty pool hits were dividers/organisers, not damage) · a full recipe scan resolving **233 distinct phaser slots, zero dangling** · an old-vs-new diff accounting for every change as deliberate work. Plus a repeatable script left on disk (`phaser_recheck.py`: GUID cross-ref + health + diff) so the check is re-runnable rather than re-derived.

**Relation:** `operators-eyes-are-the-census-of-record` · `color-consolidation-crowning` · `import-resolver-laws` · `preset-references-are-object-bound-rename-and-move-safe` · `export-plus-python-bulk-lane` · `empty-census-deserves-selector-suspicion`.

History: none — the scan's blindness was found, admitted and closed inside one session, 2026-08-19.
