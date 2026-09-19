"""Shared figure-extraction. SAFE full parse (no iterparse clearing games —
the first pass used root.clear() inside the loop, which can drop nested
Dependency subtrees; that bug produced a validation run of 0 figures and is
exactly why the validation existed)."""
import xml.etree.ElementTree as ET, hashlib, gc

def num(v):
    """'*67108864' -> '67108864'. The 08-01 asterisk fixed-point guard."""
    return '' if v is None else v.strip().lstrip('*')

def figures(path):
    """name -> dict(h, shapes, attrs, meas, spds, phases, nrows). First name wins."""
    root = ET.parse(path).getroot()
    out = {}
    for dep in root.iter('Dependency'):
        if '.Phaser.' not in (dep.get('RelAddr') or ''):
            continue
        pr = dep.find('Preset')
        if pr is None:
            continue
        nm = pr.get('Name')
        if not nm or nm in out:
            continue
        shapes, attrs, meas, spds, phases = set(), set(), set(), set(), set()
        nrows = 0
        for ph in pr.iter('Phaser'):
            nrows += 1
            attrs.add(ph.get('Attribute') or '')
            meas.add(num(ph.get('Measure')))
            spds.add(num(ph.get('Speed')))
            phases.add(num(ph.get('Phase')))
            shapes.add(tuple(
                (s.get('Function') or '', num(s.get('Absolute')), s.get('Trans') or '',
                 num(s.get('Width')), num(s.get('Accel')), num(s.get('Decel')))
                for s in ph.findall('Step')))
        if not shapes:
            continue
        canon = repr((sorted(attrs), sorted(meas), sorted(shapes)))
        out[nm] = {'h': hashlib.sha1(canon.encode()).hexdigest()[:12],
                   'shapes': shapes, 'attrs': sorted(attrs),
                   'meas': sorted(m for m in meas if m), 'spds': sorted(spds),
                   'nphase': len(phases), 'nrows': nrows}
    del root; gc.collect()
    return out
