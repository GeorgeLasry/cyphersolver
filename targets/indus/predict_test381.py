"""Set 381 (goal run loop 27): repeated square-seal texts: shared motif and shared site. Writes results/predict_test381.md."""
import random
from collections import defaultdict

import rtools as R


def main():
    rnd = random.Random(381)
    rd = R.Round('Three-hundred-and-eighty-first registered predictions: goal loop 27, repeated seal texts', 'predict_test381')
    A, B, rowsA, recs, F = R.load_all()
    seals = []
    for r in F:
        rec = recs.get(r['sealid'])
        if rec and str(rec[20]).startswith('SEAL:S') and r['flat']:
            seals.append((tuple(r['flat']), str(rec[18]).split(':')[0], r['site']))  # motif from record field 18 (F's 'motif' is empty; fixed before the reported run)
    by = defaultdict(list)
    for i, (t, m, s) in enumerate(seals):
        by[t].append(i)
    groups = [ix for ix in by.values() if len(ix) > 1 and len(by) > 0 and len(ix[0:]) and len(seals[ix[0]][0]) >= 2]

    def stat(motifs, sites):
        sm = tot = ss = 0
        for ix in groups:
            for a in range(len(ix)):
                for b in range(a + 1, len(ix)):
                    tot += 1
                    sm += motifs[ix[a]] == motifs[ix[b]]
                    ss += sites[ix[a]] == sites[ix[b]]
        return sm / tot, ss / tot, tot
    motifs = [m for t, m, s in seals]
    sites = [s for t, m, s in seals]
    om, os_, tot = stat(motifs, sites)
    nm = ns = 0
    for _ in range(1000):
        # motif null: shuffle motifs within site, so a shared site cannot make a shared motif
        bys = defaultdict(list)
        for i, s in enumerate(sites):
            bys[s].append(i)
        mm = list(motifs)
        for s, ix in bys.items():
            vals = [motifs[i] for i in ix]
            rnd.shuffle(vals)
            for i, v in zip(ix, vals):
                mm[i] = v
        ss = list(sites)
        rnd.shuffle(ss)
        a, _, _ = stat(mm, sites)
        _, b, _ = stat(motifs, ss)
        nm += a >= om
        ns += b >= os_
    pm, ps = (nm + 1) / 1001, (ns + 1) / 1001
    rd.say('- %d repeated texts (2+ signs) on %d seals, %d copy pairs.' % (len(groups), sum(len(g) for g in groups), tot))
    rd.rec('RT1', 'copies share the motif beyond the site', 'same motif %.1f%% of pairs, p = %.4f' % (100 * om, pm), pm < 0.05)
    rd.rec('RT2', 'copies stay at one site', 'same site %.1f%% of pairs, p = %.4f' % (100 * os_, ps), ps < 0.05)
    rd.rec('P', 'progress rule: either holds', 'RT1 %s, RT2 %s' % (pm < 0.05, ps < 0.05), pm < 0.05 or ps < 0.05)
    rd.finish()


if __name__ == '__main__':
    main()
