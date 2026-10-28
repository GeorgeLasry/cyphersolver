"""Ciphertext-only attack on a one-part (alphabetical) word code.

The code numbers, sorted, are assumed to map to plaintext words in alphabetical
order (ascending, or descending with --desc). Each distinct number gets a word;
the assignment is annealed under a Spanish word-bigram model plus a prior that
a word's alphabetical position in a typical diplomatic vocabulary is roughly
proportional to its code number.

  python mono.py control [--seed N]   # encipher a Spanish passage the same way, try to solve it
  python mono.py letter  [--desc]     # run on ciphertext.tsv
"""
import bisect, collections, csv, math, os, random, re, sys, unicodedata

HERE = os.path.dirname(os.path.abspath(__file__))
CORP = os.path.join(HERE, '..', '..', 'lang', 'corpora')


def norm_words(text):
    t = unicodedata.normalize('NFD', text.lower())
    t = ''.join(c for c in t if not unicodedata.combining(c))
    return re.findall(r'[a-zñ]+', t)


def load_corpus():
    words = []
    for f in ('es-vasto-memorias.txt', 'es-gutenberg.txt'):
        words += norm_words(open(os.path.join(CORP, f), encoding='utf8', errors='ignore').read())
    return words


class Bigram:
    def __init__(self, words, vocab):
        vs = set(vocab)
        w = [x if x in vs else '<unk>' for x in words]
        self.uni = collections.Counter(w)
        self.bi = collections.Counter(zip(w, w[1:]))
        self.n = len(w)
        self.foll = collections.Counter(a for a, b in self.bi)
        self.types = collections.Counter(a for a, b in self.bi.keys())

    def lp(self, a, b):
        # Witten-Bell interpolation with the unigram
        pu = (self.uni[b] + 0.5) / (self.n + 0.5 * len(self.uni))
        c, t = self.foll[a], self.types[a]
        if c == 0:
            return math.log(pu)
        lam = c / (c + t)
        return math.log(lam * self.bi[(a, b)] / c + (1 - lam) * pu)


def anneal(toks, vocab, lm, ref_cdf, nmax, iters=2000000, seed=0, sigma=0.07, wprior=1.0, fixed=None):
    rnd = random.Random(seed)
    codes = sorted(set(toks))
    K, V = len(codes), len(vocab)
    pos = collections.defaultdict(list)
    for i, t in enumerate(toks):
        pos[t].append(i)
    # initial: spread by expected position
    exp_idx = []
    for c in codes:
        target = c / nmax
        exp_idx.append(bisect.bisect_left(ref_cdf, target))
    assign = []
    last = -1
    for j in range(K):
        x = max(last + 1, min(exp_idx[j], V - (K - j)))
        assign.append(x)
        last = x
    fixed = fixed or {}
    for j, c in enumerate(codes):
        if c in fixed:
            assign[j] = vocab.index(fixed[c])
    seq = [None] * len(toks)
    cj = {c: j for j, c in enumerate(codes)}
    for i, t in enumerate(toks):
        seq[i] = vocab[assign[cj[t]]]

    def prior(j, vi):
        d = (ref_cdf[vi] - codes[j] / nmax) / sigma
        return -0.5 * d * d * wprior

    def local(j, word):
        s = 0.0
        for i in pos[codes[j]]:
            if i > 0:
                s += lm.lp(seq[i - 1] if toks[i - 1] != codes[j] else word, word)
            if i + 1 < len(toks) and toks[i + 1] != codes[j]:
                s += lm.lp(word, seq[i + 1])
        return s

    T0, T1 = 3.0, 0.05
    for it in range(iters):
        T = T0 * (T1 / T0) ** (it / iters)
        j = rnd.randrange(K)
        if codes[j] in fixed:
            continue
        lo = assign[j - 1] + 1 if j > 0 else 0
        hi = assign[j + 1] - 1 if j + 1 < K else V - 1
        if hi <= lo:
            continue
        # propose near the current position mostly
        if rnd.random() < 0.7:
            nv = min(hi, max(lo, assign[j] + rnd.randint(-30, 30)))
        else:
            nv = rnd.randint(lo, hi)
        if nv == assign[j]:
            continue
        old = vocab[assign[j]]
        new = vocab[nv]
        d = local(j, new) + prior(j, nv) - local(j, old) - prior(j, assign[j])
        if d > 0 or rnd.random() < math.exp(d / T):
            assign[j] = nv
            for i in pos[codes[j]]:
                seq[i] = new
    total = sum(lm.lp(a, b) for a, b in zip(seq, seq[1:]))
    return dict(zip(codes, (vocab[a] for a in assign))), seq, total


def setup(vsize=6000):
    words = load_corpus()
    freq = collections.Counter(words)
    vocab = sorted(w for w, _ in freq.most_common(vsize))
    # reference distribution of a code book: the 900 commonest words, alphabetically
    book = set(w for w, _ in freq.most_common(900))
    cum, n = [], 0
    for w in vocab:
        n += w in book
        cum.append(n / len(book))
    return words, freq, vocab, cum


def control(seed=1, length=317, nmax=770):
    words, freq, vocab, cum = setup()
    rnd = random.Random(seed)
    # held-out passage from the Vasto memoirs, last tenth (also in training: say so)
    vasto = norm_words(open(os.path.join(CORP, 'es-vasto-memorias.txt'), encoding='utf8', errors='ignore').read())
    book = sorted(w for w, _ in freq.most_common(700))
    start = rnd.randrange(int(len(vasto) * 0.9), len(vasto) - 2000)
    plain = [w for w in vasto[start:start + 3 * length] if w in set(book)][:length]
    nums = sorted(rnd.sample(range(2, nmax), len(book)))
    code = dict(zip(book, nums))
    toks = [code[w] for w in plain]
    train = words[:len(words)]
    lm = Bigram(train, vocab)
    best = None
    for s in range(3):
        key, seq, tot = anneal(toks, vocab, lm, cum, nmax, seed=s)
        if best is None or tot > best[2]:
            best = (key, seq, tot)
    key, seq, tot = best
    ok = sum(a == b for a, b in zip(seq, plain))
    print(f'control seed {seed}: {ok}/{len(plain)} tokens right ({ok / len(plain):.0%}); '
          f'{sum(key[c] == w for w, c in code.items() if c in key)}/{len(key)} code words right')
    print(' '.join(plain[:60]))
    print(' '.join(seq[:60]))


def letter(desc=False, nmax=None):
    rows = list(csv.DictReader(open(os.path.join(HERE, 'ciphertext.tsv'), encoding='utf8'), delimiter='\t'))
    toks = [int(r['value'].strip('?')) for r in rows]
    nmax = nmax or 780
    if desc:
        toks = [nmax + 1 - t for t in toks]
    words, freq, vocab, cum = setup()
    lm = Bigram(words, vocab)
    best = None
    for s in range(4):
        key, seq, tot = anneal(toks, vocab, lm, cum, nmax, seed=s)
        print('run', s, round(tot, 1))
        if best is None or tot > best[2]:
            best = (key, seq, tot)
    key, seq, tot = best
    lines = collections.OrderedDict()
    for r, w in zip(rows, seq):
        lines.setdefault((r['folio'], r['line']), []).append(f"{r['value']}={w}")
    for k, v in lines.items():
        print(k[0], k[1], ' '.join(v))


if __name__ == '__main__':
    if sys.argv[1] == 'control':
        control(seed=int(sys.argv[3]) if len(sys.argv) > 3 else 1)
    else:
        letter(desc='--desc' in sys.argv)
