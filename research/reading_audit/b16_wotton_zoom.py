"""b16 (wotton1585): one zoomed crop of a DECODE page image. Usage: b16_wotton_zoom.py REC PAGE X0 X1 Y0 Y1 NAME [WIDTH]"""
import sys
from PIL import Image, ImageOps
rec, page = sys.argv[1], sys.argv[2]
x0, x1, y0, y1 = map(float, sys.argv[3:7]); name = sys.argv[7]; W = int(sys.argv[8]) if len(sys.argv) > 8 else 1800
S = 'C:/Users/dbour/AppData/Local/Temp/claude/C--Users-dbour-cypher/6b6912a8-0ad3-4eda-b63e-c79291f1bcc5/scratchpad/reread/wotton/'
im = Image.open(f'C:/Users/dbour/cypher/targets/wotton1585/decode/R{rec}_p{page}.jpg').convert('L')
w, h = im.size
c = ImageOps.autocontrast(im.crop((int(x0 * w), int(y0 * h), int(x1 * w), int(y1 * h))), cutoff=1)
c = c.resize((W, int(c.size[1] * W / c.size[0])), Image.LANCZOS); c.save(S + name + '.jpg', quality=90); print(c.size)
