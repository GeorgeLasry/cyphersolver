"""Verification pass (22 Oct 2026), matignon1586: align each hand-built reading letter by letter with the corrected
figures and the leaf key's letter sets, and list the words the figures do not carry.

    python research/reading_audit/verify1_matignon_align.py [doc ...]

A figure carries a reading letter when the letter is in its set (codes give whole words); u/v, i/j/y count as one.
A '+' or '' figure (unidentified code, null, stop) carries nothing and may be skipped free; a figure not in the key
carries any one letter at half weight. Words already in [...] are aligned but not listed. Braces {...} (f. 201's
wording) and italics (clear text) are cut out. Per word: share of its letters carried; listed when below 0.6.
"""
import json
import pathlib
import re
import sys
import unicodedata

ROOT = pathlib.Path(__file__).resolve().parents[2]
T = ROOT / 'targets' / 'matignon1586'
C = T / 'brackx2026' / 'corrections'
TH = 0.8

# doc: reading file, (section start, section end), cipher files [(file, header-section or None, line range or None)], key
DOCS = {
    'f173': ('reading_f173.md', ('## The cipher', 'Files:'), [('f173_cipher.txt', None, None)], 'f173'),
    'f196_201': ('reading_f196_201.md', ('## The fever', None), [('f196_201_cipher.txt', '## f. 196', None)], 'f196_201'),
    'f201': ('reading_f196_201.md', ('## The fever', None), [('f196_201_cipher.txt', '## f. 201', None)], 'f196_201'),
    'f196v': ('reading_f196v.md', ('## The siege', '## The clear close'), [('f196v_cipher.txt', None, None)], 'f196v'),
    'f177': ('reading_f177.md', ('## The cipher', '## What stays open'), [('f177_cipher.txt', None, None)], 'f177'),
    'f110': ('reading_f110.md', ('## The cipher', 'Files:'), [('f110_v3_cipher.txt', None, None)], 'f110'),
    'f123v': ('reading_f123.md', ('## The cipher, f. 123v', '## Notes on the reading'),
              [('f123_cipher.txt', '## f. 123v', None)], 'f123'),
    'f124v': ('reading_f124.md', ('## f. 124v', '## The clear end'), [('f124_cipher.txt', None, (42, 79))], 'f124'),
    'f143v': ('reading_f143v_tail.md', ('## The cipher, from', '## Notes on the words'),
              [('f143v_cipher.txt', None, (26, 35))], None),
}
NEAR = [set('uv'), set('ijy')]


def norm(s):
    s = ''.join(c for c in unicodedata.normalize('NFD', s.lower()) if unicodedata.category(c) != 'Mn')
    return re.sub(r'[^a-z]', '', s)


def section(path, a, b):
    s = path.read_text(encoding='utf8')
    i = s.index(a)
    j = s.index(b, i + len(a)) if b else len(s)
    return s[s.index('\n', i):j]


def figures(spec):
    toks, lines = [], []
    for f, sec, rng in spec:
        ls = (C / f).read_text(encoding='utf8').splitlines()
        if sec:
            i = ls.index(sec)
            j = next((k for k in range(i + 1, len(ls)) if ls[k].startswith('## ')), len(ls))
            ls = ls[i + 1:j]
        else:
            ls = [l for l in ls if not l.startswith('#')]
        if rng:
            ls = ls[rng[0] - 1:rng[1]]
        n = 0
        for l in ls:
            if l.startswith('#'):
                continue
            n += 1
            for t in l.split():
                toks.append(t); lines.append(n)
    return toks, lines


def key_for(name):
    if name is None:
        k = json.loads((T / 'key_cipher1.json').read_text(encoding='utf8'))
    else:
        k = json.loads((T / f'key_cipher1_{name}.json').read_text(encoding='utf8'))
    return {t: [x.replace('v', 'u').replace('j', 'i') for x in v] for t, v in k.items()}


def reading_words(text):
    text = re.sub(r'<!--.*?-->', '', text, flags=re.S)
    text = '\n'.join(l for l in text.splitlines() if not l.startswith('#'))
    text = re.sub(r'\((f\.|in clear)[^)]*\)', ' ', text)
    text = re.sub(r'\{[^}]*\}', ' ', text)
    text = re.sub(r'\[(?![?l]|f\. ?\d)[^\]]*\s[^\]]*\]', ' ', text)
    text = re.sub(r'\*[^*]*\*', ' ', text)
    words = []
    for m in re.finditer(r'\S+', text):
        w = m.group(0)
        if re.fullmatch(r'\[(l\.|f\.)[^\]]*\]?|l\.|\d+\]|f\.', w):
            continue
        if re.fullmatch(r'\[[^\]?]*\][.,;:]?', w) and not re.search(r'[a-zà-ü]{2,}', w[1:-1].lower()):
            continue  # [44], […], [UNK], [cs]
        if '[' in w and re.fullmatch(r'\[(cs|UNK|me|tm|th)\][.,;:]?', w):
            continue
        n = norm(w.replace('[?', '').replace('[', '').replace(']', ''))
        if not n:
            continue
        words.append((w, n, '[' in w or ']' in w))
    return words


def align(r, toks, key):
    n, m = len(r), len(toks)
    G = -1.5
    NEG = -1e9
    opts = []
    for t in toks:
        v = key.get(t)
        if v is None:
            opts.append(('wild',))
        elif all(x in ('+', '') for x in v):
            opts.append(('free',))
        else:
            opts.append(tuple(x for x in v if x not in ('+', '')))
    S = [[NEG] * (m + 1) for _ in range(n + 1)]
    B = [[None] * (m + 1) for _ in range(n + 1)]
    S[0][0] = 0.0
    band = max(400, abs(n - m) + 400)

    def le(a, b):
        return 2 if a == b else (1.5 if any(a in g and b in g for g in NEAR) else None)

    for i in range(n + 1):
        lo = max(0, int(i * m / max(n, 1)) - band)
        hi = min(m, int(i * m / max(n, 1)) + band)
        Si = S[i]
        for j in range(lo, hi + 1):
            cur = Si[j]
            if cur <= NEG / 2:
                continue
            if i < n and cur + G > S[i + 1][j]:
                S[i + 1][j] = cur + G; B[i + 1][j] = (i, j, 'ins', None)
            if j < m:
                o = opts[j]
                if o[0] == 'free':
                    if cur > Si[j + 1]:
                        Si[j + 1] = cur; B[i][j + 1] = (i, j, 'skip', None)
                    continue
                if cur + G > Si[j + 1]:
                    Si[j + 1] = cur + G; B[i][j + 1] = (i, j, 'skip', None)
                if i < n:
                    if o[0] == 'wild':
                        if cur + 0.5 > S[i + 1][j + 1]:
                            S[i + 1][j + 1] = cur + 0.5; B[i + 1][j + 1] = (i, j, 'wild', None)
                        continue
                    sub = True
                    for v in o:
                        L = len(v)
                        if i + L > n:
                            continue
                        sc, cr = 0.0, []
                        for a, b in zip(v, r[i:i + L]):
                            x = le(a, b)
                            if x is None:
                                sc -= 1; cr.append(0)
                            else:
                                sc += x; cr.append(1)
                        if L == 1 and not cr[0]:
                            continue
                        if L > 1 and sum(cr) < L * 0.6:
                            continue
                        if cur + sc > S[i + L][j + 1]:
                            S[i + L][j + 1] = cur + sc; B[i + L][j + 1] = (i, j, 'm', cr)
                    if sub and cur - 1 > S[i + 1][j + 1]:
                        S[i + 1][j + 1] = cur - 1; B[i + 1][j + 1] = (i, j, 'sub', None)
    credit = [0.0] * n
    at = [None] * n
    i, j = n, m
    while i > 0 or j > 0:
        pi, pj, kind, cr = B[i][j]
        if kind == 'm':
            for k, c in enumerate(cr):
                credit[pi + k] = c; at[pi + k] = pj
        elif kind == 'wild':
            credit[pi] = 0.5; at[pi] = pj
        elif kind in ('sub',):
            at[pi] = pj
        i, j = pi, pj
    return credit, at


PAIR = {}


def check(doc, show=True):
    rf, (a, b), spec, kname = DOCS[doc]
    words = reading_words(section(T / 'texts' / rf, a, b))
    toks, lines = figures(spec)
    key = key_for(kname)
    r = ''.join(w[1] for w in words)
    credit, at = align(r, toks, key)
    pos, out = 0, []
    tot = 0
    alt = {}
    if doc in PAIR:
        _, cr2, _ = PAIR[doc]
    for k, (w, n, marked) in enumerate(words):
        c = credit[pos:pos + len(n)]
        if doc in PAIR:
            c2 = cr2[pos:pos + len(n)]
            c = c if sum(c) >= sum(c2) else c2
        frac = sum(c) / len(n)
        tot += sum(c)
        if frac < TH and not marked:
            js = [x for x in at[pos:pos + len(n)] if x is not None]
            if js:
                j0, j1 = max(0, min(js) - 4), min(len(toks), max(js) + 5)
            else:
                pj = next((at[q] for q in range(pos - 1, -1, -1) if at[q] is not None), 0)
                j0, j1 = max(0, pj - 2), min(len(toks), pj + 6)
            figs = ' '.join(f'{toks[q]}={"/".join(key.get(toks[q], ["?"]))}' for q in range(j0, j1))
            ctx = ' '.join(x[0] for x in words[max(0, k - 4):k + 5])
            out.append((w, round(frac, 2), f'l.{lines[j0] if toks else 0}', ctx, figs))
        pos += len(n)
    if show:
        print(f'== {doc}: {len(words)} words, {len(r)} letters, carried {tot / max(len(r), 1):.3f}, '
              f'{len(out)} listed')
        for w, f, ln, ctx, figs in out:
            print(f'  {w!r} {f} {ln} | {ctx}\n      {figs}')
    return out


def dump(doc, lns):
    rf, _, spec, kname = DOCS[doc]
    toks, lines = figures(spec)
    key = key_for(kname)
    for L in lns:
        print(f'l.{L}: ' + ' '.join(f'{t}={"/".join(key.get(t, ["?"]))}' for t, x in zip(toks, lines) if x == L))


if __name__ == '__main__':
    if len(sys.argv) > 2 and sys.argv[1] == 'dump':
        dump(sys.argv[2], [int(x) for x in sys.argv[3:]])
    else:
        ds = sys.argv[1:] or list(DOCS)
        if 'f196_201' in ds:
            rf, (a, b), spec, kname = DOCS['f201']
            words = reading_words(section(T / 'texts' / rf, a, b))
            toks, lines = figures(spec)
            PAIR['f196_201'] = (None, align(''.join(w[1] for w in words), toks, key_for(kname))[0], None)
        for d in ds:
            check(d)
