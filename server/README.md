# gma3-mcp-server (Python)

A Model Context Protocol server that exposes bounded grandMA3 console / onPC control to AI agents.

Start with [the agent quickstart](../docs/AGENT_QUICKSTART.md) for Codex,
Claude Desktop, other local MCP clients, and corpus-only use. The original design
spec and private show scaffolds mentioned in historical notes are not shipped;
this README, the guide, code, and tests describe the public package.

## Unreleased — 0.2.2 portability and execution gates

- Local stdio works independently of the model provider; an offline MCP check
  verifies tool discovery and corpus lookup with `tools/check_mcp.py`.
- `--config` now reaches `serve`; plugin install verification uses the real
  keyword-only query interface. Optional unshipped resources default to null.
- Every caller-supplied Lua expression is Tier 3. Dry-run blocks it; supervised
  execution requires a fresh operator live-enable file and exact single-use
  `confirm_gate` approval. CLI `query` refuses arbitrary Lua instead of bypassing
  that approval path. Dedicated fixed read tools and `probe` remain available.
- Approval matching preserves whitespace inside code/quoted values. Safety mode
  spelling is validated. These controls support a trusted attended workflow;
  they are not a sandbox or independent proof of human consent.

The following version sections preserve historical receipts; current behavior
above supersedes their references to generic Lua as an ungated read channel.

## v0.2.1 (2026-07-05) — post-review polish

`concept_lookup` tool (WORKING/concepts knowledge base) · `manual_lookup` grep-fallback for curated-vocabulary misses · plugin-XML `DataVersion` threaded from config (`ma3.data_version`) instead of hardcoded · README safety section brought current. Version bump doubles as the restart-freshness check: `get_console_info().server_version == "0.2.1"` ⇔ the relaunch loaded this code.

## v0.2 (2026-07-04) — the Lua-file round-trip release

The core change: **all queries and the probe now ride the Lua-file round-trip**, because MA3 has no OSC echo of command results (that was the v0.1 design's dead assumption — see "Transport truths" below).

How a query works:

1. Python sends `Lua "<generated one-liner>"` via OSC `/cmd` (UDP :8000).
2. The generated Lua evaluates the expression under `pcall` and writes a
   sentinel file (nonce + ok + tostring(value)) into the console's
   `gma3_library` folder — tmp-write + rename, effectively atomic.
3. Python polls the file, matches the nonce, deletes it, reports value + RTT.

`lua_roundtrip_ok: true` therefore means *the console executed our code* —
the only honest liveness signal on this transport. Typical loopback RTT: ~35 ms.

**Topology constraint:** server and console must share a filesystem
(single-machine onPC dev, or a mounted console share). Two-machine rigs need
the Phase-2 push-channel plugin (spec §8).

**Generated-Lua transport rules** (MA3 CLI quoting is unforgiving): single
line, Lua single-quotes only (no `"`), no `;` (the CLI batches on it —
verified 2.4.2.2), no backslashes. `send_lua`/`query` reject violations with
a pointed error instead of corrupting the command.

## Tools

Fixed read/reversible tools:

- `get_console_info()` — config + REAL liveness probe (round-trip + console identity)
- `send_lua(code, want_result=True)` — Tier 3 arbitrary code, separately gated as described above. `want_result=False` provides only a send result, not execution proof. Direct GPDF calls remain denied; dynamic Lua is not safely analyzed by regex.
- `resolve_object_address(object_ref)` — enumerated address at runtime (they SHIFT between versions: Group 101 = `13.13...` on 2.3.2, `14.14.1.5.101` on 2.4.2 — never hardcode)
- `list_plugins()` / `manual_lookup(keyword)` / `get_manual_summary()` / `get_showfile_snapshot()`
  - `manual_lookup` falls back to a bounded live word-boundary scan of the manual files when the curated index vocabulary misses (`source: grep-fallback` on those hits — the SaveShow gap, 2026-07-05)
- `concept_lookup(keyword)` — search the WORKING/concepts knowledge base (ids, summaries, domains); exact-id or single match ships the full body (0.2.1)
- `hook_add/remove/list/tail` — talk to the `alchemease_hooks` host api via the round-trip; `'host-not-active'` = host not Toggle-activated

Tier 2 (gated: dry_run blocks absolutely; supervised needs a confirm_gate grant when the default require_confirm_for_tier2=true is retained):

- `confirm_gate(command, approve)` — time-boxed single-shot exact-match approvals (§5)
- `install_plugin(name, lua_source, ...)` — REAL since 2026-07-05 (stub retired): validate → write pair → ReloadAllPlugins → Import → optional one-shot run; gate string binds name+slot+run+content-sha over both sources; ≥5 s cooldown under a TOCTOU lock; verify reads the pool slot back (Name must match)
- `install_hook_host(slot=5)` — packaged persistent hook host (DRAFT — lifecycle console-verification pending); never auto-runs (activation = pool Toggle, attended)

Still stubbed: `fire_sequence` (Tier 3 — pending confirm_gate + live-enable interlock per §5.6)

CLI: `gma3-mcp probe` (fixed liveness code) · `gma3-mcp serve` (local stdio by default). The retained `query` command returns a migration error and sends nothing.

## Quickstart

For installation without console contact, use the commands in
[the agent quickstart](../docs/AGENT_QUICKSTART.md#local-mcp-setup).
The following bootstrap explicitly includes a console probe.


```bash
cd server                   # this directory (was WORKING/gma3-mcp-server-py in the show repo)
bash setup_and_probe.sh     # venv at ~/.venvs/gma3-mcp + install + tests + probe
```

The venv lives OUTSIDE the repo (`~/.venvs/gma3-mcp`, override `GMA3_MCP_VENV`)
— the repo's move into Google Drive killed the old in-project `.venv`
(venvs aren't relocatable), and thousands of venv files don't belong in Drive
sync anyway. Any `./.venv` you still see is a dead artifact; delete at will.

Operator-requested fixed probe:

```bash
GMA3_MCP_CONFIG="$PWD/config.yaml" ~/.venvs/gma3-mcp/bin/gma3-mcp probe
```

## Console-side requirements (all live-verified 2.4.2.2, 2026-07-04)

| Layer | Requirement |
|---|---|
| Network window | **Active session** (loopback/local session fine — without one the OSC subsystem is dormant; this is THE classic silent failure) |
| In & Out → OSC master | `Enable Input = Yes`; `Interface` = a real NIC (`lo0 (127.0.0.1)` for local), not `<None>` <!-- scrub-ok: In & Out --> |
| OSC line 1 | `Port 8000`, `Receive Yes`, `ReceiveCommand Yes` (CLI-settable: `Set OSC 1 "Receive" "Yes"` etc.) |
| Outbound | NOT required — leave `Enable Output` off for pure inbound loopback work |

A failed probe prints this checklist inline.

## Wiring into Claude Desktop

Done on Dave's Mac 2026-07-04 (backup saved next to the config):

```json
{
  "mcpServers": {
    "grandma3": {
      "command": "/Users/{USER}/.venvs/gma3-mcp/bin/gma3-mcp",
      "args": ["serve"],
      "env": {
        "GMA3_MCP_CONFIG": "<ABSOLUTE-PATH-TO>/ma3-share/server/config.yaml"
      }
    }
  }
}
```

Restart Claude Desktop to load it, then in a chat: `get_console_info` → expect
`probe.lua_roundtrip_ok: true` with onPC open + session active. For an offline
retrieval check, use `concept_lookup keyword="import-resolver-laws"`.
`manual_lookup` needs a separately supplied manual index.

## Safety posture

For raw Lua in `rehearsal` or `live`, the operator must create/refresh the file
configured by `safety.live_enable_file` within `live_enable_freshness_seconds`,
and authorize the exact command through the host before `confirm_gate` is called.
The agent must not create its own interlock or self-authorize. Missing/stale
interlocks and missing/expired/used approvals block the send. Keep one controlling
session per console and serialize console tool calls, even within that session:
the round-trip scratch filename is shared.

The fixed probe executes Lua and writes/removes a scratch file; dry-run is not
network isolation. Hooks alter the hook registry. The HTTP transport is loopback
only and has no built-in authentication; use stdio for local agents.


- Default mode `dry_run` — generic Lua and Tier 2+ installs refuse to send (verified in-process AND live: `install_plugin` dry-run returns a preview and touches nothing; approvals are never consulted).
- Deny-list (LoadShow/Delete User/Network/Reset — word-boundary since 2026-07-04, so `Preset*` never trips `Reset`) checked as literal patterns in the classifier; these checks do not sandbox executable code. SaveShow moved deny→Tier 2 on 2026-07-04 (save-before-big-moves discipline); LoadShow stays denied.
- `GetPresetDataFast` is denied at `classify()` itself (tier 99, any casing, any command string) — direct literal calls through that classifier are rejected; constructed names and arbitrary plugin code are not proven safe (concept `gpdf-console-killer`).
- **Deny-word plugin names are un-approvable BY DESIGN (fail-closed).** The gate string `InstallPlugin <name> …` passes through `classify()`, and its word-boundary deny scan catches deny words inside the name (e.g. `reset_tool`) → tier 99 → `confirm_gate` refuses ("cannot approve a denied/unknown command"). There is deliberately no operator override path — rename the plugin instead.
- Tier 3 (`fire_sequence`) remains a stub pending the live-enable interlock (spec §5.6).

## Transport truths (paid-for; don't relearn)

- `udp_sent`/old `out_ok` is a **send-succeeded flag, not liveness** — UDP is connectionless; onPC fully closed still "succeeds".
- MA3 emits **no OSC echo of command results**; `EchoInput/EchoOutput` are System Monitor diagnostics. Outbound OSC is event-driven (mapped Page/Fader/Key) only.
- The optional `echo_listener` (config) exists for two-machine event-stream diagnostics; useless on loopback (MA3 binds every OSC line's port once a session is active).

## Install troubleshooting

**`pip install -e .` fails with a metadata-generation error.** This project
requires **Python >= 3.12** and builds with **hatchling**. A virtualenv created
by Apple's system `python3` (3.9.x) ships **pip 21.2.4**, which predates PEP 660
and cannot do an editable install with a non-setuptools backend. The tell is the
pip version, not the error text.

```bash
python3 --version            # if this is 3.9.x, that is the problem
python3.13 -m venv .venv     # rebuild on 3.12+
./.venv/bin/python -m pip install --upgrade pip
./.venv/bin/pip install -e . pytest
```

**`Readme file does not exist: README.md`** — hatchling reads `readme` from
`pyproject.toml` at build time. Run the install from the `server/` directory,
with this file present.

## Tested against

- MA3 onPC **2.4.2.2** on macOS (2026-07-04): 29/29 tests, live probe 33–63 ms RTT, Lua 5.4 (core 5.4.8)
- MA3 onPC 2.3.2.0 (2026-05-27, v0.1 era)
- Python 3.13 · FastMCP 3.4.2 · python-osc 1.10.2 · pydantic 2.13.4
- Clean-room verification **2026-08-29**: Python **3.13.13**, fresh venv, editable install via hatchling — **95 passed / 4 self-declared skips**. The skips name their own reason (they want a concepts corpus and a built manual index a fresh clone does not have), so the count moves as the suite grows. Read the stamp, not the number: an earlier receipt in this repo recorded 12/12 and was true when written.
