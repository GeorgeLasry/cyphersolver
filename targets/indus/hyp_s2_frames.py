"""Session-2 loop 15: frames a _ b with an open middle, from a wider pool than set 545."""
import math
from collections import Counter

import s2kit as K
from hyp_s2_longdist import stats

TITLE = 'open-slot frames'
REG = '''Pairs a ... b (2+ apart, never adjacent on A, in 4+ A lines, positive PMI), the 200 highest by PMI, kept if the
commonest middle string covers under half of their A lines (open slot) (`hyp_s2_frames.py`).

- **FR1** 15+ open-slot frames are testable on B (both signs in 5+ B lines).
- **FR2** 70%+ of them co-occur on B more than chance (PMI > 0).
- Progress rule: FR1 and FR2 (frames with an open slot, replicated: a syntactic template).'''
SUMMARY = ''


def run(rd):
    global SUMMARY
    DA, DB = K.ab()
    n, one, adj, far = stats(DA)
    cand = [(math.log(far[x] * n / (one[x[0]] * one[x[1]])), x) for x in far if far[x] >= 4 and x not in adj and x[0] != x[1]]
    cand = [(s, x) for s, x in cand if s > 0]
    top = [x for s, x in sorted(cand, reverse=True)[:200]]
    frames = []
    for a, b in top:
        mids = Counter()
        for t in DA:
            for i in range(len(t)):
                for j in range(i + 2, len(t)):
                    if t[i] == a and t[j] == b:
                        mids[t[i + 1:j]] += 1
        tot = sum(mids.values())
        if tot and mids.most_common(1)[0][1] / tot < 0.5:
            frames.append((a, b))
    nb, oneb, adjb, farb = stats(DB)
    test = [x for x in frames if oneb[x[0]] >= 5 and oneb[x[1]] >= 5]
    pos = sum(farb[x] * nb > oneb[x[0]] * oneb[x[1]] for x in test)
    ok1 = len(test) >= 15
    ok2 = bool(test) and pos / len(test) >= 0.7
    rd.rec('FR1', '15+ testable frames', '%d open-slot frames of %d; %d testable' % (len(frames), len(top), len(test)), ok1)
    rd.rec('FR2', 'frames co-occur on B', '%d of %d; %s' % (pos, len(test), ' '.join('%s_%s' % x for x in test[:40])), ok2)
    SUMMARY = 'frames %d, testable %d, positive on B %d.' % (len(frames), len(test), pos)
    return ok1 and ok2
