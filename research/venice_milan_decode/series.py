import json, re, collections
D = 'research/catalogue_harvest/decode/'
recs = {}
for f in ['views.jsonl','views_b.jsonl','views_c.jsonl']:
    for line in open(D+f, encoding='utf-8'):
        r = json.loads(line)
        if r.get('record_type') in ('1','3',None) and r.get('status') != '1': recs[r['id']] = r
json.dump(recs, open('research/venice_milan_decode/inscope.json','w',encoding='utf-8'), ensure_ascii=False)
g = collections.defaultdict(list)
for r in recs.values():
    h = re.sub(r'[\d\s.,;:fol\-–rv]+$', '', (r.get('current_holder') or r.get('name') or ''))[:70]
    g[h].append(r)
for h, rs in sorted(g.items(), key=lambda x: x[0]):
    ys = sorted(int(r['start_year']) for r in rs if (r.get('start_year') or '').isdigit())
    snd = collections.Counter((r.get('sender') or '')[:25]+'>'+(r.get('receiver') or '')[:20]+'@'+(r.get('origin_city') or '')[:12] for r in rs).most_common(2)
    st = collections.Counter(r['status'] for r in rs)
    print(f"{len(rs):4d} {h} | {ys[0] if ys else ''}-{ys[-1] if ys else ''} | {dict(st)} | {snd}")
