---
id: set-command-unknown-property-fails-silently
title: "Set with an unknown/wrong property name fails SILENTLY — no error echo, no effect, clean prompt ≠ success"
role: programmer
tags: [ma3, cli, paid-for-lesson]
when_to_load: "Before trusting that any Set <object> \"<property>\" <value> command worked — especially with a property name you haven't confirmed against the object's actual schema"
status: active
source: "findings/INBOX.md, 2026-07-14, console live 2.4.2.2 — paid-for lesson"
verified: grandMA3 onPC 2.4.2.2 (Mac)
supersedes: []
superseded_by: null
---

**`Set` with an unknown or incorrect property name fails silently** on 2.4.2.2: no error echo in the command line, no visible effect, and the prompt returns clean — indistinguishable from success at the command line.

**Paid for twice before the catch:** `Set <layout element> "Border" 1` and `Set <layout element> "Border" "Visible"` both silently no-op'd — "Border" is a sheet **column header**, not the actual property name (the real property is `VisibilityBorder`; see `layout-element-property-names-vs-sheet-headers`).

**Rule: a clean prompt is never sufficient evidence that a `Set` succeeded.** Always verify by readback via one of:
- the object's property sheet (visually confirm the value changed),
- a header/bounds readout (e.g. Layout's `Used X/Y/W/H`),
- or an XML export of the object.

This generalizes beyond Layout — treat it as a standing rule for **any** generated `Set` command against a property name that hasn't been independently confirmed.

**Related failure modes, different trigger:** on **patch fixtures** specifically, `Set` also fails/misbehaves silently in two more ways that have nothing to do with the property name being wrong — chaining multiple properties onto one `Set` silently drops all but the first pair, and unquoted negative values get their sign silently flipped. See `patch-set-one-prop-quoted-values` (⛔ hard rule) for both.

History: none — first paid for live, 2026-07-14, discovered while trying to toggle Layout element borders via CLI.
