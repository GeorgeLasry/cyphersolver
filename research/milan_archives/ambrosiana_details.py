"""Fetch Ambrosiana OPAC detail pages for the manuscript hits in ambrosiana_hits.json.

    PYTHONUTF8=1 python -I research/milan_archives/ambrosiana_details.py

Keeps records that sit in a manuscript ("Fa parte di" a shelfmark) or whose title looks like a letter/cipher item.
Extracts Pubblicazione, Descrizione fisica, Fa parte di, Nota, Nomi, Luoghi and the image file ids
(clavisng/index.php?file=N). Writes ambrosiana_details.json incrementally (resumable).
"""
import html, json, os, re, subprocess, time

HERE = os.path.dirname(os.path.abspath(__file__))
HITS = os.path.join(HERE, 'ambrosiana_hits.json')
OUT = os.path.join(HERE, 'ambrosiana_details.json')
SHELF = re.compile(r'\b[A-Z]{1,2} \d+ (?:inf|sup|suss)\b|Pergamena|^S\.P\.|Trotti|Borromeo')
TITLE = re.compile(r'^\s*(Pergamena|Schemi|Lettera|Lettere|Biglietto|Cifra|Cifrario|Dispaccio|Avviso|Avvisi|Copia|Minuta|Memoriale|Relazione|Istruzione)', re.I)


def fetch(url):
    for _ in range(3):
        r = subprocess.run(['curl', '-s', '-L', '-m', '60', url], capture_output=True)
        if r.returncode == 0 and r.stdout:
            return r.stdout.decode('utf-8', 'replace')
        time.sleep(3)
    return ''


def fields(page):
    imgs = sorted(set(re.findall(r'clavisng/index\.php\?file=(\d+)', page)), key=int)
    body = re.sub(r'<script.*?</script>|<style.*?</style>', '', page, flags=re.S)
    t = html.unescape(re.sub(r'<[^>]+>', ' | ', body))
    t = re.sub(r'(\s*\|\s*)+', ' | ', t)
    t = re.sub(r'\s+', ' ', t)
    i = t.find('Dettagli')
    j = t.find('Collocazioni', i)
    det = t[i:j] if i >= 0 else ''
    title = re.search(r'<title>(.*?)</title>', page, re.S)
    out = {'detail': det[:2500], 'images': imgs, 'page_title': html.unescape(title.group(1)).strip() if title else ''}
    for key, name in [('Nota:', 'nota'), ('Pubblicazione:', 'pub'), ('Descrizione fisica:', 'phys'), ('Fa parte di:', 'part')]:
        m = re.search(re.escape(key) + r' \| (.*?)(?: \| (?:Nomi|Soggetti|Luoghi|Immagini|Lingua|Data|Fa parte di|Descrizione fisica|Nota|Comprende|Dati generali):|$)', det)
        out[name] = m.group(1).strip(' |') if m else ''
    return out


def main():
    hits = json.load(open(HITS, encoding='utf-8'))
    done = {}
    if os.path.exists(OUT):
        done = {r['id']: r for r in json.load(open(OUT, encoding='utf-8'))}
    todo = [h for h in hits if h['id'] not in done and (SHELF.search(h.get('part_of', '')) or TITLE.search(h.get('title', '')))]
    print(len(todo), 'to fetch')
    for k, h in enumerate(todo, 1):
        r = dict(h)
        r.update(fields(fetch(h['url'])))
        done[h['id']] = r
        if k % 10 == 0 or k == len(todo):
            with open(OUT, 'w', encoding='utf-8') as fh:
                json.dump(list(done.values()), fh, ensure_ascii=False, indent=1)
            print(k)
        time.sleep(0.4)


if __name__ == '__main__':
    main()
