---
id: mx-cell-geometry-law
title: "⛔ MX cell-geometry law: Blocks and Groups encode PER-UNIT or SUB-UNIT texture and break when a venue's fixtures arrive 1-cell — strip Block/Group, KEEP wings, shuffle and phase ranges; mint flat twins and repoint SELECTION-SCOPED so other populations are untouched"
role: programmer
tags: [ma3, matricks, doctrine, festival, v2.4, tourshow]
when_to_load: "Before adapting a show to a venue whose fixtures have a different cell count than the file was built for — 1-cell strobes, 14-cell plates, 28-cell tubes; this is the doctrine and the whole venue MX kit is built on it"
status: active
verified: grandMA3 onPC 2.4.2.2 (Mac), EU tour leg 2026-08
source: "findings/INBOX.md [0826-1cLD] (12>14 delta) · [0826-2cLD] (twins minted) · [0826-5cLD] (1-cell doctrine, 18 lines) · [0828-1cLD] (19 lines, tubes live) · [0828-3cLD] (11 units, prime) 2026-08-26→28"
supersedes: []
superseded_by: null
---

## The distinction that carries everything

MAtricks properties split into two classes:

| Class | Properties | Depends on |
|---|---|---|
| **Cell geometry** | `XBlock`, `XGroup` (B12/B14/B7/B28, G7/G14/G16/G21) | the **cell count of one fixture** |
| **Population geometry** | `XWings`, shuffle, `PhaseFrom/To` ranges | **how many units** are in the selection |

**Cell geometry is what breaks when the venue's fixture is a different animal.** Population geometry is portable.

## The three venue cases

- **1-cell units** (single beam + single colour plate, or a 13-channel basic mode): the per-unit texture the blocks encoded is now **automatic**. **Strip Block and Group, keep wings + shuffle + phase ranges.** Clearing is `m.XBlock = 0` / `m.XGroup = 0`, reading back `None` (`matricks-property-clear-encoding`).
- **Different multicell count** (heritage 12 → venue 14 plates, 28 tubes): **mint block twins at the new number** — `B12 → B14`, tubes `→ B28` — and repoint. Same doctrine, different target.
- **Native multicell** matching the file's build number: the file needs **nothing**.

## Selection-scoping is not optional

The same MAtricks object is used by populations that are *not* affected — spots, the touring pixel line, QX40. Repoints are therefore **scoped to the recipe lines whose Selection is the affected family**, so the untouched populations keep the original object. This is also why the tour file stays pure: the originals are never edited, only new twins are minted beside them.

**Per-sequence reverse maps make restore exact.** Several sources collapse onto the same twin (`W2 FLAT` arrives from both `WING 2` and `G7 FLAT` on different songs), so a naive reverse is ambiguous. Record the map per sequence as you sweep.

## Receipts across four venues

| Venue class | Units (plates / tubes) | Broken lines found | Result |
|---|---|---|---|
| 14-cell plates + 28-cell tubes | 52 | 3-4 | twins `B14`/`B28` minted, repointed |
| 1-cell, tubes dormant | 18 / 0 | 18 | flat twins, still-broken = 0 |
| 1-cell, tubes LIVE | 24 / 24 | 19 (the 18 + one tubes line) | flat twins, still-broken = 0 |
| 1-cell, prime population | 11 / 11 | 19 | one macro tap, still-broken = 0 |

**Verification is always the same:** a fresh export sweep across the plate *and* tube families reporting **still-broken = 0** (`export-plus-python-bulk-lane`).

## Aesthetic notes for the operator's eye

- Stripping blocks spreads a pattern **across the whole population** instead of chunking it per unit — looks read smoother. If a look reads *too* smooth, **small Groups are the grain dial**: pick divisors of the population (G2/G3/G6/G9 at 18; G2/3/4/6/8/12 at 24).
- **Prime populations run wings uneven** — 11 units on W2 is 6+5, a mirror that is functional but slightly asymmetric. Functional call is cLD's, aesthetic call is Dave's.
- A dormant family (tubes with an empty group) makes its recipes **cook to nothing** rather than error — a silent, benign no-op that becomes live at the next venue.

**Relation:** `tourshow-whole-fixture-block-law` (where the per-family block numbers come from) · `matricks-property-clear-encoding` · `venue-adapt-macro-pattern` (the kit this doctrine became) · `selection-count-probe` (how the unit counts are established) · `phase-math-formulas`.

History: none — doctrine formed at the first 1-cell venue 2026-08-26 and re-attested at every subsequent venue through the end of the leg.
