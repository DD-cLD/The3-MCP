"""example_submap.py — the substitution map, as code. WORKED EXAMPLE.

WHAT THIS IS
------------
`cld_songbuild.py` turns a source LD's export into cue lines for YOUR rig. It
never guesses: it reads a map that says "when the source calls for THIS group,
bind THAT one of mine." This file is that map, populated with a small fantasy
rig so the kit runs on a fresh clone.

  Copy it to `cld_submap.py`, replace the fantasy names with your own, and
  `cld_songbuild.py` will import yours instead (it prefers `cld_submap`, and
  falls back to this file).

WHY IT IS NAME-KEYED, NOT NUMBER-KEYED
--------------------------------------
Group numbers are assigned per sheet in order of use, so the same group lands on
a different code in every song. NAMES are the stable join key. Every target
below is a NAME, never a number — your contract groups will not sit at the same
slots as anyone else's, so name-form Selection binds are the only safe lane.

THE SENTINELS
-------------
Not every source group maps one-to-one. Two escape hatches:

  HELD             — no equivalent on this rig. The emitter DROPS the line and
                     records the cue site, so a human can decide later. Silence
                     is never the answer; a recorded hold is.
  EXPAND_MULTI_STB — one source group becomes a MULTI-LINE pattern on your rig
                     (a strobe layer that needs colour + rate + release, say),
                     not a single bind. The emitter expands it.

Sentinels are compared with `is`, not `==`, so a real group named "__HELD__"
could never collide with one.

VERSION STAMP: written against grandMA3 onPC 2.4.2.2 (Mac). Slot-addressing
rules follow `concepts/import-resolver-laws` — numeric preset NAMES parse as
slot INDEXES, which is why every preset below is written as `Pool.slot`.
"""

HELD = "__HELD__"                    # park the line, record the cue site
EXPAND_MULTI_STB = "__MULTI_STB__"   # multi-line pattern, not a single bind

# Back-compat alias: the show this kit came from called the second sentinel
# after its own fixture type. Keep both names pointed at the same object so
# either spelling works.
EXPAND_QX40_STB = EXPAND_MULTI_STB

# ---------------------------------------------------------------- groups
# source LD's group NAME -> your group NAME (or a sentinel above).
#
# Note the shape of the real problem: the source names carry FIXTURE TYPE and
# ATTRIBUTE QUALIFIERS ([RGB], [STB], (Grid)) that your rig may not split the
# same way. Several source names collapsing onto one of your groups is normal
# and correct — that is the map doing its job.
GROUPS = {
    # --- house wash: source splits by colour vs strobe layer, we do not
    "Wash Bar [RGB] (Fest)":        "HOUSE WASH LEFT",
    "Wash Bar [RGB] (Lin) (Fest)":  "HOUSE WASH LEFT",
    "Wash Bar [STB] (Fest)":        "HOUSE WASH RIGHT",

    # --- overhead grid
    "Grid Pods [RGB] (Grid)":       "OVERHEAD POD GRID",
    "Grid Pods [MM] (Grid)":        "OVERHEAD POD GRID",

    # --- back truss beams
    "Back Beams [RGB]":             "BACK TRUSS BEAMS",
    "Back Beams [STB]":             EXPAND_MULTI_STB,   # 3-line strobe pattern here

    # --- floor package
    "Floor Cans [RGB]":             "FLOOR UPLIGHT ROW",

    # --- side booms: this rig has none. Recorded, not silently dropped.
    "Side Booms [RGB]":             HELD,
    "Side Booms [STB]":             HELD,
}

# Groups that are MULTI-CELL: a bind against one of these wants the whole-fixture
# block, not a single cell (see `concepts/` on whole-fixture block law).
MULTI_CELL_TARGETS = {"OVERHEAD POD GRID", "HOUSE WASH LEFT"}
JDC_TARGETS = MULTI_CELL_TARGETS          # name the emitter still uses

# Master/opener groups that a cue might have been expected to drive open.
GATE_OPENERS = ("OVERHEAD POD MASTER", "BACK TRUSS MASTER")
JDC_OPENERS = GATE_OPENERS                # name the emitter still uses

# ⛔ MASTERS ARE NEVER PROGRAMMED. All values flow from the children; masters sit
# at their default and no cue opens or closes one. Then there is never a question
# of whether a master was opened at the right spot — and nothing has to be swept
# at the end, because the asymmetry is the point: leaving a master at its default
# is harmless, setting it to 0 and forgetting to restore is the failure.
#
# Leave this True unless you have a specific reason. False re-enables the opener
# lines, which exists only so a pre-existing regression golden keeps reproducing
# byte-exact.
JDC_OPENERS_RETIRED = True

# ---------------------------------------------------------------- presets
# (pool-prefix, source preset NAME) -> your slot ref.
#
# Read your OWN ladder off the console and write it here. It will NOT be
# contiguous and it will NOT match this example. A numerically-named preset is
# SLOT-addressed by law: `Dimmer.0` resolves to nil, so a "0%" preset living in
# slot 15 must be written `Dimmer.15`.
PRESETS_FIXED = {
    ("Dimmer", "Full"): "Dimmer.5",
    ("Dimmer", "75"):   "Dimmer.7",
    ("Dimmer", "50"):   "Dimmer.9",
    ("Dimmer", "30"):   "Dimmer.10",
    ("Dimmer", "20"):   "Dimmer.11",
    ("Dimmer", "10"):   "Dimmer.13",
    ("Dimmer", "0"):    "Dimmer.15",
    ("Focus", "Narrow"): "Focus.2",
    ("Focus", "Medium"): "Focus.3",
    ("Focus", "Wide"):   "Focus.4",
    ("Beam", "Open"):     "Beam.1",
    ("Beam", "RateFast"): "Beam.2",
    ("Beam", "RateMed"):  "Beam.3",
    ("Beam", "RateSlow"): "Beam.4",
}

# The strobe-layer trio the EXPAND_MULTI_STB sentinel emits. Mint these on your
# own rig and record the slots here; the release pair is what lets a strobe
# hand back cleanly instead of latching.
STB_WHITE    = "Color.83"   # a white the strobe layer opens on
STB_RELEASE  = "Color.84"   # its release partner
STB_RATE_REL = "Beam.8"     # rate release — see the emitter's note on why this
                            # one is deliberately NOT auto-emitted everywhere

# Dimmer preset names that are bare numerals with no ruled slot yet. Anything in
# here makes the emitter refuse rather than guess. Empty = the ladder is fully
# mapped, which is where you want to be before a build.
DIMMER_UNRULED = set()

# ------------------------------------------------------- phaser templates
# Template NAME -> slot in your phaser pool. Read these off the console once.
TEMPLATES = {
    "SINE": 51, "LINEAR": 52,
    "RAMP UP": 53, "RAMP DOWN": 54, "SNAP": 55, "TRAPEZE": 56, "CHASE": 57,
    "SINE 1/2": 58, "LINEAR 1/2": 59, "RAMP UP 1/2": 60, "RAMP DOWN 1/2": 61,
    "SNAP 1/2": 62, "STROBE": 63, "CIRCLE": 64, "CIRCLE INV": 65,
}
# Some stock templates carry no XML in the export payload, so they cannot be
# cloned file-side — they must be COPIED on the console itself. Anything listed
# here the emitter will refuse to import.
COPY_ONLY = {51, 52}

# ------------------------------------------------------------- MAtricks
MATRICKS = {"full": 101, "half": 102}   # your full-spread / half-spread objects


# --------------------------------------------------------------- numbering
def song_slots(century):
    """Every per-song number falls out of one number: the sequence century.

    Pick a century per song (1000, 1100, 1200 ...) and the rest is arithmetic.
    Offsets are a convention, not a law — but keep them CONSTANT across a show,
    because the whole point is that a number tells you what it is on sight.
    """
    return {
        "main_seq":      century + 10,   # 1000 -> your main at 1010
        "aux_seq_base":  century + 11,   # aux run upward from +11
        "phaser_base":   century + 20,   # phaser pool 21.<century>20+
        "source_main":     century,      # the source's own main, for pairing
        "source_aux_base": century + 1,  # the source's aux run
    }


def aux_slot(source_seq):
    """Source aux 1001 -> ours 1011. Straight +10, keeps the pairing readable."""
    return source_seq + 10


def beats_to_seconds(beats, bpm):
    """Fade math regenerates per song — NEVER copy another song's literal seconds.

    A fade authored in beats is a musical intent; the same intent at a different
    tempo is a different number of seconds. Copying seconds across songs is the
    single easiest way to make a build look right and feel wrong.
    """
    return round(beats * 60.0 / bpm, 3)
