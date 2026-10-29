"""Biblioteca Ambrosiana OPAC (ambrosiana.comperio.it, ClavisNG) full-text search for cipher terms.

    PYTHONUTF8=1 python -I research/milan_archives/ambrosiana_harvest.py [term ...]

Pages through /opac/search/lst?q=<term>&page=N (fetched with curl; the server resets Python's TLS),
parses each result block (id man_NNN, COinS title/author/place/date, "Fa parte di" parent shelfmark,
material type) and merges into ambrosiana_hits.json (keyed by catalog id, list of matching terms).
"""
import html, json, os, re, subprocess, sys, time, urllib.parse

HERE = os.path.dirname(os.path.abspath(__file__))
OUT = os.path.join(HERE, 'ambrosiana_hits.json')
BASE = 'https://ambrosiana.comperio.it/opac/search/lst?'
TERMS = ['cifra', 'cifre', 'cifrata', 'cifrate', 'cifrato', 'cifrati', 'decifrata', 'decifrate', 'decifrato',
         'decifrazione', 'deciferata', 'zifra', 'ziffra', 'zifre', 'cifrario', 'cifrari', 'contracifra', 'contrazifra',
         'contracifera', 'cifera', 'ciffra', 'chiffre', 'chiffres', 'deschiffré', 'cyfra', 'cifrada', 'cifras',
         'descifrada', 'enciphered', 'cipher', 'Geheimschrift', 'occulte', 'segreta scrittura', 'caratteri segreti']


def fetch(url):
    for _ in range(3):
        r = subprocess.run(['curl', '-s', '-L', '-m', '60', url], capture_output=True)
        if r.returncode == 0 and r.stdout:
            return r.stdout.decode('utf-8', 'replace')
        time.sleep(3)
    return ''


def clean(s):
    return re.sub(r'\s+', ' ', html.unescape(re.sub('<[^>]+>', ' ', s))).strip()


def parse(page):
    rows = []
    blocks = re.split(r'<div id="man_', page)[1:]
    for b in blocks:
        mid = re.match(r'(\d+)', b).group(1)
        coins = re.search(r'class="Z3988" title="([^"]*)"', b)
        c = {}
        if coins:
            for k, v in urllib.parse.parse_qsl(html.unescape(coins.group(1))):
                c[k] = v.strip()
        parent = re.search(r'Fa parte di:\s*(?:</[^>]+>\s*)*(?:<[^>]+>\s*)*([^<]+)', b)
        mtype = re.search(r'class="[^"]*(?:manifestation-type|bib-type|type)[^"]*"[^>]*>([^<]+)<', b)
        title = c.get('rft.title') or ''
        if not title:
            t = re.search(r'class="cover" property="url" href="[^"]*" title="([^"]*)"', b)
            title = html.unescape(t.group(1)) if t else ''
        rows.append({'id': 'ambro:catalog:' + mid,
                     'title': title.strip(),
                     'author': c.get('rft.au', ''),
                     'place': c.get('rft.place', ''),
                     'date': c.get('rft.date', ''),
                     'part_of': clean(parent.group(1)) if parent else '',
                     'mtype': clean(mtype.group(1)) if mtype else '',
                     'manuscript': 'Manoscritti' in b,
                     'url': 'https://ambrosiana.comperio.it/opac/detail/view/ambro:catalog:' + mid})
    return rows


def main(terms):
    data = {}
    if os.path.exists(OUT):
        data = {r['id']: r for r in json.load(open(OUT, encoding='utf-8'))}
    for term in terms:
        seen_page_sets = set()
        total = 0
        for p in range(1, 200):
            page = fetch(BASE + urllib.parse.urlencode({'q': term, 'page': p}))
            rows = parse(page)
            new = [r for r in rows if r['id'] not in seen_page_sets]
            if not new:
                break
            seen_page_sets.update(r['id'] for r in rows)
            for r in rows:
                old = data.get(r['id'])
                if old:
                    if term not in old['terms']:
                        old['terms'].append(term)
                else:
                    r['terms'] = [term]
                    data[r['id']] = r
            total += len(new)
            time.sleep(0.5)
        print(term, total, file=sys.stderr)
        with open(OUT, 'w', encoding='utf-8') as fh:
            json.dump(list(data.values()), fh, ensure_ascii=False, indent=1)
    print(len(data), 'records')


if __name__ == '__main__':
    main(sys.argv[1:] or TERMS)
