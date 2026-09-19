---
id: macro-phaser-at-layer-edit-grammar-reference
title: "At-layer phaser edit grammar has factory file-side ground truth (flyout phaser.xml): Step n / Attribute \"X\" At Transition/Phase/Width as macro lines"
role: programmer
tags: [ma3, macro, phaser, v2.4]
when_to_load: "Before writing or verifying macro-line syntax that edits a phaser's layer attributes (Transition/Phase/Width/Speed/NShot) — factory content proves the At-layer grammar works as macro lines, a known-good reference before spending console time"
status: active
source: "findings/INBOX.md, 2026-07-19 [0718-19cLD]; MACRO_LIB_CATALOG_v0.1.md §2 (flyout phaser.xml)"
verified: grandMA3 onPC 2.4.2.2 (Mac)
supersedes: []
superseded_by: null
---

MA's own `flyout phaser.xml` builds an entire flyout phaser from 15 macro lines using the `At <layer>` edit-mode grammar — direct factory ground truth that this grammar works as plain macro-line `Command` text, not just as live CLI entry:

```
Step 2
Attribute "Dimmer" At Transition 15
At Phase 0 Thru 360
At Width 50
...
```

`Step n` moves to a phaser step; `Attribute "X"` selects the attribute being edited; `At <LayerName> <value>` (or `<value> Thru <value>` for a spread) sets that layer directly, chainable across successive lines without re-stating the attribute each time.

**Why this matters:** it's a known-good reference for the same `At <layer>` family used live at the CLI (`Measure` is one member of this family — see `phaser-layer-cli-grammar-measure-keyword`) — specifically for the **Transition/Phase/Width** layers here, and by extension the sibling **Speed/NShot** layers, all now provable from factory content before any console time is spent verifying them live.

History: none — captured 2026-07-19, read file-side from factory `lib_macros` content.
