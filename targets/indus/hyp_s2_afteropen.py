"""Session-2 loop 14: the sign after an opener is drawn from a small set."""
import math
from collections import Counter

import s2kit as K

TITLE = 'what follows an opener'
REG = '''Openers of set 539 (104 491 692 817 820 853 861 920). Entropy of the sign that follows an opener against the sign
that follows other line-initial signs of matched frequency (`hyp_s2_afteropen.py`).

- **AO1** On A the follower entropy after openers is lower than after 200 random frequency-matched sets of non-opener
  first signs (p < 0.05).
- **AO2** The same on B.
- Progress rule: AO1 and AO2, unless sets 230-279 (heading unit, its second sign) already fix it: consistency.'''
SUMMARY = ''
OP = {'104', '491', '692', '817', '820', '853', '861', '920'}


def ent(S, firsts):
    c = Counter(t[1] for t in S if len(t) > 1 and t[0] in firsts)
    n = sum(c.values())
    return -sum(v / n * math.log2(v / n) for v in c.values()) if n else 0, n


def run(rd):
    global SUMMARY
    import random
    rnd = random.Random(549)
    DA, DB = K.ab()
    out = []
    for key, name, S in (('AO1', 'A', DA), ('AO2', 'B', DB)):
        e, n = ent(S, OP)
        fc = Counter(t[0] for t in S if len(t) > 1)
        others = [g for g in fc if g not in OP and fc[g] >= 3]
        le = 0
        for _ in range(200):
            pick, tot = set(), 0
            pool = others[:]
            rnd.shuffle(pool)
            for g in pool:
                if tot >= n:
                    break
                pick.add(g)
                tot += fc[g]
            le += ent(S, pick)[0] <= e
        p = (le + 1) / 201
        rd.rec(key, 'low follower entropy after openers, %s' % name, 'entropy %.2f bits over %d lines; random sets as low %d of 200, p = %.4f' % (e, n, le, p), p < 0.05)
        out.append(p < 0.05)
    SUMMARY = 'A %s, B %s; the heading unit (sets 230-279) covers it: consistency.' % tuple(out)
    return False
