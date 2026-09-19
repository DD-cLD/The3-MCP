---
id: jdc1-utility-sequence-plate-masters-pattern
title: "Deletable utility sequence holds JDC plate masters full while programming cells — Seq 103 'cLD JDC UTIL', ON while working, OFF/deleted at cleanup"
role: programmer
tags: [ma3, jdc1, multi-instance, v2.4, process]
when_to_load: "Before a JDC1 plate/cell programming session (not just a one-off output test) — turn this sequence on first so the gate chain stands open while you work"
status: active
source: "findings/INBOX.md, 2026-07-16"
verified: grandMA3 onPC 2.4.2.2 (Mac)
supersedes: []
superseded_by: null
---

Pattern: store a **DELETABLE** utility sequence holding JDC plate masters at full. Turn it **ON** when programming plates/cells (the chain stands open, everything reads correctly per `jdc1-output-gated-chain`), turn it **OFF** when done, **delete** it at cleanup.

Built live as **Sequence 103 "cLD JDC UTIL"** — `401 Thru 464.1 At Full`.

Per its own source note, this pattern supersedes the raw per-test "put plate master at 100 in the programmer" workaround (see `jdc1-standing-order-plate-master-full`) for actual programming work — a real sequence that toggles on/off is more robust than remembering to hand-set the programmer every time. The standing order's independent hardware-gate VERIFY question (ch8 vs ch20) is untouched by this tool and remains open.

History: none — built live 2026-07-16, same session as the JDC gating root-cause work.
