"""Fetch every EAD XML finding aid listed at www.lib.uchicago.edu/ead/rlg/ (polite: 3 s between requests).
Stops on 403/429. Files go to ead/ (git-ignored scratch)."""
import os, re, sys, time, urllib.request
BASE = 'https://www.lib.uchicago.edu/ead/rlg/'
UA = 'Mozilla/5.0 (compatible; cyphersolver-archive-sweep/1.0; historical cipher catalogue)'
here = os.path.dirname(os.path.abspath(__file__))
idx = open(os.path.join(here, 'rlg_index.html'), encoding='utf-8', errors='replace').read()
names = sorted(set(n for n in re.findall(r'href="([^"]+\.xml)"', idx) if not n.startswith('.')))
PRI = re.compile(r'WILKINSONJ|BRECKINRIDGE|CLARK\.|CLARKGR|SHELBY|LYNEE|TODDRS|JTWILSON|HARTJ|DURRETT|DOUGLAS|BARTON|LINCOLN|MANLY|RICKERT|GARDOQUI|CODEX|MS\d|ITAL|FRENCH|CIVILWAR|BUTLER|WILKINSON|INNES|BURR|SEBASTIAN|CLAY|KENTUCKY', re.I)
names = [n for n in names if PRI.search(n)] + [n for n in names if not PRI.search(n)]
out = os.path.join(here, 'ead'); os.makedirs(out, exist_ok=True)
print(len(names), 'xml files', flush=True)
for i, n in enumerate(names):
    p = os.path.join(out, n)
    if os.path.exists(p) and os.path.getsize(p) > 0:
        continue
    req = urllib.request.Request(BASE + n, headers={'User-Agent': UA})
    try:
        with urllib.request.urlopen(req, timeout=60) as r:
            data = r.read()
        open(p, 'wb').write(data)
    except urllib.error.HTTPError as e:
        print('HTTP', e.code, n, flush=True)
        if e.code in (403, 429):
            print('stopping', flush=True); sys.exit(1)
    except Exception as e:
        print('ERR', n, e, flush=True)
    if i % 100 == 0:
        print(i, n, flush=True)
    time.sleep(3)
print('done', flush=True)
