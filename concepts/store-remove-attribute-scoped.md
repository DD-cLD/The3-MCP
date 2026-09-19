---
id: store-remove-attribute-scoped
title: "Store /Remove is ATTRIBUTE-scoped: it removes exactly the SELECTED fixtures' ACTIVE attributes from the addressed cue/part — select, activate, then Store /Remove /nc"
role: programmer
tags: [ma3, cli, cues, store, v2.4, tourshow]
when_to_load: "Before using Store /Remove — its scope is the intersection of your selection and your ACTIVE attributes, not the whole cue and not the whole fixture; and it does nothing at all to recipe-cooked rows"
status: active
verified: grandMA3 onPC 2.4.2.2 (Mac), EU tour leg 2026-08
source: "findings/INBOX.md [0826-3cLD] 2026-08-26, {FESTIVAL} — scratch-proven flow before the masters surgery"
supersedes: []
superseded_by: null
---

**Scope, exactly:** `Store /Remove` removes **the selected fixtures' ACTIVE attributes** from the addressed cue/part. Three things gate it — the fixture **selection**, the **active** attribute set in the programmer, and the **addressed** cue/part. Anything outside that intersection is untouched.

**Scratch-proven flow:**

```
Select the fixtures
Activate the attributes to be removed
Store Cue <n> Part <n> /Remove /nc
```

Skipping the *activate* step is the common failure: with nothing active the command has no attribute scope and removes nothing while reporting success.

**⛔ It cannot touch recipe-cooked rows.** If the values in the cue are recipe output, this lane is a silent no-op regardless of selection and activation — see `cooked-recipe-rows-immune-to-store-remove` for the repoint lane that does work.

**Companion lane for raw rows:** `At Remove` with `/Merge` default-store also kills raw stored values (scratch-proven the same session).

**Relation:** `cooked-recipe-rows-immune-to-store-remove` · `merge-store-part-auto-routing` · `store-default-values-keyword` · `store-recall-recipe-toggle-rules`.

History: none — scratch-proven 2026-08-26.
