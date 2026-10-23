"""verify1 (sauli1579): crop a region of a DECODE page image (session scratchpad copy) for checking a gloss word.
    python research/reading_audit/verify1_sauli_crop.py IMG_R192_I1235_P5 x0 y0 x1 y1 out.png [scale]"""
import sys
from PIL import Image
D = r'C:\Users\dbour\AppData\Local\Temp\claude\C--Users-dbour-cypher\6b6912a8-0ad3-4eda-b63e-c79291f1bcc5\scratchpad\reread\sauli'
name, x0, y0, x1, y1, out = sys.argv[1:7]
sc = float(sys.argv[7]) if len(sys.argv) > 7 else 1.0
im = Image.open(f'{D}\{name}.jpg').crop((int(x0), int(y0), int(x1), int(y1)))
if sc != 1.0:
    im = im.resize((int(im.width * sc), int(im.height * sc)))
im.save(out)
print(im.size)
