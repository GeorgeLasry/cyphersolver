"""Ciphertext-only substitution solve of the 1644 passage (letter 153), scored on lang pt-modern.

Hill-climb with restarts over a cipher->plain map (homophones allowed: several cipher letters may share a
plain letter). Word divisions are kept, so the LM sees spaces.
Usage: python solve153.py [file] [restarts]
"""
import os, sys, random, re
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', '..'))
from lang import lm

M = lm.load('pt-modern')
PLAIN = 'abcdefghijlmnopqrstuvxz'
FREQ = 'aeosrinmdtculpvgqfhbzjx'


def load(path):
    words = []
    for line in open(path, encoding='utf8'):
        line = line.strip()
        if not line or line.startswith('#'):
            continue
        words += line.split(':', 1)[1].split()
    return words


def score(text):
    return M.score(text) if hasattr(M, 'score') else M.per_char(text)


def run(words, restarts=40, iters=6000, seed=1):
    rnd = random.Random(seed)
    syms = sorted(set(''.join(words)))
    ct = ' '.join(words)
    best = (-1e18, None)
    for r in range(restarts):
        key = {s: rnd.choice(FREQ[:12]) for s in syms}
        dec = lambda k: ''.join(k.get(c, ' ') for c in ct)
        cur = score(dec(key))
        for i in range(iters):
            s = rnd.choice(syms)
            old = key[s]
            key[s] = rnd.choice(PLAIN)
            new = score(dec(key))
            if new >= cur:
                cur = new
            else:
                key[s] = old
        if cur > best[0]:
            best = (cur, dict(key))
            print(r, round(cur, 1), dec(key), flush=True)
    return best


if __name__ == '__main__':
    path = sys.argv[1] if len(sys.argv) > 1 else os.path.join(os.path.dirname(__file__), 'l153_cipher.txt')
    w = load(path)
    sc, key = run(w, int(sys.argv[2]) if len(sys.argv) > 2 else 40)
    print(sorted(key.items()))
