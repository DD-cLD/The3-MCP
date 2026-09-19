---
id: pool-labeling-doctrine-inherited-risk
title: "Renaming stock pools for a show is fine — the risk is INHERITING a file where someone else already did it undocumented"
role: programmer
tags: [ma3, doctrine, pools, v2.4, tourshow]
when_to_load: "Before renaming a stock pool, or before trusting pool numbers/contents at face value in an inherited/handed-off show file"
status: active
source: "findings/INBOX.md, 2026-07-16 (Dave, dictated live, [0716-1cLD] session)"
verified: grandMA3 onPC 2.4.2.2 (Mac)
supersedes: []
superseded_by: null
---

Dave's ruling: renaming a stock pool for a show is fine on its own — e.g. pool 22 → "Recipe Phasers" is a live candidate, still pending Dave's decision (see `NEXT_ACTIONS_A0716.1.md`, "pool-22 rename" under decisions pending Dave). The risk isn't renaming; it's **inheriting a file where a different programmer already renamed/customized pools without documenting it** — those custom pools become a dependency trap for whoever inherits the file next, since pool numbers/contents can no longer be trusted at face value.

This was the concrete trigger for the {TOUR} rebuild: the other-programmer custom pools found in the {FESTIVAL} predecessor file were what forced Dave's hand — "random pool creations don't travel."

**Extends `pool-discipline-stock-vs-custom`:** that concept's rule is "use stock unless a fantastic reason not to"; this finding sharpens *why* — not because renaming itself is risky, but because renaming without provenance is what breaks the next person's ability to trust the file.

History: none — doctrine stated 2026-07-16, prompted by the {FESTIVAL} file's custom pools.
