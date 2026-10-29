"""Query public AtoM catalogues (Paraguay ANA: historia / riobranco) for cipher terms."""
import re, html, sys, time, json, urllib.request, urllib.parse
UA = "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 Chrome/124 Safari/537.36"
hosts = sys.argv[1].split(',')
terms = sys.argv[2].split(',')
PFX = {"atom.arquivoestado.sp.gov.br": "", "redisap.unicamp.br": ""}
out = {}
for h in hosts:
    for q in terms:
        url = f"https://{h}{PFX.get(h, '/index.php')}/informationobject/browse?topLod=0&sort=relevance&query={urllib.parse.quote(q)}"
        try:
            t = urllib.request.urlopen(urllib.request.Request(url, headers={'User-Agent': UA}), timeout=60).read().decode('utf8', 'replace')
        except Exception as e:
            print(h, q, 'ERR', e); continue
        n = re.search(r'Showing\s+([\d,]+)\s+results', t) or re.search(r'Results\s+\d+\s+to\s+\d+\s+of\s+([\d,]+)', t)
        rows = []
        for m in re.finditer(r'<a class="h5 mb-0 text-truncate" href="([^"]+)" title="([^"]*)"', t):
            rows.append((m.group(1), html.unescape(m.group(2)).strip()))
        rows = list(dict.fromkeys(rows))
        print(h, q, 'n=', n.group(1) if n else ('none' if 'No results' in t else '?'), len(rows))
        for s, ti in rows: print('   ', s, '|', ti[:160])
        out[f'{h}|{q}'] = rows
        time.sleep(2)
json.dump(out, open('atom_hits_' + hosts[0].split('.')[0] + '.json', 'w', encoding='utf8'), ensure_ascii=False, indent=1)
