"""r2c (23 Oct 2026): kurtz1639 lines whose decode (key.json + overrides) matches a regex; prints stem side i/n.
    python research/reading_audit/r2c_grep.py R3813 "salVIo" "#f-cross=VI" """
import json, sys, os, re, glob
sys.path.insert(0, 'targets/kurtz1639')
from parse import tokens_of
from solve2 import value
k = json.load(open('targets/kurtz1639/key.json', encoding='utf-8'))
h = {int(a[1:]): b for a, b in k.items() if a.startswith('H')}
s = {a: b for a, b in k.items() if not a.startswith('H')}
for kv in filter(None, (sys.argv[3] if len(sys.argv) > 3 else '').split(',')):
    a, b = kv.split('='); s[a] = b
for f in sorted(glob.glob(f'targets/kurtz1639/tr/IMG_{sys.argv[1]}_*.txt')):
    side, lines = 'F', {}
    for l in open(f, encoding='utf8'):
        t = l.strip()
        if t.startswith('## '):
            side = 'L' if 'left' in t.lower() else 'R' if 'right' in t.lower() else 'F'; continue
        if not t or t == '#' or t.startswith('# ') or t.lower().startswith('legend'): continue
        lines.setdefault(side, []).append(t)
    for sd, ls in lines.items():
        for i, t in enumerate(ls):
            d = ''.join(('{' + it[1] + '}') if it[0] == 'clear' else value(it[1], h, s) for it in tokens_of(t))
            if re.search(sys.argv[2], d):
                print(os.path.basename(f)[:-4], sd, i + 1, len(ls), '|', t, '|', d)
