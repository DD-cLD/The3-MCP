---
id: jdc1-output-gated-chain
title: "JDC1 output is a gated chain — fixture master × plate master (401.1) × cell (401.1.1..12) — any level at zero is dark even while other levels show values"
role: programmer
tags: [ma3, jdc1, multi-instance, v2.4, doctrine]
when_to_load: "Before running or troubleshooting ANY JDC1 output — cells or plates showing no light despite values being set almost always means one gate level in the chain is still at zero; working recipe below opens the whole chain"
status: active
source: "findings/INBOX.md, 2026-07-16, console live 2.4.2.2"
verified: grandMA3 onPC 2.4.2.2 (Mac)
supersedes: []
superseded_by: null
---

JDC1's real output — this is the actual gating behavior of the fixture/console chain, not a visualization artifact; contrast with `jdc1-gdtf-no-gating-relations-root-cause`, which is about why onPC can't *show* this correctly — multiplies through three gate levels: **fixture master × plate master (401.1) × cell (401.1.1..12)**. Any one level at zero produces dark output even while the other levels show set values.

**Why this bit us:** post-`Store Default` (per `store-default-values-keyword` / `master-default-doctrine`, which defaults cells to zero), a pool preset that doesn't explicitly open EVERY level in the chain outputs nothing — even though the preset's own values look correct. Highlight mode bypassed the chain entirely, which is what produced the earlier "only Highlight shows it" symptom (see `jdc1-display-weirdness-symptom-history`).

**Working recipe (live-verified):** `401.1 At Full` AND `401.1.1 Thru 12 At Full` — opens the plate master AND every cell.

**Refines `master-default-doctrine`:** that doctrine says masters should ride full by default so cell-level recipes carry the look alone — this finding sharpens WHICH intermediate masters that applies to on a multi-instance fixture: plate masters are included, not just the top-level fixture master. On JDC1 specifically, the plate master (401.1) is itself an intermediate gate that must also default full, or cell-level recipes underneath it go dark regardless of their own values.

History: none — solved live 2026-07-16, same session as the JDC display-weirdness investigation.
