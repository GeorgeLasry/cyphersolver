"""Tests for session-2 goal loops (26 Oct 2026): discovery on A, replication on B (Mahadevan's lines not in A)."""
import random
from collections import Counter, defaultdict

import rtools as R
from scipy.stats import binomtest
from signs import load

_AB = None


def ab():
    global _AB
    if _AB is None:
        A, B, *_ = R.load_all()
        DA = sorted({tuple(t) for t in A})
        DB = sorted({tuple(ln) for r in load(only_m77=True) for ln in r['seq'] if ln} - set(DA))
        _AB = (DA, DB)
    return _AB


def predict_rep(rule_a, check_b, minb=3):
    """rule_a(DA) -> {item: predicted label}; check_b(DB, item) -> (label on B, n on B). Share of items whose B label
    matches, binomial against the B base rate of agreement by chance (0.5 when binary)."""
    DA, DB = ab()
    pred = rule_a(DA)
    hits = n = 0
    for it, lab in pred.items():
        lb, nb = check_b(DB, it)
        if nb >= minb:
            n += 1
            hits += lb == lab
    p = binomtest(hits, n, 0.5, alternative='greater').pvalue if n else 1.0
    return hits, n, p


def ending_pref(S, g):
    c = Counter(t[i + 1] for t in S for i in range(len(t) - 1) if t[i] == g and t[i + 1] in R.END)
    n = sum(c.values())
    return (c.most_common(1)[0][0] if n else None), n
