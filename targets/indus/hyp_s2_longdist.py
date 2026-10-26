"""Session-2 loop 10: sign pairs that co-occur at a distance (2+ apart) in one line, never adjacent."""
import math
from collections import Counter

import s2kit as K

TITLE = 'long-distance sign pairs'
REG = '''Pairs (a ... b), a before b, 2+ positions apart, never adjacent anywhere on A, in 4+ distinct A lines; PMI against the
signs' line frequencies (`hyp_s2_longdist.py`). The 30 highest-PMI pairs are A's long-distance pairs.

- **LD1** 70%+ of them that have both signs in 5+ B lines co-occur on B more than their B frequencies predict (PMI > 0).
- **LD2** At least 10 such pairs are testable on B.
- Progress rule: LD1 and LD2 (dependencies beyond the neighbour, replicated).'''
SUMMARY = ''


def stats(S):
    n = len(S)
    one = Counter(g for t in S for g in set(t))
    adj = {x for t in S for x in zip(t, t[1:])}
    far = Counter()
    for t in S:
        seen = set()
        for i in range(len(t)):
            for j in range(i + 2, len(t)):
                seen.add((t[i], t[j]))
        far.update(seen)
    return n, one, adj, far


def run(rd):
    global SUMMARY
    DA, DB = K.ab()
    n, one, adj, far = stats(DA)
    cand = [(math.log(far[x] * n / (one[x[0]] * one[x[1]])), x) for x in far if far[x] >= 4 and x not in adj and x[0] != x[1]]
    top = [x for s, x in sorted(cand, reverse=True)[:30]]
    nb, oneb, adjb, farb = stats(DB)
    test = [x for x in top if oneb[x[0]] >= 5 and oneb[x[1]] >= 5]
    pos = sum(farb[x] * nb > oneb[x[0]] * oneb[x[1]] for x in test)
    ok1 = bool(test) and pos / len(test) >= 0.7
    ok2 = len(test) >= 10
    rd.rec('LD1', 'long-distance pairs co-occur on B', '%d of %d; pairs %s' % (pos, len(test), ' '.join('%s..%s' % x for x in test)), ok1)
    rd.rec('LD2', '10+ testable', '%d' % len(test), ok2)
    SUMMARY = '%d of %d A long-distance pairs positive on B.' % (pos, len(test))
    return ok1 and ok2
