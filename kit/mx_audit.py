"""cLD MAtricks pool auditor — name-vs-content, grammar-aware.

audit(dump_text) -> list[finding]
Dump line format:  slot|name|Prop=Val+Prop=Val...   (props omitted when None)
Self-contained, stdlib only. Re-derives the MISMATCH table and AMBIGUITY list
mechanically so a fresh dump can be re-audited without eyeball work.
"""


def audit(dump_text):
    import re

    U32 = 1 << 32
    INT_PROPS = {"XWings", "XShuffle", "XBlock", "XGroup", "XShift", "XWidth",
                 "YWings", "YShuffle", "YBlock", "YGroup", "YShift", "YWidth"}
    NUM = r"-?\d+(?:\.\d+)?"
    EPS = 1e-6
    findings = []

    def F(slot, name, kind, field, expected, actual, note, fix=None):
        findings.append({"slot": slot, "name": name, "kind": kind, "field": field,
                         "expected": expected, "actual": actual, "note": note, "fix": fix})

    # ---------- parse dump ----------
    objs = []
    for raw in dump_text.strip().splitlines():
        raw = raw.strip()
        if not raw or "|" not in raw:
            continue
        parts = raw.split("|")
        slot, name = int(parts[0]), parts[1].strip()
        props, suspect = {}, set()
        if len(parts) > 2 and parts[2].strip():
            for kv in parts[2].split("+"):
                k, v = kv.split("=", 1)
                x = float(v)
                if k in INT_PROPS and x > 0x7FFFFFFF:      # uint32 wraparound
                    x -= U32
                    suspect.add(k)
                props[k] = x
        objs.append((slot, name, props, suspect))

    # ---------- parse a name into claims ----------
    def parse_name(name):
        toks = re.sub(r"^cLD\s+", "", name).split()
        claims, notes = {}, []          # prop -> value ; notes -> (kind, field, note)
        spd = mir = shift_tok = False
        ys = None
        i = 0
        while i < len(toks):
            t = toks[i]
            nxt = toks[i + 1] if i + 1 < len(toks) else None
            if t in ("Full", "Half") and nxt and nxt.lower() == "spread":
                claims["PhaseFromX"] = 0.0
                claims["PhaseToX"] = 360.0 if t == "Full" else 180.0
                claims["_spread_prose"] = t
                i += 2; continue
            if t == "Quarter":
                claims["PhaseFromX"], claims["PhaseToX"] = 0.0, 90.0; i += 1; continue
            if t == "2-Wing":
                claims["XWings"] = 2.0; i += 1; continue
            if t == "WING":                                   # prose: bare WING = 2 wings
                if nxt and re.fullmatch(r"\d+", nxt):
                    claims["XWings"] = float(nxt); i += 2
                else:
                    claims["XWings"] = 2.0; i += 1
                continue
            if t == "QUAD":
                claims["XGroup"] = 4.0; i += 1; continue
            if t == "SHUFFLE" and nxt and re.fullmatch(r"\d+", nxt):
                claims["XShuffle"] = float(nxt); i += 2; continue
            m = re.fullmatch(r"YS(" + NUM + r")", t)
            if m:
                ys = float(m.group(1)); i += 1; continue
            m = re.fullmatch(r"([WSGB])(\d+)", t)
            if m:
                claims[{"W": "XWings", "S": "XShuffle",
                        "G": "XGroup", "B": "XBlock"}[m.group(1)]] = float(m.group(2))
                i += 1; continue
            m = re.fullmatch(r"SPD(" + NUM + r")-(" + NUM + r")", t)
            if m:
                spd = (m.group(1), m.group(2)); i += 1; continue
            if t == "MIR":
                mir = True; i += 1; continue
            if t == "SHIFT":
                shift_tok = True; i += 1; continue
            m = re.fullmatch(r"XY(" + NUM + r")", t)
            if m:
                a = float(m.group(1))
                claims.update(PhaseFromX=0.0, PhaseToX=a, PhaseFromY=0.0, PhaseToY=a)
                i += 1; continue
            if t == "XY":                                     # bare / spaced forms
                nums = []
                j = i + 1
                while j < len(toks) and len(nums) < 2 and re.fullmatch(NUM, toks[j]):
                    nums.append(float(toks[j])); j += 1
                if len(nums) == 2:
                    claims.update(PhaseFromX=0.0, PhaseToX=nums[0],
                                  PhaseFromY=0.0, PhaseToY=nums[1])
                    notes.append(("AMBIGUITY", "XY <a> <b>",
                                  "two-number XY not in grammar; read as X 0->%g, Y 0->%g"
                                  % (nums[0], nums[1])))
                elif len(nums) == 1:
                    claims.update(PhaseFromX=0.0, PhaseToX=nums[0],
                                  PhaseFromY=0.0, PhaseToY=nums[0])
                else:                                         # bare XY scoping a modifier
                    claims.update(PhaseFromX=0.0, PhaseToX=360.0,
                                  PhaseFromY=0.0, PhaseToY=360.0)
                    notes.append(("AMBIGUITY", "XY scope",
                                  "bare XY read as both-axis 0->360; alternate read scopes "
                                  "the next modifier to both axes"))
                i = j if nums else i + 1
                continue
            if t in ("X", "Y"):                               # spaced: X 360 / X FROM 180
                ax = t
                if nxt == "FROM" and i + 2 < len(toks) and re.fullmatch(NUM, toks[i + 2]):
                    claims["PhaseFrom" + ax] = float(toks[i + 2])
                    claims["_noTo" + ax] = True
                    i += 3; continue
                if nxt and re.fullmatch(NUM, nxt):
                    claims["PhaseFrom" + ax], claims["PhaseTo" + ax] = 0.0, float(nxt)
                    i += 2; continue
                notes.append(("NOTE", "token", "dangling axis token '%s'" % t)); i += 1; continue
            m = re.fullmatch(r"([XY])(" + NUM + r")to(" + NUM + r")", t)
            if m:
                ax = m.group(1)
                claims["PhaseFrom" + ax] = float(m.group(2))
                claims["PhaseTo" + ax] = float(m.group(3))
                i += 1; continue
            m = re.fullmatch(r"([XY])(" + NUM + r")", t)
            if m:
                ax = m.group(1)
                claims["PhaseFrom" + ax], claims["PhaseTo" + ax] = 0.0, float(m.group(2))
                i += 1; continue
            notes.append(("NOTE", "token", "unparsed token '%s'" % t))
            i += 1
        return claims, notes, spd, mir, shift_tok, ys

    # ---------- canonical rename suggestion from stored props ----------
    def canon(props, suspect):
        def phase(ax):
            f, tt = props.get("PhaseFrom" + ax), props.get("PhaseTo" + ax)
            if f is None and tt is None:
                return None
            if tt is None:
                return "%s FROM %g" % (ax, f)
            if abs(f or 0.0) < EPS:
                return "%s%g" % (ax, tt)
            return "%s%gto%g" % (ax, f, tt)
        out = []
        for k, tok in (("XWings", "W"), ("XShuffle", "S"), ("XGroup", "G"), ("XBlock", "B")):
            if k in props:
                out.append("%s%g" % (tok, props[k]))
        for part in (phase("X"),
                     "YS%g" % props["YShuffle"] if "YShuffle" in props else None,
                     "YSH%g%s" % (props["YShift"], "?" if "YShift" in suspect else "")
                     if "YShift" in props else None,
                     phase("Y")):
            if part:
                out.append(part)
        return "cLD " + " ".join(out)

    # ---------- per-object compare ----------
    ys_meanings = set()
    for slot, name, props, suspect in objs:
        claims, notes, spd, mir, shift_tok, ys = parse_name(name)
        prose_spread = claims.pop("_spread_prose", None)
        no_to = {ax for ax in "XY" if claims.pop("_noTo" + ax, False)}

        for kind, field, note in notes:
            F(slot, name, kind, field, None, None, note)

        # resolve ambiguous YS token against content (YS>0 = YShuffle; YS<0 = YShift, house)
        if ys is not None:
            prim = "YShuffle" if ys >= 0 else "YShift"
            alt = "YShift" if ys >= 0 else "YShuffle"
            if abs(props.get(prim, float("nan")) - ys) < EPS:
                claims[prim] = ys
                ys_meanings.add(prim)
                if ys < 0:
                    F(slot, name, "AMBIGUITY", "YS token", "YShift %g (house: negative YS = shift)" % ys,
                      "YShift=%g" % props[prim],
                      "YS<0 reads as YShift by house usage, not YShuffle; token is overloaded")
            elif abs(props.get(alt, float("nan")) - ys) < EPS:
                claims[alt] = ys
                ys_meanings.add(alt)
                F(slot, name, "AMBIGUITY", "YS token", prim, alt,
                  "YS%g resolved as %s only via content; token is overloaded" % (ys, alt))
            else:
                F(slot, name, "MISMATCH", "YS token", "%s=%g or %s=%g" % (prim, ys, alt, ys),
                  "YShuffle=%s YShift=%s" % (props.get("YShuffle"), props.get("YShift")),
                  "YS token matches neither Y prop", fix=canon(props, suspect))

        # prose Full Spread: accept 360 or house literal 360-360/N (N integer 2..64)
        if prose_spread == "Full" and "PhaseToX" in props:
            act = props["PhaseToX"]
            if abs(act - 360.0) >= EPS:
                n_impl = 360.0 / (360.0 - act) if abs(360.0 - act) > EPS else None
                if n_impl and abs(n_impl - round(n_impl)) < 1e-9 and 2 <= round(n_impl) <= 64:
                    F(slot, name, "AMBIGUITY", "PhaseToX", "360 (naive full)", act,
                      "house PHASE MATH: %g = 360-360/N at N=%d -> content-plausible; "
                      "verify an N=%d population is the intended target"
                      % (act, round(n_impl), round(n_impl)))
                    claims["PhaseToX"] = act        # suppress naive-360 mismatch
                else:
                    pass                            # fall through -> mismatch vs 360

        # claimed props vs stored
        for k, v in claims.items():
            act = props.get(k)
            tag = " (u32-decoded, needs export verify)" if k in suspect else ""
            if act is None:
                F(slot, name, "MISMATCH", k, v, None,
                  "name claims %s=%g; prop not stored" % (k, v), fix=canon(props, suspect))
            elif abs(act - v) >= EPS:
                F(slot, name, "MISMATCH", k, v, act,
                  "name claims %s=%g; stored %g%s" % (k, v, act, tag), fix=canon(props, suspect))

        # X FROM <a> claims: PhaseToX must be absent
        for ax in no_to:
            if "PhaseTo" + ax in props:
                F(slot, name, "MISMATCH", "PhaseTo" + ax, None, props["PhaseTo" + ax],
                  "name says FROM-only; PhaseTo%s is stored" % ax, fix=canon(props, suspect))

        # stored props the name never mentions (unstated X 0->360 = house default, allowed)
        default_ok = set()
        if "PhaseFromX" not in claims and "PhaseToX" not in claims \
                and abs(props.get("PhaseFromX", 1) - 0.0) < EPS \
                and abs(props.get("PhaseToX", 0) - 360.0) < EPS:
            default_ok = {"PhaseFromX", "PhaseToX"}
        for k in sorted(set(props) - set(claims) - default_ok):
            tag = " (u32-decoded=%g, needs export verify)" % props[k] if k in suspect else ""
            F(slot, name, "MISMATCH", k, None, props[k],
              "stored %s=%g not expressed in name%s" % (k, props[k], tag),
              fix=canon(props, suspect))

        # bare SHIFT token: axis+value unstated in name
        if shift_tok:
            hits = {k: props[k] for k in ("XShift", "YShift") if k in props}
            if hits:
                for k, v in hits.items():
                    tag = " (u32-decoded, needs export verify)" if k in suspect else ""
                    F(slot, name, "AMBIGUITY", "SHIFT token", "axis+value unstated",
                      "%s=%g%s" % (k, v, tag),
                      "prose SHIFT carries no axis or value; stored %s=%g%s" % (k, v, tag))
            else:
                F(slot, name, "MISMATCH", "SHIFT token", "some shift", None,
                  "name claims SHIFT; no shift prop stored", fix=canon(props, suspect))

        # uint32 wraparound fields always need export readback
        for k in sorted(suspect):
            F(slot, name, "VERIFY", k, "signed value from export", "raw u32 -> %g" % props[k],
              "integer read through Lua :Get() wrapped; confirm via Export MAtricks readback")

        # SPD claim: speed-layer props were not in the probe list
        if spd:
            F(slot, name, "VERIFY", "speed layer", "SPD %s->%s" % spd, "not probed",
              "probe gap: speed props absent from probe list; confirm via export readback "
              "(then single-prop probe once the v2.4 key name is confirmed)")

        # MIR claim: nothing in the probed prop set encodes mirror
        if mir:
            F(slot, name, "VERIFY", "MIR", "a mirror/invert prop", "none in dump",
              "no probed prop distinguishes this from a non-MIR sibling "
              "(InvertStyle=Pan pool-wide); export readback, else drop MIR from name",
              fix=canon(props, suspect))

    # ---------- pool-level passes ----------
    if len(ys_meanings) > 1:
        F(None, "(pool)", "AMBIGUITY", "YS token",
          "one meaning", "YShuffle and YShift both in use",
          "YS token is overloaded across the pool (sign-dependent); reserve YS=YShuffle, "
          "adopt YSH<n> for YShift")
    by_content = {}
    for slot, name, props, _ in objs:
        by_content.setdefault(tuple(sorted(props.items())), []).append((slot, name))
    for key, hits in by_content.items():
        if len(hits) > 1:
            F(None, " / ".join("%d %s" % h for h in hits), "NOTE", "duplicate content",
              None, None, "identical stored content under different names (alias pair)")

    order = {"MISMATCH": 0, "AMBIGUITY": 1, "VERIFY": 2, "NOTE": 3}
    findings.sort(key=lambda f: (order.get(f["kind"], 9), f["slot"] if f["slot"] else 999))
    return findings


if __name__ == "__main__":
    import sys, json
    DUMP = open(sys.argv[1]).read() if len(sys.argv) > 1 else sys.stdin.read()
    for f in audit(DUMP):
        print(json.dumps(f))
