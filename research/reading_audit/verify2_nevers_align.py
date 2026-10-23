"""verify2 (nevers1574): check f15_reading.md word by word against its two sources, the contemporary interlinear
gloss (f15_gloss.md) and the cipher signs (f15_signs.tsv) decoded with the recovered alphabet (f15_key.md).

    python research/reading_audit/verify2_nevers_align.py [-a]

Per page section (f. 15r, f. 15v, f. 16r cipher lines), the reading's letters are aligned with the decoded signs
(each sign a letter set; '.', '?', 'XX' and number groups are wildcards at half credit; SS/[RM]/[-d-] are the name
signs Roy / Royne mere / Royne), and the reading's words are aligned with the gloss words (difflib, near-equal words
count). A word is listed when the signs carry under 0.6 of its letters and the gloss does not have it.
Words in [...] and […] are skipped; the clear ending and the address are not checked.
"""
import difflib
import pathlib
import re
import sys
import unicodedata

T = pathlib.Path(__file__).resolve().parents[2] / 'targets' / 'nevers1574'
KEY = {'1': ['a'], '±': ['b'], 'C': ['c'], 'b': ['d'], 'F': ['e'], 'E': ['e'], '+': ['f', 'm'], '0': ['g'],
       'h': ['h'], '7': ['i'], '3': ['l'], '2': ['n'], '8': ['o'], 'G': ['p'], '(9': ['p'], '9': ['q', 's'],
       'T': ['r'], '4': ['t'], '6': ['u'], 'Z': ['x', 'z'], 'y': ['y'], 'ʒ': ['ss', 'll', 's', 'l'],
       'b̶': ['ll', 'l'], 'q̶': ['f'], 'Z̶': ['z', 's'], 'SS': ['roy'], '[RM]': ['roynemere'], '[-d-]': ['royne'],
       '[Roy?]': ['roy'], 'o': ['g'], '∧': [], 'm': []}
SECT = [('## f. 15r', '## f. 15v', '15r'), ('## f. 15v', '## f. 16r (cipher', '15v'),
        ('## f. 16r (cipher', '## f. 16r (clear', '16r')]


def norm(s):
    s = ''.join(c for c in unicodedata.normalize('NFD', s.lower()) if unicodedata.category(c) != 'Mn')
    return re.sub(r'[^a-z]', '', s).replace('v', 'u').replace('j', 'i')


def units(page):
    out = []
    for l in (T / 'f15_signs.tsv').read_text(encoding='utf8').splitlines():
        if l.startswith('#') or not l.startswith(page):
            continue
        sig = l.split('\t')[2].split('|')[0]
        if sig.startswith('(gloss'):
            continue
        i = 0
        while i < len(sig):
            c = sig[i]
            if c.isspace():
                i += 1; continue
            for u in ('[Roy?]', '[RM]', '[-d-]', 'SS', 'XX', '(9', 'b̶', 'q̶', 'Z̶'):
                if sig.startswith(u, i):
                    out.append(u); i += len(u); break
            else:
                if sig.startswith('..', i):
                    out.append('..'); i += 2
                else:
                    out.append(c); i += 1
    return out


def opts(u):
    if u in KEY:
        return [x.replace('v', 'u').replace('j', 'i') for x in KEY[u]] or None
    return 'W'


def align(r, toks):
    n, m = len(r), len(toks)
    NEG = -1e9
    S = [[NEG] * (m + 1) for _ in range(n + 1)]
    B = [[None] * (m + 1) for _ in range(n + 1)]
    S[0][0] = 0.0
    for i in range(n + 1):
        for j in range(m + 1):
            v = S[i][j]
            if v == NEG:
                continue
            if i < n and v - 1.5 > S[i + 1][j]:
                S[i + 1][j] = v - 1.5; B[i + 1][j] = (i, j, 'ins')
            if j < m:
                o = opts(toks[j])
                c = 0 if o is None else (-0.3 if o == 'W' else -1.2)
                if v + c > S[i][j + 1]:
                    S[i][j + 1] = v + c; B[i][j + 1] = (i, j, 'skip')
                if o == 'W':
                    for L in (1, 2, 3, 4):
                        if i + L <= n and v + 0.3 * L > S[i + L][j + 1]:
                            S[i + L][j + 1] = v + 0.3 * L; B[i + L][j + 1] = (i, j, 'W')
                elif o:
                    for x in o:
                        L = len(x)
                        if i + L <= n and r[i:i + L] == x and v + 2 * L > S[i + L][j + 1]:
                            S[i + L][j + 1] = v + 2 * L; B[i + L][j + 1] = (i, j, 'm')
                        if L == 1 and i < n and r[i] != x and v - 1 > S[i + 1][j + 1]:
                            S[i + 1][j + 1] = v - 1; B[i + 1][j + 1] = (i, j, 'sub')
    cred = [0.0] * n
    i, j = n, m
    while (i, j) != (0, 0):
        pi, pj, k = B[i][j]
        if k == 'm':
            for x in range(pi, i):
                cred[x] = 1.0
        elif k == 'W':
            for x in range(pi, i):
                cred[x] = 0.5
        i, j = pi, pj
    return cred


def gloss(page):
    s = (T / 'f15_gloss.md').read_text(encoding='utf8')
    a = s.index('## f. ' + page)
    b = s.find('\n## ', a + 5)
    sec = s[a:b if b > 0 else len(s)]
    ws = []
    for l in sec.splitlines()[1:]:
        m = re.match(r'\s*\d+\.\s+(.*)', l)
        if not m:
            continue
        t = re.sub(r'\[\?\]', ' ', m.group(1))
        t = re.sub(r'\(rest of the line in clear[^)]*\)', ' ', t)
        for w in re.findall(r"[A-Za-zÀ-ÿ\[\]?']+", t):
            for p in re.split(r"'", w.replace('[?', '').replace('[', '').replace(']', '')):
                if norm(p):
                    ws.append(norm(p))
    return ws


def reading(a, b):
    s = (T / 'f15_reading.md').read_text(encoding='utf8')
    sec = s[s.index(a):s.index(b)]
    sec = '\n'.join(l for l in sec.splitlines() if not l.startswith('#'))
    words = []
    for m in re.finditer(r"\[[^\]]*\]|[^\s\[\]]+", sec):
        w = m.group(0)
        if w.startswith('['):
            continue
        for p in re.split(r"'", w):
            n = norm(p)
            if n and not re.fullmatch(r'\d+', p):
                words.append((w, n))
    return words


def main():
    allw = '-a' in sys.argv
    for a, b, page in SECT:
        words = reading(a, b)
        if page == '15r' and words and words[0][1] == 'monseigneur':
            words = words[1:]
        r = ''.join(n for _, n in words)
        cred = align(r, units(page))
        gw = gloss(page)
        sm = difflib.SequenceMatcher(None, [n for _, n in words], gw, autojunk=False)
        ing = set()
        for tag, i1, i2, j1, j2 in sm.get_opcodes():
            if tag == 'equal':
                ing.update(range(i1, i2))
            elif tag == 'replace':
                for i in range(i1, i2):
                    if any(difflib.SequenceMatcher(None, words[i][1], gw[j]).ratio() >= 0.75 for j in range(j1, j2)):
                        ing.add(i)
        pos, listed = 0, 0
        print(f'== f. {page}: {len(words)} words')
        for k, (w, n) in enumerate(words):
            f = sum(cred[pos:pos + len(n)]) / len(n)
            pos += len(n)
            if (f < 0.6 and k not in ing) or allw:
                listed += f < 0.6 and k not in ing
                ctx = ' '.join(x[0] for x in words[max(0, k - 3):k + 4])
                print(f'  {w!r} signs {f:.2f} gloss {"yes" if k in ing else "no"} | {ctx}')
        print(f'  listed {listed}')


if __name__ == '__main__':
    main()
