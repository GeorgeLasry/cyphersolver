"""PARES description sweep for cipher items (Oct 2026 archive sweep).

    python research/pares_ags/sweep.py "en cifra" [maxpages]

Fetches catalogo/find?texto=<term> 100 results a page, slowly (PARES returns 429 when hammered), and appends
each hit (id, signatura, dates, title, has_images, term) to research/pares_ags/hits.jsonl. Raw pages go to the
scratch dir given by PARES_RAW (not the repo).
"""
import json, os, re, sys, time, urllib.parse, urllib.request, http.cookiejar, urllib.error

BASE = 'https://pares.cultura.gob.es/ParesBusquedas20'
HERE = os.path.dirname(os.path.abspath(__file__))
OUT = os.path.join(HERE, 'hits.jsonl')
RAW = os.environ.get('PARES_RAW')
DELAY = float(os.environ.get('PARES_DELAY', '8'))
cj = http.cookiejar.CookieJar()
op = urllib.request.build_opener(urllib.request.HTTPCookieProcessor(cj))
op.addheaders = [('User-Agent', 'Mozilla/5.0 (research; cyphersolver archive sweep)')]


def get(url):
    for attempt in range(6):
        try:
            return op.open(url, timeout=90).read()
        except urllib.error.HTTPError as e:
            if e.code == 429:
                print('  429, waiting', 120 * (attempt + 1), file=sys.stderr)
                time.sleep(120 * (attempt + 1))
                continue
            raise
    raise RuntimeError('still 429')


def parse(h):
    out = []
    ms = list(re.finditer(r'href="/ParesBusquedas20/catalogo/description/(\d+)\?nm"[^>]*?(?:title=\'([^\']*)\')?[^>]*>([^<]*)<', h))
    for k, m in enumerate(ms):
        end = ms[k + 1].start() if k + 1 < len(ms) else m.end() + 3000
        raw = h[m.end():end]
        seg = re.sub(r'\s+', ' ', re.sub(r'<[^>]*>', ' ', raw))
        f = re.search(r'Fechas?: (.*?) Signatura: (\S+)', seg)
        title = (m.group(2) or m.group(3)).replace('&nbsp;', ' ').strip()
        out.append({'id': m.group(1), 'sig': f.group(2) if f else '?', 'date': f.group(1).strip() if f else '?',
                    'title': title, 'images': ('catalogo/show/' in raw) or ('imagen' in raw.lower())})
    return out


def run(term, maxpages=20):
    seen = set()
    if os.path.exists(OUT):
        for line in open(OUT, encoding='utf-8'):
            r = json.loads(line)
            if r['term'] == term:
                seen.add(r['id'])
    n = 0
    for p in range(1, maxpages + 1):
        q = urllib.parse.urlencode({'nm': '', 'texto': term, 'tambloque': 100, 'pagina': p}, encoding='latin-1')
        h = get(f'{BASE}/catalogo/find?{q}').decode('latin-1')
        if RAW:
            open(os.path.join(RAW, f'find_{re.sub(r"\\W+", "_", term)}_{p}.html'), 'w', encoding='utf-8').write(h)
        rows = parse(h)
        with open(OUT, 'a', encoding='utf-8') as fh:
            for r in rows:
                if r['id'] in seen:
                    continue
                seen.add(r['id'])
                r['term'] = term
                fh.write(json.dumps(r, ensure_ascii=False) + '\n')
                n += 1
        tot = re.search(r'([\d.]+)\s*(?:resultados|registros|descripciones)', h)
        print(f'{term!r} page {p}: {len(rows)} rows ({tot.group(0) if tot else "?"})', file=sys.stderr)
        if not rows or 'raquo' not in h:
            break
        time.sleep(DELAY)
    return n


if __name__ == '__main__':
    sys.stdout.reconfigure(encoding='utf-8')
    print(run(sys.argv[1], int(sys.argv[2]) if len(sys.argv) > 2 else 20), 'new hits')
