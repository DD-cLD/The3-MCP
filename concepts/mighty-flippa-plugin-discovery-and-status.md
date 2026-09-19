---
id: mighty-flippa-plugin-discovery-and-status
title: "Mighty Flippa plugin (Chris Thoms/Chris.UK) found and v0.6 downloaded — free pixel-instance inverter, relevant to pix-RotX-flip / JDC1↔JDC2 swap; no 2.4.2.2 compat statement, sandbox-test first"
role: programmer
tags: [ma3, plugin, v2.4, verify]
when_to_load: "Before working the pix-RotX-flip or JDC1↔JDC2 swap decision, or before installing/trusting Mighty Flippa on the sandbox console"
status: verify
source: "findings/INBOX.md, 2026-07-17 [0717-2cLD], Dave-requested find + Dave-side download"
verified: grandMA3 onPC 2.4.2.2 (Mac)
supersedes: []
superseded_by: null
---

**What it is:** a free grandMA3 plugin by Chris Thoms (Chris.UK) that inverts pixel-instance grid locations/layout positions **inside parent fixtures**. Four modes, including flip-by-group and a "Selection 2" mode.

**Source:** sole source found is `addondesk.com/product/mighty-flippa/` — 0 EUR, WooCommerce checkout (likely needs an email/account — Dave-side to complete). Tutorial: `youtube.com/watch?v=gNX_2rBPdMg`.

**Relevance:** directly applicable to the pending **pix-RotX-flip** / **JDC1↔JDC2 swap** decision — flipping instance grid positions inside a fixture is exactly the kind of correction that decision needs.

**Compatibility caveat:** **no published 2.4.2.2 compatibility statement.** Sandbox-test before trusting it on the working show.

**Status (2026-07-17):** **v0.6 RELEASE already downloaded Dave-side** at `~/Downloads/ChrisUK_MightyFlippa_0.6_RELEASE` (mounted in this project's working directories). **Next-session action:** read the actual Lua source, then run a sandbox install test — in that order, code read before install.

History: created 2026-07-17 — plugin found and Dave downloaded the v0.6 release in the same session; not yet read or installed. Status `verify` until the code read + sandbox test happen.
