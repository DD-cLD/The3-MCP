---
id: recipe-line-set-property-syntax-and-value-casing
title: "Recipe-line property writes require the Property keyword — Set Sequence x Cue y Part 0.1 Property \"PropName\" \"Value\" — text values are case-sensitive per forum doctrine, but live-verified Enabled specifically only takes Y/N, YES/NO, or 0/1 (not mixed-case Yes/No); MCP doctrine is to emit 0/1"
role: programmer
tags: [ma3, cli, recipes, v2.4, doc-correction]
when_to_load: "Before generating any Set command that writes a property on a recipe line (cue-part address) — the Property keyword is mandatory, and text-value casing has a live-verified exception for Enabled-class props that contradicts the forum-sourced general rule"
status: active
source: "findings/INBOX.md, 2026-07-17 — forum 69919, dherderich live-confirmed June 2026, ACT KB 34108761 via forum 69919, live 2.4.2.2 doc-correction (Dave attended) [0717-1cLD]"
verified: grandMA3 onPC 2.4.2.2 (Mac)
supersedes: []
superseded_by: null
---

**The `Property` keyword is mandatory on recipe-line writes:** `Set Sequence <x> Cue <y> Part 0.1 Property "PropName" "Value"` — omitting `Property` is not just a stylistic choice, it's required syntax for this address class (forum 69919; live-confirmed by dherderich with `"Enabled" "No"`, June 2026).

**General text-value casing rule (forum doctrine, ACT KB 34108761 via forum 69919):** text property values are case-sensitive — first letter capitalized. `"Yes"` ≠ `"yes"`.

**Live-verified exception, 2.4.2.2 (doc-correction):** for the **`Enabled`** property specifically, the accepted values are **`Y`/`N`**, **`YES`/`NO`** (uppercase), or **`0`/`1`** — the forum/ACT KB's mixed-case `"Yes"`/`"No"` form **did NOT take** live. This directly contradicts the general capitalization rule above for this one property; treat the general rule as unreliable for `Enabled` until each other enable-class property is independently checked.

**MCP doctrine:** emit **`0`/`1`** for enable-class recipe-line properties — this sidesteps the casing question entirely rather than relying on a value form that's been shown to fail.

Cross-reference: `set-command-unknown-property-fails-silently` for the standing rule that a clean `Set` prompt never proves success — always verify recipe-line writes via `recipe-line-cli-addressing-and-list-readback`'s `List` lane. `recipe-line-pool-binding-via-assign` covers the sibling case (pool-object binds, which use `Assign` instead of `Set Property`).

History: none — captured in one session, 2026-07-17; the Enabled-casing exception is a live doc-correction against the forum/ACT KB general rule, not a separate concept, since both describe the same "how do I write a text/enum value on a recipe-line Set" decision.
