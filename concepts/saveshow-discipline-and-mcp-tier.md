---
id: saveshow-discipline-and-mcp-tier
title: "SaveShow discipline: always /NoConfirmation, now Tier 2 in the MCP; LoadShow stays denied; deny-list is word-boundary; send_lua needs single-quote-in-long-bracket quoting"
role: programmer
tags: [mcp, crash]
when_to_load: "Before issuing a SaveShow command via MCP/generated Lua, or when reasoning about what the MCP's Tier 2 permission level allows"
status: active
source: "MEMORY §Console-crash paid-for lessons — Save discipline validated in the wild, 2026-07-04, onPC 2.4.2.2, MCP-driven, live; SaveShow syntax from help.malighting.com/grandMA3/2.4 keyword_saveshow; send_lua quoting + shows-dir access added findings/INBOX.md 2026-07-21 (07-21 song-g-infra), wraps/2026-07-20-days-programming-bridge.md"
verified: grandMA3 onPC 2.4.2.2 (Mac)
supersedes: []
superseded_by: null
---

**Dave's save-before-experimenting rule paid for itself twice:** `SaveShow "name" /NoConfirmation` before the crash-inducing experiments (see `gpdf-console-killer`) meant both crashes cost **zero** — clean revert to `cLD_BENCH_WORK`.

- **`SaveShow` was reclassified deny→Tier 2 in the MCP (2026-07-04)** so cLD can checkpoint autonomously. **`LoadShow` stays denied.**
- **⚠️ Bare `SaveShow` (without the flag) opens a confirm dialog** → returns **"User Canceled Command"** when run unattended. (The 2.4 manual says same-name saves overwrite; the live-observed unattended behavior is the dialog — trust the live lesson for MCP work.)
- **⚠️ Second, distinct gotcha (live-verified, attended CLI, 2.4.2.2, 2026-07-10):** `SaveShow /NoConfirmation` **with the flag present but NO show name** gets its `/NoConfirmation` parsed as the **FILENAME argument** → opens a **"Change show file name?"** dialog (the console echoed the flag back, quoted, as if it were the typed name). **The MCP path was never bitten by this because it always passed an explicit name.**
- **Always use the full form, name AND flag together: `SaveShow "name" /NoConfirmation`.** Never omit either half.
- **Documented syntax (2.4 manual):** `SaveShow ("Show_Name") (/Option)`; shortcut `Sa`; option keywords `/Enumerate` and `/Path`.
- **MCP deny-list matching was fixed to word-boundary** (it was previously substring-matching — "Reset" was incorrectly blocking every command containing "Preset").

For versioned/commit-style saves see `saveshow-enumerate-versioning`.

**Standing rule (Dave, dictated, 2026-07-17): checkpoint immediately before any XML import.** Always fire a `SaveShow .../Enumerate` checkpoint right before importing any handwritten/authored XML into the show (`Import Preset`, `Import Layout`, etc.) — cheap insurance against a malformed import corrupting the live show. This is now standard bracketing around the file-side authoring lane (see `xml-file-side-authoring-import-lane-proven`): checkpoint → import → verify, never import cold.

**Filesystem verify lane (live-confirmed 2026-07-17, [0717-2cLD], first Tier-2 write over MCP):** `SaveShow /Enumerate` on `cLD_SANDBOX` incremented v0.16→v0.17, `confirm_gate` flow worked exactly as designed. The file-side readback location is `~/MALightingTechnology/gma3_2.4.2/shared/shows/` (a **version-scoped** directory — NOT `gma3_library/shows`); the newest `.show` file's mtime is the readback signal for "did the save land."

**⚠ `send_lua` transport quoting (paid-for live, 2026-07-21, 07-21 song-g-infra):** the `send_lua` MCP transport forbids a raw `"` character in the command string, so quoting a show name the normal CLI way breaks the channel. Worse: an **UNQUOTED dotted show name silently TRUNCATES AT THE DOT** — `Cmd('SaveShow cLD_SANDBOX_v0.21 /NoConfirmation')` saved junk `cLD_SANDBOX_v.show` on disk and still returned a **FALSE "OK."** **Verified fix:** quote the show name with **single quotes inside a Lua long-bracket**: `Cmd([[SaveShow 'cLD_SANDBOX_v0.21' /NoConfirmation]])` — this landed the correct file. Gate flow: send (Tier-2 block → returns `wrapped_cmd`) → `confirm_gate(that exact string, approve=true)` → resend within TTL. **Always quote this way, and always verify the actual `.show` file on disk afterward — never trust the "OK" echo**, which lied outright in the truncation case.

**Shows-dir is reachable by MCP filesystem tools, NOT by `device_bash` (2026-07-21):** the shows directory (`~/MALightingTechnology/gma3_2.4.2/shared/shows`) is readable via `Desktop_Commander`/`Filesystem` MCP tools but is **not** a mounted project folder reachable by `device_bash` — use the MCP filesystem tools for the SaveShow verify lane (newest/named `.show` file), not a shell command. **⚑ Narrowed 2026-08-05 [0805cLD]: this does NOT hold for `Filesystem` as currently scoped** — on that session's setup, `Filesystem` was scoped to `/Users/{USER}/My Drive` and `/Users/{USER}/dev` only, and the shows dir returned "Access denied - path outside allowed directories." `Desktop_Commander` was untested that specific run (though it demonstrably reaches other MALightingTechnology paths elsewhere in the corpus, e.g. `gma3_library` — see `xml-file-side-authoring-import-lane-proven`). **Treat `Filesystem` as NOT reaching the shows dir on a `My Drive`+`dev`-scoped setup; confirm `Desktop_Commander` before relying on it for this specific verify lane.**

**Lua has no reliable programmatic filename getter:** `GetShowFileName()` does **NOT exist** in 2.4.2.2 Lua — it's a nil global, not a function that errors gracefully. `Root().ShowData.Name` returns the literal string `"ShowData"` — useless for reading the actual filename. Filesystem mtime (above) is the only confirmed readback path for SaveShow's result.

## `send_lua` rejects a semicolon even inside a string literal, 2026-08-05 [0805cLD]

**Transport gotcha, same family as the quoting/truncation issues above.** A census payload
using `table.concat(binds, ' ; ')` was blocked pre-send ("Lua expression contains forbidden
semicolon"). **The guard is a plain substring scan, not a parse**, so a `;` anywhere in the
command string — including inside a separator or any quoted text — kills the call before it
reaches the console. **Use another separator** (not `;`) when building any `send_lua` payload
that concatenates multiple values.

History: was `status: verify` carrying the unconfirmed "description = commit" CLI-syntax question; split out 2026-07-04 into `saveshow-enumerate-versioning` after the 2.4 manual showed there is NO description option on SaveShow — the documented versioning lane is `/Enumerate`. Core rules here are live-verified; flipped to `active`. Refined 2026-07-04→2026-07-10: a second attended-CLI gotcha found live (bare `/NoConfirmation` with no name gets parsed as the filename) — the rule now explicitly requires both a quoted name and the flag together, not just "append /NoConfirmation." Extended 2026-07-17: Dave's standing pre-import-checkpoint rule folded in (paraphrased per house dictation rule), proven in the same session that first exercised the XML authoring/import lane. Extended 2026-07-17 (parallel capture): added the filesystem verify lane (version-scoped shows dir, mtime readback) and the `GetShowFileName()`/`Root().ShowData.Name` dead-end, both from the first live Tier-2 MCP write. Extended 2026-07-21 (07-21 song-g-infra): added the `send_lua`-transport single-quote-in-long-bracket fix for dotted show names (unquoted dotted names silently truncate at the dot and still return a false OK) and the shows-dir MCP-vs-device_bash access distinction.

**[0805-2cLD] EXTENSION — second send_lua transport constraint:** expressions >1800 chars are refused ("transport-unsafe") — split batch loops into sub-1800-char chunks.

History: extended 2026-08-05 [0805-2cLD] — send_lua transport cap: >1800-char expressions refused; split batch loops.


## EU tour leg attestation, 2026-08 — and one conflict to resolve on disk, not from memory

- **The 1800-char cap held all leg.** Batch writes were chunked or shipped as macro artifacts (`many-lines-ride-macros-not-lua`).
- **⚠ Conflict with the bare-`SaveShow` warning above.** This file records (2026-07-04, sandbox) that *bare* `SaveShow` pops a confirm dialog unattended. On the tour file at 2.4.2.2 the **bare in-place save WORKED and was disk-verified**, while **`/Enumerate` was the form that silently died** (`saveshow-enumerate-headless-cancel-class`). Both observations are real; the deciding factor is not established. **Do not resolve this from memory — fire the save, then verify the file on disk** (`save-disk-verify-mtime-delta`). Disk truth outranks both rules.
- **`LoadShow` stays denied on the bridge** and is a desk-typed lane when the Backup UI fails — form banked at `loadshow-cli-when-menu-dead`.

History: extended 2026-08-28 (librarian, tour leg) — tour attestation of the transport cap plus the bare-vs-/Enumerate conflict flag.
