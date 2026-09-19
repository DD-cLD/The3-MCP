---
id: segfault-manifests-as-mcp-timeout
title: "A console segfault reaches the MCP as a TIMEOUT, not an error — diagnose via changed onPC PID"
role: programmer
tags: [mcp, crash, onpc]
when_to_load: "When lua_roundtrip_ok comes back false / 'no round-trip file within Ns' and onPC appears up — check for a crash+relaunch before assuming a transport bug"
status: active
source: "MEMORY §Console-crash paid-for lessons — A segfault reaches the MCP as a TIMEOUT, not an error, 2026-07-04, onPC 2.4.2.2, MCP-driven, live"
verified: grandMA3 onPC 2.4.2.2 (Mac)
supersedes: []
superseded_by: null
---

`lua_roundtrip_ok:false` + `no round-trip file within Ns` (with onPC seemingly up) = the console likely died mid-command.

**Confirm with `get_console_info` after a few seconds** — a **changed onPC PID** means crash+relaunch happened.

**Recovery on 2.4.2.2 Mac is automatic:** new process spawns, MA-Net session + OSC line are restored, and the show reverts to the **last SaveShow**. (Both observed crashes that day logged `Show file Name: cLD_BENCH_WORK` — the pre-work save, confirming the revert-to-last-save behavior.)

This diagnostic pattern is the practical symptom of the crash described in `gpdf-console-killer`, but applies generally to any command that kills the console mid-execution, not just `GetPresetDataFast()`.

**Diagnostic gap found (2026-07-05, restart-gate smoke):** `get_console_info` on server **v0.2.0** has **NO PID field in its output** — so "confirm with `get_console_info` after a few seconds" above has **no data source to check against**. The diagnostic as written cannot currently be executed; either `get_console_info`'s probe needs a `pid` field added, or this concept needs a different confirmation method until that ships. Treat the "changed onPC PID" check as **aspirational/blocked** until verified live against a server version that exposes PID.

History: none — first-observed, live, 2026-07-04. 2026-07-05: PID-field gap in `get_console_info` (server 0.2.0) found during restart-gate smoke — the confirmation step this concept prescribes has no data to read; flagged for a tool fix or concept amend, not yet resolved either way.
