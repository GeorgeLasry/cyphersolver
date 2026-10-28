"""neg.py: slice L, word hits from the caps/word rerun of the early groups (out/<rg>_cw.jsonl) whose context says the
text was not read: one line per item, every distinct context."""
import json, os, re, sys, glob, collections
OUT = os.path.join(os.path.dirname(__file__), '..', 'nara_reels', 'out')
NEG = re.compile(r'undeciph|undecyph|not (been |yet )?(be )?deciph|not (been |yet )?decyph|unable to (de|read)|could not (be )?(de|read)'
                 r'|cannot (be )?(de|read)|no key|unsolved|key .{0,25}(lost|missing|not)|not .{0,12}solved|indecipherable'
                 r'|cryptogram|secret writing|invisible ink|secret ink|sympathetic ink', re.I)
BOILER = re.compile(r'errors .{0,3}cipher|CLASSES OF SERVICE|cipher machine|cipher device|crypto ?aid|SIGABA|M-209|converter m', re.I)
by = collections.defaultdict(list)
for f in sorted(glob.glob(os.path.join(OUT, 'rg_*_cw.jsonl'))):
    for l in open(f, encoding='utf-8'):
        d = json.loads(l)
        if d['kind'] != 'word': continue
        s = re.sub(r'\s+', ' ', d['snippet'])
        m = NEG.search(s)
        if not m or BOILER.search(s): continue
        d['rg'] = os.path.basename(f)[:-9]; d['ctx'] = s[max(0, m.start() - 170):m.end() + 130]; by[d['naId']].append(d)
print(len(by), 'items')
for nid, v in sorted(by.items(), key=lambda x: (x[1][0]['rg'], -len(x[1]))):
    d = v[0]
    print(f"== {d['rg']} {nid} x{len(v)} | {d['title'][:70]} | {' '.join(d.get('microform') or [])} | {' > '.join(d.get('ancestors') or [])[-70:]}")
    seen = set()
    for e in v:
        k = e['ctx'][:60]
        if k in seen: continue
        seen.add(k)
        if len(seen) > 4: break
        print('   ', e['file'], '|', e['ctx'])
