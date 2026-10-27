"""Harvest the Decoding the Civil War transcriptions from the Huntington Digital Library.

Every page of the Thomas T. Eckert Papers (CONTENTdm collection p16003coll11) carries the
volunteers' transcription in its `transc` field. This writes one JSONL file per item to
data/items/<pointer>.jsonl: {item, callid, title, pageptr, pagetitle, transc}.

    python harvest.py            # all items, skips files already complete
    python harvest.py 5126 6796  # only these items
"""
import json, os, sys, time, urllib.request

BASE = 'https://hdl.huntington.org/digital/bl/dmwebservices/index.php?q='
COLL = 'p16003coll11'
HERE = os.path.dirname(os.path.abspath(__file__))
OUT = os.path.join(HERE, 'data', 'items')


def get(q, tries=4):
    for k in range(tries):
        try:
            with urllib.request.urlopen(BASE + q, timeout=60) as r:
                return json.loads(r.read().decode('utf8'))
        except Exception as e:
            if k == tries - 1:
                raise
            time.sleep(3 * (k + 1))


def text(v):
    return v if isinstance(v, str) else ''


def items():
    d = get(f'dmQuery/{COLL}/0/title!date/title/1024/1/0/0/0/0/json')
    return [r['pointer'] for r in d['records']]


def harvest(ptr):
    path = os.path.join(OUT, f'{ptr}.jsonl')
    if os.path.exists(path):
        return
    info = get(f'dmGetItemInfo/{COLL}/{ptr}/json')
    pages = get(f'dmGetCompoundObjectInfo/{COLL}/{ptr}/json').get('page', [])
    if isinstance(pages, dict):
        pages = [pages]
    rows = []
    for p in pages:
        pi = get(f"dmGetItemInfo/{COLL}/{p['pageptr']}/json")
        rows.append(dict(item=ptr, callid=text(info.get('callid')), title=text(info.get('title')),
                         pageptr=p['pageptr'], pagetitle=p['pagetitle'], transc=text(pi.get('transc'))))
        time.sleep(0.15)
    tmp = path + '.part'
    with open(tmp, 'w', encoding='utf8') as f:
        for r in rows:
            f.write(json.dumps(r, ensure_ascii=False) + '\n')
    os.replace(tmp, path)
    n = sum(1 for r in rows if r['transc'].strip())
    print(ptr, text(info.get('callid')), len(rows), 'pages,', n, 'transcribed', flush=True)


if __name__ == '__main__':
    os.makedirs(OUT, exist_ok=True)
    for ptr in (sys.argv[1:] or items()):
        harvest(ptr)
