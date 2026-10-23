"""verify2 (smith1562): align each grade-A reading (the letters Forbes prints, A Full View ii, 1741) word by word with
Forbes's text (OCR of the archive.org scan, targets/smith1562/forbes2.txt in the main checkout, git-ignored) and list
the reading words the print does not carry. The print is the source for these readings (it sets the deciphered words in
italic); the figures were checked against it in the re-read (no01-no23_reread_log.md).

    python research/reading_audit/verify2_smith_align.py [doc ...]

Words are compared after old-spelling folding (long s, u/v, i/j/y, doubled letters, final e dropped, ie/y); a pair
counts as carried when the folded forms agree or are close (SequenceMatcher >= 0.7, or the OCR form garbled).
Words already in [...] are skipped. Each listed word is shown with the reading's and the print's context, to be judged
by hand (OCR garbles, modernised spellings).
"""
import difflib
import pathlib
import re
import sys
import unicodedata

ROOT = pathlib.Path(__file__).resolve().parents[2]
T = ROOT / 'targets' / 'smith1562'
MAIN = pathlib.Path(r'C:\Users\dbour\cypher\targets\smith1562\forbes2.txt')
# doc: (first OCR line, last OCR line) of the letter in forbes2.txt (1-based, inclusive)
WIN = {'no01': (24393, 24545), 'no03': (29178, 29285), 'no04': (29738, 29900), 'no05': (31854, 31935),
       'no19': (10610, 10625), 'no20': (11078, 11090)}


def fold(w):
    w = w.replace('ſ', 's').lower()
    w = ''.join(c for c in unicodedata.normalize('NFD', w) if unicodedata.category(c) != 'Mn')
    w = re.sub(r'[^a-z]', '', w)
    w = w.replace('v', 'u').replace('j', 'i').replace('y', 'i').replace('w', 'u')
    w = re.sub(r'(.)\1+', r'\1', w)
    w = re.sub(r'ie', 'i', w)
    if len(w) > 3 and w.endswith('e'):
        w = w[:-1]
    return w


def forbes_words(doc):
    a, b = WIN[doc]
    ls = MAIN.read_text(encoding='utf8').splitlines()[a - 1:b]
    s = '\n'.join(ls)
    s = re.sub(r'-\s*\n\s*', '', s)  # rejoin hyphenated breaks
    return [w for w in (fold(x) for x in s.split()) if w]


def reading_words(doc):
    s = (T / f'{doc}_reading.md').read_text(encoding='utf8')
    s = re.sub(r'<!--.*?-->', '', s, flags=re.S)
    s = '\n'.join(l for l in s.splitlines() if not l.startswith('#'))
    out = []
    for m in re.finditer(r'\S+', s):
        w = m.group(0)
        marked = '[' in w
        n = fold(w.replace('⟨', '').replace('⟩', '').replace("'s", 's'))
        if n:
            out.append((w, n, marked))
    return out


def sim(a, b):
    if a == b:
        return 1.0
    return difflib.SequenceMatcher(None, a, b).ratio()


def align(r, f):
    n, m = len(r), len(f)
    NEG = -1e9
    S = [[NEG] * (m + 1) for _ in range(n + 1)]
    B = [[None] * (m + 1) for _ in range(n + 1)]
    S[0] = [0.0] * (m + 1)  # free start in the window
    for i in range(n + 1):
        for j in range(m + 1):
            v = S[i][j]
            if v == NEG:
                continue
            if i < n and v - 1.5 > S[i + 1][j]:
                S[i + 1][j] = v - 1.5; B[i + 1][j] = (i, j, 'ins')
            if j < m and v - 0.05 > S[i][j + 1]:
                S[i][j + 1] = v - 0.05; B[i][j + 1] = (i, j, 'del')
            if i < n and j < m:
                x = sim(r[i], f[j])
                sc = 2 * x if x >= 0.7 else -1.0
                if v + sc > S[i + 1][j + 1]:
                    S[i + 1][j + 1] = v + sc; B[i + 1][j + 1] = (i, j, ('m', x))
    j = max(range(m + 1), key=lambda q: S[n][q])
    i = n
    res = [None] * n
    while i > 0:
        pi, pj, k = B[i][j]
        if k == 'ins':
            res[pi] = (None, pj)
        elif isinstance(k, tuple):
            res[pi] = (k[1], pj)
        i, j = pi, pj
    return res


def check(doc):
    rw = reading_words(doc)
    fw = forbes_words(doc)
    res = align([x[1] for x in rw], fw)
    out = []
    for k, ((w, nw, marked), (x, j)) in enumerate(zip(rw, res)):
        if marked:
            continue
        if x is None or x < 0.7:
            ctx = ' '.join(y[0] for y in rw[max(0, k - 4):k + 5])
            fctx = ' '.join(fw[max(0, j - 4):j + 5])
            out.append((w, x, ctx, fctx))
    print(f'== {doc}: {len(rw)} words, {len(out)} listed')
    for w, x, c, fc in out:
        print(f'  {w!r} {x if x is None else round(x, 2)} | {c}\n      forbes: {fc}')


if __name__ == '__main__':
    for d in sys.argv[1:] or list(WIN):
        check(d)
