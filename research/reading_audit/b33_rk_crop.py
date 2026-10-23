"""Crop R483 page images (rakoczi1711) into the scratchpad for viewing.
usage: python b33_rk_crop.py <page 1-6> <x0> <y0> <x1> <y1> <out-name> [scale]"""
import sys
from PIL import Image
S = r'C:/Users/dbour/AppData/Local/Temp/claude/C--Users-dbour-cypher/6b6912a8-0ad3-4eda-b63e-c79291f1bcc5/scratchpad/reread/R483/'
IM = {1: 'IMG_R483_I3666_P1', 2: 'IMG_R483_I3667_P2', 3: 'IMG_R483_I3668_P3',
      4: 'IMG_R483_I3669_P4', 5: 'IMG_R483_I3670_P5', 6: 'IMG_R483_I3671_P6'}
p, x0, y0, x1, y1 = map(int, sys.argv[1:6])
out = sys.argv[6]
sc = float(sys.argv[7]) if len(sys.argv) > 7 else 1.0
im = Image.open(S + IM[p] + '.png').convert('RGB').crop((x0, y0, x1, y1))
if sc != 1.0:
    im = im.resize((int(im.width * sc), int(im.height * sc)), Image.LANCZOS)
im.save(S + 'crops/' + out + '.jpg', quality=88)
print(S + 'crops/' + out + '.jpg', im.size)
