"""FranceArchives full-text harvest. The site answers a first request with a JS redirect to /redirect_<token>/<path>;
following that redirect (plain GET, same cookie jar) returns the page. Records cards incl. 'Extrait de la notice'.
Output: fa_hits.json (unique by facomponent id)."""
import html, json, re, sys, time, urllib.parse
import requests

S = requests.Session()
S.headers['User-Agent'] = 'Mozilla/5.0 (research sweep; cyphersolver)'
BASE = 'https://francearchives.gouv.fr'
TERMS = ['"lettre chiffrée"', '"lettres chiffrées"', '"en chiffre"', '"en chiffres"', 'chiffrée', 'chiffrées', 'déchiffrement',
         'déchiffrée', '"écriture secrète"', '"clef du chiffre"', '"clé du chiffre"', '"clef de chiffre"', '"alphabet chiffré"',
         '"dépêche chiffrée"', '"dépêches chiffrées"', 'cifra', 'cryptogramme', '"chiffre diplomatique"', '"table de chiffre"',
         '"partie en chiffre"', '"partie chiffrée"', '"caractères chiffrés"', '"chiffres secrets"', '"chiffre secret"',
         'chifre', '"lettre en chiffre"', '"lettres en chiffre"', '"écrit en chiffre"', '"écrite en chiffre"', 'chiffré',
         '"écriture chiffrée"', 'nomenclateur', '"correspondance chiffrée"', '"avec chiffre"', '"chiffre de"', 'cryptographie',
         '"alphabet secret"', '"langage chiffré"', '"billet chiffré"', 'déchiffrée', '"non déchiffré"', 'illisible chiffre']


def fetch(path):
    for i in range(5):
        try:
            r = S.get(BASE + path, timeout=60)
            m = re.search(r"window\.location\.href='(/redirect_[^']+)'", r.text)
            if m and len(r.text) < 1000:
                r = S.get(BASE + html.unescape(m.group(1)), timeout=60)
            if len(r.text) > 5000:
                return r.text
        except Exception as e:
            pass
        time.sleep(4 * (i + 1))
    return ''


def cards(t):
    out = []
    for blk in t.split('fa-sr-card">')[1:]:
        d = {}
        m = re.search(r'<h3 class="fr-card__title"><a href="([^"]+)">(.*?)</a>', blk, re.S)
        if not m:
            continue
        d['url'], d['title'] = m.group(1), html.unescape(re.sub('<[^>]+>', '', m.group(2))).strip()
        for lab, val in re.findall(r'fa-sr-card__props--label">(.*?)</(?:span|p)>\s*<(?:span|div)[^>]*fa-sr-card__props--value[^>]*>(.*?)</(?:span|div)>', blk, re.S):
            d[html.unescape(lab).strip()] = html.unescape(re.sub(r'<[^>]+>', '', val)).strip()
        out.append(d)
    return out


def main(terms, tag):
    seen = {}
    log = open(f'fa_counts_{tag}.txt', 'w', encoding='utf-8')
    for term in terms:
        q = urllib.parse.quote_plus(term)
        page, npages, n = 1, 1, 0
        while page <= npages:
            t = fetch(f'/fr/search?es_escategory=archives&items_per_page=50&q={q}&page={page}')
            if not t:
                break
            m = re.search(r'\[page (\d+) sur (\d+)\]', t)
            npages = int(m.group(2)) if m else 1
            cs = cards(t)
            for c in cs:
                k = c['url']
                if k not in seen:
                    seen[k] = c
                    c['terms'] = []
                seen[k]['terms'].append(term)
            n += len(cs)
            page += 1
            time.sleep(0.8)
            if page > 40:
                break
        msg = f'{term}\tpages={npages}\tcards={n}\tunique_total={len(seen)}'
        print(msg); log.write(msg + '\n'); log.flush()
        json.dump(list(seen.values()), open(f'fa_hits_{tag}.json', 'w', encoding='utf-8'), ensure_ascii=False)


if __name__ == '__main__':
    sys.stdout.reconfigure(encoding='utf-8')
    main(sys.argv[2].split('|'), sys.argv[1])
