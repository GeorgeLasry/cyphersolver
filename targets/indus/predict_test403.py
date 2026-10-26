"""Set 403 (goal run loop 49): jointly fitted domain weights; per-group component weights for the subtype model.
Fixed split and split C. Writes results/predict_test403.md."""
import itertools
import math
import random
from collections import defaultdict

import loopkit as L
import rtools as R
from famlm import M3, fit3
from progress import MODEL


def domain_probs(train, test, kf, own_weights=False):
    random.seed(2026)
    w, _ = fit3(train, MODEL['keys'])
    glob = M3(train)
    groups = defaultdict(list)
    for t in train:
        groups[kf(t, L.META)].append(t)
    models = {}
    for k, v in groups.items():
        if len(v) >= 40:
            wk = w
            if own_weights and len(v) >= 100:
                random.seed(2026)
                wk, _ = fit3(v, MODEL['keys'])
            models[k] = (M3(v), wk)
    out = []
    for t in test:
        m, wk = models.get(kf(t, L.META), (glob, w))
        out.append([sum(wk[k] * r[k] for k in wk) for r in m.rows(t, MODEL['kn'])])
    return out


def mix(rows_list, ws):
    out = []
    for parts in zip(*rows_list):
        out.append([sum(w * p[j] for w, p in zip(ws, parts)) for j in range(len(parts[0]))])
    return out


def bits(rows):
    return sum(-math.log2(max(x, 1e-12)) for r in rows for x in r) / sum(len(r) for r in rows)


def sequential(train, test):
    return L.base_probs(train, test)


def joint(train, test):
    rnd = random.Random(2026)
    ls = list(train)
    rnd.shuffle(ls)
    k = int(0.8 * len(ls))
    itr, dv = ls[:k], ls[k:]

    def comps(a, b):
        return [L._plain(a, b)] + [domain_probs(a, b, kf) for kf, _ in L.BASE_DOMAINS]
    cd = comps(itr, dv)
    best = None
    grid = (0.0, 0.1, 0.2, 0.3)
    for ws in itertools.product(grid, repeat=len(L.BASE_DOMAINS)):
        w0 = 1 - sum(ws)
        if w0 < 0.2:
            continue
        b = bits(mix(cd, (w0,) + ws))
        if best is None or b < best[0]:
            best = (b, (w0,) + ws)
    return bits(mix(comps(train, test), best[1])), best[1]


def main():
    rd = R.Round('Four-hundred-and-third registered predictions: goal loop 49, jointly fitted and per-group weights', 'predict_test403')
    res1, res2 = [], []
    for name, (a, b) in (('fixed', L.splits()[0]), ('C', L.splits_c()[1])):
        s0 = bits(sequential(a, b))
        s1, ws = joint(a, b)
        res1.append((s0, s1))
        rd.say('- %s: sequential base %.4f; joint weights %s -> %.4f.' % (name, s0, ' '.join('%.1f' % x for x in ws), s1))
        sub = L.BASE_DOMAINS[2][0]
        p0 = domain_probs(a, b, sub)
        p1 = domain_probs(a, b, sub, own_weights=True)
        pl = L._plain(a, b)
        m0, m1 = bits(mix([pl, p0], (0.8, 0.2))), bits(mix([pl, p1], (0.8, 0.2)))
        res2.append((m0, m1))
        rd.say('- %s: plain + subtype (global weights) %.4f; with per-group weights %.4f.' % (name, m0, m1))
    rd.say()
    ok1 = res1[0][0] - res1[0][1] >= 0.005 and res1[1][1] < res1[1][0]
    ok2 = res2[0][0] - res2[0][1] >= 0.005 and res2[1][1] < res2[1][0]
    rd.rec('JW1', 'jointly fitted weights lower S (0.005 fixed, any on C)', '; '.join('%.4f -> %.4f' % r for r in res1), ok1)
    rd.rec('JW2', 'per-group component weights lower S for the subtype model', '; '.join('%.4f -> %.4f' % r for r in res2), ok2)
    rd.rec('P', 'progress rule: either holds', 'JW1 %s, JW2 %s' % (ok1, ok2), ok1 or ok2)
    rd.finish()


if __name__ == '__main__':
    main()
