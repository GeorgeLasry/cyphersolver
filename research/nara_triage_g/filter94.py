"""Stream rg_94.jsonl, drop service/pension/medical card records by ancestor title, write the rest to slice94.jsonl
(regenerable, git-ignore) and print counts per series."""
import json, re, collections, sys, os
sys.stdout.reconfigure(encoding='utf-8')
HERE = os.path.dirname(os.path.abspath(__file__))
DROP = re.compile(r'carded record|compiled (military )?service|service record|military service of|pension|muster roll|'
                  r'medical|hospital|enlistment|returns from|register of enlistments|burial|headstone|draft|'
                  r'index to|personal papers of|bounty|claims? for|casualt', re.I)
kept, dropped, bad = collections.Counter(), collections.Counter(), 0
with open(os.path.join(HERE, 'slice94.jsonl'), 'w', encoding='utf-8') as out:
    for line in open(os.path.join(HERE, '..', 'nara_reels', 'out', 'rg_94.jsonl'), encoding='utf-8'):
        try:
            h = json.loads(line)
        except Exception:
            bad += 1; continue
        anc = ' > '.join(h['ancestors'][1:]) + ' > ' + (h.get('title') or '')
        key = (','.join(h['microform']) or '-') + ' | ' + ' > '.join(h['ancestors'][1:2])[:90]
        if DROP.search(' > '.join(h['ancestors'][1:])) and h['kind'] == 'frame':
            dropped[key] += 1; continue
        kept[(h['kind'], key)] += 1
        out.write(line)
print('bad lines', bad, 'dropped', sum(dropped.values()), 'kept', sum(kept.values()))
for k, v in kept.most_common(80): print(v, k)
print('--- dropped series (top)')
for k, v in dropped.most_common(25): print(v, k)
