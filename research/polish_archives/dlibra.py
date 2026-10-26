"""Sweep Polish dLibra digital libraries (simple search) for cipher manuscripts.

    python research/polish_archives/dlibra.py [host ...]     # appends to dlibra_hits.jsonl

Search URL: https://<host>/dlibra/results?q=<term>&action=SimpleSearchAction&type=-6&p=<page>
Result boxes are parsed for edition link, title, date and type. Pages capped at 5 per term.
"""
import html, json, os, re, sys, time, urllib.parse, urllib.request

HERE = os.path.dirname(os.path.abspath(__file__))
HOSTS = ['www.wbc.poznan.pl', 'pbc.gda.pl', 'jbc.bj.uj.edu.pl', 'www.sbc.org.pl', 'kpbc.umk.pl',
         'www.bibliotekacyfrowa.pl', 'rcin.org.pl', 'mbc.cyfrowemazowsze.pl', 'mbc.malopolska.pl',
         'polona.pl_skip', 'www.pbc.rzeszow.pl', 'bc.umcs.pl', 'zbc.uz.zgora.pl', 'www.bibliotekacyfrowa.eu',
         'dlibra.bibliotekaelblaska.pl', 'www.pbc.uw.edu.pl', 'www.e-bc.pl']
TERMS = ['szyfr', 'szyfrem', 'szyfrowany', 'szyfrowana', 'szyfrowane', 'zaszyfrowany', 'zaszyfrowana', 'szyfrowy',
         'cyfrą', 'Chiffre', 'Ziffern', 'Geheimschrift', 'chiffriert', 'chiffre', 'cifra', 'tajnopis']
BOX = re.compile(r'<div class="objectbox objectbox--main">(.*?)<div class="objectbox__icons">', re.S)


def fetch(url):
    req = urllib.request.Request(url, headers={'User-Agent': 'Mozilla/5.0 (cyphersolver research sweep)'})
    with urllib.request.urlopen(req, timeout=60) as r:
        return r.read().decode('utf-8', 'replace')


def parse(page, host):
    out = []
    for b in BOX.findall(page):
        m = re.search(r'href="(https?://[^"]*/dlibra/publication/(\d+)/edition/(\d+))"', b)
        t = re.search(r'objectbox__text--title" title="([^"]*)"', b)
        d = re.search(r'objectbox__text--date"\s+title="([^"]*)"', b)
        ty = re.findall(r'objectbox__type">\s*<span[^>]*>\s*([^<]*?)\s*</span>', b, re.S)
        if m:
            out.append({'host': host, 'url': m.group(1), 'edition': m.group(3),
                        'title': html.unescape(t.group(1)) if t else '', 'date': d.group(1) if d else '',
                        'type': html.unescape(ty[0]).strip() if ty else ''})
    return out


def main(hosts):
    path = os.path.join(HERE, 'dlibra_hits.jsonl')
    seen = set()
    if os.path.exists(path):
        for l in open(path, encoding='utf-8'):
            seen.add(json.loads(l)['url'])
    fh = open(path, 'a', encoding='utf-8')
    for host in hosts:
        for t in TERMS:
            for p in range(5):
                url = f'https://{host}/dlibra/results?' + urllib.parse.urlencode(
                    {'q': t, 'action': 'SimpleSearchAction', 'type': '-6', 'p': p})
                try:
                    page = fetch(url)
                except Exception as e:
                    print('ERR', host, t, p, e); break
                items = parse(page, host)
                new = 0
                for it in items:
                    if it['url'] in seen:
                        continue
                    seen.add(it['url']); it['term'] = t; new += 1
                    fh.write(json.dumps(it, ensure_ascii=False) + '\n')
                fh.flush()
                print(host, t, p, len(items), new)
                if not items or 'pagination__next' not in page:
                    break
                time.sleep(0.5)
    fh.close()


if __name__ == '__main__':
    main(sys.argv[1:] or [h for h in HOSTS if not h.endswith('_skip')])
