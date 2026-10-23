"""Apply the relabel brief (RELABEL_BRIEF.md) to one target's profile.json (relabel batch 0).

Used from a short per-target call, e.g.

    from relabel_r0 import relabel
    relabel('castelcicala1816', default_state=('decoded, not read', 'why'), lang='it',
            cls='not read', method='not solved', fraction=0.0, fraction_source='...', step='...')

save() patches only the changed spans of the source file, so the hand formatting of the rest is kept.
"""
import json
import pathlib

ROOT = pathlib.Path(__file__).resolve().parents[2]
DATE = '2026-10-22'
BY = 'Claude (reading audit)'
NL = chr(10)
_WS = ' \t\r' + NL


def load(folder):
    return json.loads((ROOT / 'targets' / folder / 'profile.json').read_text(encoding='utf8'))


def _compact(x):
    return json.dumps(x, ensure_ascii=False)


def _parse(s, i=0):
    """Minimal JSON parser returning nodes (kind, children-or-value, start, end) with source spans."""
    while s[i] in _WS: i += 1
    c = s[i]
    if c == '{':
        j, kids = i + 1, {}
        while True:
            while s[j] in _WS: j += 1
            if s[j] == '}': return ('d', kids, i, j + 1)
            if s[j] == ',': j += 1; continue
            ks = j
            k, j = json.decoder.scanstring(s, j + 1)
            while s[j] in _WS + ':': j += 1
            node = _parse(s, j)
            kids[k] = (ks, node)
            j = node[3]
    if c == '[':
        j, kids = i + 1, []
        while True:
            while s[j] in _WS: j += 1
            if s[j] == ']': return ('l', kids, i, j + 1)
            if s[j] == ',': j += 1; continue
            node = _parse(s, j)
            kids.append(node)
            j = node[3]
    v, end = json.JSONDecoder().raw_decode(s, i)
    return ('v', v, i, end)


def _value(node):
    k, v = node[0], node[1]
    if k == 'v': return v
    if k == 'd': return {kk: _value(n) for kk, (_, n) in v.items()}
    return [_value(n) for n in v]


def _indent_of(s, pos):
    j = s.rfind(NL, 0, pos)
    return s[j + 1:pos] if s[j + 1:pos].strip() == '' else None


def _enc(x, pad, ind):
    if not isinstance(x, (dict, list)) or not x:
        return _compact(x)
    p1 = pad + ' ' * ind
    if isinstance(x, dict):
        return '{' + NL + (',' + NL).join(f'{p1}{_compact(k)}: {_enc(v, p1, ind)}' for k, v in x.items()) + NL + pad + '}'
    if all(not isinstance(v, (dict, list)) for v in x):
        return _compact(x)
    return '[' + NL + (',' + NL).join(p1 + _enc(v, p1, ind) for v in x) + NL + pad + ']'


def _patch(s, node, new, ind, out):
    kind, kids, a, b = node
    if _value(node) == new: return
    oneline = NL not in s[a:b]
    if kind == 'd' and isinstance(new, dict) and all(k in new for k in kids) and kids:
        last = None
        for k, (ks, n) in kids.items():
            _patch(s, n, new[k], ind, out)
            last = (ks, n)
        for k, v in new.items():
            if k in kids: continue
            if oneline:
                out.append((last[1][3], last[1][3], f', {_compact(k)}: {_compact(v)}'))
            else:
                pad = _indent_of(s, last[0]) or ' ' * ind
                out.append((last[1][3], last[1][3], f',{NL}{pad}{_compact(k)}: {_enc(v, pad, ind)}'))
        return
    if kind == 'l' and isinstance(new, list) and len(new) >= len(kids) and kids:
        for n, v in zip(kids, new):
            _patch(s, n, v, ind, out)
        last = kids[-1]
        for v in new[len(kids):]:
            if oneline:
                out.append((last[3], last[3], ', ' + _compact(v)))
            else:
                pad = _indent_of(s, last[2]) or ' ' * ind
                lone = NL not in s[last[2]:last[3]]
                out.append((last[3], last[3], ',' + NL + pad + (_compact(v) if lone else _enc(v, pad, ind))))
        return
    if oneline or kind == 'v':
        out.append((a, b, _compact(new)))
    else:
        pad = _indent_of(s, a)
        if pad is None:
            j = s.rfind(NL, 0, a); line = s[j + 1:a]; pad = line[:len(line) - len(line.lstrip())]
        out.append((a, b, _enc(new, pad, ind)))


def save(folder, p):
    f = ROOT / 'targets' / folder / 'profile.json'
    s = f.read_text(encoding='utf8')
    ind = 2 if s.startswith('{' + NL + '  "') else 1
    out = []
    _patch(s, _parse(s), p, ind, out)
    # same-position inserts (several items appended to one list) must keep their order: apply later ones first
    for _, (a, b, r) in sorted(enumerate(out), key=lambda t: (t[1][0], t[0]), reverse=True):
        s = s[:a] + r + s[b:]
    assert json.loads(s) == p
    f.write_text(s, encoding='utf8', newline='')


def _key(t):
    d = t.get('doc')
    return '/'.join(d) if isinstance(d, list) else str(d)


def relabel(folder, *, lang=None, langs=None, default_state=None, states=None, reviews=None,
            cls=None, method=None, method_basis=None, fraction=None, fraction_method='measured',
            fraction_source=None, coherent=None, parts=None, step=None, step_result='failed', extra=None):
    """states: {doc-key or index: (state, note)}; reviews: {doc-key or index: (grade, note)};
    langs: {doc-key or index: lang}. default_state applies to entries not in states."""
    p = load(folder)
    o = p['outcome']
    states, reviews, langs = states or {}, reviews or {}, langs or {}
    for i, t in enumerate(o.get('texts', [])):
        k = _key(t)
        L = langs.get(k, langs.get(i, lang))
        if L and (not t.get('language') or k in langs or i in langs):
            t['language'] = L
        st = states.get(k, states.get(i, default_state))
        if st:
            t['state'] = st[0]
            if st[1]:
                t['note'] = st[1]
        rv = reviews.get(k, reviews.get(i))
        if rv:
            t['state'] = 'read'
            t['reading_review'] = {'grade': rv[0], 'by': BY, 'date': DATE, 'note': rv[1]}
    if cls: o['class'] = cls
    if method: o['method'] = method
    if method_basis: o['method_basis'] = method_basis
    if fraction is not None:
        o['fraction_read'] = fraction
        o['fraction_read_method'] = fraction_method
        if fraction_source: o['fraction_read_source'] = fraction_source
    if coherent is not None:
        o['fraction_coherent'] = coherent
    if parts is not None:
        o['parts'] = parts
    if extra:
        extra(p)
    if step:
        p['solution'].append({'date': DATE, 'kind': 'verification', 'what': step, 'result': step_result,
                              'technique': ['language-model scoring', 'statistical test']})
    save(folder, p)
    return p
