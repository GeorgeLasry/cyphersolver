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


def build_dir():
    A, B, rowsA, recs, F = R.load_all()
    d = defaultdict(Counter)
    for r in list(rowsA) + list(load(only_m77=True)):
        for ln in r['seq']:
            if ln and r.get('direction'):
                d[tuple(ln)][r['direction']] += 1
    return {ln: c.most_common(1)[0][0] for ln, c in d.items()}


DIRECTION = build_dir()


def build_subtype():
    A, B, rowsA, recs, F = R.load_all()
    d = defaultdict(Counter)
    for r in list(rowsA) + list(F):
        for ln in r['seq']:
            if ln and r.get('type'):
                d[tuple(ln)][':'.join(r['type'].split(':')[:2])] += 1
    return {ln: c.most_common(1)[0][0] for ln, c in d.items()}


SUBTYPE = build_subtype()

_FIELD_CACHE = {}


def field(j):
    """line -> the commonest value of ICIT record field j (8 period, 9-10 phase, 13 material, 14 colour, 15 shape,
    19 secondary motif, 22 workmanship, 31-33 dimensions) over the clean F objects carrying the line (set 374)."""
    if j not in _FIELD_CACHE:
        import icit_full
        A, B, rowsA, recs, F = R.load_all()
        d = defaultdict(Counter)
        for r in F:
            rec = recs.get(r['sealid'])
            if rec and len(rec) > j and str(rec[j]).strip() not in ('', '-', '--', '- -', 'None'):
                for ln in r['seq']:
                    if ln:
                        d[tuple(ln)][str(rec[j]).strip()] += 1
        _FIELD_CACHE[j] = {ln: c.most_common(1)[0][0] for ln, c in d.items()}
    return _FIELD_CACHE[j]


def build_depth_place():
    A, B, rowsA, recs, F = R.load_all()
    dep, by_site = {}, defaultdict(list)
    for r in F:
        if r['depth'] is not None:
            by_site[r['site']].append(r['depth'])
    cut = {}
    for site, ds in by_site.items():
        ds = sorted(ds)
        cut[site] = (ds[len(ds) // 3], ds[2 * len(ds) // 3]) if len(ds) >= 9 else None
    place = {}
    for r in list(rowsA) + list(load(only_m77=True)) + list(F):
        lines = [tuple(ln) for ln in r['seq'] if ln]
        for k, ln in enumerate(lines):
            place.setdefault(ln, 'single' if len(lines) == 1 else ('first' if k == 0 else 'later'))
            if r.get('depth') is not None and cut.get(r['site']) and ln not in dep:
                a, b = cut[r['site']]
                dep[ln] = 'shallow' if r['depth'] < a else ('middle' if r['depth'] < b else 'deep')
    return dep, place


DEPTH, PLACE = build_depth_place()


REGION_W = 0.3  # set 357 (DM2, audited against random groups): the region-domain model mixed in at weight 0.3


def _plain(train, test):
    random.seed(2026)  # fit3's inner split uses the global generator (fixed after set 355)
    w, _ = fit3(train, MODEL['keys'])
    m = M3(train)
    return [[sum(w[k] * r[k] for k in w) for r in m.rows(t, MODEL['kn'])] for t in test]


# adopted domain models, mixed in order onto the plain model: (keyfn, weight)
BASE_DOMAINS = [  # region (set 357) dropped by set 372: it adds 0.0018 on top of the type models
                (lambda t, m: min(max(len(t), 2), 6), 0.3),  # set 359 DL1, length band
                (lambda t, m: m.get(t, ('', '', ''))[1], 0.2),  # set 367 OT1, object type (B lacks it: no effect there)
                (lambda t, m: SUBTYPE.get(t, ''), 0.2),  # set 369 ST1, object subtype
                (lambda t, m: (min(max(len(t), 2), 6), SUBTYPE.get(t, '')), 0.2)]  # set 372 AB2, length x subtype


def base_probs(train, test):
    pb = _plain(train, test)
    for kf, wt in BASE_DOMAINS:
        f = domain_model(kf)(train, META)
        pb = [[(1 - wt) * a + wt * f(t, i) for i, a in enumerate(row)] for t, row in zip(test, pb)]
    return pb


def _bits(pb, pe, lam, signs_only=False):
    n = s = 0
    for row_b, row_e in zip(pb, pe):
        for j, (a, b) in enumerate(zip(row_b, row_e)):
            if signs_only and j == len(row_b) - 1:
                continue
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
    SIGNS_ONLY.append((_bits(pb, pe, 0.0, True), _bits(pb, pe, lam, True)))
    return _bits(pb, pe, 0.0), _bits(pb, pe, lam), lam


SIGNS_ONLY = []  # (base, mix) bits on sign tokens, end token left out (rule from set 362, after the set 361 audit)


def _splits_ab():
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


def cache(source, alpha=2.0):
    """Probability that the token repeats a sign from source(line, i): its earlier signs, or the object's other lines."""
    def extra(train, meta):
        glob = Counter(g for t in train for g in list(t) + ['</s>'])
        V, n = len(glob) + 1, sum(glob.values())

        def f(t, i):
            w = t[i] if i < len(t) else '</s>'
            pg = (glob[w] + 0.5) / (n + 0.5 * V)
            c = Counter(source(t, i))
            m = sum(c.values())
            return (c[w] + alpha * pg) / (m + alpha)
        return f
    return extra


def domain_model_fit(keyfn, minlines=150):
    """As domain_model, but each group's interpolation weights are fitted on that group's own lines (set 378)."""
    def extra(train, meta):
        random.seed(2026)
        w, _ = fit3(train, MODEL['keys'])
        glob = M3(train)
        groups = defaultdict(list)
        for t in train:
            groups[keyfn(t, meta)].append(t)
        models = {}
        for k, v in groups.items():
            if len(v) >= minlines:
                random.seed(2026)
                models[k] = (M3(v), fit3(v, MODEL['keys'])[0])
        cache = {}

        def f(t, i):
            if t not in cache:
                m, ww = models.get(keyfn(t, meta), (glob, w))
                cache[t] = [sum(ww[k] * r[k] for k in ww) for r in m.rows(t, MODEL['kn'])]
            return cache[t][i]
        return f
    return extra


def domain_model(keyfn, minlines=40, skip0=False):
    """The registered model trained only on the training lines that share keyfn's value (global weights), for groups
    with minlines+ lines; other lines get the global model (so the mix changes nothing for them)."""
    def extra(train, meta):
        random.seed(2026)
        w, _ = fit3(train, MODEL['keys'])
        glob = M3(train)
        groups = defaultdict(list)
        for t in train:
            groups[keyfn(t, meta)].append(t)
        models = {k: M3(v) for k, v in groups.items() if len(v) >= minlines}
        cache = {}

        def f(t, i):
            if t not in cache:
                m = models.get(keyfn(t, meta), glob)
                cache[t] = [sum(w[k] * r[k] for k in w) for r in m.rows(t, MODEL['kn'])]
                if skip0:  # the key reads the line's own first sign: position 0 must not see it (set 373)
                    cache[t][0] = sum(w[k] * r[k] for k in w for r in glob.rows(t, MODEL['kn'])[:1])
            return cache[t][i]
        return f
    return extra


def ctx_model(ctxfn, D=0.5):
    """p(token | ctxfn(line, i)), absolutely discounted onto the add-0.5 unigram. ctxfn may use only signs before i
    and the line length (S is given the length)."""
    def extra(train, meta):
        glob = Counter(g for t in train for g in list(t) + ['</s>'])
        V, n = len(glob) + 1, sum(glob.values())
        c = defaultdict(Counter)
        for t in train:
            for i in range(len(t) + 1):
                c[ctxfn(t, i)][t[i] if i < len(t) else '</s>'] += 1

        def f(t, i):
            w = t[i] if i < len(t) else '</s>'
            pg = (glob[w] + 0.5) / (n + 0.5 * V)
            cc = c.get(ctxfn(t, i))
            if not cc:
                return pg
            m = sum(cc.values())
            return max(cc[w] - D, 0) / m + D * len(cc) / m * pg
        return f
    return extra


def test_pair(extra):
    del SIGNS_ONLY[:]
    (tr, te), (DA, DB) = splits()
    a0, a1, la = evaluate(tr, te, extra)
    b0, b1, lb = evaluate(DA, DB, extra)
    return (a0, a1, la), (b0, b1, lb)


def random_groups(real, salt):
    """Lines assigned to groups of the same sizes as real's, by a fixed hash: the ensemble-only control (set 357 audit)."""
    import hashlib
    (tr, te), (DA, DB) = splits()
    allines = sorted(set(tr) | set(te) | set(DA) | set(DB))
    sizes = Counter(real(t, META) for t in allines)
    order = sorted(allines, key=lambda t: hashlib.md5((salt + ' '.join(t)).encode()).hexdigest())
    lab, k = {}, 0
    for g, n in sizes.most_common():
        for t in order[k:k + n]:
            lab[t] = g
        k += n
    return lambda t, m: lab.get(t, '')


def run_domain_set(num, title, hyps, gain=0.005, skip0=False):
    """hyps: [(key, title, keyfn)]. Holds if the domain model's gains pass the S rule AND beat the mean gain of two
    random-group controls of the same sizes on both splits (rule from set 358)."""
    rd = R.Round(title, 'predict_test%d' % num)
    held = []
    for key, t, kf in hyps:
        (a0, a1, la), (b0, b1, lb) = test_pair(domain_model(kf, skip0=skip0))
        (sa0, sa1), (sb0, sb1) = SIGNS_ONLY
        ctl = [test_pair(domain_model(random_groups(kf, salt), skip0=skip0)) for salt in ('a', 'b')]
        ca = sum(x[0][0] - x[0][1] for x in ctl) / 2
        cb = sum(x[1][0] - x[1][1] for x in ctl) / 2
        ok = a0 - a1 >= gain and b1 < b0 and a0 - a1 > ca and b0 - b1 > cb and sa1 < sa0 and sb1 < sb0
        rd.rec(key, t, ['fixed test S %.4f -> %.4f (gain %.4f, weight %.2f; random groups %.4f); signs only %.4f -> %.4f' % (a0, a1, a0 - a1, la, ca, sa0, sa1),
                        'A -> B %.4f -> %.4f (gain %.4f, weight %.2f; random groups %.4f); signs only %.4f -> %.4f' % (b0, b1, b0 - b1, lb, cb, sb0, sb1)], ok)
        held.append(ok)
    rd.rec('P', 'progress rule: either hypothesis holds', ', '.join('%s %s' % (k, o) for (k, _, _), o in zip(hyps, held)), any(held))
    rd.finish()
    return held


splits = _splits_ab


def splits_c():
    """Fixed split, plus split C: the fixed training lines cut 80/20 (seed 2027), so C's test lines are disjoint from
    the fixed test. For side information Mahadevan's records lack (type and motif are 'M77' / empty on B; set 367)."""
    (tr, te), _ = _splits_ab()
    rnd = random.Random(2027)
    ls = list(tr)
    rnd.shuffle(ls)
    k = int(0.8 * len(ls))
    return (tr, te), (ls[:k], ls[k:])


def run_domain_set_c(num, title, hyps, gain=0.005):
    """As run_domain_set, with split C in place of A -> B."""
    global splits
    orig = splits
    splits = splits_c
    try:
        return run_domain_set(num, title, hyps, gain)
    finally:
        splits = orig


def run_set(num, title, hyps, gain=0.005):
    """hyps: [(key, title, extra)]. A hypothesis holds if the fixed-test S falls by `gain` or more and A -> B falls."""
    rd = R.Round(title, 'predict_test%d' % num)
    held = []
    for key, t, extra in hyps:
        (a0, a1, la), (b0, b1, lb) = test_pair(extra)
        (sa0, sa1), (sb0, sb1) = SIGNS_ONLY
        ok = a0 - a1 >= gain and b1 < b0 and sa1 < sa0 and sb1 < sb0
        rd.rec(key, t, ['fixed test S %.4f -> %.4f (gain %.4f, weight %.2f); signs only %.4f -> %.4f' % (a0, a1, a0 - a1, la, sa0, sa1),
                        'A -> B %.4f -> %.4f (gain %.4f, weight %.2f); signs only %.4f -> %.4f' % (b0, b1, b0 - b1, lb, sb0, sb1)], ok)
        held.append(ok)
    rd.rec('P', 'progress rule: either hypothesis holds', ', '.join('%s %s' % (k, o) for (k, _, _), o in zip(hyps, held)), any(held))
    rd.finish()
    return held


def _scorer(train, domains, rev=False):
    """log2 P(line) under the plain model mixed with the given domain models (keyfns read META of the original line)."""
    import math as _m
    flip = (lambda t: tuple(reversed(t))) if rev else (lambda t: t)
    tr = [flip(t) for t in train]
    random.seed(2026)
    w, _ = fit3(tr, MODEL['keys'])
    glob = M3(tr)
    doms = []
    for kf, wt in domains:
        groups = defaultdict(list)
        for t in train:
            groups[kf(t, META)].append(flip(t))
        doms.append((kf, wt, {k: M3(v) for k, v in groups.items() if len(v) >= 40}))

    def lp(orig, cand):
        c = flip(cand)
        p = [sum(w[k] * r[k] for k in w) for r in glob.rows(c, MODEL['kn'])]
        for kf, wt, models in doms:
            m = models.get(kf(orig, META))
            q = [sum(w[k] * r[k] for k in w) for r in m.rows(c, MODEL['kn'])] if m else p
            p = [(1 - wt) * a + wt * b for a, b in zip(p, q)]
        return sum(_m.log2(max(x, 1e-12)) for x in p)
    return lp


def sign_task(train, test, domains, ncand=150, limit=None):
    """SIGN (set 204): hide each sign, rank the ncand commonest training signs by forward + backward log-probability."""
    f, b = _scorer(train, domains), _scorer(train, domains, rev=True)
    cands = [g for g, c in Counter(g for t in train for g in t).most_common(ncand)]
    top1 = top5 = n = 0
    for t in (test[:limit] if limit else test):
        for i, g in enumerate(t):
            sc = sorted(cands, key=lambda c: -(f(t, t[:i] + (c,) + t[i + 1:]) + b(t, t[:i] + (c,) + t[i + 1:])))
            n += 1
            top1 += sc[0] == g
            top5 += g in sc[:5]
    return top1 / n, top5 / n, n


def run_set_c(num, title, hyps, gain=0.005):
    """As run_set, with split C in place of A -> B (set 378)."""
    global splits
    orig = splits
    splits = splits_c
    try:
        return run_set(num, title, hyps, gain)
    finally:
        splits = orig
