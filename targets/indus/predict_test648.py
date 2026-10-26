"""Set 648 (lead 7): does 892 alternate with 700 inside otherwise identical texts (minimal pairs), more than
frequency-matched sign pairs do? Writes results/predict_test648.md."""
import random
from collections import Counter, defaultdict

import rtools as R
from leadkit import ab


def minimal_pairs(L):
    slots = defaultdict(Counter)
    for t in set(L):
        for i in range(len(t)):
            slots[(t[:i], t[i + 1:])][t[i]] += 1
    mp = Counter()
    for frame, c in slots.items():
        gs = sorted(c)
        for a in range(len(gs)):
            for b in range(a + 1, len(gs)):
                mp[(gs[a], gs[b])] += 1
    return mp


def main():
    rd = R.Round('Set 648 registered predictions: 892 and 700 in minimal pairs', 'predict_test648')
    rnd = random.Random(648)
    DA, DB = ab()
    out = []
    for key, name, L in (('MP1', 'A', DA), ('MP2', 'B', DB)):
        mp = minimal_pairs(L)
        occ = Counter(g for t in L for g in t)
        obs = mp[tuple(sorted(('892', '700')))]
        near = lambda g: sorted((x for x in occ if x not in ('892', '700')), key=lambda x: abs(occ[x] - occ[g]))[:15]
        n892, n700 = near('892'), near('700')
        null = [mp[tuple(sorted((rnd.choice(n892), rnd.choice(n700))))] for _ in range(1000)]
        p = (sum(x >= obs for x in null) + 1) / 1001
        rd.rec(key, '892 / 700 minimal pairs on %s exceed frequency-matched pairs' % name, '%d minimal pairs (892 %d tokens, 700 %d); matched pairs mean %.2f; p = %.4f' % (obs, occ['892'], occ['700'], sum(null) / 1000, p), p < 0.05 and obs > 0)
        out.append(p < 0.05 and obs > 0)
    rd.rec('P', 'progress rule: MP1 and MP2 (892 is an alternant of 700)', '', all(out))
    rd.finish()


if __name__ == '__main__':
    main()
