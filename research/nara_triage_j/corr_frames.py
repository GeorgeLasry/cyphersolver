"""corr_frames.py: stream out/rg_64_all.jsonl and keep, for correspondence series only (State decimal files, Russian
consulates, Naval Records, territorial/political papers), the frames that look like code: >= 25 number groups, a run of
>= 12, words < nums/3. Writes out/rg_64_corr.tsv: item naId, series, title, n code frames, sample frame + snippet."""
import json, os, re, collections
OUT = os.path.join(os.path.dirname(__file__), '..', 'nara_reels', 'out')
CORR = re.compile(r'Department of State|Imperial Russian|Naval Records|Political Relations|Territorial Papers|Consul', re.I)
hits, info = collections.Counter(), {}
for line in open(os.path.join(OUT, 'rg_64_all.jsonl'), encoding='utf-8'):
    if '"frame"' not in line: continue
    d = json.loads(line)
    if d.get('kind') != 'frame': continue
    anc = ' > '.join(d.get('ancestors') or [])
    if not CORR.search(anc): continue
    n, w, r = d.get('nums', 0), d.get('words', 0), d.get('run', 0)
    if n >= 25 and r >= 12 and w * 3 < n:
        k = d['naId']; hits[k] += 1
        if k not in info or n > info[k][0]:
            info[k] = (n, anc.split(' > ')[-1][:60], d['title'][:70], d.get('file'), re.sub(r'\s+', ' ', d.get('snippet', ''))[:220])
with open(os.path.join(OUT, 'rg_64_corr.tsv'), 'w', encoding='utf-8') as fh:
    for k, c in hits.most_common():
        n, s, t, f, sn = info[k]; fh.write(f'{k}\t{c}\t{s}\t{t}\t{f}\t{sn}\n')
print('items', len(hits), 'frames', sum(hits.values()))
