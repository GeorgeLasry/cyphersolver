"""r2g: fetch DECODE record pages (and optionally their images) into the session scratchpad with the project cookie.
usage: python r2g_fetch.py OUTDIR REC [REC ...] [--img]"""
import os, re, sys, urllib.request
OUT = sys.argv[1]
recs = [int(a) for a in sys.argv[2:] if a.isdigit()]
IMG = '--img' in sys.argv
CK = open(r'C:\Users\dbour\cypher\targets\bordeaux\decode\cookie.txt', encoding='utf8').read().strip()
CK = re.sub(r'^cookie:\s*', '', CK, flags=re.I)
UA = "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 Chrome/128.0 Safari/537.36"
op = urllib.request.build_opener(urllib.request.ProxyHandler({}))
os.makedirs(OUT, exist_ok=True)
for rec in recs:
    p = os.path.join(OUT, 'rec%d.htm' % rec)
    if not os.path.exists(p):
        r = urllib.request.Request('https://de-crypt.org/decrypt-web/RecordsView/%d' % rec, headers={'User-Agent': UA, 'Cookie': CK})
        open(p, 'wb').write(op.open(r, timeout=60).read())
    h = open(p, encoding='utf8', errors='ignore').read()
    names = sorted(set(re.findall(r'filesrv/\?file=TH_(IMG_[A-Za-z0-9_.]+)', h)))
    docs = sorted(set(re.findall(r'filesrv/\?file=(DOC_[A-Za-z0-9_.]+)', h)))
    print(rec, len(names), 'images', docs)
    if not IMG: continue
    for n in names:
        o = os.path.join(OUT, n)
        if os.path.exists(o) and os.path.getsize(o) > 20000: continue
        r = urllib.request.Request('https://de-crypt.org/decrypt-custom/filesrv/?file=' + n,
            headers={'User-Agent': UA, 'Cookie': CK, 'Referer': 'https://de-crypt.org/decrypt-web/RecordsView/%d' % rec})
        d = op.open(r, timeout=180).read()
        open(o, 'wb').write(d); print(' ', rec, n, len(d))
    for n in docs:
        o = os.path.join(OUT, n)
        if os.path.exists(o): continue
        r = urllib.request.Request('https://de-crypt.org/decrypt-custom/filesrv/?file=' + n,
            headers={'User-Agent': UA, 'Cookie': CK, 'Referer': 'https://de-crypt.org/decrypt-web/RecordsView/%d' % rec})
        d = op.open(r, timeout=180).read()
        open(o, 'wb').write(d); print(' ', rec, n, len(d))
