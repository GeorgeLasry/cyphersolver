"""Keyword search of AGN Colombia's DataViva (dataviva.archivogeneral.gov.co) public API.

The body is the one the web app sends from /explore/agn (captured 28 Oct 2026). Results go to dataviva_hits.json.
    python research/latam_north/dataviva.py cifra "en cifra" ...
"""
import json, os, sys, time, urllib.request

API = 'https://dataviva.archivogeneral.gov.co/api/search/public'
ROOT_ID = '66acc915a58c7bfd59b83353'   # Archivo General de la Nación root node
TYPES = ["agrupación", "agrupación-documental", "archivo", "caja", "carpeta", "documento", "expediente", "fondo",
         "grupo", "legajo", "libro", "mapa", "n/a", "protocolo", "sección", "serie", "sub-fondo", "subsección",
         "subserie", "tomo", "transferencia", "unidad-de-conservación", "unidad-conservacion-caja",
         "unidad-conservacion-carpeta", "unidad-documental", "unidad-documental-documento",
         "unidad-documental-expediente", "unidad-documental-compuesta"]
OUT = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'dataviva_hits.json')


def search(kw, page=0, limit=100):
    body = {"post_type": TYPES, "status": "published", "page": page, "limit": limit, "sortBy": "ident",
            "sortOrder": "asc", "keyword": kw, "activeFilters": [], "date_filters": [], "input_filters": [],
            "root": {"id": ROOT_ID}}
    req = urllib.request.Request(API, data=json.dumps(body).encode(), method='POST',
                                 headers={'Content-Type': 'application/json', 'Accept': 'application/json',
                                          'User-Agent': 'Mozilla/5.0 (cipher catalogue research)'})
    with urllib.request.urlopen(req, timeout=120) as r:
        return json.load(r)


def main(terms):
    hits = json.load(open(OUT, encoding='utf-8')) if os.path.exists(OUT) else {}
    for kw in terms:
        res, page = [], 0
        while True:
            try:
                d = search(kw, page)
            except Exception as e:
                print(kw, 'error', e); break
            rs = d.get('resources') or d.get('data') or []
            res += rs
            total = d.get('total', 0)
            print(kw, 'page', page, len(rs), 'total', total, flush=True)
            if not rs or len(res) >= total or page >= 9:
                break
            page += 1
            time.sleep(2)
        hits[kw] = {'total': total if res else 0, 'resources': res}
        json.dump(hits, open(OUT, 'w', encoding='utf-8'), ensure_ascii=False, indent=1)
        time.sleep(2)


if __name__ == '__main__':
    main(sys.argv[1:])
