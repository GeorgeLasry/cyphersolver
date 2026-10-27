"""Scan NARA's open-data catalogue export (AWS, s3://nara-national-archives-catalog) for cipher material.

    python research/nara_reels/bulk_scan.py <record group> [<record group> ...] [--workers 4]

Each record group is published as up to 400 JSONL files (descriptions/record-groups/rg_<n>/rg_<n>-<k>.jsonl) whose
records carry every digital object's OCR text (digitalObjects[].extractedText). The files are streamed, never stored
(the disk is nearly full), and only hits are kept, in out/rg_<n>.jsonl:

- kind "frame": a frame whose OCR looks like numeric code (frame_score in reels.py: many 2-4 digit groups that are
  not years, with a long unbroken run), with the item's title, ancestors and microfilm publication;
- kind "phrase": a frame whose OCR has a rare cipher phrase (undeciphered, not deciphered, in cipher ...);
- kind "desc": a description (title, scope note, general notes) that names cipher or code.

The bucket is AWS Open Data, meant for bulk download; no catalogue API call is made, so nothing here can trip the
catalogue's rate limit or bot check. Finished files are listed in out/done_rg_<n>.txt so a rerun resumes.
"""
import concurrent.futures as cf, json, os, re, sys, threading, urllib.request

HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, HERE)
from reels import frame_score, letter_score  # noqa: E402

LETTERS = False  # --letters: a second pass that flags only five-letter code-word / letter-cipher frames

OUT = os.path.join(HERE, 'out')
BUCKET = 'https://nara-national-archives-catalog.s3.amazonaws.com/'
DESC = re.compile(r'\b(cipher|ciphers|ciphered|cypher|cyphers|cyphered|decipher\w*|decypher\w*|cryptogra\w*|'
                  r'cryptogram\w*|code (?:book|message|telegram|key)s?|in code|coded|secret writing|invisible ink|'
                  r'nomenclator|chiffr\w*|geheimschrift|cifra\w*)\b', re.I)
PHRASE = re.compile(r'\b(undeciphered|undecyphered|not (?:been )?decipher\w*|not (?:been )?decypher\w*|'
                    r'not (?:been )?decoded|could not (?:be )?(?:decipher|decode)\w*|in cipher|in cypher|'
                    r'key (?:is |was )?(?:lost|not found|missing))\b', re.I)
lock = threading.Lock()


def keys(rg):
    out, token = [], None
    while True:
        url = f'{BUCKET}?list-type=2&max-keys=1000&prefix=descriptions/record-groups/rg_{rg}/'
        if token:
            url += '&continuation-token=' + urllib.request.quote(token, safe='')
        x = urllib.request.urlopen(url, timeout=120).read().decode()
        out += re.findall(r'<Key>([^<]+\.jsonl)</Key>', x)
        m = re.search(r'<NextContinuationToken>([^<]+)</NextContinuationToken>', x)
        if not m:
            return out
        token = m.group(1)


def context(r):
    anc = [a.get('title', '') for a in r.get('ancestors') or []]
    mf = [m.get('identifier') for m in r.get('microformPublications') or []]
    d = r.get('productionDates') or r.get('inclusiveDates') or ''
    return {'naId': r.get('naId'), 'title': r.get('title'), 'level': r.get('levelOfDescription'),
            'ancestors': anc, 'microform': mf, 'dates': d}


def scan_file(rg, key):
    hits = []
    req = urllib.request.Request(BUCKET + key)
    with urllib.request.urlopen(req, timeout=600) as fh:
        for raw in fh:
            try:
                d = json.loads(raw)
            except ValueError:
                continue
            r = d.get('record', d)
            if LETTERS:
                for o in r.get('digitalObjects') or []:
                    t = o.get('extractedText') or ''
                    n5, share, run5 = letter_score(t)
                    if n5 >= 25 and share >= 0.35 and run5 >= 8:  # 1 flag in 37,150 cached frames, the true one
                        hits.append(dict(kind='letters', **context(r), file=o.get('objectFilename'),
                                         objectId=o.get('objectId'), n5=n5, share=round(share, 2), run=run5,
                                         snippet=' '.join(t.split())[:400]))
                continue
            text = ' '.join(str(r.get(k) or '') for k in ('title', 'scopeAndContentNote', 'generalNotes'))
            if DESC.search(text):
                hits.append(dict(kind='desc', **context(r), snippet=text[:600]))
            for o in r.get('digitalObjects') or []:
                t = o.get('extractedText') or ''
                if not t:
                    continue
                n, run, words = frame_score(t)
                if n >= 12 and run >= 6:
                    hits.append(dict(kind='frame', **context(r), file=o.get('objectFilename'), objectId=o.get('objectId'),
                                     nums=n, run=run, words=words, snippet=' '.join(t.split())[:400]))
                m = PHRASE.search(t)
                if m:
                    a = max(0, m.start() - 200)
                    hits.append(dict(kind='phrase', **context(r), file=o.get('objectFilename'), objectId=o.get('objectId'),
                                     phrase=m.group(0), snippet=' '.join(t[a:m.end() + 200].split())))
    return hits


def run(rg, workers):
    os.makedirs(OUT, exist_ok=True)
    tag = f'rg_{rg}_letters' if LETTERS else f'rg_{rg}'
    out_p, done_p = os.path.join(OUT, f'{tag}.jsonl'), os.path.join(OUT, f'done_{tag}.txt')
    done = set(open(done_p).read().split()) if os.path.exists(done_p) else set()
    todo = [k for k in keys(rg) if k not in done]
    print(f'rg {rg}: {len(todo)} files to scan', flush=True)

    def one(k):
        for attempt in range(4):
            try:
                hits = scan_file(rg, k)
                break
            except Exception as e:  # network hiccup: retry the whole file
                err = e
        else:
            print(f'FAILED {k}: {err}', flush=True)
            return
        with lock:
            with open(out_p, 'a', encoding='utf-8') as fh:
                for h in hits:
                    fh.write(json.dumps(h, ensure_ascii=False) + '\n')
            with open(done_p, 'a') as fh:
                fh.write(k + '\n')
        print(f'{k}: {len(hits)} hits', flush=True)

    with cf.ThreadPoolExecutor(workers) as ex:
        list(ex.map(one, todo))


if __name__ == '__main__':
    sys.stdout.reconfigure(encoding='utf-8')
    args = sys.argv[1:]
    workers = 4
    if '--letters' in args:
        LETTERS = True
        args.remove('--letters')
    if '--workers' in args:
        i = args.index('--workers'); workers = int(args[i + 1]); del args[i:i + 2]
    for rg in args:
        run(rg, workers)
