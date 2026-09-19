---
id: tourshow-fx-preset-dependency-anomaly
title: "FX White/Red/Green appear in BOTH pool 21 and pool 22 at slots 110-112, despite predefined_phaser.xml having no FX presets — dependency-export routing, not a duplicate import"
role: programmer
tags: [ma3, inventory, pools, v2.4, tourshow, stock-library]
when_to_load: "If a preset appears to exist in a pool it shouldn't, per that pool's own source XML — this is the precedent case and its resolution"
status: active
source: "findings/INBOX.md, 2026-07-16, console census (opened and closed same session)"
verified: grandMA3 onPC 2.4.2.2 (Mac)
supersedes: []
superseded_by: null
---

**Anomaly found during census:** FX White/Red/Green presets sit at pool 21 slots 110-112 AND at pool 22 ("All 2") slots 110-112. But `predefined_phaser.xml` — pool 21's own source file — contains **no FX presets at all**, so their presence in pool 21 isn't explained by pool 21's own import.

**Working explanation:** the pool-22 import (Include Dependencies ON, see `tourshow-stock-recipe-library-inventory`) routed copies to the matching authored addresses in pool 21 as a dependency side-effect, rather than pool 21 having native FX presets of its own.

**Resolution (census closed):** FX Blue — the 4th FX preset, at slot 113 — was confirmed by Dave as something HE created, not a stock/import artifact. This closes the References-section census question (see `tourshow-stock-recipe-library-inventory`).

History: none — anomaly found and closed same session, 2026-07-16.
