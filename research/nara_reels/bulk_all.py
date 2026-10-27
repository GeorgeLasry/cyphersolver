"""One combined pass over every record group not yet scanned: all detectors at once, in parallel processes.

    python research/nara_reels/bulk_all.py [--procs 16] [--only rg_226,rg_87]

Runs the detectors of bulk_scan.py together on each export file (numeric code 'frame', 'phrase', 'desc', five-letter
'letters', capital-letter polyalphabetic 'caps', cipher 'word'), skipping personnel series (SKIP_SERIES), and writes
out/<rg>_all.jsonl with a done list out/done_<rg>_all.txt (a rerun resumes). Order: smallest record groups first, the
mass series last (Census, draft registration, pensions, civil service, WPA, NARA's own RG 64), since cipher is far
likelier in agency files than in those.
"""
import concurrent.futures as cf, json, os, sys, urllib.request

HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, HERE)
import bulk_scan as B  # noqa: E402
from reels import caps_score, frame_score, letter_score  # noqa: E402

DONE_EARLIER = {f'rg_{r}' for r in '59 84 45 38 165 107 393 76 11 457 65 360 109 242 94'.split()}
LAST = ['rg_69', 'rg_15', 'rg_146', 'rg_147', 'rg_24', 'rg_29', 'rg_64']


def scan(key):
    hits = []
    with urllib.request.urlopen(urllib.request.Request(B.BUCKET + key), timeout=900) as fh:
        for raw in fh:
            try:
                d = json.loads(raw)
            except ValueError:
                continue
            r = d.get('record', d)
            if any(s in a for a in (x.get('title', '') for x in r.get('ancestors') or []) for s in B.SKIP_SERIES):
                continue
            text = ' '.join(str(r.get(k) or '') for k in ('title', 'scopeAndContentNote', 'generalNotes'))
            if B.DESC.search(text):
                hits.append(dict(kind='desc', **B.context(r), snippet=text[:600]))
            for o in r.get('digitalObjects') or []:
                t = o.get('extractedText') or ''
                if not t:
                    continue
                base = dict(**B.context(r), file=o.get('objectFilename'), objectId=o.get('objectId'))
                n, run, words = frame_score(t)
                if n >= 12 and run >= 6:
                    hits.append(dict(kind='frame', **base, nums=n, run=run, words=words, snippet=' '.join(t.split())[:400]))
                n5, share, run5 = letter_score(t)
                if n5 >= 25 and share >= 0.35 and run5 >= 8:
                    hits.append(dict(kind='letters', **base, n5=n5, share=round(share, 2), run=run5,
                                     snippet=' '.join(t.split())[:400]))
                nc, cshare, runc, nl, ic = caps_score(t)
                if nc >= 15 and runc >= 6 and nl >= 80 and ic < 0.055:
                    hits.append(dict(kind='caps', **base, ncaps=nc, run=runc, ic=round(ic, 4),
                                     snippet=' '.join(t.split())[:400]))
                for kind, rx in (('phrase', B.PHRASE), ('word', B.WORD)):
                    m = rx.search(t)
                    if m:
                        a = max(0, m.start() - 250)
                        hits.append(dict(kind=kind, **base, match=m.group(0),
                                         snippet=' '.join(t[a:m.end() + 250].split())))
    return hits


def one(key):
    for attempt in range(4):
        try:
            return key, scan(key), None
        except Exception as e:  # network hiccup: retry the whole file
            err = e
    return key, None, repr(err)


def main(procs, only):
    sizes = {p: s for p, n, s in json.load(open(os.path.join(B.OUT, 'rg_sizes.json')))}
    rgs = only or sorted((p for p in sizes if p not in DONE_EARLIER), key=lambda p: (p in LAST, LAST.index(p) if p in LAST else 0, sizes[p]))
    for rg in rgs:
        out_p, done_p = os.path.join(B.OUT, f'{rg}_all.jsonl'), os.path.join(B.OUT, f'done_{rg}_all.txt')
        done = set(open(done_p).read().split()) if os.path.exists(done_p) else set()
        num = rg.split('_', 1)[1] if rg.startswith('rg_') else None
        try:
            keys = B.keys(num) if num else []
        except Exception as e:
            print(f'{rg}: listing failed {e!r}', flush=True)
            continue
        todo = [k for k in keys if k not in done]
        if not todo:
            continue
        with cf.ProcessPoolExecutor(procs) as ex:
            for key, hits, err in ex.map(one, todo):
                if err:
                    print(f'FAILED {key}: {err}', flush=True)
                    continue
                with open(out_p, 'a', encoding='utf-8') as fh:
                    for h in hits:
                        fh.write(json.dumps(h, ensure_ascii=False) + '\n')
                with open(done_p, 'a') as fh:
                    fh.write(key + '\n')
        print(f'{rg}: {len(todo)} files scanned', flush=True)


if __name__ == '__main__':
    sys.stdout.reconfigure(encoding='utf-8')
    a = sys.argv[1:]
    procs = int(a[a.index('--procs') + 1]) if '--procs' in a else 16
    only = a[a.index('--only') + 1].split(',') if '--only' in a else None
    main(procs, only)
