---
id: jdc1-standing-order-plate-master-full
title: "Standing order: until JDC1 viz is resolved, every output test puts plate master at 100 in the programmer"
role: programmer
tags: [ma3, jdc1, v2.4, process, verify]
when_to_load: "Before running any JDC1 output test/verification pass — apply this standing order first; also the reference for the stored plate/beam master group handles (426/446) that gate all cell output, and for the open warehouse hardware question below"
status: active
source: "findings/INBOX.md, 2026-07-16"
verified: grandMA3 onPC 2.4.2.2 (Mac)
supersedes: []
superseded_by: null
---

Until `jdc1-gdtf-no-gating-relations-root-cause` is resolved (i.e., until the profile itself is fixed or replaced), the standing order for any JDC1 output test is: **put the plate master at 100 in the programmer first.**

**[VERIFY] Hardware question carried to warehouse day:** on the real unit, ch8 (401.1 Dimmer) AND ch20 (the PLATE MASTER attribute, which gates the pixel layer ch21-56) both appear to act as gates. Which one — or whether both — the hardware actually demands is not yet confirmed; verify at warehouse day.

**Both masters gate output — stored as group handles (2026-07-21):** the JDC1 intermediate nodes carry the masters you MUST turn up to see ANY cell output. `Fixture 401 Thru 464.1` = all PLATE masters (the MAIN PLATE `.1` node — its intensity/strobe); `Fixture 401 Thru 464.2` = all BEAM masters (the MAIN BEAM `.2` node). Cell pixels (`.1.n` plate / `.2.n` tube) output nothing unless the matching master intensity is up — this is also how you reach the plate/beam STROBE function and drive intensity. Stored as reusable groups **426 cLD JDC PLATE MASTER** (`401 Thru 464.1`, 64 masters) and **446 cLD JDC BEAM MASTER** (`401 Thru 464.2`, 64 masters). Extends the plate-only standing order below to the beam branch and to a stored handle; consistent with `jdc1-output-gated-chain` (fixture master × plate/beam master × cell) and `master-default-doctrine`.

**Related tool:** for actual programming sessions (not just one-off output tests), `jdc1-utility-sequence-plate-masters-pattern` describes a deletable utility sequence (Seq 103) that holds plate masters full while working. Per its own source note it supersedes the raw per-test programmer workaround described here for that use case. This standing order remains the right call for quick verification passes, and it still carries the independent hardware-gate VERIFY question above, which the utility sequence doesn't resolve.



## ⛔ CORRECTED 2026-07-31 [0731cLD] — master group numbers, and the warehouse gate is gone

**Live read:** the stored master handles are **Group 415 `cLD JDC PLATE MASTER`** and **Group 422 `cLD JDC BEAM MASTER`**; **426/446 are EMPTY**. Any reference above to 426/446 is stale — use 415/422.

**The `[VERIFY]` ch8-vs-ch20 hardware-gate question is re-homed:** there is **no warehouse day** on this tour (ruled 2026-07-30). It resolves at **previz, else first load-in** — and note that JDC1 is exactly the fixture whose visualization cannot be trusted for the answer, so the DMX viewer or the real unit is the only readback. See `tourshow-no-warehouse-day-previz-proof-lane` and `jdc1-gdtf-no-gating-relations-root-cause`.

History: none — established live 2026-07-16; cross-referenced later the same session once the utility-sequence tool was built. Extended 2026-07-21: both the plate (.1) and beam (.2) masters confirmed as output gates and stored as reusable groups 426/446. 2026-07-31 [0731cLD] — 426/446 -> 415/422 (live read); hardware-gate VERIFY re-homed off warehouse day to previz/load-in.
