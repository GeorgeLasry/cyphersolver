"""PARES description sweep for cipher items (Oct 2026 archive sweep).

    python research/pares_ags/sweep.py "en cifra" [maxpages]

Fetches catalogo/find?texto=<term> 100 results a page, slowly (PARES returns 429 when hammered), and appends
each hit (id, signatura, dates, title, has_images, term) to research/pares_ags/hits.jsonl. Raw pages go to the
scratch dir given by PARES_RAW (not the repo).

Politeness (27 Oct 2026): PARES_DELAY seconds (default 20) plus up to 10 s jitter between requests; the run stops at
the first 429 (exit 2) instead of retrying into the block; hits_progress.json keeps the last page done per term, so
a restart resumes after it; PARES_MAXREQ (default 50) caps the requests of one run.

Known bug (27 Oct 2026, see README access log): PARES ignores `tambloque` and `pagina` on catalogo/find. Every page
comes back as 25 rows, and pages 2..n repeat page 1. The site pages with the displaytag parameter `d-2677838-p=<n>` on
the `SearchController.do;jsessionid=...` links in the `pagelinks` div of page 1 (and sets 100 rows through the POST
form `formBusqueda`). Until that is implemented and tested, the run stops as soon as a page repeats the previous one,
so only the first 25 rows of each term are collected.
"""
import datetime, html, json, os, random, re, sys, time, urllib.parse, urllib.request, http.cookiejar, urllib.error

BASE = 'https://pares.cultura.gob.es/ParesBusquedas20'
HERE = os.path.dirname(os.path.abspath(__file__))
OUT = os.path.join(HERE, 'hits.jsonl')
PROGRESS = os.path.join(HERE, 'hits_progress.json')
RAW = os.environ.get('PARES_RAW')
DELAY = float(os.environ.get('PARES_DELAY', '20'))
MAXREQ = int(os.environ.get('PARES_MAXREQ', '50'))
NREQ = 0
cj = http.cookiejar.CookieJar()
op = urllib.request.build_opener(urllib.request.HTTPCookieProcessor(cj))
op.addheaders = [('User-Agent', 'Mozilla/5.0 (research; cyphersolver archive sweep)')]


class Blocked(Exception):
    pass


def get(url):
    global NREQ
    if NREQ >= MAXREQ:
        raise Blocked('request cap reached')
    NREQ += 1
    try:
        return op.open(url, timeout=90).read()
    except urllib.error.HTTPError as e:
        if e.code == 429:
            raise Blocked('429, retry-after %s' % e.headers.get('Retry-After'))
        raise


def load_progress():
    return json.load(open(PROGRESS, encoding='utf-8')) if os.path.exists(PROGRESS) else {}


def save_progress(pr):
    json.dump(pr, open(PROGRESS, 'w', encoding='utf-8'), ensure_ascii=False, indent=1)


def parse(h):
    """One dict per result row (<tr class="odd|even">). The thumbnail link to catalogo/show/<id> sits in the row's
    first cell, before the title link, so has_images must be read per row (the 27 Oct 2026 run read it from the
    text after the title link, which belongs to the next row)."""
    out = []
    for row in re.findall(r'(?s)<tr class="(?:odd|even)">(.*?)</tr>', h):
        m = re.search(r'href="/ParesBusquedas20/catalogo/description/(\d+)\?nm"[^>]*>(.*?)</a>', row, re.S)
        if not m:
            continue
        txt = lambda x: re.sub(r'\s+', ' ', html.unescape(re.sub(r'<[^>]*>', ' ', x))).strip()
        full = re.search(r"title='([^']*)'", row)
        dates = re.search(r'Fechas?: </em>(.*?)</p>', row, re.S)
        sig = re.search(r'Signatura: </em>(.*?)</p>', row, re.S)
        sig = re.sub(r'\s*\[ Signaturas anteriores \]', '', txt(sig.group(1))) if sig else '?'
        out.append({'id': m.group(1), 'sig': sig, 'date': txt(dates.group(1)) if dates else '?',
                    'title': txt(full.group(1) if full else m.group(2)),
                    'images': f'catalogo/show/{m.group(1)}' in row})
    return out


def run(term, maxpages=20):
    seen = set()
    if os.path.exists(OUT):
        for line in open(OUT, encoding='utf-8'):
            r = json.loads(line)
            if r['term'] == term:
                seen.add(r['id'])
    n = 0
    prev = None
    pr = load_progress()
    start = pr.get(term, {}).get('last_page', 0) + 1
    if pr.get(term, {}).get('done'):
        return 0
    for p in range(start, maxpages + 1):
        q = urllib.parse.urlencode({'nm': '', 'texto': term, 'tambloque': 100, 'pagina': p}, encoding='latin-1')
        h = get(f'{BASE}/catalogo/find?{q}').decode('utf-8', 'replace')
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
        tot = re.search(r'Todos los resultados \(([\d.]+)\)', h)
        print(f'{term!r} page {p}: {len(rows)} rows ({tot.group(0) if tot else "?"})', file=sys.stderr)
        ids = [r['id'] for r in rows]
        last = not rows or 'raquo' not in h or ids == prev  # ids == prev: pagination ignored (see docstring)
        prev = ids
        pr[term] = {'last_page': p, 'done': last, 'date': datetime.date.today().isoformat(),
                    'unique_hits': len(seen), 'total': tot.group(1) if tot else '?'}
        save_progress(pr)
        if last:
            break
        time.sleep(DELAY + random.uniform(0, 10))
    return n


if __name__ == '__main__':
    sys.stdout.reconfigure(encoding='utf-8')
    try:
        print(run(sys.argv[1], int(sys.argv[2]) if len(sys.argv) > 2 else 20), 'new hits')
    except Blocked as e:
        print('stopped:', e, file=sys.stderr)
        sys.exit(2)
