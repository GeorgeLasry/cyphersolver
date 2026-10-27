"""Download the full-size AIS images of one unit of description.
python fetch_ais.py <AIS ID> <label>   -> img/<label>_<n>.jpg (img/ is git-ignored)"""
import os, re, sys, requests

vid, label = sys.argv[1], sys.argv[2]
s = requests.Session(); s.headers['User-Agent'] = 'Mozilla/5.0 (research)'
page = s.get('https://www.archivinformationssystem.at/detail.aspx?ID=' + vid, timeout=60).text
n = max(int(x) for x in re.findall(r'getimage\.aspx\?veid=%s&(?:amp;)?deid=0&(?:amp;)?sqnznr=(\d+)' % vid, page))
os.makedirs(os.path.join(os.path.dirname(__file__), 'img'), exist_ok=True)
for i in range(1, n + 1):
    out = os.path.join(os.path.dirname(__file__), 'img', '%s_%02d.jpg' % (label, i))
    if os.path.exists(out): continue
    r = s.get('https://www.archivinformationssystem.at/getimage.aspx?veid=%s&deid=10&sqnznr=%d&width=4000&klid=9' % (vid, i), timeout=120)
    open(out, 'wb').write(r.content)
print(label, n, 'images')
