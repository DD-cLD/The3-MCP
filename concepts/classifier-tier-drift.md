---
id: classifier-tier-drift
title: "⛔ The MCP tier classifier is a WORD-LIST, and concatenation hides keywords: Cmd('Delete Preset '..slot..' /nc') and Cmd('Go Macro N') both ride Tier 1 — a 43-slot mass delete slid through the read channel. Gate flagged ops properly, never dodge, and ANNOUNCE LOUDLY regardless of tier."
role: operational-live
tags: [mcp, safety, classifier, tourshow]
when_to_load: "Before trusting the tier gate to catch a write, and whenever a command is assembled by string concatenation or dispatched through a toolbox function — the gate cannot see keywords it never receives as literals"
status: active
verified: EU tour leg 2026-08
source: "findings/INBOX.md [0808-4cLD], [0808-9cLD], [0812-3cLD], [0819-2cLD] 2026-08-08→19 — four independent instances across the leg"
supersedes: []
superseded_by: null
---

## The gap, stated once

**The classifier matches literal keywords in the command string it is handed.** Anything that keeps the keyword out of that string at inspection time evades it. Three evasion patterns are now attested:

1. **Concatenation.** `Cmd('Delete Preset 4.'..slot..' /nc')` classified **Tier 1** — the gate literally refused approval as unneeded — and **a 43-slot mass delete ran on the read channel.** The worst instance of the leg.
2. **Whole-command literals that happen to lack a listed word.** `Cmd('Go Macro N')` classified **Tier 1**; firing a macro is a write-effect op riding the read channel.
3. **Toolbox indirection.** A call to a plugin function (`Toolbox.DoThing('token')`) carries **no keywords at all** in the calling line, yet performs whatever the function performs. **The toolbox pattern is itself a classifier gap.**

**And it false-positives in the other direction:** a read whose payload merely *contained* the word `Plugin` tripped Tier 2. That is fine — gated, single-shot, clean.

## The standing rules

- **Gate flagged ops properly; NEVER dodge a gate.** A false positive costs one approval; a dodge costs the habit.
- **ANNOUNCE-ALWAYS.** Tier is not the safety mechanism — the announcement is. Every write-effect op is announced before it fires whatever tier says, and every batch is censused after.
- **Grants are single-shot and expire on their TTL.** A long pause mid-batch (a model switch, an operator stepping away) silently ages out every pending grant. **Re-granting is cheap; assuming a grant is still live is not.**
- **Tier is not stable across time.** The same class of operation classified Tier 1 in one era and Tier 2 in another as the server changed, and `Go+` sits at Tier 3. **Never reason from a remembered tier.**

## For server hardening (the bank)

The word list cannot see through concatenation or indirection. The candidates named across the leg: **Delete-in-`Cmd`**, **`Go Macro`-in-`Cmd`**, **`Update`-in-`Cmd`**, and **toolbox function calls generally**. A structural fix (classify the assembled string at send time, or classify by effect rather than by literal) would close all four at once.

**Relation:** `delete-command-classifier-tier-gap` (the same gap, first sighting) · `classifier-tier-gap-edit-and-bare-layer-keywords` (the settled ruling on which ops stay Tier 1) · `classifier-plugin-token-false-positive-block` · `desk-clear-callout-before-console-write-rule` · `saveshow-discipline-and-mcp-tier`.

History: none — assembled from four independent instances across 2026-08-08 → 2026-08-19.
