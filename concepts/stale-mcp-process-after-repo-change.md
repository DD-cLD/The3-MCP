---
id: stale-mcp-process-after-repo-change
title: "Running grandma3 MCP process is stale code — restart after any safety-layer/server change before trusting its behavior"
role: operational-live
tags: [mcp, process, safety]
when_to_load: "After editing gma3-mcp-server-py (classifier, deny-list, tool code) and before trusting the wire's behavior; when a deny/allow decision contradicts what the repo's current tests say"
status: active
source: "findings/INBOX.md, 2026-07-05, caught live"
verified: grandMA3 onPC 2.4.2.2 (Mac)
supersedes: []
superseded_by: null
---

The **running** grandma3 MCP instance is the code that was loaded at **Claude Desktop launch** — editing the server repo does not hot-reload the live process.

**Caught live (2026-07-05):** a "PresetMode" read was substring-denied on the word 'Reset' **hours after** the word-boundary fix for that exact bug had already landed in the repo (see `saveshow-discipline-and-mcp-tier`'s word-boundary note). The fix was correct and present on disk; the running process just hadn't picked it up.

**Rule:** after any safety-layer or server code change (classifier rules, deny-list, tool definitions), **restart Claude Desktop** (or relaunch the MCP server process) before trusting the wire's behavior.

**Diagnostic signature:** a stale-filter symptom looks like a deny reason that the repo's current tests/code say can't happen — e.g., a denial citing a substring-match bug that was already fixed. If live behavior contradicts what you just read in the source, suspect a stale process before suspecting the fix.

**Refinement (2026-07-05, same day, re-caught): a NEW Cowork session/chat does NOT restart MCP server processes.** Re-verified live a second time — grandma3 still ran pre-fix code (Reset substring denial + a `/` path bug) a full day after both fixes had landed in the repo, despite multiple fresh Cowork sessions/chats having started in between. **"Restart Claude Desktop" means a FULL QUIT (Cmd+Q) + relaunch — a new session/chat/window is not a restart.** The venv is an editable install, so quit+relaunch alone is sufficient to load new code; no reinstall step needed.

**Mitigation shipped (2026-07-05, restart-gate-021): version bump as an instant freshness signal.** `get_console_info().server_version` now disambiguates stale-vs-fresh in one call — bump the server's version string on every repo-affecting release (0.2.0 → 0.2.1 this run) and compare it live against the version you expect from the latest ship. No more inferring staleness indirectly from a deny-reason that contradicts the repo; just read the version. Confirmed working live: the restart-gate smoke this session used exactly this check (0.2.0 seen live before the Cmd+Q relaunch Dave performed on waking, 0.2.1 confirmed after) to prove the gate had cleared.

History: first-observed 2026-07-05 (PresetMode/Reset substring denial); refined same day after a second live reproduction (Reset substring denial + `/` path bug, both already fixed on disk) showed a fresh Cowork session alone does not clear the staleness — only full quit+relaunch does. Same day, third update: `server_version` version-bump check shipped and used live as the cheap freshness signal, closing the loop this concept opened.
