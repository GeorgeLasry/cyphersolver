"""b09: fetch DECODE page images of nuncio1566 R85-R90 into the session scratchpad with the project cookie."""
import os, re, sys, urllib.request
OUT = sys.argv[1]
CK = open(r'C:\Users\dbour\cypher\targets\bordeaux\decode\cookie.txt', encoding='utf8').read().strip()
CK = re.sub(r'^cookie:\s*', '', CK, flags=re.I)
UA = "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 Chrome/128.0 Safari/537.36"
op = urllib.request.build_opener(urllib.request.ProxyHandler({}))
os.makedirs(OUT, exist_ok=True)
for rec in [int(a) for a in sys.argv[2:]] or [85, 86, 87, 88, 89, 90]:
    p = os.path.join(OUT, 'rec%d.htm' % rec)
    if not os.path.exists(p):
        r = urllib.request.Request('https://de-crypt.org/decrypt-web/RecordsView/%d' % rec, headers={'User-Agent': UA, 'Cookie': CK})
        open(p, 'wb').write(op.open(r, timeout=60).read())
    names = sorted(set(re.findall(r'filesrv/\?file=TH_(IMG_[A-Za-z0-9_.]+)', open(p, encoding='utf8', errors='ignore').read())))
    for n in names:
        o = os.path.join(OUT, n)
        if os.path.exists(o) and os.path.getsize(o) > 20000: continue
        r = urllib.request.Request('https://de-crypt.org/decrypt-custom/filesrv/?file=' + n,
            headers={'User-Agent': UA, 'Cookie': CK, 'Referer': 'https://de-crypt.org/decrypt-web/RecordsView/%d' % rec})
        d = op.open(r, timeout=180).read()
        open(o, 'wb').write(d); print(rec, n, len(d))
