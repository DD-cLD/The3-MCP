---
id: tourshow-showfile-intake-ritual
title: "Incoming {FESTIVAL} showfile — expected contents and the 3-step intake ritual on arrival"
role: programmer
tags: [tourshow, ma3]
when_to_load: "The moment the {FESTIVAL}/{FESTIVAL} showfile from Michael/{LD} arrives — run this ritual before touching it"
status: verify
source: "MEMORY §Bird's Eye tour — team, routing, file architecture, LTC — Incoming showfile expectation + intake ritual, 2026-07-02 evening; findings/INBOX.md 2026-07-06 + wrap 2026-07-07-beatgrid04-festival-tc"
verified: grandMA3 onPC 2.4.2.2 (Mac)
supersedes: []
superseded_by: null
---

**Expectation:** the {FESTIVAL} file ≈ last year's tour file + new songs on top (Dave ~certain, not yet confirmed on arrival).

**On arrival, in order:**
1. Inventory before touching (snapshot plugin).
2. Tag legacy vs. festival-add layers.
3. **Save As untouched "AR" master** — **"AR" = as-received** (working term, **[VERIFY] unconfirmed** — this expansion is not officially confirmed, just the working assumption). This file serves as both their fallback and our diff baseline.

**First open on 2.4:** mind the pre-2.4 migration traps — programmer wipe, Universal→Generic ID type, "Auto" preset mode removed. See `v24-migration-facts` for the full migration list.

**Ritual executed, 2026-07-06 ({FESTIVAL} file arrived):** arrived via **Dave direct-drop** of {LD}'s Drive original, `"{ARTIST} {FESTIVAL}.show"` (not via Michael, as the expectation above assumed). Steps 1–3 (inventory, tag layers, Save-As AR master) are **done**: archived as `WORKING/showfiles/ARTIST_festival_AR_as-received_2026-07-06.show`, sha256 `879061b1…7e15`, **104,954,011 B**. The as-received naming matches the working "AR = as-received" assumption but doesn't itself confirm the term officially — `status: verify` still reflects only that. **Console-side AR ritual (first onPC load, migration traps) is still pending.** Midway Deadmau5 `v3.show` (21 MB) is also in Drive, not yet pulled.

History: none — the ritual itself is settled; `status: verify` reflects only the unconfirmed "AR" term expansion, not the ritual steps. 2026-07-06: file-side execution of the ritual (steps 1–3) recorded against the real {FESTIVAL} file; console-side (first onPC load) not yet run.
