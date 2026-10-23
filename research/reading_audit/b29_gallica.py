"""b29: fetch a Gallica view (or a region of it) through openapi.bnf.fr IIIF into the scratchpad.

    python research/reading_audit/b29_gallica.py <ark> <view> <out.jpg> [region] [width]
    region: full | x,y,w,h | pct:x,y,w,h  (default full); width: e.g. max or 3000 (default max)
"""
import sys, time, urllib.request
ark, view, out = sys.argv[1], int(sys.argv[2]), sys.argv[3]
reg = sys.argv[4] if len(sys.argv) > 4 else 'full'
w = sys.argv[5] if len(sys.argv) > 5 else 'max'
size = 'max' if w == 'max' else w + ','
url = f'https://openapi.bnf.fr/iiif/image/v3/ark:/12148/{ark}/f{view}/{reg}/{size}/0/default.jpg'
UA = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 Chrome/128.0 Safari/537.36'}
for t in range(5):
    try:
        d = urllib.request.urlopen(urllib.request.Request(url, headers=UA), timeout=300).read()
        open(out, 'wb').write(d); print(view, len(d), out); break
    except Exception as e:
        print('retry', e); time.sleep(5 * (t + 1))
