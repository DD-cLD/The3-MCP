---
id: desk-clear-callout-before-console-write-rule
title: "No Go+ / no console write-chain without an explicit 'desk clear?' callout and Dave's clear-to-fire — the console is ONE shared command surface and MCP writes land wherever the desk's context currently is; the clearance is PER-BATCH, not per-session"
role: programmer
tags: [console-killer, safety-rule, mcp]
when_to_load: "Before firing any Go+, builder macro, or console write-chain via MCP — mandatory pre-flight callout, repeated before EVERY write batch, not just once per session"
status: active
source: "findings/INBOX.md 2026-07-23 [0723cLD] (⛔-CLASS PAID-FOR LESSON — DESK COLLISION; collision mechanics; same-day CORRECTION reassigning the symptom); extended findings/INBOX.md [0729cLD] 2026-07-29 (near-miss, candidate per-batch sharpening)"
verified: grandMA3 onPC 2.4.2.2 (Mac)
supersedes: []
superseded_by: null
---

**⛔-CLASS PAID-FOR LESSON — DESK COLLISION (Dave):** a Go+ on Macro 6 (a 66-line builder) fired via MCP while Dave was working in the Patch. His open Patch context ate/deflected the programmer-context command lines — the collision's visible symptom that session was groups stored unlabeled/derailed and 0/11 preset stores landing, and it interrupted Dave's own patch session. **The console is ONE shared command surface** — MCP writes land in whatever context the desk currently has open, not necessarily the context the command was written for.

**NEW STANDING RULE (Dave concurred):** no `Go+` / no console write-chain without an explicit **"desk clear?" callout** and Dave's **clear-to-fire** first. Candidate MEMORY ⛔ item #11.

**Collision mechanics observed (2.4.2.2, for diagnosis reference):** with Patch open, a macro-driven `Store Group` created default-named group objects (labels did not apply), and `Group-recall → At → Store Preset` chains no-oped silently — the commands neither errored nor queued, they simply misfired against the patch context. Only a readback census caught it; screen echo alone would not have.

**⚠ CORRECTION (same day, Dave):** the desk collision itself was real and the standing rule above stands independently — but the SPECIFIC symptom signature (unlabeled groups + 0/11 presets) that first evidenced it was later reassigned: a clean re-fire of the same builder (v0.1.2) on an uncollided desk reproduced the identical symptom, proving the actual cause was the macro-XML raw-quote truncation bug (see `macro-xml-schema-cracked`), not the Patch-context collision. **Both lessons stand independently** — the collision is real and dangerous (hence the standing callout rule), and the quote bug is real and separately dangerous; only the causal attribution of that one specific symptom was corrected.

## Near-miss 2026-07-29 — desk-clear is PER-BATCH and expires the moment the operator comes back; CANDIDATE rule, not yet Dave-ratified

Dave fired the fills and went hands-on at the desk while cLD was **mid-write-chain on scratch** — *"i didn't know you started i might have oops some stuff out."*

**Full census after the halt: ALL cLD content intact** (`21.1525-27`, Seq 1511/1512 binds + XShuffle, even the scratch object at 1990) — Dave's Oops ate only his own/live state; `v.40` on disk was the net result regardless. Writes were halted and the pending gate **REVOKED cleanly** (`confirm_gate approve=false` works clean).

**NEW CANDIDATE DISCIPLINE (Dave has NOT yet ratified this, as of 2026-07-29):** a fresh **"desk clear?" callout before EVERY write batch**, not once per session — cLD announces **"starting writes" / "writes done"** so the operator always knows when the shared surface is in use. This sharpens the existing standing rule above (which already requires a callout before any Go+/write-chain) by making explicit that the clearance is **per-batch and expires the instant the operator re-engages the desk**, not a one-time session-opening check.

Card-candidate for `CARD_DESK`.

Relation: `macro-xml-schema-cracked` for the quote-bug root cause ultimately responsible for the unlabeled-groups/0-preset symptom; `console-cli-feedback-channels` for the readback-census/audit-lane mechanics that caught it; `recipe-line-cli-addressing-and-list-readback` for a possibly-related (not confirmed identical) desk-collision-family symptom, a numeric part address misresolving while a sequence-edit dialog was open.

History: none — captured 2026-07-23 [0723cLD] digest run; includes same-session correction reassigning the diagnostic symptom without retracting the standing rule. Extended 2026-07-29: added a near-miss (Dave went hands-on mid-write-chain; census showed no actual loss) and a candidate per-batch sharpening of the callout discipline, explicitly not yet Dave-ratified.


## Sibling near-miss noted 2026-08-01 [0801-2cLD] — Tier-2 confirm_gate grants also expire on TTL and are single-shot

**A different mechanism than this concept's desk-clear callout, but the same shape:** Tier-2 `confirm_gate` grants expire on their own TTL and are single-shot. A long pause mid-batch (a model switch, or the operator stepping away) silently ages out every pending grant, exactly the way this concept's "Near-miss 2026-07-29" desk-clear expiry does. Re-granting is cheap and safe, and the standing clear-to-fire posture covers it — **but the batch must be explicitly RE-GATED after any pause, never assumed still live.** Treat desk-clear expiry and confirm_gate TTL expiry as two separate mechanisms that both demand the same discipline: re-check before continuing any paused write batch, don't assume prior clearance survived the pause.
