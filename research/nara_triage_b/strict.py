"""Frame-level strict filter: many bare 3-5 digit non-year groups, not sequential, little table vocabulary.
    python research/nara_triage_b/strict.py > research/nara_triage_b/strict.tsv"""
import re, sys, os, json
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from triage import load, TABLE
sys.stdout.reconfigure(encoding='utf-8')
EX = re.compile(r'Lincoln|Marshals|Aqueduct|Diplomatic Instructions|Subject-Numeric|Mongoose')
for rg in (59, 84, 76):
    for h in load(rg):
        if h['kind'] != 'frame' or EX.search(' '.join(h['ancestors'])):
            continue
        s = h['snippet']
        toks = s.split()
        g = [t for t in toks if re.fullmatch(r'\d{3,5}', t) and not (1850 <= int(t) <= 1950)]
        if len(g) < 12:
            continue
        v = [int(t) for t in g]
        seq = sum(1 for a, b in zip(v, v[1:]) if abs(b - a) <= 20) / (len(v) - 1)
        rep = 1 - len(set(g)) / len(g)
        tab = len(TABLE.findall(s))
        dotted = sum(1 for t in toks if re.search(r'\d[.,]\d', t))
        if seq > 0.25 or tab > 2 or dotted > 3 or rep > 0.4:
            continue
        print('\t'.join(map(str, [rg, h['naId'], ','.join(h['microform']) or '-', h['file'], h['objectId'], len(g),
                                  round(seq, 2), round(rep, 2), tab, h['title'][:60], ' '.join(toks)[:300]])))
