---
id: edit-session-mechanics-and-contamination-risk
title: "`Edit Preset x` pulls the preset INTO the programmer; exiting edit mode (Escape/Quickey) does NOT clear it — ClearAll is the flush, careless Store after exit bakes/contaminates"
role: programmer
tags: [ma3, recipes, presets, v2.4, danger]
when_to_load: "Before or immediately after using `Edit Preset x` (or the Recipe Editor's equivalent Edit function) to open an existing preset/recipe — read this before your next Store to avoid baking stale edit-session content into it"
status: active
source: "findings/INBOX.md, 2026-07-16 (two convergent mentions, same mechanic)"
verified: grandMA3 onPC 2.4.2.2 (Mac)
supersedes: []
superseded_by: null
---

`Edit Preset x` pulls the target preset **INTO THE PROGRAMMER** — that's the mechanism that lets the editor show and manipulate its values.

Exiting the edit session — via Escape or via `Quickey 20` (see `quickey-20-popup-abort-lane`, since synthetic Escape doesn't reach the console) — closes the edit **MODE**, but the content does **NOT** leave the programmer. The pulled-in values REMAIN there as live programmer values; that's why the editor still shows them after exit. `ClearAll` is the actual flush.

**Danger:** a careless `Store` after exiting an edit session — before running `ClearAll` — bakes/contaminates whatever gets Stored with the leftover edit-session values still sitting in the programmer.

**Distinct from `edit-command-escape-pending-line-trap`:** that concept is about a staged-but-uncommitted CLI **text line** surviving an Escape on the Edit Command popup and later firing with appended junk. This concept is about a committed preset-edit's **programmer values** surviving in the programmer after the edit session's mode is closed. Different objects (a pending keystroke line vs. loaded programmer values), same family of "Escape doesn't mean gone" console danger.

History: none — first captured live 2026-07-16, during the phaser/recipe session (recipe-preset editing via the Recipe Editor's Edit function).
