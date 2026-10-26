"""Set 490 (goal run loop 136): seals with the same text: same phase? same workmanship? Writes results/predict_test490.md."""
import random
from collections import defaultdict

import rtools as R


def main():
    rnd = random.Random(490)
    rd = R.Round('Four-hundred-and-ninetieth registered predictions: goal loop 136, copies of a seal text', 'predict_test490')
    A, B, rowsA, recs, F = R.load_all()
    seals = []
    for r in F:
        rec = recs.get(r['sealid'])
        if rec and str(rec[20]).startswith('SEAL') and r['flat'] and len(r['flat']) >= 2:
            seals.append((tuple(r['flat']), r['site'], str(rec[9]).strip(), str(rec[22]).strip()))

    def test(j, keep, key, title):
        rows = [s for s in seals if keep(s) and s[j] not in ('', '-', '--')]
        by = defaultdict(list)
        for k, s in enumerate(rows):
            by[s[0]].append(k)
        groups = [v for v in by.values() if len(v) > 1]
        vals = [s[j] for s in rows]

        def stat(v):
            h = n = 0
            for g in groups:
                for a in range(len(g)):
                    for b in range(a + 1, len(g)):
                        n += 1
                        h += v[g[a]] == v[g[b]]
            return h, n
        o, n = stat(vals)
        ge = 0
        bysite = defaultdict(list)
        for k, s in enumerate(rows):
            bysite[s[1]].append(k)
        for _ in range(1000):
            v = list(vals)
            for site, ix in bysite.items():
                vv = [vals[i] for i in ix]
                rnd.shuffle(vv)
                for i, x in zip(ix, vv):
                    v[i] = x
            ge += stat(v)[0] >= o
        p = (ge + 1) / 1001
        rd.rec(key, title, '%d of %d copy pairs share it, p = %.4f' % (o, n, p), n > 0 and p < 0.05)
        return n > 0 and p < 0.05
    o1 = test(2, lambda s: s[1] == 'Mohenjo-daro', 'CP1', 'copies at Mohenjo-daro share the phase (field 9) more than chance')
    o2 = test(3, lambda s: True, 'CP2', 'copies share the workmanship grade (field 22) more than chance (shuffled within site)')
    rd.rec('P', 'progress rule: either holds', 'CP1 %s, CP2 %s' % (o1, o2), o1 or o2)
    rd.finish()


if __name__ == '__main__':
    main()
