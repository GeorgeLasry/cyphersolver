"""DECODE JSON API helper (cookie from targets/bordeaux/decode/cookie.txt + page JWT)."""
import json, os, re, sys, time, urllib.request
ROOT = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
BASE = "https://de-crypt.org/decrypt-web/"
UA = "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 Chrome/128.0 Safari/537.36"
op = urllib.request.build_opener(urllib.request.ProxyHandler({}))
def cookie():
    return open(os.path.join(ROOT, "targets", "bordeaux", "decode", "cookie.txt"), encoding="utf-8").read().strip()
def get(url, hdr=None):
    h = {"User-Agent": UA, "Cookie": cookie()}; h.update(hdr or {})
    return op.open(urllib.request.Request(url, headers=h), timeout=120).read().decode("utf-8", "replace")
def jwt():
    html = get(BASE + "RecordsView/7537")
    return re.search(r'"API_JWT_TOKEN":"([^"]+)"', html).group(1)
def api(path, tok):
    return json.loads(get(BASE + "api/" + path, {"X-Authorization": "Bearer " + tok}))
if __name__ == "__main__":
    tok = jwt()
    print(json.dumps(api("view/Records/" + sys.argv[1], tok), ensure_ascii=False)[:3000])
