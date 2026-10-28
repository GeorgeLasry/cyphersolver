"""caps.py: slice L, caps hits from the caps/word rerun of the early groups, one line per item (longest run first),
with the run of capital-letter groups shown. Items whose best run is under 8 groups are dropped."""
import json, os, re, glob, collections
OUT = os.path.join(os.path.dirname(__file__), '..', 'nara_reels', 'out')
RUN = re.compile(r'(?:\b[A-Z]{4,7}\b[\s.,]+){6,}')
by = collections.defaultdict(list)
for f in sorted(glob.glob(os.path.join(OUT, 'rg_*_cw.jsonl'))):
    for l in open(f, encoding='utf-8'):
        d = json.loads(l)
        if d['kind'] == 'caps':
            d['rg'] = os.path.basename(f)[:-9]; by[d['naId']].append(d)
rows = []
for nid, v in by.items():
    best = max(v, key=lambda d: d.get('run', 0))
    if best.get('run', 0) < 8: continue
    rows.append((best['rg'], -best['run'], nid, len(v), best))
rows.sort()
print(len(rows), 'items')
for rg, r, nid, n, d in rows:
    s = re.sub(r'\s+', ' ', d['snippet']); m = RUN.search(s)
    ctx = s[max(0, m.start() - 80):m.end() + 40] if m else s[:240]
    print(f"== {rg} {nid} x{n} run{-r} ic{d.get('ic')} | {d['title'][:60]} | {' '.join(d.get('microform') or [])} | {' > '.join(d.get('ancestors') or [])[-60:]}")
    print('    ', d['file'], '|', ctx[:330])
