"""b28: contact sheet of images (labels = file stems).  python b28_sheet.py <out.jpg> <cols> <w> img1 img2 ..."""
import sys, os
from PIL import Image, ImageDraw
out, cols, w = sys.argv[1], int(sys.argv[2]), int(sys.argv[3]); fs = sys.argv[4:]
ims = []
for f in fs:
    im = Image.open(f).convert('L'); im = im.resize((w, int(im.height * w / im.width))); ims.append((os.path.basename(f), im))
h = max(i.height for _, i in ims); rows = (len(ims) + cols - 1) // cols
sh = Image.new('L', (cols * w, rows * (h + 20)), 255); d = ImageDraw.Draw(sh)
for k, (n, im) in enumerate(ims):
    x, y = (k % cols) * w, (k // cols) * (h + 20); sh.paste(im, (x, y + 20)); d.text((x + 4, y + 4), n, fill=0)
sh.save(out, quality=85)
