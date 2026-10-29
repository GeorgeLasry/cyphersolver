"""Blacklight/ArcLight JSON harvester (UNC, Princeton). usage: bl_harvest.py unc|princeton term..."""
import sys, json, time, os, urllib.request, urllib.parse
BASES = {'unc': 'https://finding-aids.lib.unc.edu', 'princeton': 'https://findingaids.princeton.edu'}
UA = 'Mozilla/5.0 (cyphersolver research catalogue sweep)'
def flat(v):
    if isinstance(v, dict):
        if 'attributes' in v and 'value' in v['attributes']: return flat(v['attributes']['value'])
        return {k: flat(x) for k, x in v.items() if k not in ('id', 'type', 'label')}
    if isinstance(v, list): return [flat(x) for x in v]
    return v
def run(site, term, maxpages=30):
    out = []
    for p in range(1, maxpages + 1):
        url = f"{BASES[site]}/catalog.json?q={urllib.parse.quote(term)}&per_page=100&page={p}"
        req = urllib.request.Request(url, headers={'User-Agent': UA, 'Accept': 'application/json'})
        try: d = json.load(urllib.request.urlopen(req, timeout=60))
        except Exception as e: print('ERR', site, term, p, e); break
        for r in d['data']:
            a = r['attributes']; rec = {'id': r['id'], 'site': site, 'term': term}
            for k, v in a.items():
                if k in ('highlight', 'breadcrumbs'): continue
                rec[k] = flat(v)
            h = a.get('highlight'); rec['hl'] = flat(h) if h else None
            out.append(rec)
        tot = d['meta']['pages']
        if not tot.get('next_page'): break
        time.sleep(3)
    return out, d['meta']['pages'].get('total_count')
if __name__ == '__main__':
    site = sys.argv[1]
    f = f'raw/{site}.jsonl'
    for term in sys.argv[2:]:
        recs, n = run(site, term)
        print(site, term, n, len(recs), flush=True)
        with open(f, 'a', encoding='utf-8') as fh:
            for r in recs: fh.write(json.dumps(r, ensure_ascii=False) + '\n')
        time.sleep(3)
