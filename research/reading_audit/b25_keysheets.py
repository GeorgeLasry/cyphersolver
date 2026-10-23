"""b25: contact sheets of the heading band of each Sforza key image (DECODE cart. 1597/1591/1598 downloads), to look
for the key of Maffeo da Treviglio's Hungarian embassy (1489-90).
    python b25_keysheets.py <keydir> <outdir> [per_sheet]"""
import os, sys, glob
from PIL import Image, ImageOps, ImageDraw
src, out = sys.argv[1], sys.argv[2]; per = int(sys.argv[3]) if len(sys.argv) > 3 else 8
os.makedirs(out, exist_ok=True)
fs = sorted(f for f in glob.glob(os.path.join(src, '*')) if os.environ.get('PAT', '1597') in f)
W = 1400
for s in range(0, len(fs), per):
    bands = []
    for f in fs[s:s + per]:
        try:
            if f.lower().endswith('.pdf'):
                import pymupdf, io
                d = pymupdf.open(f); pg = d[0]; pix = pg.get_pixmap(dpi=110)
                im = Image.open(io.BytesIO(pix.tobytes('png'))).convert('L')
            else:
                im = Image.open(f).convert('L')
        except Exception as e:
            print('skip', f, e); continue
        b = im.crop((0, 0, im.width, int(im.height * 0.22)))
        b = b.resize((W, int(b.height * W / b.width)))
        b = ImageOps.autocontrast(b, cutoff=1)
        c = Image.new('L', (W, b.height + 30), 255); c.paste(b, (0, 30))
        ImageDraw.Draw(c).text((5, 5), os.path.basename(f)[:90], fill=0)
        bands.append(c)
    if not bands: continue
    H = sum(b.height for b in bands)
    sheet = Image.new('L', (W, H), 255); y = 0
    for b in bands: sheet.paste(b, (0, y)); y += b.height
    sheet.save(os.path.join(out, 'sheet_%03d.png' % (s // per)))
print(len(fs), 'files')
