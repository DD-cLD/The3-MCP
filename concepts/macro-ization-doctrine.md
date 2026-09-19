---
id: macro-ization-doctrine
title: "Macro-ization doctrine: anything done more than once on console becomes a macro; repeated chat-driven entry work becomes one Lua-triggered macro call instead of re-streaming long Lua/CLI each time"
role: programmer
tags: [ma3, doctrine, macro, mcp, process]
when_to_load: "Before repeating a console entry task a second time, or when deciding whether to build a reusable macro/plugin/script instead of streaming another one-off Lua/CLI block from chat"
status: active
source: "findings/INBOX.md, 2026-07-17 [0717-2cLD] (Dave, dictated, paraphrased per house dictation rule)"
verified: grandMA3 onPC 2.4.2.2 (Mac)
supersedes: []
superseded_by: null
---

**Standing rule (Dave):** anything cLD does more than once on the console becomes a **MACRO** — built properly, with variables and conditionals, "the whole nine yards," not a quick hack.

**Why:** repeated entry work should become a macro **trigger fired from chat via one Lua call** — change the variables and run — instead of streaming a long Lua/CLI block from the chat every time the task recurs. This is a token/time economics call as much as a reliability one: one short trigger call beats re-authoring and re-sending the same long payload repeatedly.

**Same rule extends to tooling generally:** scripts and plugins should be built as reusable tooling **wherever repetition appears** along the way — don't wait for a dedicated "build a tool" moment; catch repetition as it happens and macro/script/plugin-ize it on the spot.

Cross-reference: `macro-line-syntax-and-batching-rule` for the mechanical Store/Set macro CLI syntax this doctrine builds on; `plugin-install-loop` for the install→run cycle when the reusable unit is a plugin rather than a bare macro.

History: created 2026-07-17 from Dave's dictated standing rule, paraphrased per the project's dictation-capture house style (meaning preserved, coined shorthands kept verbatim: "MACRO-IZATION," "the whole nine yards").
