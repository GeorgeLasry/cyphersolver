"""Stream out/rg_109.jsonl, drop compiled service records, keep the rest (slice109.jsonl) and count kinds/series."""
import json, collections, sys
SRC = '../nara_reels/out/rg_109.jsonl'
skip = ('Carded Records Showing Military Service', 'Compiled Military Service Record', 'Compiled Service Record')
cnt = collections.Counter(); kept = collections.Counter()
with open(SRC, encoding='utf-8') as f, open('slice109.jsonl', 'w', encoding='utf-8') as out:
    for line in f:
        try: r = json.loads(line)
        except Exception: cnt['bad'] += 1; continue
        anc = ' > '.join(r.get('ancestors', []))
        cnt[r['kind']] += 1
        if any(s in anc or s in r.get('title', '') for s in skip):
            cnt['skip_csr_' + r['kind']] += 1; continue
        kept[(r['kind'], ' > '.join(r.get('ancestors', [])[1:3])[:140])] += 1
        out.write(line)
for k, v in sorted(cnt.items()): print(k, v)
for k, v in kept.most_common(): print(v, k)
