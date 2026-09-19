---
id: empty-preset-mint-clear-then-store
title: "Minting a legal EMPTY preset: Clear ×3 then a bare Store into a free slot — an empty preset asserts nothing, which is what makes it a usable SHELL for silencing an ingredient without deleting it"
role: programmer
tags: [ma3, presets, cli, v2.4, tourshow]
when_to_load: "When you need a reference target that asserts no values — silencing a pan ingredient, a master row, or any cue ingredient you want to keep structurally but neutralise"
status: active
verified: grandMA3 onPC 2.4.2.2 (Mac), EU tour leg 2026-08
source: "findings/INBOX.md [0822-1cLD] 2026-08-22 (Preset 2.199 'PAN SHELL', {FESTIVAL}) and [0826-3cLD] 2026-08-26 (Preset 1.99 'cLD MM SHELL', {FESTIVAL} — kids=0 verified)"
supersedes: []
superseded_by: null
---

**The mint:**

```
Clear
Clear
Clear
Store Preset <pool>.<free slot> /nc
```

Three `Clear`s empty the programmer completely; the bare store then writes a **legal empty preset**. Verified twice: `Preset 2.199 'PAN SHELL'` and `Preset 1.99 'cLD MM SHELL'` (readback `kids = 0`).

**Why an empty preset and not a hard zero.** An empty preset **asserts nothing** — it occupies the reference slot without contributing a value. A hard `0` asserts zero, which on a master is the exact hazard Dave ruled against ("same issue"): a closed gate that someone has to remember to reopen (`master-default-doctrine`, `mm-shell-empty-preset-armor`).

**Why a shell and not a delete.** The recipe line, the cue ingredient and the reference all stay valid and in place. The look is silenced, the structure is intact, and the **restore is a reverse repoint** rather than a rebuild. This is the middle state the whole venue-adaptation kit is built on:

- **pan shell** — 39 refs swept from three pan presets to `2.199` so venue positions could be crowned in without the tour's pan arguing (`venue-position-crowning-and-shell`);
- **MM shell** — mark-cue master rows pointed at `1.99` so every mark opens gate-neutral (`mm-shell-empty-preset-armor`).

**Fill it once and every reference follows.** Because the shell is a single object, giving it content later changes every site that points at it — the reason Dave prefers it to per-site edits.

**Caveat:** a *recipe* line can point at an empty preset (festival-proven). A **raw `AbsPreset` reference is not reachable through the object tree** and cannot be repointed this way — those rows need the desk (`recipe-line-creation-not-wire-reachable`).

**Relation:** `stock-recipe-presets-empty-as-templates` (the *other* kind of empty preset — recipe templates that are empty by design and no-op if called bare) · `venue-position-crowning-and-shell` · `mm-shell-empty-preset-armor` · `store-default-values-keyword`.

History: none — proven at {FESTIVAL} 2026-08-22, reused at {FESTIVAL} 2026-08-26.
