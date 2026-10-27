import urllib.request, os, sys, io
from concurrent.futures import ThreadPoolExecutor
from PIL import Image, ImageOps
Image.MAX_IMAGE_PIXELS=None
B="https://www.arcinsys-digitalisate.niedersachsen.de/nla_ha/hann._9g/nr._{n}/m_ha_hann._9g_nr._{n}_aufn_{i:03d}.jpg"
def get(a):
    n,i=a; out=f"md{n}/{i:03d}.jpg"
    if os.path.exists(out): return
    d=urllib.request.urlopen(B.format(n=n,i=i),timeout=120).read()
    im=Image.open(io.BytesIO(d)).convert('L'); im.thumbnail((2400,2400))
    ImageOps.autocontrast(im,cutoff=1).save(out,quality=82)
jobs=[]
for arg in sys.argv[1:]:
    n,cnt=arg.split(':'); os.makedirs(f"md{n}",exist_ok=True)
    jobs+= [(n,i) for i in range(1,int(cnt)+1)]
with ThreadPoolExecutor(6) as ex: list(ex.map(get,jobs))
print('done',len(jobs))
