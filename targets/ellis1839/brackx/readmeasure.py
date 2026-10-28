"""Measure how much of the clean-copy text the decode gives, word by word.

The decoded groups (image transcriptions) are aligned letter by letter with the clean text (banded DP). A group may
match with its table value, the table's listed alternatives ("also ..."), or, with --corr, the corrections in
keys/ellis_values.tsv. A word is read when every letter is covered by groups that match exactly; a final plural s the
code leaves out is allowed. Prints the share and the words not read.
usage: readmeasure.py cleantext [--corr]"""
import sys, re

def letters(s): return re.sub(r'[^a-z]', '', s.lower())

def squeeze(s): return re.sub(r'(.)\1+', r'\1', s)

def lev(a, b):
    p = list(range(len(b) + 1))
    for i, x in enumerate(a, 1):
        c = [i]
        for j, y in enumerate(b, 1): c.append(min(p[j] + 1, c[j - 1] + 1, p[j - 1] + (x != y)))
        p = c
    return p[-1]

def load(corr):
    cand = {}
    for l in open('code_table.tsv'):
        p = l.rstrip('\n').split('\t')
        if len(p) < 2 or not p[0].isdigit(): continue
        vs = [p[1]]
        if len(p) > 3 and 'also' in p[3]:
            vs += re.split(r'[/,]', p[3].split('also', 1)[1])
        cand[int(p[0])] = {letters(v) for v in vs if v.strip()}
    for g, v in {1261: '', 1262: '', 1263: '', 1264: '', 1267: '', 1268: ''}.items(): cand[g] = {v}
    base = {647: 'mil', 116: 'congress', 1152: 'por'}
    for g, v in base.items(): cand.setdefault(g, set()).add(v)
    if corr:
        for l in open('ellis_values.tsv'):
            if l.startswith('#') or not l.strip(): continue
            g, v = l.split('\t')[:2]
            cand.setdefault(int(g), set()).add('' if v == '0' else letters({'1':'one','2':'two','3':'three','4':'four','5':'five','6':'six','8':'eight'}.get(v, v)))
    return cand

def main():
    text = open(sys.argv[1]).read().split()
    corr = '--corr' in sys.argv
    cand = load(corr)
    groups = []
    files = ['f015L', 'f015R', 'f016L', 'f016R', 'f017L', 'f017R', 'f018L', 'f018R', 'f019L', 'f019R']
    if '--files' in sys.argv: files = sys.argv[sys.argv.index('--files') + 1].split(',')
    for f in files:
        for l in open(f'ct_{f}.txt'):
            if not l.startswith('#'): groups += [int(x) for x in l.split() if x.isdigit()]
    chars, wid = [], []
    for k, w in enumerate(text):
        for c in letters(w): chars.append(c); wid.append(k)
    T, M = ''.join(chars), len(groups)
    N = len(T); INF = 10 ** 9; band = 250
    D = [dict() for _ in range(M + 1)]; B = [dict() for _ in range(M + 1)]
    D[0][0] = 0
    for i in range(M + 1):
        jc = int(i * N / M)
        for j in range(max(0, jc - band - 1), min(N, jc + band + 1) + 1):
            if j not in D[i]: continue
            d = D[i][j]
            if j < N and abs(j + 1 - jc) <= band:  # text letter with no group (supplied)
                if d + 1 < D[i].get(j + 1, INF): D[i][j + 1] = d + 1; B[i][j + 1] = ('skip', i, j)
            if i == M: continue
            jn = int((i + 1) * N / M)
            for s in cand.get(groups[i], set()):
                if T.startswith(s, j) and abs(j + len(s) - jn) <= band:
                    if d < D[i + 1].get(j + len(s), INF): D[i + 1][j + len(s)] = d; B[i + 1][j + len(s)] = ('ok', i, j)
            for k in range(0, 7):
                if j + k <= N and abs(j + k - jn) <= band:
                    c = d + 2 + (0 if k else 1)
                    if c < D[i + 1].get(j + k, INF): D[i + 1][j + k] = c; B[i + 1][j + k] = ('bad', i, j)
    # backtrace
    gid = [[] for _ in range(N)]
    good = [False] * N
    dec = [''] * N            # decoded letters attached to each text position (at the start of a group's span)
    unk = [False] * N         # a group with no value covers this position
    i, j = M, N
    while (i, j) != (0, 0):
        op, pi, pj = B[i][j]
        if op == 'ok':
            for x in range(pj, j): good[x] = True
        if op in ('ok', 'bad'):
            gid[min(pj, N - 1)].insert(0, groups[pi])
        if op in ('ok', 'bad') and pj < N:
            vals = cand.get(groups[pi])
            if op == 'ok': dec[pj] = T[pj:j] + dec[pj]
            elif vals: dec[pj] = sorted(vals, key=len)[-1] + dec[pj]
            else:
                for x in range(pj, max(j, pj + 1)): unk[min(x, N - 1)] = True
        i, j = pi, pj
    read, bad, var, marked = 0, [], [], []
    for k, w in enumerate(text):
        idx = [x for x in range(N) if wid[x] == k]
        if not idx: continue
        ok = all(good[x] for x in idx) or (all(good[x] for x in idx[:-1]) and T[idx[-1]] == 's' and len(idx) > 1)
        if not ok and '--variants' in sys.argv and not any(unk[x] for x in idx):
            d = ''.join(dec[x] for x in idx); wl = T[idx[0]:idx[-1] + 1]
            ok = squeeze(d) == squeeze(wl) or (len(wl) >= 7 and lev(d, wl) <= 1)
            if ok: var.append(f'{w}={d}')
        if ok: read += 1
        else:
            bad.append(w)
            if '--why' in sys.argv:
                gs = [g for x in range(idx[0], idx[-1] + 1) for g in gid[x]]
                print(f'  {w:16} groups {gs}  decoded {"".join(dec[x] for x in idx)!r}')
        marked.append(w if ok else '[?' + w.rstrip(',.:;') + ']' + w[len(w.rstrip(',.:;')):])
    n = len([w for w in text if letters(w)])
    print(f'words {n}  read {read}  share {read / n:.3f}  ({"with" if corr else "without"} corrections)')
    print('not read:', ' '.join(bad))
    if var: print('read as variant spellings:', ' '.join(var))
    if '--mark' in sys.argv:
        open(sys.argv[sys.argv.index('--mark') + 1], 'w').write(' '.join(marked) + '\n')

if __name__ == '__main__':
    main()

