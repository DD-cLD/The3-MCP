---
id: uservariable-cli-and-lua-surface
title: "UserVariable surface (P1, settled): CLI Set/Get/DeleteUserVariable typing trap + Lua GetVar/SetVar zero-not-nil gotcha + macro $ recall grammar"
role: programmer
tags: [lua, cli, ma3, macro]
when_to_load: "Before reading or writing a UserVariable from CLI or generated Lua, or before recalling a variable's value inline inside a macro command line — typing (INTEGER vs TEXT), missing-variable behavior, and $ vs $\"\" recall all have gotchas"
status: active
source: "findings/INBOX.md, 2026-07-05 (manual 06_Macros; live-proven onPC 2.4.2.2); $ recall grammar added 2026-07-17 (official manual, macro_variables.html)"
verified: grandMA3 onPC 2.4.2.2 (Mac)
supersedes: []
superseded_by: null
---

**CLI side:**
- `SetUserVariable` / `GetUserVariable` (supports wildcards `*`) / `DeleteUserVariable`.
- **Typing trap:** `SetUserVariable X 9` stores an **INTEGER**; `SetUserVariable X "9"` stores **TEXT** — these differ in subsequent math. (Source: manual 06_Macros.)
- **Object-property capture (added 2026-07-19, factory-verified):** `SetUserVariable "Name" At <Object> Property "PropName"` captures a console object's property value straight into a variable without touching Lua — e.g. `SetUserVariable "CurrentCueNumber" At Cue Property "No"` (factory `current cue number to user_variable.xml`). Paired lifecycle idiom (factory `off page 1 thru 10 - current page.xml`): `SetUserVariable` → use inline as `$VarName` (see the macro $ recall grammar below) → `DeleteUserVariable` cleanup, three lines total.

**Lua side:**
- `GetVar(UserVars(), 'name')` / `SetVar(UserVars(), 'name', value)`.
- **Live-proven, onPC 2.4.2.2:** a missing/unset variable returns **ZERO values, not `nil`**.
- Bare `tostring()` on that return **errors "value expected"** — wrap in parens to normalize: `tostring((GetVar(UserVars(),'name')))`.

**Macro $ recall grammar (third access surface, not in repo manual or previously pinned here):**
- `$VarName` substitutes as a raw command fragment (parsed as tokens).
- `$"VarName"` substitutes as one literal quoted string.
- Using the wrong form breaks the command. (Source: official manual, `macro_variables.html`.)

All three sides are recorded together because they always load together for UserVariable work — same underlying storage, three different access surfaces (CLI Set/Get, Lua GetVar/SetVar, macro-line $ recall).

History: none — first-observed/settled, live, 2026-07-05. Extended 2026-07-17: macro $ recall grammar added from official manual (macro deep-dive session). Extended 2026-07-19: added the `At <Object> Property` capture form and its paired set→use→delete lifecycle idiom, both from factory macro content.
