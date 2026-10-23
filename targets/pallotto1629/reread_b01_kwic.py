"""KWIC of unknown three-digit groups across the 28 decodes, with the edition alignments (reread batch b01).
    python reread_b01_kwic.py [min_count] > reread_b01/kwic.txt"""
import collections, json, os, re, sys
HERE = os.path.dirname(os.path.abspath(__file__))
mn = int(sys.argv[1]) if len(sys.argv) > 1 else 3
ctx = collections.defaultdict(list)
for f in sorted(os.listdir(os.path.join(HERE, 'reread_b01'))):
    if not f.endswith('_dec.txt'): continue
    rec = f[:4]
    for ln in open(os.path.join(HERE, 'reread_b01', f), encoding='utf-8'):
        if not ln.startswith('C: '): continue
        s = ln[3:].rstrip()
        for m in re.finditer(r'\[(\d{3})\]', s):
            ctx[m.group(1)].append(f'{rec}: ' + s[max(0, m.start() - 45):m.start()] + ' <' + m.group(1) + '> ' + s[m.end():m.end() + 35])
g = json.load(open(os.path.join(HERE, 'reread_b01', 'all_groups.json'), encoding='utf-8'))
ev = collections.defaultdict(list)
for x in g:
    if x['rate'] <= 0.55: ev[x['code']].append(x['raw'].strip())
for c, v in sorted(ctx.items(), key=lambda kv: -len(kv[1])):
    if len(v) < mn: continue
    e = collections.Counter(ev.get(c, [])).most_common(5)
    print(f'== {c} n={len(v)}  ED: {e}')
    step = max(1, len(v) // 7)
    for x in v[::step][:7]: print('   ', x)
