---
id: mcp-layout-probe-2026-07-14
title: "Layout-by-MCP is architecturally viable (same Cmd() strings + XML-import lane); Set/Assign classify Tier 2; live probe found console-side OSC prerequisites still unmet"
role: programmer
tags: [mcp, ma3, v2.4, layout]
when_to_load: "When deciding whether to do Layout work via the MCP instead of clipboard/CLI, or when reasoning about which Tier a Layout-building command classifies as"
status: active
source: "findings/INBOX.md, 2026-07-14"
verified: grandMA3 onPC 2.4.2.2 (Mac)
supersedes: []
superseded_by: null
---

**Dave asked: is Layout work doable from the MCP?** Answer: **YES, architecturally** — the same `Cmd()` strings used for the clipboard-pasted Layout work, and the XML-import lane (`layout-xml-export-schema-and-import-lane`), are both viable MCP routes.

**Command classification:** `Set` and `Assign` (the two commands this session's Layout work depended on) **classify as Tier 2** → require `confirm_gate` per command.

**Live probe result (server 0.2.1, fresh):** `udp_sent=true`, **`lua_roundtrip_ok=FALSE`**. Console side is **dormant** — no active Session, and OSC SONG_S unconfigured — matching the server's own checklist, i.e. our `osc-inbound-config-requirements` (Network-window Session + SONG_S enable/interface layers were never set up this session).

**Also gates when live:** `dry_run`→live is a **Dave-side config** decision, separate from the OSC prerequisites above.

**This session's actual Layout work went via the clipboard lane instead** (not MCP) — **zero blockage**, since the clipboard/CLI paste loop (`computer-use-input-loop`) was already the established input method. Activating the MCP lane for Layout work is described as "a 10-minute desk task with Dave" (per the wrap), not yet done.

History: none — probe run and result recorded same session, 2026-07-14.
