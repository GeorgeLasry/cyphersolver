"""Fetch DECODE record images: fetch_keys.py FIRST LAST [OUTDIR]. Default: cart. 1597 keys R5301-R5336 into img/keys/.
Uses targets/bordeaux/decode/cookie.txt (git-ignored). Run from the repo root."""
import os, re, sys, time, urllib.request
C = open('targets/bordeaux/decode/cookie.txt').read().strip()
UA = 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) Chrome/128.0'
OUT = sys.argv[3] if len(sys.argv) > 3 else 'targets/visconti1446/img/keys'
os.makedirs(OUT, exist_ok=True)
def get(u):
    r = urllib.request.Request(u, headers={'Cookie': C, 'User-Agent': UA})
    return urllib.request.urlopen(r, timeout=120).read()
lo, hi = (int(a) for a in sys.argv[1:3]) if len(sys.argv) > 2 else (5301, 5336)
for rid in range(lo, hi + 1):
    h = get('https://de-crypt.org/decrypt-web/RecordsView/%d' % rid).decode('utf8', 'ignore')
    files = sorted(set(re.findall(r'filesrv/\?file=([A-Za-z0-9_]+)\.(\w+)', h)))
    for stem, ext in files:
        fn = '%s/R%d_%s.%s' % (OUT, rid, stem, ext)
        if os.path.exists(fn): continue
        b = get('https://de-crypt.org/decrypt-custom/filesrv/?file=%s.%s' % (stem, ext))
        open(fn, 'wb').write(b)
    print(rid, len(files), flush=True)
    time.sleep(.3)
