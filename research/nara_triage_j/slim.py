"""slim.py <rg>: stream out/<rg>_all.jsonl (GB-size) into out/<rg>_slim.jsonl: every non-frame hit, plus for frames
only the top frame (most nums, fewest words) of each of the 60 items with most solid frames. Lets review_i.py run."""
import json, os, sys, collections
OUT = os.path.join(os.path.dirname(__file__), '..', 'nara_reels', 'out')
rg = sys.argv[1]
keep, solid, best = [], collections.Counter(), {}
for line in open(os.path.join(OUT, f'{rg}_all.jsonl'), encoding='utf-8'):
    if '"kind": "frame"' not in line and '"kind":"frame"' not in line:
        keep.append(line); continue
    d = json.loads(line)
    if d.get('words', 0) < d.get('nums', 0):
        k = d['naId']; solid[k] += 1
        sc = d.get('nums', 0) - d.get('words', 0)
        if k not in best or sc > best[k][0]:
            best[k] = (sc, line)
top = [k for k, _ in solid.most_common(60)]
with open(os.path.join(OUT, f'{rg}_slim.jsonl'), 'w', encoding='utf-8') as fh:
    fh.writelines(keep)
    for k in top:
        fh.write(best[k][1])
with open(os.path.join(OUT, f'{rg}_slim_items.tsv'), 'w', encoding='utf-8') as fh:
    for k, n in solid.most_common():
        d = json.loads(best[k][1]); fh.write(f"{k}\t{n}\t{d['title'][:80]}\t{' > '.join(d.get('ancestors') or [])[-100:]}\n")
print(rg, 'kept', len(keep), 'solid items', len(solid))
