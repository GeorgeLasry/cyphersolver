"""Size audits with motif strata (goal run, from set 497): square seals with a motif and a size; Mantel-Haenszel of large
against small over length band x site x motif (unicorn / other), and within unicorn seals."""
from statistics import median

import rtools as R
from predict_test379 import mantel_haenszel

_ROWS = None


def rows():
    global _ROWS
    if _ROWS is None:
        A, B, rowsA, recs, F = R.load_all()
        out = []
        for r in F:
            rec = recs.get(r['sealid'])
            if rec and str(rec[20]).startswith('SEAL:S') and r['flat']:
                m = str(rec[18]).split(':')[0]
                try:
                    sz = float(rec[31])
                except (TypeError, ValueError):
                    sz = 0
                if m not in ('', '-', 'None') and sz > 0:
                    out.append((tuple(r['flat']), m == 'Bull1', r['site'], sz))
        _ROWS = out
    return _ROWS


def size_motif(feat, unicorn_only=False):
    R_ = [r for r in rows() if r[1] or not unicorn_only]
    cut = median(s for t, u, x, s in rows())
    band = lambda t: min(max(len(t), 2), 7)
    tabs = []
    for k in sorted({(band(t), x, u) for t, u, x, s in R_}):
        lg = [feat(t) for t, u, x, s in R_ if (band(t), x, u) == k and s > cut]
        sm = [feat(t) for t, u, x, s in R_ if (band(t), x, u) == k and s <= cut]
        tabs.append([[sum(lg), len(lg) - sum(lg)], [sum(sm), len(sm) - sum(sm)]])
    return mantel_haenszel(tabs)
