"""b37: fetch the DOC files of a range of DECODE records (no images) and test each key file against glossed groups.
python b37_keyscan.py <outdir> <from> <to>"""
import re, sys, urllib.request
from pathlib import Path
cookie = re.sub(r"^cookie:\s*", "", Path(r"C:/Users/dbour/cypher/targets/bordeaux/decode/cookie.txt").read_text(encoding="utf-8").strip(), flags=re.I)
def get(u, ref=None):
    h = {"User-Agent": "Mozilla/5.0", "Cookie": cookie}
    if ref: h["Referer"] = ref
    return urllib.request.urlopen(urllib.request.Request(u, headers=h), timeout=90).read()
out = Path(sys.argv[1]); out.mkdir(parents=True, exist_ok=True)
# glossed groups of R473 (gloss syllable, normalised)
TEST = {'300': 'a', '22': 'n', '200': 'k', '19': 'l', '193': 'po', '26': 's', '213': 'ta', '68': 'ad', '181': 'ok',
        '228': 'va', '140': 'r', '89': 'do', '123': 'na', '214': 'te', '113': 'fe', '175': 'mi', '101': 'el', '17': 'i'}
for rid in range(int(sys.argv[2]), int(sys.argv[3]) + 1):
    try:
        url = f"https://de-crypt.org/decrypt-web/RecordsView/{rid}"
        html = get(url)
    except Exception as e:
        print(rid, 'err', e); continue
    docs = sorted(set(re.findall(rb"DOC_R%d_[A-Za-z0-9_.-]+\.txt" % rid, html)))
    for d in docs:
        f = out / d.decode()
        if not f.exists():
            f.write_bytes(get(f"https://de-crypt.org/decrypt-custom/filesrv/?file={d.decode()}", url))
        t = f.read_text(encoding='utf-8-sig', errors='ignore')
        if not t.lstrip().startswith('#KEY'):
            continue
        m = {}
        for line in t.splitlines():
            mm = re.match(r'\s*([\d|]+)\s*-\s*(.+?)\s*$', line)
            if mm:
                for c in mm.group(1).split('|'):
                    if c: m[c] = mm.group(2).lower()
        hit = sum(1 for c, v in TEST.items() if m.get(c, '').replace('j', 'i') == v)
        cat = re.search(r'#CATALOG NAME:\s*(\S+)', t)
        lang = re.search(r'#LANGUAGE:\s*(\S+)', t)
        print(rid, d.decode(), cat.group(1) if cat else '', lang.group(1) if lang else '', 'hits', hit, '/', len(TEST))
