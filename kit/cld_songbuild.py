"""cLD SONG BUILD KIT — the mechanical half of a per-song crosswalk build.

What this does:  parse the prework sheet, join {LD}'s group NAMES against the
ratified SUBMAP, carry his cue skeleton + fade attributes verbatim, and emit
resolver-law-compliant sequence XML + a builder macro.

What this deliberately does NOT do:  choose phaser template classes, choose
MAtricks binds, or set speed gears.  Those are the musical read — decode_phasers()
hands you the spec, you make the call.  (idea-file-design-programmer-boundary:
the mechanics ride along, the taste does not.)

Proven by regenerating SONG_A byte-exact against what shipped to the
console at v.43 (sha f45a122f3d43…).
"""
import re, hashlib
import sys as _sys
import xml.etree.ElementTree as ET
from xml.sax.saxutils import escape
# Your rig's map. `cld_submap.py` is NOT shipped — it encodes one specific
# show's group architecture. Copy `example_submap.py` to `cld_submap.py`, point
# it at your own groups and presets, and it wins here. Without it the kit still
# runs, on the worked example.
# The load is ANNOUNCED, always. A fresh clone silently running the worked
# example while the operator believes their own rig is live is exactly the
# failure this corpus exists to prevent — never trust a clean echo.
try:
    import cld_submap as M          # your rig
    print("[songbuild] submap: cld_submap (your rig)", file=_sys.stderr)
except ModuleNotFoundError:
    import example_submap as M      # the shipped worked example
    print("[songbuild] submap: example_submap — THE WORKED EXAMPLE, NOT YOUR RIG. "
          "Copy example_submap.py to cld_submap.py and map your own groups.",
          file=_sys.stderr)

PP = "ShowData.DataPools.Default.PresetPools."
POOL_PREFIX = {"D": "Dimmer", "C": "Color", "PO": "Position", "F": "Focus", "B": "Beam"}
SEQ_ATTRS = ('AutoStart="Yes" AutoStop="Yes" AutoFix="No" AutoStomp="No" SoftLTP="Yes" '
             'XFadeReload="No" SwapProtect="No" KillProtect="No" UseExecutorTime="No" '
             'OffwhenOverridden="No" SequMIB="Enabled" AutoPrePos="No" WrapAround="Yes" '
             'MasterGoMode="None" SpeedfromRate="No" Tracking="Yes" IncludeLinkLastGo="Yes" '
             'RateScale="One" SpeedScale="One" PreferCueAppearance="No" '
             'ExecutorDisplayMode="Data and&#xD;Appearance" Action="Pool Default"')
PART_ATTRS = ('AlignRangeX="No" AlignRangeY="No" AlignRangeZ="No" PreserveGridPositions="No" '
              'MAgic="No" Mode="0" Action="Pool Default"')
FADE_ATTRS = ("CueInFade", "CueInDelay", "CueOutFade", "CueOutDelay")


# ------------------------------------------------------------------ parsing
def parse_prework(path):
    """Prework sheet -> {binds: {cue: [(gcode,pool,val,active,strict)]},
                         groups: {gcode: (source_name, lines, active, cells)},
                         phasers: {PHn: (name, uses, active)}}"""
    text = open(path, encoding="utf-8").read()
    binds, groups, phasers = {}, {}, {}

    for m in re.finditer(r"^\s{2}`([^`]+)`:\s+(.*)$", text, re.M):
        cue_no = m.group(1).split(" ", 1)[0]
        row = []
        for tok in (t.strip() for t in m.group(2).split(",") if t.strip()):
            g, rhs = tok.split(">", 1)
            core, marks = re.match(r"^(.*?)([*!s]*)$", rhs).groups()
            if core.startswith("PH"):
                pool, val = "Phaser", core
            else:
                pfx, val = core.split(".", 1)
                pool = POOL_PREFIX[pfx]
            row.append((g, pool, val, "*" in marks, "s" in marks))
        binds[cue_no] = row

    gsec = text.split("### Distinct Selection groups")[1].split("### Distinct Values presets")[0]
    for entry in re.split(r"\s\|\s|\n", gsec):
        mm = re.match(r"^(G\d+)\((\d+)/(\d+)\)\s+(.*?)(?:\s+\[(\d+) cells\])?$", entry.strip())
        if mm:
            groups[mm.group(1)] = (mm.group(4), int(mm.group(2)), int(mm.group(3)),
                                   int(mm.group(5)) if mm.group(5) else None)
    for mm in re.finditer(r"(PH\d+)\s+'([^']+)'\s+x(\d+)\((\d+) act\)", text):
        phasers[mm.group(1)] = (mm.group(2), int(mm.group(3)), int(mm.group(4)))
    return {"binds": binds, "groups": groups, "phasers": phasers}


def read_skeleton(gb_path):
    """{LD}'s export -> cue skeleton, fades carried VERBATIM.

    Carries every fade attribute the Part holds, not just CueInFade — the
    smith catch on SONG_A 13.1 (Preset2Fade=8.000 silently dropped) is why.
    """
    root = ET.parse(gb_path).getroot()
    seq = root.find(".//Sequence")
    out = []
    for cue in seq.findall("Cue"):
        part = cue.find("Part")
        fades = {}
        if part is not None:
            for k, v in part.attrib.items():
                if k in FADE_ATTRS or re.fullmatch(r"Preset\d+Fade", k):
                    fades[k] = v
        out.append({"name": cue.get("Name"), "no": cue.get("No"),
                    "trig": cue.get("TrigType"), "dup": cue.get("AllowDuplicates"),
                    "release": cue.get("Release"), "fades": fades})
    return out


def decode_phasers(gb_path, phaser_names):
    """Spec-read {LD}'s phaser defs out of the export's embeds.

    Returns per-PH: steps, baked Speed (raw / Hz / BPM), Measure, phase span,
    row count + Selective mix.  A Selective row set at cell-level dot-IDs means
    the preset carries FIXTURE REFERENCES — it cannot be re-pointed by swapping
    the group, it has to be re-authored (paid for on SONG_A's Synth Swell).
    """
    FIX = 16777216
    root = ET.parse(gb_path).getroot()
    want = {v: k for k, v in phaser_names.items()}
    defs = {}
    for pre in root.iter("Preset"):
        nm = pre.get("Name")
        if nm not in want or want[nm] in defs:
            continue
        rows = list(pre.iter("Phaser"))
        # Guard: some exports carry */?-prefixed fixed-point values (seen on
        # SONG_E and SONG_H, 0801) — strip the prefix before int().
        _fp = lambda v: int(re.sub(r'^[\*\?]', '', str(v)))
        speeds = {_fp(r.get("Speed")) for r in rows if r.get("Speed")}
        meas = {_fp(r.get("Measure")) for r in rows if r.get("Measure")}
        phases = [float(r.get("Phase")) for r in rows if r.get("Phase") is not None]
        sel = {r.get("Selective") for r in rows}
        ids = [r.get("ID", "") for r in rows]
        steps = []
        for r in rows:
            st = list(r.iter("Step"))
            if st:
                steps = [(s.get("Absolute"), s.get("Width"), s.get("Trans")) for s in st]
                break
        defs[want[nm]] = {
            "name": nm, "rows": len(rows), "selective": sorted(x for x in sel if x),
            "cell_level": any("." in i for i in ids),
            "attrs": sorted({r.get("Attribute") for r in rows}),
            "speed_bpm": [round(s / FIX * 60, 2) for s in sorted(speeds)],
            "measure_beats": [round(v / FIX, 3) for v in sorted(meas)],
            "phase_span": (min(phases), max(phases)) if phases else None,
            "nsteps": len(steps), "steps": steps,
        }
    return defs


# ----------------------------------------------------------------- emitting
def _sr(sel, ref, strict=False, mx=None, strict_attr="SelectionMode"):
    a = 'ShuffleMode="Auto" '
    if mx:
        a += f'MAtricks="Default.MAtricks.{mx}" '
    a += f'Selection="Default.Groups.{escape(sel)}" Preset="{PP}{ref}" Values="{PP}{ref}" '
    if strict:
        a += f'{strict_attr}="Strict" '
    a += 'Enabled="Yes" SelectionFromValue="No"'
    return f'                <StandardRecipe {a}/>'


def _stb_nonphaser(ref, strict=False):
    """QX40-STB expansion for a NON-phaser (direct-value) site.

    R3 (Dave 2026-08-03): every `JDC1 US [STB]` use needs a (W) white and an (R)
    release.  The PHASER branch in build_sequence has carried that since 08-03;
    this direct-value branch never did — it emitted one bare MM line.  That gap
    IS the correction sheet: 21 of the 29 rows in
    generated/desk_pack/STB_CORRECTION_SHEET.csv read 'no colour bound at all',
    and every one of them is a direct-value site.  Ruled into the emitter by
    Dave 2026-08-05 [0805-2cLD] so new songs build correct instead of enlarging
    the circle-back.

    ⛔ CONTENT SITES ONLY — and that scoping is LOAD-BEARING, not tidiness.
    The first cut of this patch also emitted `cLD LED (R)` at every direct-value
    Dimmer.0 site.  regress_ig.py refused it: SONG_A carries two such sites
    (cues 12 and 19.1), so the "blanket release" rule silently rewrote a shipped,
    heard song 122 -> 124 SRs.  The deeper reason it was wrong: the release is a
    PER-SITE DISPOSITION, not a law.  STB_CORRECTION_SHEET.csv resolves each of
    its 29 rows to one of three — ADD (9) / SUBSTITUTE (12) / **NO RELEASE (8)** —
    so any blanket rule is wrong at 8 sites by construction.  The (W) white IS a
    law (colour_wanted is `cLD STB WHITE (4.83)` on all 29 rows); the (R) rides
    the per-song `extras` with its sheet disposition.  [0805-2cLD]

      content (anything but Dimmer.0) -> MM keeps the site's own value; the
                                         COLOUR engine opens and takes
                                         `cLD LED WHITE`.               1 -> 3
      release (Dimmer.0 == Dimmer.15) -> UNCHANGED, 1 -> 1.  Its (R), if the
                                         sheet calls for one, comes via extras.

    ⚠ Scope note on the '1->4' in the prework sheets: that string is a fixed
    label emitted by batch_prework.py and describes the PHASER shape (MM dim +
    MM content + COLOUR dim + COLOUR white).  On a direct-value site the value
    IS the content, so the honest arithmetic is 1->3.  Counted as 3 here and in
    the reconciliation identity — a count without its scope is a defect.

    ⚠ The BEAM-rate release (`cLD RATE (R)`, M.STB_RATE_REL) is deliberately NOT
    emitted: at the release sites seen so far, {LD}'s own [MM]/[MMSTB]/[MMRGB]
    lines already drive `cLD QX40 MM ALL` to Beam.1 (Open) in the very same cue.
    Whether Open suffices as a rate release, or Beam.8 is additionally required,
    is a DESK verification — not a file-side inference.  [0805-2cLD]
    """
    mm = _sr("cLD QX40 MM ALL", ref, strict=strict)
    if ref == M.PRESETS_FIXED[("Dimmer", "0")]:
        return [mm]
    return [mm,
            _sr("cLD QX40 COLOR", M.PRESETS_FIXED[("Dimmer", "Full")]),
            _sr("cLD QX40 COLOR", M.STB_WHITE)]


def _cue_no(no, name):
    if no is None or name in ("OffCue", "CueZero"):
        return None
    s = no.strip()
    try:
        return str(int(s))
    except ValueError:
        try:
            return str(float(s)).rstrip("0").rstrip(".")
        except ValueError:
            return s


def build_sequence(*, name, note, skeleton, prework, colors, phaser_slots,
                   matricks=None, set_cue=None, extras=None, jdc_openers=None):
    """Emit sequence XML.

    colors        : {"{LD} preset name": "Color.<slot>"} — the per-song palette
                    collapse ({DESIGNER} families), the one genuinely per-song table.
    phaser_slots  : {"PHn": <pool-21 slot int>}
    matricks      : {(cue, gcode, PHn): 101|102}
    set_cue       : cue number that gets the JDC gate-openers ("1" normally)
    extras        : {cue: [(sel, ref), ...]} appended verbatim to that cue
    jdc_openers   : emit the two JDC master-opener lines at set_cue?
                    None (default) = follow M.JDC_OPENERS_RETIRED, which is the
                    R1 ruling: masters are never programmed, values flow from the
                    children — so new songs emit NONE. Pass True only to
                    reproduce a golden that shipped BEFORE R1 (regress_ig does).
    """
    matricks, extras = matricks or {}, extras or {}
    if jdc_openers is None:
        jdc_openers = not getattr(M, "JDC_OPENERS_RETIRED", False)
    groups, binds = prework["groups"], prework["binds"]
    X = ['<?xml version="1.0" encoding="UTF-8"?>', '<GMA3 DataVersion="2.4.2.2">',
         f'    <Sequence Name="{escape(name)}" Note="{note}" {SEQ_ATTRS}>']
    per_cue, dropped, uses_jdc = {}, [], False

    for cue in skeleton:
        nm, cue_no = cue["name"], _cue_no(cue["no"], cue["name"])
        hdr = f'Name="{escape(nm)}"'
        if cue["release"]:
            hdr += f' Release="{cue["release"]}"'
        if nm == "OffCue":
            hdr += ' Assert="Assert" AllowDuplicates="" TrigType=""'
        else:
            if cue["no"] is not None:
                hdr += f' No="{cue["no"]}"'
            if cue["dup"] is not None:
                hdr += f' AllowDuplicates="{cue["dup"]}"'
            if cue["trig"]:
                hdr += f' TrigType="{cue["trig"]}"'
        X.append(f'        <Cue {hdr}>')

        pa = PART_ATTRS if nm in ("OffCue", "CueZero") else \
            f'Name="{escape(nm)}" {PART_ATTRS} Sync="" Morph=""'
        f = cue["fades"]
        for k in FADE_ATTRS:
            if k in f:
                pa += f' {k}="{f[k]}"'
        for k in sorted((k for k in f if re.fullmatch(r"Preset\d+Fade", k)),
                        key=lambda s: int(re.search(r"\d+", s).group())):
            pa += f' {k}="{f[k]}"'

        rows = binds.get(cue_no, []) if cue_no else []
        lines = []
        for g, pool, val, _act, strict in rows:
            gname = groups[g][0]
            tgt = M.GROUPS.get(gname)
            if tgt is None:
                raise KeyError(f"UNMAPPED GROUP {g} '{gname}' — add a SUBMAP row or get a ruling")
            if tgt is M.HELD:
                dropped.append((cue_no, g, gname))
                continue
            if pool == "Phaser":
                ref = f"Phaser.{phaser_slots[val]}"
                mx = matricks.get((cue_no, g, val))
                if tgt is M.EXPAND_QX40_STB:
                    lines += [_sr("cLD QX40 MM ALL", "Dimmer.5"),
                              _sr("cLD QX40 MM ALL", ref, mx=mx),
                              _sr("cLD QX40 COLOR", "Dimmer.5"),
                              _sr("cLD QX40 COLOR", colors["__STB_COLOR__"])]
                    uses_jdc = True
                    continue
                # wash-STRICT reaches phaser lines too (smith-found latent gap,
                # fired on SONG_P 08-04; root fix 08-05. Inert on the SONG_A golden:
                # SONG_A has zero wash-phaser sites — regression proves byte-exact, no flag.)
                lines.append(_sr(tgt, ref, mx=mx, strict=strict))
            else:
                if pool == "Color":
                    ref = colors[val]
                elif pool == "Dimmer" and val in M.DIMMER_UNRULED:
                    raise KeyError(f"Dimmer '{val}' has no ruled slot — needs one console read")
                else:
                    ref = M.PRESETS_FIXED[(pool, val)]
                if tgt is M.EXPAND_QX40_STB:
                    lines += _stb_nonphaser(ref, strict=strict)
                else:
                    lines.append(_sr(tgt, ref, strict=strict))
            if tgt in M.JDC_TARGETS or tgt is M.EXPAND_QX40_STB:
                uses_jdc = True

        for sel, ref in extras.get(cue_no, []):
            lines.append(_sr(sel, ref))
        if cue_no and cue_no == set_cue and uses_jdc and jdc_openers:
            lines += [_sr(o, "Dimmer.5") for o in M.JDC_OPENERS]

        if lines:
            X.append(f'            <Part {pa}>')
            X += lines
            X.append('            </Part>')
            per_cue[cue_no] = len(lines)
        else:
            X.append(f'            <Part {pa}/>')
        X.append('        </Cue>')

    X += ['    </Sequence>', '</GMA3>', '']
    return "\n".join(X), {"per_cue": per_cue, "total": sum(per_cue.values()), "dropped": dropped}


def build_aux(*, name, note, off_fade, cue_name, lines, cue_fade=None):
    """One-bump aux sequence, Fill-2 golden shape (OffCue release + CueZero + cue 1)."""
    X = ['<?xml version="1.0" encoding="UTF-8"?>', '<GMA3 DataVersion="2.4.2.2">',
         f'    <Sequence Name="{escape(name)}" Note="{note}" {SEQ_ATTRS}>',
         '        <Cue Name="OffCue" Release="Yes" Assert="Assert" AllowDuplicates="" TrigType="">',
         f'            <Part {PART_ATTRS} CueInFade="{off_fade}"/>', '        </Cue>',
         '        <Cue Name="CueZero" No="  0">', f'            <Part {PART_ATTRS}/>', '        </Cue>',
         f'        <Cue Name="{escape(cue_name)}" No="  1" AllowDuplicates="">']
    pa = f'Name="{escape(cue_name)}" {PART_ATTRS} Sync="" Morph=""'
    if cue_fade:
        pa += f' CueInFade="{cue_fade}"'
    X.append(f'            <Part {pa}>')
    X += [_sr(sel, ref, mx=mx) for sel, ref, mx in lines]
    X += ['            </Part>', '        </Cue>', '    </Sequence>', '</GMA3>', '']
    return "\n".join(X)


def build_macro(macro_name, commands):
    X = ['<?xml version="1.0" encoding="UTF-8"?>', '<GMA3 DataVersion="2.4.2.2">',
         f'    <Macro Name="{escape(macro_name)}">']
    X += [f'        <MacroLine Command="{c}" />' for c in commands]
    X += ['    </Macro>', '</GMA3>', '']
    return "\n".join(X)


def import_pair(slot, fname):
    return [f"Delete {slot} /NoConfirmation", f"Import {slot} '{fname}' /NoConfirmation"]


def copy_label(src, dst, label):
    """Templates 21.51/52 have no file-side XML — copy on console, label inline.
    Inner quotes MUST be &quot;-escaped or MA3 truncates the line at import."""
    return [f"Copy Preset {src} At {dst}", f'Label Preset {dst} &quot;{label}&quot;']


# --------------------------------------------------------------------- lint
def lint(xml, *, kind="sequence", expect_srs=None, forbid_slots=()):
    """Doctrine lint. A structure census is NOT a content census — this checks
    the things that pass silently: dialect, scope, resolver form."""
    e = []
    if kind == "sequence":
        if "PresetData" in xml:
            e.append("cooked PresetData present (pins stale values)")
        if 'UseExecutorTime="No"' not in xml:
            e.append("UseExecutorTime is not No")
        cues = re.findall(r'<Cue Name="([^"]+)"', xml)
        if cues[:2] != ["OffCue", "CueZero"]:
            e.append(f"ordered-header law: first two cues are {cues[:2]}")
        if re.search(r'Selection="Default\.Groups\.(?!cLD )', xml):
            e.append("a Selection binds a non-cLD group")
        for m in re.findall(r'(?:Preset|Values)="[^"]*PresetPools\.(\w[\w ]*)\.([^"]+)"', xml):
            if not m[1].isdigit():
                e.append(f"pool ref by NAME not slot: {m[0]}.{m[1]}")
        if expect_srs is not None and xml.count("<StandardRecipe") != expect_srs:
            e.append(f"SR count {xml.count('<StandardRecipe')} != expected {expect_srs}")
    if "&apos;" in xml:
        e.append("&apos;-quoting present — kills path resolution silently")
    for c in re.findall(r'Command="([^"]*)"', xml):
        bare = re.sub(r"&[a-z]+;", "", c)
        if '"' in bare:
            e.append(f"raw quote in macro Command (MA3 truncates here): {c}")
        if ";" in bare:
            e.append(f"batched macro line: {c}")
    for s in forbid_slots:
        if str(s) in xml:
            e.append(f"touches protected slot {s}")
    return e


def sha(text):
    return hashlib.sha256(text.encode("utf-8")).hexdigest()
