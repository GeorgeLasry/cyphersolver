"""Which bulk_all record groups are complete, with hit counts by kind."""
import json, os, sys, collections
OUT = os.path.join(os.path.dirname(__file__), '..', 'nara_reels', 'out')
sizes = {r[0]: r[1] for r in json.load(open(os.path.join(OUT, 'rg_sizes.json')))}
rows = []
for f in sorted(os.listdir(OUT)):
    if not (f.startswith('done_') and f.endswith('_all.txt')): continue
    rg = f[5:-8]
    done = len([l for l in open(os.path.join(OUT, f)) if l.strip()])
    c = collections.Counter()
    p = os.path.join(OUT, f'{rg}_all.jsonl')
    if os.path.exists(p):
        for l in open(p, encoding='utf-8'):
            try: c[json.loads(l)['kind']] += 1
            except Exception: pass
    rows.append((rg, done, sizes.get(rg), done >= (sizes.get(rg) or 10**9), dict(c)))
for r in rows:
    if '-a' in sys.argv or r[3]: print(*r, sep='\t')
