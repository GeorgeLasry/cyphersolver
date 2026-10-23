"""b17: fetch Nationaal Archief scans (full-size jpg) of one inventory number into a scratch folder.

    python research/reading_audit/b17_na_fetch.py <outdir> <archive> <invnr> <scan> [<scan> ...]
e.g. b17_na_fetch.py OUT 3.01.18 401 91 92 99 100
The scan page's embedded file list gives each scan's service.archief.nl 'default' url.
"""
import json, os, re, sys, urllib.request
out, arch, inv = sys.argv[1:4]
scans = [int(x) for x in sys.argv[4:]]
UA = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) Chrome/128.0'}
os.makedirs(out, exist_ok=True)
pfx = 'NL-HaNA_%s_%s_' % (arch, inv)
url = 'https://www.nationaalarchief.nl/onderzoeken/archief/%s/invnr/%s/file/%s%04d' % (arch, inv, pfx, scans[0])
html = urllib.request.urlopen(urllib.request.Request(url, headers=UA), timeout=60).read().decode('utf8')
html = html.replace('\\u0022', '"').replace('\\/', '/')
files = dict(re.findall(r'"label":"(%s\d{4}\.jpg)","order":\d+,"default":\{"url":"([^"]+)"' % re.escape(pfx), html))
print(len(files), 'scans listed')
for n in scans:
    lab = '%s%04d.jpg' % (pfx, n)
    p = os.path.join(out, lab)
    if os.path.exists(p) and os.path.getsize(p) > 10000: continue
    d = urllib.request.urlopen(urllib.request.Request(files[lab], headers=UA), timeout=180).read()
    open(p, 'wb').write(d); print(lab, len(d))
