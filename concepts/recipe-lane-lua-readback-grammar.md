---
id: recipe-lane-lua-readback-grammar
title: "Lua readback grammar for recipe lines — ObjectList('Seq x Cue y Part z')[1]:Get('Prop'); PropertyName(i) is 0-based; wrap before tostring"
role: programmer
tags: [ma3, lua, recipes, v2.4]
when_to_load: "Before writing generated Lua that reads back recipe cue-part properties — the exact ObjectList/Get/PropertyName grammar and its gotchas"
status: active
source: "findings/INBOX.md line 40, 2026-07-17 [0717-2cLD], console live 2.4.2.2"
verified: grandMA3 onPC 2.4.2.2 (Mac)
supersedes: []
superseded_by: null
---

**Readback pattern:** `ObjectList('Seq x Cue y Part 0.1')[1]:Get('PropName')` returns live values as strings (e.g. `'false'`, `'Group 123'`, `'Preset 22.9'`).

**`PropertyName(i)` is 0-BASED** — a 1-based loop over it errors.

**Wrap in parens before `tostring`** — a zero-return index crashes a bare `tostring()` call; `tostring((...))` guards it.

**`handle.no` / `handle.name`** work correctly in an `ipairs` loop over an `ObjectList`.

**Relation:** pairs with `recipe-part-property-surface-lua-dump` (what to read) and `objectlist-thru-vs-wildcard-gotcha` (how ObjectList ranges behave) — load together when generating any recipe-lane Lua readback.

History: none — established live 2026-07-17.
