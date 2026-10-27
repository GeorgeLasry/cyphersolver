"""Drop duplicate and malformed lines from the bulk-scan output (two scan processes once ran on the same files).

    python research/nara_reels/dedupe.py

Every out/*.jsonl keeps the first copy of each identical hit and drops lines that do not parse; every out/done_*.txt
keeps each file name once. Run it only when no bulk_scan.py process is writing.
"""
import glob, json, os

HERE = os.path.dirname(os.path.abspath(__file__))
for p in sorted(glob.glob(os.path.join(HERE, 'out', '*.jsonl'))):
    seen, keep, bad = set(), [], 0
    for line in open(p, encoding='utf-8', errors='replace'):
        try:
            h = json.loads(line)
        except ValueError:
            bad += 1
            continue
        k = (h.get('kind'), h.get('naId'), h.get('objectId'), h.get('file'), h.get('snippet', '')[:80])
        if k not in seen:
            seen.add(k)
            keep.append(line if line.endswith('\n') else line + '\n')
    total = len(keep) + bad + (sum(1 for _ in open(p, encoding='utf-8', errors='replace')) - len(keep) - bad)
    open(p, 'w', encoding='utf-8').writelines(keep)
    print(f'{os.path.basename(p)}: kept {len(keep)}, dropped {total - len(keep)} ({bad} malformed)')
for p in sorted(glob.glob(os.path.join(HERE, 'out', 'done_*.txt'))):
    names = list(dict.fromkeys(l.strip() for l in open(p) if l.strip()))
    open(p, 'w').write('\n'.join(names) + '\n')
