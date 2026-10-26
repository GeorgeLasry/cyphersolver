"""Gapped alignment of the f. 325r cipher block with its marginal decipherment, anchored on the key values of the two
glossed name groups (f. 325v 'messieurs de surich', f. 326r 'de monsieur de [?Sury]'), then extended by iteration:
an unanchored sign takes the letter it falls on most often (at least twice, 60% of its tokens) and the alignment is
run again until nothing changes.

Score per token: +3 on a letter its value predicts, -3 on another letter, 0 for a sign with no value; a sign may cover
two letters (-1 plus the same test on the pair) or be skipped as a null (-1.5); a margin letter may be skipped (-1.5,
the decipherer writing more than the cipher). Free gaps at both ends of the margin.

Control: the same procedure on random passages of the same length from the fr-henri4 corpus (lang/), n runs.

    python targets/fleury1585/realign.py [n_controls]
"""
import random, re, sys, pathlib
ROOT = pathlib.Path(__file__).resolve().parents[2]
sys.path.insert(0, str(ROOT))
HERE = pathlib.Path(__file__).resolve().parent
NULLS = {'/', '///', 'o', '·:', '∴', 'Do.', ':'}


def norm(t):
    t = t.lower().replace('j', 'i').replace('v', 'u')
    t = re.sub(r'[éèêë]', 'e', t)
    t = re.sub(r'[àâ]', 'a', t)
    return re.sub(r'[^a-z]', '', t)


def block():
    toks = []
    for l in (HERE / 'f325r_transcription.txt').read_text(encoding='utf8').splitlines():
        if l.startswith('#') or not l.strip(): continue
        toks += [t for t in l.split() if t not in NULLS]
    return toks


def margin():
    t = '\n'.join(l for l in (HERE / 'f325r_margin.txt').read_text(encoding='utf8').splitlines() if not l.startswith('#'))
    t = t.replace('[?]', ' ').replace('?', '')
    return norm(t)


def anchors():
    k = {}
    g1 = '7 C A@ X M Z 6 9 TRI L q+ A@ 6 OM M z Yx'.split()
    for s, c in zip(g1, 'messieursdesurich'):
        k[s] = c
    # f. 326r group, Brackx's alignment (issue #82, 25 Oct 2026): X M Z = s i e, A@ 6^ OM = s u r
    k.update({'X': 's', 'M': 'i', 'Z': 'e', 'A@': 's', '6^': 'u', 'OM': 'r'})
    return k


def align(toks, text, key):
    n, m = len(toks), len(text)
    NEG = -1e9
    D = [[NEG] * (m + 1) for _ in range(n + 1)]
    B = [[None] * (m + 1) for _ in range(n + 1)]
    for j in range(m + 1):
        D[0][j] = 0.0                      # free leading gap in the margin
    for i in range(1, n + 1):
        v = key.get(toks[i - 1])
        for j in range(m + 1):
            best, bk = D[i - 1][j] - 1.5, 'null'
            if j >= 1:
                c = text[j - 1]
                sc = D[i - 1][j - 1] + (0 if v is None else (3 if v == c else -3))
                if sc > best: best, bk = sc, 'one'
                sc = D[i][j - 1] - 1.5
                if sc > best: best, bk = sc, 'skip'
            if j >= 2:
                pair = text[j - 2:j]
                sc = D[i - 1][j - 2] - 1 + (0 if v is None else (3 if v == pair else -3))
                if sc > best: best, bk = sc, 'two'
            D[i][j], B[i][j] = best, bk
    j = max(range(m + 1), key=lambda x: D[n][x])     # free trailing gap
    score = D[n][j]
    pairs, i = [], n
    while i > 0:
        bk = B[i][j]
        if bk == 'null': pairs.append((toks[i - 1], None)); i -= 1
        elif bk == 'one': pairs.append((toks[i - 1], text[j - 1])); i -= 1; j -= 1
        elif bk == 'two': pairs.append((toks[i - 1], text[j - 2:j])); i -= 1; j -= 2
        else: j -= 1
    return score, pairs[::-1]


def extend(toks, text, key0, rounds=8):
    key = dict(key0)
    for _ in range(rounds):
        score, pairs = align(toks, text, key)
        votes = {}
        for s, c in pairs:
            if s in key0 or c is None or len(c) != 1: continue
            votes.setdefault(s, []).append(c)
        new = dict(key0)
        for s, cs in votes.items():
            top = max(set(cs), key=cs.count)
            if cs.count(top) >= 2 and cs.count(top) / len(cs) >= 0.6:
                new[s] = top
        if new == key: break
        key = new
    score, pairs = align(toks, text, key)
    hits = sum(1 for s, c in pairs if s in key0 and c == key0[s])
    misses = sum(1 for s, c in pairs if s in key0 and c is not None and c != key0[s])
    return score, key, pairs, hits, misses


def controls(n, length, seed=1):
    from lang import corpora
    corpus = norm(corpora.text(['fr-henri4']))
    rnd = random.Random(seed)
    return [corpus[p:p + length] for p in (rnd.randrange(0, len(corpus) - length) for _ in range(n))]


if __name__ == '__main__':
    nc = int(sys.argv[1]) if len(sys.argv) > 1 else 50
    toks, text, k0 = block(), margin(), anchors()
    s, key, pairs, h, mi = extend(toks, text, k0)
    print(f'tokens {len(toks)}, margin letters {len(text)}, anchored signs {len(k0)}')
    print(f'margin: score {s:.1f}, anchored tokens on their letter {h}, on another {mi}, signs added {len(key) - len(k0)}')
    out = []
    for c in controls(nc, len(text)):
        cs, _, _, ch, cm = extend(toks, c, k0)
        out.append((cs, ch, cm))
    out.sort()
    sc = [o[0] for o in out]
    print(f'controls n={nc}: score median {sc[len(sc)//2]:.1f}, best {sc[-1]:.1f}; margin beats {sum(x < s for x in sc)} of {nc}')
    print(f'controls anchored hits median {sorted(o[1] for o in out)[nc//2]}, best {max(o[1] for o in out)}')
    print('added:', {k: v for k, v in key.items() if k not in k0})
    line = ' '.join(f'{a}={b or "-"}' for a, b in pairs)
    print('alignment:', line)
