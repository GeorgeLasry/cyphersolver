"""Session-2 loop 2: does the sign before the ending choose 740 or 520 (lexical selection), and does the choice replicate?"""
from collections import Counter

import rtools as R
import s2kit as K

TITLE = 'which signs take 740 and which 520'
REG = '''Each sign directly before an ending (740 / 520) has a preferred ending on A (5+ ending tokens, 80%+ one ending).
(`hyp_s2_ending.py`). The fish class's 520 preference is known (sets 196, 446); this tests every sign.

- **EN1** 80%+ of A-preferring signs with 3+ ending tokens on B keep their preference on B (binomial against 50%).
- **EN2** Signs preferring 520 are more often non-fish than fish (the choice is not only the fish class): 5+ non-fish
  signs prefer 520 on A and keep it on B.
- Progress rule: EN2 holds (a new, replicated finding beyond the fish class; EN1 alone re-finds known structure).'''
SUMMARY = ''
FISH = {str(x) for x in range(220, 250)}


def run(rd):
    global SUMMARY
    DA, DB = K.ab()

    def rule(S):
        out = {}
        for g in {t[i] for t in S for i in range(len(t) - 1) if t[i + 1] in R.END}:
            lab, n = K.ending_pref(S, g)
            c = Counter(t[i + 1] for t in S for i in range(len(t) - 1) if t[i] == g and t[i + 1] in R.END)
            if n >= 5 and c[lab] / n >= 0.8:
                out[g] = lab
        return out
    pred = rule(DA)
    h, n, p = K.predict_rep(rule, lambda S, g: K.ending_pref(S, g))
    ok1 = n > 0 and h / n >= 0.8 and p < 0.05
    rd.rec('EN1', 'preferences replicate on B', '%d of %d, p = %.4f' % (h, n, p), ok1)
    nf = [g for g, lab in pred.items() if lab == '520' and g not in FISH]
    kept = [g for g in nf if K.ending_pref(DB, g)[1] >= 3 and K.ending_pref(DB, g)[0] == '520']
    ok2 = len(kept) >= 5
    rd.rec('EN2', 'non-fish signs that prefer 520 keep it on B (5+)', 'non-fish 520 signs on A: %s; kept on B: %s' % (' '.join(sorted(nf)), ' '.join(sorted(kept))), ok2)
    SUMMARY = 'preferences replicate %d/%d; non-fish 520 signs kept on B: %d.' % (h, n, len(kept))
    return ok2
