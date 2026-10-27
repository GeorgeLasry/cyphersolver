"""24 May 1655 passage: annealing against the shared Latin model (lang/, model 'la', 5-grams with spaces).

Review pass of 27 Oct 2026 (Claude, for Daniel Bourdeau). anneal.py scored with 4-grams built from a word list;
this script uses the repository's shared Latin model instead and tries two systems:

  mono   one-to-one letter substitution, digits left aside (as anneal.py)
  homo   the 4 Aug 1655 system: letters and digits are all cipher signs, several signs may share a plain letter
         (on 4 Aug the digits 5, 6, 9 were homophones of l, i, n); so 7, 865 and 73 are treated as words

Each mode first runs a matched control: a Latin sentence of the same shape enciphered the same way, with the same
number of signs. Score = Latin 5-gram log-probability + a word bonus from lang/lexicons/la.json.gz. Run from the
repository root or this folder:

    PYTHONUTF8=1 python targets/comenius1655/anneal_lm.py          # about 15 seconds
    PYTHONUTF8=1 python targets/comenius1655/anneal_lm.py --long   # 60 restarts x 20,000 steps, a few minutes
"""
import gzip, json, math, pathlib, random, sys

ROOT = pathlib.Path(__file__).resolve().parents[2]
sys.path.insert(0, str(ROOT))
from lang import lm  # noqa: E402

M = lm.load('la')                                   # order 5, spaces, 'latin' normalisation (no j v k y w)
ALPHA = M.alpha.strip()                             # 21 plain letters
SP = M.index[' ']
LEX = json.load(gzip.open(ROOT / 'lang' / 'lexicons' / 'la.json.gz', 'rt', encoding='utf-8'))
LEX = {w: n for w, n in LEX.items() if w.isalpha()}

MAY_MONO = 'lmqsxmyo gpdlmuoyqnotlses pnofeyprp ap pys pdyp xyopatus'
MAY_HOMO = 'lmqsxmyo 7 gpdlmuoyqnotlses pnofeyprp 865 ap 73 pys pdyp xyopatus'


def score(words_idx, key):
    x = [SP]
    for w in words_idx:
        x.extend(key[s] for s in w); x.append(SP)
    import numpy as np
    s = M.score_idx(np.array(x))
    txt = ''.join(M.alpha[i] for i in x).split()
    return s + sum(3 * math.log(1 + LEX.get(w, 0)) for w in txt if len(w) > 1), ' '.join(txt)


LONG = '--long' in sys.argv


def anneal(ct, homophonic, seed, restarts=20, iters=6000):
    if LONG: restarts, iters = 60, 20000
    rnd = random.Random(seed)
    syms = sorted(set(ct.replace(' ', '')))
    sid = {s: i for i, s in enumerate(syms)}
    words = [[sid[c] for c in w] for w in ct.split()]
    letters = [M.index[c] for c in ALPHA]
    out = []
    for _ in range(restarts):
        if homophonic:
            key = [rnd.choice(letters) for _ in syms]
        else:
            p = letters[:]; rnd.shuffle(p); key = p[:len(syms)]
        s0, d0 = score(words, key); T = 8.0
        for _ in range(iters):
            k2 = key[:]
            i = rnd.randrange(len(syms))
            if homophonic or rnd.random() < 0.3:
                new = rnd.choice(letters)
                if not homophonic and new in k2:          # keep it one-to-one: swap with the holder
                    j = k2.index(new); k2[i], k2[j] = k2[j], k2[i]
                else:
                    k2[i] = new
            else:
                j = rnd.randrange(len(syms)); k2[i], k2[j] = k2[j], k2[i]
            s1, d1 = score(words, k2)
            if s1 >= s0 or rnd.random() < math.exp((s1 - s0) / T):
                key, s0, d0 = k2, s1, d1
            T = max(0.2, T * 0.999)
        out.append((round(s0, 1), d0))
    return sorted(set(out), reverse=True)[:3]


def encipher(pt, homophonic, seed):
    """Random substitution; homophonic: each plain letter gets 1-3 signs from letters+digits, used in turn."""
    rnd = random.Random(seed)
    signs = list('abcdefghilmnopqrstuxyz0123456789'); rnd.shuffle(signs)
    if not homophonic:
        k = dict(zip(ALPHA, signs))
        return ' '.join(''.join(k[c] for c in w) for w in pt.split())
    used = sorted(set(pt.replace(' ', '')), key=lambda c: -pt.count(c))
    k, it = {}, iter(signs)
    for n, c in enumerate(used):
        k[c] = [next(it) for _ in range(3 if n < 3 else 2 if n < 6 else 1)]
    return ' '.join(''.join(rnd.choice(k[c]) for c in w) for w in pt.split())


CONTROLS = {False: 'gallia est omnis diuisa in partes tres quarum unam incolunt belgae',
            True: 'nihil certius quam poloniam periisse et papatum in illa nunc rex in castris est'}

if __name__ == '__main__':
    for homo, name in ((False, 'mono'), (True, 'homo')):
        pt = CONTROLS[homo]; ct = encipher(pt, homo, 11)
        n_ct = len(set(ct.replace(' ', '')))
        print(f'[{name}] control, {len(ct.replace(" ", ""))} signs, {n_ct} distinct: {ct}')
        for s, d in anneal(ct, homo, seed=1):
            print('   ', s, round(M.per_char(d), 2), d)
        print('    plaintext:', pt)
        may = MAY_HOMO if homo else MAY_MONO
        print(f'[{name}] 24 May 1655, {len(may.replace(" ", ""))} signs, {len(set(may.replace(" ", "")))} distinct: {may}')
        for s, d in anneal(may, homo, seed=5):
            print('   ', s, round(M.per_char(d), 2), d)
    print('per-char reference: Patera\'s 4 Aug plaintext', round(M.per_char('nihil certius quam poloniam periisse et papatum in illa'), 2))
