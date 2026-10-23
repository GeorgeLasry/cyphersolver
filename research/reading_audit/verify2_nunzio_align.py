"""Verification pass 2 (22 Oct 2026), nunzio1736: align each Spagna 423 reading (texts/423-<n>_reading.md, body only)
letter by letter with its key decode (texts/423-<n>_decode_b04.txt, running decode; the transcription corrections of
423_b04_corrections.tsv are already applied by b04_seg.py) and list the words the decode does not carry.

    python research/reading_audit/verify2_nunzio_align.py [n ...]

Stream: syllables and nomenclator stems {x} as letters; {1234} open groups, [?x] probable values and <..> no-value
figures are wildcards that carry nothing (skipped free). Reading words already in [...] are dropped. u/v and i/j count
as one; a reading letter that doubles the letter before it gets half credit (the cipher writes single consonants);
vowels right after a nomenclator stem, inside the same word, are credited (the code stands for the whole word). Per word: share
of its letters carried; listed when below 0.8.
"""
import re
import sys
import unicodedata
import pathlib

T = pathlib.Path(__file__).resolve().parents[2] / 'targets' / 'nunzio1736' / 'texts'
TH = float(__import__("os").environ.get("TH", "0.8"))


def norm(s):
    s = unicodedata.normalize('NFD', s)
    s = ''.join(c for c in s if unicodedata.category(c) != 'Mn').lower().replace('v', 'u').replace('j', 'i')
    return re.sub(r'[^a-z]', '', s)


def stream(n):
    t = (T / f'423-{n}_decode_b04.txt').read_text(encoding='utf8').split('Running decode:')[1].replace('\n', '')
    chars, stem_end = [], []
    for m in re.finditer(r'\[\?[^\]]*\]|\{[^}]*\}|<[^>]*>|\(che\)|.', t):
        x = m.group(0)
        if x.startswith('[?') or x.startswith('<') or re.fullmatch(r'\{1\d{3}\}', x):
            chars.append('#'); stem_end.append(False)
        elif x.startswith('{'):
            v = norm(x[1:-1])
            for k, c in enumerate(v):
                chars.append(c); stem_end.append(k == len(v) - 1)
        else:
            for c in norm(x):
                chars.append(c); stem_end.append(False)
    return chars, stem_end


def body(n):
    s = (T / f'423-{n}_reading.md').read_text(encoding='utf8')
    s = s.split('\n## ')[0]
    ls = s.split('\n')
    i = max(k for k, l in enumerate(ls) if l.startswith('Marks') or l.startswith('[..] = '))
    while ls[i].strip():
        i += 1
    return '\n'.join(ls[i:])


def words_of(b):
    out = []
    for m in re.finditer(r"\[[^\]]*\]\S*|[^\s'’]+['’]?", b):
        w = m.group(0)
        if w.startswith('['):
            continue
        n = norm(re.sub(r'\[[^\]]*\]', '', w))
        if n:
            out.append((w, n, m.start()))
    return out


def align(r, s, se, ws=frozenset()):
    n, m = len(r), len(s)
    NEG = -1e9
    S = [[NEG] * (m + 1) for _ in range(n + 1)]
    B = [[None] * (m + 1) for _ in range(n + 1)]
    S[0][0] = 0.0
    for i in range(n + 1):
        Si = S[i]
        c0 = int(i * m / max(n, 1))
        for j in range(max(0, c0 - 700), min(m, c0 + 700) + 1):
            v = Si[j]
            if v <= NEG / 2:
                continue
            if i < n:
                if j > 0 and se[j - 1] and r[i] in 'aeiou' and i not in ws:
                    c, k = 0.5, 'stem'
                elif i > 0 and r[i] == r[i - 1]:
                    c, k = 0.3, 'dbl'
                else:
                    c, k = -1.5, 'ins'
                if v + c > S[i + 1][j]:
                    S[i + 1][j] = v + c; B[i + 1][j] = (i, j, k)
            if j < m:
                c = 0.0 if s[j] == '#' else -1.2
                if v + c > Si[j + 1]:
                    Si[j + 1] = v + c; B[i][j + 1] = (i, j, 'skip')
                if i < n and s[j] != '#':
                    c = 2.0 if r[i] == s[j] else -1.0
                    if v + c > S[i + 1][j + 1]:
                        S[i + 1][j + 1] = v + c; B[i + 1][j + 1] = (i, j, 'm' if r[i] == s[j] else 'sub')
    # free tail of the stream
    jbest = max(range(m + 1), key=lambda j: S[n][j])
    cred, at = [0.0] * n, [None] * n
    i, j = n, jbest
    while (i, j) != (0, 0):
        pi, pj, k = B[i][j]
        if k == 'm':
            cred[pi] = 1.0; at[pi] = pj
        elif k in ('stem', 'dbl'):
            cred[pi] = 1.0 if k == 'stem' else 0.5; at[pi] = pj
        elif k in ('ins', 'sub'):
            at[pi] = pj
        i, j = pi, pj
    return cred, at


def check(n):
    s, se = stream(n)
    ws = words_of(body(n))
    r = ''.join(w[1] for w in ws)
    starts, p = set(), 0
    for w in ws:
        starts.add(p); p += len(w[1])
    cred, at = align(r, s, se, starts)
    pos, out, tot = 0, [], 0.0
    for k, (w, nw, _) in enumerate(ws):
        c = cred[pos:pos + len(nw)]
        tot += sum(c)
        frac = sum(c) / len(nw)
        if frac < TH:
            js = [x for x in at[pos:pos + len(nw)] if x is not None] or [0]
            ctx = ' '.join(x[0] for x in ws[max(0, k - 4):k]) + ' <' + w + '> ' + ' '.join(x[0] for x in ws[k + 1:k + 4])
            dec = ''.join(s[max(0, min(js) - 12):max(js) + 12])
            out.append((w, round(frac, 2), ctx, dec))
        pos += len(nw)
    print(f'== 423/{n}: {len(ws)} words, carried {tot / max(len(r), 1):.3f}, {len(out)} listed')
    for w, f, c, d in out:
        print(f'  {w!r} {f} | {c}\n      dec: {d}')
    return out


if __name__ == '__main__':
    for a in sys.argv[1:] or ['1', '2', '4', '5', '6', '7', '8', '9', '10', '11']:
        check(int(a))
