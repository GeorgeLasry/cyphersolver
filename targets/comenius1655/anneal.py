"""Ciphertext-only attack on the 24 May 1655 passage, with a matched control.

A one-to-one letter substitution (word division kept, digits left aside) is annealed against a Latin letter
4-gram model plus a word bonus, both built from the repository's Latin lexicon (lang/lexicons/la.json.gz, word
counts from 27 Latin texts). The same annealer is first run on two synthetic controls: Latin sentences of 50 and
56 letters enciphered with a random substitution, the same length as the 24 May passage (50 letters).

    python anneal.py            # controls, then the 24 May passage (about a minute)

Standard library only.
"""
import gzip, json, math, pathlib, random, re, collections

ROOT = pathlib.Path(__file__).resolve().parents[2]
LEX = json.load(gzip.open(ROOT / 'lang' / 'lexicons' / 'la.json.gz', 'rt', encoding='utf-8'))
LEX = {w: n for w, n in LEX.items() if w.isalpha()}

Q = collections.Counter()
for w, n in LEX.items():
    s = ' ' + w + ' '
    for i in range(len(s) - 3): Q[s[i:i + 4]] += n
N = sum(Q.values())
ALPHA = 'abcdefghilmnopqrstuxyz'      # Latin alphabet of the lexicon (j=i, v=u; k, w rare)


def lp(g): return math.log((Q.get(g, 0) + 0.05) / N)


def decode(ct, k): return ' '.join(''.join(k.get(c, c) for c in w) for w in ct.split())


def score(ct, k):
    d = ' ' + decode(ct, k) + ' '
    return sum(lp(d[i:i + 4]) for i in range(len(d) - 3)) + sum(4 * math.log(1 + LEX.get(w, 0)) for w in d.split() if len(w) > 1)


def anneal(ct, seed, restarts=30, iters=12000):
    rnd = random.Random(seed)
    cl = sorted(set(c for c in ct if c.isalpha()))
    best = []
    for _ in range(restarts):
        perm = list(ALPHA); rnd.shuffle(perm)
        k = dict(zip(cl, perm)); spare = perm[len(cl):]
        s0, T = score(ct, k), 6.0
        for _ in range(iters):
            k2 = dict(k); c = rnd.choice(cl); used = None
            if spare and rnd.random() < 0.3:
                j = rnd.randrange(len(spare)); used = (j, k[c]); k2[c] = spare[j]
            else:
                c2 = rnd.choice(cl); k2[c], k2[c2] = k[c2], k[c]
            s1 = score(ct, k2)
            if s1 >= s0 or rnd.random() < math.exp((s1 - s0) / T):
                if used: spare[used[0]] = used[1]
                k, s0 = k2, s1
            T = max(0.15, T * 0.9995)
        best.append((round(s0, 1), decode(ct, k)))
    return sorted(set(best), reverse=True)[:3]


def encipher(pt, seed):
    rnd = random.Random(seed)
    p = list(ALPHA); rnd.shuffle(p)
    return ' '.join(''.join(dict(zip(ALPHA, p))[c] for c in w) for w in pt.split())


CONTROLS = ['gallia est omnis diuisa in partes tres quarum unam incolunt belgae',
            'omnia uincit amor et nos cedamus amori dixit poeta antiquus']
MAY = 'Lmqsxmyo 7 Gpdlmuoyqnotlses Pnofeyprp 865 ap 73 pys pdyp Xyopatus'

if __name__ == '__main__':
    for i, pt in enumerate(CONTROLS):
        ct = encipher(pt, 7 + i)
        print(f'control {i + 1} ({len(pt.replace(" ", ""))} letters): {ct}')
        for s, d in anneal(ct, seed=i + 1): print('   ', s, d)
        print('    plaintext:', pt)
    ct = re.sub(r'[^a-z ]', '', MAY.lower()); ct = re.sub(' +', ' ', ct).strip()
    print(f'24 May 1655 ({len(ct.replace(" ", ""))} letters): {ct}')
    for s, d in anneal(ct, seed=5): print('   ', s, d)
