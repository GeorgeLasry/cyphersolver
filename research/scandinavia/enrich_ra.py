"""Fetch the JSON-LD for each Riksarkivet hit (ra_hits.jsonl, start year <= 1925) and keep all text fields + IIIF manifest.

    python research/scandinavia/enrich_ra.py -> ra_enriched.jsonl
"""
import json, os, re, time, urllib.request

HERE = os.path.dirname(os.path.abspath(__file__))
UA = {'User-Agent': 'Mozilla/5.0 (cyphersolver research)'}
SKIP = ('Fanritningar', 'Marinens ritningar', 'kyrkoarkiv', 'Troféavbildningar')


def year(d):
    m = re.search(r'(1[0-9]{3})', d or '')
    return int(m.group(1)) if m else 0


def texts(o, out):
    if isinstance(o, dict):
        for k, v in o.items():
            if isinstance(v, str) and k not in ('@id', '@type') and not v.startswith('http'):
                out.append(f'{k}: {v}')
            else:
                texts(v, out)
    elif isinstance(o, list):
        for v in o:
            texts(v, out)


def main():
    rows = [json.loads(l) for l in open(os.path.join(HERE, 'ra_hits.jsonl'), encoding='utf-8')]
    out = os.path.join(HERE, 'ra_enriched.jsonl')
    done = set()
    if os.path.exists(out):
        done = {json.loads(l)['id'] for l in open(out, encoding='utf-8')}
    fh = open(out, 'a', encoding='utf-8')
    for r in rows:
        if r['id'] in done or (year(r['date']) > 1925) or any(s in (r['path'] or '') for s in SKIP):
            continue
        url = f"https://data.riksarkivet.se/archive/{r['id']}.jsonld"
        try:
            with urllib.request.urlopen(urllib.request.Request(url, headers=UA), timeout=60) as f:
                d = json.load(f)
        except Exception as e:
            print('ERR', r['id'], e); continue
        t = []
        texts(d, t)
        imgs = sorted({m for m in re.findall(r'https://lbiiif\.riksarkivet\.se/[^"\s]+', json.dumps(d))})
        r['texts'] = [x for x in t if len(x) > 12][:60]
        r['iiif'] = imgs
        fh.write(json.dumps(r, ensure_ascii=False) + '\n'); fh.flush()
        time.sleep(0.3)


if __name__ == '__main__':
    main()
