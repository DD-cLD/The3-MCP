---
id: import-file-argument-must-be-quoted
title: "⛔ Import with an UNQUOTED /File filename SILENTLY NO-OPS — the CLI answers nothing and the target stays empty; build the quotes with string.char(34) inside Cmd()"
role: programmer
tags: [ma3, cli, import, v2.4, gotcha, mcp, tourshow]
when_to_load: "Before any Import … /File call from a macro, generated Lua or the MCP bridge — an unquoted filename produces no error and no import, and only a census of the target catches it"
status: active
verified: grandMA3 onPC 2.4.2.2 (Mac), EU tour leg 2026-08
source: "findings/INBOX.md [0808-9cLD] 2026-08-08 — Seq 5 'Resolume' rebuild; the empty shell was caught by census, not by the CLI"
supersedes: []
superseded_by: null
---

**Broken (silent no-op):**
```
Import Sequence 5 /File cld_resolume_seq5.xml /nc
```
The command line **answered nothing** and the sequence stayed an empty shell.

**Working — quotes built inside the Lua payload:**
```lua
local q = string.char(34)
Cmd('Import Sequence 5 /File '..q..'cld_resolume_seq5.xml'..q..' /nc')   -- → "OK"
```

`string.char(34)` is the workaround for the transport's refusal of raw `"` characters in a command string (`saveshow-discipline-and-mcp-tier`); the single-quote-inside-a-long-bracket form is the alternative where the payload allows it.

**Lane note:** the **delete-then-import** sequence is the proven take-2 pattern when re-importing over an existing object.

**⇒ Never trust the clean echo.** The tour leg produced three independent members of this family — this one, the phantom checkpoint (`saveshow-enumerate-headless-cancel-class`), and the closed-range preset export (`preset-range-export-open-ended-only`). The common defence is the same: **census the target after every write**, and treat the echo as decoration.

**Attested working imports using the quoted form:** Seq 5 Resolume (21 cues, SR=40 exact) · the TC macro pair `cld_tc_internal.xml` / `cld_tc_default.xml` · the venue kit macros `cld_mx_1cell.xml` / `cld_mx_restore.xml` at {FESTIVAL}.

**Relation:** `saveshow-discipline-and-mcp-tier` (the quoting family) · `xml-file-side-authoring-import-lane-proven` · `import-resolver-laws` (what happens *after* a file successfully imports) · `plugin-import-verify-name-match`.

History: none — caught by census on first use, 2026-08-08; the quoted form carried every import of the rest of the leg.
