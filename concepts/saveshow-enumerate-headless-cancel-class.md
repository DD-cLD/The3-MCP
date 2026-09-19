---
id: saveshow-enumerate-headless-cancel-class
title: "⛔ SaveShow /Enumerate is a SILENT NO-OP headless — every dialog-variant save cancels unattended ('User Canceled Command'); the only working lanes are bare SaveShow and SaveShow \"name\" /nc"
role: programmer
tags: [ma3, cli, v2.4, saveshow, gotcha, mcp, tourshow]
when_to_load: "Before firing ANY checkpoint from a script/macro/MCP call, and immediately when a rollback discovers the newest .show on disk is hours old — /Enumerate and the other dialog-variant saves return OK and write nothing"
status: active
verified: grandMA3 onPC 2.4.2.2 (Mac), EU tour leg 2026-08
source: "findings/INBOX.md [0819-4cLD] 2026-08-19, live on the tour file; caught by Dave's eye ('not saved up') against 13 clean OK echoes"
supersedes: []
superseded_by: null
---

**⛔ The paid-for discovery.** On 2026-08-19 a rollback found the newest `.show` on disk was **nine hours old**. Every checkpoint fired that day — and plausibly the "clean checkpoint lane" banked back at [0806] — was **phantom**. The commands echoed OK. Nothing reached the disk.

**Cause:** `SaveShow /Enumerate` (and the save-as *dialog* variants generally) opens a confirmation/naming dialog. Run headless — from a macro, from generated Lua, over the MCP — nothing answers it, so the console resolves it as **`"User Canceled Command"`** and the save never happens. The command channel still reports success upstream.

## The two working lanes (disk-verified the same session)

| Form | Behaviour | Proof |
|---|---|---|
| `SaveShow` (bare, in-place) | ✅ writes | `v1.1` mtime **and** size moved |
| `SaveShow "name" /nc` (save-as) | ✅ writes | created `EXAMPLE_SHOW use fOR bASE v1.4.show`, 128.9 MB, newest on disk |
| `SaveShow ... /Enumerate` | ❌ silent no-op headless | nine hours of phantom checkpoints |
| save-as without `/nc` | ❌ `"User Canceled Command"` | observed directly |

**Note the collision with the older rule.** `saveshow-discipline-and-mcp-tier` warns that *bare* `SaveShow` pops a confirm dialog when run unattended — that was the 2026-07-04 observation on the sandbox. On the tour file at 2.4.2.2 the bare in-place save **worked and was disk-verified**, while `/Enumerate` was the form that died. Do not resolve this from memory: **fire the save, then verify the file on disk** (`save-disk-verify-mtime-delta`). Disk truth outranks both rules.

**Why it survived so long undetected:** the rollback that exposed it only worked because *Dave's own hand-saves* (v1.1–v1.3) existed. Nothing cLD wrote that day was on disk. Clean echoes are not evidence — `never-trust-clean-echo` in its most expensive form to date.

**Supersedes in practice:** the [0806] "clean checkpoint lane" note, and any assumption that `/Enumerate` versioning (see `saveshow-enumerate-versioning`) is available to an unattended caller. `/Enumerate`'s *attended*-CLI increment behaviour is unchallenged by this — the finding is specifically that it does not survive the headless channel.

**Relation:** `save-disk-verify-mtime-delta` (the ritual this forced) · `saveshow-discipline-and-mcp-tier` (the quoting/flag rules that still apply to the working lanes) · `saveshow-enumerate-versioning` (attended behaviour) · `operators-eyes-are-the-census-of-record` (how it was caught).

History: none — discovered, root-caused and both working lanes disk-proven in one session, 2026-08-19.
