"""r2d (23 Oct 2026): align a Spagna 423 decode (texts/423-<n>_decode_b04.txt tokens) with the transcription of its
contemporary clear copy (texts/423-<n>_copy.txt), so that each nomenclator group and each pair gets the copy's letters.

    python research/reading_audit/r2d_align.py <n> [out.tsv]

Banded DP over tokens x copy letters (both normalised: lower case, accents off, j=i, v=u, abbreviation dots and
punctuation dropped). A pair costs the edit distance between its label and the copy letters it takes; a nomenclator
group with a value costs the edit distance to its value (so a wrong value shows), an open group a small cost per
letter. Prints token / label / copy letters / mark (= agree, ~ differ, * group) and writes a tsv.
"""
import functools, pathlib, re, sys, unicodedata
ROOT = pathlib.Path(__file__).resolve().parents[2]
sys.path.insert(0, str(ROOT / 'research' / 'reading_audit'))
from r2d_kwic import tokens, T


def norm(s):
    s = unicodedata.normalize('NFD', s)
    s = ''.join(c for c in s if not unicodedata.combining(c)).lower()
    s = s.replace('j', 'i').replace('v', 'u')
    return re.sub(r'[^a-z]', '', s)


def copy_text(n):
    t = (T / f'423-{n}_copy.txt').read_text(encoding='utf8')
    t = '\n'.join(l for l in t.split('\n') if not l.startswith('#'))
    t = re.sub(r'\{struck:[^}]*\}', ' ', t)
    t = re.sub(r'\[\.\.\]', ' ', t)
    t = re.sub(r'\[\?([^\]]*)\]', r'\1', t)
    t = re.sub(r'^Copia\.?.*?\d{4}\.', '', t.strip(), flags=re.S)
    return t


@functools.lru_cache(maxsize=None)
def ed(a, b):
    if not a: return len(b)
    if not b: return len(a)
    return min(ed(a[1:], b[1:]) + (a[0] != b[0]), ed(a[1:], b) + 1, ed(a, b[1:]) + 1)


def label_of(l):
    if l.startswith('(') and l.endswith(')'): return norm(l[1:-1]), 'pair'
    if l.startswith('{') and l.endswith('}'):
        v = l[1:-1]
        return (None, 'open') if re.fullmatch(r'\d+', v) else (norm(v), 'group')
    if l.startswith('[?'): return norm(l[2:-1]), 'group'
    if l.startswith('<'): return '', 'blank'
    return norm(l), 'pair'


def align(toks, c):
    n, m = len(toks), len(c)
    INF = 1e18
    ratio = m / max(1, n)
    BAND = 260
    D = {(0, 0): (0.0, None)}
    for j in range(1, min(m, BAND) + 1): D[(0, j)] = (j * 1.0, (0, j - 1, 0))
    for i in range(1, n + 1):
        code, l = toks[i - 1]
        lab, kind = label_of(l)
        is_grp = len(code) == 4
        centre = int(i * ratio)
        lo, hi = max(0, centre - BAND), min(m, centre + BAND)
        for j in range(lo, hi + 1):
            best = (INF, None)
            # skip copy letter
            if (i, j - 1) in D:
                v = D[(i, j - 1)][0] + 1.0
                if v < best[0]: best = (v, (i, j - 1, -1))
            if kind == 'pair':
                L = len(lab)
                for k in range(max(0, L - 1), L + 2):
                    if j - k < 0 or (i - 1, j - k) not in D: continue
                    v = D[(i - 1, j - k)][0] + ed(lab, c[j - k:j])
                    if v < best[0]: best = (v, (i - 1, j - k, k))
            elif kind == 'blank':
                for k in range(0, 3):
                    if j - k < 0 or (i - 1, j - k) not in D: continue
                    v = D[(i - 1, j - k)][0] + 0.6 + 0.3 * k
                    if v < best[0]: best = (v, (i - 1, j - k, k))
            else:
                for k in range(0, 16):
                    if j - k < 0 or (i - 1, j - k) not in D: continue
                    if kind == 'open':
                        v = D[(i - 1, j - k)][0] + (1.5 if k == 0 else 0.25 + 0.02 * k)
                    else:
                        v = D[(i - 1, j - k)][0] + min(ed(lab, c[j - k:j]) * 0.7, 0.25 + 0.02 * k + 2.5) + (1.0 if k == 0 else 0)
                    if v < best[0]: best = (v, (i - 1, j - k, k))
            if best[1] is not None: D[(i, j)] = best
    # end: allow trailing copy letters
    j = min((jj for (ii, jj) in D if ii == n), key=lambda jj: D[(n, jj)][0] + (m - jj))
    out = []
    i = n
    while i > 0:
        pi, pj, k = D[(i, j)][1]
        if k == -1:
            out.append((None, None, c[pj:j])); j = pj; continue
        out.append((toks[i - 1][0], toks[i - 1][1], c[pj:j])); i, j = pi, pj
    out.reverse()
    return out


if __name__ == '__main__':
    n = sys.argv[1]
    toks = [t for t in tokens(T / f'423-{n}_decode_b04.txt') if t[0] != '7']
    c = norm(copy_text(n))
    res = align(toks, c)
    rows = []
    extra = ''
    for code, l, s in res:
        if code is None:
            extra += s; continue
        if extra and rows: rows[-1][2] += '+' + extra
        extra = ''
        lab, kind = label_of(l)
        mark = '*' if len(code) == 4 else ('=' if lab == s else '~')
        rows.append([code, l, s, mark])
    out = sys.argv[2] if len(sys.argv) > 2 else None
    lines = ['\t'.join(r) for r in rows]
    if out: pathlib.Path(out).write_text('code\tlabel\tcopy\tmark\n' + '\n'.join(lines) + '\n', encoding='utf8')
    for r in rows:
        if r[3] != '=': print('\t'.join(r))
