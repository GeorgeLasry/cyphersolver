"""verify2 (ronquillo1676): align each reading word by word with its key decode (the corrected transcription txi/ or tx/
decoded with keyx.py, code words expanded) and list the words the decode does not carry; for
each, say whether DECODE's margin transcription (img/DOC_*.txt, the <PLAINTEXT ES ...> lines of the main checkout)
has it.

    python research/reading_audit/verify2_ronquillo_align.py [doc ...]

Decode units: letters; a group with no or an empty key value (null, unread code, misread) is a wildcard (skippable free,
or carrying one to three reading letters at half credit). Spanish spelling equivalences count as matches (b/v/u,
i/y/j, c/z/s/x, g/j/x, q/c, n/ñ); a reading 'h' with no figure gets half credit (silent h). Words already in [...]
and clear text in ⟨ ⟩ are skipped. A word is listed when under half its letters are carried, or under half are
carried by real (non-wildcard) letters.
"""
import difflib
import glob
import pathlib
import re
import sys
import unicodedata

ROOT = pathlib.Path(__file__).resolve().parents[2]
T = ROOT / 'targets' / 'ronquillo1676'
IMG = pathlib.Path(r'C:\Users\dbour\cypher\targets\ronquillo1676\img')
TH = 0.5
GROUPS = ['bvu', 'iyj', 'czsx', 'gjx', 'qc', 'nñ']
DOCS = ['R966', 'R967', 'R968', 'R969', 'R970', 'R971', 'R972', 'R973', 'R974', 'R975', 'R976', 'R977', 'R978',
        'R979', 'R980', 'R981', 'R982', 'R983', 'R984', 'R1001']


def near(a, b):
    return a == b or any(a in g and b in g for g in GROUPS)


def norm(s):
    s = s.lower().replace('ñ', 'n')
    s = ''.join(c for c in unicodedata.normalize('NFD', s) if unicodedata.category(c) != 'Mn')
    return re.sub(r'[^a-z]', '', s)


def _key():
    ns = {'json': __import__('json'), 're': re, 'os': __import__('os')}
    cwd = __import__('os').getcwd()
    __import__('os').chdir(T)
    try:
        exec((T / 'keyx.py').read_text(encoding='utf8'), ns)
        src = (T / 'dec2.py').read_text(encoding='utf8')
        exec(src[src.index('RULES='):src.index('rows=[]')], ns)
    finally:
        __import__('os').chdir(cwd)
    return ns['K'], ns['fixtx']


K, FIXTX = _key()


def decode_units(doc):
    """[(unit, page)] from the corrected transcription (txi/, else tx/ with dec2.py's systematic fixes) decoded with
    keyx.py; a unit is a letter or 'W' (a group with no value or an empty value: null, unread code or misread)."""
    src = T / 'txi' / f'{doc}.txt'
    if not src.exists():
        src = T / 'tx' / f'{doc}.txt'
    toks, pages, page = [], [], ''
    for l in src.read_text(encoding='utf8').splitlines():
        if l.startswith('#IMAGE NAME') and ' - ' not in l:
            page = l.split(':', 1)[1].strip().split('.')[0]
        if l.startswith('C:'):
            for t in l[2:].split():
                toks.append(t); pages.append(page)
    if src.parent.name == 'tx':
        fixed = []
        for t, p in zip(toks, pages):
            for u in FIXTX([t]):
                fixed.append((u, p))
    else:
        fixed = list(zip(toks, pages))
    units = []
    for t, p in fixed:
        if t == '-':
            continue
        v = K.get(t)
        if not v:
            units.append(('W', p))
        else:
            for c in norm(v):
                units.append((c, p))
    return units


def reading_words(doc):
    s = (T / 'read' / f'{doc}_reading.md').read_text(encoding='utf8')
    s = re.sub(r'<!--.*?-->', '', s, flags=re.S).split('## Notes')[0]
    s = '\n'.join(l for l in s.splitlines() if not l.startswith('#'))
    words = []
    for m in re.finditer(r'⟨.*?⟩|\[[^\]]*\]\S*|[^\s\[\]⟨⟩]+', s, flags=re.S):
        w = m.group(0)
        if w.startswith('⟨'):
            continue
        words.append((w, None if w.startswith('[') else norm(w)))
    return [(w, n) for w, n in words if n is None or n]


def align(r, units):
    n, m = len(r), len(units)
    NEG = -1e9
    band = max(250, abs(n - m) + 250)
    S = [dict() for _ in range(n + 1)]
    B = [dict() for _ in range(n + 1)]
    S[0][0] = 0.0

    def put(i, j, v, b):
        if v > S[i].get(j, NEG):
            S[i][j] = v; B[i][j] = b

    for i in range(n + 1):
        c0 = int(i * m / max(n, 1))
        lo, hi = max(0, c0 - band), min(m, c0 + band)
        for j in range(lo, hi + 1):
            v = S[i].get(j)
            if v is None:
                continue
            if i < n:
                put(i + 1, j, v + (0.3 if r[i] == 'h' else -1.5), (i, j, 'ins'))
            if j < m:
                u = units[j][0]
                if u == 'W':
                    put(i, j + 1, v, (i, j, 'skip'))
                    for L in (1, 2, 3):
                        if i + L <= n:
                            put(i + L, j + 1, v + 0.2 * L, (i, j, 'W'))
                else:
                    put(i, j + 1, v - 1.2, (i, j, 'skip'))
                    if i < n:
                        put(i + 1, j + 1, v + (2 if r[i] == u else (1.5 if near(r[i], u) else -1)), (i, j, 'm'))
    cred = [0.0] * n
    real = [0.0] * n
    at = [None] * n
    i, j = n, m
    while (i, j) != (0, 0):
        pi, pj, k = B[i][j]
        if k == 'ins':
            cred[pi] = 0.5 if r[pi] == 'h' else 0.0; at[pi] = pj
        elif k == 'W':
            for x in range(pi, i):
                cred[x] = 0.5; at[x] = pj
        elif k == 'm':
            ok = near(r[pi], units[pj][0])
            cred[pi] = 1.0 if ok else 0.0; real[pi] = cred[pi]; at[pi] = pj
        i, j = pi, pj
    return cred, real, at


def margin(doc):
    fs = glob.glob(str(IMG / f'DOC_{doc}_*.txt'))
    if not fs:
        return ''
    s = open(fs[0], encoding='utf8').read()
    return ' '.join(re.findall(r'<PLAINTEXT ES ?([^>]*)>', s))


def margin_units(doc):
    out = []
    for tok in re.findall(r'\S+', margin(doc)):
        if '?' in tok or '*' in tok:
            out.append('W')
        else:
            out += list(norm(tok))
    return out


def align_margin(r, mu):
    """Reading letters credited by DECODE's margin transcription (in order; '?' words are wildcards)."""
    n, m = len(r), len(mu)
    if not m:
        return [0.0] * n
    NEG = -1e9
    band = max(300, abs(n - m) + 300)
    S = [dict() for _ in range(n + 1)]
    B = [dict() for _ in range(n + 1)]
    S[0][0] = 0.0

    def put(i, j, v, b):
        if v > S[i].get(j, NEG):
            S[i][j] = v; B[i][j] = b
    for i in range(n + 1):
        c0 = int(i * m / max(n, 1))
        for j in range(max(0, c0 - band), min(m, c0 + band) + 1):
            v = S[i].get(j)
            if v is None:
                continue
            if i < n:
                put(i + 1, j, v - 0.6, (i, j, 'ins'))
            if j < m:
                u = mu[j]
                if u == 'W':
                    put(i, j + 1, v, (i, j, 'skip'))
                    for L in range(1, 8):
                        if i + L <= n:
                            put(i + L, j + 1, v + 0.1 * L, (i, j, 'W'))
                else:
                    put(i, j + 1, v - 0.6, (i, j, 'skip'))
                    if i < n:
                        put(i + 1, j + 1, v + (2 if r[i] == u else (1.5 if near(r[i], u) else -1)), (i, j, 'm'))
    cred = [0.0] * n
    i, j = n, m
    while (i, j) != (0, 0):
        pi, pj, k = B[i][j]
        if k == 'W':
            for x in range(pi, i):
                cred[x] = 0.5
        elif k == 'm':
            cred[pi] = 1.0 if near(r[pi], mu[pj]) else 0.0
        i, j = pi, pj
    return cred


def in_margin(w, mtxt):
    ws = [x for x in (norm(x) for x in mtxt.split()) if x]
    joined = ''.join(ws)
    if len(w) >= 3 and w in joined:
        return 'yes'
    best = max((difflib.SequenceMatcher(None, w, x).ratio() for x in ws), default=0)
    return 'yes' if best >= 0.8 else ('~%.2f' % best if best >= 0.6 else 'no')


def check(doc):
    units = decode_units(doc)
    words = reading_words(doc)
    r = ''.join(n for _, n in words if n)
    cred, real, at = align(r, units)
    mt = margin(doc)
    mc = align_margin(r, margin_units(doc))
    pos, sus = 0, []
    for k, (w, nw) in enumerate(words):
        if not nw:
            continue
        frac = sum(cred[pos:pos + len(nw)]) / len(nw)
        fx = sum(real[pos:pos + len(nw)]) / len(nw)
        mf = sum(mc[pos:pos + len(nw)]) / len(nw)
        mx = sum(c for c in mc[pos:pos + len(nw)] if c == 1.0) / len(nw)
        if (frac < TH or fx < TH) and (mx < 0.6 or mf < 0.75):
            js = [a for a in at[pos:pos + len(nw)] if a is not None] or [0]
            ctx = ' '.join(x[0] for x in words[max(0, k - 3):k + 4])
            j0, j1 = max(0, min(js) - 6), min(len(units), max(js) + 7)
            dec = ''.join(u if u != 'W' else '_' for u, _ in units[j0:j1])
            sus.append((w, '%.2f/%.2f' % (frac, fx), ('%.2f ' % mf) + (in_margin(nw, mt) if mt else '-'), units[min(js)][1] if units else '',
                        ctx, dec))
        pos += len(nw)
    tot = sum(cred) / max(len(r), 1)
    return sus, tot, len(words)


if __name__ == '__main__':
    for doc in sys.argv[1:] or DOCS:
        s, tot, nw = check(doc)
        print(f'== {doc}: {nw} words, carried {tot:.3f}, {len(s)} listed')
        for w, f, mg, pg, c, d in s:
            print(f'  {w!r} {f} margin:{mg} p{pg} | {c}  || dec: {d}')
