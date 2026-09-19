---
id: never-edit-the-golden-gate-behind-a-flag
title: "When a ruling changes emitter output, gate it behind a flag and keep the regression on the legacy path — never edit the golden to match the new rule"
role: programmer
tags: [tourshow, songbuild-kit, regression, testing, ruling, jdc-openers]
when_to_load: "Before landing any ruling that changes what a generator/emitter produces for content that already shipped — deciding how to keep a regression test meaningful after the rule changes; also the reference for the JDC_OPENERS_RETIRED flag and why regress_ig.py passes jdc_openers=True"
status: active
source: "BACKLOG_pass2.md [0803-2cLD], line 13, 2026-08-03"
verified: grandMA3 onPC 2.4.2.2 (Mac)
supersedes: []
superseded_by: null
---

**GENERAL RULE (generalises well beyond MA3):** when a new ruling changes what an emitter/generator produces, gate the new behaviour behind a flag and have the regression test opt IN to the legacy path for old, already-shipped output. **Never edit the golden fixture to match the new rule** — a golden that moves to match the code proves nothing; the regression exists to catch exactly that kind of silent drift, and editing the golden is how a regression stops proving anything.

**Worked case — R1 retires the JDC gate-openers (2026-08-03).** Dave's ruling R1 ("Masters are never programmed. Values flow from the children.") retires the JDC chain-opener constants. It landed as a FLAG, not a deletion: `cld_submap.JDC_OPENERS_RETIRED=True`, and `build_sequence` gained a `jdc_openers=None` parameter that defaults to the R1 retirement (openers off). The constants stay defined in the module because **SONG_A shipped PRE-R1**, and its 122-line arithmetic (`118 live SRs − 1 HELD + 2 JDC chain-openers + 3 QX40 STB expansion = 122` — see `tourshow-seq1010-build-record`) includes the +2 openers. `regress_ig.py` now passes `jdc_openers=True` explicitly, deliberately opting SONG_A's regression into the pre-R1 legacy path.

**Verified:** the legacy path (`jdc_openers=True`) reproduces SONG_A's shipped **122 SRs**; the R1 default (`jdc_openers` unset) produces **120 SRs**; delta exactly **2** — matching the two retired openers precisely.

**Why the golden must never move:** if SONG_A's shipped 122-line export had instead been hand-edited down to 120 to match the new R1 default, the regression would pass trivially against a fixture nobody ever actually shipped. It would stop proving the kit reproduces what's on the console and start merely proving the kit reproduces itself. The flag preserves the golden's authority: already-shipped songs keep regressing against what actually shipped; new songs get the new ruling by default; nothing about the old proof is disturbed by the new rule.

**Relation:** `tourshow-songbuild-kit-and-runbook` (the kit and its `regress_ig.py` regression-proof discipline this rule extends — see this run's amendment for the sibling submap-debt fix paid the same session) · `tourshow-seq1010-build-record` (the SONG_A build whose 122-line arithmetic is the legacy case this flag protects).
