---
id: plugin-code-runs-at-showfile-load
title: "⛔ MA3 COMPILES AND EXECUTES EVERY PLUGIN'S TOP-LEVEL CODE AT SHOW LOAD — no fire step exists or is needed; the pool object is a SEED that replants itself every load, and the real kill-switch is deleting it"
role: programmer
tags: [ma3, plugin, lua, lifecycle, v2.4, tourshow]
when_to_load: "Before assuming a plugin toolbox must be 'fired' before a show, before designing a pre-show ritual around one, or when reasoning about what survives a quit, a reload, a PSR or a file fork"
status: active
verified: grandMA3 onPC 2.4.2.2 (Mac), EU tour leg 2026-08
source: "findings/INBOX.md [0808-6cLD] 2026-08-08 — Dave's fact corrected cLD's model; source proof read from the component's FILECONTENT property under gate. Corroborated [0812-3cLD] on a forked file."
supersedes: []
superseded_by: null
---

## The law

**Every plugin's top-level code runs automatically at show load.** There is no install step, no fire step, no pre-show ritual.

**How it was established:** the inherited show's control plugin had **never been fired by anyone** — it simply came working in the handed-over file — and the Lua global table nonetheless held toolboxes from a dozen plugins. Reading the component's source confirmed it: the toolbox build is **top-level code**, written with the re-load-safe `X = X or {}` idiom.

## The corrected lifecycle

```
LOAD    → every plugin's top-level code compiles and runs (auto-install, EVERY time)
PARKED  → nothing runs while the session lives
CALLED  → a function runs for milliseconds when the native chain calls it
QUIT    → the Lua drawer evaporates
LOAD    → reinstalls, identically
```

**`SaveShow` persists the CODE only — and that is enough**, because load re-cooks the meal. **Self-healing by design:** a console restarted minutes before doors comes back with the whole toolbox intact.

**Two lives, not one:** *install* (fires once at load, builds the toolbox, the code ends) versus *use* (the native chain calls a function per song). It is a **subroutine, not a service** — nothing is resident. If the toolbox vanished mid-show the automator would still fire every macro on time; they would simply error at their last line. **Clockwork and toolbox are separate.**

## Component anatomy (banked)

- Source lives in the component property **`FILECONTENT`** — *not* `Content`.
- `FULLPATH` = the show file; `INSTREAM = true`; `FILEEXISTS = false` ⇒ **the code is EMBEDDED in the show file** and travels with it (a PSR or import carries it).
- A per-component **`SYNTAXERROR`** flag exists.
- **Fork-proof, attested:** a file rebuilt by PSR onto a different rig carried **both** toolboxes, auto-installed at load, with zero rebuild.

## Kill-switch truth

`X = nil` lasts only until the next load. **The real off is DELETING the plugin from the pool** — that removes the seed from the file. **The pool object is not a running program; it is the seed that replants itself every load. Protect the seed.**

## What this retired

An earlier same-week finding concluded a **pre-show ritual line was owed** — "fire the control plugin once per session." **WITHDRAWN — wrong.** No fire step exists. Recorded here because the wrong model is the intuitive one.

**Note the distinction from `plugin-lifecycle-autocleanup`:** that concept covers invoking a plugin explicitly as `Plugin <N>`, where MA3 runs `Main()` then immediately `Cleanup()`. This concept covers the *load-time* execution of top-level code, which is a different entry point and is what makes a persistent toolbox possible at all.

**Relation:** `plugin-lifecycle-autocleanup` · `lua-global-drawer-is-session-not-file` · `automator-tc-architecture` · `plugin-install-loop` · `plugin-import-verify-name-match` · `plugin-xml-schema`.

History: replaced the [0808-5] "no plugin at runtime" model and withdrew that block's pre-show-ritual conclusion, 2026-08-08; corroborated on a forked file 2026-08-12.
