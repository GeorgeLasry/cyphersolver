"""r2l: zoom a region of a V2831 plate.  python r2l_zoom.py <page> <name> <xa> <xb> <yc> [scale] [half]"""
import sys
from PIL import Image, ImageOps
p, nm, xa, xb, yc = sys.argv[1], sys.argv[2], *map(int, sys.argv[3:6])
sc = float(sys.argv[6]) if len(sys.argv) > 6 else 2.5; hh = int(sys.argv[7]) if len(sys.argv) > 7 else 50
im = Image.open(rf'C:\Users\dbour\cypher\targets\buda1489\img\v2831_p{p}r.jpg').convert('L')
c = im.crop((xa, yc - hh, xb, yc + hh)); c = c.resize((int(c.width * sc), int(c.height * sc)), Image.LANCZOS)
ImageOps.autocontrast(c, cutoff=1).save(f'C:/Users/dbour/AppData/Local/Temp/claude/C--Users-dbour-cypher/6b6912a8-0ad3-4eda-b63e-c79291f1bcc5/scratchpad/reread/r2l/z_{nm}.png')
