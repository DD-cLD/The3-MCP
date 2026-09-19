---
id: loadshow-cli-when-menu-dead
title: "LoadShow \"name\" /nc is the CLI load lane when the Backup/menu UI won't open — quotes for names with spaces, no .show extension, SelectDrive first for USB, and it DISCARDS unsaved work"
role: programmer
tags: [ma3, cli, v2.4, loadshow, recovery, tourshow]
when_to_load: "When the console's Backup menu won't open and a show has to be loaded, or before typing any LoadShow — the quoting/extension/drive rules are unforgiving and the command silently discards unsaved changes"
status: active
verified: grandMA3 onPC 2.4.2.2 (Mac), EU tour leg 2026-08
source: "findings/INBOX.md [0822-3cLD] 2026-08-22 ({FESTIVAL} show day — console Backup/menu UI would not open); form cross-checked against the manual (LoadShow \"MyShow\")"
supersedes: []
superseded_by: null
---

**The situation this exists for:** show day, the console's Backup/menu UI refuses to open, and the file has to be loaded anyway. The CLI path works when the menu does not.

## The form

```
LoadShow "Show Name" /nc
```

- **Quote the name** whenever it contains spaces (tour filenames always do).
- **No `.show` extension** — the name only.
- **`/nc`** kills the dialog dependence, exactly as in the SaveShow forensics (`saveshow-enumerate-headless-cancel-class`) — without it the load is at the mercy of a dialog that may be unanswerable.
- **`SelectDrive` first** if the show lives on USB rather than the internal drive.
- **`SaveShow` (bare) first if there is anything unsaved** — LoadShow discards the running show without further ceremony.

**MCP note:** `LoadShow` is **denied** in the MCP classifier and stays denied (`saveshow-discipline-and-mcp-tier`). This is a **desk-typed** lane — Dave's hands on the console command line, not a bridge call.

**Relation:** `saveshow-enumerate-headless-cancel-class` (the `/nc` reasoning) · `save-disk-verify-mtime-delta` (verify before you discard) · `saveshow-discipline-and-mcp-tier` (why this never rides the bridge).

History: none — delivered live on a show day when the UI failed, 2026-08-22, manual-cross-checked at the time.
