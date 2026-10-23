"""b33 (rennes1563): fetch every view of 500 Colbert 390 (Gallica btv1b10033942k, 184 views) at 600 px through
openapi.bnf.fr IIIF and make labelled contact sheets (12 views each), to look for a clear copy or decipherment of the
p. 139 note ("Deschiffrez vous mesmes", view 70) elsewhere in the volume.

    python research/reading_audit/b33_rn_sheet.py <outdir>
"""
import os, sys, time, urllib.request
from PIL import Image, ImageOps, ImageDraw
out = sys.argv[1]; os.makedirs(out, exist_ok=True)
UA = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) Chrome/128.0'}
N = 184
for i in range(1, N + 1):
    fn = os.path.join(out, 'v%03d.jpg' % i)
    if os.path.exists(fn) and os.path.getsize(fn) > 3000: continue
    url = 'https://openapi.bnf.fr/iiif/image/v3/ark:/12148/btv1b10033942k/f%d/full/600,/0/default.jpg' % i
    for t in range(4):
        try:
            open(fn, 'wb').write(urllib.request.urlopen(urllib.request.Request(url, headers=UA), timeout=120).read()); break
        except Exception as e:
            print(i, 'fail', e); time.sleep(5 * (t + 1))
W = 600
for s in range(1, N + 1, 12):
    ids = list(range(s, min(s + 12, N + 1)))
    ims = []
    for i in ids:
        try: im = ImageOps.autocontrast(Image.open(os.path.join(out, 'v%03d.jpg' % i)).convert('L'), cutoff=1)
        except Exception: im = Image.new('L', (W, W), 128)
        ims.append(im)
    h = max(im.height for im in ims); cols = 4; rows = (len(ims) + 3) // 4
    sheet = Image.new('L', (W * cols, (h + 24) * rows), 255); d = ImageDraw.Draw(sheet)
    for k, im in enumerate(ims):
        x = W * (k % cols); y = (h + 24) * (k // cols); sheet.paste(im, (x, y + 24)); d.text((x + 6, y + 4), 'view %d' % ids[k], fill=0)
    sheet.save(os.path.join(out, 'sheet_%03d.png' % s))
print('done')
