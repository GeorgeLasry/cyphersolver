"""Set 429 (goal run loop 75): audit of set 395: drop dividers preceded by a heading sign anywhere in the line.
Writes results/predict_test429.md."""
import math
import random
from collections import Counter

import rtools as R
from signs import load

HEAD = {'817', '820', '861'}
DIV = {'2', '1'}


def cos(a, b):
    num = sum(a[k] * b[k] for k in a)
    den = math.sqrt(sum(v * v for v in a.values())) * math.sqrt(sum(v * v for v in b.values()))
    return num / den if den else 0.0


def main():
    rnd = random.Random(429)
    rd = R.Round('Four-hundred-and-twenty-ninth registered predictions: goal loop 75, audit of the dividers against mid-line headings', 'predict_test429')
    A, B, *_ = R.load_all()
    DA = sorted({tuple(t) for t in A})
    DB = sorted({tuple(ln) for r in load(only_m77=True) for ln in r['seq'] if ln} - set(DA))
    ok = []
    for name, L in (('A', DA), ('B', DB)):
        nohead = [t[2:] if len(t) > 3 and t[0] in HEAD and t[1] in DIV | {'60'} else t for t in L]
        openers = Counter(t[0] for t in nohead)
        pos = [(t, i) for t in L for i in range(1, len(t) - 1) if t[i] in DIV and t[i - 1] not in R.NUMS and t[i - 1] not in HEAD and t[i + 1] not in R.NUMS]
        after = Counter(t[i + 1] for t, i in pos)
        obs = cos(after, openers)
        mids = [(t, i) for t in L for i in range(1, len(t) - 1)]
        ge = sum(cos(Counter(t[i + 1] for t, i in rnd.sample(mids, len(pos))), openers) >= obs for _ in range(1000))
        p = (ge + 1) / 1001
        rd.say('- %s: %d dividers not after a heading sign; cosine %.3f, p = %.4f; mid-line headings removed %d.' % (
            name, len(pos), obs, p, sum(1 for t in L for i in range(1, len(t) - 1) if t[i] in DIV and t[i - 1] in HEAD)))
        ok.append(p < 0.05)
    rd.say()
    rd.rec('DH1', 'the divider effect holds without heading + numeral pairs, on A', 'A %s' % ok[0], ok[0])
    rd.rec('DH2', 'the same on B', 'B %s' % ok[1], ok[1])
    rd.rec('P', 'progress rule: none (audit of set 395)', 'DH1 %s, DH2 %s' % tuple(ok), False)
    rd.finish()


if __name__ == '__main__':
    main()
