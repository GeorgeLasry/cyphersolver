"""Set 517 (goal run loop 163): moulded tablet copies and their pictures. Writes results/predict_test517.md."""
import random
from collections import defaultdict

import rtools as R


def main():
    rnd = random.Random(517)
    rd = R.Round('Five-hundred-and-seventeenth registered predictions: goal loop 163, mould batches and pictures', 'predict_test517')
    A, B, rowsA, recs, F = R.load_all()
    rows = []
    for r in F:
        rec = recs.get(r['sealid'])
        if rec and r['site'] == 'Harappa' and str(rec[20]).startswith('TAB:B') and r['flat'] and len(r['flat']) >= 2:
            m = str(rec[18]).split(':')[0]
            if m not in ('', '-', 'None'):
                rows.append((tuple(r['flat']), m, str(rec[8]).strip(), str(rec[4]).strip()[:9]))
    by = defaultdict(list)
    for k, x in enumerate(rows):
        by[x[0]].append(k)
    pairs = [(g[a], g[b]) for g in by.values() if len(g) > 1 for a in range(len(g)) for b in range(a + 1, len(g))]
    mot = [x[1] for x in rows]
    strata = defaultdict(list)
    for k, x in enumerate(rows):
        strata[(x[2], x[3])].append(k)

    def test(P, key, title):
        o = sum(mot[i] == mot[j] for i, j in P)
        ge = 0
        for _ in range(1000):
            mm = list(mot)
            for ix in strata.values():
                vv = [mot[i] for i in ix]
                rnd.shuffle(vv)
                for i, v in zip(ix, vv):
                    mm[i] = v
            ge += sum(mm[i] == mm[j] for i, j in P) >= o
        p = (ge + 1) / 1001
        rd.rec(key, title, '%d of %d pairs, p = %.4f' % (o, len(P), p), len(P) > 0 and p < 0.01)
        return len(P) > 0 and p < 0.01
    o1 = test(pairs, 'MB1', 'copies share the picture')
    o2 = test([(i, j) for i, j in pairs if rows[i][2] != rows[j][2]], 'MB2', 'copies from different periods share the picture')
    rd.rec('P', 'progress rule (p < 0.01): either holds', 'MB1 %s, MB2 %s' % (o1, o2), o1 or o2)
    rd.finish()


if __name__ == '__main__':
    main()
