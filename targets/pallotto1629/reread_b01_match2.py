"""Like reread_b01_match.py but reports hit density per 40-line bin of the edition (reread batch b01)."""
import collections, os, sys, pickle
HERE = os.path.dirname(os.path.abspath(__file__)); sys.path.insert(0, HERE)
import reread_b01_match as M
lines, text, owner, numof, idx = M.edition_index()
recs = sys.argv[1:] or [f[:-4] for f in sorted(os.listdir(os.path.join(HERE, 'decode')))]
cache = os.path.join(HERE, 'reread_b01', 'docstrings.pkl')
ds = pickle.load(open(cache, 'rb')) if os.path.exists(cache) else {}
for r in recs:
    if r not in ds: ds[r] = M.doc_strings(r)
    b = collections.Counter()
    for s in ds[r]:
        for p in range(len(s) - M.W + 1):
            ps = idx.get(s[p:p + M.W], [])
            if 0 < len(ps) <= 2:
                for q in ps: b[owner[q] // 40] += 1
    print(r, ' '.join(f'{k*40+1}:{v}' for k, v in sorted(b.items()) if v >= 8))
pickle.dump(ds, open(cache, 'wb'))
