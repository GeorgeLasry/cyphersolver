"""Slice F: scan capital-letter runs in the NARA 'caps' hits (RG 109, 45, 107).

    python capscan.py hits  <caps.jsonl> [...]   # per hit: runs from the cached frame OCR (else the snippet), key-tested
    python capscan.py item  <naId> [...]         # every frame of a cached item: runs with ic < 0.055, key-tested

A run is >= 3 consecutive all-capital words (2+ letters, not a stop word). Each run of >= 15 letters gets its index of
coincidence and the best en-modern score under MANCHESTERBLUFF / COMPLETEVICTORY / COMERETRIBUTION (Vigenere, Beaufort,
variant, every offset; slice D's vig.py), plus the score of the run read as plain English, so that clear headings
(plain score high) separate from cipher (plain low, key low or high).
"""
import json, os, re, sys
sys.stdout.reconfigure(encoding='utf-8')
HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, os.path.join(HERE, '..', 'nara_triage_d'))
import vig
C = os.path.join(HERE, '..', 'nara_reels', 'cache')
STOP = {'WAR', 'RECORDS', 'COPIED', 'CSA', 'USA', 'OF', 'THE', 'AND', 'A', 'I', 'II', 'III', 'IV', 'NO', 'OK', 'TO',
        'CS', 'US'}


def runs(text):
    cur = []
    for t in re.findall(r"[A-Za-z][A-Za-z.,'-]*", text):
        w = re.sub(r'[^A-Za-z]', '', t)
        if len(w) >= 2 and w.isupper() and w not in STOP:
            cur.append(w)
        else:
            if len(cur) >= 3:
                yield cur
            cur = []
    if len(cur) >= 3:
        yield cur


def ic(s):
    n = len(s)
    if n < 2:
        return 0
    return sum(s.count(c) * (s.count(c) - 1) for c in set(s)) / (n * (n - 1))


def judge(words):
    ct = ''.join(words)
    plain = vig.M.per_char(ct.lower())
    _, best = vig.test(ct, top=1)
    s, k, m, off, p = best[0]
    return ct, ic(ct), plain, s, k, m, off, p


def show(tag, words):
    ct, i, plain, s, k, m, off, p = judge(words)
    flag = 'CIPHER?' if plain < -3.2 and i < 0.055 else ''
    print(f'{tag} len={len(ct)} ic={i:.3f} plain={plain:.2f} key={s:.2f} {k[:8]} {m} {off} {flag} | '
          f'{" ".join(words)[:80]} | {p[:40]}')
    return flag


def text_of(naid):
    p = f'{C}/{naid}.txt.json'
    if not os.path.exists(p):
        return None, None
    objs = json.load(open(p, encoding='utf-8'))
    rec = json.load(open(f'{C}/{naid}.rec.json', encoding='utf-8'))
    names = {o['objectId']: o['objectFilename'] for o in rec.get('digitalObjects') or []}
    return objs, names


if __name__ == '__main__':
    mode, args = sys.argv[1], sys.argv[2:]
    if mode == 'hits':
        for f in args:
            for line in open(f, encoding='utf-8'):
                d = json.loads(line)
                objs, _ = text_of(d['naId'])
                txt = d['snippet']
                if objs:
                    txt = next((o.get('extractedText') or '' for o in objs if str(o['objectId']) == str(d['objectId'])), txt)
                for r in runs(txt):
                    if len(''.join(r)) >= 15:
                        show(f'{d["naId"]} {d["file"]}', r)
    else:
        for naid in args:
            objs, names = text_of(naid)
            print(f'##### {naid} ({len(objs)} frames)')
            for o in sorted(objs, key=lambda o: names.get(o['objectId'], '')):
                for r in runs(o.get('extractedText') or ''):
                    ct = ''.join(r)
                    if len(ct) >= 15 and ic(ct) < 0.055:
                        show(names.get(o['objectId'], o['objectId']), r)
