---
id: macro-scratch-slot-idiom-generalizes-to-any-pool
title: "MA's shipped RemOff / World Is Selection macros both use the same delete→store→use→delete scratch-slot idiom — generalizes to any pool type"
role: programmer
tags: [ma3, macro, v2.4]
when_to_load: "Before writing a macro that needs a disposable temp object (a scratch Group, World, or similar) — MA's own factory macros establish the idiom"
status: active
source: "findings/INBOX.md, 2026-07-17"
verified: grandMA3 onPC 2.4.2.2 (Mac)
supersedes: []
superseded_by: null
---

MA's own shipped **"RemOff"** and **"World Is Selection"** example macros both implement the same scratch-slot idiom, applied to two different pool types:

`delete temp object /NoConfirmation` → `store` → `use` → `delete again`

RemOff applies this to a **Group**; World Is Selection applies it to a **World**. Since the idiom is identical across two different pool types, it generalizes: any pool type can use a disposable numbered slot the same way — delete first (clean slate, no confirmation prompt), store into it, use it, then delete it again to leave no trace.

(Distinct from `preset-copy-label-mcp-and-century-scratch-slots`, which is about cLD's own century-numbered scratch-slot ALLOCATION for presets — this concept is about the delete/store/use/delete IDIOM itself, as demonstrated in MA's shipped macros.)

**Confirmed 2026-07-19 on a third pool type:** the factory `circular copy x plus.xml` macro uses `Selection 1`/`Selection 2` pool objects as scratch slots inside its self-referential Go-loop (see `macro-control-structure-workaround-idioms`) — Group and World were the first two pool types observed using this idiom; Selection is the third, exactly as this concept predicted.

History: none — first captured 2026-07-17, macro deep-dive session. Extended 2026-07-19: third pool type (Selection) confirmed via the factory circular-copy Go-loop macro.
