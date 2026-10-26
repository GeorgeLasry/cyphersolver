"""Three-hundred-and-fifty-first registered prediction set (PREDICTIONS.md, DM1-DM5): decipherment loop 176, every drawn
mark from Parpola's descriptions (devices.py pairs, cage and jar strokes left out). Writes results/predict_test351.md."""
import math
import random
from collections import Counter, defaultdict

import rtools as R
from devices import pairs

JAR = {'741', '742', '744', '745', '746'}


def pos(t, i):
    if all(g in ('400', '90') for g in t[i + 1:]):
        return 2
    return 0 if i == 0 else 1


def toks(lines, S):
    return [pos(t, i) for t in lines for i, g in enumerate(t) if g in S]


def chi(a, b):
    n = len(a) + len(b)
    if not a or not b:
        return 0.0
    tot = 0.0
    for k in range(3):
        col = a.count(k) + b.count(k)
        for x in (a, b):
            e = col * len(x) / n
            if e:
                tot += (x.count(k) - e) ** 2 / e
    return tot


def perm_sum(P, lines, rnd, n=1000):
    data = [(toks(lines, p['gm']), toks(lines, p['gb'])) for p in P]
    obs = sum(chi(a, b) for a, b in data)
    ge = 0
    for _ in range(n):
        s = 0.0
        for a, b in data:
            z = a + b
            rnd.shuffle(z)
            s += chi(z[:len(a)], z[len(a):])
        ge += s >= obs
    return obs, (ge + 1) / (n + 1), data


def fin_p(a, b, rnd, n=1000):
    fa = lambda x: sum(v == 2 for v in x) / len(x)
    obs = abs(fa(a) - fa(b))
    z = a + b
    ge = 0
    for _ in range(n):
        rnd.shuffle(z)
        ge += abs(fa(z[:len(a)]) - fa(z[len(a):])) >= obs
    return (ge + 1) / (n + 1), fa(a) - fa(b)


def main():
    rnd = random.Random(351)
    A, B, rowsA, recs, F = R.load_all()
    DA, DB = sorted({tuple(t) for t in A}), sorted({tuple(t) for t in B})
    P = [p for p in pairs() if p['type'] != 'cage' and not p['gm'] <= JAR]
    rd = R.Round('Three-hundred-and-fifty-first registered predictions: decipherment loop 176, every drawn mark', 'predict_test351')
    rd.say('- %d pairs (cage and jar strokes left out).' % len(P))
    rd.say()
    oa, pa, data_a = perm_sum(P, DA, rnd)
    rd.rec('DM1', 'marks change position on A', 'summed chi-square %.1f, p = %.4f' % (oa, pa), pa < 0.05)
    ob, pb, data_b = perm_sum(P, DB, rnd)
    rd.rec('DM2', 'the same on B', 'summed chi-square %.1f, p = %.4f' % (ob, pb), pb < 0.05)
    DL = DA + DB
    prev = defaultdict(Counter)
    for t in DL:
        for i in range(1, len(t)):
            prev[t[i]][t[i - 1]] += 1

    def vec(S):
        v = Counter()
        for g in S:
            v.update(prev[g])
        return v

    def cos(va, vb):
        num = sum(va[k] * vb[k] for k in va)
        den = math.sqrt(sum(x * x for x in va.values())) * math.sqrt(sum(x * x for x in vb.values()))
        return num / den if den else 0.0
    use = [p for p in P if vec(p['gm']) and vec(p['gb'])]
    obs = sum(cos(vec(p['gm']), vec(p['gb'])) for p in use) / len(use)
    signs = [g for g in prev if prev[g]]
    ge = 0
    for _ in range(1000):
        ge += sum(cos(vec(p['gm']), prev[rnd.choice(signs)]) for p in use) / len(use) >= obs
    pc = (ge + 1) / 1001
    rd.rec('DM3', 'marks attach to the same stems', 'mean cosine %.3f over %d pairs, p = %.4f' % (obs, len(use), pc), pc < 0.05)
    rows, agree, tested = [], 0, 0
    for p, (a, b), (a2, b2) in zip(P, data_a, data_b):
        if len(a) < 3 or len(b) < 3:
            continue
        pp, d = fin_p(list(a), list(b), rnd)
        fa = lambda x: sum(v == 2 for v in x) / len(x)
        rep = ''
        if pp < 0.05 and len(a2) >= 5 and len(b2) >= 5:
            d2 = fa(a2) - fa(b2)
            tested += 1
            agree += (d2 > 0) == (d > 0)
            rep = 'B %+.2f' % d2
        rows.append('%s<%s %s (%s): A n %d/%d, final %.2f vs %.2f, p %.3f %s' % (
            p['marked'], p['base'], p['type'], p['extra'][:40], len(a), len(b), fa(a), fa(b), pp, rep))
    rd.say('### pairs with 3+ A tokens each side')
    for r in rows:
        rd.say('- ' + r)
    rd.say()
    rd.rec('DM4', 'final-rate shifts replicate on B', '%d of %d A-significant pairs shift the same way on B' % (agree, tested),
           tested > 0 and agree / tested >= 2 / 3)
    rd.rec('DM5', 'progress rule', 'DM1 %s, DM2 %s' % (pa < 0.05, pb < 0.05), pa < 0.05 and pb < 0.05)
    open('results/predict_test351.md', 'w', encoding='utf-8').write('\n'.join(rd.lines) + '\n')


if __name__ == '__main__':
    main()
