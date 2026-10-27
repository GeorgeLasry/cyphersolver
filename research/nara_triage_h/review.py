"""review.py <rg> [...]: compact dump of a completed bulk_all group for reading.
desc: every distinct title; phrase/word: snippet around the match (dedup per frame); frame/letters/caps: per item,
counts and the 3 most 'solid' frames (fewest words per number / lowest IC)."""
import json, os, sys, re, collections
OUT = os.path.join(os.path.dirname(__file__), '..', 'nara_reels', 'out')
BOILER = re.compile(r'errors .{0,3}cipher|obscure mess|CLASSES OF SERVICE|with ciphers|INSERT CIPHERS|Code messages, consisting', re.I)
WORD_SKIP = re.compile(r'^(in code|code book|code books|ciphers|decipherable|code letter)$', re.I)
for rg in sys.argv[1:]:
    rg = rg if rg.startswith(('rg_', 'coll_')) else 'rg_' + rg
    L = [json.loads(l) for l in open(os.path.join(OUT, f'{rg}_all.jsonl'), encoding='utf-8')]
    print(f'######## {rg}', dict(collections.Counter(d['kind'] for d in L)))
    seen = set()
    for d in L:
        if d['kind'] == 'desc' and d['naId'] not in seen:
            seen.add(d['naId'])
            print('DESC', d['naId'], d.get('level'), '|', ' > '.join(d.get('ancestors') or [])[-80:], '|', re.sub(r'\s+', ' ', d.get('snippet') or d['title'])[:260])
    seen = set()
    for d in L:
        if d['kind'] in ('phrase', 'word'):
            k = (d['objectId'], d.get('match'))
            if k in seen: continue
            seen.add(k)
            s = d['snippet']; m = (d.get('match') or '').lower(); i = s.lower().find(m)
            if BOILER.search(s): continue
            print(d['kind'].upper(), d['naId'], d.get('file'), d['title'][:40], '|', m, '|', s[max(0, i - 160):i + 140])
    items = collections.defaultdict(list)
    for d in L:
        if d['kind'] in ('frame', 'letters', 'caps'):
            items[(d['naId'], d['title'][:70], d['kind'])].append(d)
    for (n, t, k), v in sorted(items.items(), key=lambda x: -len(x[1])):
        if k == 'frame':
            v.sort(key=lambda d: d['words'] / max(1, d['nums']))
        elif k == 'caps':
            v.sort(key=lambda d: d.get('ic', 1))
        print(f'{k.upper()} {n} x{len(v)} | {t} | {" ".join(str(x.get("microform") or "") for x in v[:1])} {v[0].get("dates") or ""}')
        for d in v[:2]:
            print('    ', d.get('file'), {x: d.get(x) for x in ('nums', 'run', 'words', 'ic', 'ncaps') if x in d}, re.sub(r'\s+', ' ', d['snippet'])[:220])
