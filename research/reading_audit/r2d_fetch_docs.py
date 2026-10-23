"""r2d (23 Oct 2026): fetch every DOC_ attachment (png 'cleartext' images, txt) of DECODE records into a scratch dir.

    python research/reading_audit/r2d_fetch_docs.py <out-dir> <rec.htm dir> rec ...
"""
import os, re, sys, urllib.request
OUT, HT = sys.argv[1], sys.argv[2]
CK = open(r'C:\Users\dbour\cypher\targets\bordeaux\decode\cookie.txt', encoding='utf8').read().strip()
CK = re.sub(r'^cookie:\s*', '', CK, flags=re.I)
UA = "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 Chrome/128.0 Safari/537.36"
op = urllib.request.build_opener(urllib.request.ProxyHandler({}))
os.makedirs(OUT, exist_ok=True)
for rec in sys.argv[3:]:
    p = os.path.join(HT, 'rec%s.htm' % rec)
    if not os.path.exists(p):
        r = urllib.request.Request('https://de-crypt.org/decrypt-web/RecordsView/%s' % rec, headers={'User-Agent': UA, 'Cookie': CK})
        open(p, 'wb').write(op.open(r, timeout=60).read())
    names = sorted(set(re.findall(r'file=((?:DOC|IMG)_[A-Za-z0-9_.]+)', open(p, encoding='utf8', errors='ignore').read())))
    for n in names:
        o = os.path.join(OUT, n)
        if os.path.exists(o) and os.path.getsize(o) > 0: continue
        r = urllib.request.Request('https://de-crypt.org/decrypt-custom/filesrv/?file=' + n,
            headers={'User-Agent': UA, 'Cookie': CK, 'Referer': 'https://de-crypt.org/decrypt-web/RecordsView/%s' % rec})
        try:
            d = op.open(r, timeout=180).read()
        except Exception as e:
            print(rec, n, 'ERR', e); continue
        open(o, 'wb').write(d); print(rec, n, len(d))
