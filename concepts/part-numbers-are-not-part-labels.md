---
id: part-numbers-are-not-part-labels
title: "⛔ A part NAME like 'P8 QX40' is a ROLE LABEL, not a part number — real part numbers are unrelated, parts expose no No via the object tree, and addressing a missing part number under /Merge CREATES a junk part"
role: programmer
tags: [ma3, cues, parts, v2.4, gotcha, tourshow]
when_to_load: "Before addressing a cue part by number from a name you read in an export or on the desk — 'P8' in a part name is a role label, and guessing the number under /Merge silently creates a junk part"
status: active
verified: grandMA3 onPC 2.4.2.2 (Mac), EU tour leg 2026-08
source: "findings/INBOX.md [0826-3cLD] 2026-08-26, {FESTIVAL} — junk part created and deleted live on a scratch cue during the masters surgery"
supersedes: []
superseded_by: null
---

**The trap.** The tour show's parts carry names in the shape `P1 …`, `P5 BEAMS`, `P8 QX40`. These are **role labels inherited from the originating programmer's convention** — a naming scheme, not an address. The part's **real number is unrelated** to the digit in its name.

**Addressing a part number that does not exist, under `/Merge`, CREATES it** — a junk empty part appears in the cue and stays. (Recovery: `Delete Part <n>` removes it; done live on a chorus cue, parts restored to their real set.)

**And you cannot look the number up from the object tree** — parts expose **no `No` property** there. So:

**⇒ PROBE BEFORE ADDRESSING.** Establish the real part set from an export-back (`export-plus-python-bulk-lane`) or by enumeration before writing to any part by number. Never derive an address from a name.

**Second-order consequence:** because parts cannot be reliably addressed by inference, a default-addressed merge is often the safer write — but that lane has its own routing behaviour, see `merge-store-part-auto-routing`.

**Relation:** `merge-store-part-auto-routing` · `cue-display-number-vs-no-addressing-gotcha` (the same display-vs-internal confusion one level up, at the cue) · `parts-per-century-emit-pattern-and-et-gate` (where the role-label convention comes from) · `recipe-part-property-surface-lua-dump`.

History: none — paid for with one junk part, 2026-08-26.
