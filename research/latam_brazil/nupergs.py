"""NUPERGS (UFRGS, Porto Alegre) acervo documental: list record ids for a search term (field 'assunto',
which searches the summary), then fetch each record. Writes nupergs_hits.json."""
import re, html, sys, time, gzip, json, urllib.request, urllib.parse

UA = {'User-Agent': 'Mozilla/5.0 Chrome/124'}
BASE = "https://www.ufrgs.br/nupergs/index.php/acervos/"


def get(url):
    b = urllib.request.urlopen(urllib.request.Request(url, headers=UA), timeout=90).read()
    if b[:2] == b'\x1f\x8b':
        b = gzip.decompress(b)
    return b.decode('utf8', 'replace')


def ids_for(term):
    ids, page = [], 1
    while True:
        t = get(BASE + "acervo-documental?" + urllib.parse.urlencode({'assunto': term, 'buscar': 'Buscar', 'page': page}))
        new = [i for i in dict.fromkeys(re.findall(r'detalhe-acervo/(\d+)', t)) if i not in ids]
        if not new:
            break
        ids += new
        page += 1
        time.sleep(1.5)
        if page > 60:
            break
    return ids


def record(i):
    t = get(BASE + f"detalhe-acervo/{i}")
    t = re.sub(r'<(script|style).*?</\1>', '', t, flags=re.S)
    t = html.unescape(re.sub(r'<[^>]+>', ' ', t))
    t = re.sub(r'\s+', ' ', t)
    a = t.find('Assunto:')
    return t[a + 9:t.find('voltar', a)].strip()


import os
OUT = os.environ.get('NUP_OUT', 'nupergs_hits.json')
if __name__ == '__main__':
    out = {}
    for term in sys.argv[1:]:
        ids = ids_for(term)
        print(term, len(ids), flush=True)
        for i in ids:
            if i in out:
                continue
            out[i] = {'term': term, 'text': record(i)}
            print(' ', i, out[i]['text'][:300], flush=True)
            time.sleep(1.2)
        json.dump(out, open(OUT, 'w', encoding='utf8'), ensure_ascii=False, indent=1)
