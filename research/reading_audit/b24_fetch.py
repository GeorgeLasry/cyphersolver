"""b24: fetch DECODE record pages and every linked file (images and DOC_ attachments) into the session scratchpad with the project cookie.

    python research/reading_audit/b17_fetch.py <outdir> <record> [<record> ...]
"""
import os, re, sys, urllib.request
OUT = sys.argv[1]
CK = open(r'C:\Users\dbour\cypher\targets\bordeaux\decode\cookie.txt', encoding='utf8').read().strip()
CK = re.sub(r'^cookie:\s*', '', CK, flags=re.I)
UA = "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 Chrome/128.0 Safari/537.36"
op = urllib.request.build_opener(urllib.request.ProxyHandler({}))
os.makedirs(OUT, exist_ok=True)
for rec in [int(a) for a in sys.argv[2:]]:
    p = os.path.join(OUT, 'rec%d.htm' % rec)
    r = urllib.request.Request('https://de-crypt.org/decrypt-web/RecordsView/%d' % rec, headers={'User-Agent': UA, 'Cookie': CK})
    html = op.open(r, timeout=60).read()
    open(p, 'wb').write(html)
    html = html.decode('utf8', 'ignore')
    names = set(re.findall(r'filesrv/\?file=(?:TH_)?((?:IMG|DOC)_[^"\'&<> ]+)', html))
    print(rec, 'logged in' if 'Logout' in html or 'logout' in html else 'NOT LOGGED IN?', sorted(names))
    for n in sorted(names):
        o = os.path.join(OUT, n)
        if os.path.exists(o) and os.path.getsize(o) > 2000: continue
        r = urllib.request.Request('https://de-crypt.org/decrypt-custom/filesrv/?file=' + n,
            headers={'User-Agent': UA, 'Cookie': CK, 'Referer': 'https://de-crypt.org/decrypt-web/RecordsView/%d' % rec})
        for k in range(4):
            try: d = op.open(r, timeout=180).read(); break
            except Exception as e: print("retry", n, e)
        open(o, 'wb').write(d); print(rec, n, len(d))
