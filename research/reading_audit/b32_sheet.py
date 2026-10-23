"""b32: contact sheet of image files.  python b32_sheet.py <out.jpg> <cols> <cell_width> <img> [...]  (labels = file name)"""
import os, sys
from PIL import Image, ImageDraw
out, cols, cw = sys.argv[1], int(sys.argv[2]), int(sys.argv[3])
cells = []
for f in sys.argv[4:]:
    if not os.path.exists(f):
        continue
    im = Image.open(f).convert('L')
    h = int(im.height * cw / im.width); cells.append((f, im.resize((cw, h))))
ch = max(c[1].height for c in cells) + 20
rows = (len(cells) + cols - 1) // cols
S = Image.new('L', (cols * cw, rows * ch), 255); d = ImageDraw.Draw(S)
for i, (f, c) in enumerate(cells):
    x, y = (i % cols) * cw, (i // cols) * ch
    S.paste(c, (x, y + 20)); d.text((x + 4, y + 4), os.path.basename(f), fill=0)
S.save(out, quality=85)
