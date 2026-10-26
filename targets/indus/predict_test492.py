"""Set 492 (goal run loop 138): copies share the animal: at Harappa; among non-unicorn seals at all sites. Length-matched
null. Writes results/predict_test492.md."""
import random
from collections import defaultdict

import rtools as R


def test(rows, rnd):
    by = defaultdict(list)
    for k, x in enumerate(rows):
        by[x[0]].append(k)
    pairs = [(g[a], g[b]) for g in by.values() if len(g) > 1 for a in range(len(g)) for b in range(a + 1, len(g))]
    pairs = [(i, j) for i, j in pairs if rows[i][2] != rows[j][2] or rows[i][2] == ('0', '0')]
    mot = [x[1] for x in rows]
    o = sum(mot[i] == mot[j] for i, j in pairs)
    bylen = defaultdict(list)
    for k, x in enumerate(rows):
        bylen[(len(x[0]), x[3])].append(k)
    ge = 0
    for _ in range(1000):
        mm = list(mot)
        for ix in bylen.values():
            vv = [mot[i] for i in ix]
            rnd.shuffle(vv)
            for i, v in zip(ix, vv):
                mm[i] = v
        ge += sum(mm[i] == mm[j] for i, j in pairs) >= o
    return o, len(pairs), (ge + 1) / 1001


def main():
    rnd = random.Random(492)
    rd = R.Round('Four-hundred-and-ninety-second registered predictions: goal loop 138, copies share the animal elsewhere', 'predict_test492')
    A, B, rowsA, recs, F = R.load_all()
    rows = []
    for r in F:
        rec = recs.get(r['sealid'])
        if rec and str(rec[20]).startswith('SEAL:S') and r['flat'] and len(r['flat']) >= 2:
            m = str(rec[18]).split(':')[0]
            if m not in ('', '-', 'None'):
                rows.append((tuple(r['flat']), m, (str(rec[31]), str(rec[32])), r['site']))
    h = test([x for x in rows if x[3] == 'Harappa'], rnd)
    rd.rec('CH1', 'at Harappa copies share the animal more than chance', '%d of %d pairs, p = %.4f' % h, h[1] > 0 and h[2] < 0.05)
    nu = [x for x in rows if x[1] != 'Bull1']
    o = test(nu, rnd)
    rd.rec('CH2', 'among non-unicorn seals (all sites, shuffled within length and site) copies share the animal', '%d of %d pairs, p = %.4f' % o, o[1] > 0 and o[2] < 0.05)
    rd.rec('P', 'progress rule: none (re-test of set 491)', '', False)
    rd.finish()


if __name__ == '__main__':
    main()
