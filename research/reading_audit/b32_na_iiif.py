"""b32: Nationaal Archief scans of one inventory number through the archive's IIIF server, at a chosen width or region.

    python b32_na_iiif.py <outdir> <archive> <invnr> <width|full> <scan>[-<scan>] [...] [--region x,y,w,h]

The inventory page embeds, per scan, a IIIF info.json URL (service.archief.nl/iip/iipsrv?IIIF=...jp2); the image is
<base>/<region>/<width>,/0/default.jpg. Saves <outdir>/<invnr>_<scan>[_<region>]_<width>.jpg.
"""
import os, re, sys, urllib.request
args = [a for a in sys.argv[1:] if not a.startswith('--region')]
reg = 'full'
for i, a in enumerate(sys.argv):
    if a == '--region':
        reg = sys.argv[i + 1]; args.remove(reg)
out, arch, inv, width = args[:4]
UA = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) Chrome/128.0'}
os.makedirs(out, exist_ok=True)
cache = os.path.join(out, 'inv_%s_%s.htm' % (arch, inv))
if not os.path.exists(cache):
    url = 'https://www.nationaalarchief.nl/onderzoeken/archief/%s/invnr/%s' % (arch, inv)
    open(cache, 'wb').write(urllib.request.urlopen(urllib.request.Request(url, headers=UA), timeout=60).read())
html = open(cache, encoding='utf8').read()
BS = chr(92); html = html.replace(BS + "u0022", chr(34)).replace(BS + "/", "/")
pfx = 'NL-HaNA_%s_%s_' % (arch, inv)
iiif = {int(n): u for n, u in re.findall(r'"label":"%s(\d{4})\.jpg".*?"iiif":\{"url":"([^"]+)/info\.json"' % re.escape(pfx), html)}
print(len(iiif), 'scans listed')
want = []
for a in args[4:]:
    if '-' in a:
        x, y = map(int, a.split('-')); want += list(range(x, y + 1))
    else:
        want.append(int(a))
for n in want:
    if n not in iiif:
        print(n, 'not listed'); continue
    w = 'max' if width == 'full' else width + ','
    tag = '' if reg == 'full' else '_' + reg.replace(',', '-').replace(':', '')
    p = os.path.join(out, '%s_%04d%s_%s.jpg' % (inv, n, tag, width))
    if os.path.exists(p) and os.path.getsize(p) > 5000: continue
    u = '%s/%s/%s/0/default.jpg' % (iiif[n], reg, w)
    for k in range(3):
        try:
            d = urllib.request.urlopen(urllib.request.Request(u, headers=UA), timeout=180).read(); break
        except Exception as e:
            print(n, 'retry', e); d = None
    if d:
        open(p, 'wb').write(d); print(p, len(d))
