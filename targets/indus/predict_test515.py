"""Set 515 (goal run loop 161): tablets with the same text: same Harappa period? Writes results/predict_test515.md."""
import random
from collections import defaultdict

import rtools as R


def main():
    rnd = random.Random(515)
    rd = R.Round('Five-hundred-and-fifteenth registered predictions: goal loop 161, tablet copies and period', 'predict_test515')
    A, B, rowsA, recs, F = R.load_all()

    def test(sub, key, title):
        rows = []
        for r in F:
            rec = recs.get(r['sealid'])
            if rec and r['site'] == 'Harappa' and str(rec[20]).startswith(sub) and r['flat'] and len(r['flat']) >= 2:
                per = str(rec[8]).strip()
                if per not in ('', '-', 'Period 3', 'Period 3B/C', 'Period 3C'):
                    rows.append((tuple(r['flat']), per))
        by = defaultdict(list)
        for k, x in enumerate(rows):
            by[x[0]].append(k)
        pairs = [(g[a], g[b]) for g in by.values() if len(g) > 1 for a in range(len(g)) for b in range(a + 1, len(g))]
        per = [x[1] for x in rows]
        o = sum(per[i] == per[j] for i, j in pairs)
        ge = 0
        for _ in range(1000):
            pp = list(per)
            rnd.shuffle(pp)
            ge += sum(pp[i] == pp[j] for i, j in pairs) >= o
        p = (ge + 1) / 1001
        rd.rec(key, title, '%d of %d copy pairs share the period, p = %.4f' % (o, len(pairs), p), len(pairs) > 0 and p < 0.05)
        return len(pairs) > 0 and p < 0.05
    o1 = test('TAB:I', 'TP1', 'incised tablet copies share the Harappa period more than chance')
    o2 = test('TAB:B', 'TP2', 'moulded tablet copies share the Harappa period more than chance')
    rd.rec('P', 'progress rule: either holds', 'TP1 %s, TP2 %s' % (o1, o2), o1 or o2)
    rd.finish()


if __name__ == '__main__':
    main()
