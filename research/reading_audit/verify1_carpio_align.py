"""verify1 (carpio1677): align each reading word by word with its key decode (read/R*.raw.txt, the figures) and list
the words the decode does not carry; for each, say whether DECODE's margin transcription (decode/DOC_*.txt) has it.

    python research/reading_audit/verify1_carpio_align.py [doc ...]

Decode tokens: syllables (letters), code words (expanded to their meanings, NOTES.md table), {..}/[..] = misread
group (wildcard, half credit), _ = null. Spanish spelling equivalences count as matches (b/v/u, i/y/j, c/z/s, g/j/x,
q/c); a reading 'h' with no figure gets half credit (silent h). Words already in [...] are skipped.
"""
import difflib
import glob
import pathlib
import re
import sys
import unicodedata

ROOT = pathlib.Path(__file__).resolve().parents[2]
T = ROOT / 'targets' / 'carpio1677'
TH = 0.5
CODES = {'sen': ['elrey', 'rey'], 'gin': ['sumajestad', 'majestad', 'elrey', 'rey'], 'jin': ['sumajestad', 'elrey'],
         'jen': ['sumajestad', 'elrey', 'reino'], 'Jen': ['reino', 'sumajestad'], 'gus': ['principe', 'principedeorange'],
         'mus': ['principe'], 'quol': ['inglaterra'], 'ana': ['napoles'], 'ten': ['francia'], 'den': ['francia'],
         'pon': ['armada'], 'san': ['bruselas'], 'tan': ['flandes'], 'gon': ['senor', 'senores'],
         'ran': ['gobernador'], 'xan': ['gobernador'], 'xon': ['guerra'], 'cun': ['espana', 'espanoles'],
         'cen': ['duque'], 'ren': ['gobierno'], 'xen': ['gobierno'], 'xin': ['gente'], 'tin': ['francia', 'franceses'],
         'gen': ['enemigos'], 'lun': ['carta', 'cartas'], 'men': ['reino'], 'min': ['sumajestad', 'majestad'],
         'V.S.': ['vs'], 'rin': []}
GROUPS = ['bvu', 'iyj', 'czs', 'gjx', 'qc', 'nñ']


def near(a, b):
    return a == b or any(a in g and b in g for g in GROUPS)


def norm(s):
    s = s.lower().replace('ñ', 'n')
    s = ''.join(c for c in unicodedata.normalize('NFD', s) if unicodedata.category(c) != 'Mn')
    return re.sub(r'[^a-z]', '', s)


def tokens(doc):
    out = []
    for t in (T / 'read' / f'{doc}.raw.txt').read_text(encoding='utf8').split():
        if t == '_':
            out.append((t, None))
        elif t in CODES:
            out.append((t, CODES[t] or None) if CODES[t] else (t, 'W'))
        elif re.match(r'^[{\[]', t) or not re.search(r'[a-z]', t.lower()):
            out.append((t, 'W'))
        else:
            out.append((t, [norm(t)]))
    return out


def reading_words(doc):
    s = (T / 'read' / f'{doc}_reading.md').read_text(encoding='utf8')
    s = re.sub(r'<!--.*?-->', '', s, flags=re.S).split('## Notes')[0]
    s = '\n'.join(l for l in s.splitlines() if not l.startswith('#'))
    words = []
    for m in re.finditer(r'⟨.*?⟩|\[[^\]]*\]|[^\s\[\]⟨⟩]+', s, flags=re.S):
        w = m.group(0)
        if w.startswith('⟨'):
            continue
        words.append((w, None if w.startswith('[') else norm(w)))
    return words


def align(r, toks):
    n, m = len(r), len(toks)
    NEG = -1e9
    S = [[NEG] * (m + 1) for _ in range(n + 1)]
    B = [[None] * (m + 1) for _ in range(n + 1)]
    S[0][0] = 0
    for i in range(n + 1):
        for j in range(m + 1):
            v = S[i][j]
            if v == NEG:
                continue
            # insert reading letter
            if i < n:
                c = 0.3 if r[i] == 'h' else -1.5
                if v + c > S[i + 1][j]:
                    S[i + 1][j] = v + c; B[i + 1][j] = (i, j, 'ins')
            if j < m:
                t, opts = toks[j]
                cost = 0 if opts is None else -1.2
                if v + cost > S[i][j + 1]:
                    S[i][j + 1] = v + cost; B[i][j + 1] = (i, j, 'skip')
                if opts == 'W':
                    for L in (1, 2, 3):
                        if i + L <= n and v + 0.2 * L > S[i + L][j + 1]:
                            S[i + L][j + 1] = v + 0.2 * L; B[i + L][j + 1] = (i, j, 'W')
                elif opts:
                    for o in opts:
                        L = len(o)
                        if i + L > n:
                            continue
                        sc = sum(2 if r[i + k] == o[k] else (1.5 if near(r[i + k], o[k]) else -1) for k in range(L))
                        if v + sc > S[i + L][j + 1]:
                            S[i + L][j + 1] = v + sc; B[i + L][j + 1] = (i, j, ('o', o))
    cred = [0.0] * n
    at = [None] * n
    i, j = n, m
    # free end: best over j at i=n is just m since skipping costs; allow trailing
    while (i, j) != (0, 0):
        pi, pj, k = B[i][j]
        if k == 'ins':
            cred[pi] = 0.5 if r[pi] == 'h' else 0.0; at[pi] = pj
        elif k == 'W':
            for x in range(pi, i):
                cred[x] = 0.5; at[x] = pj
        elif isinstance(k, tuple):
            o = k[1]
            for x in range(pi, i):
                cred[x] = 1.0 if near(r[x], o[x - pi]) else 0.0; at[x] = pj
        i, j = pi, pj
    return cred, at


def margin(doc):
    f = glob.glob(str(T / 'decode' / f'DOC_{doc}_*.txt'))[0]
    s = open(f, encoding='utf8').read()
    out = []
    for part in s.split('#COMMENTS')[1:]:
        if 'margin' not in part.split('\n')[0]:
            continue
        out += re.findall(r'<(?:PLAINTEXT|CLEARTEXT) ES ([^>]*)>', part)
    return ' '.join(out)


def in_margin(w, mtxt):
    ws = [norm(x) for x in mtxt.split()]
    ws = [x for x in ws if x]
    joined = ''.join(ws)
    if len(w) >= 3 and w in joined:
        return 'yes'
    best = max((difflib.SequenceMatcher(None, w, x).ratio() for x in ws), default=0)
    return 'yes' if best >= 0.8 else ('~%.2f' % best if best >= 0.6 else 'no')


def check(doc):
    toks = tokens(doc)
    words = reading_words(doc)
    r = ''.join(w[1] for w in words if w[1])
    cred, at = align(r, toks)
    mt = margin(doc)
    pos, sus = 0, []
    for k, (w, nw) in enumerate(words):
        if not nw:
            continue
        frac = sum(cred[pos:pos + len(nw)]) / len(nw)
        fx = sum(c for c in cred[pos:pos + len(nw)] if c == 1.0) / len(nw)
        if frac < TH or fx < TH:
            js = [a for a in at[pos:pos + len(nw)] if a is not None] or [0]
            ctx = ' '.join(x[0] for x in words[max(0, k - 3):k + 4])
            dec = ' '.join(t for t, _ in toks[max(0, min(js) - 4):max(js) + 5])
            sus.append((w, '%.2f/%.2f' % (frac, fx), in_margin(nw, mt) if mt else '-', ctx, dec))
        pos += len(nw)
    return sus


if __name__ == '__main__':
    for doc in sys.argv[1:] or ['R1002', 'R1003', 'R1006', 'R1007', 'R1008', 'R1009', 'R1010', 'R1011']:
        s = check(doc)
        print(f'== {doc}: {len(s)} suspect')
        for w, f, mg, c, d in s:
            print(f'  {w!r} {f} margin:{mg} | {c}  || dec: {d}')
