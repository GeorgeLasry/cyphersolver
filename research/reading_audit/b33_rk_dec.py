"""rakoczi1711 R483: per line, each cipher run decoded group by group with the rebuilt key (value, or <g> if unknown;
'*' marks a value seen once). usage: python b33_rk_dec.py [page]"""
import json, re, sys, glob, os
R = r'C:/Users/dbour/cypher/.worktrees/reading-gate/targets/rakoczi1711/'
K = json.load(open(R + 'R483_key_rebuilt.json', encoding='utf8'))
def v(g):
    g2 = re.sub(r'\D', '', g)
    if g2 in K:
        return K[g2]['value'] + ('*' if K[g2]['of'] < 2 else '')
    return '<%s>' % g2
pages = sys.argv[1:] or ['1', '2', '3', '4', '5', '6']
for p in pages:
    print('[p%s]' % p); n = 0
    for l in open(R + 'tr/R483_p%s.txt' % p, encoding='utf8'):
        if not l.startswith('C:'): continue
        n += 1
        parts = re.split(r'(\{clear:[^}]*\})', l[2:].strip())
        out = []
        for part in parts:
            if part.startswith('{'): out.append('[clr]'); continue
            gs = [g for g in part.split() if re.search(r'\d', g)]
            if gs: out.append('.'.join(v(g) for g in gs))
        print('%02d %s' % (n, ' '.join(out)))
