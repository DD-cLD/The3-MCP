---
id: edit-command-escape-pending-line-trap
title: "⛔ Escape on the Edit Command popup does NOT discard the line — it stays pending and can fire later with appended junk"
role: programmer
tags: [ma3, computer-use, danger]
when_to_load: "Before backing out of / aborting ANY staged Edit Command popup line — this is the correct abort procedure; never reach for Escape"
status: active
source: "findings/INBOX.md, 2026-07-15, console live 2.4.2.2 (caught via Display-2 Command Line History readback); corroborated in wrap 2026-07-15-multiinstance-gs-recipes-storedefault.md"
verified: grandMA3 onPC 2.4.2.2 (Mac)
supersedes: []
superseded_by: null
---

**The trap:** pressing **Escape** on the Edit Command popup does **not** discard the typed line. The popup closes, but the text stays **PENDING in the docked command line underneath** — alive, uncommitted, and waiting for whatever keystroke or click reaches the docked line next.

**Paid-for case (2026-07-15, live):** a staged line was Escaped out of, believed dead. A subsequent **canvas click appended "Grid 12/7"** to the still-pending line, and the whole thing then **committed as `Store Group 128 ... Grid 12/7 /MAtricks`** — a dirty, unintended Store the operator never meant to execute, with no further confirmation prompt in between. This was only caught via a **Display-2 Command Line History** readback (see `console-cli-feedback-channels`); the dirty Group 128 then had to be deleted.

**The rule:** to abort a staged popup line, **select-all (Cmd+A) + delete** the text, or **commit a harmless replacement value** over it. **Never trust Escape to discard content** — treat it as a popup-dismiss action only, with zero guarantee about what happens to the text it was covering.

**Distinct from the self-close race:** this is a different failure direction than the popup self-close hazard documented in `computer-use-input-loop` / `paste-round-verification-protocol`. Self-close silently **drops** a commit (nothing executes). This Escape trap silently **preserves and later contaminates** a commit (something unintended executes). Both are popup-lifecycle dangers; they fail in opposite directions, so a mitigation for one does not cover the other.

**⛔-candidate:** flagged as such in the source INBOX line — a strong candidate for promotion to a `MEMORY.md` hard-rule pointer (paid for live, matches the bar set by existing hard rules like `patch-set-one-prop-quoted-values`). The librarian does not edit `MEMORY.md`; surfaced in the run report for Dave/cLD to ratify.

History: none — first capture 2026-07-15.
