---
id: patch-cli-set-command-gotchas
title: "⛔ Set on patch fixtures: one property per command, quote every numeric value — chains and bare negatives fail silently"
role: programmer
tags: [ma3, v2.4, cli, patch, danger]
when_to_load: "Before writing or editing any patch-fixture property (positions especially) via CLI Set — read this before batching a paste"
status: superseded
source: "findings/INBOX.md, 2026-07-14, console live-verified 2.4.2.2"
verified: grandMA3 onPC 2.4.2.2 (Mac)
supersedes: []
superseded_by: patch-set-one-prop-quoted-values
---

Three live-verified gotchas, all specific to `Set` on **patch** fixtures (not the same object type as `Set Layout`, which behaves differently — see below):

- **⛔ One property per `Set` command.** A chained multi-property `Set` on a patch fixture silently drops everything after the first property/value pair — no error, it just doesn't apply. This is unlike `Set Layout n.e "PosX" 0 "PosY" 600`-style chains, which **do** work (see `layout-cli-assign-and-posxy-syntax`). On patch fixtures, issue one `Set` per property.

- **⛔ Bare negative numeric values get their minus sign silently eaten.** Sending an unquoted `-0.5` applies **+0.5** instead — no error, no warning. Always **quote** numeric values (`"-0.5"`) to preserve the sign; this was live-verified.

- **CLI value-spread grammar has the same trap, plus a second one.** `a Thru b` on `Set` (patch properties) parses as a spread across the selection, but a leading negative bound gets eaten the same way as above: `−5.5 Thru 5.5` degenerates to a flat `5.5 Thru 5.5` (i.e., 5.5 applied everywhere). Quoting the whole expression avoids the sign-eating bug but kills the spread grammar entirely instead — it just applies the leading number flat across the selection. Net result: **CLI spreads only work for non-negative bounds.** A spread that needs a negative bound has to go through the patch sheet's cell-editor lane instead (see `ma3-3d-stage-coordinate-conventions`), which is Dave's mass-edit idiom for exactly this case.

**Practical rule:** never trust a clean CLI echo on a patch `Set` — verify by census/readback after every batch (see `paste-round-verification-protocol`), and default to one-property-per-command, always-quoted syntax rather than chaining or relying on spread grammar for anything that could go negative.

History: none — all three gotchas captured live in the same session, 2026-07-14, while writing the template rig's final 3D positions.

History addendum: superseded 2026-07-14 — duplicate minted by parallel librarian run 10 (shard brief overlap); content folded into `patch-set-one-prop-quoted-values`.
