---
id: macro-entry-helper-mechanisms
title: "Macro entry-helper mechanisms: Execute=No, inline (), AddToCmdline, and the MA2→MA3 Rosetta mapping"
role: programmer
tags: [ma3, macro, v2.4]
when_to_load: "Before building a macro that needs to pause for operator input or assemble a command interactively — or before porting an MA2 macro (@ syntax) to MA3"
status: active
source: "findings/INBOX.md, 2026-07-17 (official v2.4 QSG, macros.html, extended_command_line.html, forum thread 5563)"
verified: grandMA3 onPC 2.4.2.2 (Mac)
supersedes: []
superseded_by: null
---

Two distinct entry-helper mechanisms, plus the cell that pairs with them, plus the MA2 translation:

**1. `Execute=No`** stages the line's command on the live command line and waits for the operator to hit Please/Enter — the primary entry-helper mechanism (official v2.4 QSG; factory example `help context sensitive.xml` is built this way).

**2. Inline empty `()`** opens a value-entry text-input-field popup at that spot in the command. Officially documented (`extended_command_line.html`, "Use Parentheses () to open the Text Input Field"): the text INSIDE the parens is the prompt label (shown in the field's title bar after "Please enter"); the operator's entry replaces the parens and is processed. Quoted text `("x")` = string type; unquoted numeric `(x)` = number type; free text with no matching keyword = string. Worked example: `Fixture (the FID of the fixture)` → prompts "Please enter the FID of the fixture" → operator enters `5` → selects Fixture 5. The manual states this is "especially useful for creating macros." (Originally forum-discovered and flagged live-unconfirmed; CONFIRMED by this official doc passage the same session.)

**3. `AddToCmdline` macro-line cell:** `Yes` appends that line's command to EXISTING command-line content rather than replacing/firing it — pairs with `Execute=No` to assemble a multi-part command for the operator to finish (official `macros.html`, "Elements in a Macro").

**MA2→MA3 Rosetta** (forum 5563 + `macros.html` + `extended_command_line.html`):
- MA2 `@` at END of a macro line = MA3 `Execute=No`
- MA2 `@` at START of a macro line = MA3 `AddToCmdline=Yes`
- MA2 macro input pop-ups = MA3 inline `()` text-input field

History: created 2026-07-17 from the macro deep-dive session; folds together the initial Execute=No/() discovery with its same-session official-doc confirmation.
