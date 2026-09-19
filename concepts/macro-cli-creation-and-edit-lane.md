---
id: macro-cli-creation-and-edit-lane
title: "CLI macro creation/edit lane: ChangeDestination Macro → Store [N] → ChangeDestination [N] → Insert → Set [Line] Property 'Command'/'Wait'"
role: programmer
tags: [ma3, macro, cli, v2.4]
when_to_load: "Before authoring or editing a single macro live via CLI/MCP — same shape as the proven preset/sequence CLI-first authoring pattern"
status: active
source: "findings/INBOX.md, 2026-07-17 (official manual, macro_create.html)"
verified: grandMA3 onPC 2.4.2.2 (Mac)
supersedes: []
superseded_by: null
---

Live CLI lane for creating/editing a macro, one line at a time:

```
ChangeDestination Macro
Store [N]
ChangeDestination [N]
Insert
Set [Line] Property "Command" "..."
Set [Line] Property "Wait" [...]
```

Same shape as the MCP/CLI-first authoring pattern already used for presets and sequences (see `recipe-step-level-cli-write-path` for the analogous recipe-line pattern) — one property per `Set`, address the line, write the property.

History: none — first captured 2026-07-17, macro deep-dive session, official manual `macro_create.html`.


## EU tour leg truths, 2026-08-12

- **A macro OBJECT's `.Name =` assignment WORKS** by direct Lua assignment — unlike a **cue**, where it silently fails and `:Set('Name', ...)` is required (`object-name-assignment-asymmetry-cues-vs-others`).
- **A macro LINE handle's `:Delete()` SILENTLY NO-OPS.** An empty line left behind by a PSR import survived every attempt and was left for the desk — a critical macro is not the place for ambiguous CLI delete experiments.
- **`Export Macro <n> /File "<name>.xml"` writes clean XML** (431 bytes for a one-line macro), which makes a macro a portable artifact between file lineages — the basis of the venue-adaptation kit (`venue-adapt-macro-pattern`). Re-import with the filename **quoted** (`import-file-argument-must-be-quoted`).
- **A macro Lua line must not consume names minted by earlier `Cmd` lines in the same macro without a `Wait`** — `macro-lua-label-race-needs-wait`.

History: extended 2026-08-28 (librarian, tour leg).
