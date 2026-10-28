"""Fill the detector gap on the 15 groups scanned before bulk_all.py existed (DONE_EARLIER): they were run for frame,
phrase, desc and (mostly) letters only. This reruns bulk_all.scan on their export files and keeps only the 'caps'
(capital-letter polyalphabetic) and 'word' hits, into out/<rg>_cw.jsonl with out/done_<rg>_cw.txt (a rerun resumes).

    python research/nara_reels/bulk_cw.py [--procs 16]
"""
import concurrent.futures as cf, json, os, sys

HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, HERE)
import bulk_scan as B  # noqa: E402
from bulk_all import DONE_EARLIER, scan  # noqa: E402


def one(key):
    for _ in range(4):
        try:
            return key, [h for h in scan(key) if h['kind'] in ('caps', 'word')], None
        except Exception as e:
            err = e
    return key, None, repr(err)


def main(procs):
    order = '11 360 393 457 76 65 107 45 109 84 165 38 59 242 94'.split()  # agency files first, mass series last
    for rg in [f'rg_{n}' for n in order if f'rg_{n}' in DONE_EARLIER]:
        out_p, done_p = os.path.join(B.OUT, f'{rg}_cw.jsonl'), os.path.join(B.OUT, f'done_{rg}_cw.txt')
        done = set(open(done_p).read().split()) if os.path.exists(done_p) else set()
        todo = [k for k in B.keys(rg.split('_', 1)[1]) if k not in done]
        with cf.ProcessPoolExecutor(procs) as ex:
            for key, hits, err in ex.map(one, todo):
                if err:
                    print(f'FAILED {key}: {err}', flush=True)
                    continue
                with open(out_p, 'a', encoding='utf-8') as fh:
                    fh.writelines(json.dumps(h, ensure_ascii=False) + '\n' for h in hits)
                with open(done_p, 'a') as fh:
                    fh.write(key + '\n')
        print(f'{rg}: {len(todo)} files scanned', flush=True)


if __name__ == '__main__':
    sys.stdout.reconfigure(encoding='utf-8')
    a = sys.argv[1:]
    main(int(a[a.index('--procs') + 1]) if '--procs' in a else 16)
