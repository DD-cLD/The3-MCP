---
id: saveshow-enumerate-versioning
title: "Versioned saves: SaveShow /Enumerate is live-verified (increments a trailing version number, e.g. v0.1→v0.2) — but that differs from the manual's documented 3-digit-count behavior; description-triggers-numbering remains unverified"
role: programmer
tags: [mcp, ma3, verify]
when_to_load: "When you want commit-style versioned checkpoint saves from the CLI/MCP, or before relying on Dave's description-as-commit workflow, or before assuming /Enumerate always appends a 3-digit counter"
status: verify
source: "help.malighting.com/grandMA3/2.4 keyword_saveshow + ok_enumerate (fetched 2026-07-04); Dave's description=commit observation, MEMORY §Console-crash paid-for lessons, 2026-07-04; live verification findings/INBOX.md 2026-07-14"
verified: grandMA3 onPC 2.4.2.2 (Mac)
supersedes: []
superseded_by: null
---

**Documented (2.4 manual, not yet run live):**
- `SaveShow "Show_Name" /Enumerate` (or bare `SaveShow /Enumerate`) appends a **three-digit count** to the show file name — the CLI versioning mechanism. Shortcut: `/En`.
- **⚠️ 31-character limit gotcha:** if name + enumeration exceeds 31 characters, the excess characters of the NAME are cut and replaced by the number. Keep checkpoint-show names short (`cLD_SANDBOX` = 11 chars, safe).
- There is **NO description/note option keyword on SaveShow** in 2.4 — only `/Enumerate` and `/Path`. A save "description" exists in the save-dialog UI, not the CLI.

**Live-verified 2026-07-14 (attended CLI, 2.4.2.2):** `SaveShow "cLD_SANDBOX_v0.1" /Enumerate` → saved as **`cLD_SANDBOX_v0.2`**. **No confirm dialog appeared.** This confirms `/Enumerate` works live over the wire — but the *observed* behavior is **not** the manual's documented "appends a three-digit count": here, `/Enumerate` **incremented an existing trailing version number already in the name** (`v0.1` → `v0.2`) rather than appending a separate `_001`-style counter. Both behaviors may be real, gated by whether the name already ends in a recognizable version-like suffix — this trigger condition is itself unconfirmed; treat the manual's 3-digit-count description as applying only to names *without* a trailing version pattern until tested.

**Further reproduced, same day, evening session (2026-07-14):** the trailing-version increment kept firing consistently across an entire session's checkpoint chain — `v0.3→v0.4→v0.5→v0.6`, logged in-session as "increment behavior now 4-for-4", continuing on to `v0.7` and `v0.8` per that session's wrap. This still only demonstrates the increment behavior on an already-version-suffixed name — the bare-name / 3-digit-count question below remains untested.

**Further reproduced, 2026-07-17:** increment behavior logged as **"now 6-for-6"**, `v0.15→v0.16`. Still only the version-suffixed-name case; the bare-name / 3-digit-count question and the description-as-commit premise remain untested.

**Unverified (what keeps this at `verify`):**
- **Which trigger governs which behavior:** does a version-suffixed name (`..._v0.1`) always get incremented while a bare name (`cLD_SANDBOX`, no suffix) gets a 3-digit count appended instead? Not yet tested against a bare name on 2.4.2.2.
- Dave's observed behavior: MA3 auto-numerates the show file **when the save description changes** (description = commit message). Presumably the UI dialog's description field interacts with the same enumeration mechanism — unconfirmed, and not touched by the 2026-07-14 test (which used the CLI form, not the save-dialog description field).

**Clears with:** run `SaveShow /Enumerate /NoConfirmation` on a **bare, non-version-suffixed** name (e.g. `cLD_SANDBOX` with no `_vX.Y`) and observe whether it gets a 3-digit count instead of an increment; separately, change the description in the save dialog and observe whether the number bumps without `/Enumerate`.

**Further reproduced, 2026-07-17 session:** checkpoint chain continued `v0.16 → v0.17` (first Tier-2 MCP write landed) `→ v0.18` (checkpoint taken under the new pre-XML-import standing rule, see `saveshow-discipline-and-mcp-tier`) — increment behavior now **8-for-8** across the full run of checkpoints logged so far. Still only exercises version-suffixed names; the bare-name / 3-digit-count question remains untested.

History: split from `saveshow-discipline-and-mcp-tier` 2026-07-04 (atomicity: the proven save-discipline rule was being held at `verify` by this one open question). Updated 2026-07-14: `/Enumerate` confirmed live-working (no confirm dialog), but revealed a version-suffix-increment behavior not described by the manual's 3-digit-count language — kept at `status: verify` since the exact trigger rule and the description-as-commit premise both remain open. Updated again 2026-07-14 (evening session): the increment behavior reproduced across a full v0.3→v0.8 checkpoint chain in a single session, consistent with the earlier v0.1→v0.2 finding; the two open questions above are untouched by this and status stays `verify`. Updated 2026-07-17: further corroborated, v0.15→v0.16, logged "6-for-6" — same open questions remain, status stays `verify`. Updated 2026-07-17: chain continued v0.16→v0.18 (6-for-6 → 8-for-8), still only on version-suffixed names; status unchanged.


## ⛔ SCOPE COLLAPSE, 2026-08-19 (EU tour leg) — /Enumerate DOES NOT SURVIVE THE HEADLESS CHANNEL

Everything above describes **attended CLI** behaviour and stands as such. On the tour file, run **unattended** — from a macro, from generated Lua, over the bridge — **`SaveShow /Enumerate` is a SILENT NO-OP**: it opens a dialog nothing answers, resolves as `"User Canceled Command"`, and reports success upstream. A full day of checkpoints was phantom; the newest `.show` on disk was nine hours old.

**⇒ Do not use `/Enumerate` for unattended checkpointing.** The working headless lanes are **bare `SaveShow`** (in-place) and **`SaveShow "name" /nc`** (save-as), both disk-verified. Full account and receipts: **`saveshow-enumerate-headless-cancel-class`**; the ritual it forced: **`save-disk-verify-mtime-delta`**.

The open questions above (bare-name vs version-suffixed trigger, description-as-commit) are unaffected and still open — they are attended-lane questions. Status stays `verify` for that reason.

History: extended 2026-08-19 — the headless scope collapse found on tour; see `saveshow-enumerate-headless-cancel-class`.
