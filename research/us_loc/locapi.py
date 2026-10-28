"""Polite loc.gov JSON fetcher with an on-disk cache (Oct 2026 LoC sweep).

At most one request every 3.2 s, descriptive User-Agent, stops on 429/403 (never retries a 403).
Cache: research/us_loc/raw/<sha1>.json (git-ignore it; regenerable).
"""
import hashlib, http.client, json, os, sys, time, urllib.request, urllib.error

HERE = os.path.dirname(os.path.abspath(__file__))
RAW = os.path.join(HERE, 'raw')
os.makedirs(RAW, exist_ok=True)
UA = 'cyphersolver research (catalogue sweep)'
_last = [0.0]
GAP = float(os.environ.get('LOC_GAP', '3.2'))


class Blocked(Exception):
    pass


def get(url, cache=True):
    key = hashlib.sha1(url.encode()).hexdigest()
    p = os.path.join(RAW, key + '.json')
    if cache and os.path.exists(p):
        with open(p, encoding='utf-8') as fh:
            return json.load(fh)
    wait = GAP - (time.time() - _last[0])
    if wait > 0:
        time.sleep(wait)
    req = urllib.request.Request(url, headers={'User-Agent': UA, 'Accept': 'application/json'})
    for attempt in range(5):
        _last[0] = time.time()
        try:
            with urllib.request.urlopen(req, timeout=60) as r:
                data = json.loads(r.read().decode('utf-8'))
            break
        except urllib.error.HTTPError as e:
            if e.code == 403:
                raise Blocked(f'403 on {url}')
            if e.code == 429:
                print('429, backing off 120 s', file=sys.stderr)
                time.sleep(120)
                continue
            if 500 <= e.code < 600:
                time.sleep(20)
                continue
            if e.code == 404:
                return None
            raise
        except (urllib.error.URLError, TimeoutError, http.client.IncompleteRead, ConnectionError, json.JSONDecodeError) as e:
            print('retry', type(e).__name__, url, file=sys.stderr)
            time.sleep(20)
            continue
    else:
        raise Blocked(f'gave up on {url}')
    with open(p, 'w', encoding='utf-8') as fh:
        json.dump(data, fh)
    return data
