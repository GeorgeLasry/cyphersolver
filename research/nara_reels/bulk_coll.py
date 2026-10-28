"""bulk_all.py's detectors over the export's second prefix, descriptions/collections/ (5,192 donated and presidential
collections, ~216k files, ~28 GB), plus record-groups/coll_Wattenberg, which the record-group pass missed.

    python research/nara_reels/bulk_coll.py [--procs 16]

Writes out/collections_all.jsonl (each hit tagged with its collection) and out/done_collections_all.txt (a rerun resumes).
The files come from the AWS Open Data bucket, not from catalog.archives.gov, so NARA's rate limit is not involved."""
import concurrent.futures as cf, json, os, re, sys, urllib.parse, urllib.request

HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, HERE)
import bulk_scan as B  # noqa: E402
from bulk_all import one  # noqa: E402


def list_keys(prefix):
    out, tok = [], None
    while True:
        u = f'{B.BUCKET}?list-type=2&max-keys=1000&prefix={urllib.parse.quote(prefix)}' + (
            f'&continuation-token={urllib.parse.quote(tok)}' if tok else '')
        x = urllib.request.urlopen(u, timeout=120).read().decode()
        out += [k for k in re.findall(r'<Key>([^<]+)</Key>', x) if k.endswith('.jsonl')]
        m = re.search(r'<NextContinuationToken>([^<]+)<', x)
        if not m:
            return out
        tok = m.group(1)


def main(procs):
    out_p, done_p = os.path.join(B.OUT, 'collections_all.jsonl'), os.path.join(B.OUT, 'done_collections_all.txt')
    done = set(open(done_p, encoding='utf-8').read().splitlines()) if os.path.exists(done_p) else set()
    keys = list_keys('descriptions/collections/') + list_keys('descriptions/record-groups/coll_')
    todo = [urllib.parse.quote(k, safe='/') for k in keys if k not in done]
    print(f'{len(keys)} files, {len(todo)} to scan', flush=True)
    n = 0
    with cf.ProcessPoolExecutor(procs) as ex:
        for key, hits, err in ex.map(one, todo, chunksize=8):
            key = urllib.parse.unquote(key)
            if err:
                print(f'FAILED {key}: {err}', flush=True)
                continue
            coll = key.split('/')[2]
            with open(out_p, 'a', encoding='utf-8') as fh:
                for h in hits:
                    fh.write(json.dumps(dict(h, coll=coll), ensure_ascii=False) + '\n')
            with open(done_p, 'a', encoding='utf-8') as fh:
                fh.write(key + '\n')
            n += 1
            if n % 5000 == 0:
                print(f'{n} files scanned', flush=True)
    print(f'collections: {n} files scanned', flush=True)


if __name__ == '__main__':
    sys.stdout.reconfigure(encoding='utf-8')
    a = sys.argv[1:]
    main(int(a[a.index('--procs') + 1]) if '--procs' in a else 16)
