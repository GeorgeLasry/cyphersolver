"""Session-2 loop 4: do name heads (sign before an ending) and line openers form separate vocabularies?"""
from collections import Counter

import rtools as R
import s2kit as K
from scipy.stats import binomtest

TITLE = 'heads and openers as separate vocabularies'
REG = '''A sign is a 'head' on A if 60%+ of its tokens (10+) stand before an ending, an 'opener' if 60%+ open the line
(`hyp_s2_heads.py`).

- **HO1** No sign is both a head and an opener on A, and 80%+ of A heads and openers with 5+ B tokens keep their class on
  B (binomial against 50%).
- **HO2** Heads are graphically varied: heads come from 5+ different decade families, openers from fewer families than
  heads (openers are a small closed set).
- Progress rule: HO2 holds with HO1 (a replicated description of the two slots' vocabularies).'''
SUMMARY = ''


def run(rd):
    global SUMMARY
    DA, DB = K.ab()

    def classes(S, minn):
        occ = Counter(g for t in S for g in t)
        hd = Counter(t[i] for t in S for i in range(len(t) - 1) if t[i + 1] in R.END)
        op = Counter(t[0] for t in S)
        return ({g for g in occ if occ[g] >= minn and hd[g] / occ[g] >= 0.6},
                {g for g in occ if occ[g] >= minn and op[g] / occ[g] >= 0.6}, occ, hd, op)
    H, O, *_ = classes(DA, 10)
    _, _, ob, hb, pb = classes(DB, 1)
    kept = n = 0
    for g in H | O:
        if ob[g] >= 5:
            n += 1
            kept += (hb[g] / ob[g] >= 0.5) if g in H else (pb[g] / ob[g] >= 0.5)
    p = binomtest(kept, n, 0.5, alternative='greater').pvalue if n else 1
    ok1 = not (H & O) and n > 0 and kept / n >= 0.8 and p < 0.05
    rd.rec('HO1', 'heads and openers disjoint and kept on B', 'heads %d, openers %d, both %d; kept %d of %d, p = %.4f' % (len(H), len(O), len(H & O), kept, n, p), ok1)
    fam = lambda S: {int(g) // 10 for g in S if g.isdigit()}
    ok2 = len(fam(H)) >= 5 and len(fam(O)) < len(fam(H))
    rd.rec('HO2', 'heads graphically varied, openers fewer families', 'head families %d, opener families %d; openers %s' % (len(fam(H)), len(fam(O)), ' '.join(sorted(O))), ok2)
    SUMMARY = 'heads %d (%d families), openers %d (%d families); kept on B %d/%d.' % (len(H), len(fam(H)), len(O), len(fam(O)), kept, n)
    return ok1 and ok2
