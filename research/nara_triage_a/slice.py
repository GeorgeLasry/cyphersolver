"""Extract the 1789-1906 RG 59 slice from research/nara_reels/out/rg_59.jsonl into slice.jsonl (grouped by pub)."""
import json, re, os, collections
HERE = os.path.dirname(os.path.abspath(__file__))
SRC = os.path.join(HERE, '..', 'nara_reels', 'out', 'rg_59.jsonl')
LATE = {'M862', 'M367', 'M1442', 'M973', 'T1249', 'M1284', 'M1286', 'M1751'}
LATE_ANC = ('Central Decimal Files', 'Numerical Files', 'Civilian Internee', 'Purport Lists', 'Passport Applications',
            'Polish Ministry')

def years(d):
    ys = []
    for x in d.get('dates') or []:
        if isinstance(x, dict) and x.get('year'):
            ys.append(x['year'])
    ys += [int(y) for y in re.findall(r'\b(1[789]\d\d)\b', d['title'])]
    return ys

out = []
for line in open(SRC, encoding='utf-8'):
    d = json.loads(line)
    pub = (d.get('microform') or ['-'])[0]
    anc = ' > '.join(d.get('ancestors') or [])
    if pub in LATE or any(a in anc for a in LATE_ANC):
        continue
    ys = years(d)
    if ys and min(ys) > 1906:
        continue
    if ys and max(ys) < 1789:
        pass  # keep pre-1789 strays (none expected), they are noted
    d['pub'] = pub
    d['yr'] = min(ys) if ys else None
    out.append(d)
with open(os.path.join(HERE, 'slice.jsonl'), 'w', encoding='utf-8') as f:
    for d in out:
        f.write(json.dumps(d, ensure_ascii=False) + '\n')
c = collections.Counter((d['pub'], d['kind']) for d in out)
print(len(out))
