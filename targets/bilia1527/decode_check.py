"""Independent check of Harumi-Matsuba's f. 102r reading (issue #55).

Applies OUR key for DECODE R5258 (targets/gilino1527: the sheet rows of dec.py, the letter table of key_R5258.md,
key_r8572.tsv and key_extra.tsv) to the contributor's sign transcription, translating their sign names into ours,
and compares the result sign by sign with their decoded values (their key.tsv). Then scores both decodes with the
shared Italian model (it-cinquecento, no spaces) against 1000 shuffled keys.

Run from the repository root:  PYTHONUTF8=1 python targets/bilia1527/decode_check.py [f102r|f102v]
Writes targets/bilia1527/measure.txt (f102r) or measure_f102v.txt and decoded_ours_<page>.txt.
"""
import csv, os, random, sys
HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, os.path.join(HERE, '..', '..'))
from lang import lm

G = os.path.join(HERE, '..', 'gilino1527')
C = os.path.join(HERE, 'contributed', 'data')

# --- our key, in our sign names -------------------------------------------------------------
K = {}
def rng(base, start, s):
    for i, v in enumerate(s.split()): K[f'{base}.{start+i}'] = v
rng('B', 31, 'ba be bi bo bu ca ce ci co cu da de di do du ga ge gi go gu')
rng('B', 51, 'fa fe fi fo fu')
rng('D', 51, 'la le li lo lu ma me mi mo mu na ne ni no nu')
rng('6', 56, 'pa pe pi po pu qua que qui quo quu ra re ri ro ru sa se si so su ta te ti to tu')
rng('o', 33, 'va ve vi vo vu xa xe xi xo xu za ze zi zo zu')
K.update({'A.42': 'al', 'A.43': 'am', 'A.44': 'an', 'H.26': 'cosa', 'H.27': 'che', 'H.28': 'come',
          'R.28': 'ancora', 'R.23': 'con', 'D.40': 'sara'})
# the sheet alphabet (key_R5258.md, "Letters"); bare numbers
for v, signs in {'a': '19 28', 'b': '20', 'c': '21', 'e': '25 49', 'f': '26', 'g': '29', 'h': '30', 'i': '31',
                 'l': '34', 'm': '35', 'n': '36', 'o': '39', 'p': '40', 'q': '41', 'r': '44', 's': '45',
                 't': '46', 'x': '50', 'et': '55'}.items():
    for s in signs.split(): K.setdefault(s, v)
# sheet null row (key_R5258.md "Nulls"): bare numbers and a#
for s in '22 32 42 48 37 33 23 27 43 47 73 45'.split():
    pass   # 33, 45 are also letters; only those not in the alphabet are nulls below
for s in '22 32 42 48 37 23 27 43 47 73'.split(): K[s] = ''
def tsv(p):
    for r in open(p, encoding='utf-8'):
        if r.startswith('#') or not r.strip() or r.startswith('token\t'): continue
        f = r.rstrip('\n').split('\t')
        if len(f) >= 2: yield f[0].rstrip('?'), f[1]
for t, v in list(tsv(os.path.join(G, 'key_r8572.tsv'))) + list(tsv(os.path.join(G, 'key_extra.tsv'))):
    v = '' if v in ('(null)', 'NULL') else v
    v = v.split('/')[0]                 # first value where two are given (o/v, a/o, con/null)
    if v.startswith('<'): v = '[' + v.strip('<>') + ']'
    K[t] = v

# their name -> our name
NAME = {'φ': 'bf', 'θ': 'th', '÷': 'dots', '3p': 'xp', 'zd': 'sq', 'r7': 'Rp', 'a++': 'a++'}
def ours(t):
    t = t.rstrip('?')
    if t in NAME: return NAME[t]
    if t.startswith('G.'): return '6.' + t[2:]
    if t.startswith('o.') and t[2:].isdigit() and int(t[2:]) >= 48: return 'D.' + t[2:]
    return t

def theirs_key():
    k = {}
    for r in csv.DictReader(open(os.path.join(C, 'key.tsv'), encoding='utf-8'), delimiter='\t'):
        v = r['value']; k[r['token']] = '' if v in ('(null)', '') else v.strip('<>?')
    return k

def lines(page):
    f = {'f102r': 'transcription_f102r.txt', 'f102v': 'transcription_f102v_unconfirmed.txt'}[page]
    for l in open(os.path.join(C, f), encoding='utf-8'):
        if l.startswith('#') or not l.strip(): continue
        lab, *toks = l.split(); yield lab, toks

def main(page):
    TK = theirs_key()
    L = list(lines(page))
    out, rows = [], []
    n = agree = both = mine_only = their_only = none = 0
    for lab, toks in L:
        s = []
        for t in toks:
            n += 1
            o = ours(t); mv = K.get(o); tv = TK.get(t.rstrip('?'))
            s.append(mv if mv is not None else f'[{t}]')
            if mv is not None and tv is not None:
                both += 1; agree += (mv == tv)
                if mv != tv: rows.append((lab, t, o, mv or '(null)', tv or '(null)'))
            elif mv is not None: mine_only += 1
            elif tv is not None: their_only += 1; rows.append((lab, t, o, '-', tv or '(null)'))
            else: none += 1
        out.append(f'{lab} ' + ''.join(s))
    open(os.path.join(HERE, f'decoded_ours_{page}.txt'), 'w', encoding='utf-8').write('\n'.join(out) + '\n')

    # LM: both decodes as one stream, signs without a value dropped, against shuffled keys
    m = lm.load('it-cinquecento', order=5, spaces=False)
    toks = [t for _, ts in L for t in ts]
    def text(key, f):
        return lm.norm(''.join(key.get(f(t), '') or '' for t in toks if not key.get(f(t), '').startswith('[')), 'early')
    sc_ours = m.per_char(text(K, ours))
    sc_theirs = m.per_char(text(TK, lambda t: t.rstrip('?')))
    used = sorted({ours(t) for t in toks if K.get(ours(t))})
    vals = [K[u] for u in used]
    rnd = random.Random(1527); best = -99; ge = 0
    for _ in range(1000):
        rnd.shuffle(vals); KS = dict(K); KS.update(zip(used, vals))
        s = m.per_char(text(KS, ours)); best = max(best, s); ge += (s >= sc_ours)
    with open(os.path.join(HERE, 'measure.txt' if page == 'f102r' else f'measure_{page}.txt'), 'w', encoding='utf-8') as f:
        p = lambda *a: print(*a, file=f)
        p(f'{page}: {n} signs in the contributor transcription ({len(L)} lines)')
        p(f'  our R5258 key gives a value (incl. null) to {n - their_only - none} signs ({(n - their_only - none)/n:.1%})')
        p(f'  their key gives a value (incl. null) to {n - mine_only - none} signs')
        p(f'  both give a value: {both}; same value: {agree} ({agree/both:.1%}); neither: {none}')
        p(f'  only theirs (their inferred values, not in our key): {their_only}')
        p(f'LM it-cinquecento o5 no spaces, mean log-prob per char: ours {sc_ours:.3f}, theirs {sc_theirs:.3f}')
        p(f'  1000 shuffles of our key over the {len(used)} valued signs used: best {best:.3f}, at or above ours: {ge}')
        p('Disagreements (line, their sign, our name, our value, their value):')
        for r in rows: p('  ' + '\t'.join(r))
    print(open(os.path.join(HERE, 'measure.txt' if page == 'f102r' else f'measure_{page}.txt'), encoding='utf-8').read())

if __name__ == '__main__':
    main(sys.argv[1] if len(sys.argv) > 1 else 'f102r')
