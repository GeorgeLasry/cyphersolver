"""Set 653 (lead 3): substitution classes from minimal pairs (texts identical except at one position), with a Linear B
positive control. Writes results/predict_test653.md and results/substitution_classes.tsv."""
import json
import random
import re
from collections import Counter, defaultdict

import rtools as R
from leadkit import ab
from predict_test648 import minimal_pairs

LB = 'C:/Users/dbour/indus_data/linb/corpus_damos_documents.jsonl'
MEASURE = {'S', 'V', 'T', 'Z', 'M', 'N', 'P', 'Q', 'L'}


def lb_lines():
    out = set()
    for ln in open(LB, encoding='utf-8'):
        for line in json.loads(ln).get('lines', []):
            tk = tuple(x for x in line['tokens'] if x not in (',', '/'))
            if 2 <= len(tk) <= 12 and not any('[' in x or ']' in x for x in tk):
                out.add(tk)
    return sorted(out)


def lb_class(x):
    if x.isdigit():
        return 'numeral'
    if x in MEASURE:
        return 'measure'
    if re.match(r'^[A-Z*][A-Z0-9*+]*$', x):
        return 'ideogram'
    return 'word'


def indus_class(g):
    if g in R.NUMS:
        return 'numeral'
    if g in R.END:
        return 'ending'
    if g in ('400', '90'):
        return 'marker'
    return 'other'


def same_class_test(mp, cls, rnd, n=1000):
    pairs = [(a, b, k) for (a, b), k in mp.items()]
    obs = sum(k for a, b, k in pairs if cls[a] == cls[b]) / sum(k for a, b, k in pairs)
    signs = sorted({x for a, b, k in pairs for x in (a, b)})
    labs = [cls[s] for s in signs]
    ge = 0
    for _ in range(n):
        rnd.shuffle(labs)
        c2 = dict(zip(signs, labs))
        ge += sum(k for a, b, k in pairs if c2[a] == c2[b]) / sum(k for a, b, k in pairs) >= obs
    return obs, (ge + 1) / (n + 1), sum(k for a, b, k in pairs)


def main():
    rd = R.Round('Set 653 registered predictions: substitution classes from minimal pairs', 'predict_test653')
    rnd = random.Random(653)
    L = lb_lines()
    mp = minimal_pairs(L)
    cls = {x: lb_class(x) for t in L for x in t}
    obs, p, n = same_class_test(mp, cls, rnd)
    rd.rec('SC1', 'Linear B control: minimal-pair partners share a class (numeral / measure / ideogram / word) beyond shuffled classes', '%d minimal-pair frames; same class %.3f, p = %.4f' % (n, obs, p), p < 0.05)
    DA, DB = ab()
    res = {}
    for key, name, S in (('SC2', 'A', DA), ('SC3', 'B', DB)):
        m = minimal_pairs(S)
        c = {g: indus_class(g) for t in S for g in t}
        o, pp, nn = same_class_test(m, c, rnd)
        rd.rec(key, 'Indus %s: minimal-pair partners share a class (numeral / ending / marker / other) beyond shuffles' % name, '%d frames; same class %.3f, p = %.4f' % (nn, o, pp), pp < 0.05)
        res[name] = (m, pp < 0.05)
    mA, mB = res['A'][0], res['B'][0]
    partners = defaultdict(Counter)
    for (a, b), k in mA.items():
        partners[a][b] += k
        partners[b][a] += k
    pB = defaultdict(set)
    for (a, b), k in mB.items():
        pB[a].add(b)
        pB[b].add(a)
    core = [g for g in partners if sum(partners[g].values()) >= 3 and indus_class(g) == 'other' and pB[g]]
    jac = lambda s1, s2: len(s1 & s2) / len(s1 | s2) if s1 | s2 else 0
    obsj = sum(jac(set(partners[g]), pB[g]) for g in core) / max(1, len(core))
    keys = list(pB)
    ge = 0
    for _ in range(1000):
        rnd.shuffle(keys)
        perm = dict(zip(list(pB), keys))
        ge += sum(jac(set(partners[g]), pB[perm[g]]) for g in core) / max(1, len(core)) >= obsj
    pj = (ge + 1) / 1001
    rd.rec('SC4', "lexical signs' A partner sets recur on B beyond shuffled sign identities", '%d signs with 3+ A frames and B partners; mean Jaccard %.3f, p = %.4f' % (len(core), obsj, pj), bool(core) and pj < 0.05)
    with open('results/substitution_classes.tsv', 'w', encoding='utf-8') as f:
        f.write('sign\tclass\tA_frames\tpartners_A (sign:frames)\tpartners_B\n')
        for g in sorted(partners, key=lambda g: -sum(partners[g].values())):
            f.write('%s\t%s\t%d\t%s\t%s\n' % (g, indus_class(g), sum(partners[g].values()), ' '.join('%s:%d' % x for x in partners[g].most_common()), ' '.join(sorted(pB[g]))))
    rd.rec('P', 'progress rule: SC1, SC2 and SC3 (a validated substitution method; classes in results/substitution_classes.tsv)', '', p < 0.05 and res['A'][1] and res['B'][1])
    rd.finish()


if __name__ == '__main__':
    main()
