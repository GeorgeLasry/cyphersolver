"""b19: list and fetch Nationaal Archief scans of one inventory number from its inventory page (the scan list is
embedded in the page).  python b19_na_fetch.py <outdir> <archive> <invnr> [all | <scan> ...]"""
import os, re, sys, urllib.request
out, arch, inv = sys.argv[1:4]
UA = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) Chrome/128.0'}
os.makedirs(out, exist_ok=True)
pfx = 'NL-HaNA_%s_%s_' % (arch, inv)
url = 'https://www.nationaalarchief.nl/onderzoeken/archief/%s/invnr/%s' % (arch, inv)
html = urllib.request.urlopen(urllib.request.Request(url, headers=UA), timeout=60).read().decode('utf8')
BS = chr(92); html = html.replace(BS + "u0022", chr(34)).replace(BS + "/", "/")
files = dict(re.findall(r'"label":"(%s\d{4}\.jpg)","order":\d+,"default":\{"url":"([^"]+)"' % re.escape(pfx), html))
print(len(files), 'scans listed')
want = sorted(files) if sys.argv[4:] == ['all'] else ['%s%04d.jpg' % (pfx, int(n)) for n in sys.argv[4:]]
for lab in want:
    p = os.path.join(out, lab)
    if os.path.exists(p) and os.path.getsize(p) > 10000: continue
    try:
        d = urllib.request.urlopen(urllib.request.Request(files[lab], headers=UA), timeout=180).read()
    except Exception as e:
        print(lab, 'fail', e); continue
    open(p, 'wb').write(d); print(lab, len(d))
