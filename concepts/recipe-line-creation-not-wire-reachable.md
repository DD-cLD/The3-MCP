---
id: recipe-line-creation-not-wire-reachable
title: "⛔ Recipe LINES are born at the desk: part:Append/Acquire/Create all silent-no-op and Insert dialog-cancels headless — but EXISTING lines' Selection/Values/Preset/MAtricks all reassign cleanly by Lua"
role: programmer
tags: [ma3, recipes, lua, mcp, v2.4, gotcha, tourshow]
when_to_load: "Before planning any batch that needs NEW recipe lines — creation is a desk/macro job, not a bridge job; reassignment of existing lines is fully automatable"
status: active
verified: grandMA3 onPC 2.4.2.2 (Mac), EU tour leg 2026-08
source: "findings/INBOX.md [0826-3cLD] 2026-08-26 (four creation lanes tried, all dead) and Dave's Assign-lane note [0826-4cLD] 2026-08-27"
supersedes: []
superseded_by: null
---

## The hard boundary

**Creation is not reachable over the wire.** On a cue part, all of these failed:

- `part:Append(...)` — silent no-op
- `part:Acquire(...)` — silent no-op
- `part:Create(...)` — silent no-op
- `Insert` — opens a dialog, cancels headless (`"User Canceled Command"` family)

**⇒ A new recipe line is born at the desk** — Recipe editor, new line — or through Dave's **Assign lane**: recipe fields *are* assignable by macro line, so a macro artifact can carry the work even where raw Lua cannot (`many-lines-ride-macros-not-lua`).

## What IS fully automatable

**Every field on an EXISTING line reassigns cleanly by Lua**, readback-exact:

- `rl.Selection = <group handle>`
- `rl.Values = <preset handle>` and `rl.Preset = <preset handle>`
- `rl.MAtricks = <matricks handle>`

Handle assignment — not pool numbers, not name strings — is the proven form (`assign-cli-recipe-line-grammar`). This is what carried **407 colour repoints**, **65 master-migration repoints**, **39 pan-shell repoints** and every venue MX repoint of the leg.

## The planning consequence

Design surgeries around **repointing what exists**, never around **conjuring what doesn't**. Where new lines are genuinely required — the mark-cue MM shell rows are the standing example — the work is **handed to Dave's fingers with an exact per-part recipe** rather than attempted from the bridge (`mm-shell-empty-preset-armor`).

**Relation:** `assign-cli-recipe-line-grammar` · `many-lines-ride-macros-not-lua` · `mm-shell-empty-preset-armor` · `recipe-line-cli-addressing-and-list-readback` · `recipe-step-level-cli-write-path`.

History: none — four creation lanes attested dead 2026-08-26; Dave's Assign-lane note added 2026-08-27.
