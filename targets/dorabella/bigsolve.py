"""Rounds 33-34: large parallel searches with matched controls, for the two fixed-table explanations left.

mode 'misread': one-to-one key plus up to K orientation slips (neighbouring orientation, same arcs), each slip
  penalised LAM nats; annealed jointly (key moves and slip moves).
mode 'homo': fixed table with homophones: up to 2 signs per letter.
Targets: Dorabella (consensus) and controls = windows of Elgar's letters (not in en-modern) put through the same
system (random key; for 'misread' with S seeded slips; for 'homo' with the 6 commonest letters given two signs).
Each target gets RESTARTS independent runs spread over the CPU cores; best per target is reported with accuracy.

python targets/dorabella/bigsolve.py <mode> <restarts> [K or S]
"""
import os, sys, random, math
import numpy as np
from multiprocessing import Pool
sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__)), '..', '..'))
HERE = os.path.dirname(os.path.abspath(__file__))
MODE = sys.argv[1]; RESTARTS = int(sys.argv[2]); K = int(sys.argv[3]) if len(sys.argv) > 3 else 6
TOKS = [(o, a) for o in range(8) for a in range(3)]
LAM, ITERS = 4.0, 60000
_M = None


def model():
    global _M
    if _M is None:
        from lang import lm, corpora
        tf = os.environ.get('DORA_TF')
        if tf:                                     # a model of English in a transformed form, built per worker
            _M = lm.DenseLM.build(tf_text(tf), 4, 'abcdefghijklmnopqrstuvwxyz')
        else:
            _M = lm.load(os.environ.get('DORA_MODEL', 'en-modern'), order=4, spaces=False)
    return _M


def tf_text(tf, which='corpus'):
    import re
    from lang import corpora
    raw = corpora.text(['en-gutenberg'])[:5_000_000].lower() if which == 'corpus' else which
    w = re.findall(r'[a-z]+', raw)
    if tf == 'backslang':
        return ''.join(x[::-1] for x in w)
    if tf == 'skeleton':
        return ''.join(re.sub('[aeiou]', '', x) or x[0] for x in w)
    if tf == 'abbrev3':
        return ''.join(x[:3] for x in w)
    if tf == 'reversed':
        return ''.join(w)[::-1]
    if tf == 'phon25':                         # CMU pronunciations folded to 25 sound classes, one letter each
        MERGE = {'AO': 'AA', 'AH': 'AA', 'IY': 'IH', 'UW': 'UH', 'ER': 'R', 'Z': 'S', 'DH': 'TH', 'ZH': 'SH', 'NG': 'N',
                 'JH': 'CH', 'OY': 'OW', 'AW': 'AY', 'Y': 'IH', 'V': 'F'}
        cmu = {}
        for line in open(os.environ['DORA_CMU'], encoding='utf-8', errors='replace'):
            ww, *ph = line.split('#')[0].split()
            if '(' not in ww and ww not in cmu:
                cmu[ww] = [MERGE.get(re.sub(r'\d', '', p), re.sub(r'\d', '', p)) for p in ph]
        inv = sorted({p for v in cmu.values() for p in v})
        code = {p: 'abcdefghijklmnopqrstuvwxyz'[i] for i, p in enumerate(inv)}
        return ''.join(code[p] for x in w if x in cmu for p in cmu[x])
    raise ValueError(tf)


def run(args):
    seq, seed = args
    m = model(); rng = random.Random(seed); A = m.A
    base = np.array([TOKS.index(tuple(s)) for s in seq]); n = len(base)
    slips = np.zeros(n, dtype=np.int64)                     # -1, 0, +1 orientation slip per position
    ARC = os.environ.get('DORA_SLIP') == 'arcs'          # slips in the arc count (1..3) instead of the orientation
    BOTH = os.environ.get('DORA_SLIP') == 'both'          # +-1 turns the orientation, +-2 changes the arc count
    def reading(sl):
        if BOTH:
            return np.array([(((t // 3 + d) % 8) * 3 + t % 3) if abs(d) == 1 else
                             ((t // 3) * 3 + min(2, max(0, t % 3 + (d // 2)))) for t, d in zip(base, sl)])
        if ARC:
            return np.array([(t // 3) * 3 + min(2, max(0, t % 3 + d)) for t, d in zip(base, sl)])
        return np.array([((t // 3 + d) % 8) * 3 + t % 3 for t, d in zip(base, sl)])
    if MODE in ('homo', 'homoslip'):
        key = np.array([rng.randrange(A) for _ in range(24)])
    else:
        key = np.array(rng.sample(range(A), 24) if A >= 24 else [rng.randrange(A) for _ in range(24)])
    c = reading(slips)
    def score(key, c, sl):
        return m.score_idx(key[c]) - LAM * np.count_nonzero(sl)
    cur = score(key, c, slips); best = (cur, key.copy(), c.copy(), slips.copy())
    for i in range(ITERS):
        T = 4.0 * (1 - i / ITERS) ** 2 + 0.03
        k2, s2, c2 = key, slips, c
        u = rng.random()
        if MODE in ('misread', 'homoslip') and u < 0.2:
            s2 = slips.copy(); p = rng.randrange(n)
            s2[p] = 0 if slips[p] else rng.choice((-2, -1, 1, 2) if BOTH else (-1, 1))
            if np.count_nonzero(s2) > K:
                continue
            c2 = reading(s2)
        elif MODE in ('homo', 'homoslip') and u < 0.4:
            k2 = key.copy(); k2[rng.randrange(24)] = rng.randrange(A)
            if np.bincount(k2, minlength=A).max() > 2:
                continue
        elif u < 0.5 and MODE not in ('homo', 'homoslip'):
            k2 = key.copy(); s = rng.randrange(24)
            free = [a for a in range(A) if a not in set(k2.tolist())]
            if not free:
                continue
            k2[s] = rng.choice(free)
        else:
            k2 = key.copy(); s, t = rng.randrange(24), rng.randrange(24); k2[s], k2[t] = k2[t], k2[s]
        sc = score(k2, c2, s2)
        if sc >= cur or rng.random() < math.exp((sc - cur) / T):
            key, slips, c, cur = k2, s2, c2, sc
            if cur > best[0]:
                best = (cur, key.copy(), c.copy(), slips.copy())
    return best[0] / n, ''.join(m.alpha[i] for i in best[1][best[2]]), int(np.count_nonzero(best[3]))


def make_controls(n_ctl, rng):
    from lang import lm, corpora
    mid = os.environ.get('DORA_MODEL', 'en-modern')
    if os.environ.get('DORA_TF'):              # controls in the same transformed form, from Elgar's letters
        t = tf_text(os.environ['DORA_TF'], open(os.path.join(HERE, 'src', 'elgar_register.txt'), encoding='utf-8').read())
    elif mid in ('en-modern', 'en-elgar'):
        t = lm.norm(open(os.path.join(HERE, 'src', 'elgar_register.txt'), encoding='utf-8').read(), 'modern', False)
    else:                                         # own-language controls: text from the model's corpus
        spec = lm.registry()[0][mid]
        t = lm.norm(corpora.text(spec['sources'])[:2_000_000], spec['norm'], False)
    out = []
    for j in range(n_ctl):
        p = rng.randrange(len(t) - 87); pt = t[p:p + 87]
        letters = sorted(set(pt)); cells = rng.sample(TOKS, 24)
        if len(letters) > 24:
            continue
        if MODE in ('homo', 'homoslip'):
            freq = sorted(letters, key=lambda ch: -pt.count(ch))[:6]
            spare = [c for c in cells if c not in cells[:len(letters)]]
            key = {ch: [cells[i % 24]] for i, ch in enumerate(letters)}
            for ch, extra in zip(freq, spare):
                key[ch].append(extra)
            sg = [rng.choice(key[ch]) for ch in pt]
            if MODE == 'homoslip':
                for q in rng.sample(range(87), K):
                    o, a = sg[q]; sg[q] = ((o + rng.choice((-1, 1))) % 8, a)
        else:
            key = {ch: cells[i % 24] for i, ch in enumerate(letters)}
            sg = [key[ch] for ch in pt]
            for q in rng.sample(range(87), K):
                o, a = sg[q]
                kind = os.environ.get('DORA_SLIP')
                if kind == 'both':
                    kind = rng.choice(('arcs', 'orient'))
                if kind == 'arcs':
                    sg[q] = (o, 1 if a != 1 else rng.choice((0, 2)))      # a neighbouring arc count
                else:
                    sg[q] = ((o + rng.choice((-1, 1))) % 8, a)
        out.append((sg, pt))
    return out


if __name__ == '__main__':
    rng = random.Random(33)
    ctf = next((a.split('=')[1] for a in sys.argv if a.startswith('--ct=')), 'ct.txt')
    ct = [((ord(t[0]) - 65), int(t[1]) - 1) for t in open(os.path.join(HERE, ctf)).read().split()]
    if '--nulls' in sys.argv:                      # shuffles of the same signs under the identical search
        targets = [(f'null {j}', [ct[i] for i in np.random.default_rng(j).permutation(len(ct))], None) for j in range(int(os.environ.get('DORA_NNULL', 4)))]
    else:
        targets = [(f'DORABELLA {ctf}', ct, None)]
        if '--noctl' not in sys.argv:
            targets += [(f'control {j}', sg, pt) for j, (sg, pt) in enumerate(make_controls(int(os.environ.get('DORA_NCTL', 4)), rng))]
    with Pool(max(1, (os.cpu_count() or 2) - 1)) as pool:
        for name, seq, truth in targets:
            res = pool.map(run, [(seq, 1000 * hash(name) % 100000 + r) for r in range(RESTARTS)])
            res.sort(reverse=True)
            sc, txt, e = res[0]
            acc = f'acc {np.mean([a == b for a, b in zip(txt, truth)]):.2f}' if truth else ''
            print(f'{MODE} K={K} {name:10s} best {sc:.3f} slips {e} {acc}  {txt}', flush=True)
