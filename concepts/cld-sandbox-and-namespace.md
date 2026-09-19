---
id: cld-sandbox-and-namespace
title: "CLAUDE_SETUP_V0.1.show sandbox and the cLD console namespace reservations (objects 101+, Views 24-26)"
role: programmer
tags: [ma3, coachella]
when_to_load: "Before creating any cLD-authored console object — check the namespace reservation to avoid colliding with production pools"
status: active
source: "MEMORY §v2.4 console-UI first contact — Sandbox + namespace reservations, 2026-07-04, onPC 2.4.2.2 Mac"
verified: grandMA3 onPC 2.4.2.2 (Mac)
supersedes: []
superseded_by: null
---

- **`CLAUDE_SETUP_V0.1.show`** = the cLD sandbox showfile: 10 generic fixtures, FID 1–10, one 1×10 line. Full-spread phase for N=10 = **324°** (see `phase-math-formulas`).
- **cLD console namespace: objects 101+, labeled `cLD *`.** Example allocations: Groups 101–103 = All/Odd/Even; MAtricks 101–104 = Full/Half/2-Wing/Quarter.
- **Views 24–26 reserved** for cLD Program/Phaser/Verify — not yet built as of this entry.
- **View buttons:** `ViewButton 1.1–1.6` = Fixture / Preset / SeqSheet / Phaser / 3D / DMX.
- `Store View 23 "CLAUDE 1"` exists (already created).

**⭐ EXTENDED TO PRESET NAMES, 2026-07-28 (Dave ruling) — `cLD ` PREFIX ON EVERY cLD-AUTHORED PRESET.**
The namespace rule above governs object NUMBERS; this extends it to NAMES, which is where the
{FESTIVAL} transplant actually needs it — our phasers (`21.<century>20`), colours and positions
all live in pools {LD} already occupies. **Standing form: `cLD <name>`.**

**The console fact that forced it (live-verified 2.4.2.2):** MA3 enforces unique preset names
within a pool and **silently auto-suffixes an exact duplicate with `#2`** — labelling Preset
2.69-75 with names already held at 2.2-2.8 produced `Lowest#2`, `Low#2`, `Down#2`… The command
returned `ok` with **no error and no warning that a rename had occurred**; only a name readback
caught it (same silent-success family as `set-command-unknown-property-fails-silently`).
Re-labelling with the `cLD ` prefix landed clean, confirming the suffix fires **only on an exact
collision** and a prefix avoids it entirely.

**Three reasons this is the right rule, not just a workaround:** it dodges the silent
auto-suffix; it makes **provenance readable at a glance** in a file whose names have already
proved false twice (groups, then position presets — see
`inherited-file-membership-is-ground-truth`); and it is one decision instead of a per-batch one.

**Possible continuity note (unconfirmed, flagged 2026-07-14):** a similarly-named show, `cLD_SANDBOX_v0.1`→`v0.2`, is in active use as of 2026-07-10/2026-07-14 as the festival-template-rig testbed (FID 101–164, MAC Encore Performance CLD spots — see `tourshow-template-rig-patch-and-layout-state`). Whether this is the **same** showfile as `CLAUDE_SETUP_V0.1.show` (renamed/evolved over time) or a **separate** sandbox is **not confirmed** by the corpus — don't assume continuity. Notably, the new patch's fixtures do land inside the **objects 101+ namespace reservation** documented above, which is consistent with either reading (a genuinely separate sandbox would still be expected to respect the same reservation). Confirm file identity (show-file metadata, or ask Dave) before assuming either sandbox's contents describe the other.

## ⛔ COPY CARRIES THE SOURCE NAME AND FIRES THE SILENT `#2` TOO — live 2026-08-05 [0805cLD]

**`Copy Preset 21.73 At 21.2220` echoed `OK` and landed as `cLD PAN SINE#2`**, because the copy
inherits the source object's name and MA3 auto-suffixes an exact in-pool duplicate with **no
error and no warning**. **Confirms the `#2` rule above now applies to the COPY verb
specifically, not just Store/Label.** Same behaviour confirmed on MAtricks copies.

**Standing move: `Copy` then `Label` immediately, then name-census the readback** — the
readback is the only tell, exactly as with the original Store/Label discovery above.

History: none — established 2026-07-04 as the first namespace convention for cLD-authored objects. Flagged 2026-07-14: a same-family-named later sandbox exists; identity/continuity with this one is unconfirmed, noted above rather than assumed.

History: extended 2026-07-28 [0727-2cLD] — Dave ruled the `cLD ` name prefix standing for all cLD-authored presets, after MA3's silent `#2` duplicate-suffix behaviour was discovered live on the first console write of the session.
