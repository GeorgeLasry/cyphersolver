"""Batch b02 (fiesque1567): align each reading word by word with its key decode and list the words the figures do
not carry (unbracketed words whose letters mostly fall in alignment gaps or mismatches).

    python research/reading_audit/reread_b02_align.py [doc ...]

Prints, per document, the suspect words with their decode context. Words already in [...] are skipped.
"""
import json
import pathlib
import re
import sys
import unicodedata

ROOT = pathlib.Path(__file__).resolve().parents[2]
TH = 0.5
T = ROOT / 'targets' / 'fiesque1567'

CODES = {'QUEL/QUIL': 'quil', 'QUE': 'que', 'ET': 'et', 'VOUS': 'vous', 'LE ROY': 'leroy', "L'EMPEREUR": 'lempereur',
         'POUR': 'pour', 'FAIRE': 'faire', 'EST': 'est', 'TANT': 'tant', 'CE': 'ce', 'SAXE': 'saxe'}
GROUPS = ['sp', 'coqr', 'aoe', 'ul', 'bd', 'fcx', 'iy', 'uv', 'nh', 'mn', 'tf', 'ss', 'ij']


def conf(a, b):
    return any(a in g and b in g for g in GROUPS)


def strip_acc(s):
    return ''.join(c for c in unicodedata.normalize('NFD', s) if unicodedata.category(c) != 'Mn')


def decode_text(files):
    out = []
    for f in files:
        for ln in (T / f).read_text(encoding='utf8').splitlines():
            if ln.startswith('#') or not ln.strip():
                continue
            ln = re.sub(r'^c\w+\s', '', ln)
            for k, v in sorted(CODES.items(), key=lambda kv: -len(kv[0])):
                ln = ln.replace(k, v)
            out.append(re.sub(r'[^a-z]', '', strip_acc(ln.lower())))
    return ''.join(out)


def reading_words(path):
    s = path.read_text(encoding='utf8')
    s = re.sub(r'<!--.*?-->', '', s, flags=re.S)
    s = s.split('## Notes')[0].split('## Alignment notes')[0]
    s = '\n'.join(l for l in s.splitlines() if not l.startswith('#'))
    s = re.sub(r'⟨.*?⟩', ' ', s, flags=re.S)
    words = []
    for m in re.finditer(r'\[[^\]]*\]|[^\s\[\]]+', s):
        w = m.group(0)
        if w.startswith('['):
            words.append((w, None))
        else:
            words.append((w, re.sub(r'[^a-z]', '', strip_acc(w.lower()))))
    return words


def align(r, d):
    n, m = len(r), len(d)
    G = -1.5
    prev = [j * G for j in range(m + 1)]
    bt = [bytearray(m + 1)]
    for i in range(1, n + 1):
        cur = [i * G] + [0.0] * m
        b = bytearray(m + 1); b[0] = 1
        ri = r[i - 1]
        for j in range(1, m + 1):
            dj = d[j - 1]
            s = 2 if ri == dj else (1 if conf(ri, dj) else -1)
            x, y, z = prev[j - 1] + s, prev[j] + G, cur[j - 1] + G
            if x >= y and x >= z: cur[j] = x; b[j] = 0
            elif y >= z: cur[j] = y; b[j] = 1
            else: cur[j] = z; b[j] = 2
        prev = cur; bt.append(b)
    ok = [False] * n
    at = [None] * n
    i, j = n, m
    while i > 0 and j > 0:
        k = bt[i][j]
        if k == 0:
            ok[i - 1] = r[i - 1] == d[j - 1] or conf(r[i - 1], d[j - 1]); at[i - 1] = j - 1; i -= 1; j -= 1
        elif k == 1: at[i - 1] = j; i -= 1
        else: j -= 1
    return ok, at


def check(doc):
    p = json.loads((T / 'profile.json').read_text(encoding='utf8'))
    t = next(x for x in p['outcome']['texts'] if x['doc'] == doc)
    dec = [f for f in t['decryption'] if f.endswith('.txt') and 'decoded' in f]
    d = decode_text(dec)
    words = reading_words(T / 'read' / f'{doc}_reading.md')
    r = ''.join(w[1] for w in words if w[1])
    ok, at = align(r, d)
    pos, sus = 0, []
    for k, (w, norm) in enumerate(words):
        if not norm:
            continue
        frac = sum(ok[pos:pos + len(norm)]) / len(norm)
        if frac < TH:
            ctx = ' '.join(x[0] for x in words[max(0, k - 3):k + 4])
            js = [a for a in at[pos:pos + len(norm)] if a is not None] or [0]
            sus.append((w, round(frac, 2), ctx + '  || dec: ' + d[max(0, min(js) - 12):max(js) + 12]))
        pos += len(norm)
    return sus


if __name__ == '__main__':
    docs = sys.argv[1:]
    for doc in docs:
        s = check(doc)
        print(f'== {doc}: {len(s)} suspect')
        for w, f, c in s:
            print(f'  {w!r} {f}  | {c}')
