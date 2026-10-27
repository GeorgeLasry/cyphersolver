"""Jordan to "My Dearest Rachel" (Greenhow), 1861: the cipher original (NARA naId 6925618, catalogue 646) against
the clerk's clear copy (NARA naId 1634051 images 1-2, catalogue 645).

Applies the 1864 Greenhow key (NARA M1091 naId 62017285 image 0484; ../greenhow1861/key_1864.md) to the cipher groups
of the fragment, written as neutral shape labels (the labels of ../greenhow1861), and compares every sign with the
letter the clear copy has at that place. Signs marked '?' were not read securely and are shown but not scored.

Controls: 20,000 random substitution keys; the key shifted by 1, 2, 3 and 13 letters; the true key with the groups
assigned to the wrong copy words (20,000 derangements); whole groups exactly right, true key against random keys.

    python decode.py          (output kept in decode_output.txt; seeded, standard library only)
"""
import random

KEY = {'hk': 'A', 'b7': 'B', 'c3': 'C', 'cx': 'D', 'yf': 'E', 'tr': 'F', 'e8': 'G', 'cm': 'H', 'f4': 'I', 'o0': 'J',
       'n9': 'K', 'ls': 'L', 'dd': 'M', 'qm': 'N', 'f5': 'O', 'cc': 'P', 'q1': 'Q', 'ph': 'R', 'bx': 'S', 'dt': 'T',
       'e8s': 'U', 'zt': 'V', 'fl': 'W', 'ta': 'X', 'ys': 'Y', 'rr': 'Z'}

# (line, clear words before the group, signs, the clear copy's letters at those signs, the copy's word)
GROUPS = [
    ('L1',   'to get for me', 'o0? cm hk ph', '?HAR', "Hardee's (interlinear gloss 'h a r'; the leading O unexplained)"),
    ('L2',   '',              'c3 bx',        'CS',   'Tactics'),
    ('L3a',  '',              'yf fl?',       'EW',   'new'),
    ('L3b',  '',              'c3 f5 cc',     'COP',  'Copies'),
    ('L4',   '',              'bx c3 f5 dt dt', 'SCOTT', "Scott's"),
    ('L5a',  '',              'f4 c3 bx',     'ICS',  'Tactics'),
    ('L5b',  '',              'e8s? dd yf bx', 'UMES', 'volumes (U written as an 8 with a stroke)'),
    ('L6a',  '',              'cm hk qm bx',  'HANS', 'Mahans'),
    ('L6b',  '',              'tr f4 yf ls cx', 'FIELD', 'field'),
    ('L7',   '',              'tr f5 ph dt f4 tr f4 c3 hk dt f4 f5 qm', 'FORTIFICATION', 'fortifications'),
    ('L9',   '..ing of',      'bx? f5 e8s ls cx yf ph', 'SOULDER', 'Shoulder (first sign S or the sh digraph)'),
    ('L10a', '',              'hk? cc bx',    'APS',  'Straps'),
    ('L10b', 'for a',         'ls f4 yf',     'LIE',  'Lieutenant'),
    ('L11',  '',              'c3 f5',        'CO',   'Colonel (rest of the line too faint)'),
    ('R1',   'he in[?] 6[?] ,', 'ph f4 qm',   'RIN',  'bring'),
    ('R2a',  '',              'hk qm ys',     'ANY',  'any'),
    ('R2b',  'you',           'c3 hk qm e8',  'CANG', 'can get'),
    ('R3',   '',              'cm? f4 dd',    'HIM',  'him (first sign an arch with a dot)'),
    ('R6',   'These',         'b7 f5 f5',     'BOO',  'books'),
    ('R7',   'position as',   'ls f4 yf e8s', 'LIEU', 'Lieutenant'),
    ('R8a',  '',              'c3 f5 ls f5 qm yf ls', 'COLONEL', 'Colonel'),
    ('R8b',  'of',            'f4 qm?',       'IN',   'Infantry'),
]


def signs(s): return s.split()
def dec(s, key): return ''.join(key[t.rstrip('?')].lower() if t.endswith('?') else key[t] for t in signs(s))


def secure_pairs(groups):
    return [(t, e) for _, _, s, exp, _ in groups for t, e in zip(signs(s), exp) if not t.endswith('?') and e != '?']


def score(key, pairs): return sum(key[t] == e for t, e in pairs)


def main():
    pairs = secure_pairs(GROUPS)
    total_signs = sum(len(signs(g[2])) for g in GROUPS)
    print('== Decode with the 1864 key (lower case = uncertain sign, not scored) ==')
    for lab, ctx, s, exp, word in GROUPS:
        print(f'{lab:5s} {ctx:16s} {s:42s} -> {dec(s, KEY):14s} copy {exp:14s} {word}')
    print(f'signs in these groups: {total_signs}; securely read and scored: {len(pairs)}')
    print(f'TRUE KEY: {score(KEY, pairs)}/{len(pairs)} scored signs agree with the clear copy')

    names = list(KEY)
    random.seed(1861)
    s = best = 0
    for _ in range(20000):
        L = list(KEY.values()); random.shuffle(L); k = dict(zip(names, L))
        h = score(k, pairs); s += h; best = max(best, h)
    print(f'CONTROL 20,000 random keys: mean {s / 20000:.2f}/{len(pairs)}, best {best}/{len(pairs)}')
    for sh in (1, 2, 3, 13):
        k = {n: chr((ord(KEY[n]) - 65 + sh) % 26 + 65) for n in names}
        print(f'CONTROL key shifted +{sh}: {score(k, pairs)}/{len(pairs)}; FORTIFICATION group -> {dec(GROUPS[9][2], k)}')
    sg = [[t for t in signs(g[2])] for g in GROUPS]
    ex = [g[3] for g in GROUPS]
    s = best = 0
    for _ in range(20000):
        idx = list(range(len(GROUPS)))
        while True:
            random.shuffle(idx)
            if all(i != j for i, j in enumerate(idx)): break
        p = [(t, e) for i in range(len(GROUPS)) for t, e in zip(sg[i], ex[idx[i]]) if not t.endswith('?') and e != '?']
        h = score(KEY, p); s += h; best = max(best, h)
    print(f'CONTROL groups assigned to the wrong copy words (20,000 derangements): mean {s / 20000:.2f}, best {best}')

    def exact(key):
        n = 0
        for _, _, sg_, exp, _ in GROUPS:
            ts = [(t, e) for t, e in zip(signs(sg_), exp) if not t.endswith('?') and e != '?']
            n += all(key[t] == e for t, e in ts)
        return n
    random.seed(4646)
    mg = 0
    for _ in range(20000):
        L = list(KEY.values()); random.shuffle(L); mg = max(mg, exact(dict(zip(names, L))))
    print(f'CONTROL whole groups right on their secure signs: true key {exact(KEY)}/{len(GROUPS)}, '
          f'best of 20,000 random keys {mg}/{len(GROUPS)}')


if __name__ == '__main__':
    main()
