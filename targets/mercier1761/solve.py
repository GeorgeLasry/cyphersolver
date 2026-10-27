"""Ciphertext-only attack on ANOM C8 A 64 f. 1 (Martinique, 12 June 1761).

Model: a two-part nomenclator. Each code group stands for one entry of a vocabulary; the vocabulary is the printed
Navy form used for Martinique in 1765 (key1765_ennery.tsv, 800 entries), taken as a proxy for the 1761 form.
Simulated annealing over the map group -> entry (one entry per group), scored by the shared French LM
(fr-modern, order 5, no spaces) on the whole letter stream, clear passages included, plus a unigram prior on
entries estimated by segmenting French text into vocabulary units.

  python solve.py control [seed]     encipher held-out 1757 French (d'Affry) in the same system and shape, solve it
  python solve.py letter [seed]      solve the letter
"""
import math, os, random, re, sys, unicodedata
from collections import Counter

import numpy as np

HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, os.path.join(HERE, '..', '..'))
from lang import lm  # noqa: E402


def norm(s):
    s = s.replace('&', 'et')
    s = ''.join(c for c in unicodedata.normalize('NFD', s.lower()) if unicodedata.category(c) != 'Mn')
    return re.sub(r'[^a-z]', '', s)


def load_vocab():
    units = []
    for line in open(os.path.join(HERE, 'key1765_ennery.tsv'), encoding='utf8'):
        if not line[:1].isdigit():
            continue
        num, val = line.rstrip('\n').split('\t')
        base = norm(val.split(',')[0].replace('?', ''))
        if base:
            units.append(base)
    return sorted(set(units))


def segmenter(units, prior=None):
    """Min-cost segmentation of an unspaced string into units (cost = -log prior, or 1 per unit)."""
    by_first = {}
    for i, u in enumerate(units):
        by_first.setdefault(u[0], []).append(i)
    cost = [(-math.log(prior[i]) if prior is not None else 1.0) for i in range(len(units))]
    maxlen = max(map(len, units))

    def seg(s):
        n = len(s)
        best = [math.inf] * (n + 1)
        back = [None] * (n + 1)
        best[0] = 0.0
        for i in range(n):
            if best[i] == math.inf:
                continue
            for j in by_first.get(s[i], ()):
                u = units[j]
                if s.startswith(u, i):
                    c = best[i] + cost[j]
                    if c < best[i + len(u)]:
                        best[i + len(u)], back[i + len(u)] = c, (i, j)
        if best[n] == math.inf:
            return None
        out, k = [], n
        while k:
            i, j = back[k]
            out.append(j)
            k = i
        return out[::-1]
    return seg


def unit_prior(units):
    """Unigram prior over units: segment held-in French (fr-gutenberg) word by word, two passes."""
    text = open(os.path.join(HERE, '..', '..', 'lang', 'corpora', 'fr-gutenberg.txt'), encoding='utf8',
                errors='ignore').read()[2_000_000:3_500_000]
    words = [norm(w) for w in text.split()]
    words = [w for w in words if w]
    prior = None
    for _ in range(2):
        seg = segmenter(units, prior)
        c = Counter()
        cache = {}
        for w in words:
            if w not in cache:
                cache[w] = seg(w)
            if cache[w]:
                c.update(cache[w])
        tot = sum(c.values()) + 0.5 * len(units)
        prior = [(c[i] + 0.5) / tot for i in range(len(units))]
    return prior


def parse_letter():
    """Segments in order: ('clear', text) or ('code', [groups])."""
    segs = []
    t = open(os.path.join(HERE, 'transcription.txt'), encoding='utf8').read()
    body = []
    for line in t.splitlines():
        if line.startswith('#') or line.startswith('[img'):
            continue
        body.append(line.split(':', 1)[1] if re.match(r'(l|c)\d+:', line) else line)
    s = ' '.join(body).replace('+', '').replace('?', '')
    for m in re.finditer(r'\{([^}]*)\}|(\d+)', s):
        if m.group(1) is not None:
            if 'other hand' in m.group(1):
                continue
            segs.append(('clear', norm(m.group(1))))
        else:
            if segs and segs[-1][0] == 'code':
                segs[-1][1].append(m.group(2))
            else:
                segs.append(('code', [m.group(2)]))
    return segs


def make_control(segs, units, prior, seed):
    """Encipher held-out 1757 French in the same shape: same code-run lengths, same clear lengths."""
    rng = random.Random(seed)
    text = open(os.path.join(HERE, '..', 'affry1757', 'corpus_fr.txt'), encoding='utf8').read()
    text = norm(text)
    seg = segmenter(units, prior)
    start = rng.randrange(0, len(text) - 20000)
    pos, out, truth = start, [], {}
    numbers = rng.sample(range(1, 1000), len(units))
    code_of = {}
    for kind, val in segs:
        if kind == 'clear':
            out.append(('clear', text[pos:pos + len(val)]))
            pos += len(val)
        else:
            need, toks = len(val), []
            while len(toks) < need:
                piece = text[pos:pos + 40]
                s = seg(piece)
                if s is None:          # drop a char nothing in the vocabulary covers
                    pos += 1
                    continue
                s = s[:-1] if len(s) > 1 else s   # last unit may be cut by the window
                for j in s:
                    pos += len(units[j])
                    toks.append(j)
                    if len(toks) == need:
                        break
            grp = []
            for j in toks:
                if j not in code_of:
                    code_of[j] = str(numbers[len(code_of)])
                truth[code_of[j]] = j
                grp.append(code_of[j])
            out.append(('code', grp))
    return out, truth


class Solver:
    def __init__(self, segs, units, prior, model, lam=1.0, rng=None, words=None, beta=0.0):
        self.units, self.model, self.lam = units, model, lam
        self.words, self.beta = words, beta
        self.rng = rng or random.Random(0)
        self.enc = [model.encode(u) for u in units]
        self.logp = np.log(np.array(prior))
        self.types = sorted({g for k, v in segs if k == 'code' for g in v}, key=int)
        self.tix = {g: i for i, g in enumerate(self.types)}
        self.pieces, self.tok_type = [], []
        for k, v in segs:
            if k == 'clear':
                self.pieces.append(('c', model.encode(v)))
            else:
                for g in v:
                    self.pieces.append(('t', self.tix[g]))
                    self.tok_type.append(self.tix[g])
        self.count = Counter(self.tok_type)

    def stream(self, a):
        return np.concatenate([p if k == 'c' else self.enc[a[p]] for k, p in self.pieces])

    def score(self, a):
        s = self.model.score_idx(self.stream(a))
        s += self.lam * sum(self.count[t] * self.logp[a[t]] for t in range(len(self.types)))
        if self.beta:
            s += self.beta * self.words.score(self.plain(a))
        return s

    def init(self):
        # frequency rank matching: most frequent groups to the most probable units
        order_t = sorted(range(len(self.types)), key=lambda t: -self.count[t])
        order_u = sorted(range(len(self.units)), key=lambda u: -self.logp[u])
        a = [0] * len(self.types)
        for t, u in zip(order_t, order_u):
            a[t] = u
        return a

    def anneal(self, iters=200_000, t0=8.0, t1=0.2, a=None, log=None):
        rng = self.rng
        a = list(a or self.init())
        used = Counter(a)
        cur = self.score(a)
        best, besta = cur, list(a)
        T = len(self.types)
        U = len(self.units)
        for it in range(iters):
            temp = t0 * (t1 / t0) ** (it / iters)
            if rng.random() < 0.5:
                t, u2 = rng.randrange(T), rng.randrange(U)
                if used[u2]:
                    continue
                old = a[t]
                a[t] = u2
                new = self.score(a)
                if new >= cur or rng.random() < math.exp((new - cur) / temp):
                    cur = new
                    used[old] -= 1
                    used[u2] += 1
                else:
                    a[t] = old
            else:
                t1_, t2_ = rng.randrange(T), rng.randrange(T)
                if t1_ == t2_:
                    continue
                a[t1_], a[t2_] = a[t2_], a[t1_]
                new = self.score(a)
                if new >= cur or rng.random() < math.exp((new - cur) / temp):
                    cur = new
                else:
                    a[t1_], a[t2_] = a[t2_], a[t1_]
            if cur > best:
                best, besta = cur, list(a)
            if log and it % max(1, iters // 50) == 0:
                log(f'  it {it} T={temp:.2f} cur={cur:.1f} best={best:.1f}')
        return best, besta

    def render(self, a, segs):
        out = []
        for k, v in segs:
            if k == 'clear':
                out.append('{' + v + '}')
            else:
                out.append(' '.join(f'{g}={self.units[a[self.tix[g]]]}' for g in v))
        return '\n'.join(out)

    def plain(self, a):
        return ''.join(self.units[a[t]] for t in self.tok_type)


def main():
    mode = sys.argv[1]
    seed = int(sys.argv[2]) if len(sys.argv) > 2 else 1
    iters = int(sys.argv[3]) if len(sys.argv) > 3 else 200_000
    beta = float(sys.argv[4]) if len(sys.argv) > 4 else 0.0
    words = None
    if beta:
        import wordscore
        words = wordscore.WordScorer(wordscore.load_words())
    units = load_vocab()
    prior = unit_prior(units)
    model = lm.load('fr-modern', order=5, spaces=False)
    segs = parse_letter()
    ntok = sum(len(v) for k, v in segs if k == 'code')
    print(f'vocab {len(units)} units; letter {ntok} code tokens, {len(segs)} segments')
    if mode == 'control':
        segs, truth = make_control(segs, units, prior, seed)
        ntok = sum(len(v) for k, v in segs if k == 'code')
        print(f'control: {ntok} tokens, {len(truth)} types')
    s = Solver(segs, units, prior, model, rng=random.Random(seed), words=words, beta=beta)
    best, a = s.anneal(iters=iters, log=print)
    print('best', round(best, 1), 'per-char', round(model.score_idx(s.stream(a)) / len(s.stream(a)), 3))
    out = os.path.join(HERE, f'run_{mode}_{seed}' + (f'_b{beta:g}' if beta else '') + '.txt')
    with open(out, 'w', encoding='utf8') as f:
        f.write(s.render(a, segs) + '\n')
        if mode == 'control':
            ok = sum(1 for t in s.tok_type if a[t] == truth[s.types[t]])
            oks = sum(1 for t in s.tok_type if units[a[t]] == units[truth[s.types[t]]])
            f.write(f'\nTRUTH tokens correct {ok}/{len(s.tok_type)} = {ok / len(s.tok_type):.1%}\n')
            f.write('truth plain: ' + ''.join(units[truth[s.types[t]]] for t in s.tok_type) + '\n')
            ta = [truth[g] for g in s.types]
            f.write(f'score found {best:.1f}  truth {s.score(ta):.1f}\n')
            print(f'score found {best:.1f}  truth {s.score(ta):.1f}')
            print(f'control: tokens correct {ok}/{len(s.tok_type)} = {ok / len(s.tok_type):.1%} (string-equal {oks})')
        f.write('solver plain: ' + s.plain(a) + '\n')
    print('wrote', out)
    print(s.plain(a)[:600])


if __name__ == '__main__':
    main()
