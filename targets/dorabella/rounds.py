"""Hypothesis rounds for the Dorabella loop; run with run_round.py <round> [...].
Results go to runs/ledger.tsv via hyp.py."""
import sys, random, itertools, re, math
import numpy as np
from hyp import *

ROUNDS = {}


def rnd(k):
    def deco(f):
        ROUNDS[k] = f
        return f
    return deco


# ------------------------------------------------------------------ round 1: fractionation
BACON = 'abcdefghiklmnopqrstuwxyz'           # 24-letter Bacon (i=j, u=v)
BITS = {'o//4': lambda s: s[0] // 4, 'o%2': lambda s: s[0] % 2, '(o//2)%2': lambda s: (s[0] // 2) % 2,
        'a==0': lambda s: int(s[1] == 0), 'a==2': lambda s: int(s[1] == 2), 'a%2': lambda s: s[1] % 2,
        'F/B axis': lambda s: int(s[0] % 4 == 1), 'C/G axis': lambda s: int(s[0] % 4 == 2)}


def bacon_family(signs):
    for nm, f in BITS.items():
        b = [f(s) for s in signs]
        for pol in (0, 1):
            for ph in range(5):
                out = ''
                for i in range(ph, len(b) - 4, 5):
                    v = int(''.join(str(x ^ pol) for x in b[i:i + 5]), 2)
                    out += BACON[v] if v < 24 else 'q'
                yield out, f'{nm} pol{pol} ph{ph}'


def bacon_encoder(text, rng):
    t = [c for c in text if c in BACON][:17]
    bits = ''.join(format(BACON.index(c), '05b') for c in t)
    s = [((rng.randrange(4) + 4 * int(b)), rng.randrange(3)) for b in bits]
    while len(s) < N:
        s.append((rng.randrange(8), rng.randrange(3)))
    return s


def ternary(ph):
    return lambda signs: [tuple(s[1] for s in signs[i:i + 3]) for i in range(ph, len(signs) - 2, 3)]


def ternary_encoder(text, rng):
    cells = rng.sample(list(itertools.product(range(3), repeat=3)), 26)
    s = []
    for ch in text[:29]:
        for d in cells[AZ.index(ch)]:
            s.append((rng.randrange(8), d))
    return s


def opairs(ph, unordered=False):
    def f(signs):
        out = []
        for i in range(ph, len(signs) - 1, 2):
            p = (signs[i][0], signs[i + 1][0])
            out.append(tuple(sorted(p)) if unordered else p)
        return out
    return f


def opair_encoder(unordered):
    def enc(text, rng):
        cells = rng.sample([(a, b) for a in range(8) for b in range(8) if (not unordered or a <= b)], 26)
        s = []
        for ch in text[:44]:
            a, b = cells[AZ.index(ch)]
            if unordered and rng.random() < .5:
                a, b = b, a
            s += [(a, rng.randrange(3)), (b, rng.randrange(3))]
        return s[:N]
    return enc


@rnd(1)
def round1():
    direct(1, 'Bacon biliteral (8 bit readings x 5 phases x 2)', bacon_family, bacon_encoder)
    for ph in range(3):
        solver(1, f'arcs as ternary triplets, phase {ph}', ternary(ph), ternary_encoder)
    for ph in range(2):
        solver(1, f'orientation pairs (64 values), phase {ph}', opairs(ph), opair_encoder(False))
        solver(1, f'semaphore-like unordered pairs, phase {ph}', opairs(ph, True), opair_encoder(True))




# ------------------------------------------------------------------ round 2: Morse
MORSE = {'a': '.-', 'b': '-...', 'c': '-.-.', 'd': '-..', 'e': '.', 'f': '..-.', 'g': '--.', 'h': '....', 'i': '..',
         'j': '.---', 'k': '-.-', 'l': '.-..', 'm': '--', 'n': '-.', 'o': '---', 'p': '.--.', 'q': '--.-', 'r': '.-.',
         's': '...', 't': '-', 'u': '..-', 'v': '...-', 'w': '.--', 'x': '-..-', 'y': '-.--', 'z': '--..'}
RMORSE = {v: k for k, v in MORSE.items()}
LP3 = None


def morse_dp(elems):
    """Best segmentation of an unsegmented dot/dash string into Morse letters under en-modern order 3."""
    global LP3
    if LP3 is None:
        m3 = lm.load('en-modern', order=3, spaces=False); LP3 = (m3, m3.lp.reshape(m3.A, m3.A, m3.A))
    m3, lp = LP3
    n = len(elems)
    # dp[pos] = {(a, b): (score, text)}; letters as model indices; start state uses 'e','e' context
    E = m3.index['e']
    dp = [dict() for _ in range(n + 1)]
    dp[0][(E, E)] = (0.0, '')
    for i in range(n):
        if not dp[i]:
            continue
        for L in range(1, 5):
            code = elems[i:i + L]
            if len(code) < L or code not in RMORSE:
                continue
            c = m3.index[RMORSE[code]]
            for (a, b), (s, t) in dp[i].items():
                ns = s + lp[a, b, c]
                if ns > dp[i + L].get((b, c), (-1e18,))[0]:
                    dp[i + L][(b, c)] = (ns, t + RMORSE[code])
        if len(dp[i]) > 60:                      # beam
            dp[i] = dict(sorted(dp[i].items(), key=lambda kv: -kv[1][0])[:60])
    for k in range(n, 0, -1):
        if dp[k]:
            return max(dp[k].values())[1]
    return ''


def morse_family(signs):
    for nm, f in BITS.items():
        for pol in (0, 1):
            elems = ''.join('-' if f(s) ^ pol else '.' for s in signs)
            yield morse_dp(elems), f'{nm} pol{pol}'


def morse_encoder(text, rng):
    elems = ''.join(MORSE[c] for c in text)[:N]
    return [((rng.randrange(4) + 4 * (e == '-')), rng.randrange(3)) for e in elems]


def morse_letter_family(signs):
    """sign = whole Morse letter: arcs+1 = length, orientation bits (under 16 dial labelings x 6 bit orders x 8
    polarities) = elements."""
    for start in range(8):
        for step in (1, -1):
            for perm in itertools.permutations(range(3)):
                for pol in range(8):
                    out = ''
                    for o, a in signs:
                        v = ((o - start) * step) % 8
                        bits = [((v >> perm[k]) & 1) ^ ((pol >> k) & 1) for k in range(3)]
                        code = ''.join('-' if b else '.' for b in bits[:a + 1])
                        out += RMORSE.get(code, 'q')
                    yield out, f'start{start} step{step} perm{perm} pol{pol}'


def morse_letter_encoder(text, rng):
    s = []
    for ch in text:
        code = MORSE.get(ch, '')
        if 1 <= len(code) <= 3:
            v = sum((c == '-') << k for k, c in enumerate(code)) | (rng.randrange(8) & ~((1 << len(code)) - 1))
            s.append((v % 8, len(code) - 1))
    return (s * 3)[:N]


@rnd(2)
def round2():
    direct(2, 'Morse: sign = dot/dash, unsegmented (16 bit readings)', morse_family, morse_encoder)
    direct(2, 'Morse: sign = letter, arcs = length (768 labelings)', morse_letter_family, morse_letter_encoder)


def morse_runlength_family(signs):
    for nm, f in BITS.items():
        if nm.startswith('a'):
            continue                                  # arcs carry the run length here
        for pol in (0, 1):
            elems = ''.join(('-' if f(s) ^ pol else '.') * (s[1] + 1) for s in signs)
            yield morse_dp(elems), f'{nm} pol{pol}'


def morse_runlength_encoder(text, rng):
    elems = ''.join(MORSE[c] for c in text)
    s, i = [], 0
    while i < len(elems) and len(s) < N:
        e = elems[i]; r = 1
        while r < 3 and i + r < len(elems) and elems[i + r] == e and rng.random() < .7:
            r += 1
        s.append((rng.randrange(4) + 4 * (e == '-'), r - 1)); i += r
    return s


@rnd(102)
def round2b():
    direct(2, 'Morse run-length: arcs = repeats, orientation bit = element', morse_runlength_family, morse_runlength_encoder)


# ------------------------------------------------------------------ round 3: context keywords
E24 = 'abcdefghiklmnopqrstuwxyz'                  # Elgar's notebook table order (I/J, U/V merged)
KEYWORDS = ['courage', 'dora', 'dorabella', 'penny', 'dorapenny', 'misspenny', 'elgar', 'edward', 'edwardelgar',
            'alice', 'carice', 'enigma', 'malvern', 'forli', 'wolverhampton', 'prudentia', 'caractacus',
            'luxchristi', 'boscobel', 'kites', 'kite', 'oak', 'variations', 'worcester', 'music', 'secret', 'cipher']


def k24(word):
    return [E24.index({'j': 'i', 'v': 'u'}.get(c, c)) for c in word]


def grids():
    for start in range(8):
        for step in (1, -1):
            for arcrev in (0, 1):
                yield (start, step, arcrev)


def to24(signs, g):
    start, step, arcrev = g
    return [((o - start) * step % 8) * 3 + (2 - a if arcrev else a) for o, a in signs]


def from24(vals, g, rng):
    start, step, arcrev = g
    out = []
    for v in vals:
        gg, c = divmod(v, 3)
        out.append(((gg * step + start) % 8, 2 - c if arcrev else c))
    return out


def keyed(vals, key, kind):
    out, ak = [], list(key)
    for i, c in enumerate(vals):
        k = ak[i] if kind.startswith('auto') else key[i % len(key)]
        if kind in ('vig', 'auto-vig'):
            p = (c - k) % 24
        elif kind in ('beau', 'auto-beau'):
            p = (k - c) % 24
        else:
            p = (c + k) % 24
        out.append(p)
        if kind.startswith('auto'):
            ak.append(p)
    return ''.join(E24[p] for p in out)


def keyword_family(kinds, keys):
    def fam(signs):
        for g in grids():
            vals = to24(signs, g)
            for w in keys:
                for kind in kinds:
                    yield keyed(vals, w, kind), f'{kind} key={w} grid={g}'
    return fam


def keyword_encoder(kinds, keys, numeric=False):
    def enc(text, rng):
        pt = [E24.index({'j': 'i', 'v': 'u'}.get(c, c)) for c in text]
        w = rng.choice(keys); kind = rng.choice(kinds); g = rng.choice(list(grids()))
        out, ak = [], list(w)
        for i, p in enumerate(pt):
            k = ak[i] if kind.startswith('auto') else w[i % len(w)]
            c = {'vig': (p + k), 'auto-vig': (p + k), 'beau': (k - p), 'auto-beau': (k - p), 'varbeau': (p - k)}[kind] % 24
            out.append(c)
            if kind.startswith('auto'):
                ak.append(p)
        return from24(out, g, rng)
    return enc


KW = [k24(w) for w in KEYWORDS]
NUMKEYS = [[int(d) for d in s] for s in ('14797', '1897', '18970714', '147', '97', '1407')]


@rnd(3)
def round3():
    direct(3, 'Vigenere/Beaufort/variant, 27 context keywords', keyword_family(['vig', 'beau', 'varbeau'], KW),
           keyword_encoder(['vig', 'beau', 'varbeau'], KW))
    direct(3, 'autokey Vigenere/Beaufort, 27 context primers', keyword_family(['auto-vig', 'auto-beau'], KW),
           keyword_encoder(['auto-vig', 'auto-beau'], KW))
    direct(3, 'Gronsfeld from the date 14.97 (6 digit keys)', keyword_family(['vig', 'beau', 'varbeau'], NUMKEYS),
           keyword_encoder(['vig', 'beau', 'varbeau'], NUMKEYS))


# ------------------------------------------------------------------ round 4: running keys from known texts
import os as _os, re as _re
DL = _os.environ.get('DORA_DL', '')
FREQ24 = None


def text24(raw):
    t = lm.norm(raw, 'modern', False).replace('j', 'i').replace('v', 'u')
    return np.array([E24.index(c) for c in t], dtype=np.int16)


def running_texts():
    out = {'gutenberg': text24(corpora.text(['en-gutenberg'])[:3_000_000])}
    for g, nm in (('10', 'KJV'), ('100', 'Shakespeare'), ('1304', 'verse')):
        f = _os.path.join(DL, f'pg{g}.txt')
        if _os.path.exists(f):
            out[nm] = text24(corpora.strip_gutenberg(open(f, encoding='utf-8', errors='replace').read()))
    mem = _os.path.join(HERE, 'src', 'memories1937', 'memories.txt')
    if _os.path.exists(mem):
        out['Powell1937'] = text24(open(mem, encoding='utf-8').read())
    return out


def running_best(signs, texts, grids_, top=300):
    global FREQ24
    if FREQ24 is None:
        c = np.bincount(texts['gutenberg'], minlength=24) + 1.0
        FREQ24 = np.log(c / c.sum())
    cand = []
    for g in grids_:
        c = np.array(to24(signs, g), dtype=np.int16)
        for nm, K in texts.items():
            L = len(K) - len(c)
            for kind in ('vig', 'beau', 'varbeau'):
                for s in range(0, L, 400000):
                    idx = np.arange(s, min(L, s + 400000))
                    win = K[idx[:, None] + np.arange(len(c))[None, :]]
                    P = {'vig': c - win, 'beau': win - c, 'varbeau': c + win}[kind] % 24
                    sc = FREQ24[P].sum(1)
                    k = min(top, len(sc) - 1)
                    for j in np.argpartition(-sc, k)[:k]:
                        cand.append((sc[j], g, nm, kind, int(idx[j]), P[j]))
    cand.sort(key=lambda r: -r[0])
    best = (-1e9, '', '')
    for _, g, nm, kind, off, P in cand[:top]:
        txt = ''.join(E24[p] for p in P)
        s = M4.per_char(txt)
        if s > best[0]:
            best = (s, txt, f'{kind} {nm}@{off} grid={g}')
    return best


@rnd(4)
def round4():
    texts = running_texts()
    print({k: len(v) for k, v in texts.items()}, flush=True)
    G = [(0, 1, 0), (0, -1, 0), (0, 1, 1), (0, -1, 1)]          # Elgar's table and its reflections
    D = running_best(SIGNS, texts, G)
    nulls = [running_best(s, texts, G)[0] for s in shuffles(3)]
    rng = random.Random(11); ctl = []
    for j in range(2):
        pt = text24(english(200, rng))[:N]
        nm = rng.choice(list(texts)); K = texts[nm]; off = rng.randrange(len(K) - N)
        g = rng.choice(G); kind = rng.choice(['vig', 'beau', 'varbeau'])
        c = {'vig': pt + K[off:off + N], 'beau': K[off:off + N] - pt, 'varbeau': pt - K[off:off + N]}[kind] % 24
        ctl.append(running_best(from24(c, g, rng), texts, G)[0])
    log(4, 'running key from KJV/Shakespeare/verse/prose/Powell', D[0], nulls, ctl, D[1], D[2])


# ------------------------------------------------------------------ round 5: order and direction of writing
def mirror(s):            # mirror across the vertical axis: right<->left
    return ((4 - s[0]) % 8, s[1])


def flip180(s):
    return ((s[0] + 4) % 8, s[1])


def line_tf(ops):
    """ops: per line, a function list applied to that line; returns transform over flat signs."""
    def f(signs):
        L = lines_of(signs)
        out = []
        for i, l in enumerate(L):
            for op in ops[i]:
                l = op(l)
            out += l
        return [tuple(x) for x in out]
    return f


REV = lambda l: l[::-1]
MIR = lambda l: [mirror(s) for s in l]
ROT = lambda l: [flip180(s) for s in l][::-1]
ID = lambda l: l


def reorder(order):
    def f(signs):
        L = lines_of(signs)
        return [tuple(x) for i in order for x in L[i]]
    return f


@rnd(5)
def round5():
    enc = mono_encoder()
    for order in itertools.permutations(range(3)):
        if order != (0, 1, 2) and order != (2, 1, 0):
            solver(5, f'line order {order}', reorder(order), enc)
    solver(5, 'line 2 right-to-left, mirrored (boustrophedon)', line_tf([[ID], [REV, MIR], [ID]]), enc)
    solver(5, 'lines 1 and 3 right-to-left, mirrored', line_tf([[REV, MIR], [ID], [REV, MIR]]), enc)
    solver(5, 'line 2 mirrored, left-to-right', line_tf([[ID], [MIR], [ID]]), enc)
    for k in range(3):
        ops = [[ID], [ID], [ID]]; ops[k] = [ROT]
        solver(5, f'line {k + 1} upside down', line_tf(ops), enc)


def inverse_reorder(order):
    inv = [order.index(i) for i in range(3)]
    def f(signs):                               # signs are in reading order; put lines back where Elgar wrote them
        lens = [len(LINES[i]) for i in order]
        chunks, i = [], 0
        for L in lens:
            chunks.append(signs[i:i + L]); i += L
        return [tuple(x) for k in inv for x in chunks[k]]
    return f


@rnd(105)
def round5b():
    solver(5, 'line order (0,2,1), 15 nulls, valid controls', reorder((0, 2, 1)),
           mono_encoder(inverse_reorder((0, 2, 1))), nn=15, nc=4)
    solver(5, 'line 2 upside down, 15 nulls, valid controls', line_tf([[ID], [ROT], [ID]]),
           mono_encoder(line_tf([[ID], [ROT], [ID]])), nn=15, nc=4)


# ------------------------------------------------------------------ round 6: per-line keys
from collections import Counter as _C


def ioc_t(x):
    c = _C(x); n = len(x)
    return sum(v * (v - 1) for v in c.values()) / (n * (n - 1))


def perline_shift(arcs_only=False):
    def f(signs):
        L = lines_of(signs)
        best = None
        rs = [0] if arcs_only else range(8)
        for r2, r3 in itertools.product(rs, rs):
            for s2, s3 in itertools.product(range(3), range(3)):
                sh = [(0, 0), (r2, s2), (r3, s3)]
                seq = [((o - sh[k][0]) % 8, (a - sh[k][1]) % 3) for k, l in enumerate(L) for o, a in l]
                v = ioc_t(seq)
                if best is None or v > best[0]:
                    best = (v, seq)
        return best[1]
    return f


def perline_encoder(arcs_only=False):
    def enc(text, rng):
        s = mono_encoder()(text, rng)
        sh = [(0, 0)] + [((0 if arcs_only else rng.randrange(8)), rng.randrange(3)) for _ in range(2)]
        out, i = [], 0
        for k, l in enumerate(LINES):
            for _ in l:
                o, a = s[i]; out.append(((o + sh[k][0]) % 8, (a + sh[k][1]) % 3)); i += 1
        return out
    return enc


def perline_trithemius(a):
    def f(signs):
        return [((o - a * i) % 8, s) for l in lines_of(signs) for i, (o, s) in enumerate(l)]
    return f


def trith_encoder(a):
    def enc(text, rng):
        s = mono_encoder()(text, rng); out, i = [], 0
        for l in LINES:
            for j in range(len(l)):
                o, c = s[i]; out.append(((o + a * j) % 8, c)); i += 1
        return out
    return enc


@rnd(6)
def round6():
    solver(6, 'per-line dial + arc shift (IoC-chosen)', perline_shift(), perline_encoder(), nn=6)
    solver(6, 'per-line arc shift only (IoC-chosen)', perline_shift(True), perline_encoder(True), nn=6)
    for a in (1, 2, 3, 4):
        solver(6, f'per-line progressive rotation a={a}', perline_trithemius(a), trith_encoder(a))


# ------------------------------------------------------------------ round 7: the plaintext's form
def model_variant(rnd_, name, tf, nn=4, nc=3, maxper=None):
    """Plaintext = tf(English words). Builds an order-4 model on tf(corpus), solves Dorabella, nulls, controls."""
    import re as re_
    words = re_.findall(r'[a-z]+', corpora.text(['en-gutenberg'])[:5_000_000].lower())
    text = tf(words)
    alpha = ''.join(sorted(set(text)))
    m = lm.DenseLM.build(text, 4, alpha)
    inj = maxper is None
    def run(tokens, seed):
        syms = sorted(set(tokens), key=str); ct = np.array([syms.index(t) for t in tokens])
        if maxper:
            from solve import anneal as an
            sc, key = an(ct, len(syms), m, restarts=8, iters=12000, seed=seed, injective=False, maxper=maxper)
        else:
            sc, key = anneal(ct, len(syms), m, restarts=8, iters=12000, seed=seed, injective=len(syms) <= m.A)
        return sc / len(ct), ''.join(m.alpha[i] for i in key[ct])
    D, txt = run(SIGNS, 0)
    nulls = [run(s, 100 + j)[0] for j, s in enumerate(shuffles(nn))]
    rng = random.Random(5); ctl, acc = [], []
    for j in range(nc):
        p = rng.randrange(len(text) - N); pt = text[p:p + N]
        cells = rng.sample([(o, a) for o in range(8) for a in range(3)], 24)
        key = {c: cells[i % 24] for i, c in enumerate(sorted(set(pt)))}
        sc, t2 = run([key[c] for c in pt], 200 + j)
        ctl.append(sc); acc.append(np.mean([a == b for a, b in zip(t2, pt)]))
    return log(rnd_, name, D, nulls, ctl, txt, f'ctl acc {min(acc):.2f}..{max(acc):.2f}', acc)


@rnd(7)
def round7():
    model_variant(7, 'consonant skeleton (no vowels)', lambda ws: ''.join(re.sub('[aeiou]', '', w) for w in ws))
    model_variant(7, 'back-slang: each word reversed', lambda ws: ''.join(w[::-1] for w in ws))
    model_variant(7, 'abbreviated: first 3 letters of each word', lambda ws: ''.join(w[:3] for w in ws))
    model_variant(7, 'homophonic, up to 3 signs per letter', lambda ws: ''.join(ws), maxper=3)


# ------------------------------------------------------------------ round 8: transposition (key-free screen)
def rep_bigrams(seq):
    c = _C(zip(seq, seq[1:]))
    return sum(v - 1 for v in c.values() if v > 1)


def columnar_reads(n):
    """Inverse columnar transpositions: text written in rows of width w, read column by column in order perm.
    Yields (index list, label); the inverse (undoing the transposition) is what we apply to the ciphertext."""
    for w in range(2, 8):
        rows = (n + w - 1) // w
        for perm in itertools.permutations(range(w)):
            # ciphertext = columns in perm order; recover row order
            cols, pos = [], 0
            lens = [len(range(c, n, w)) for c in range(w)]
            order = [None] * n
            for c in perm:
                for r in range(lens[c]):
                    order[r * w + c] = pos; pos += 1
            yield order, f'columnar w={w} perm={perm}'


def other_reads(n):
    for k in range(2, 7):
        period = 2 * (k - 1)
        pat = [(i % period) if (i % period) < k else period - (i % period) for i in range(n)]
        srt = sorted(range(n), key=lambda i: (pat[i], i))
        order = [None] * n
        for j, i in enumerate(srt):
            order[i] = j
        yield order, f'rail fence {k}'
    for w in range(2, 30):                       # snake columns
        order = []
        for c in range(w):
            col = list(range(c, n, w))
            order += col if c % 2 == 0 else col[::-1]
        yield order, f'snake columns w={w}'


def transposition_screen(signs, top=8):
    cands = []
    for order, lab in itertools.chain(columnar_reads(len(signs)), other_reads(len(signs))):
        seq = [signs[i] for i in order]
        cands.append((rep_bigrams(seq), lab, seq))
    cands.sort(key=lambda r: -r[0])
    return cands[:top]


@rnd(8)
def round8():
    base = rep_bigrams(SIGNS)
    top = transposition_screen(SIGNS)
    nul = [transposition_screen(s, 1)[0][0] for s in shuffles(8)]
    print(f'repeated-pair excess: written order {base}; best transposition {top[0][0]} ({top[0][1]}); '
          f'best over shuffles {min(nul)}..{max(nul)}', flush=True)
    for score, lab, seq in top[:3]:
        D, txt, _, _ = solve_tokens(seq, R=10)
        nulls = [solve_tokens([s[i] for i in range(N)], R=10, seed=50 + j)[0] for j, s in enumerate(shuffles(3))]
        log(8, f'{lab} (pairs {score})', D, nulls, [], txt)


# ------------------------------------------------------------------ round 9: other languages
def lang_variant(rnd_, model_id, nn=4, nc=3):
    spec = lm.registry()[0][model_id]
    m = lm.load(model_id, order=4, spaces=False)
    text = lm.norm(corpora.text(spec['sources'])[:3_000_000], spec['norm'], False)
    def run(tokens, seed):
        syms = sorted(set(tokens), key=str); ct = np.array([syms.index(t) for t in tokens])
        sc, key = anneal(ct, len(syms), m, restarts=10, iters=12000, seed=seed, injective=len(syms) <= m.A)
        return sc / len(ct), ''.join(m.alpha[i] for i in key[ct])
    D, txt = run(SIGNS, 0)
    nulls = [run(s, 100 + j)[0] for j, s in enumerate(shuffles(nn))]
    rng = random.Random(5); ctl, acc = [], []
    for j in range(nc):
        p = rng.randrange(len(text) - N); pt = text[p:p + N]
        cells = rng.sample([(o, a) for o in range(8) for a in range(3)], 24)
        key = {c: cells[i % 24] for i, c in enumerate(sorted(set(pt)))}
        sc, t2 = run([key[c] for c in pt], 200 + j)
        ctl.append(sc); acc.append(np.mean([a == b for a, b in zip(t2, pt)]))
    return log(rnd_, f'language {model_id}', D, nulls, ctl, txt, f'ctl acc {min(acc):.2f}..{max(acc):.2f}', acc)


@rnd(9)
def round9():
    for mid in ('nl-modern', 'pt-modern', 'da-modern', 'sv-modern', 'cy-modern', 'pl-modern', 'hu-modern'):
        lang_variant(9, mid)


# ------------------------------------------------------------------ round 10: fixed-position cribs
OPEN = ['dearmisspenny', 'mydeardora', 'deardora', 'dearestdora', 'missdora', 'misspenny', 'dorabella',
        'mydeardorabella', 'deardorabella', 'mydearmisspenny', 'dearmissdora', 'dora', 'mydearest', 'dear']
CLOSE = ['ee', 'yoursee', 'edwardelgar', 'yourseveree', 'yourssincerelyee', 'elgar', 'eelgar', 'yoursever', 'ede']


def crib_fit(signs, crib, start):
    s2l, l2s = {}, {}
    for t, ch in zip(signs[start:start + len(crib)], crib):
        if s2l.setdefault(t, ch) != ch or l2s.setdefault(ch, t) != t:
            return None
    return s2l


def anneal_fixed_signs(signs, fixed, seed, R=6, iters=8000):
    m = M4; rng = random.Random(seed)
    syms = sorted(set(signs)); ct = np.array([syms.index(t) for t in signs])
    fx = {syms.index(t): m.index[c] for t, c in fixed.items()}
    free = [s for s in range(len(syms)) if s not in fx]; used = set(fx.values())
    pool = [a for a in range(m.A) if a not in used]
    best = (-1e18, '')
    for r in range(R):
        key = np.zeros(len(syms), dtype=np.int64)
        for s, a in fx.items():
            key[s] = a
        for s, a in zip(free, rng.sample(pool, len(free))):
            key[s] = a
        cur = m.score_idx(key[ct])
        for i in range(iters):
            T = 2.0 * (1 - i / iters) + 0.05
            k2 = key.copy(); s = rng.choice(free)
            if rng.random() < 0.5:
                t = rng.choice(free); k2[s], k2[t] = k2[t], k2[s]
            else:
                inuse = set(k2[free].tolist()) | used
                opts = [a for a in range(m.A) if a not in inuse]
                if not opts:
                    continue
                k2[s] = rng.choice(opts)
            sc = m.score_idx(k2[ct])
            if sc >= cur or rng.random() < math.exp((sc - cur) / T):
                key, cur = k2, sc
        if cur > best[0]:
            best = (cur, ''.join(m.alpha[i] for i in key[ct]))
    return best[0] / len(ct), best[1]


def crib_round(signs, which, seed=0):
    best = (-1e9, '', '')
    if which in ('open', 'both'):
        opens = [(c, 0) for c in OPEN]
    if which == 'close':
        tries = [((c, len(signs) - len(c)),) for c in CLOSE]
    elif which == 'open':
        tries = [(o,) for o in opens]
    else:
        tries = [(o, (c, len(signs) - len(c))) for o in opens for c in CLOSE]
    for t in tries:
        fixed = {}
        ok = True
        for crib, st in t:
            f = crib_fit(signs, crib, st)
            if f is None:
                ok = False; break
            for k, v in f.items():
                if fixed.setdefault(k, v) != v:
                    ok = False
            if len(set(fixed.values())) != len(fixed):
                ok = False
        if not ok:
            continue
        sc, txt = anneal_fixed_signs(signs, fixed, seed)
        if sc > best[0]:
            best = (sc, txt, '+'.join(c for c, _ in t))
    return best


@rnd(10)
def round10():
    for which in ('open', 'close', 'both'):
        D = crib_round(SIGNS, which)
        if D[0] < -1e8:                               # no placement passes crib_fit: an exclusion, not a score
            print(f'[R10] fixed cribs: {which}: excluded, no crib fits Dorabella at that position', flush=True)
            with open(LEDGER, 'a', encoding='utf-8') as f:
                f.write(chr(9).join(['10', f'fixed cribs: {which}', '-', '-', '-', 'excluded', 'no crib fits at that position', '']) + chr(10))
            continue
        nulls = [crib_round(s, which, 100 + j)[0] for j, s in enumerate(shuffles(5))]
        nulls = [x for x in nulls if x > -1e8] or [-9.0]
        log(10, f'fixed cribs: {which}', D[0], nulls, [], D[1], D[2])


# ------------------------------------------------------------------ round 11: source-type diagnostics
def inv_stats(seq):
    c = _C(seq); n = len(seq)
    big = _C(zip(seq, seq[1:]))
    return np.array([len(c), sum(v * (v - 1) for v in c.values()) / (n * (n - 1)),
                     sum(v - 1 for v in big.values() if v > 1), sum(a == b for a, b in zip(seq, seq[1:])),
                     sum(1 for v in c.values() if v == 1)])


def source_windows(name, k=3000, rng=None):
    rng = rng or random.Random(0)
    if name.startswith('lang:'):
        mid = name[5:]; spec = lm.registry()[0][mid]
        t = lm.norm(corpora.text(spec['sources'])[:2_000_000], spec['norm'], False)
        return [t[p:p + N] for p in (rng.randrange(len(t) - N) for _ in range(k))]
    if name == 'initials':
        w = re.findall(r'[a-z]+', corpora.text(['en-gutenberg'])[:3_000_000].lower())
        t = ''.join(x[0] for x in w)
        return [t[p:p + N] for p in (rng.randrange(len(t) - N) for _ in range(k))]
    if name == 'elgar':
        t = lm.norm(open(_os.path.join(HERE, 'src', 'elgar_register.txt'), encoding='utf-8').read(), 'modern', False)
        return [t[p:p + N] for p in (rng.randrange(len(t) - N) for _ in range(k))]
    if name == 'music':
        import json, glob
        seqs = []
        for f in glob.glob(_os.path.join(HERE, 'src', 'music', '*.json')):
            seqs.append([tuple(x[:2]) for x in json.load(open(f)) if x[0] is not None])
        allm = [x for s in seqs for x in s]
        return [allm[p:p + N] for p in (rng.randrange(len(allm) - N) for _ in range(k))]
    if name == 'phonemes':
        import glob
        cmu = {}
        dl = DL
        for line in open(_os.path.join(dl, 'cmudict.dict'), encoding='utf-8', errors='replace'):
            w, *ph = line.split('#')[0].split()
            if '(' not in w and w not in cmu:
                cmu[w] = [re.sub(r'\d', '', p) for p in ph]
        words = re.findall(r"[a-z']+", corpora.text(['en-gutenberg'])[:2_000_000].lower())
        t = [p for w in words if w in cmu for p in cmu[w]]
        return [t[p:p + N] for p in (rng.randrange(len(t) - N) for _ in range(k))]


@rnd(11)
def round11():
    D = inv_stats(SIGNS)
    names = ['lang:en-modern', 'lang:la', 'lang:de-modern', 'lang:fr-modern', 'elgar', 'initials', 'phonemes', 'music']
    print('statistics: distinct, IoC, repeated-pair excess, doubles, singletons')
    print(f'{"DORABELLA":16s}', np.round(D, 3))
    res = []
    for nm in names:
        try:
            W = np.array([inv_stats(list(w)) for w in source_windows(nm)])
        except Exception as e:
            print(nm, 'skipped:', e); continue
        mu, sd = W.mean(0), W.std(0) + 1e-9
        z = (D - mu) / sd
        # empirical joint tail: share of windows at least as close to their own mean as Dorabella is, in z-distance
        dz = np.sqrt((((W - mu) / sd) ** 2).sum(1)); dd = np.sqrt((z ** 2).sum())
        p = np.mean(dz >= dd)
        res.append((p, nm))
        print(f'{nm:16s} mean {np.round(mu, 3)}  z {np.round(z, 2)}  P(as typical) {p:.3f}', flush=True)
    res.sort(reverse=True)
    log(11, 'source type by key-invariant statistics', res[0][0], [r[0] for r in res[1:]] or [0], [],
        ' > '.join(f'{n}:{p:.3f}' for p, n in res))


# ------------------------------------------------------------------ round 12: Playfair, word-space sign, regular nulls
def playfair_possible(signs):
    """Playfair never gives a cipher digraph of two identical letters. Check every pairing: across the text
    (phase 0/1) and within each line (phase 0/1)."""
    res = {}
    for ph in (0, 1):
        res[f'text phase {ph}'] = not any(signs[i] == signs[i + 1] for i in range(ph, len(signs) - 1, 2))
        ok = True
        for l in lines_of(signs):
            if any(l[i] == l[i + 1] for i in range(ph, len(l) - 1, 2)):
                ok = False
        res[f'per-line phase {ph}'] = ok
    return res


def space_sign_solve(signs, sp, seed=0):
    m = lm.load('en-modern', order=4, spaces=True)
    toks = [s for s in signs]
    syms = sorted(set(t for t in toks if t != sp))
    rng = random.Random(seed); SP = m.index[' ']
    LET = [i for i in range(m.A) if i != SP]
    ct = np.array([syms.index(t) if t != sp else -1 for t in toks])
    best = (-1e18, '')
    for r in range(8):
        key = np.array(rng.sample(LET, len(syms)) + [SP])
        def txt(k):
            return k[ct]                                     # index -1 picks the trailing SP
        cur = m.score_idx(txt(key))
        for i in range(12000):
            T = 3.0 * (1 - i / 12000) + 0.05
            k2 = key.copy(); s = rng.randrange(len(syms))
            if rng.random() < 0.3:
                free = [a for a in LET if a not in set(k2[:-1].tolist())]; k2[s] = rng.choice(free)
            else:
                t = rng.randrange(len(syms)); k2[s], k2[t] = k2[t], k2[s]
            sc = m.score_idx(txt(k2))
            if sc >= cur or rng.random() < math.exp((sc - cur) / T):
                key, cur = k2, sc
        if cur > best[0]:
            best = (cur / len(ct), ''.join(m.alpha[i] for i in txt(key)))
    return best


@rnd(12)
def round12():
    pf = playfair_possible(SIGNS)
    print('Playfair possible under pairing:', pf, flush=True)
    log(12, 'Playfair on the 3x8 / 8x3 sign grid', 0.0 if any(pf.values()) else -9.0, [0.0], [],
        'excluded: identical signs fall inside a digraph under every pairing' if not any(pf.values()) else str(pf))
    top = [s for s, _ in _C(SIGNS).most_common(8)]
    for sp in top:
        words = ''.join('|' if s == sp else 'x' for s in SIGNS).split('|')
        L = [len(w) for w in words if w]
        D = space_sign_solve(SIGNS, sp)
        nulls = [space_sign_solve(s, sp, 100 + j)[0] for j, s in enumerate(shuffles(3))]
        log(12, f'sign {TOK[sp[0] * 3 + sp[1]]} = word space ({len(L)} words, mean {np.mean(L):.1f})', D[0], nulls, [], D[1])
    for k in range(2, 7):
        for ph in range(k):
            tf = (lambda k, ph: lambda s: [x for i, x in enumerate(s) if i % k != ph])(k, ph)
            solver(12, f'drop every {k}th sign, phase {ph}', tf, None, nn=3)


# ------------------------------------------------------------------ round 13: musical letter alphabets
def notes_family(signs):
    o = np.array([s[0] for s in signs])
    for perm in itertools.permutations('abcdefgh'):
        yield ''.join(perm[x] for x in o), ''.join(perm)


def ah_words_encoder(text, rng):
    w = [x for x in re.findall(r'[a-z]+', corpora.text(['en-gutenberg'])[:2_000_000].lower())
         if len(x) > 1 and set(x) <= set('abcdefgh')]
    s = ''
    while len(s) < N:
        s += rng.choice(w)
    perm = rng.sample(range(8), 8)
    return [(perm['abcdefgh'.index(c)], rng.randrange(3)) for c in s[:N]]


def keyboard_family(signs):
    o = np.array([s[0] for s in signs]); a = np.array([s[1] for s in signs])
    rows = np.array([list(E24[r * 8:(r + 1) * 8]) for r in range(3)])
    for rperm in itertools.permutations(range(3)):
        for cperm in itertools.permutations(range(8)):
            cp = np.array(cperm)
            yield ''.join(rows[np.array(rperm)[a], cp[o]]), f'rows{rperm} cols{cperm}'


def keyboard_encoder(text, rng):
    rperm = rng.sample(range(3), 3); cperm = rng.sample(range(8), 8)
    out = []
    for ch in text:
        v = E24.index({'j': 'i', 'v': 'u'}.get(ch, ch)); r, c = divmod(v, 8)
        out.append((cperm.index(c), rperm.index(r)))
    return out


@rnd(13)
def round13():
    direct(13, 'orientation = note name a-h (40,320 assignments)', notes_family, ah_words_encoder, nn=3, nc=2)
    direct(13, 'keyboard: 3 rows of 8, any column/row order (241,920)', keyboard_family, keyboard_encoder, nn=2, nc=2)


# ------------------------------------------------------------------ round 14: misaligned orientation / arc streams
def arcs_shift(k):
    return lambda s: [(s[i][0], s[(i + k) % len(s)][1]) for i in range(len(s))]


def arcs_rev(s):
    return [(s[i][0], s[len(s) - 1 - i][1]) for i in range(len(s))]


def orient_rev(s):
    return [(s[len(s) - 1 - i][0], s[i][1]) for i in range(len(s))]


def arcs_rev_lines(s):
    out = []
    for l in lines_of(s):
        out += [(l[i][0], l[len(l) - 1 - i][1]) for i in range(len(l))]
    return out


@rnd(14)
def round14():
    for k in (1, -1, 2, -2, 3, -3):
        solver(14, f'arcs stream shifted by {k:+d}', arcs_shift(k), mono_encoder(arcs_shift(-k)))
    solver(14, 'arcs stream reversed', arcs_rev, mono_encoder(arcs_rev))
    solver(14, 'orientation stream reversed', orient_rev, mono_encoder(orient_rev))
    solver(14, 'arcs stream reversed within each line', arcs_rev_lines, mono_encoder(arcs_rev_lines))


# ------------------------------------------------------------------ round 15: polygraphic units
def unit_inventory(kind):
    t = corpora.text(['en-gutenberg'])[:3_000_000].lower()
    letters = list(AZ)
    s = lm.norm(t, 'modern', False)
    bigr = [b for b, _ in _C(s[i:i + 2] for i in range(len(s) - 1)).most_common(60)]
    words = ['the', 'and', 'of', 'to', 'you', 'in', 'i', 'my', 'a', 'is', 'it', 'that', 'be', 'for', 'with', 'will']
    if kind == 'mixed':
        return letters + bigr[:30] + [w for w in words if len(w) > 1][:10]
    if kind == 'digraphs':
        return bigr
    if kind == 'nomenclator':
        return letters + ['the', 'and', 'you', 'to', 'of', 'in']


def unit_solve(tokens, units, seed, R=6, iters=8000):
    rng = random.Random(seed)
    syms = sorted(set(tokens), key=str); ct = [syms.index(t) for t in tokens]
    U = len(units)
    best = (-1e18, '')
    def score(key):
        s = ''.join(units[key[c]] for c in ct)
        return M4.score(s) / len(ct), s                         # per sign: units of any length compete fairly
    for r in range(R):
        key = rng.sample(range(U), len(syms)); cur, _ = score(key)
        for i in range(iters):
            T = 2.0 * (1 - i / iters) + 0.02
            k2 = list(key); s = rng.randrange(len(syms))
            if rng.random() < 0.5:
                t = rng.randrange(len(syms)); k2[s], k2[t] = k2[t], k2[s]
            else:
                free = [u for u in range(U) if u not in set(k2)]; k2[s] = rng.choice(free)
            sc, _ = score(k2)
            if sc >= cur or rng.random() < math.exp((sc - cur) / T):
                key, cur = k2, sc
        if cur > best[0]:
            best = (cur, score(key)[1])
    return best


def unit_encoder(units):
    def enc(text, rng):
        out, i = [], 0
        cells = rng.sample([(o, a) for o in range(8) for a in range(3)], 24)
        chosen = {}
        while len(out) < N and i < len(text):
            for L in (3, 2, 1):
                u = text[i:i + L]
                if u in units and (u in chosen or len(chosen) < 24):
                    if u not in chosen:
                        chosen[u] = cells[len(chosen)]
                    out.append(chosen[u]); i += L; break
            else:
                i += 1
        return out
    return enc


@rnd(15)
def round15():
    for kind in ('mixed', 'digraphs', 'nomenclator'):
        U = unit_inventory(kind)
        D = unit_solve(SIGNS, U, 0)
        nulls = [unit_solve(s, U, 100 + j)[0] for j, s in enumerate(shuffles(3))]
        rng = random.Random(9); enc = unit_encoder(U)
        ctl = [unit_solve(enc(english(250, rng), rng), U, 200 + j)[0] for j in range(2)]
        log(15, f'polygraphic units: {kind} ({len(U)} units)', D[0], nulls, ctl, D[1])


# ------------------------------------------------------------------ round 16: the key changes partway
def tagged(fn):
    """fn(i, line_index) -> stream id; tokens become (stream, sign) so each stream gets its own key."""
    def f(signs):
        out, i = [], 0
        for li, l in enumerate(lines_of(signs)):
            for s in l:
                out.append((fn(i, li), s)); i += 1
        return out
    return f


def tagged_encoder(fn):
    def enc(text, rng):
        keys = {}
        out, i = [], 0
        for li, l in enumerate(LINES):
            for _ in l:
                sid = fn(i, li)
                if sid not in keys:
                    cells = rng.sample([(o, a) for o in range(8) for a in range(3)], 24)
                    keys[sid] = {c: cells[k % 24] for k, c in enumerate(AZ)}
                out.append(keys[sid][text[i]]); i += 1
        return out
    return enc


@rnd(16)
def round16():
    for nm, fn in (('two interleaved messages (odd/even)', lambda i, li: i % 2),
                   ('new key from line 2', lambda i, li: int(li > 0)),
                   ('new key at the halfway point', lambda i, li: int(i >= N // 2)),
                   ('separate key per line', lambda i, li: li)):
        solver(16, nm, tagged(fn), tagged_encoder(fn), injective=False)


# ------------------------------------------------------------------ round 17: Sukhotin vowels and the flips
def sukhotin(seq):
    syms = sorted(set(seq), key=str); idx = {s: i for i, s in enumerate(syms)}
    n = len(syms); Mx = np.zeros((n, n))
    for a, b in zip(seq, seq[1:]):
        if a != b:
            Mx[idx[a], idx[b]] += 1; Mx[idx[b], idx[a]] += 1
    sums = Mx.sum(1).copy(); vowels = set()
    while True:
        cand = [i for i in range(n) if i not in vowels]
        if not cand:
            break
        i = max(cand, key=lambda k: sums[k])
        if sums[i] <= 0:
            break
        vowels.add(i)
        for k in range(n):
            if k not in vowels:
                sums[k] -= 2 * Mx[k, i]
    return {syms[i] for i in vowels}


def vc_stats(seq):
    V = sukhotin(seq)
    b = [s in V for s in seq]
    alt = np.mean([x != y for x, y in zip(b, b[1:])])
    runs, r = [], 1
    for x, y in zip(b, b[1:]):
        if x == y:
            r += 1
        else:
            runs.append(r); r = 1
    runs.append(r)
    return V, alt, np.mean(b), max(runs)


@rnd(17)
def round17():
    V, alt, share, mrun = vc_stats(SIGNS)
    print('Sukhotin vowel signs:', sorted(TOK[o * 3 + a] for o, a in V), f'share {share:.2f}, alternation {alt:.3f}, longest run {mrun}')
    rng = random.Random(1)
    E = [vc_stats(list(english(N, rng))) for _ in range(500)]
    eng_v = [sorted(e[0]) for e in E[:3]]
    S = [vc_stats(s) for s in shuffles(300)]
    ea = np.array([e[1] for e in E]); sa = np.array([s[1] for s in S])
    print(f'alternation: Dorabella {alt:.3f}; English {ea.mean():.3f} (P(<=D) {np.mean(ea <= alt):.3f}); shuffles {sa.mean():.3f} (P(>=D) {np.mean(sa >= alt):.3f})')
    print('English Sukhotin vowels (3 samples):', eng_v)
    log(17, 'Sukhotin V/C alternation like English', alt, list(sa), list(ea), ' '.join(sorted(TOK[o * 3 + a] for o, a in V)))
    vo = _C(o for o, a in V); allo = _C(o for o, a in set(SIGNS))
    print('vowel signs by orientation:', {'ABCDEFGH'[k]: f'{vo.get(k, 0)}/{allo[k]}' for k in range(8)})
    flips = [(i, SIGNS[i - 1], SIGNS[i]) for i in range(1, N) if (SIGNS[i][0] - SIGNS[i - 1][0]) % 8 == 4]
    vcsw = np.mean([(a in V) != (b in V) for _, a, b in flips])
    nonfl = [(SIGNS[i - 1], SIGNS[i]) for i in range(1, N) if (SIGNS[i][0] - SIGNS[i - 1][0]) % 8 != 4]
    vcsw_n = np.mean([(a in V) != (b in V) for a, b in nonfl])
    print(f'V/C switch at opposite flips {vcsw:.2f} vs at other steps {vcsw_n:.2f}')
    log(17, 'opposite flips coincide with V/C switches', vcsw, [vcsw_n], [], f'flip switch {vcsw:.2f} vs other {vcsw_n:.2f}')


# ------------------------------------------------------------------ round 18: known quotation; Elgar table + transposition
from numpy.lib.stride_tricks import sliding_window_view as _swv
from scipy.optimize import linear_sum_assignment as _lsa


def letter_texts():
    out = {}
    for g, nm in (('10', 'KJV'), ('100', 'Shakespeare'), ('1304', 'verse')):
        f = _os.path.join(DL, f'pg{g}.txt')
        if _os.path.exists(f):
            out[nm] = lm.norm(corpora.strip_gutenberg(open(f, encoding='utf-8', errors='replace').read()), 'modern', False)
    out['gutenberg'] = lm.norm(corpora.text(['en-gutenberg'])[:4_000_000], 'modern', False)
    for nm, f in (('Elgar letters', _os.path.join(HERE, 'src', 'elgar_register.txt')),
                  ('Powell 1937', _os.path.join(HERE, 'src', 'memories1937', 'memories.txt'))):
        if _os.path.exists(f):
            out[nm] = lm.norm(open(f, encoding='utf-8').read(), 'modern', False)
    return {k: np.frombuffer(v.encode(), dtype=np.uint8) - 97 for k, v in out.items()}


def quote_search(seq, texts, top=200):
    syms = sorted(set(seq)); ct = [syms.index(s) for s in seq]
    pairs = [(i, j) for i in range(N) for j in range(i + 1, N) if ct[i] == ct[j]]
    I = np.array([p[0] for p in pairs]); J = np.array([p[1] for p in pairs])
    best = []
    for nm, v in texts.items():
        W = _swv(v, N)
        for s in range(0, len(W), 250000):
            Wc = W[s:s + 250000]
            sc = (Wc[:, I] == Wc[:, J]).sum(1)
            k = min(top, len(sc) - 1)
            for i in np.argpartition(-sc, k)[:k]:
                best.append((int(sc[i]), nm, s + int(i)))
    best.sort(reverse=True)
    res = []
    for scr, nm, st in best[:top]:
        w = texts[nm][st:st + N]
        Mx = np.zeros((len(syms), 26))
        for a, b in zip(ct, w):
            Mx[a, b] += 1
        r_, c_ = _lsa(-Mx)
        res.append((int(Mx[r_, c_].sum()), nm, st, ''.join(chr(97 + x) for x in w)))
    res.sort(reverse=True)
    return res[0]


@rnd(18)
def round18():
    texts = letter_texts()
    print({k: len(v) for k, v in texts.items()}, flush=True)
    D = quote_search(SIGNS, texts)
    nulls = [quote_search(s, texts)[0] for s in shuffles(3)]
    # control: a real window of KJV enciphered, with 6 misreads
    rng = random.Random(4); ctl = []
    for j in range(2):
        nm = rng.choice(list(texts)); st = rng.randrange(len(texts[nm]) - N); w = texts[nm][st:st + N]
        cells = rng.sample([(o, a) for o in range(8) for a in range(3)], 24)
        sg = [cells[x % 24] for x in w]
        for q in rng.sample(range(N), 6):
            sg[q] = (rng.randrange(8), rng.randrange(3))
        ctl.append(quote_search(sg, texts)[0])
    log(18, 'known quotation, letter by letter (6 texts, misread-tolerant)', D[0], nulls, ctl,
        D[3], f'{D[1]}@{D[2]} explains {D[0]}/87')
    # 18.2 Elgar's table, letters right but scrambled: letter-frequency fit
    c = np.bincount(texts['gutenberg'], minlength=26) + 1.0
    LF = np.log(c / c.sum())
    def freq_ll(txt):
        return np.mean([LF[ord(ch) - 97] for ch in txt])
    best = (-1e9, '')
    for g in grids():
        vals = to24(SIGNS, g)
        for sh in range(24):
            t = ''.join(E24[(v + sh) % 24] for v in vals)
            f = freq_ll(t)
            if f > best[0]:
                best = (f, t, f'grid={g} shift={sh}')
    eng = [freq_ll(english(N, rng)) for _ in range(300)]
    rnd_tables = []
    for _ in range(300):
        perm = rng.sample(range(24), 24)
        rnd_tables.append(freq_ll(''.join(E24[perm[v]] for v in to24(SIGNS, (0, 1, 0)))))
    log(18, "Elgar's table (832 variants) + transposition: letter frequencies", best[0], rnd_tables, eng, best[1], best[2])


# ------------------------------------------------------------------ round 19: keyword-mixed alphabets; block-wise rearrangement
def mixed_alphabet(word, cont):
    w = []
    for ch in word:
        ch = {'j': 'i', 'v': 'u'}.get(ch, ch)
        if ch not in w:
            w.append(ch)
    rest = [c for c in E24 if c not in w]
    if cont:                                      # continue the alphabet from the keyword's last letter
        k = E24.index(w[-1])
        rest = [E24[(k + i) % 24] for i in range(1, 25) if E24[(k + i) % 24] not in w]
    return ''.join(w + rest)


def mixed_family(signs):
    for word in KEYWORDS:
        for cont in (0, 1):
            alpha = mixed_alphabet(word, cont)
            for g in grids():
                vals = to24(signs, g)
                for sh in range(24):
                    yield ''.join(alpha[(v + sh) % 24] for v in vals), f'{word} cont={cont} grid={g} shift={sh}'


def mixed_encoder(text, rng):
    alpha = mixed_alphabet(rng.choice(KEYWORDS), rng.randrange(2)); g = rng.choice(list(grids())); sh = rng.randrange(24)
    vals = [(alpha.index({'j': 'i', 'v': 'u'}.get(c, c)) - sh) % 24 for c in text]
    return from24(vals, g, rng)


def block_tf(p, mode):
    def f(signs):
        out = []
        for b in range(0, len(signs), p):
            blk = signs[b:b + p]
            arcs = [s[1] for s in blk]
            arcs = arcs[1:] + arcs[:1] if mode == 'rot' else arcs[::-1]
            out += [(s[0], a) for s, a in zip(blk, arcs)]
        return out
    return f


def block_inv(p, mode):
    def f(signs):
        out = []
        for b in range(0, len(signs), p):
            blk = signs[b:b + p]
            arcs = [s[1] for s in blk]
            arcs = arcs[-1:] + arcs[:-1] if mode == 'rot' else arcs[::-1]
            out += [(s[0], a) for s, a in zip(blk, arcs)]
        return out
    return f


@rnd(19)
def round19():
    direct(19, 'keyword-mixed alphabets on Elgar table (41,472)', mixed_family, mixed_encoder, nn=4, nc=2)
    for p in range(2, 7):
        for mode in ('rot', 'rev'):
            if p == 2 and mode == 'rev':
                continue
            solver(19, f'block {p}: arcs {"rotated" if mode == "rot" else "reversed"} within block',
                   block_tf(p, mode), mono_encoder(block_inv(p, mode)), nn=3, nc=2)


# ------------------------------------------------------------------ round 20: syllabic script; longer-range structure
CCLS = {**{c: 1 for c in 'pb'}, **{c: 2 for c in 'td'}, **{c: 3 for c in 'kcgqxjh'}, **{c: 4 for c in 'fvw'},
        **{c: 5 for c in 'sz'}, **{c: 6 for c in 'mn'}, **{c: 7 for c in 'lry'}}


def abugida(words):
    out = []
    for w in words:
        i = 0
        while i < len(w):
            c = w[i]
            if c in 'aeiou':
                cls, v = 0, c; i += 1
            else:
                cls = CCLS.get(c, 3); i += 1
                v = w[i] if i < len(w) and w[i] in 'aeiou' else ''
                if v:
                    i += 1
            vt = 0 if not v else (1 if v in 'aou' else 2)
            out.append(chr(97 + cls * 3 + vt))
    return ''.join(out)


def ngram_repeats(seq, k):
    c = _C(tuple(seq[i:i + k]) for i in range(len(seq) - k + 1))
    return sum(v - 1 for v in c.values() if v > 1)


@rnd(20)
def round20():
    model_variant(20, 'syllabic: orientation = consonant class, arcs = vowel', abugida)
    rng = random.Random(3)
    E = np.array([[ngram_repeats(list(english(N, rng)), k) for k in (2, 3, 4)] for _ in range(1000)])
    S = np.array([[ngram_repeats(s, k) for k in (2, 3, 4)] for s in shuffles(300)])
    Dd = np.array([[ngram_repeats(s, k) for k in (2, 3, 4)] for s in doublet_shuffles(300)])
    D = np.array([ngram_repeats(SIGNS, k) for k in (2, 3, 4)])
    for i, k in enumerate((2, 3, 4)):
        print(f'repeated {k}-grams: Dorabella {D[i]}; English mean {E[:, i].mean():.2f} (P(<=D) {np.mean(E[:, i] <= D[i]):.3f}); '
              f'shuffles {S[:, i].mean():.2f}; pair-keeping shuffles {Dd[:, i].mean():.2f} (P(>=D) {np.mean(Dd[:, i] >= D[i]):.3f})')
    log(20, 'repeated trigrams: English-like or pair-generator-like?', float(D[1]), list(Dd[:, 1]), list(E[:, 1]),
        f'trigrams {D[1]} vs English {E[:, 1].mean():.2f}, pair-keeping shuffles {Dd[:, 1].mean():.2f}')


# ------------------------------------------------------------------ round 21: misread-tolerant search, more compute
def nb(t, d):
    return (((t[0] + d) % 8), t[1])


def misread_solve(seq, K, seed, R=30, lam=4.0):
    """Alternate: anneal key on the current reading; greedily accept neighbouring-orientation slips worth > lam
    nats (up to K); re-anneal from the current key; 3 rounds. 24-token key domain."""
    m = M4; rng = random.Random(seed)
    TOKS = [(o, a) for o in range(8) for a in range(3)]
    tid = {t: i for i, t in enumerate(TOKS)}
    base = np.array([tid[s] for s in seq])
    def anneal_key(c, key, iters, T0):
        cur = m.score_idx(key[c])
        for i in range(iters):
            T = T0 * (1 - i / iters) + 0.05
            k2 = key.copy(); s = rng.randrange(24)
            if rng.random() < 0.3:
                free = [a for a in range(m.A) if a not in set(k2.tolist())]; k2[s] = rng.choice(free)
            else:
                t = rng.randrange(24); k2[s], k2[t] = k2[t], k2[s]
            sc = m.score_idx(k2[c])
            if sc >= cur or rng.random() < math.exp((sc - cur) / T):
                key, cur = k2, sc
        return key, cur
    best = (-1e18, None, None)
    for r in range(R):
        key = np.array(rng.sample(range(m.A), 24)); c = base.copy(); edits = 0
        key, cur = anneal_key(c, key, 15000, 3.0)
        for rd in range(3):
            while edits < K:
                b0 = m.score_idx(key[c]); gain = (lam, None)
                for p in range(len(c)):
                    if c[p] != base[p]:
                        continue
                    for d in (-1, 1):
                        c2 = c.copy(); c2[p] = tid[nb(TOKS[base[p]], d)]
                        g = m.score_idx(key[c2]) - b0
                        if g > gain[0]:
                            gain = (g, (p, c2[p]))
                if gain[1] is None:
                    break
                c[gain[1][0]] = gain[1][1]; edits += 1
            key, cur = anneal_key(c, key, 6000, 0.8)
        tot = (cur - lam * edits) / len(c)
        if tot > best[0]:
            best = (tot, ''.join(m.alpha[i] for i in key[c]), edits)
    return best


@rnd(21)
def round21():
    rng = random.Random(21); ctl, acc = [], []
    for j in range(4):
        pt = english(N, rng)
        cells = rng.sample([(o, a) for o in range(8) for a in range(3)], 24)
        key = {c: cells[i % 24] for i, c in enumerate(sorted(set(pt)))}
        sg = [key[c] for c in pt]
        for q in rng.sample(range(N), 6):
            sg[q] = nb(sg[q], rng.choice((-1, 1)))
        sc, t2, e = misread_solve(sg, 8, 200 + j)
        ctl.append(sc); acc.append(np.mean([a == b for a, b in zip(t2, pt)]))
        print(f'  control {j}: {sc:.3f} acc {acc[-1]:.2f} edits {e}', flush=True)
    if np.median(acc) < 0.5:
        log(21, 'misread-tolerant (6 seeded slips, 30 restarts)', -9.0, [-9.0], ctl, 'controls not recovered: method still lacks power',
            f'ctl acc {min(acc):.2f}..{max(acc):.2f}', acc)
        return
    D = misread_solve(SIGNS, 8, 0)
    nulls = [misread_solve(s, 8, 100 + j)[0] for j, s in enumerate(shuffles(4))]
    log(21, 'misread-tolerant (≤ 8 slips, 30 restarts)', D[0], nulls, ctl, D[1], f'edits {D[2]}; ctl acc {min(acc):.2f}..{max(acc):.2f}', acc)


# ------------------------------------------------------------------ round 23: Nihilist with known keys
def coord(letter, g):
    v = E24.index({'j': 'i', 'v': 'u'}.get(letter, letter))
    gg, c = divmod(v, 3)
    start, step, arcrev = g
    return ((gg * step + start) % 8, 2 - c if arcrev else c)


def nihilist_family(reset):
    def fam(signs):
        for g in grids():
            inv = {coord(ch, g): ch for ch in E24}
            for w in KEYWORDS:
                kc = [coord(ch, g) for ch in w]
                for sgn in (1, -1):
                    out, i = '', 0
                    for l in (lines_of(signs) if reset else [signs]):
                        for j, (o, a) in enumerate(l):
                            ko, ka = kc[(j if reset else i) % len(kc)]
                            out += inv[((o - sgn * ko) % 8, (a - sgn * ka) % 3)]; i += 1
                    yield out, f'{w} {"sub" if sgn == 1 else "add"} grid={g}'
    return fam


def nihilist_encoder(reset):
    def enc(text, rng):
        g = rng.choice(list(grids())); w = rng.choice(KEYWORDS); sgn = rng.choice((1, -1))
        kc = [coord(ch, g) for ch in w]
        out, i = [], 0
        for l in (LINES if reset else [SIGNS]):
            for j in range(len(l)):
                o, a = coord(text[i], g); ko, ka = kc[(j if reset else i) % len(kc)]
                out.append(((o + sgn * ko) % 8, (a + sgn * ka) % 3)); i += 1
        return out
    return enc


@rnd(23)
def round23():
    direct(23, 'Nihilist on sign coordinates, 27 keys (COURAGE …)', nihilist_family(False), nihilist_encoder(False))
    direct(23, 'Nihilist, key restarting each line', nihilist_family(True), nihilist_encoder(True))


# ------------------------------------------------------------------ round 22: quotations from Elgar's 1890s reading
POETS = {'1365': 'Longfellow (incl. King Olaf)', '2039': 'Evangeline', '610': 'Idylls of the King',
         '8601': 'Tennyson early poems', '791': 'The Princess', '16376': 'Browning shorter poems'}


def poet_texts():
    out = {}
    for g, nm in POETS.items():
        f = _os.path.join(DL, f'pg{g}.txt')
        if _os.path.exists(f):
            out[nm] = corpora.strip_gutenberg(open(f, encoding='utf-8', errors='replace').read())
    return out


@rnd(22)
def round22():
    raw = poet_texts()
    letters = {k: np.frombuffer(lm.norm(v, 'modern', False).encode(), dtype=np.uint8) - 97 for k, v in raw.items()}
    initials = {k: np.array([ord(w[0].lower()) - 97 for w in re.findall(r'[A-Za-z]+', v)]) for k, v in raw.items()}
    print({k: (len(letters[k]), len(initials[k])) for k in raw}, flush=True)
    for nm, T in (('letters', letters), ('word initials', initials)):
        D = quote_search(SIGNS, T)
        nulls = [quote_search(s, T)[0] for s in shuffles(3)]
        rng = random.Random(22); ctl = []
        for j in range(2):
            k = rng.choice(list(T)); st = rng.randrange(len(T[k]) - N); w = T[k][st:st + N]
            cells = rng.sample([(o, a) for o in range(8) for a in range(3)], 24)
            sg = [cells[x % 24] for x in w]
            for q in rng.sample(range(N), 6):
                sg[q] = (rng.randrange(8), rng.randrange(3))
            ctl.append(quote_search(sg, T)[0])
        log(22, f'quotation from Longfellow/Tennyson/Browning ({nm})', D[0], nulls, ctl, D[3], f'{D[1]}@{D[2]} explains {D[0]}/87')


# ------------------------------------------------------------------ round 24: cribs from the July 1897 visit
VISIT = ['kite', 'kites', 'boscobel', 'oak', 'royaloak', 'kingcharles', 'charles', 'caractacus', 'lullaby', 'bavarian',
         'highlands', 'luxchristi', 'wolverhampton', 'mother', 'thankyou', 'thanks', 'visit', 'pennys', 'mrspenny',
         'monday', 'tuesday', 'wednesday', 'thursday', 'friday', 'saturday', 'sunday', 'july', 'music', 'sing']


def visit_cribs(signs, seed, maxper=6):
    rng = random.Random(seed); best = (-1e9, '', '')
    for crib in VISIT:
        hits = [p for p in range(len(signs) - len(crib) + 1) if crib_fit(signs, crib, p)]
        if len(crib) < 6:
            hits = rng.sample(hits, min(maxper, len(hits)))
        for p in hits:
            sc, txt = anneal_fixed_signs(signs, crib_fit(signs, crib, p), seed + p, R=6, iters=8000)
            if sc > best[0]:
                best = (sc, txt, f'{crib}@{p}')
    return best


@rnd(24)
def round24():
    D = visit_cribs(SIGNS, 0)
    nulls = [visit_cribs(s, 100 + j)[0] for j, s in enumerate(shuffles(3))]
    log(24, 'July 1897 visit cribs (29 words), every fitting offset', D[0], nulls, [], D[1], D[2])


# ------------------------------------------------------------------ round 25: can a two-habit pseudo-writer reproduce Dorabella?
def pseudo_writer(rng, q0, q4, po, pa):
    s = [(int(rng.choice(8, p=po)), int(rng.choice(3, p=pa)))]
    while len(s) < N:
        o = s[-1][0]; u = rng.random()
        if u < q4:
            no = (o + 4) % 8
        elif u < q4 + q0:
            no = o
        else:
            w = po.copy(); w[o] = 0; w[(o + 4) % 8] = 0; w /= w.sum(); no = int(rng.choice(8, p=w))
        s.append((no, int(rng.choice(3, p=pa))))
    return s


def flips(seq):
    return sum((b[0] - a[0]) % 8 == 4 for a, b in zip(seq, seq[1:]))


@rnd(25)
def round25():
    o = np.bincount([s[0] for s in SIGNS], minlength=8) / N
    a = np.bincount([s[1] for s in SIGNS], minlength=3) / N
    q4 = flips(SIGNS) / (N - 1); q0 = sum(x[0] == y[0] for x, y in zip(SIGNS, SIGNS[1:])) / (N - 1)
    rng = np.random.default_rng(25)
    def stats(seq):
        return np.append(inv_stats(seq), flips(seq))
    D = stats(SIGNS)
    G = np.array([stats(pseudo_writer(rng, q0, q4, o, a)) for _ in range(4000)])
    r2 = random.Random(25)
    E = []
    for _ in range(4000):
        t = english(N, r2); cells = r2.sample([(x, y) for x in range(8) for y in range(3)], 24)
        key = {c: cells[i % 24] for i, c in enumerate(sorted(set(t)))}
        E.append(stats([key[c] for c in t]))
    E = np.array(E)
    names = ['distinct', 'IoC', 'rep pairs', 'doubles', 'singletons', 'flips']
    out = []
    for nm, W in (('pseudo-writer', G), ('English, random key', E)):
        mu, sd = W.mean(0), W.std(0) + 1e-9
        dz = np.sqrt((((W - mu) / sd) ** 2).sum(1)); dd = np.sqrt((((D - mu) / sd) ** 2).sum())
        p = np.mean(dz >= dd); out.append(p)
        print(f'{nm:20s} mean {np.round(mu, 3)}  P(as typical) {p:.3f}', flush=True)
    print(f'{"DORABELLA":20s}      {np.round(D, 3)}   ({", ".join(names)})')
    log(25, 'two-habit pseudo-writer vs English-under-a-key', out[0], [out[1]], [],
        f'pseudo-writer P {out[0]:.3f}; English-under-key P {out[1]:.3f} (with flips as a 6th statistic)')


# ------------------------------------------------------------------ round 26: English under a flip-heavy layout
FLIP_LAYOUT = ['dgi', 'hrs', 'bcz', 'opq', 'lnw', 'aet', 'kxy', 'fmu']     # max expected opposite steps for English (S 16)


@rnd(26)
def round26():
    pos = {}
    for o, grp in enumerate(FLIP_LAYOUT):
        for k, ch in enumerate(grp):
            pos[ch] = (o, k)
    pos['j'] = pos['i']; pos['v'] = pos['u']
    def stats(seq):
        return np.append(inv_stats(seq), flips(seq))
    D = stats(SIGNS)
    r2 = random.Random(26); W = []
    for _ in range(4000):
        t = english(N, r2)
        W.append(stats([pos[c] for c in t]))
    W = np.array(W)
    mu, sd = W.mean(0), W.std(0) + 1e-9
    dz = np.sqrt((((W - mu) / sd) ** 2).sum(1)); dd = np.sqrt((((D - mu) / sd) ** 2).sum())
    p = np.mean(dz >= dd)
    print(f'English under flip-heavy layout: mean {np.round(mu, 3)}; P(as typical) {p:.3f}; P(flips >= 27) {np.mean(W[:, 5] >= 27):.3f}')
    log(26, 'English under the flip-maximising layout: all 6 statistics', p, [0.008, 0.013], [],
        f'mean flips {mu[5]:.1f}; P(flips>=27) {np.mean(W[:, 5] >= 27):.3f}')


# ------------------------------------------------------------------ round 27: every plausible reading at once
import json as _json


def candidate_sets():
    """Per position: consensus + attested alternatives + measured reading + both neighbours where the 1937 angle
    was within 8 degrees of a class boundary."""
    TOKS = [(o, a) for o in range(8) for a in range(3)]
    cands = [{s} for s in SIGNS]
    dis = _json.load(open(_os.path.join(HERE, 'disputes_merged.json')))
    for p, alts in dis.items():
        for t in alts:
            if not t.startswith('?'):
                cands[int(p)].add((('ABCDEFGH'.index(t[0])), int(t[1]) - 1))
    ang = _json.load(open(_os.path.join(HERE, 'angles_hull.json')))
    centers = {'A': 0, 'H': 45, 'G': 90, 'F': 135, 'E': 180, 'D': 225, 'C': 270, 'B': 315}
    for r in ang:
        o = 'ABCDEFGH'.index(r['consensus'][0])
        d = (r['angle'] - centers[r['consensus'][0]] + 180) % 360 - 180
        if abs(d) > 22.5 - 8:
            for k in (-1, 1):
                cands[r['i']].add(((o + k) % 8, SIGNS[r['i']][1]))
    return [sorted(c) for c in cands]


def ambig_solve(cands, m, seed, R=12, iters=30000):
    rng = random.Random(seed)
    TOKS = [(o, a) for o in range(8) for a in range(3)]; tid = {t: i for i, t in enumerate(TOKS)}
    C = [[tid[t] for t in c] for c in cands]
    multi = [i for i, c in enumerate(C) if len(c) > 1]
    best = (-1e18, '')
    for r in range(R):
        key = np.array(rng.sample(range(m.A), 24)); ch = [c[0] for c in C]
        cur = m.score_idx(key[np.array(ch)])
        for i in range(iters):
            T = 3.0 * (1 - i / iters) + 0.05
            k2, ch2 = key, ch
            u = rng.random()
            if u < 0.2 and multi:
                ch2 = list(ch); p = rng.choice(multi); ch2[p] = rng.choice(C[p])
            elif u < 0.4:
                k2 = key.copy(); s = rng.randrange(24)
                free = [a for a in range(m.A) if a not in set(k2.tolist())]; k2[s] = rng.choice(free)
            else:
                k2 = key.copy(); s, t = rng.randrange(24), rng.randrange(24); k2[s], k2[t] = k2[t], k2[s]
            sc = m.score_idx(k2[np.array(ch2)])
            if sc >= cur or rng.random() < math.exp((sc - cur) / T):
                key, ch, cur = k2, ch2, sc
        if cur > best[0]:
            best = (cur, ''.join(m.alpha[i] for i in key[np.array(ch)]))
    return best[0] / N, best[1]


@rnd(27)
def round27():
    cands = candidate_sets()
    multi = sum(len(c) > 1 for c in cands)
    print(f'{multi} positions with alternatives; {int(np.prod([len(c) for c in cands])):.3g} readings', flush=True)
    for mid in ('en-modern', 'en-elgar'):
        m = lm.load(mid, order=4, spaces=False)
        D = ambig_solve(cands, m, 0)
        nulls = []
        for j, s in enumerate(shuffles(3)):
            perm = np.random.default_rng(j).permutation(N)
            nulls.append(ambig_solve([cands[i] for i in perm], m, 100 + j)[0])
        rng = random.Random(27); ctl, acc = [], []
        for j in range(3):
            pt = english(N, rng); cells = rng.sample([(o, a) for o in range(8) for a in range(3)], 24)
            key = {c: cells[i % 24] for i, c in enumerate(sorted(set(pt)))}
            truth = [key[c] for c in pt]
            cs = []
            for i, tkn in enumerate(truth):            # same candidate-set shape: the truth hidden among slips
                if len(cands[i]) > 1:
                    alts = {tkn, ((tkn[0] + 1) % 8, tkn[1]), ((tkn[0] - 1) % 8, tkn[1])}
                    obs = rng.choice(sorted(alts))
                    cs.append(sorted({obs, tkn} | {((obs[0] + 1) % 8, obs[1])}))
                else:
                    cs.append([tkn])
            sc, t2 = ambig_solve(cs, m, 200 + j)
            ctl.append(sc); acc.append(np.mean([a == b for a, b in zip(t2, pt)]))
        log(27, f'all plausible readings jointly ({multi} positions), {mid}', D[0], nulls, ctl, D[1],
            f'ctl acc {min(acc):.2f}..{max(acc):.2f}', acc)


# ------------------------------------------------------------------ round 28: flip-heavy key as a prior, with misreads
_BIG = None


def bigram_probs():
    global _BIG
    if _BIG is None:
        t = corpus()[:2_000_000]; c = np.zeros((26, 26))
        a = np.frombuffer(t.encode(), dtype=np.uint8) - 97
        np.add.at(c, (a[:-1], a[1:]), 1); _BIG = c / c.sum()
    return _BIG


def flip_prior(key):
    """Expected opposite-orientation steps per pair if English were written with this key (token t has orientation t//3)."""
    P = bigram_probs(); m = M4
    orient = np.full(26, -1)
    for t, li in enumerate(key):
        ch = m.alpha[li]
        if ch in AZ and orient[AZ.index(ch)] < 0:
            orient[AZ.index(ch)] = t // 3
    ok = orient >= 0
    O = orient[:, None]; Q = orient[None, :]
    opp = ((O - Q) % 8 == 4) & ok[:, None] & ok[None, :]
    return float((P * opp).sum())


def prior_misread_solve(seq, K, seed, beta, R=20, lam=4.0):
    m = M4; rng = random.Random(seed)
    TOKS = [(o, a) for o in range(8) for a in range(3)]; tid = {t: i for i, t in enumerate(TOKS)}
    base = np.array([tid[s] for s in seq])
    def total(key, c):
        return m.score_idx(key[c]) + beta * (len(c) - 1) * flip_prior(key)
    def anneal_key(c, key, iters, T0):
        cur = total(key, c)
        for i in range(iters):
            T = T0 * (1 - i / iters) + 0.05
            k2 = key.copy(); s = rng.randrange(24)
            if rng.random() < 0.3:
                free = [a for a in range(m.A) if a not in set(k2.tolist())]; k2[s] = rng.choice(free)
            else:
                t = rng.randrange(24); k2[s], k2[t] = k2[t], k2[s]
            sc = total(k2, c)
            if sc >= cur or rng.random() < math.exp((sc - cur) / T):
                key, cur = k2, sc
        return key, cur
    best = (-1e18, None, 0)
    for r in range(R):
        key = np.array(rng.sample(range(m.A), 24)); c = base.copy(); edits = 0
        key, cur = anneal_key(c, key, 12000, 3.0)
        for rd in range(2):
            while edits < K:
                b0 = m.score_idx(key[c]); gain = (lam, None)
                for p in range(len(c)):
                    if c[p] != base[p]:
                        continue
                    for d in (-1, 1):
                        c2 = c.copy(); c2[p] = tid[nb(TOKS[base[p]], d)]
                        g = m.score_idx(key[c2]) - b0
                        if g > gain[0]:
                            gain = (g, (p, c2[p]))
                if gain[1] is None:
                    break
                c[gain[1][0]] = gain[1][1]; edits += 1
            key, cur = anneal_key(c, key, 5000, 0.8)
        lm_part = m.score_idx(key[c])
        tot = (lm_part - lam * edits) / len(c)
        if tot > best[0]:
            best = (tot, ''.join(m.alpha[i] for i in key[c]), edits)
    return best


@rnd(28)
def round28():
    pos = {}
    for o, grp in enumerate(FLIP_LAYOUT):
        for k, ch in enumerate(grp):
            pos[ch] = (o, k)
    pos['j'] = pos['i']; pos['v'] = pos['u']
    for beta in (0.0, 3.0):
        rng = random.Random(28); ctl, acc = [], []
        for j in range(3):
            pt = english(N, rng); rot = rng.randrange(8); rev = rng.random() < .5
            sg = [(((pos[c][0] * (-1 if rev else 1)) + rot) % 8, pos[c][1]) for c in pt]
            for q in rng.sample(range(N), 6):
                sg[q] = nb(sg[q], rng.choice((-1, 1)))
            sc, t2, e = prior_misread_solve(sg, 8, 300 + j, beta)
            ctl.append(sc); acc.append(np.mean([a == b for a, b in zip(t2, pt)]))
        print(f'  beta {beta}: controls (flip-heavy key, 6 misreads) acc {np.round(acc, 2)}', flush=True)
        if beta == 0.0:
            continue
        D = prior_misread_solve(SIGNS, 8, 0, beta)
        nulls = [prior_misread_solve(s, 8, 100 + j, beta)[0] for j, s in enumerate(shuffles(3))]
        log(28, f'flip-heavy key prior (beta {beta}) + misreads <= 8', D[0], nulls, ctl, D[1],
            f'edits {D[2]}; ctl acc {min(acc):.2f}..{max(acc):.2f}', acc)


# ------------------------------------------------------------------ round 29: do table-changing ciphers keep the flips?
@rnd(29)
def round29():
    order = [c for grp in FLIP_LAYOUT for c in grp]               # 24 cells in layout order: index = 3*o + a
    cell = {c: (i // 3, i % 3) for i, c in enumerate(order)}
    cell['j'] = cell['i']; cell['v'] = cell['u']
    idx = {c: i for i, c in enumerate(order)}; idx['j'] = idx['i']; idx['v'] = idx['u']
    rng = random.Random(29)
    texts = [english(N, rng) for _ in range(2000)]
    def fl(sg):
        return sum((b[0] - a[0]) % 8 == 4 for a, b in zip(sg, sg[1:]))
    systems = {
        'fixed table (no key layer)': lambda t, r: [cell[c] for c in t],
        'dial turned by a 5-step periodic key': lambda t, r: (lambda k: [((cell[c][0] + k[i % 5]) % 8, cell[c][1]) for i, c in enumerate(t)])([r.randrange(8) for _ in range(5)]),
        'Vigenere on the letters, period 5': lambda t, r: (lambda k: [divmod((idx[c] + k[i % 5]) % 24, 3) for i, c in enumerate(t)])([r.randrange(24) for _ in range(5)]),
        'Vigenere, period 3': lambda t, r: (lambda k: [divmod((idx[c] + k[i % 3]) % 24, 3) for i, c in enumerate(t)])([r.randrange(24) for _ in range(3)]),
        'autokey (shift by previous letter)': lambda t, r: [divmod((idx[c] + (idx[t[i - 1]] if i else r.randrange(24))) % 24, 3) for i, c in enumerate(t)],
        'running key from English': lambda t, r: (lambda kt: [divmod((idx[c] + idx[k]) % 24, 3) for c, k in zip(t, kt)])(english(N, r)),
        'Nihilist (coordinates added, key 7)': lambda t, r: (lambda k: [((cell[c][0] + k[i % 7][0]) % 8, (cell[c][1] + k[i % 7][1]) % 3) for i, c in enumerate(t)])([(r.randrange(8), r.randrange(3)) for _ in range(7)]),
        'progressive dial (+1 each sign)': lambda t, r: [((cell[c][0] + i) % 8, cell[c][1]) for i, c in enumerate(t)],
    }
    for nm, f in systems.items():
        F = np.array([fl(f(t, rng)) for t in texts])
        print(f'  {nm:40s} flips mean {F.mean():5.1f}   P(>=27) {np.mean(F >= 27):.3f}', flush=True)
        log(29, f'flips survive? {nm}', 27.0, [float(F.mean())], [], f'mean flips {F.mean():.1f}, P(>=27) {np.mean(F >= 27):.3f}')


# ------------------------------------------------------------------ round 30: is Elgar's own prose solvable at 87 signs?
@rnd(30)
def round30():
    t = lm.norm(open(_os.path.join(HERE, 'src', 'elgar_register.txt'), encoding='utf-8').read(), 'modern', False)
    rng = random.Random(30)
    for label, src in (('Elgar\'s letters (not in the model)', t), ('Gutenberg prose (in the model)', None)):
        accs = []
        for j in range(12):
            if src is None:
                pt = english(N, rng)
            else:
                p = rng.randrange(len(src) - N); pt = src[p:p + N]
            cells = rng.sample([(o, a) for o in range(8) for a in range(3)], 24)
            key = {c: cells[i % 24] for i, c in enumerate(sorted(set(pt)))}
            sc, txt, _, _ = solve_tokens([key[c] for c in pt], R=12, seed=500 + j)
            accs.append(np.mean([a == b for a, b in zip(txt, pt)]))
        accs = np.array(accs)
        print(f'  {label:36s} recovered >=90%: {np.mean(accs >= .9):.2f}; median accuracy {np.median(accs):.2f}; '
              f'{np.round(np.sort(accs), 2)}', flush=True)
        log(30, f'solvability at 87 signs: {label}', float(np.median(accs)), [0.0], list(accs), f'share >= 90%: {np.mean(accs >= .9):.2f}')


# ------------------------------------------------------------------ round 31: search failure or model failure?
@rnd(31)
def round31():
    t = lm.norm(open(_os.path.join(HERE, 'src', 'elgar_register.txt'), encoding='utf-8').read(), 'modern', False)
    rng = random.Random(30)                            # same windows as round 30
    rows = []
    for j in range(12):
        p = rng.randrange(len(t) - N); pt = t[p:p + N]
        cells = rng.sample([(o, a) for o in range(8) for a in range(3)], 24)
        key = {c: cells[i % 24] for i, c in enumerate(sorted(set(pt)))}
        for R, it in ((12, 12000), (60, 30000)):
            sc, txt, _, _ = solve_tokens([key[c] for c in pt], R=R, iters=it, seed=500 + j)
            acc = np.mean([a == b for a, b in zip(txt, pt)])
            true = M4.per_char(pt)
            kind = 'solved' if acc >= .9 else ('SEARCH failure (truth scores higher)' if true > sc + 1e-3 else 'MODEL failure (wrong text scores higher)')
            rows.append((j, R, acc, sc, true, kind))
            print(f'  window {j:2d} restarts {R:3d}: acc {acc:.2f}  found {sc:.3f}  truth {true:.3f}  {kind}', flush=True)
    for R in (12, 60):
        sub = [r for r in rows if r[1] == R]
        s = sum(r[5] == 'solved' for r in sub); se = sum(r[5].startswith('SEARCH') for r in sub); mo = sum(r[5].startswith('MODEL') for r in sub)
        log(31, f"Elgar's letters at 87 signs, {R} restarts: solved / search fail / model fail", s / len(sub), [se / len(sub)], [mo / len(sub)],
            f'solved {s}, search failures {se}, model failures {mo} of {len(sub)}')


# ------------------------------------------------------------------ round 35: pair habit or language?
@rnd(35)
def round35():
    """Statistics beyond adjacent pairs: repeats at lag 2/3/4 and repeated skip-grams (a ? b). Pair-keeping shuffles
    keep every adjacent pair exactly (the null for 'a writer with pair habits only'); English under random keys is
    the language reference."""
    def stats(s):
        n = len(s)
        lag = [sum(s[i] == s[i + k] for i in range(n - k)) for k in (2, 3, 4)]
        skip = _C((s[i], s[i + 2]) for i in range(n - 2))
        rep_skip = sum(v - 1 for v in skip.values() if v > 1)
        return np.array(lag + [rep_skip])
    D = stats(SIGNS)
    Pk = np.array([stats(s) for s in doublet_shuffles(2000)])
    rng = random.Random(35); E = []
    for _ in range(2000):
        t = english(N, rng); cells = rng.sample([(o, a) for o in range(8) for a in range(3)], 24)
        key = {c: cells[i % 24] for i, c in enumerate(sorted(set(t)))}
        E.append(stats([key[c] for c in t]))
    E = np.array(E)
    names = ['repeats at gap 2', 'repeats at gap 3', 'repeats at gap 4', 'repeated skip-pairs (a ? b)']
    for i, nm in enumerate(names):
        print(f'  {nm:28s} Dorabella {D[i]:3d} | pair-keeping shuffles mean {Pk[:, i].mean():5.2f}, P(>=D) {np.mean(Pk[:, i] >= D[i]):.3f} '
              f'| English mean {E[:, i].mean():5.2f}, P(<=D) {np.mean(E[:, i] <= D[i]):.3f}', flush=True)
        log(35, f'beyond pairs: {nm}', float(D[i]), list(Pk[:, i].astype(float)), list(E[:, i].astype(float)),
            f'pair-keeping mean {Pk[:, i].mean():.2f} P(>=D) {np.mean(Pk[:, i] >= D[i]):.3f}; English mean {E[:, i].mean():.2f}')


# ------------------------------------------------------------------ round 36: a sentence break at the 1949 dot
def split_solve(signs, cut, seed, R=20, iters=20000):
    """One shared one-to-one key; the two parts scored as separate passages (no context across the break)."""
    m = M4; rng = random.Random(seed)
    syms = sorted(set(signs)); ct = np.array([syms.index(s) for s in signs])
    a, b = ct[:cut], ct[cut:]
    best = (-1e18, '')
    for r in range(R):
        key = np.array(rng.sample(range(m.A), len(syms)))
        cur = m.score_idx(key[a]) + m.score_idx(key[b])
        for i in range(iters):
            T = 3.0 * (1 - i / iters) + 0.05
            k2 = key.copy(); s = rng.randrange(len(syms))
            if rng.random() < 0.3:
                free = [x for x in range(m.A) if x not in set(k2.tolist())]; k2[s] = rng.choice(free)
            else:
                t = rng.randrange(len(syms)); k2[s], k2[t] = k2[t], k2[s]
            sc = m.score_idx(k2[a]) + m.score_idx(k2[b])
            if sc >= cur or rng.random() < math.exp((sc - cur) / T):
                key, cur = k2, sc
        if cur > best[0]:
            best = (cur, ''.join(m.alpha[i] for i in key[a]) + ' | ' + ''.join(m.alpha[i] for i in key[b]))
    return best[0] / N, best[1]


@rnd(36)
def round36():
    for cut in (40, 41):                                # dot after sign 40 or 41 (line 2, sign 11 or 12)
        D = split_solve(SIGNS, cut, 0)
        nulls = [split_solve(s, cut, 100 + j)[0] for j, s in enumerate(shuffles(4))]
        log(36, f'sentence break after sign {cut} (1949 dot)', D[0], nulls, [], D[1])


# ------------------------------------------------------------------ round 40: notebook practice phrases; the Lullaby's words
PRACTICE = ['averyoldcypher', 'averyoldcipher', 'doyougotolondon', 'marcoelgar', 'marco', 'cypher', 'london']


@rnd(40)
def round40():
    raw = open(_os.path.join(HERE, 'src', 'music', 'lullaby_lyric.txt'), encoding='utf-8').read()
    raw = re.sub(r'edition and engraving.*?secondary edition', ' ', raw)
    words = raw.split()
    dedup = [w for i, w in enumerate(words) if i == 0 or w != words[i - 1]]
    letters = re.sub(r'[^a-z]', '', ''.join(dedup))
    print(f'lyric stream {len(letters)} letters', flush=True)
    T = {'Lullaby lyric': np.frombuffer(letters.encode(), dtype=np.uint8) - 97}
    D = quote_search(SIGNS, T); nulls = [quote_search(s, T)[0] for s in shuffles(6)]
    log(40, 'Lullaby lyric as the plaintext (every 87-letter window)', D[0], nulls, [], D[3], f'explains {D[0]}/87')
    lyric_words = sorted({w for w in re.findall(r'[a-z]{5,}', ' '.join(dedup))})
    global VISIT
    saved = VISIT
    VISIT = PRACTICE + lyric_words
    try:
        D = visit_cribs(SIGNS, 0)
        nulls = [visit_cribs(s, 100 + j)[0] for j, s in enumerate(shuffles(3))]
    finally:
        VISIT = saved
    log(40, f'cribs: notebook practice phrases + {len(lyric_words)} lyric words', D[0], nulls, [], D[1], D[2])


# ------------------------------------------------------------------ round 51: names and places of Elgar's circle in 1897
CIRCLE = ['alice', 'carice', 'jaeger', 'august', 'nimrod', 'schuster', 'troyte', 'griffith', 'winifred', 'norbury',
          'isabel', 'fitton', 'sinclair', 'nevinson', 'townshend', 'arnold', 'baker', 'forli', 'malvern', 'birchwood',
          'worcester', 'hereford', 'wolverhampton', 'penny', 'edward', 'elgar', 'ladyelgar', 'mrselgar']


@rnd(51)
def round51():
    global VISIT
    saved = VISIT; VISIT = CIRCLE
    try:
        D = visit_cribs(SIGNS, 0)
        nulls = [visit_cribs(s, 100 + j)[0] for j, s in enumerate(shuffles(3))]
    finally:
        VISIT = saved
    log(51, "cribs: names and places of Elgar's circle in 1897 (28)", D[0], nulls, [], D[1], D[2])


# ------------------------------------------------------------------ round 52: a music model from the Lullaby arrangement
@rnd(52)
def round52():
    """Note events of every staff of the NWC Lullaby arrangement as (staff position mod 7, duration class) tokens
    (21 symbols); order-3 model; Dorabella solved as a melody (one-to-one sign -> token). Controls: windows of the
    Treble staff (held out of the model), enciphered; nulls: shuffles."""
    import json, glob
    def toks(f):
        out = []
        for pos, dur, *_ in json.load(open(f)):
            if pos is None:
                continue
            dc = 0 if dur < 2 else (1 if dur == 2 else 2)
            out.append(chr(97 + (pos % 7) * 3 + dc))
        return out
    files = sorted(glob.glob(_os.path.join(HERE, 'src', 'music', '*.json')))
    held = [f for f in files if f.lower().endswith('treble.json')]
    train = ''.join(''.join(toks(f)) for f in files if f not in held)
    alpha = ''.join(chr(97 + i) for i in range(21))
    m = lm.DenseLM.build(train, 3, alpha)
    print(f'music model: {len(train)} note tokens from {len(files) - len(held)} staves', flush=True)
    def run(tokens, seed):
        syms = sorted(set(tokens), key=str); ct = np.array([syms.index(t) for t in tokens])
        sc, key = anneal(ct, len(syms), m, restarts=20, iters=20000, seed=seed, injective=len(syms) <= m.A)
        return sc / len(ct), ''.join(m.alpha[i] for i in key[ct])
    D, txt = run(SIGNS, 0)
    nulls = [run(s, 100 + j)[0] for j, s in enumerate(shuffles(4))]
    tr = ''.join(toks(held[0])); rng = random.Random(52); ctl, acc = [], []
    for j in range(3):
        p = rng.randrange(len(tr) - N); pt = tr[p:p + N]
        cells = rng.sample([(o, a) for o in range(8) for a in range(3)], 24)
        key = {c: cells[i] for i, c in enumerate(sorted(set(pt)))}
        sc, t2 = run([key[c] for c in pt], 200 + j); ctl.append(sc); acc.append(np.mean([a == b for a, b in zip(t2, pt)]))
    log(52, 'Dorabella as a melody (music model from the Lullaby arrangement)', D, nulls, ctl, txt,
        f'ctl acc {min(acc):.2f}..{max(acc):.2f}', acc)
