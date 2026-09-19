---
id: jdc1-display-weirdness-symptom-history
title: "JDC1 layout/stage viz looked wrong in BOTH directions (dark-with-values, then lit-without-output) — both symptoms of the same GDTF gating gap"
role: historical
tags: [ma3, jdc1, gdtf, v2.4]
when_to_load: "Historical only: if you're chasing why JDC1 doesn't visually match programmer state in Layout/Stage view, go straight to the root-cause concept instead — this file just records the diagnostic path that got there"
status: superseded
source: "findings/INBOX.md, 2026-07-16"
verified: grandMA3 onPC 2.4.2.2 (Mac)
supersedes: []
superseded_by: jdc1-gdtf-no-gating-relations-root-cause
---

Two sequential observations from the same investigation, both later explained by one root cause.

**First symptom (dark-with-values):** JDC1 fill/intensity values didn't render in Layout views or Stage view — only Highlight mode showed values + cell fill. At the time this read as a layout-display bug, to be drilled on SPOTS+WASHES once investigated with a real picture in front of the team.

**Second symptom (lit-without-output), after `Store Default` staging:** with the plate master defaulted to full and cells at zero (the `master-default-doctrine` staging pattern), the physically/DMX-correct result is dark — but the fixture PROFILE kept rendering the defaulted plate master AS output, staying lit-looking even after Clear. The working suspicion at the time: onPC viz reads master-level intensity directly instead of multiplying the full master×cell chain — i.e., the profile was suspected of misreporting output in **both** directions (this dark-with-values case, and the new lit-without-output case).

**Resolution:** both directions turned out to be the same structural gap, not a display bug and not two separate bugs — see `jdc1-gdtf-no-gating-relations-root-cause`. Fully superseded by that concept; kept here only as the record of how the investigation got there (symptom → suspicion → root cause).

History: superseded 2026-07-16, same session the root cause was found (GDTF read of GLP@GLP JDC1.gdtf from cld_patch_v4.mvr).
