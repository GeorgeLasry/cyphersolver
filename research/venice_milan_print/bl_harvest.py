"""British Library Archives and Manuscripts catalogue (searcharchives.bl.uk): cipher terms x Venice/Milan/Mantua.
Scrapes the HTML result lists (100 per page), 1 request / 2 s. Output bl_hits.jsonl (id, shelfmark, text, query)."""
import html, json, re, subprocess, time, urllib.parse
Q = ['cipher Venice', 'cipher Venetian', 'cypher Venice', 'cipher Milan', 'cipher Milanese', 'cipher Mantua',
     'cipher Sforza', 'cifra', 'cifre', 'zifra', '"in cifra"', 'decifrata', 'cipher Italian', 'cypher Italian',
     'chiffre Venise', 'cipher Doge', 'cipher Gonzaga', 'cipher Inquisitors Venice', 'cipher Parma', 'cipher Genoa',
     'cipher Savoy', 'cipher Florence', 'cipher Modena', 'cipher Ferrara']
out = open('bl_hits.jsonl', 'w', encoding='utf-8'); seen = set()
for q in Q:
    for page in range(1, 6):
        url = 'https://searcharchives.bl.uk/?' + urllib.parse.urlencode({'q': q, 'per_page': 100, 'page': page})
        r = subprocess.run(['curl', '-sL', '-m', '60', '-A', 'Mozilla/5.0', url], capture_output=True)
        h = r.stdout.decode('utf-8', 'replace')
        parts = re.split(r'<article', h)[1:]
        n = 0
        for p in parts:
            m = re.search(r'href="/catalog/([^"]+)"', p)
            if not m: continue
            n += 1
            t = html.unescape(re.sub(r'<[^>]+>', ' ', p)); t = re.sub(r'\s+', ' ', t).strip()
            if m.group(1) in seen: continue
            seen.add(m.group(1))
            out.write(json.dumps({'id': m.group(1), 'text': t[:1500], 'query': q}, ensure_ascii=False) + '\n')
        out.flush()
        print(q, page, n, flush=True)
        time.sleep(2)
        if n < 100: break
