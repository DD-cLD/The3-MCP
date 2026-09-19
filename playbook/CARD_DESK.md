---
card: DESK
version: "0.1"
created_at: 2026-07-24
scope: "Live console contact — bring-up, firing, import, save, census, patch, verification"
not_scope: "Off-console authoring (CARD_AUTHORING) · timecode (CARD_TIMECODE)"
---

# CARD — DESK

**What this is:** the ways the console lies to you while you are touching it. It says
OK. It echoes clean. It returns success. None of that is evidence.

---

> Portability update: generic `send_lua` is now always Tier 3. Historical notes
> below about ungated Lua describe the earlier server. Current execution requires
> supervised mode, a fresh operator interlock, and exact single-use approval.
> See [the current guide](../docs/AGENT_QUICKSTART.md).

## ⛔ ABSOLUTE

1. **Never call `GetPresetDataFast()`.** Segfaults onPC 2.4.2.2 on a freshly built preset/phaser — a C-side crash `pcall` cannot catch. Banned from all generated Lua. `gpdf-console-killer`
2. **No `Go+`, no write-chain, without an explicit "desk clear?" callout and Dave's clear-to-fire.** The console is ONE shared command surface — MCP writes land in whatever context the desk is in. With Patch open, `Store Group` made default-named groups and preset chains silently no-oped. `desk-clear-callout-before-console-write-rule`
3. **`SaveShow` before any big move and before every hand-written-XML Import.** Always `/NoConfirmation`. `LoadShow` stays denied. `saveshow-discipline-and-mcp-tier`

## BRING-UP — before anything else

- `get_console_info` first. **`udp_sent` / `out_ok` prove nothing** — `out_ok` is a send-succeeded flag, verified true with onPC fully closed and nothing bound on UDP 8000. `out-ok-is-send-not-reachability`
- **OSC carries no traffic at all without an active Session.** The tell: `ManetSend : Sending multicast (Admin) data without address. Reports skipped: N`. `osc-session-required-for-traffic`
- **A console segfault reaches the MCP as a TIMEOUT, not an error.** A changed onPC PID means crash + relaunch. `segfault-manifests-as-mcp-timeout`
- A stale MCP process needs a **full quit (Cmd+Q) and relaunch** — a new Cowork session/chat/window does not restart it. `stale-mcp-process-after-repo-change`

## SAVING — the false OK

- **An unquoted dotted show name truncates at the dot and returns a FALSE "OK".** `Cmd('SaveShow cLD_SANDBOX_v0.21 /NoConfirmation')` saved junk `cLD_SANDBOX_v.show`. `saveshow-discipline-and-mcp-tier`
- The transport-safe form — `send_lua` forbids a raw `"` — is single quotes inside a Lua long bracket: **`Cmd([[SaveShow 'cLD_SANDBOX_v0.21' /NoConfirmation]])`**. `saveshow-discipline-and-mcp-tier`
- **Never trust the OK echo — verify the `.show` on disk.** `GetShowFileName()` does not exist (nil global) and `Root().ShowData.Name` returns the literal string `"ShowData"`. Shows dir is Filesystem-MCP-reachable, not `device_bash`-reachable. `saveshow-discipline-and-mcp-tier`

## IMPORT & READBACK — what actually catches what

- **Import echoes OK regardless of content damage.** Only a **line-readback diff** (console Command strings vs the authored file) catches quote truncation. Screen echo will not. `macro-xml-schema-cracked`
- Macro execution logs **every** line to Command Line History as `(Macro N 'name')OK:cmd` or `Illegal object:…` — read the history tail after every builder `Go+`, alongside the object census. `console-cli-feedback-channels`
- **A structure census is not a content census.** Right count and right names survive a shredded import intact. `macro-xml-schema-cracked`
- `Set` with an unknown/wrong property name **fails silently** — no error, no effect, clean prompt. `set-command-unknown-property-fails-silently`
- **Sequence `SpeedMaster` value must be the master's exact object NAME, no space** — `'Speed1'` works, `'Speed 1'` (with a space) is a **silent no-op with a clean OK echo**. Readback caught it twice. `speedmaster-name-token-exact-match-gotcha`

## PROGRAMMER CONTAMINATION

- **Exiting `Edit Preset x` via Escape or `Quickey 20` does NOT clear the programmer.** Only `ClearAll` flushes it. A careless `Store` afterwards contaminates. `edit-session-mechanics-and-contamination-risk`
- **Escape on the Edit Command popup does NOT discard the line** — it stays pending and can fire later. `edit-command-escape-pending-line-trap`
- A blocking dialog **suspends** the remainder of a `;`-batched CLI line and **resumes it on resolution — even on Cancel**. `dialog-suspend-resume-batched-lines`
- **Importing an MVR in PSR / Show Creator CLEARS THE PROGRAMMER**, no warning. `patch-mvr-export-import-lane-and-schema`
- A PSR over a phaser recipe **breaks its shape links**. `v24-phaser-model`

## PATCH WRITES

- **ONE property per `Set`** — chaining silently drops everything after the first pair. `patch-set-one-prop-quoted-values`
- **QUOTE every value.** A bare negative has its minus sign eaten: `-0.5` applies as `+0.5`. `patch-set-one-prop-quoted-values`
- A CLI spread `-5.5 Thru 5.5` drops the negative and flattens to `5.5 Thru 5.5` for every fixture — **quoting does not fix this one**. `patch-set-one-prop-quoted-values`
- The Patch Export dialog **silently resets to the MVR tab on every open** — an unwatched export lands as `.mvr`, not grandMA3 XML. `patch-xml-export-lane-and-schema`

## THIS CONSOLE, THIS RIG

- **Executors 1–15 are NOT instantiated on this Mac onPC.** `Assign Sequence 15 At Executor 15` fails silently; `Executor 15` and `Page 1.15` both resolve nil. Use the 101+ bank; Assign instantiates on first use. `executor-1-15-not-instantiated-mac-onpc`
- **`GS` writes the sub-layout into the fixture TYPE**, not the selected instances — every instance inherits it, and the bake does **not** survive a repatch. Multi-fixture recall is nondeterministic. `gridstore-keyword-and-fixture-type-write` · `gs-multifixture-recall-unreliable`
- `Assign Layout` Merge onto an existing layout **silently dropped the range-head FID** (47 of 48 landed, no warning). `assign-layout-merge-dialog-behavior`
- The Layout editor's **"Layout Element Defaults" tab edits USER-PROFILE-WIDE defaults**, not the current layout. `layout-element-defaults-tab-is-user-profile-wide`
- **JDC1 Layout/Stage intensity is structurally untrustworthy** — its GDTF declares no relation for plate/beam master gating. Output gates as fixture master × plate master (`401.1`) × cell (`401.1.1..12`); any one at zero is dark. `jdc1-gdtf-no-gating-relations-root-cause` · `jdc1-output-gated-chain`
- **Whole-fixture MAtricks block size is per-fixture-MODEL, not universal, and is TOUR-VARIABLE:** {LD}'s Strike M = blocks of 14 · our JDC1 = blocks of 12 · our QX80/QX40 line = blocks of 5. Fixed at the pool level (144/145/146) so binds inherit it — expect a retune every time the house rig's fixture types change. `tourshow-whole-fixture-block-law`
- **Lua `:Get()` on a NEGATIVE MAtricks value returns the uint32 wraparound** (`YShift -1` reads as `4294967295`) — the value is stored correctly, only the live read lies. Verify signed values via export readback, not `:Get()`. `matricks-negative-value-lua-uint32-wraparound-gotcha`

## TIMECODE CUTOVER

- **The TC-track dot-index EXCLUDES the Marker track** — `<tc>.1.N` addresses the Nth NON-Marker track (tree-child N+1), so `.1.1` is the main and `.1.2` is the first aux. Assigning to the wrong one silently re-points the neighbour and echoes clean. `tc-track-target-cutover`
- **A cached `:Children()` handle reads a STALE `Target` after an Assign** — the track's identity shifts with its target, so the old handle reports a good write as a failure. Verify on the `ObjectList` dot-address. `tc-track-target-cutover`
- `Assign Sequence <s> At Timecode <tc>.1.<N>` is the proven CLI cutover lane (9/9 live); rollback = point the Target back. `tc-track-target-cutover`

## TOOLING AROUND THE DESK

- **Glob/list false-negatives on Drive-synced dirs** — `wraps/*.md` reported "No files found" against 14 real files. Cross-check with `ls`. `glob-false-negative-on-drive-synced-dirs`
- **`device_stage_files` can serve a STALE container copy** — one re-stage read 836 bytes in-container against 2473 reported by the stage call. Compare `ls -la` bytes against the stage result's own bytes field. `glob-false-negative-on-drive-synced-dirs`
- `manual_lookup` runs on a **hand-curated** keyword index, not full text — 0 hits does not mean the fact is absent. `manual-index-vocabulary-is-curated`
- `⚠VERIFY` `Cmd('Delete Preset …')` via `send_lua` classifies **Tier 1 (ungated)**, unlike `SaveShow`-inside-`Cmd` which is caught as Tier 2. Treat Delete as unguarded. `delete-command-classifier-tier-gap`
