"""Contexts of a given code (any length) across all decodes: python reread_b01_ctx.py 776 [max]"""
import os, sys, pickle
HERE = os.path.dirname(os.path.abspath(__file__)); sys.path.insert(0, HERE)
import reread_b01_decode as D
code = sys.argv[1]; mx = int(sys.argv[2]) if len(sys.argv) > 2 else 30
cache = os.path.join(HERE, 'reread_b01', 'decoded.pkl')
docs = pickle.load(open(cache, 'rb')) if os.path.exists(cache) else {}
recs = [f[:-4] for f in sorted(os.listdir(os.path.join(HERE, 'decode')))]
key = os.path.getmtime(D.EXTRA_FILE) if os.path.exists(D.EXTRA_FILE) else 0
if docs.get('_key') != key:
    docs = {'_key': key}
    for r in recs: docs[r] = D.decode_doc(r)
    pickle.dump(docs, open(cache, 'wb'))
n = 0
for r in recs:
    for k, v in docs[r]:
        if k != 'cipher': continue
        for i, (kk, c, t) in enumerate(v):
            if c == code and kk in ('l', 'w', 'u'):
                print(r, D.render(v[max(0, i - 12):i]), '<' + code + '>', D.render(v[i + 1:i + 10]))
                n += 1
                if n >= mx: sys.exit()
