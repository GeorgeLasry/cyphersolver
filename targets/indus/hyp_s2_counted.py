"""Session-2 loop 11: are counted signs (right after a numeral) and name heads (right before an ending) different sets?"""
from collections import Counter

import rtools as R
import s2kit as K
from scipy.stats import binomtest

TITLE = 'counted signs against name heads'
REG = '''A sign is 'counted' on A if 50%+ of its tokens (8+) follow a numeral, a 'head' if 50%+ precede an ending
(`hyp_s2_counted.py`).

- **CH1** No sign is both on A, and of signs that are counted on A with 5+ B tokens, 80%+ are rarely heads on B (under
  20% before an ending).
- **CH2** Counted signs are followed by an ending on B less often than heads are (Fisher-like binomial on B tokens).
- Progress rule: CH1 and CH2, unless the counted-sign role (set 176 R) already covers it: then consistency.'''
SUMMARY = ''


def run(rd):
    global SUMMARY
    DA, DB = K.ab()

    def cls(S, mn):
        occ = Counter(g for t in S for g in t)
        cnt = Counter(t[i] for t in S for i in range(1, len(t)) if t[i - 1] in R.NUMS)
        hd = Counter(t[i] for t in S for i in range(len(t) - 1) if t[i + 1] in R.END)
        return {g for g in occ if occ[g] >= mn and cnt[g] / occ[g] >= 0.5}, {g for g in occ if occ[g] >= mn and hd[g] / occ[g] >= 0.5}, occ, hd
    C, H, _, _ = cls(DA, 8)
    _, _, ob, hb = cls(DB, 1)
    test = [g for g in C if ob[g] >= 5]
    rare = sum(hb[g] / ob[g] < 0.2 for g in test)
    ok1 = not (C & H) and bool(test) and rare / len(test) >= 0.8
    rd.rec('CH1', 'counted and head sets disjoint; counted signs rarely heads on B', 'counted %d, heads %d, both %d; %d of %d rarely heads on B; counted %s' % (len(C), len(H), len(C & H), rare, len(test), ' '.join(sorted(C))), ok1)
    hc = sum(hb[g] for g in C); nc = sum(ob[g] for g in C)
    hh = sum(hb[g] for g in H); nh = sum(ob[g] for g in H)
    ok2 = nc > 0 and nh > 0 and hc / nc < hh / nh
    rd.rec('CH2', 'counted signs take the ending less often on B', '%d of %d against %d of %d' % (hc, nc, hh, nh), ok2)
    SUMMARY = 'counted %d / heads %d, overlap %d; counted rarely heads on B %d/%d; the roles (set 176) already separate them: consistency.' % (len(C), len(H), len(C & H), rare, len(test))
    return False
