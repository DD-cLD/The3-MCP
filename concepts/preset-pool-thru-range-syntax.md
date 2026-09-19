---
id: preset-pool-thru-range-syntax
title: "Preset-pool Thru ranges: `Delete Preset 4.101 Thru 105` = OK; `Delete Preset 4.101 Thru 4.105` (fully-qualified both ends) = Illegal object"
role: programmer
tags: [cli-syntax, presets]
when_to_load: "Before writing a Delete/Copy/Move/Export-style command over a range of preset-pool slots"
status: active
source: "findings/INBOX.md 2026-07-23 [0723cLD] (POOL-RANGE THRU GRAMMAR, live 2.4.2.2); extended findings/INBOX.md [0803-3cLD] 2026-08-04 (weighted notation: Export Preset Thru confirmed Illegal object on a dotted range too)"
verified: grandMA3 onPC 2.4.2.2 (Mac)
supersedes: []
superseded_by: null
---

**POOL-RANGE THRU GRAMMAR (live-verified 2.4.2.2):** `Delete Preset 4.101 Thru 4.105` → **Illegal object**. `Delete Preset 4.101 Thru 105` → **OK**. The right side of a `Thru` must NOT be fully qualified to the same depth as the left side — it continues at the deepest addressed level of the left side (here, the pool-slot number only, not the repeated `4.` pool prefix).

**Generalizes** the existing fully-qualified-both-ends-is-Illegal rule from subfixture addressing (`subfixture-thru-range-syntax`) to PRESET-POOL ranges — this is the same grammar rule, confirmed to apply one level up the addressing hierarchy.

## Export confirmed as a second verb, 2026-08-04 [0803-3cLD]

**PREFERENCE (G=0.3).** `Export Preset <a> Thru <b>` on a fully-qualified-both-ends dotted
range also returns `Illegal object` — the same grammar this concept already documents for
Delete now confirmed on Export too. **Workaround: export per slot** rather than reaching for a
Thru range on Export.

History: none — captured 2026-07-23 [0723cLD] digest run.
