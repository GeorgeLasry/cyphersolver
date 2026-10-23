"""b16 (wotton1585): re-fetch the DECODE record pages R4841-R4843 with the project cookie and list every file on them
(images IMG_*, documents DOC_*), to check whether anything was added since 21 Sept 2026. Pages go to the scratchpad."""
import os, re, sys, urllib.request
OUT = sys.argv[1]
CK = open(r'C:\Users\dbour\cypher\targets\bordeaux\decode\cookie.txt', encoding='utf8').read().strip()
CK = re.sub(r'^cookie:\s*', '', CK, flags=re.I)
UA = "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 Chrome/128.0 Safari/537.36"
op = urllib.request.build_opener(urllib.request.ProxyHandler({}))
os.makedirs(OUT, exist_ok=True)
for rec in [int(a) for a in sys.argv[2:]]:
    r = urllib.request.Request('https://de-crypt.org/decrypt-web/RecordsView/%d' % rec, headers={'User-Agent': UA, 'Cookie': CK})
    h = op.open(r, timeout=60).read().decode('utf8', 'ignore')
    open(os.path.join(OUT, 'rec%d.htm' % rec), 'w', encoding='utf8').write(h)
    files = sorted(set(re.findall(r'filesrv/\?file=([A-Za-z0-9_.]+)', h)))
    logged = 'Logout' in h or 'logout' in h
    print(rec, 'logged-in' if logged else 'NOT logged in', len(h), files)
