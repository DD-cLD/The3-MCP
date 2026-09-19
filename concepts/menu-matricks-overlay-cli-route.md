---
id: menu-matricks-overlay-cli-route
title: "Menu \"MatricksOverlay\" opens the MAtricks editor from the CLI, no click required"
role: programmer
tags: [ma3, cli]
when_to_load: "When you need to open the MAtricks editor programmatically/via CLI instead of clicking the encoder-bar MAtricks button"
status: active
source: "findings/INBOX.md, 2026-07-10, console live 2.4.2.2"
verified: grandMA3 onPC 2.4.2.2 (Mac)
supersedes: []
superseded_by: null
---

Clicking the encoder-bar **MAtricks button** echoes `Menu "MatricksOverlay"` in the command line — this is the CLI route to open the MAtricks editor directly, without clicking:

```
Menu "MatricksOverlay"
```

History: none — discovered live 2026-07-10 by observing the echo from a manual click.
