"""Fetch Query=Detail for every Calames hit (item + ancestors), keep the item's own xml and ancestors' cote/title."""
import json, re, sys, urllib.request, concurrent.futures as cf, time
hits = json.load(open('calames_hits.json', encoding='utf-8'))
out = {}
def get(i):
    url = 'https://calames.abes.fr/prod/EadSearch.aspx?Query=Detail&id=' + i
    for k in range(4):
        try:
            return i, urllib.request.urlopen(urllib.request.Request(url, headers={'User-Agent': 'Mozilla/5.0'}), timeout=90).read().decode('utf-8', 'replace')
        except Exception:
            time.sleep(3 * (k + 1))
    return i, ''
ids = [h['id'] for h in hits]
with cf.ThreadPoolExecutor(4) as ex:
    for n, (i, x) in enumerate(ex.map(get, ids)):
        out[i] = x
        if n % 200 == 0:
            print(n, flush=True)
            json.dump(out, open('calames_detail.json', 'w', encoding='utf-8'), ensure_ascii=False)
json.dump(out, open('calames_detail.json', 'w', encoding='utf-8'), ensure_ascii=False)
print('done', len(out))
