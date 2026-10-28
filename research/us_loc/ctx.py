"""Fetch transcription text for FULLTEXT hits and keep the context around each cipher word (Oct 2026 LoC sweep).

    python ctx.py [collection-substring ...]   -> context.json  {item_id: {title, url, snippets: [...]}}

Uses the item JSON (fo=json) for the text-file URLs; when an item has many pages it asks the segment search
(fa=segmentof:...&q=term) which pages match and only reads those. Same 3.2 s spacing as harvest.py.
"""
import json, os, re, sys, urllib.parse
import locapi

HERE = os.path.dirname(os.path.abspath(__file__))
WORD = re.compile(r'cipher|cypher|chiffr|cifra|cryptog|decod|in code|code word|code book|secret writing|invisible ink|sympathetic ink|nomenclat', re.I)
SKIP = ['Walt Whitman', 'Motion picture', 'Oral History', 'AIDS', 'Lomax', 'Federal Writer', 'Folk Music',
        'Bernstein', 'Rickey', 'veterans history', 'Farm Security']


def text_urls(item):
    urls = []
    for res in item.get('resources', []):
        if res.get('fulltext_file'):
            urls.append(res['fulltext_file'])
            continue
        for f in res.get('files', []):
            for x in f:
                if x.get('mimetype') == 'text/plain' and x.get('url') and 'word-coordinates' not in x['url']:
                    urls.append(x['url'])
    return urls


def fetch_text(url):
    import urllib.request, time
    wait = locapi.GAP - (time.time() - locapi._last[0])
    if wait > 0:
        time.sleep(wait)
    locapi._last[0] = time.time()
    req = urllib.request.Request(url, headers={'User-Agent': locapi.UA})
    try:
        with urllib.request.urlopen(req, timeout=60) as r:
            return r.read().decode('utf-8', 'replace')
    except Exception as e:
        if getattr(e, 'code', None) == 403:
            raise locapi.Blocked(url)
        return ''


def main():
    want = sys.argv[1:]
    hits = json.load(open(os.path.join(HERE, 'hits.json'), encoding='utf-8'))
    cp = os.path.join(HERE, 'context.json')
    ctx = json.load(open(cp, encoding='utf-8')) if os.path.exists(cp) else {}
    n = 0
    for k, h in hits.items():
        if k in ctx:
            continue
        sc = h.get('source_collection') or ''
        if isinstance(sc, list):
            sc = ' '.join(sc)
        blob = sc + ' ' + ' '.join(h.get('partof', [])) + ' ' + (h.get('title') or '')
        if want and not any(w.lower() in blob.lower() for w in want):
            continue
        if any(s.lower() in blob.lower() for s in SKIP):
            continue
        meta = ' '.join([h.get('title') or ''] + h.get('notes', []))
        if WORD.search(meta):
            continue  # catalogue record already says cipher; no transcription needed
        url = h.get('url') or k
        if 'loc.gov/item/' not in url and 'loc.gov/resource/' not in url:
            continue
        try:
            item = locapi.get(url.split('?')[0] + '?fo=json')
            if not item:
                continue
            urls = text_urls(item)
            if len(urls) > 8 and h.get('segments'):
                # ask which pages match
                seg = h['segments'][0]['link']
                pages = []
                sd = locapi.get(seg.replace('c=100', 'c=50'))
                for r in (sd or {}).get('results', []):
                    pages.append(r.get('id') or r.get('url'))
                keep = []
                for p in pages[:3]:
                    m = re.search(r'sp=(\d+)', p or '')
                    if m and int(m.group(1)) - 1 < len(urls):
                        keep.append(urls[int(m.group(1)) - 1])
                urls = keep or urls[:4]
            snippets = []
            for u in urls[:4]:
                t = fetch_text(u)
                for m in WORD.finditer(t):
                    a, b = max(0, m.start() - 250), min(len(t), m.end() + 250)
                    snippets.append(t[a:b].replace('\n', ' '))
                    if len(snippets) > 6:
                        break
            ctx[k] = {'title': h.get('title'), 'date': h.get('date'), 'url': url, 'coll': sc, 'n_text': len(urls),
                      'snippets': snippets}
        except locapi.Blocked as e:
            print('BLOCKED', e)
            break
        except Exception as e:
            print('skip', k, type(e).__name__, e)
            continue
        n += 1
        if n % 10 == 0:
            json.dump(ctx, open(cp, 'w', encoding='utf-8'), ensure_ascii=False, indent=0)
            print(n, flush=True)
    json.dump(ctx, open(cp, 'w', encoding='utf-8'), ensure_ascii=False, indent=0)
    print('done', n)


if __name__ == '__main__':
    main()
