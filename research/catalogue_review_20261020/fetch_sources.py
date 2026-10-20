"""Fetch source evidence; keep authenticated pages in ignored decode/ only."""
import concurrent.futures, json, pathlib, re, subprocess, sys, urllib.request

HERE = pathlib.Path(__file__).resolve().parent
ROOT = HERE.parent.parent
CACHE = HERE / 'decode'
CACHE.mkdir(exist_ok=True)
COMMON = pathlib.Path(subprocess.check_output(
    ['git','rev-parse','--path-format=absolute','--git-common-dir'],cwd=ROOT,text=True).strip()).parent
COOKIE_FILE = ROOT/'targets/bordeaux/decode/cookie.txt'
if not COOKIE_FILE.exists():
    COOKIE_FILE = COMMON/'targets/bordeaux/decode/cookie.txt'

def fetch(task):
    label, url = task
    out = CACHE / (label if label.startswith('IMG_') else label + '.html')
    if out.exists():
        return label, len(out.read_bytes()), 'cached'
    headers = {'User-Agent': 'Mozilla/5.0'}
    if url.startswith('https://de-crypt.org/') and COOKIE_FILE.exists():
        headers['Cookie'] = re.sub(r'^cookie:\s*', '', COOKIE_FILE.read_text().strip(), flags=re.I)
    try:
        op = urllib.request.build_opener(urllib.request.ProxyHandler({}))
        with op.open(urllib.request.Request(url, headers=headers), timeout=30) as response:
            data = response.read()
        if label.startswith('IMG_') and len(data)==17947:
            return label, 0, 'DECODE forbidden placeholder; image not saved'
        out.write_bytes(data)
        return label, len(data), 'ok'
    except Exception as exc:
        return label, 0, type(exc).__name__ + ': ' + str(exc)

if __name__ == '__main__':
    if len(sys.argv) > 1 and sys.argv[1] == 'images':
        tasks = []
        for page in CACHE.glob('R*.html'):
            names = sorted(set(re.findall(r'TH_(IMG_[A-Za-z0-9_.]+)', page.read_text(encoding='utf-8'))))
            if page.stem.startswith('R'):
                tasks.extend((n, 'https://de-crypt.org/decrypt-custom/filesrv/?file='+n) for n in names)
        with concurrent.futures.ThreadPoolExecutor(max_workers=4) as pool:
            results = list(pool.map(fetch, tasks))
        (HERE/'image_access.json').write_text(json.dumps(results, indent=2)+'\n')
        for result in results: print(*result)
        sys.exit()
    records = [1162,1163,1164,1165,1166,1167,1168,1095,1096,1097,8395,8398,4886,10181,10196,1579]
    tasks = [('R'+str(r), 'https://de-crypt.org/decrypt-web/RecordsView/'+str(r)) for r in records]
    tasks += [
        ('brussels1660', 'https://www.british-history.ac.uk/thurloe-papers/vol7/pp860-869'),
        ('hyde1659', 'https://www.british-history.ac.uk/thurloe-papers/vol7/pp771-781'),
        ('sirtori', 'https://ciphermysteries.com/2012/06/14/girolamo-sirtori-cipher-mystery'),
        ('habsburg', 'https://cryptiana.web.fc2.com/code/habsburg.htm'),
        ('rupert', 'https://cryptiana.web.fc2.com/code/rupert.htm'),
        ('charlesii2', 'https://cryptiana.web.fc2.com/code/charlesii2.htm'),
        ('louisxiv0', 'https://cryptiana.web.fc2.com/code/louisxiv0.htm'),
        ('louisxiv', 'https://cryptiana.web.fc2.com/code/louisxiv.htm'),
    ]
    if len(sys.argv)>1 and sys.argv[1]=='records':
        tasks=[('R'+r,'https://de-crypt.org/decrypt-web/RecordsView/'+r) for r in sys.argv[2:]]
    if len(sys.argv)>1 and sys.argv[1]=='catinat':
        tasks=[('catinat1702_1','https://cryptiana.web.fc2.com/code/catinat1702_1.txt')]
    with concurrent.futures.ThreadPoolExecutor(max_workers=4) as pool:
        results = list(pool.map(fetch, tasks))
    (HERE/'access.json').write_text(json.dumps(results, indent=2)+'\n')
    for result in results:
        print(*result)
