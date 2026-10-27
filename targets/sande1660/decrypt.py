"""Cipher A of ANTT LMP liv. 1 (catalogue 390): decrypt transcription.txt with the recovered key, line by line.

    python decrypt.py                    writes the line-by-line decryption to stdout (decryption.txt is its output)
    python decrypt.py --controls         function-word controls: real key against permuted keys and shuffled groups

Standard library only. The key is in key.txt; it is repeated here so the script runs alone.
"""
import os
import random
import sys

HERE = os.path.dirname(os.path.abspath(__file__))

# number -> letter. Homophones: a (3, 24), e (1, 27), l (21, 36), r (20, 30), s (13, 41).
KEY = {1: 'e', 2: 'o', 3: 'a', 4: 'u', 5: 'i', 6: 'd', 7: 'm', 8: 'g', 9: 'b', 10: 'j', 11: 'p', 12: 'f', 13: 's',
       14: 'h', 15: 'c', 16: 'q', 18: 'n', 19: 't', 20: 'r', 21: 'l', 22: 'x', 24: 'a', 27: 'e', 30: 'r', 36: 'l',
       41: 's'}
# Numbers above 41 (61, 62, 63, 64, 65, 79, 102, 128, 132, 341) have no value; they are printed as [n].

# A fixed list of common Portuguese words, set before any decoding (the second reader's list), for the controls.
FUNCTION_WORDS = set((
    'que de o a os as do da dos das em nao com por se he e mas para muito tao todos elle ele esta estao sao me lhe '
    'no na nos nas ao sua seu tem como cousas cousa noso nosso grande este desta nada tudo sobre ha q o dito monsiur'
).split())


def load(path):
    lines = []
    with open(path, encoding='utf-8') as fh:
        for raw in fh:
            if not raw.startswith('@'):
                continue
            tag, body = raw.rstrip('\n').split(' ', 1)
            words = [[t.strip() for t in w.strip().split('.')] for w in body.split('|')]
            lines.append((tag, words))
    return lines


def dec_word(tokens, key=KEY):
    out = ''
    for t in tokens:
        if t.isdigit():
            n = int(t)
            out += key.get(n, '[%d]' % n)
        else:
            out += '[?]'
    return out


def decrypt(lines, key=KEY):
    return [(tag, [dec_word(w, key) for w in words]) for tag, words in lines]


def score(lines, key=KEY):
    words = [w for _, ws in decrypt(lines, key) for w in ws]
    return sum(1 for w in words if w in FUNCTION_WORDS), len(words)


def controls(lines, trials=2000, seed=1):
    hits, n = score(lines)
    print('real key: %d of %d words are in the function-word list' % (hits, n))
    rng = random.Random(seed)
    syms = sorted(KEY)
    vals = [KEY[s] for s in syms]
    tot = best = 0
    for _ in range(trials):
        v = vals[:]
        rng.shuffle(v)
        h, _ = score(lines, dict(zip(syms, v)))
        tot += h
        best = max(best, h)
    print('wrong keys (letter values permuted, %d trials): mean %.1f, max %d' % (trials, tot / trials, best))
    pool = [t for _, ws in lines for w in ws for t in w]
    tot = best = 0
    for _ in range(trials):
        p = pool[:]
        rng.shuffle(p)
        it = iter(p)
        shuffled = [(tag, [[next(it) for _ in w] for w in ws]) for tag, ws in lines]
        h, _ = score(shuffled)
        tot += h
        best = max(best, h)
    print('shuffled groups (real key, same word lengths, %d trials): mean %.1f, max %d' % (trials, tot / trials, best))


def main():
    lines = load(os.path.join(HERE, 'transcription.txt'))
    if '--controls' in sys.argv:
        controls(lines)
        return
    print('# Cipher A, LMP liv. 1: decryption line by line against transcription.txt (output of python decrypt.py).')
    print('# Key in key.txt. [n] = code group without a value; [?] = sign not read or blotted. Plaintext Portuguese.')
    print('# Each line: tag, the numbers, then the decryption word by word (spaces as on the page).')
    for (tag, words), (_, plain) in zip(lines, decrypt(lines)):
        print(tag + '  ' + ' | '.join('.'.join(w) for w in words))
        print(' ' * (len(tag) + 2) + ' '.join(plain))


if __name__ == '__main__':
    main()
