# Catalogue 641 (revenga1822): ciphertext-only recovery of the substitution key.
# Rewritten for the review (the first solver's working script was not kept); it uses no part of the key in
# decrypt.py except to compare with it at the end. Run from this folder:
#   python solve.py                 -> 4 restarts from random keys, seed 641
#   python solve.py --restarts 8 --seed 1
# Method: the cipher groups as transcribed, cipher a (the word space), the comma-like mark and unread signs
# removed, ll taken as one sign (decrypt.signs); every other sign is given one plain letter a-z; swap annealing
# (two values exchanged, unused letters included) against the repository's Spanish 4-gram model without spaces
# (lang/lm.py, es-modern). The best restart is printed with its agreement with KEY on sign occurrences.
# Contributed by WAINUT, 27 Oct 2026.
import math
import random
import sys
from pathlib import Path

import numpy as np

HERE = Path(__file__).resolve().parent
sys.path.insert(0, str(HERE.parent.parent))
sys.path.insert(0, str(HERE))
from lang import lm  # noqa: E402
import decrypt  # noqa: E402

LETTERS = 'abcdefghijklmnopqrstuvwxyz'


def kv(s):
    """KEY's value for a sign as one model letter (ll -> l, ñ -> n), '?' for a sign without value."""
    return decrypt.KEY.get(s, '?')[0].replace('ñ', 'n')


def cipher_stream(rows):
    """Concatenated sign stream, without word spaces, commas and unread signs."""
    out = []
    for _, _, c, _ in rows:
        out += [s for s in decrypt.signs(c) if s not in ('a', ',', '?')]
    return out


def anneal(model, x, n_signs, rnd, iters=40000, t0=2.0, t1=0.02):
    perm = list(range(26)); rnd.shuffle(perm)
    perm = np.array(perm)
    cur = model.score_idx(perm[x])
    best, best_perm = cur, perm.copy()
    for i in range(iters):
        t = t0 * (t1 / t0) ** (i / iters)
        a = rnd.randrange(n_signs); b = rnd.randrange(26)
        if a == b: continue
        perm[a], perm[b] = perm[b], perm[a]
        new = model.score_idx(perm[x])
        if new >= cur or rnd.random() < math.exp((new - cur) / t):
            cur = new
            if cur > best: best, best_perm = cur, perm.copy()
        else:
            perm[a], perm[b] = perm[b], perm[a]
    return best, best_perm


def main(argv):
    restarts = int(argv[argv.index('--restarts') + 1]) if '--restarts' in argv else 4
    seed = int(argv[argv.index('--seed') + 1]) if '--seed' in argv else 641
    rnd = random.Random(seed)
    model = lm.load('es-modern', order=4, spaces=False)
    rows = decrypt.groups()
    stream = cipher_stream(rows)
    types = sorted(set(stream))
    idx = {s: i for i, s in enumerate(types)}
    x = np.array([idx[s] for s in stream])
    n_chars = max(1, len(x) - model.order + 1)
    print(f'{len(stream)} cipher signs (word space, commas and unread signs left out), {len(types)} types')
    results = []
    for r in range(restarts):
        score, perm = anneal(model, x, len(types), rnd)
        key = {s: LETTERS[perm[i]] for s, i in idx.items()}
        agree = sum(key[s] == kv(s) for s in stream) / len(stream)
        results.append((score, key, agree))
        print(f'restart {r + 1}: {score / n_chars:.3f} per char, agreement with KEY on sign occurrences {agree:.3f}')
    score, key, agree = max(results, key=lambda t: t[0])
    print(f'best: {score / n_chars:.3f} per char; true KEY scores '
          f'{model.score_idx(np.array([LETTERS.index(kv(s)) for s in stream if s in decrypt.KEY])) / n_chars:.3f}')
    diff = sorted(s for s in types if key[s] != kv(s))
    print('signs where the best key differs from KEY (sign: solver / KEY, occurrences):',
          ', '.join(f'{s}: {key[s]}/{decrypt.KEY.get(s, "(none)")} ({stream.count(s)})' for s in diff) or 'none')
    full = dict(key, a=' ', **{',': ','})
    print('C01 with the best key:', ''.join(full.get(s, '?') for s in decrypt.signs(rows[0][2])))


if __name__ == '__main__':
    sys.stdout.reconfigure(encoding='utf-8')
    main(sys.argv[1:])
