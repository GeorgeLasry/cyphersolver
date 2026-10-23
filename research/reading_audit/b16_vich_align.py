"""b16: word-by-word check of a vich1511 reading build (Lnn | text) against the decode of its transcription.

For each line, the reading's letters are aligned (difflib, after normalising u/v, i/j/y, c/ç/z, h, doubled letters)
with the decode's letters (code values included, unread [groups] dropped). Each unbracketed reading word gets the
share of its letters that the alignment carries; words under 0.6 are listed as NOT CARRIED (they must be bracketed or
corrected). [?w] words are reported separately; [w] (supplied) and [..] are skipped. Writes a tsv when asked.
python b16_vich_align.py <build.txt> <transcription> [align.tsv]"""
import sys, re, unicodedata, pathlib
sys.path.insert(0, str(pathlib.Path(__file__).resolve().parent))
from b16_vich_dec import compact

def norm(s):
    s = unicodedata.normalize('NFD', s.lower()); s = ''.join(c for c in s if not unicodedata.combining(c))
    s = s.replace('ç', 'z').translate(str.maketrans('vjyç', 'uiiz')).replace('h', '')
    s = re.sub(r'[^a-z]', '', s)
    return s

EXPAND = {'nro': 'nuestro', 'vras': 'vuestras', 'vro': 'vuestro', 'vra': 'vuestra'}

def nw_align(a, b):
    """Global edit-distance alignment; returns, for each char of a, 1 if aligned to an equal char of b."""
    n, m = len(a), len(b)
    D = [[0] * (m + 1) for _ in range(n + 1)]
    for i in range(n + 1): D[i][0] = i
    for j in range(m + 1): D[0][j] = j
    for i in range(1, n + 1):
        for j in range(1, m + 1):
            D[i][j] = min(D[i-1][j] + 1, D[i][j-1] + 1, D[i-1][j-1] + (a[i-1] != b[j-1]))
    got, i, j = [0] * n, n, m
    while i > 0 and j > 0:
        if D[i][j] == D[i-1][j-1] + (a[i-1] != b[j-1]):
            got[i-1] = int(a[i-1] == b[j-1]); i -= 1; j -= 1
        elif D[i][j] == D[i-1][j] + 1: i -= 1
        else: j -= 1
    return got

def main(build, trans, out=None):
    dec = {}
    for line in open(trans, encoding='utf-8'):
        if line.startswith('L') and ':' in line:
            tag, body = line.split(':', 1); dec[tag] = compact(body.split())
    rows, bad, doubt, n = [], [], [], 0
    for line in open(build, encoding='utf-8'):
        if not line.startswith('L'): continue
        tag, text = [x.strip() for x in line.split('|', 1)]
        raw = re.sub(r'\[[^\]]*\]', '', dec[tag])
        for k, v in EXPAND.items(): raw = raw.replace(k.upper(), v)
        d = norm(raw)
        words = re.findall(r'\[\?[^\]]*\]|\[[^\]]*\]|[^\s\[\]]+', text)
        seq, owner = '', []
        for wi, w in enumerate(words):
            if w.startswith('[') and not w.startswith('[?'): continue
            nw = norm(w.strip('[?]'))
            seq += nw; owner += [wi] * len(nw)
        got = nw_align(seq, d)
        for wi, w in enumerate(words):
            ks = [k for k, o in enumerate(owner) if o == wi]
            if not ks: continue
            share = sum(got[k] for k in ks) / len(ks)
            n += not w.startswith('[?')
            rows.append((tag, w, round(share, 2)))
            if w.startswith('[?'): doubt.append((tag, w, share))
            elif share < 0.6: bad.append((tag, w, share))
    if out:
        with open(out, 'w', encoding='utf-8') as f:
            f.write('line\tword\tcarried_share\n'); f.writelines(f'{a}\t{b}\t{c}\n' for a, b, c in rows)
    sys.stdout.reconfigure(encoding='utf-8')
    print(f'{n} unbracketed words; {len(bad)} not carried (<0.6); {len(doubt)} [?] words')
    for t, w, s in bad: print('NOT CARRIED', t, w, round(s, 2))
    for t, w, s in doubt: print('doubt', t, w, round(s, 2))

if __name__ == '__main__':
    main(*sys.argv[1:4])
