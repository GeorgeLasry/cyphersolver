"""Polite NARA catalog client for the Chicago sweep (4 s spacing; stop on 403; back off on 429/503)."""
import json, os, sys, time, urllib.parse, urllib.request, hashlib
HERE = os.path.dirname(os.path.abspath(__file__))
CACHE = os.path.join(HERE, 'cache')
BASE = 'https://catalog.archives.gov/proxy/'
UA = {'User-Agent': 'cyphersolver research (catalogue sweep; contact via github.com/dbourdeau/cyphersolver)',
      'Accept': 'application/json'}
PAUSE = 4.0
_last = [0.0]

class Blocked(Exception):
    pass

def get(path):
    os.makedirs(CACHE, exist_ok=True)
    cp = os.path.join(CACHE, hashlib.md5(path.encode()).hexdigest() + '.json')
    if os.path.exists(cp):
        return json.load(open(cp, encoding='utf-8'))
    for attempt in range(4):
        wait = _last[0] + PAUSE - time.time()
        if wait > 0:
            time.sleep(wait)
        _last[0] = time.time()
        try:
            with urllib.request.urlopen(urllib.request.Request(BASE + path, headers=UA), timeout=120) as r:
                body = r.read().decode('utf-8')
            if body.lstrip().startswith('{'):
                d = json.loads(body)
                json.dump(d, open(cp, 'w', encoding='utf-8'), ensure_ascii=False)
                return d
        except urllib.error.HTTPError as e:
            if e.code == 403:
                raise Blocked('403 ' + path)
            if e.code in (429, 500, 502, 503, 504):
                if e.code == 429:
                    raise Blocked('429 ' + path)
                time.sleep(20 * (attempt + 1)); continue
            raise
        except Blocked:
            raise
        except Exception as e:
            print('  err', e, file=sys.stderr)
        time.sleep(10 * (attempt + 1))
    return None

def search(**params):
    return get('records/search?' + urllib.parse.urlencode(params))
