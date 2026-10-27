"""Find runs of capital-letter cipher words in cached OCR of RG 109 letter/telegram books and test each run against the
three Confederate keys (every offset, Vigenere/Beaufort/variant), printing the best en-modern score.
    python capruns.py <naId> [...]
"""
import json, os, re, sys
sys.stdout.reconfigure(encoding='utf-8')
HERE = os.path.dirname(os.path.abspath(__file__)); sys.path.insert(0, HERE)
import vig
C = os.path.join(HERE, '..', 'nara_reels', 'cache')
STOP = {'WAR', 'RECORDS', 'COPIED', 'CSA', 'USA', 'OF', 'THE', 'AND', 'A', 'I', 'II', 'III', 'IV', 'NO', 'OK', 'TO', 'CS', 'US'}
def runs(text):
    toks = re.findall(r"[A-Za-z][A-Za-z.,'-]*", text)
    cur = []
    for t in toks:
        w = re.sub(r'[^A-Za-z]', '', t)
        if len(w) >= 2 and w.isupper() and w not in STOP: cur.append(w)
        else:
            if len(cur) >= 3: yield cur
            cur = []
    if len(cur) >= 3: yield cur
for naid in sys.argv[1:]:
    rec = json.load(open(f'{C}/{naid}.rec.json', encoding='utf-8')); objs = json.load(open(f'{C}/{naid}.txt.json', encoding='utf-8'))
    names = {o['objectId']: o['objectFilename'] for o in rec.get('digitalObjects') or []}
    print(f'##### {naid} {rec.get("title")} ({len(objs)} frames)')
    for o in sorted(objs, key=lambda o: names.get(o['objectId'], '')):
        for r in runs(o.get('extractedText') or ''):
            ct = ''.join(r)
            if len(ct) < 12: continue
            _, best = vig.test(ct, top=1)
            s, k, m, off, p = best[0]
            print(f'{names.get(o["objectId"])} len={len(ct)} best={s:.2f} {k[:8]} {m} {off} | {" ".join(r)[:90]} | {p[:50]}')
