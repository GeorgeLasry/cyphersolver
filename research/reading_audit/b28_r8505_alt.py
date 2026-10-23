"""b28: for every occurrence of a sign, compare the run's word-segmentation score under each candidate letter.
    python research/reading_audit/b28_r8505_alt.py <sign> <letters e.g. at> [glob]"""
import sys, glob, re
sys.argv_saved = sys.argv; sys.argv = ['x']
sys.path.insert(0, 'research/reading_audit')
import b28_r8505_decode as D
sign, letters = sys.argv_saved[1], sys.argv_saved[2]
files = sys.argv_saved[3:] or sorted(glob.glob('targets/harley1582r8505/final/f*.txt'))
def score(s):
    n = len(s); best = [-1e18]*(n+1); best[0] = 0
    for i in range(1, n+1):
        b = best[i-1] + D.UNK
        for j in range(max(0, i-18), i):
            lp = D.VOC.get(s[j:i])
            if lp is not None and best[j] + lp - D.BCOST > b: b = best[j] + lp - D.BCOST
        best[i] = b
    return best[n]
tally = {c: 0 for c in letters}
for fn in files:
    for line in open(fn, encoding='utf-8'):
        p = [x.strip() for x in line.rstrip('\n').split('|')]
        if len(p) < 3: continue
        toks = [t.rstrip('?') for t in ' '.join(p[2::2]).replace('/', ' ').split()]
        for k, t in enumerate(toks):
            if t != sign: continue
            lo, hi = max(0, k-9), min(len(toks), k+10)
            res = {}
            for c in letters:
                s = ''.join('m' if re.fullmatch(r'[:.]+|:[234]', x) else (c if j == k else ('' if x.startswith('#') else D.key.get(x, '?'))) for j, x in enumerate(toks[lo:hi], lo))
                res[c] = (score(s), s)
            bestc = max(res, key=lambda c: res[c][0]); tally[bestc] += 1
            print(p[0], k, bestc, ' '.join('%s:%.1f %s' % (c, res[c][0], res[c][1]) for c in letters))
print(tally)
