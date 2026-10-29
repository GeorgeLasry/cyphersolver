"""Do signs have preferred places inside the word groups of f. 85 (first vs last)?

Skew = half the summed |first - last| counts over signs, per 2+ sign group; compared with 200 shuffles that keep the
group lengths and sign frequencies.  python targets/sirtori1604/position_test.py
"""
import random
from collections import Counter
from vowel_set_test import groups_f85


def skew(gs):
    f = Counter(x[0] for x in gs if len(x) >= 2)
    l = Counter(x[-1] for x in gs if len(x) >= 2)
    return sum(abs(f[s] - l[s]) for s in set(f) | set(l)) / (2 * sum(f.values()))


if __name__ == '__main__':
    g = groups_f85()
    print('first', Counter(x[0] for x in g if len(x) >= 2).most_common(8))
    print('last ', Counter(x[-1] for x in g if len(x) >= 2).most_common(8))
    rng, flat, sh = random.Random(1), list(''.join(g)), []
    for _ in range(200):
        rng.shuffle(flat)
        it = iter(flat)
        sh.append(skew([''.join(next(it) for _ in x) for x in g]))
    sh.sort()
    print('skew real %.2f, shuffled median %.2f, 99th percentile %.2f' % (skew(g), sh[100], sh[198]))
