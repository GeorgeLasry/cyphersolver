"""Three-hundred-and-fifty-fourth registered prediction set (PREDICTIONS.md, PL1-PL7): decipherment loop 179, Parpola's
later readings (rebus/parpola_later.tsv) as structural predictions. Writes results/predict_test354.md."""
import math
import random
from collections import Counter, defaultdict

import rtools as R
from rtools import fisher_less, hyper_ge

STROKED = {'742', '744', '745', '746'}
CAGED = {'226', '232', '153', '236', '241'}
BULLYOKE = {'154', '155', '156', '157', '158'}


def main():
    rnd = random.Random(354)
    A, B, rowsA, recs, F = R.load_all()
    DA, DB = sorted({tuple(t) for t in A}), sorted({tuple(t) for t in B})
    DL = sorted(set(DA) | set(DB))
    rd = R.Round("Three-hundred-and-fifty-fourth registered predictions: decipherment loop 179, Parpola's later readings", 'predict_test354')
    held = 0

    def initial(L, S):
        return sum(1 for t in L for i, g in enumerate(t) if g in S and i == 0), sum(1 for t in L for g in t if g in S)
    a, na = initial(DA, STROKED)
    c, nc = initial(DA, {'740'})
    p = hyper_ge(a, na - a, c, nc - c)
    a2, na2 = initial(DB, STROKED)
    c2, nc2 = initial(DB, {'740'})
    ok = p < 0.05 and a / na > c / nc and a2 / max(1, na2) > c2 / max(1, nc2)
    rd.rec('PL1', "stroked bull's heads open the line", ['A: %s' % R.fl(a, na, c, nc, p), 'B: %d of %d against %d of %d' % (a2, na2, c2, nc2)], ok)
    held += ok
    prev = defaultdict(Counter)
    for t in DL:
        for i in range(1, len(t)):
            prev[t[i]][t[i - 1]] += 1
    cnt = Counter(g for t in DL for g in t)

    def vec(S):
        v = Counter()
        for g in S:
            v.update(prev[g])
        return v

    def cos(va, vb):
        num = sum(va[k] * vb[k] for k in va)
        den = math.sqrt(sum(x * x for x in va.values())) * math.sqrt(sum(x * x for x in vb.values()))
        return num / den if den else 0.0

    def band(S):
        n = sum(cnt[g] for g in S)
        pool = [g for g in cnt if 0.5 * n <= cnt[g] <= 2 * n and g not in S and prev[g]]
        return pool or [g for g in cnt if prev[g] and g not in S]

    def cos_test(key, title, X, Ys):
        obs = sum(cos(vec(X), vec(Y)) for Y in Ys) / len(Ys)
        pools = [band(Y) for Y in Ys]
        ge = sum(sum(cos(vec(X), prev[rnd.choice(pl)]) for pl in pools) / len(Ys) >= obs for _ in range(1000))
        pp = (ge + 1) / 1001
        rd.rec(key, title, 'cosine %.3f, random partners as high in %d of 1000, p = %.4f' % (obs, ge, pp), pp < 0.05)
        return pp < 0.05
    held += cos_test('PL2', '741 shares the preceding signs of 740', {'741'}, [{'740'}])
    held += cos_test('PL3', 'caged fish share the preceding signs of the spear 520', CAGED, [{'520'}])
    held += cos_test('PL4', 'two long strokes share the preceding signs of the fish', {'32'}, [{'220'}])
    a = sum(1 for t in DL for i in range(len(t) - 2) if t[i:i + 3] == ('16', '220', '151'))
    na = sum(1 for t in DL for i in range(len(t) - 2) if t[i:i + 2] == ('16', '220'))
    c = sum(1 for t in DL for i in range(len(t) - 1) if t[i:i + 2] == ('220', '151') and (i == 0 or t[i - 1] != '16'))
    nc = sum(1 for t in DL for i in range(len(t) - 1) if t[i] == '220' and (i == 0 or t[i - 1] != '16'))
    p = hyper_ge(a, na - a, c, nc - c)
    ok = p < 0.05 and a / max(1, na) > c / max(1, nc)
    rd.rec('PL5', 'six + fish is followed by the yoke-carrier', R.fl(a, na, c, nc, p), ok)
    held += ok
    held += cos_test('PL6', "the yoke-carrier ligatures share 151's preceding signs", {'151'}, [BULLYOKE, {'161'}])
    rd.rec('PL7', 'progress rule: 4+ of PL1-PL6 hold', '%d of 6 held' % held, held >= 4)
    rd.finish()


if __name__ == '__main__':
    main()
