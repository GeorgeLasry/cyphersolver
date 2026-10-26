"""Set 377b (goal run loop 23): the tier 3 restoration check (sets 283, 284, 314) rescored with the object-kind domain
models of the S base (loopkit.BASE_DOMAINS: length, type, subtype, length x subtype). The gap line's object record gives
its type and subtype. Plain and domain predictions on the same copy-free training lines. Writes results/predict_test377.md."""
import csv
import os
from collections import Counter

import loopkit as L
import rtools as R
from predict_test283 import copy_of
from predict_test284 import new_cases
from predict_test314 import cases as cases2, copy2
from progress import data

HERE = os.path.dirname(os.path.abspath(__file__))


def setmeta(t, rec):
    if rec:
        L.META[t] = (rec[3], rec[20].split(':')[0], rec[18].split(':')[0])
        L.SUBTYPE[t] = ':'.join(rec[20].split(':')[:2])


def best1(train, t, k, doms):
    f, b = L._scorer(train, doms), L._scorer(train, doms, rev=True)
    cands = [c for c, n in Counter(c for x in train for c in x).most_common(150)]
    return max(cands, key=lambda c: (f(t, t[:k] + (c,) + t[k + 1:]) + b(t, t[:k] + (c,) + t[k + 1:]), c))


def best2(train, t, ks, doms):
    f, b = L._scorer(train, doms), L._scorer(train, doms, rev=True)
    cands = [c for c, n in Counter(c for x in train for c in x).most_common(60)]
    best, bs = None, None
    for a in cands:
        for c in cands:
            u = list(t)
            u[ks[0]], u[ks[1]] = a, c
            u = tuple(u)
            sc = f(t, u) + b(t, u)
            if bs is None or sc > bs:
                best, bs = (a, c), sc
    return best


def main():
    rd = R.Round('Three-hundred-and-seventy-seventh registered predictions: goal loop 23, restoration with the object-kind models', 'predict_test377b')
    A, B, rowsA, recs, F = R.load_all()
    DL, tr, te = data()
    byc = {}
    for rec in recs.values():
        if rec[1]:
            byc.setdefault(rec[1], rec)
    one = []
    with open(os.path.join(HERE, 'results', 'restoration_m77.tsv'), encoding='utf-8') as fh:
        for r in csv.DictReader(fh, delimiter='\t'):
            if r['reading'] not in ('no match', 'conflict', 'illegible') and len(r['text_with_gap'].split()) >= 4:
                one.append((recs.get(r['id']) or byc.get(r['cisi']), tuple(r['text_with_gap'].split()), r['reading']))
    for sid, cisi, li, k, t, g in new_cases():
        one.append((recs.get(sid), t, g))
    p1 = d1 = 0
    for rec, t, g in one:
        k = t.index('???')
        setmeta(t, rec)
        train = [u for u in DL if not copy_of(t, k, u)]
        a, b = best1(train, t, k, []), best1(train, t, k, L.BASE_DOMAINS)
        p1 += a == g
        d1 += b == g
    rd.say('- single gaps: %d cases; plain %d right, domains %d.' % (len(one), p1, d1))
    p2 = d2 = n2 = 0
    for cid, t, ks, gold in cases2():
        rec = recs.get(cid) or byc.get(cid)
        setmeta(t, rec)
        train = [u for u in DL if not copy2(t, ks, u)]
        a, b = best2(train, t, ks, []), best2(train, t, ks, L.BASE_DOMAINS)
        for j in range(2):
            n2 += 1
            p2 += a[j] == gold[j]
            d2 += b[j] == gold[j]
    rd.say('- two-gap lines: %d signs; plain %d right, domains %d.' % (n2, p2, d2))
    rd.say()
    rd.rec('RS1', 'single gaps: domains right more often than plain', '%d against %d of %d' % (d1, p1, len(one)), d1 > p1)
    rd.rec('RS2', 'two-gap lines: domains right more often than plain', '%d against %d of %d' % (d2, p2, n2), d2 > p2)
    rd.rec('P', 'progress rule: the restoration line rises (domains total above plain total)', '%d against %d' % (d1 + d2, p1 + p2), d1 + d2 > p1 + p2)
    rd.finish()


if __name__ == '__main__':
    main()
