"""Set 635: the Tamil Nadu graffiti sequences (tngraffiti.in concordance) against the Indus texts, through the corpus's
own Indus parallels (data/graffiti/graffiti_indus_map.tsv). Writes results/predict_test635.md."""
import csv
import glob
import json
import random
from collections import Counter

import rtools as R
from scipy.stats import binomtest
from signs import load


def graffiti():
    recs = {}
    for f in glob.glob('data/graffiti/raw/conc_*.json'):
        for r in json.load(open(f, encoding='utf-8')).get('unique_response', []):
            recs[r['_id']] = r
    base = {}
    for r in recs.values():
        if 's2' not in r and r['type'] in ('Base', 'Variant'):
            base[r['s1']] = str(r['base'])
    seqs = Counter()
    for r in recs.values():
        if 's2' in r:
            s = tuple(r['s%d' % k] for k in range(1, 7) if r.get('s%d' % k) is not None)
            seqs[s] = max(seqs[s], r['occurrence_count'])
    return base, seqs


def mapping():
    m = {}
    for r in csv.DictReader((l for l in open('data/graffiti/graffiti_indus_map.tsv', encoding='utf-8') if not l.startswith('#')), delimiter='\t'):
        if '.' not in r['tnsda'] and r['icit']:
            m[r['tnsda']] = set(r['icit'].split('/'))
    return m


def indus():
    A, B, *_ = R.load_all()
    L = {tuple(t) for t in A} | {tuple(ln) for r in load(only_m77=True) for ln in r['seq'] if ln}
    return Counter(x for t in L for x in set(zip(t, t[1:]))), Counter(t[-1] for t in L), Counter(g for t in L for g in t)


def pairs(seqs, base, m):
    out = []
    for s in seqs:
        b = [base.get(x) for x in s]
        for x, y in zip(b, b[1:]):
            if x and y and x != y and x in m and y in m:
                out.append((x, y))
    return out


def hit(p, m, big):
    return any(big[(a, b)] or big[(b, a)] for a in m[p[0]] for b in m[p[1]])


def main():
    rd = R.Round('Set 635 registered predictions: the Tamil Nadu graffiti sequences against the Indus texts', 'predict_test635')
    rnd = random.Random(635)
    base, seqs = graffiti()
    m = mapping()
    big, last, occ = indus()
    P = pairs(seqs, base, m)
    rd.say('- %d multi-sign graffiti sequence types; %d adjacent pairs of two distinct mapped base signs; %d mapped base signs.' % (len(seqs), len(P), len(m)))
    obs = sum(hit(p, m, big) for p in P)
    keys = sorted(m)
    vals = [m[k] for k in keys]
    ge1 = 0
    for _ in range(1000):
        rnd.shuffle(vals)
        mm = dict(zip(keys, vals))
        ge1 += sum(hit(p, mm, big) for p in P) >= obs
    p1 = (ge1 + 1) / 1001
    flat = [x for p in P for x in p]
    ge2 = 0
    for _ in range(1000):
        rnd.shuffle(flat)
        PP = [(flat[2 * i], flat[2 * i + 1]) for i in range(len(P)) if flat[2 * i] != flat[2 * i + 1]]
        ge2 += sum(hit(p, m, big) for p in PP) * len(P) / max(1, len(PP)) >= obs
    p2 = (ge2 + 1) / 1001
    rd.rec('GR1', 'graffiti pairs are Indus pairs more often than under shuffled mappings and shuffled pairings',
           ['%d of %d graffiti pairs attested as Indus neighbours (either order)' % (obs, len(P)),
            'mapping shuffles as many or more: %d of 1000 (p = %.4f); pairing shuffles: %d of 1000 (p = %.4f)' % (ge1, p1, ge2, p2)], p1 < 0.05 and p2 < 0.05)
    agree = n = 0
    for a, b in P:
        f = sum(big[(x, y)] for x in m[a] for y in m[b])
        r = sum(big[(y, x)] for x in m[a] for y in m[b])
        if f + r >= 3 and max(f, r) >= 3 * max(1, min(f, r)):
            n += 1
            agree += f > r
    pb = binomtest(agree, n, 0.5).pvalue if n else 1
    rd.rec('GR2', 'graffiti order follows (or consistently reverses) Indus reading order', '%d of %d testable pairs in Indus order, two-sided p = %.4f' % (agree, n, pb), pb < 0.05)
    endb = {g for g, c in last.items() if occ[g] >= 20 and c / occ[g] >= 0.5}
    endm = {k for k, v in m.items() if v & endb}
    fin = tot = 0
    for s in seqs:
        b = [base.get(x) for x in s]
        for i, x in enumerate(b):
            if x in endm:
                tot += 1
                fin += i == len(b) - 1
    exp = sum(1 / len(s) for s in seqs for x in s if base.get(x) in endm)
    pe = binomtest(fin, tot, exp / max(1, tot), alternative='greater').pvalue if tot else 1
    rd.rec('GR3', 'graffiti signs whose parallels end Indus lines stand last in the graffiti sequence', 'end-type signs %s; last in %d of %d, expected %.1f, p = %.4f' % (' '.join(sorted(endm, key=int)), fin, tot, exp, pe), tot > 0 and pe < 0.05)
    rd.rec('P', 'progress rule: GR1 (with their mapping, the graffiti combine their signs as the Indus texts do)', 'GR1 %s' % (p1 < 0.05 and p2 < 0.05), p1 < 0.05 and p2 < 0.05)
    rd.finish()


if __name__ == '__main__':
    main()
