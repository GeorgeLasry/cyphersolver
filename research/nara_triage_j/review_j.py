"""review_i.py <rg> [--frames N] [--words N]: condensed review of a bulk_all group (slice J, slim files from slim.py).
Like nara_triage_h/review.py, but for big groups: every desc, every phrase (boilerplate filtered), word hits
summarised by series and match, the stronger word matches printed (one per item+match, capped), and frame/letters/caps
items capped to the N with most hits (one solid frame each)."""
import json, os, sys, re, collections
OUT = os.path.join(os.path.dirname(__file__), '..', 'nara_reels', 'out')
BOILER = re.compile(r'errors .{0,3}cipher|obscure mess|CLASSES OF SERVICE|with ciphers|INSERT CIPHERS|Code messages, consisting'
                    r'|in cipher mode|key was missing|cipher machine|cipher device|crypto ?aid|SIGABA|M-209|converter m', re.I)
WEAK = re.compile(r'^(cipher|ciphers|cypher|cyphers|in code|code book|code books|decipherable|code letter|cryptographic|cryptography)$', re.I)
args = sys.argv[1:]
NF = int(args[args.index('--frames') + 1]) if '--frames' in args else 40
NW = int(args[args.index('--words') + 1]) if '--words' in args else 300
rgs = [a for a in args if not a.startswith('--') and not a.isdigit()]
for rg in rgs:
    rg = rg if rg.startswith(('rg_', 'coll_')) else 'rg_' + rg
    L = [json.loads(l) for l in open(os.path.join(OUT, f'{rg}_slim.jsonl'), encoding='utf-8')]
    print(f'######## {rg}', dict(collections.Counter(d['kind'] for d in L)))
    seen = set()
    for d in L:
        if d['kind'] == 'desc' and d['naId'] not in seen:
            seen.add(d['naId'])
            print('DESC', d['naId'], d.get('level'), '|', ' > '.join(d.get('ancestors') or [])[-80:], '|', re.sub(r'\s+', ' ', d.get('snippet') or d['title'])[:300])
    seen = set()
    for d in L:
        if d['kind'] == 'phrase':
            k = (d['objectId'], d.get('match'))
            if k in seen: continue
            seen.add(k)
            s = d['snippet']; m = (d.get('match') or '').lower(); i = s.lower().find(m)
            if BOILER.search(s): continue
            print('PHRASE', d['naId'], d.get('file'), d['title'][:50], '|', m, '|', re.sub(r'\s+', ' ', s[max(0, i - 180):i + 160]))
    W = [d for d in L if d['kind'] == 'word' and not BOILER.search(d['snippet'])]
    ser = collections.Counter(((d.get('ancestors') or [''])[-1][:70], d['title'][:50]) for d in W)
    print('WORD by series/title (top 40):')
    for (a, t), n in ser.most_common(40): print(f'   {n:5d} {a} | {t}')
    print('WORD matches:', dict(collections.Counter((d.get('match') or '').lower() for d in W).most_common(25)))
    seen = set(); n = 0
    for d in W:
        m = (d.get('match') or '').lower()
        if WEAK.match(m): continue
        k = (d['naId'], m)
        if k in seen: continue
        seen.add(k); n += 1
        if n > NW: break
        s = d['snippet']; i = s.lower().find(m)
        print('WORD', d['naId'], d.get('file'), d['title'][:45], '|', m, '|', re.sub(r'\s+', ' ', s[max(0, i - 150):i + 130]))
    items = collections.defaultdict(list)
    for d in L:
        if d['kind'] in ('frame', 'letters', 'caps'):
            items[(d['naId'], d['title'][:70], d['kind'])].append(d)
    print(f'ITEMS: {len(items)} (showing top {NF} per kind)')
    top = []
    for kk in ('frame', 'letters', 'caps'):
        top += sorted([x for x in items.items() if x[0][2] == kk], key=lambda x: -len(x[1]))[:NF]
    for (nid, t, k), v in top:
        if k == 'frame': v.sort(key=lambda d: d['words'] / max(1, d['nums']))
        elif k == 'caps': v.sort(key=lambda d: d.get('ic', 1))
        print(f'{k.upper()} {nid} x{len(v)} | {t} | {" ".join(str(x) for x in (v[0].get("microform") or [])[:1])} {v[0].get("dates") or ""} | {" > ".join(v[0].get("ancestors") or [])[-60:]}')
        d = v[0]
        print('    ', d.get('file'), {x: d.get(x) for x in ('nums', 'run', 'words', 'ic', 'ncaps') if x in d}, re.sub(r'\s+', ' ', d['snippet'])[:200])
