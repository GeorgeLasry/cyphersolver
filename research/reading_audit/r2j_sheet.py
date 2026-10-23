"""r2j: fetch a range of Gallica views at a given width through openapi.bnf.fr IIIF and make labelled contact sheets.

    python research/reading_audit/r2j_sheet.py <ark> <first> <last> <outdir> [width] [per_sheet]
"""
import os, sys, time, urllib.request
from PIL import Image, ImageOps, ImageDraw
ark, a, b, out = sys.argv[1], int(sys.argv[2]), int(sys.argv[3]), sys.argv[4]
W = int(sys.argv[5]) if len(sys.argv) > 5 else 600
PER = int(sys.argv[6]) if len(sys.argv) > 6 else 8
os.makedirs(out, exist_ok=True)
UA = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) Chrome/128.0'}
for i in range(a, b + 1):
    fn = os.path.join(out, 'v%04d_%d.jpg' % (i, W))
    if os.path.exists(fn) and os.path.getsize(fn) > 3000: continue
    url = 'https://openapi.bnf.fr/iiif/image/v3/ark:/12148/%s/f%d/full/%d,/0/default.jpg' % (ark, i, W)
    for t in range(4):
        try:
            open(fn, 'wb').write(urllib.request.urlopen(urllib.request.Request(url, headers=UA), timeout=120).read()); break
        except Exception as e:
            print(i, 'fail', e); time.sleep(5 * (t + 1))
ids_all = list(range(a, b + 1))
for s in range(0, len(ids_all), PER):
    ids = ids_all[s:s + PER]; ims = []
    for i in ids:
        try: im = ImageOps.autocontrast(Image.open(os.path.join(out, 'v%04d_%d.jpg' % (i, W))).convert('L'), cutoff=1)
        except Exception: im = Image.new('L', (W, W), 128)
        ims.append(im)
    h = max(im.height for im in ims); cols = 4; rows = (len(ims) + 3) // 4
    sheet = Image.new('L', (W * cols, (h + 24) * rows), 255); d = ImageDraw.Draw(sheet)
    for k, im in enumerate(ims):
        x = W * (k % cols); y = (h + 24) * (k // cols); sheet.paste(im, (x, y + 24)); d.text((x + 6, y + 4), 'view %d' % ids[k], fill=0)
    sheet.save(os.path.join(out, 'sheet_%04d.png' % ids[0]))
print('done')
