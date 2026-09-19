---
id: jdc1-gdtf-no-gating-relations-root-cause
title: "JDC1's GDTF declares NO relation for plate/beam master gating cells — only per-cell virtual dimmers — so onPC viz structurally cannot gate; layout/stage intensity is untrustworthy, DMX viewer + real unit = truth"
role: programmer
tags: [ma3, jdc1, gdtf, v2.4, danger]
when_to_load: "Before trusting JDC1's Layout/Stage-view intensity for ANY output judgment call — read this first. Also useful as a template for root-causing any other multi-instance fixture that looks visually wrong: check the GDTF's relations, not just its channel map"
status: active
source: "findings/INBOX.md, 2026-07-16 — GDTF read of GLP@GLP JDC1.gdtf, extracted from cld_patch_v4.mvr (see patch-mvr-export-import-lane-and-schema); console 2.4.2.2"
verified: grandMA3 onPC 2.4.2.2 (Mac)
supersedes: [jdc1-display-weirdness-symptom-history]
superseded_by: null
---

Read directly from the GDTF (**GLP@GLP JDC1.gdtf**, pulled out of `cld_patch_v4.mvr` — every patched fixture type's GDTF is embedded in an MVR export, see `patch-mvr-export-import-lane-and-schema`): JDC1's **ONLY** dimmer relations are per-cell **VIRTUAL** dimmers — a single `PLATE_Dimmer` **Multiply** relation over that cell's own R/G/B — plus 7 **Grand**-master follows.

**No relation in the profile declares** ch8 plate master, ch20 PLATE MASTER, or ch3 beam master as gating their cells. That gating is real — it exists in the physical fixture's electronics — but it is **ABSENT from the GDTF profile**.

**Consequence:** onPC's visualization structurally CANNOT gate JDC1 the way the real fixture does, in either direction:
- **dark-with-values:** the programmer/cue holds correct values but the profile doesn't render the intended output, because it isn't multiplying through the (electronics-only) master chain.
- **lit-without-output:** the profile renders a defaulted/full master level as visible output even when the true master chain would actually leave the real fixture dark.

Both directions are **structural** — not a display bug fixable by switching views, and not something an MA3-side workaround changes, because the information the visualizer would need simply isn't present in the profile.

**Practical rule:** layout/stage intensity readings on JDC1 are **UNTRUSTWORTHY** with the stock profile. The DMX viewer and the real unit are the only sources of truth for JDC1 output. See `jdc1-standing-order-plate-master-full` for the standing operational workaround during output tests, and `jdc1-output-gated-chain` for the separate, *real* (non-viz) fact about how many gate levels the actual DMX output chain requires.

This root cause directly explains and supersedes the two prior symptom/suspicion observations from the same investigation — see `jdc1-display-weirdness-symptom-history`.

History: none — root-caused live 2026-07-16, same session as the symptom and suspicion that preceded it.
