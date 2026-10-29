"""Arquivo Público Mineiro (SIAAPM): query each module's search.php for cipher terms. Writes apm_hits.json."""
import re, html, sys, time, json, urllib.request, urllib.parse
UA = {'User-Agent': 'Mozilla/5.0 Chrome/124'}
B = "https://www.siaapm.cultura.mg.gov.br/modules/"
def get(u):
    return urllib.request.urlopen(urllib.request.Request(u, headers=UA), timeout=90).read().decode('latin-1')
home = get("https://www.siaapm.cultura.mg.gov.br/")
mods = sorted(set(re.findall(r'modules/([a-z0-9_]+)/search\.php', home)))
print(mods)
out = {}
for m in mods:
    for q in sys.argv[1:]:
        u = B + m + "/search.php?" + urllib.parse.urlencode({'query': q, 'andor': 'AND', 'dt1': '', 'dt2': '', 'notacao': '', 'nantiga': '', 'ordenar': '30', 'asc_desc': '10', 'submit': 'Executar pesquisa', 'action': 'results'})
        try:
            t = get(u)
        except Exception as e:
            print(m, q, 'ERR', e); continue
        t = re.sub(r'<(script|style).*?</\1>', '', t, flags=re.S)
        n = re.search(r'(\d+)\s+(?:registro|resultado|documento)', t)
        links = sorted(set(re.findall(r'href="([^"]*(?:brtacervo|docs|photo|display|detalhe|id=)[^"]*)"', t)))
        x = re.sub(r'\s+', ' ', html.unescape(re.sub(r'<[^>]+>', ' ', t)))
        hits = [x[max(0, k.start() - 200):k.start() + 250] for k in re.finditer(q[:5], x, re.I)][:15]
        print(m, q, n.group(0) if n else '-', len(hits))
        out[f'{m}|{q}'] = {'n': n.group(0) if n else None, 'snips': hits, 'links': links[:60]}
        time.sleep(1)
json.dump(out, open('apm_hits.json', 'w', encoding='utf8'), ensure_ascii=False, indent=1)
