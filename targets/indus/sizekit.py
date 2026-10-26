"""Stratified seal-size test (goal run, from set 471): Mantel-Haenszel of large against small square seals (median
first dimension) over length band x site, for a feature of the text."""
from statistics import median

from predict_test379 import mantel_haenszel
from predict_test430 import seals

_SQ = None


def size_test(feat, kind=31):
    global _SQ
    if _SQ is None:
        _SQ = seals(kind)
    cut = median(s for s, t, x in _SQ)
    band = lambda t: min(max(len(t), 2), 7)
    tabs = []
    for k in sorted({(band(t), x) for s, t, x in _SQ}):
        lg = [feat(t) for s, t, x in _SQ if (band(t), x) == k and s > cut]
        sm = [feat(t) for s, t, x in _SQ if (band(t), x) == k and s <= cut]
        tabs.append([[sum(lg), len(lg) - sum(lg)], [sum(sm), len(sm) - sum(sm)]])
    return mantel_haenszel(tabs)
