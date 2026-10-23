"""b35 (siena1431, siena15, soria1527, sp106r787, sp106r924): fetch DECODE record pages with the project cookie, list every file on them
(images IMG_*, documents DOC_*, attachments), print the record's text fields, and download every file to the scratchpad.

    python b33_fetch.py <outdir> <record> [<record> ...]
"""
import html, os, re, sys, urllib.request
OUT = sys.argv[1]
CK = open(r'C:\Users\dbour\cypher\targets\bordeaux\decode\cookie.txt', encoding='utf8').read().strip()
CK = re.sub(r'^cookie:\s*', '', CK, flags=re.I)
UA = "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 Chrome/128.0 Safari/537.36"
op = urllib.request.build_opener(urllib.request.ProxyHandler({}))


def get(url):
    r = urllib.request.Request(url, headers={'User-Agent': UA, 'Cookie': CK})
    return op.open(r, timeout=120).read()


for rec in [int(a) for a in sys.argv[2:]]:
    d = os.path.join(OUT, 'R%d' % rec)
    os.makedirs(d, exist_ok=True)
    h = get('https://de-crypt.org/decrypt-web/RecordsView/%d' % rec).decode('utf8', 'ignore')
    open(os.path.join(d, 'rec.htm'), 'w', encoding='utf8').write(h)
    files = sorted(set(re.findall(r'filesrv/\?file=(?:TH_)?([^"\'&<> ]+)', h)))
    logged = 'logout' in h.lower()
    print('==', rec, 'logged-in' if logged else 'NOT logged in', len(h), len(files), 'files')
    txt = re.sub(r'<script.*?</script>|<style.*?</style>', ' ', h, flags=re.S)
    txt = html.unescape(re.sub(r'<[^>]+>', '\n', txt))
    txt = '\n'.join(l.strip() for l in txt.splitlines() if l.strip())
    open(os.path.join(d, 'rec.txt'), 'w', encoding='utf8').write(txt)
    for f in files:
        p = os.path.join(d, os.path.basename(f))
        if not os.path.exists(p) or os.path.getsize(p) < 2000:
            try:
                open(p, 'wb').write(get('https://de-crypt.org/decrypt-custom/filesrv/?file=' + f))
            except Exception as e:
                print('  fail', f, e); continue
        print('  ', f, os.path.getsize(p))
