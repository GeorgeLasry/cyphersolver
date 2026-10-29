"""Controls for padgett_test.py: same dictionary-parse coverage statistic, several languages, three nulls."""
import os, sys, gzip, json, random
HERE = os.path.dirname(os.path.abspath(__file__))
toks = open(os.path.join(HERE, 'ct.txt')).read().split()
seq = list('ABCDEFGHIKLMNOPQRSTUWXYZ')
tab = {o + str(c): seq[i * 3 + c - 1] for i, o in enumerate('ABCDEFGH') for c in (1, 2, 3)}
LX = os.path.join(HERE, '..', '..', 'lang', 'lexicons')
import unicodedata
def fold(w): return ''.join(c for c in unicodedata.normalize('NFD', w) if c.isalpha() and ord(c) < 128).upper()
def load(lang, minc):
    d = json.load(gzip.open(os.path.join(LX, lang + '.json.gz'), 'rt', encoding='utf8'))
    ws = {fold(w) for w, c in d.items() if c >= minc}
    ws = {w for w in ws if len(w) >= 2}
    return ws
def mk(words, singles):
    words = set(words) | set(singles); ml = max(map(len, words))
    def cover(s):
        n = len(s); best = [0] * (n + 1)
        for i in range(n - 1, -1, -1):
            b = best[i + 1]
            for L in range(1, min(ml, n - i) + 1):
                if s[i:i + L] in words:
                    b = max(b, best[i + L] + L)
            best[i] = b
        return best[0]
    return cover
def key(tk, k=tab): return ''.join(k[t] for t in tk)
def run(lang, singles, minc, N, rng):
    cover = mk(load(lang, minc), singles)
    real = cover(key(toks))
    # null 1: symbol shuffle
    n1 = []
    for _ in range(N):
        t = toks[:]; rng.shuffle(t); n1.append(cover(key(t)))
    # null 2: random bijective key on the real symbol order
    syms = sorted(tab); n2 = []
    for _ in range(N):
        p = seq[:]; rng.shuffle(p); k = dict(zip(syms, p)); n2.append(cover(key(toks, k)))
    # null 3: shuffle that keeps adjacent-pair blocks: shuffle the 3 lines' internal order of bigram chunks (chunks of 2)
    n3 = []
    ch = [toks[i:i + 2] for i in range(0, 86, 2)] + [toks[86:]]
    for _ in range(N):
        c = ch[:]; rng.shuffle(c); t = [x for b in c for x in b]; n3.append(cover(key(t)))
    f = lambda a: ('mean %.1f p95 %d max %d P>=real %.4f' % (sum(a) / len(a), sorted(a)[int(.95 * len(a))], max(a), sum(x >= real for x in a) / len(a)))
    print(f'{lang:3s} real {real:2d} | symbol-shuffle {f(n1)} | random-key {f(n2)} | chunk-shuffle {f(n3)}', flush=True)
if __name__ == '__main__':
    rng = random.Random(7); N = int(sys.argv[1]) if len(sys.argv) > 1 else 600
    for lang, singles in [('es', ['Y', 'A', 'O', 'E', 'U', 'IR']), ('en', ['A', 'I', 'O']), ('fr', ['A', 'Y']), ('it', ['A', 'E', 'O', 'I']), ('la', ['A', 'E', 'O']), ('de', ['A', 'O'])]:
        if os.path.exists(os.path.join(LX, lang + '.json.gz')): run(lang, singles, 1, N, rng)
