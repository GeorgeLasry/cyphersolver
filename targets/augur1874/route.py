"""Decipher the four Augur route-cipher telegrams of January 1874 (Newberry, Ayer MS 3008).

    python targets/augur1874/route.py            # prints the grids and the deciphered text of each telegram

System (recovered here; method described in the 18 Feb 1869 Fifth Military District letter, Ayer MS 3039 box 3
f. 153): the cipher words are written into rows of K words; the plaintext is read off down or up the columns in
the order the route gives. A first word that names a city (Baltic, Dresden) is the route indicator and stands
outside the grid. The last column ends in filler words (Texas place names). Words are not changed, except for
arbitraries (code words) standing for names or phrases, which this script leaves as they are.
"""
import os, re

HERE = os.path.dirname(os.path.abspath(__file__))

# telegram: (file, indicator word or None, K columns, route as (column 1-based, 'd' down | 'u' up), fillers)
TELEGRAMS = {
    '22': ('ct_22.txt', 'Baltic', 9, [(2, 'd'), (4, 'd'), (6, 'd'), (8, 'd'), (9, 'd'), (7, 'd'), (5, 'd'), (3, 'd'), (1, 'd')], 0),
    '29': ('ct_29.txt', 'Dresden', 7, [(1, 'd'), (7, 'u'), (6, 'u'), (2, 'd'), (5, 'u'), (4, 'd'), (3, 'd')], 3),
    '30': ('ct_30.txt', None, 7, [(1, 'd'), (7, 'u'), (4, 'd'), (6, 'u'), (2, 'd'), (5, 'u'), (3, 'd')], 1),
    '45': ('ct_45.txt', None, 7, [(1, 'd'), (7, 'u'), (4, 'd'), (6, 'u'), (2, 'd'), (5, 'u'), (3, 'd')], 3),
}


def words(fn):
    t = open(os.path.join(HERE, fn), encoding='utf-8').read()
    return ' '.join(l for l in t.splitlines() if l.strip() and not l.startswith('#')).split()


def decipher(key):
    fn, ind, K, route, fill = TELEGRAMS[key]
    w = words(fn)
    if ind:
        assert w[0] == ind, (key, w[0])
        w = w[1:]
    assert len(w) % K == 0, (key, len(w), K)
    rows = [w[i:i + K] for i in range(0, len(w), K)]
    out = []
    for c, d in route:
        col = [r[c - 1] for r in rows]
        out += col if d == 'd' else col[::-1]
    return rows, out[:len(out) - fill], out[len(out) - fill:]


if __name__ == '__main__':
    for k in TELEGRAMS:
        rows, plain, fillers = decipher(k)
        print(f'== telegram {k}: {len(rows)} rows x {len(rows[0])} columns')
        for r in rows:
            print('   ' + ' '.join(f'{x:13s}' for x in r))
        print('   plain:', ' '.join(plain))
        print('   fillers:', ' '.join(fillers) or '-')
