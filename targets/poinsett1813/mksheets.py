"""Contact sheets, 6 frames each: python mksheets.py <imgdir> <outdir> <prefix> [from to]"""
import sys, glob, os
from PIL import Image
src, out, pre = sys.argv[1:4]
a, b = (int(sys.argv[4]), int(sys.argv[5])) if len(sys.argv) > 5 else (0, 99999)
fs = sorted(f for f in glob.glob(f'{src}/{pre}-*.jpg') if a <= int(f[-8:-4]) <= b)
os.makedirs(out, exist_ok=True)
W, H = 800, 545
for k in range(0, len(fs), 6):
    sh = Image.new('L', (W * 3, H * 2), 255)
    for i, f in enumerate(fs[k:k + 6]):
        im = Image.open(f).convert('L'); im.thumbnail((W, H))
        sh.paste(im, ((i % 3) * W, (i // 3) * H))
    sh.save(f'{out}/s{int(fs[k][-8:-4]):04d}.jpg', quality=70)
print(len(fs))
