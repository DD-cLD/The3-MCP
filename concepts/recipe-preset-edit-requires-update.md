---
id: recipe-preset-edit-requires-update
title: "⚠ Editing values inside an existing recipe preset does not persist without Update — reverts silently on clear"
role: programmer
tags: [ma3, recipes, v2.4, gotcha]
when_to_load: "Before editing a value (e.g. Speed) inside an already-stored recipe preset (such as a preset copied Strobe→Strobe 2) — the edit will not survive a selection clear unless committed via Update"
status: active
source: "findings/INBOX.md, 2026-07-16, Dave, console live 2.4.2.2, paid-for as a repeat build cycle"
verified: grandMA3 onPC 2.4.2.2 (Mac)
supersedes: []
superseded_by: null
---

**⚠ Paid-for lesson (cost a repeat build cycle).** Editing a value — speed or any other property — inside an **existing** recipe preset (e.g. a preset copied `Strobe` → `Strobe 2`) does **NOT** take effect by editing alone. The change **reverts on selection clear** unless committed through the **Update** function.

This is a **silent-revert class** issue: the encoders show the changed value while you're editing, so the edit visually looks stored — but it isn't, until Update is explicitly invoked.

Related pattern: compare to `set-command-unknown-property-fails-silently` (a different silent-failure surface — wrong property name, vs. this concept's uncommitted edit) — both share the "clean-looking prompt/display, no actual effect" shape and the same defense: verify by readback / re-open, never trust the encoder display alone.

History: created 2026-07-16 from a live paid-for lesson during the second recipe build session.
