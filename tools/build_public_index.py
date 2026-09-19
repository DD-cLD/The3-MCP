#!/usr/bin/env python3
"""build_public_index.py — regenerates concepts/INDEX.md and concepts/SPINE.md.
[0919-1cLD, decision D-B — closes STATE obligation 1b]

GENERATED ARTIFACTS. Never hand-edit either file; edit the concept, rerun this.

INDEX.md  — one line per concept, the form `concept_lookup` parses:
              - `id` — <title>
            grouped under `## <ROLE> · <DOMAIN>` headings, deep-link sentence
            as the single epigraph. Titles are already naive-vocabulary
            (LIBRARIAN schema), so a cold agent's words hit.
SPINE.md  — the whole-load view: full bodies of every ACTIVE `programmer` +
            `operational-live` concept, frontmatter stripped (matches what
            playbook/LIBRARIAN.md says SPINE is). Big by design; not a boot load.

THE BUILD ASSERTS ITS OWN OUTPUT PARSES BACK. It feeds INDEX.md to the server's
`concepts.index_entries()` and FAILS if the entry count != the concept-file
count, or if any id round-trips wrong. P2 found 315/340 index bullets invisible
to retrieval because the generator and the parser had never been diffed — a
generator that cannot read its own output is not a generator.

Usage:  python3 tools/build_public_index.py [--concepts concepts] [--check]
        --check: build in memory, assert, write nothing (exit 1 on failure)
"""
import argparse, os, re, sys, tempfile

HERE = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.abspath(os.path.join(HERE, '..'))
sys.path.insert(0, os.path.join(ROOT, 'server', 'src'))

EPIGRAPH = ('> A story in this corpus is a stored value: the miss that drew the '
            "rule's edge, the receipt that earned its trust, the why that covers "
            'the case nobody wrote down — 🔴 READ IT LIKE PATCH, NOT LINER NOTES.')

GENERATED = {'INDEX.md', 'SPINE.md'}
ROLE_ORDER = ['programmer', 'operational-live', 'tools', 'design',
              'operational-meta', 'historical']
SPINE_ROLES = {'programmer', 'operational-live'}

# Domain buckets — first match wins; checked against id then tags.
DOMAINS = [
    ('TIMECODE', r'\btc\b|timecode|beatgrid|beat-grid'),
    ('MACROS', r'macro'),
    ('LUA & PLUGINS', r'\blua\b|plugin|gpdf|hook|coroutine'),
    ('PATCH & RIG', r'patch|gdtf|mvr|jdc1|fixture|subfixture|multi-instance|rig\b|dmx'),
    ('RECIPES, PHASERS & MATRICKS', r'phaser|matricks|recipe|speed|gear|figure|stb|xblock|phase'),
    ('PRESETS & VALUES', r'preset|colou?r|palette|dimmer|intensity|value'),
    ('GROUPS, SELECTION & LAYOUT', r'group|selection|grid|layout|position|3d|mark-'),
    ('SEQUENCES, CUES & PLAYBACK', r'sequence|\bseq|cue|executor|page|playback|release|fade'),
    ('SHOW FILE & IMPORT LANE', r'import|export|showfile|saveshow|\bxml\b|resolver|gma3_library|library'),
    ('TRANSPORT, MCP & SAFETY', r'\bosc\b|\bmcp\b|transport|safety|tier|desk-clear|confirm|gate|send_lua|clearance'),
    ('CLI, INPUT & FEEDBACK', r'\bcli\b|command|keyword|syntax|feedback|dialog|encoder|quoted'),
    ('METHOD & VERIFICATION', r'census|reconcil|golden|smith|wrap|subagent|kit|crosswalk|scope|verify|two-pass|build-method|doctrine|law|ruling|contract'),
]


def parse_frontmatter(text):
    if not text.startswith('---'):
        return None, text
    lines = text.split('\n')
    fm, i = {}, 1
    while i < len(lines) and lines[i].strip() != '---':
        line = lines[i]
        if ':' in line and not line.startswith(' '):
            k, v = line.split(':', 1)
            fm[k.strip()] = v.strip()
        i += 1
    body = '\n'.join(lines[i + 1:]) if i < len(lines) else ''
    return fm, body


def unquote(v):
    v = (v or '').strip()
    if len(v) >= 2 and v[0] == v[-1] and v[0] in '"\'':
        v = v[1:-1]
    return v.replace('\\"', '"').strip()


def domain_of(cid, tags):
    hay = cid + ' ' + ' '.join(tags)
    for name, rx in DOMAINS:
        if re.search(rx, hay, re.IGNORECASE):
            return name
    return 'GENERAL'


def strip_history(body):
    """Drop a trailing History section (filing record, stays in the source)."""
    out, skipping, level = [], False, 0
    for line in body.split('\n'):
        m = re.match(r'^(#+)\s*(.*)$', line)
        if m:
            lvl = len(m.group(1))
            if re.match(r'history\b', m.group(2).strip(), re.IGNORECASE):
                skipping, level = True, lvl
                continue
            if skipping and lvl <= level:
                skipping = False
        if not skipping:
            out.append(line)
    return '\n'.join(out).rstrip() + '\n'


def load_concepts(cdir):
    items = []
    for fn in sorted(os.listdir(cdir)):
        if not fn.endswith('.md') or fn in GENERATED:
            continue
        text = open(os.path.join(cdir, fn), encoding='utf-8').read()
        fm, body = parse_frontmatter(text)
        if fm is None or 'id' not in fm:
            print(f'SKIP (no frontmatter/id): {fn}')
            continue
        cid = fm['id']
        if cid != fn[:-3]:
            print(f'FAIL id/filename mismatch: {fn} has id: {cid}')
            sys.exit(1)
        tags = [t.strip() for t in unquote(fm.get('tags', '')).strip('[]').split(',') if t.strip()]
        title = unquote(fm.get('title', '')) or unquote(fm.get('when_to_load', '')) or cid
        title = ' '.join(title.split())  # one line, always
        items.append({'id': cid, 'title': title, 'role': fm.get('role', 'unfiled'),
                      'status': fm.get('status', 'active'), 'tags': tags,
                      'domain': domain_of(cid, tags), 'body': body,
                      'when': unquote(fm.get('when_to_load', ''))})
    return items


def build_index(items):
    out = ['# CONCEPTS — INDEX', '',
           '*Generated by `tools/build_public_index.py` — never hand-edit; edit the concept and rebuild.*',
           '', EPIGRAPH, '',
           f'{len(items)} concepts. One line each: `- \\`id\\` — title`. Bodies at `concepts/<id>.md`.',
           'Titles are written in plain words on purpose — search them with the words you would type.',
           '`⚠ VERIFY` = banked, not yet live-confirmed. GRAVEYARD = superseded, kept for provenance.', '']
    live = [i for i in items if i['status'] != 'superseded']
    dead = [i for i in items if i['status'] == 'superseded']
    roles = ROLE_ORDER + sorted({i['role'] for i in live} - set(ROLE_ORDER))
    for role in roles:
        ri = [i for i in live if i['role'] == role]
        if not ri:
            continue
        for dom in sorted({i['domain'] for i in ri}):
            out.append(f'## {role.upper()} · {dom}')
            for i in sorted((i for i in ri if i['domain'] == dom), key=lambda x: x['id']):
                flag = '⚠ VERIFY — ' if i['status'] == 'verify' else ''
                out.append(f"- `{i['id']}` — {flag}{i['title']}")
            out.append('')
    if dead:
        out.append('## GRAVEYARD — superseded, kept for provenance')
        for i in sorted(dead, key=lambda x: x['id']):
            out.append(f"- `{i['id']}` — [superseded] {i['title']}")
        out.append('')
    return '\n'.join(out)


def build_spine(items):
    sel = [i for i in items if i['role'] in SPINE_ROLES and i['status'] != 'superseded']
    out = ['# MA3 PROGRAMMER SPINE — generated, do not hand-edit', '',
           'Source of truth: the individual files in `concepts/`. This is the whole-load view',
           '(`tools/build_public_index.py`): every ACTIVE `programmer` + `operational-live`',
           'concept, frontmatter and History sections stripped. Not a boot load — pull depth',
           'per phase (see `skills/ma3-run-session.SKILL.md`).', '',
           EPIGRAPH, '',
           f'CONCEPTS: {len(sel)} · `⚠ VERIFY` = banked, not live-confirmed.', '', '---', '']
    for dom in sorted({i['domain'] for i in sel}):
        out.append(f'## {dom}'); out.append('')
        for i in sorted((i for i in sel if i['domain'] == dom), key=lambda x: x['id']):
            flag = ' ⚠ VERIFY' if i['status'] == 'verify' else ''
            out.append(f"### {i['id']}{flag}")
            out.append(f"**{i['title']}**")
            if i['when']:
                out.append(f"*when:* {i['when']}")
            out.append('')
            out.append(strip_history(i['body']))
            out.append('')
    return '\n'.join(out), len(sel)


def assert_parses_back(index_text, items):
    from gma3_mcp import concepts as C
    with tempfile.TemporaryDirectory() as td:
        open(os.path.join(td, 'INDEX.md'), 'w', encoding='utf-8').write(index_text)
        entries = C.index_entries(td)
        ids = [e['id'] for e in entries]
        want = [i['id'] for i in items]
        problems = []
        if len(entries) != len(items):
            problems.append(f'count: parsed {len(entries)} != {len(items)} concept files')
        if set(ids) != set(want):
            problems.append(f'ids: missing {sorted(set(want)-set(ids))[:5]} extra {sorted(set(ids)-set(want))[:5]}')
        empty = [e['id'] for e in entries if not e['summary'].strip()]
        if empty:
            problems.append(f'empty summaries: {empty[:5]}')
        # naive-vocabulary smoke: words a cold agent types must hit. Only
        # meaningful on the real corpus — a 10-file proof batch legitimately
        # lacks "strobe"; the full corpus does not.
        if len(items) >= 50:
            for kw in ('strobe', 'timecode', 'crash', 'import', 'macro', 'store'):
                if not C.search(td, kw, limit=3):
                    problems.append(f'search("{kw}") returned 0 — index is unsearchable')
        else:
            print(f'(naive-vocabulary smoke skipped: {len(items)} < 50 concepts)')
        return problems


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument('--concepts', default=os.path.join(ROOT, 'concepts'))
    ap.add_argument('--check', action='store_true')
    a = ap.parse_args()
    items = load_concepts(a.concepts)
    if not items:
        print('ABORT: zero concepts found — an empty census indicts the selector first'); sys.exit(2)
    index = build_index(items)
    spine, nspine = build_spine(items)
    problems = assert_parses_back(index, items)
    if problems:
        for p in problems:
            print('PARSE-BACK FAIL:', p)
        print('VERDICT: FAIL — nothing written'); sys.exit(1)
    print(f'parse-back: {len(items)}/{len(items)} entries round-trip through concepts.index_entries()')
    if a.check:
        print('VERDICT: PASS (--check, nothing written)'); return
    open(os.path.join(a.concepts, 'INDEX.md'), 'w', encoding='utf-8').write(index)
    open(os.path.join(a.concepts, 'SPINE.md'), 'w', encoding='utf-8').write(spine)
    print(f'written: INDEX.md ({len(items)} entries, {len(index)} bytes) · '
          f'SPINE.md ({nspine} bodies, {len(spine)} bytes)')
    print('VERDICT: PASS')


if __name__ == '__main__':
    main()
