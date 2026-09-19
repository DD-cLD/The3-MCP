---
id: layout-cli-assign-and-posxy-syntax
title: "Building a Layout entirely by CLI: Assign Layout <n> creates it from a selection; Set Layout n.e \"PosX\"/\"PosY\" places elements; the editor doesn't need to be open"
role: programmer
tags: [ma3, cli, v2.4, layout]
when_to_load: "Before building or editing a grandMA3 Layout view from the command line instead of by hand"
status: active
source: "findings/INBOX.md, 2026-07-14, console live-verified 2.4.2.2"
verified: grandMA3 onPC 2.4.2.2 (Mac)
supersedes: []
superseded_by: null
---

**All live-verified on 2.4.2.2.**

**Create a layout from a selection:**
```
Assign Layout 2
```
With fixtures selected, this creates Layout 2 and adds the selection **as elements, in selection order**, addressed `Layout 2.1` .. `Layout 2.n`.

**Place/move an element:** position properties are **`"PosX"`** / **`"PosY"`** (quoted). Chained properties in one `Set` work:
```
Set Layout 2.1 "PosX" 0 "PosY" 600
```

**Scale confirmed:** a 64-element plot was placed in **3 clipboard pastes** (batched `;` chains — see `macro-line-syntax-and-batching-rule`).

**Verifying mass sets without the canvas:** the layout header's **`Used X/Y/W/H`** fields are a **live bounding-box readout** — after a batch of `Set Layout n.e "PosX"/"PosY"` calls, check `Used` to confirm the placements landed in the expected bounding box, without needing to look at the canvas.

**The Edit Layout editor is a viewer/verifier, not a required context:** it auto-closed mid-session (2026-07-14, either from Dave's UI activity or a `SaveShow`) and `Set Layout` commands continued to work fine with the editor **closed**. Don't assume the editor needs to be open for CLI layout work.

**Related:** property names for things like borders/IDs are **not** the same as the sheet's column headers — see `layout-element-property-names-vs-sheet-headers`. `Set` with a wrong property name fails silently — see `set-command-unknown-property-fails-silently`; always confirm via `Used` bounds or an XML export, not just a clean prompt.

**If Layout `<n>` already exists, `Assign Layout <n>` behaves differently** — instead of creating cleanly, it pops an Overwrite/Merge/Remove/Cancel dialog. See `assign-layout-merge-dialog-behavior` for the dialog options, the overlap-triggers-dialog rule, and a live 47/48-merge anomaly.

History: none — first built live, 2026-07-14 (Layout 2 "SPOT PLOT").
