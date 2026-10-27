"""Stitch full-resolution tiles from a IIIF level-0 image service.
usage: python iiif_stitch.py <service-id> <out.jpg>"""
import io, json, sys, urllib.request
from PIL import Image

def get(url):
    req = urllib.request.Request(url, headers={'User-Agent': 'Mozilla/5.0'})
    return urllib.request.urlopen(req, timeout=60).read()

svc, out = sys.argv[1], sys.argv[2]
info = json.loads(get(svc + '/info.json'))
W, H = info['width'], info['height']
T = info['tiles'][0]['width']
img = Image.new('RGB', (W, H), 'white')
for y in range(0, H, T):
    for x in range(0, W, T):
        w, h = min(T, W - x), min(T, H - y)
        tile = Image.open(io.BytesIO(get(f'{svc}/{x},{y},{w},{h}/{w},/0/default.jpg')))
        img.paste(tile, (x, y))
img.save(out, quality=92)
print(out, W, H)
