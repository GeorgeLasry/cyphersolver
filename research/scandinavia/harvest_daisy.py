"""Harvest Danish Rigsarkivet Daisy series hits for cipher terms, then fetch each series' detail page.

    python research/scandinavia/harvest_daisy.py -> daisy_hits.jsonl
Daisy's global search (?c=) matches creator and series names/notes; results are arkivserier with an heid.
"""
import html, json, os, re, time, urllib.parse, urllib.request

HERE = os.path.dirname(os.path.abspath(__file__))
UA = {'User-Agent': 'Mozilla/5.0 (cyphersolver research)'}
BASE = 'https://daisy.rigsarkivet.dk'
TERMS = ['chiffer', 'chiffre', 'chiffrer', 'chiffreret', 'chiffrerede', 'chifreret', 'chifrerede', 'dechiffrering',
         'dechiffreret', 'dechiffrerede', 'dechifrerede', 'dechiffrer', 'chifferbreve', 'chifferbrev', 'chiffernøgle',
         'chiffernøgler', 'chifferskrift', 'ziffer', 'ziffern', 'Chiffern', 'Geheimschrift', 'cifre', 'cifferskrift',
         'opsnappede', 'opsnappet', 'intercepterede', 'chiffrerte', 'chiffres', 'chiffrées', 'déchiffrées',
         'dechiffrirt', 'dechiffrierte', 'Dechiffrierung', 'chiffrirt', 'chiffrierte', 'lønskrift', 'hemmelig skrift',
         'usynligt blæk', 'sympatetisk', 'chifferdepecher', 'chifferdepescher', 'chiffertelegrammer', 'chifferprotokol',
         'chiffersystem', 'chiffersystemer', 'Chiffre', 'kodebog', 'intercipierte', 'intercipirte', 'interciperede', 'Chiffren', 'chiffrerede breve', 'dechiffrerede breve', 'Dechiffrement', 'Dechiffrements', 'chiffrerede depecher', 'Chiffres', 'Ziffern', 'Cifre', 'Cipher', 'Ciphers', 'Geheimschriften', 'chifre', 'chifrer', 'Chifferbog', 'kodetelegrammer', 'chiffertelegrammer', 'sympatetisk blæk']


def get(url):
    with urllib.request.urlopen(urllib.request.Request(url, headers=UA), timeout=120) as f:
        return f.read().decode('utf-8', 'replace')


def strip(s):
    return html.unescape(re.sub(r'\s+', ' ', re.sub(r'<[^>]+>', ' ', s))).strip()


def search(term):
    rows, page = [], 1
    while True:
        q = {'c': term}
        if page > 1:
            q['side'] = page
        h = get(BASE + '/arkivskaber_eller_arkivserie_liste?' + urllib.parse.urlencode(q))
        for tr in re.findall(r'<tr[^>]*>(.*?)</tr>', h, re.S):
            m = re.search(r"toHeDetaljer\('(\d+)','(\d+)'\);\">(.*?)</a>", tr, re.S)
            if not m:
                continue
            tds = [strip(t) for t in re.findall(r'<td[^>]*>(.*?)</td>', tr, re.S)]
            rows.append({'heid': m.group(1), 'series': strip(m.group(3)), 'cells': tds, 'term': term})
        mp = re.search(r'Side\s*(\d+)\s*af\s*(\d+)', strip(h))
        if not mp or int(mp.group(1)) >= int(mp.group(2)) or page >= 20:
            break
        page += 1
        time.sleep(0.5)
    return rows


def detail(heid):
    h = get(f'{BASE}/arkivserie_detaljer?heid={heid}&henid={heid}')
    i = h.find('Arkivseriens indholdsoversigt')
    t = strip(h[i:]) if i >= 0 else ''
    t = t.split('Indholdsoversigt')[0]
    return t[:3000]


def main():
    out = os.path.join(HERE, 'daisy_hits.jsonl')
    seen = set()
    if os.path.exists(out):
        seen = {json.loads(l)['heid'] for l in open(out, encoding='utf-8')}
    fh = open(out, 'a', encoding='utf-8')
    for t in TERMS:
        try:
            rows = search(t)
        except Exception as e:
            print(t, 'ERR', e); continue
        new = 0
        for r in rows:
            if r['heid'] in seen:
                continue
            seen.add(r['heid']); new += 1
            try:
                r['detail'] = detail(r['heid'])
            except Exception as e:
                r['detail'] = f'ERR {e}'
            fh.write(json.dumps(r, ensure_ascii=False) + '\n'); fh.flush()
            time.sleep(0.3)
        print(t, len(rows), 'new', new, flush=True)


if __name__ == '__main__':
    main()
