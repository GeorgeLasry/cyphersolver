"""Grid-code signature test (Tomokiyo Item 4 / 8B structure): numbers >= LO are laid out row by row in a table of
k columns, each column one initial letter, so the column (n - base) mod k carries information.  For each k, score the
token-weighted chi-square of the residues and compare with the same statistic after randomly relabelling the
distinct high numbers (permutation null).  Reports z and empirical p."""
import json, random, collections, os, sys
here = os.path.dirname(os.path.abspath(__file__))
toks = json.load(open(os.path.join(here, sys.argv[1] if len(sys.argv) > 1 else 'tokens.json')))
LO = int(sys.argv[2]) if len(sys.argv) > 2 else 100
hi = [t for t in toks if t >= LO]
cnt = collections.Counter(hi); vals = sorted(cnt)
span = list(range(LO, max(toks) + 1))
def chi(assign, k):
    r = collections.Counter()
    for v, c in cnt.items(): r[assign[v] % k] += c
    n = sum(r.values()); e = n / k
    return sum((r[i] - e) ** 2 / e for i in range(k))
ident = {v: v for v in vals}
rnd = random.Random(1)
print('high tokens', len(hi), 'distinct', len(vals))
for k in range(5, 31):
    obs = chi(ident, k)
    null = []
    for _ in range(400):
        sample = rnd.sample(span, len(vals)); a = dict(zip(vals, sample))
        null.append(chi(a, k))
    mu = sum(null) / len(null); sd = (sum((x - mu) ** 2 for x in null) / len(null)) ** .5
    p = (1 + sum(x >= obs for x in null)) / (1 + len(null))
    print('k=%2d chi=%7.1f null=%6.1f±%5.1f z=%5.2f p=%.3f' % (k, obs, mu, sd, (obs - mu) / sd, p))
