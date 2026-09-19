---
id: split-and-guard-per-sequence-walk-law
title: "⛔ SPLIT-AND-GUARD is the scan law: one concern per pass, pcall per sequence, capped output — and on a file whose sequence pool reports Count()=9999 a full-pool nested walk DIES outright while a single-sequence walk runs in ~70ms"
role: programmer
tags: [ma3, lua, mcp, census, scan, v2.4, tourshow]
when_to_load: "Before writing ANY show-wide Lua scan or audit, and immediately when a scan times out or silently kills the round-trip — the payload's SHAPE (one big nested walk vs per-sequence guarded calls) is the first suspect, not the wire"
status: active
verified: grandMA3 onPC 2.4.2.2 (Mac), EU tour leg 2026-08
source: "findings/INBOX.md [0822-2cLD] 2026-08-22 (full-show recipe destination audit — first attempt killed the round-trip) and [0826-5cLD] 2026-08-26 ({FESTIVAL} file: sequence pool Count()=9999)"
supersedes: []
superseded_by: null
---

## The law

A show-wide scan is **not** one big nested walk. It is:

1. **One concern per pass.** Values in one pass, selections in another. The audit that combined values + selections + a per-song rollup in a single payload **silently killed the round-trip** — the wire itself was fine.
2. **`pcall` per sequence.** Each sequence's walk is its own protected call, so one bad object cannot take the pass with it.
3. **Capped output.** Lists are truncated at the source; counts come back, not bodies. (Compare `tourshow-context-health-never-read-bulk-xml-rule`.)

**Rebuilt that way, the same audit completed clean:** **6201 value refs, 0 errors, 0 dead** (Dimmer 2910 · Color 1027 · Phaser 895 · Beam 703 · Position 455 · Focus 203 · pool 22 ×8) and **6075 group refs, 0 errors, 0 dead** — the pre-flight that made walking onto a festival stage with no rig time safe.

## The attested kill, and the working budget

On the **{FESTIVAL}** file the sequence pool reports **`Count() = 9999`**. Against that number:

- a **full-pool nested walk DIES** — repeat timeouts, every attempt;
- a **single-sequence walk runs in ~70 ms**.

**⇒ Portability warning:** the all-sequences sweep that worked on the base file is **not portable**. On any file with an inflated pool count, the only lanes are **per-sequence calls** or **export + Mac-side python** (`export-plus-python-bulk-lane`). The rule of thumb the leg settled on: **bulk questions go export+python, targeted writes go per-sequence calls.**

**Relation:** `lua-pool-walk-allocation-law` (the sibling truth about `#pool` reporting allocation, not occupancy — the two together explain why pool-count-driven loops are hazardous) · `export-plus-python-bulk-lane` · `wire-timeout-vs-console-busy` (the other reason a scan times out) · `send-lua-expression-payload-rule` · `saveshow-discipline-and-mcp-tier` (the 1800-char transport cap that forces chunking).

History: born as the scan law after the 2026-08-22 full-show audit crashed the round-trip; extended 2026-08-26 with the Count()=9999 attested kill and the ~70ms single-sequence budget.
