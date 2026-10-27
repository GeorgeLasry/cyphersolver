"""Contact sheet per item: python sheets.py 22-2-51 ... -> img/small/sheet_<item>.jpg (pages 560 px wide, 4 per row)."""
import sys, glob
from PIL import Image

for item in sys.argv[1:]:
    fs = sorted(glob.glob('img/%s_*.jpg' % item))
    ims = []
    for f in fs:
        im = Image.open(f); im.thumbnail((560, 780)); ims.append(im)
    rows = (len(ims) + 3) // 4
    c = Image.new('RGB', (560 * 4, 780 * rows), 'white')
    for k, im in enumerate(ims):
        c.paste(im, ((k % 4) * 560, (k // 4) * 780))
    c.save('img/small/sheet_%s.jpg' % item, quality=85)
