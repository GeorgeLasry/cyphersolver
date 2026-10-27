"""contact.py <dir> <first> <last> <out.jpg> [width] [cols]: tile images first..last (1-based) with labels."""
import sys, os
from PIL import Image, ImageDraw

d, a, b, out = sys.argv[1], int(sys.argv[2]), int(sys.argv[3]), sys.argv[4]
W = int(sys.argv[5]) if len(sys.argv) > 5 else 400
cols = int(sys.argv[6]) if len(sys.argv) > 6 else 5
files = sorted(f for f in os.listdir(d) if f.endswith('.jpg'))[a - 1:b]
tiles = []
for f in files:
    im = Image.open(os.path.join(d, f)).convert('L')
    im = im.resize((W, int(im.height * W / im.width)))
    dr = ImageDraw.Draw(im); dr.rectangle((0, 0, 60, 22), fill=255); dr.text((4, 4), f[:3], fill=0)
    tiles.append(im)
H = max(t.height for t in tiles)
rows = (len(tiles) + cols - 1) // cols
sheet = Image.new('L', (W * cols, H * rows), 255)
for i, t in enumerate(tiles):
    sheet.paste(t, ((i % cols) * W, (i // cols) * H))
sheet.save(out, quality=80)
