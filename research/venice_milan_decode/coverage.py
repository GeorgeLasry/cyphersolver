import json, os, sys, collections
D = 'research/catalogue_harvest/decode/'
lst = json.load(open(D+'list.json', encoding='utf-8'))
views = {}
for f in ['views.jsonl','views_b.jsonl','views_c.jsonl']:
    for line in open(D+f, encoding='utf-8'):
        r = json.loads(line); views[r['id']] = r
c = collections.Counter(); miss = collections.Counter()
for r in lst:
    k = (r['record_type'], r['status']); c[k] += 1
    if r['id'] not in views: miss[k] += 1
print(len(lst), len(views), 'max id', max(int(r['id']) for r in lst))
for k in sorted(c, key=str): print(k, c[k], 'missing views', miss[k])
