"""Set 655 (lead 4): does the measure sign 700 take numbers the way a measure does? The value distribution of the long
strokes before 700 on Harappa's moulded (TAB:B) and incised (TAB:I) tablets, against discrete counts (short strokes
before other signs) and against Linear B's measure sub-units (T, Z) and discrete counts (livestock, persons) in DAMOS.
Writes results/predict_test655.md."""
import json
import re
from collections import Counter

import rtools as R
from leadkit import objects
from numerals import NUMS
from scipy.stats import fisher_exact

LB = 'C:/Users/dbour/indus_data/linb/corpus_damos_documents.jsonl'


def indus():
    d = {'TAB:B': Counter(), 'TAB:I': Counter(), 'discrete': Counter(), 'plain': Counter()}
    for s, ty, mo, size, lines, rec in objects():
        for t in set(lines):
            for i, g in enumerate(t):
                if g == '700' and ty in ('TAB:B', 'TAB:I'):
                    if i and t[i - 1] in NUMS and NUMS[t[i - 1]][1] == 'long':
                        d[ty][NUMS[t[i - 1]][0]] += 1
                    elif not (i and t[i - 1] in NUMS):
                        d['plain'][ty] += 1
                if i and t[i - 1] in NUMS and NUMS[t[i - 1]][1] == 'short' and g not in NUMS and g != '700':
                    d['discrete'][NUMS[t[i - 1]][0]] += 1
    return d


def linb():
    meas, disc = Counter(), Counter()
    for ln in open(LB, encoding='utf-8'):
        for line in json.loads(ln).get('lines', []):
            tk = line['tokens']
            for i in range(len(tk) - 1):
                if tk[i + 1].isdigit():
                    v = int(tk[i + 1])
                    if tk[i] in ('T', 'Z'):
                        meas[v] += 1
                    elif re.match(r'^(OVIS|CAP|SUS|BOS|VIR|MUL|EQU)', tk[i]):
                        disc[v] += 1
    return meas, disc


def share1(c, top=4):
    n = sum(v for k, v in c.items() if 1 <= k <= top)
    return c[1] / n if n else 0, c[1], n


def main():
    rd = R.Round('Set 655 registered predictions: the numbers before the measure sign 700', 'predict_test655')
    d = indus()
    meas, disc = linb()
    for name, c in (('Indus 700 on moulded tablets', d['TAB:B']), ('Indus 700 on incised tablets', d['TAB:I']), ('Indus discrete (short strokes, other signs)', d['discrete']), ('Linear B measure sub-units T, Z', meas), ('Linear B discrete (livestock, persons)', disc)):
        rd.say('- %s: %s.' % (name, ' '.join('%d:%d' % kv for kv in sorted(c.items()) if kv[0] <= 12)))
    rd.say('- plain 700 (no numeral) on these tablets: %s.' % dict(d['plain']))
    rd.say()
    oks = []
    for ty in ('TAB:B', 'TAB:I'):
        s, k, n = share1(d[ty])
        sd, kd, nd = share1(d['discrete'])
        p = fisher_exact([[k, n - k], [kd, nd - kd]], alternative='less')[1]
        rd.say('- %s: value 1 is %d of %d (values 1-4) against %d of %d for discrete counts, p = %.4g' % (ty, k, n, kd, nd, p))
        oks.append(p < 0.05)
    rd.rec('VM1', 'before 700 the value 1 is rarer than in discrete counts, on moulded and on incised tablets', '', all(oks))
    sm, km, nm = share1(meas)
    sd_, kd_, nd_ = share1(disc)
    rd.rec('VM2', 'Linear B control: measure sub-units also show value 1 less often than discrete counts', 'T/Z 1 is %d of %d (%.2f), discrete %d of %d (%.2f)' % (km, nm, sm, kd_, nd_, sd_), sm < sd_)
    modes = []
    for ty in ('TAB:B', 'TAB:I'):
        c = Counter(d[ty])
        c[1] += d['plain'][ty]
        modes.append((ty, max(c, key=c.get), dict(sorted(c.items()))))
    rd.rec('VM3', 'counting plain 700 as one unit, the mode is still above 1 on both tablet kinds (unlike Linear B measures and discrete counts, whose mode is 1)', '; '.join('%s mode %d %s' % m for m in modes), all(m[1] > 1 for m in modes))
    rd.rec('P', 'progress rule: none (characterisation of the 700 series against two known shapes)', '', False)
    rd.finish()


if __name__ == '__main__':
    main()
