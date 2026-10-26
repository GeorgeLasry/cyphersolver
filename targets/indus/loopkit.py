"""Harness for the goal-run loops (from set 355, 25 Oct 2026): the registered S model (progress.MODEL) gives each test
token a probability; an extra source gives its own; they are mixed linearly, the weight fitted on an inner dev split of
the training lines only. Scored on the fixed 80/20 split (progress.data) and A -> B (B lines not in A), as set 286.
An extra is built as extra(train_lines, META) -> f(line, i) = probability of the token at i (i == len(line): end)."""
import math
import random
from collections import Counter, defaultdict

import rtools as R
from famlm import M3, fit3
from progress import MODEL, data
from signs import load

LAMS = (0.0, 0.02, 0.05, 0.1, 0.15, 0.2, 0.3, 0.4, 0.5)


def build_meta():
    A, B, rowsA, recs, F = R.load_all()
    meta = defaultdict(Counter)
    others = {}
    for r in list(rowsA) + list(load(only_m77=True)) + list(F):
        lines = [tuple(ln) for ln in r['seq'] if ln]
        ty = (r.get('type') or '').split(':')[0]
        for ln in lines:
            meta[ln][(r.get('site') or '', ty, (r.get('motif') or '').split(':')[0])] += 1
            if len(lines) > 1 and ln not in others:
                others[ln] = [x for x in lines if x != ln]
    return {ln: c.most_common(1)[0][0] for ln, c in meta.items()}, others


META, OTHERS = build_meta()


def base_probs(train, test):
    w, _ = fit3(train, MODEL['keys'])
    m = M3(train)
    return [[sum(w[k] * r[k] for k in w) for r in m.rows(t, MODEL['kn'])] for t in test]


def _bits(pb, pe, lam):
    n = s = 0
    for row_b, row_e in zip(pb, pe):
        for a, b in zip(row_b, row_e):
            s -= math.log2(max((1 - lam) * a + lam * b, 1e-12))
            n += 1
    return s / n


def evaluate(train, test, extra, seed=2026):
    rnd = random.Random(seed)
    ls = list(train)
    rnd.shuffle(ls)
    k = int(0.8 * len(ls))
    itr, dv = ls[:k], ls[k:]
    f = extra(itr, META)
    pb = base_probs(itr, dv)
    pe = [[f(t, i) for i in range(len(t) + 1)] for t in dv]
    lam = min(LAMS, key=lambda l: _bits(pb, pe, l))
    f = extra(train, META)
    pb = base_probs(train, test)
    pe = [[f(t, i) for i in range(len(t) + 1)] for t in test]
    return _bits(pb, pe, 0.0), _bits(pb, pe, lam), lam


def splits():
    A, B, *_ = R.load_all()
    DL, tr, te = data()
    DA = sorted({tuple(t) for t in A})
    DB = sorted({tuple(ln) for r in load(only_m77=True) for ln in r['seq'] if ln} - set(DA))
    return (tr, te), (DA, DB)


def unigram_given(keyfn, alpha=5.0):
    """Unigram over signs + end, conditioned on keyfn(line, META), backed off to the global unigram."""
    def extra(train, meta):
        glob = Counter(g for t in train for g in list(t) + ['</s>'])
        V = len(glob) + 1
        n = sum(glob.values())
        by = defaultdict(Counter)
        for t in train:
            by[keyfn(t, meta)].update(list(t) + ['</s>'])

        def f(t, i):
            w = t[i] if i < len(t) else '</s>'
            pg = (glob[w] + 0.5) / (n + 0.5 * V)
            c = by.get(keyfn(t, meta), Counter())
            m = sum(c.values())
            return (c[w] + alpha * pg) / (m + alpha)
        return f
    return extra


def test_pair(extra):
    (tr, te), (DA, DB) = splits()
    a0, a1, la = evaluate(tr, te, extra)
    b0, b1, lb = evaluate(DA, DB, extra)
    return (a0, a1, la), (b0, b1, lb)


def run_set(num, title, hyps, gain=0.005):
    """hyps: [(key, title, extra)]. A hypothesis holds if the fixed-test S falls by `gain` or more and A -> B falls."""
    rd = R.Round(title, 'predict_test%d' % num)
    held = []
    for key, t, extra in hyps:
        (a0, a1, la), (b0, b1, lb) = test_pair(extra)
        ok = a0 - a1 >= gain and b1 < b0
        rd.rec(key, t, ['fixed test S %.4f -> %.4f (gain %.4f, weight %.2f)' % (a0, a1, a0 - a1, la),
                        'A -> B %.4f -> %.4f (gain %.4f, weight %.2f)' % (b0, b1, b0 - b1, lb)], ok)
        held.append(ok)
    rd.rec('P', 'progress rule: either hypothesis holds', ', '.join('%s %s' % (k, o) for (k, _, _), o in zip(hyps, held)), any(held))
    rd.finish()
    return held
