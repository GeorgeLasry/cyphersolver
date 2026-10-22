"""Re-measure Harumi-Matsuba's contributed reading of Baluze 103 f. 50 (issue #54) with this project's tools.

Our own decoder and scoring, not the contributor's scripts. Reads contributed/data/key.tsv,
contributed/data/transcription_f50.txt and contributed/docs/READING.en.md; writes measure.txt.

1. counts: cipher signs, signs with a key value (main or other), code groups.
2. LM: fr-1600-letters (order 5, no spaces, 'early' norm) per-char score of the bare key decode, of the
   contributor's joined reading, and of 200 decodes with the key's values shuffled over its signs.
3. coherence: per line, the signs are aligned by dynamic programming with the letters of the contributor's line
   reading (letters they supplied in [ ] and unread ⟨ ⟩ removed); a sign counts as read when one of its key
   values (or its code word) matches the reading at that place. This is the share of cipher signs whose key value
   survives into the reading, i.e. what the key gives, not what context supplied.
4. calibration: letter LCS of the contributor's frozen f. 171r reading against their transcription of the period
   decipherment f. 172r (recomputes their 337/360).

Run: PYTHONUTF8=1 python targets/letellier1644/measure.py
"""
import os, re, sys, random, unicodedata
HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, os.path.join(HERE, '..', '..'))
from lang import lm

C = os.path.join(HERE, 'contributed')
CODES = {'=9': 'pour', '=11': 'que', '=12': 'qui', '=26': 'vous', '=32': 'barcelone', '81': 'faire',
         '39': 'catalogne', '=y': 'monsieurlemareschal', '=3': 'delamotte', '=o': 'lareyne', '=83': 'legouverneur'}
# '=11 =o' is 'la Reyne' as a pair (v06); handled below


def norm(s):
    s = unicodedata.normalize('NFD', s.lower())
    s = ''.join(c for c in s if not unicodedata.combining(c))
    return re.sub('[^a-z]', '', s.replace('j', 'i').replace('v', 'u').replace('y', 'i'))


def load_key():
    key = {}
    for l in open(os.path.join(C, 'data', 'key.tsv'), encoding='utf-8'):
        if l.startswith('#') or not l.strip(): continue
        f = l.rstrip('\n').split('\t')
        vals = [f[1]] + ([v for v in f[2].split(',') if v] if len(f) > 2 and f[2] else [])
        key[f[0]] = [v for v in vals if v != '?']
    return key


def load_tx():
    lines = []
    for l in open(os.path.join(C, 'data', 'transcription_f50.txt'), encoding='utf-8'):
        if l.startswith('#') or not l.strip(): continue
        lid, *toks = l.split()
        lines.append((lid, toks))
    return lines


def load_reading():
    out = {}
    for l in open(os.path.join(C, 'docs', 'READING.en.md'), encoding='utf-8'):
        m = re.match(r'\|\s*([rv]\d\d)\s*\|\s*(.*?)\s*\|', l)
        if m:
            t = re.sub(r'\[[^\]]*\]', '', m.group(2))       # letters supplied by the contributor
            t = re.sub(r'⟨[^⟩]*⟩', '', t)                   # unread signs
            out[m.group(1)] = norm(t)
    return out


def units(toks, key):
    """(token, [candidate strings]) for cipher tokens; clear words in [ ] and the gutter cut are skipped."""
    out, i = [], 0
    while i < len(toks):
        t = toks[i]
        if t.startswith('['): i += 1; continue
        if t == 'cut': out.append((t, [])); i += 1; continue
        if t == '=11' and i + 1 < len(toks) and toks[i + 1] == '=o':
            out.append(('=11 =o', ['lareyne'])); i += 2; continue
        if t in CODES: out.append((t, [CODES[t]]))
        else: out.append((t, [norm(v) for v in key.get(t, [])]))
        i += 1
    return out


def align(us, target):
    """max number of units whose candidate matches target at its place (DP; unmatched units may absorb or skip)."""
    n, m = len(us), len(target)
    NEG = -10 ** 9
    dp = [[NEG] * (m + 1) for _ in range(n + 1)]
    for j in range(m + 1): dp[0][j] = 0
    for i in range(1, n + 1):
        cands = us[i - 1][1]
        for j in range(m + 1):
            best = max(dp[i - 1][j], dp[i][j - 1] if j else NEG)      # unit gives nothing / reading letter unmatched
            for c in cands:
                L = len(c)
                if L and j >= L and target[j - L:j] == c: best = max(best, dp[i - 1][j - L] + 1)
                elif L and j >= L: best = max(best, dp[i - 1][j - L])   # wrong letters in place
            dp[i][j] = best
    return dp[n][m]


def main():
    key, tx, rd = load_key(), load_tx(), load_reading()
    model = lm.load('fr-1600-letters', order=5, spaces=False)
    out = []
    allu = [(lid, units(t, key)) for lid, t in tx]
    nsig = sum(len(u) for _, u in allu)
    ncode = sum(1 for _, u in allu for t, c in u if t in CODES or t == '=11 =o')
    nval = sum(1 for _, u in allu for t, c in u if c)
    out.append(f'cipher units (signs, a code pair =11 =o counted once, clear words excluded): {nsig}')
    out.append(f'  code groups: {ncode}; units with a key value or code word: {nval} ({nval / nsig:.1%})')
    # LM
    bare = ''.join((c[0] if c else '') for _, u in allu for t, c in u)
    joined = ''.join(rd[l] for l, _ in tx)
    sb, sj = model.per_char(lm.norm(bare, 'early')), model.per_char(lm.norm(joined, 'early'))
    signs = sorted(key); vals = [key[s][0] if key[s] else '' for s in signs]
    rnd = random.Random(1); sh = []
    for _ in range(200):
        v = vals[:]; rnd.shuffle(v); k2 = {s: [x] for s, x in zip(signs, v)}
        d = ''.join((c[0] if c else '') for _, t in tx for _t, c in units(t, k2))
        sh.append(model.per_char(lm.norm(d, 'early')))
    sh.sort()
    out.append(f'LM fr-1600-letters o5 no spaces, per char: bare key decode {sb:.3f}; joined reading {sj:.3f}; '
               f'200 shuffled keys median {sh[100]:.3f}, max {sh[-1]:.3f}, >= bare {sum(x >= sb for x in sh)}/200')
    # coherence
    tot = hit = 0; per = []
    for lid, u in allu:
        h = align(u, rd.get(lid, '')); tot += len(u); hit += h; per.append(f'{lid} {h}/{len(u)}')
    out.append(f'signs whose key value or code word stands in the contributor\'s line reading: {hit}/{tot} = {hit / tot:.1%}')
    out.append('  per line: ' + ', '.join(per))
    # calibration
    def rd_c(p):
        d = {}
        for l in open(os.path.join(C, 'calib', p), encoding='utf-8'):
            if l.startswith('#') or not l.strip(): continue
            lid, _, t = l.partition(' ')
            t = re.sub(r'\(\?\)|\[\?\]|\.\.\.', '', t)
            d[lid] = norm(t.replace('[', '').replace(']', ''))
        return d
    a, b = rd_c('f171r_reading.txt'), rd_c('f172r_ref.txt')
    def lcs(x, y):
        p = [0] * (len(y) + 1)
        for cx in x:
            q = [0]
            for j, cy in enumerate(y): q.append(p[j] + 1 if cx == cy else max(p[j + 1], q[j]))
            p = q
        return p[-1]
    m = sum(lcs(a[k], b[k]) for k in b); n = sum(len(b[k]) for k in b)
    out.append(f'calibration f. 171r ll. 12-24 vs f. 172r (their transcriptions; brackets kept as letters): {m}/{n} = {m / n:.1%}')
    s = '\n'.join(out)
    print(s)
    open(os.path.join(HERE, 'measure.txt'), 'w', encoding='utf-8').write(s + '\n')


if __name__ == '__main__':
    main()
