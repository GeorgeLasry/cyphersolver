"""b18 (ceva1632): word-by-word check of a reading against its two carriers, the decode (r75/r84.read3.txt, Lasry's
key + adopted values) and the contemporary decipherment (R75_decifrato_f82r.txt / R84_decifrato_f136r.txt).
A reading word counts as carried by a source when its normalised letters occur in that source within a window
around the word's relative position. Lists the words carried by neither (must be bracketed) and the shares.

    python research/reading_audit/b18_ceva_check.py r75|r84
"""
import re, sys, pathlib, unicodedata
T = pathlib.Path(__file__).resolve().parents[2] / 'targets' / 'ceva1632'
def norm(s):
    s = unicodedata.normalize('NFD', s.lower())
    s = ''.join(c for c in s if c.isalpha() and c.isascii()).replace('u', 'v').replace('j', 'i')
    return re.sub(r'(.)\1+', r'\1', s)
doc = sys.argv[1]
dec = {'r75': 'R75_decifrato_f82r.txt', 'r84': 'R84_decifrato_f136r.txt'}[doc]
rd = (T / f'{doc.upper()}_reading.md').read_text(encoding='utf-8')
body = rd.split('## Reading', 1)[1].split('## Notes', 1)[0]
body = re.sub(r'\[[^\]]*\]', ' ', body)             # bracketed material is marked already
words = re.findall(r"[A-Za-zÀ-ÿ.']+", body)
words = [w for w in (x.strip(".'") for x in words) if w]
S1 = norm(re.sub(r'[<{][^>}]*[>}]', '', (T / f'{doc}.read3.txt').read_text(encoding='utf-8')))
S2 = norm(' '.join(l for l in (T / dec).read_text(encoding='utf-8').splitlines() if not l.startswith('#')))
n = len(words); c1 = c2 = 0; none = []
for i, w in enumerate(words):
    x = norm(w)
    if not x: continue
    f = i / max(1, n - 1)
    def near(S):
        a = max(0, int(f * len(S)) - 250); return x in S[a:a + 500]
    a, b = near(S1), near(S2)
    c1 += a; c2 += b
    if not (a or b): none.append(w)
print(f'{doc}: {n} words; in the decode {c1} ({c1/n:.2f}), in the decipherment {c2} ({c2/n:.2f}); in neither: {len(none)}')
print('  neither:', ' '.join(none) or '-')
