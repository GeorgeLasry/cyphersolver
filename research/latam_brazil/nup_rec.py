"""Print the description of NUPERGS (UFRGS) acervo documental records by id."""
import re, html, sys, time, gzip, urllib.request

for i in sys.argv[1:]:
    req = urllib.request.Request(f"https://www.ufrgs.br/nupergs/index.php/acervos/detalhe-acervo/{i}",
                                 headers={'User-Agent': 'Mozilla/5.0 Chrome/124'})
    b = urllib.request.urlopen(req, timeout=60).read()
    if b[:2] == b'\x1f\x8b':
        b = gzip.decompress(b)
    t = b.decode('latin-1')
    t = re.sub(r'<(script|style).*?</\1>', '', t, flags=re.S)
    t = html.unescape(re.sub(r'<[^>]+>', ' ', t))
    t = re.sub(r'\s+', ' ', t)
    a = t.find('Assunto:')
    e = t.find('voltar', a)
    print(i, '|', t[a + 9:e].strip()[:700])
    time.sleep(1.5)
