"""r2c (23 Oct 2026): kurtz1639 kwic with record name, comparing key.json and an override (sign=value,...).
    python research/reading_audit/r2c_kwic.py TOKEN "k=to,m=va,29=q" [width]"""
import json, sys, os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', '..', 'targets', 'kurtz1639'))
os.chdir(os.path.join(os.path.dirname(__file__), '..', '..', 'targets', 'kurtz1639'))
from parse import load
from solve2 import value
k = json.load(open('key.json', encoding='utf-8'))
h = {int(a[1:]): b for a, b in k.items() if a.startswith('H')}
s = {a: b for a, b in k.items() if not a.startswith('H')}
s2 = dict(s)
for kv in filter(None, sys.argv[2].split(',')):
    a, b = kv.split('='); s2[a] = b
w = int(sys.argv[3]) if len(sys.argv) > 3 else 10
runs, _ = load()
tgt = sys.argv[1]
for f, r in runs:
    for i, t in enumerate(r):
        if t == tgt:
            d = lambda S: ''.join(value(x, h, S) for x in r[max(0, i-w):i]) + '[' + value(t, h, S) + ']' + ''.join(value(x, h, S) for x in r[i+1:i+w+1])
            print(f'{os.path.basename(str(f))[4:22]:18} {d(s):>50}  |  {d(s2)}')
