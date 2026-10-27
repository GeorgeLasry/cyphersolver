"""Walk NARA microfilm reels through their OCR text and flag frames that look like numeric code.

    python research/nara_reels/reels.py fetch <reel naId> [...]   # cache record + OCR text (one request each)
    python research/nara_reels/reels.py score <reel naId> [...]   # print flagged frames

The catalogue serves a reel's whole OCR text in one call: /proxy/extractedText/<naId>?limit=1000&page=1, and its frame
list (filenames such as M31-024-0002.jpg) in the record: /proxy/records/search?naId=<naId>. Both are cached under
cache/ (git-ignored), and requests are spaced by PAUSE seconds so the walk never bursts.
"""
import json, os, re, sys, time, urllib.request

HERE = os.path.dirname(os.path.abspath(__file__))
CACHE = os.path.join(HERE, 'cache')
BASE = 'https://catalog.archives.gov/proxy/'
UA = {'User-Agent': 'cyphersolver research (catalogue sweep; contact via github.com/dbourdeau/cyphersolver)',
      'Accept': 'application/json'}
PAUSE = 4.0
_last = [0.0]


def get(path):
    wait = _last[0] + PAUSE - time.time()
    if wait > 0:
        time.sleep(wait)
    for attempt in range(5):
        _last[0] = time.time()
        try:
            with urllib.request.urlopen(urllib.request.Request(BASE + path, headers=UA), timeout=180) as r:
                body = r.read().decode('utf-8')
            if body.lstrip().startswith('{'):
                return json.loads(body)
        except urllib.error.HTTPError as e:
            if e.code in (429, 503):
                time.sleep(60 * (attempt + 1))  # back off hard; never hammer
                continue
            raise
        except Exception:
            pass
        time.sleep(15 * (attempt + 1))
    raise RuntimeError(f'failed: {path}')


def fetch(naid):
    os.makedirs(CACHE, exist_ok=True)
    rec_p, txt_p = os.path.join(CACHE, f'{naid}.rec.json'), os.path.join(CACHE, f'{naid}.txt.json')
    if not os.path.exists(rec_p):
        d = get(f'records/search?naId={naid}')
        rec = d['body']['hits']['hits'][0]['_source']['record']
        json.dump(rec, open(rec_p, 'w', encoding='utf-8'), ensure_ascii=False)
    if not os.path.exists(txt_p):
        objs, page = [], 1
        while True:
            d = get(f'extractedText/{naid}?limit=1000&page={page}')
            objs += d.get('digitalObjects') or []
            if len(objs) >= (d.get('total') or 0) or not d.get('digitalObjects'):
                break
            page += 1
        json.dump(objs, open(txt_p, 'w', encoding='utf-8'), ensure_ascii=False)
    return json.load(open(rec_p, encoding='utf-8')), json.load(open(txt_p, encoding='utf-8'))


NUM = re.compile(r'(?<![\d,./-])\d{2,4}(?![\d,./-])')
YEAR = re.compile(r'^1[6-9]\d\d$')


def frame_score(text):
    """Code-likeness of one frame: numeric groups that are not years, and the longest run of them."""
    toks = re.findall(r'\S+', text or '')
    nums = [t for t in toks if NUM.fullmatch(t.strip('.,;:)(')) and not YEAR.match(t.strip('.,;:)('))]
    run = best = 0
    for t in toks:
        if NUM.fullmatch(t.strip('.,;:)(')) and not YEAR.match(t.strip('.,;:)(')):
            run += 1
            best = max(best, run)
        elif len(t) > 2:
            run = 0
    words = sum(1 for t in toks if re.fullmatch(r'[A-Za-z]{3,}', t))
    return len(nums), best, words


def letter_score(text):
    """Code-word likeness: alphabetic tokens of exactly five letters (the post-1900 code-word and letter-cipher
    group), their share of all alphabetic tokens, and the longest unbroken run of them. Prose runs about 12-15%."""
    toks = re.findall(r'[A-Za-z]+', text or '')
    five = [len(t) == 5 for t in toks]
    run = best = 0
    for f in five:
        run = run + 1 if f else 0
        best = max(best, run)
    n5 = sum(five)
    return n5, (n5 / len(toks) if toks else 0.0), best


def frames(naid):
    rec, objs = fetch(naid)
    names = {o['objectId']: o['objectFilename'] for o in rec.get('digitalObjects') or []}
    for o in objs:
        n, run, words = frame_score(o.get('extractedText'))
        yield names.get(o['objectId'], o['objectId']), n, run, words, o.get('extractedText') or ''


def flagged(naid, min_nums=12, min_run=6):
    for name, n, run, words, text in frames(naid):
        if n >= min_nums and run >= min_run:
            yield name, n, run, words, text


if __name__ == '__main__':
    sys.stdout.reconfigure(encoding='utf-8')
    cmd, ids = sys.argv[1], sys.argv[2:]
    for naid in ids:
        if cmd == 'fetch':
            fetch(naid)
            print('cached', naid)
        elif cmd == 'score':
            for name, n, run, words, text in flagged(naid):
                print(f'{naid} {name} nums={n} run={run} words={words} | {" ".join(text.split())[:140]}')
