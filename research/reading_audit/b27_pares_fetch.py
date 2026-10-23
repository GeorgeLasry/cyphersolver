"""b27: fetch the images of a PARES record (fresh cookie jar, show page first, zoom 10), into a scratch dir.

    python research/reading_audit/b27_pares_fetch.py <record id> <out dir> [first last]
"""
import http.cookiejar, os, re, sys, urllib.request
rec, out = sys.argv[1], sys.argv[2]
first, last = (int(sys.argv[3]), int(sys.argv[4])) if len(sys.argv) > 4 else (1, 60)
os.makedirs(out, exist_ok=True)
UA = 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 Chrome/128.0 Safari/537.36'
cj = http.cookiejar.CookieJar()
op = urllib.request.build_opener(urllib.request.HTTPCookieProcessor(cj))
B = 'https://pares.cultura.gob.es/ParesBusquedas20/'
h = op.open(urllib.request.Request(B + 'catalogo/show/' + rec, headers={'User-Agent': UA}), timeout=60).read().decode('utf8', 'ignore')
db = re.search(r'dbCode=(\d+)', h).group(1)
n = re.search(r'txt_totalImagenes[^0-9]*(\d+)', h)
print('dbCode', db, 'images', n.group(1) if n else '?')
for i in range(first, last + 1):
    u = (B + f'ViewImage.do?accion=42&txt_descarga=1&dbCode={db}&txt_id_imagen={i}&txt_zoom=10&txt_contraste=0'
         '&txt_polarizado=&txt_brillo=10.0&txt_contrast=1.0')
    d = op.open(urllib.request.Request(u, headers={'User-Agent': UA}), timeout=120).read()
    if len(d) < 3000: print('stop at', i, len(d)); break
    open(os.path.join(out, f'{rec}_{i:02d}.jpg'), 'wb').write(d); print(i, len(d))
