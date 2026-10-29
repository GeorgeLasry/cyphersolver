"""Padgett 2025 claim: the notebook key turns the Dorabella tokens into a string holding Spanish words
(peca y ir cerre se es sed ser = 22 of 87 chars). Check the words are really there, then ask how often shuffles
of the same symbols get the same Spanish coverage under the same key (best non-overlapping dictionary parse)."""
import os, sys, gzip, json, random
sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__)), '..', '..'))
HERE = os.path.dirname(os.path.abspath(__file__))
toks = open(os.path.join(HERE, 'ct.txt')).read().split()
seq = list('ABCDEFGHIKLMNOPQRSTUWXYZ')
tab = {o + str(c): seq[i * 3 + c - 1] for i, o in enumerate('ABCDEFGH') for c in (1, 2, 3)}
lex = json.load(gzip.open(os.path.join(HERE, '..', '..', 'lang', 'lexicons', 'es.json.gz'), 'rt', encoding='utf8'))
MINC = int(sys.argv[1]) if len(sys.argv) > 1 else 20
words = {w.upper() for w, c in lex.items() if c >= MINC and (len(w) >= 2 or w == 'y')}
words |= {'Y','IR','SE','ES','ED'}
maxlen = max(map(len, words))
def cover(s):
    n = len(s); best = [0] * (n + 1); nw = [0] * (n + 1)
    for i in range(n - 1, -1, -1):
        b, k = best[i + 1], nw[i + 1]
        for L in range(1, min(maxlen, n - i) + 1):
            if s[i:i + L] in words:
                v = best[i + L] + L
                if v > b or (v == b and nw[i + L] + 1 < k): b, k = v, nw[i + L] + 1
        best[i], nw[i] = b, k
    return best[0], nw[0]
def key(tk): return ''.join(tab[t] for t in tk)
real = key(toks)
print(len(words), 'words; real string:', real)
for w in 'PECA Y IR CERRE SE ES SED SER'.split(): print(w, w in words, end=' | ')
print()
rc, rn = cover(real)
print('Dorabella: covered', rc, 'of 87 by', rn, 'words')
rng = random.Random(1)
N = 3000
sh = []
for _ in range(N):
    t = toks[:]; rng.shuffle(t); sh.append(cover(key(t))[0])
sh.sort()
print('shuffles (same symbols): mean %.1f, median %d, 95th %d, max %d; P(>= real) = %.4f' % (
    sum(sh) / N, sh[N // 2], sh[int(.95 * N)], sh[-1], sum(x >= rc for x in sh) / N))
# line-preserving shuffle and reversed reading
rv = cover(real[::-1])[0]; print('reversed string covers', rv)
# Padgett's specific claim: those 8 words in that order as separate substrings
need = ['PECA', 'Y', 'IR', 'CERRE', 'SE', 'ES', 'SED', 'SER']
def inorder(s):
    p = 0
    for w in need:
        j = s.find(w, p)
        if j < 0: return False
        p = j + len(w)
    return True
print('8 words in order, disjoint, in real string:', inorder(real))
hit = 0
for _ in range(20000):
    t = toks[:]; rng.shuffle(t)
    hit += inorder(key(t))
print('same in shuffles: %d / 20000' % hit)
# any 8 words of the lexicon with total length 22 is easy: median number of words of len>=3 covered
