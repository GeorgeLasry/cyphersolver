"""Score editions on the anchors that fall within +-6 pages of Entick 1800 (the ~430-pp chain)."""
import sys, re, json
import test_editions as t
C = sys.argv[1]
ref = 'bim_eighteenth-century_enticks-new-spelling-di_entick-john_1800'
def words(i):
    leaves, _ = t.pages(C, i)
    return [set(re.findall(r'[a-z]+', x)) for x in leaves]
def nearest(W, p, w, k):
    c = [l - k for l in range(len(W)) if w in W[l]]
    return min(c, key=lambda x: abs(x - p)) if c else None
W0 = words(ref)
chain = [a for a in t.anchors() if (n := nearest(W0, a[0], a[3], 44)) is not None and abs(n - a[0]) <= 6]
print('chain size', len(chain), file=sys.stderr)
for i in sys.argv[2:]:
    try:
        W = words(i)
        best = max(range(-10, 80), key=lambda k: sum(1 for p, r, c, w in chain if 0 <= p + k < len(W) and w in W[p + k]))
        exact = sum(1 for p, r, c, w in chain if 0 <= p + best < len(W) and w in W[p + best])
        within1 = sum(1 for p, r, c, w in chain if any(0 <= p + best + d < len(W) and w in W[p + best + d] for d in (-1, 0, 1)))
        print(json.dumps(dict(id=i[-30:], leaves=len(W), offset=best, exact=exact, within1=within1, n=len(chain))), flush=True)
    except Exception as e:
        print(i, repr(e), flush=True)
