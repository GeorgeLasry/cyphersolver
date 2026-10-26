"""Score table.tsv on glossed runs of unglossed_*.txt: share of sure decoded values (2+ letters) found in the run's own
gloss vs in another run's gloss. Usage: python validate.py [fold 0|1|all]  (fold = runs with index % 2 == fold)"""
import sys
from align import runs, nz
from decode import load
from table import norm_group
fold = sys.argv[1] if len(sys.argv) > 1 else 'all'
M, B = load()
R = [(ct, pt) for i, (t, ct, pt) in enumerate(runs()) if fold == 'all' or i % 2 == int(fold)]
def score(ct, pt):
    h = t = 0
    for g in ct:
        n, k = norm_group(g); v = M.get(k) or B.get(n)
        if v and v[1] and len(nz(v[0])) >= 2:
            t += 1; h += nz(v[0]) in pt
    return h, t
own = [score(c, p) for c, p in R]; oth = [score(R[i][0], R[(i + 5) % len(R)][1]) for i in range(len(R))]
H, T = map(sum, zip(*own)); H2, T2 = map(sum, zip(*oth))
print(f'fold {fold}: {len(R)} runs; sure values in own gloss {H}/{T} {H/T:.0%}; in another gloss {H2}/{T2} {H2/T2:.0%}')
