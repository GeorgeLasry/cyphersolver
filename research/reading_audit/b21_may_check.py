"""b21: word-by-word check of a mayenne1586c2 reading against its letter decode.

    python -X utf8 research/reading_audit/b21_may_check.py <reading.md> <decoded_1.txt> [<decoded_2.txt> ...]

The decode files are the contributors' line decodes (upper-case runs are code words, (a|b) two-valued signs, [?] a
sign with no value). Both sides are reduced to letters (lower case, j=i, v=u, y=i, accents off; a two-valued sign
keeps its first value and is matched as either). The reading body (## Reading) is aligned to the decode letters by
difflib; for every word of the reading the share of its letters matched in the decode is printed when below 1, and
words in [plain brackets] (supplied) are reported separately. A reading word with no matched letter that is not in
[brackets] is an invented word.
"""
import difflib, re, sys, unicodedata
from pathlib import Path


def base(s):
    s = unicodedata.normalize('NFD', s.lower())
    s = ''.join(c for c in s if not unicodedata.combining(c))
    return s.replace('j', 'i').replace('v', 'u').replace('y', 'i')


def dec_letters(files):
    out = []
    for f in files:
        for ln in Path(f).read_text(encoding='utf-8').splitlines():
            if ln.startswith('#') or not ln.strip(): continue
            ln = re.sub(r'^[cv]?\d+\s', '', ln)
            ln = re.sub(r'\[\?\]', '#', ln)
            ln = re.sub(r'\(([^|)]*)\|[^)]*\)', r'\1', ln)
            out.append(base(re.sub(r'[^A-Za-z#]', '', ln)))
    return ''.join(out)


md = Path(sys.argv[1]).read_text(encoding='utf-8')
body = re.search(r'^## Reading[^\n]*\n(.*?)(?=^## |\Z)', md, re.S | re.M).group(1)
D = dec_letters(sys.argv[2:])
# reading tokens
toks = re.findall(r"\[[^\]]*\]|[^\s\[\]]+", body)
words = []                       # (token, letters counted for alignment, kind)
for t in toks:
    if t.startswith('[?') or t.startswith('[…') or t == '[?]':
        inner = t[2:-1] if t.startswith('[?') else ''
        words.append((t, base(re.sub(r'[^\w]', '', inner.replace('…', ''))), 'partly'))
    elif t.startswith('['):
        words.append((t, '', 'supplied'))
    else:
        clean = re.sub(r'\[[^\]]*\]', '', t)
        words.append((t, base(re.sub(r"[^\w]", '', clean)), 'plain'))
R = ''.join(w[1] for w in words)
sm = difflib.SequenceMatcher(None, R, D, autojunk=False)
hit = [False] * len(R)
for a, b, n in sm.get_matching_blocks():
    for k in range(n): hit[a + k] = True
pos, nplain, full, weak = 0, 0, 0, []
for t, letters, kind in words:
    n = len(letters)
    h = sum(hit[pos:pos + n]); pos += n
    if kind == 'plain' and n:
        nplain += 1
        if h == n: full += 1
        else: weak.append((t, h, n))
print('decode letters', len(D), 'reading letters', len(R), 'matched', sum(hit))
print('plain words', nplain, 'fully carried', full)
for t, h, n in weak: print('  ', t, f'{h}/{n}')
print('supplied:', [t for t, l, k in words if k == 'supplied'])
