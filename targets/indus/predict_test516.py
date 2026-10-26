"""Set 516 (goal run loop 162): audit of set 515 with periods shuffled within excavation area. Writes results/predict_test516.md."""
import random
from collections import defaultdict

import rtools as R


def main():
    rnd = random.Random(516)
    rd = R.Round('Five-hundred-and-sixteenth registered predictions: goal loop 162, audit of tablet copies and period', 'predict_test516')
    A, B, rowsA, recs, F = R.load_all()

    def test(sub, key, title):
        rows = []
        for r in F:
            rec = recs.get(r['sealid'])
            if rec and r['site'] == 'Harappa' and str(rec[20]).startswith(sub) and r['flat'] and len(r['flat']) >= 2:
                per = str(rec[8]).strip()
                if per not in ('', '-', 'Period 3', 'Period 3B/C', 'Period 3C'):
                    rows.append((tuple(r['flat']), per, str(rec[4]).strip()[:9]))
        by = defaultdict(list)
        for k, x in enumerate(rows):
            by[x[0]].append(k)
        pairs = [(g[a], g[b]) for g in by.values() if len(g) > 1 for a in range(len(g)) for b in range(a + 1, len(g))]
        per = [x[1] for x in rows]
        area = defaultdict(list)
        for k, x in enumerate(rows):
            area[x[2]].append(k)
        o = sum(per[i] == per[j] for i, j in pairs)
        ge = 0
        for _ in range(1000):
            pp = list(per)
            for ix in area.values():
                vv = [per[i] for i in ix]
                rnd.shuffle(vv)
                for i, v in zip(ix, vv):
                    pp[i] = v
            ge += sum(pp[i] == pp[j] for i, j in pairs) >= o
        p = (ge + 1) / 1001
        rd.rec(key, title, '%d of %d pairs, within-area shuffle p = %.4f' % (o, len(pairs), p), len(pairs) > 0 and p < 0.05)
    test('TAB:I', 'TA1', 'incised copies share the period beyond their area')
    test('TAB:B', 'TA2', 'moulded copies share the period beyond their area')
    rd.rec('P', 'progress rule: none (audit of set 515)', '', False)
    rd.finish()


if __name__ == '__main__':
    main()
