---
id: patch-set-one-prop-quoted-values
title: "Set on patch fixtures: ONE property per Set (chains silently drop), QUOTE every value (bare negatives silently flip sign) — CLI value-spreads also reject negative bounds"
role: programmer
tags: [ma3, cli, v2.4, patch, paid-for-lesson]
when_to_load: "Before generating or running ANY Set command against patch/fixture objects (PosX/PosY/PosZ/RotX/RotY/RotZ etc.) — read this before trusting a chained Set or an unquoted negative value"
status: active
source: "findings/INBOX.md, 2026-07-14, console live 2.4.2.2 — paid-for lesson; corroborated wraps/2026-07-14-3drig-mirror-doctrine-grid-drills.md"
verified: grandMA3 onPC 2.4.2.2 (Mac)
supersedes: []
superseded_by: null
---

**⛔ Hard rule — MEMORY.md hard rule #10 points here.** Everything below is live-verified, 2026-07-14, onPC 2.4.2.2.

**Context:** `Set Fixture` operates from the LivePatch prompt, addressing patch-fixture objects whose property names match their XML attribute names (`PosX`, `PosY`, `PosZ`, `RotX`, `RotY`, `RotZ` — see `patch-export-dialog-and-mvr-lane`).

**One property per `Set` on patch fixtures.** Unlike `Set Layout n.e "PosX" 0 "PosY" 600`, where chained properties work fine (see `layout-cli-assign-and-posxy-syntax`), chaining multiple properties onto one `Set` against a **patch fixture** silently drops everything after the first property/value pair. No error, no partial-success notice — the prompt returns clean. Issue one `Set` per property when writing patch-fixture attributes.

**Quote every numeric value, always — especially negatives.** A bare (unquoted) negative value in a patch `Set` has its minus sign silently eaten and the POSITIVE value gets applied instead — a command meaning `-0.5` lands as `+0.5`, with no warning. Quoting fixes it: `"-0.5"` applies correctly (live-verified). Treat this as absolute: quote every value sent to a patch `Set`, not just the ones that look negative.

**`Thru` ranges work fine with `Set`** on patch fixtures — this part behaves as expected.

**CLI value-spreads (`a Thru b`) parse but reject negative bounds.** A spread like `-5.5 Thru 5.5` is read as spread grammar, but the leading negative sign is eaten the same way as the single-value case — the result degenerates to a flat `5.5 Thru 5.5` (no real spread; every fixture gets `5.5`). Quoting the whole expression doesn't rescue it either — quoting kills the spread semantics entirely and applies the leading number flat, negative sign intact this time (`"-5.5 Thru 5.5"` → every fixture gets `-5.5`). **Net result: CLI-side `Thru` spreads only work for non-negative bounds.**

**Scope boundary pinned, 2026-07-19: this negative-bound trap is specific to patch-`Set` CLI spreads — it does NOT extend to programmer attribute spreads.** Factory macro content proves negative-bound `Thru` spreads work fine on programmer attributes: `Pan At Absolute Physical 30 Thru -30` (POSITION_WIZ's Fan In preset, see `factory-position-wiz-anatomy-and-porting`) runs correctly. The failure mode documented above is specifically about `Set` against **patch fixture** objects (PosX/RotX/etc.) — a different command context from attribute-value spreads issued against the programmer.

**Negative spreads: use the patch sheet's cell editor instead.** The patch sheet's cell editor (click into a Pos/Rot cell) is itself a `Thru`-capable calculator — typing an expression like `-7 Thru <value>` into the cell spreads that range across every selected row directly (this is how a 1.309 m spread got applied across a run of DS spots this session). This is Dave's mass-edit idiom for exactly the case the CLI can't do. **Open question:** what the cell editor's ✗-close button does (commit vs. cancel the typed expression) is unconfirmed — treat any ✗-close as a commit until tested, and verify the result either way.

**Never trust a clean echo on a patch `Set`** — verify by census/readback after every batch (see `paste-round-verification-protocol` and `export-diff-verification-loop`).

History: none — all four failure modes (chain-drop, sign-eat, spread-sign-eat, quoted-spread-degenerate) paid for live in one session, 2026-07-14; this is the concept MEMORY.md hard rule #10 points to. Extended 2026-07-19: scope boundary confirmed — the negative-bound trap is patch-Set-specific and does not apply to programmer attribute spreads (factory macro evidence).
