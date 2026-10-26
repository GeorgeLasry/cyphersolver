"""Session-2 loop 13: audit of set 545 (long-distance pairs): repeated phrases, or frames with an open middle?"""
import math
from collections import Counter

import s2kit as K
from hyp_s2_longdist import stats

TITLE = 'long-distance pairs: phrases or frames'
REG = '''Set 545's top-30 long-distance pairs on A. For each, the sign strings between a and b in the A lines carrying them
(`hyp_s2_ldaudit.py`).

- **LA1** For 60%+ of the pairs the commonest middle string covers under half of the pair's lines (an open middle:
  frames, not one repeated phrase).
- **LA2** Among pairs with an open middle on A that are testable on B (both signs in 5+ B lines), 70%+ co-occur on B
  more than chance (PMI > 0).
- Progress rule: LA1 and LA2 (frames with an open slot, replicated). If LA1 fails, set 545 is recorded as repeated
  phrases (downgraded).'''
SUMMARY = ''


def run(rd):
    global SUMMARY
    DA, DB = K.ab()
    n, one, adj, far = stats(DA)
    cand = [(math.log(far[x] * n / (one[x[0]] * one[x[1]])), x) for x in far if far[x] >= 4 and x not in adj and x[0] != x[1]]
    top = [x for s, x in sorted(cand, reverse=True)[:30]]
    open_ = []
    for a, b in top:
        mids = Counter()
        for t in DA:
            for i in range(len(t)):
                for j in range(i + 2, len(t)):
                    if t[i] == a and t[j] == b:
                        mids[t[i + 1:j]] += 1
        tot = sum(mids.values())
        if tot and mids.most_common(1)[0][1] / tot < 0.5:
            open_.append((a, b))
    ok1 = len(open_) / len(top) >= 0.6
    rd.rec('LA1', 'open middles for 60%+ of pairs', '%d of %d open' % (len(open_), len(top)), ok1)
    nb, oneb, adjb, farb = stats(DB)
    test = [x for x in open_ if oneb[x[0]] >= 5 and oneb[x[1]] >= 5]
    pos = sum(farb[x] * nb > oneb[x[0]] * oneb[x[1]] for x in test)
    ok2 = bool(test) and pos / len(test) >= 0.7
    rd.rec('LA2', 'open-middle pairs co-occur on B', '%d of %d; %s' % (pos, len(test), ' '.join('%s_%s' % x for x in test)), ok2)
    SUMMARY = 'open middles %d/%d; of those positive on B %d/%d.' % (len(open_), len(top), pos, len(test))
    return ok1 and ok2
