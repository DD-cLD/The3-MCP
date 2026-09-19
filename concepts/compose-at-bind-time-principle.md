---
id: compose-at-bind-time-principle
title: "Keep orthogonal layers separate and compose them at recall/bind time — never pre-multiply combinations into objects (the architecture landed on this four independent times)"
role: programmer
tags: [tourshow, doctrine, architecture, portability, economy]
when_to_load: "Before creating any new set of console objects — presets, phasers, positions, groups. If the set's size is the PRODUCT of two independent axes, you are pre-multiplying and should be composing instead."
status: active
source: "cLD synthesis 2026-07-28 [0727-2cLD] across four separate rulings Dave made in one session"
verified: grandMA3 onPC 2.4.2.2 (Mac)
supersedes: []
superseded_by: null
---

**The rule: when two properties vary independently, store them as separate objects and let the
recall or the bind multiply them. Do not author the cross-product.**

This was not designed up front. The architecture arrived at it **four times independently** in
a single session, which is what promotes it from a convenience to a principle.

| Instance | Axis A | Axis B | Composed at |
|---|---|---|---|
| The recipe contract | **Group** (who) | **Preset** (what) | the cue-part recipe line |
| Phaser / spatial split | **phaser preset** (the temporal figure) | **MAtricks** (spatial distribution) | the sequence recipe line |
| Position system | **universal TILT ladder** (7) | **selective PAN set** (4) | preset recall — presets stack |
| Fixture portability | **GROUP** absorbs the rig | **PRESET** absorbs the fixture type | `/Universal` resolution |

## Why it pays

**Object count collapses from a product to a sum.** 7 tilts × 4 pans = 28 positions from
**11 objects**. A phaser template set only has to vary in TIME (figure, direction, measure)
because MAtricks carries the spatial layer — so the phaser set stays small AND the MAtricks set
stays small, instead of one exploding to cover the other.

**Portability comes free.** A pre-multiplied object has both axes baked in, so a rig change
invalidates the whole cross-product. Composed layers let one axis change while the other holds
— which is exactly why `recipe-layer-is-fixture-agnostic-doctrine` works, and why a rig
shrinking hits the FILL layer instead of the CONTENT layer.

**Editing stays local.** Change one MAtricks and every recipe bound to it moves; change one
tilt and every position built on it moves. A pre-multiplied set needs N edits.

## The deliberate exception — and why it does not break the rule

`tourshow-authoring-contract-v01` rules **one phaser preset PER USE-SITE**: copy the template
rather than share a reference, so a single cue's figure can be tuned without touching the
others. That is DRY at **authoring** time (one template set to copy from) and copies at **use**
time. **Compose the axes; duplicate the instances.** The two are not in conflict — the
composition rule is about not authoring cross-products, not about forbidding copies.

## The smell test

If you are about to create a set of objects whose SIZE is the product of two things that vary
independently, stop — you are pre-multiplying. Find the bind point that could multiply them
instead.

History: none — synthesised 2026-07-28 after the same shape appeared in four unrelated rulings
in one session (recipe contract, phaser/MAtricks split, tilt×pan positions, fixture-agnostic
portability).
