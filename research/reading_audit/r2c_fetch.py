"""r2c (23 Oct 2026): fetch DECODE record pages, DOC files and full-size images into the scratchpad (cookie: targets/bordeaux/decode/cookie.txt).
python b37_fetch.py <outdir> <record id> [...]"""
from pathlib import Path
import re, sys, urllib.request
BASE = "https://de-crypt.org"
cookie = re.sub(r"^cookie:\s*", "", Path(r"C:/Users/dbour/cypher/targets/bordeaux/decode/cookie.txt").read_text(encoding="utf-8").strip(), flags=re.I)
def get(url, ref=None):
    h = {"User-Agent": "Mozilla/5.0", "Cookie": cookie}
    if ref: h["Referer"] = ref
    with urllib.request.urlopen(urllib.request.Request(url, headers=h), timeout=120) as r:
        d = r.read()
    if len(d) == 17947: raise RuntimeError("cookie rejected")
    return d
out = Path(sys.argv[1]); out.mkdir(parents=True, exist_ok=True)
for rid in map(int, sys.argv[2:]):
    url = f"{BASE}/decrypt-web/RecordsView/{rid}"
    html = get(url)
    (out / f"rec{rid}.htm").write_bytes(html)
    names = sorted(set(re.findall(rb"((?:DOC|IMG)_R%d_[A-Za-z0-9_.-]+.(?:png|jpg|txt|xlsx|pdf|docx))" % rid, html)))
    print(rid, len(html), [n.decode() for n in names])
    for n in names:
        n = n.decode()
        if 'TH_' in n or n.startswith('IMG_'): continue
        f = out / n
        if f.exists(): continue
        f.write_bytes(get(f"{BASE}/decrypt-custom/filesrv/?file={n}", url))
        print('  ', n, f.stat().st_size)
