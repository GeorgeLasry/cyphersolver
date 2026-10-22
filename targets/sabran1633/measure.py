"""Re-measure Harumi-Matsuba's fr. 4134 reading (issue #56) with the project's own tools.

Reads only the copied files in contributed/ (no code from that repository is run):
  1. sign counts per leaf and share of signs with a value in Lasry's key (contributed/data/key.tsv)
  2. LM score per leaf (lang fr-1600-letters, no spaces, norm 'early') against 1000 shuffled keys
     (letter values permuted among the letter signs; word, double and unknown signs left as they are)
  3. coherent share: characters of the decoded letter runs covered by dictionary words of 3+ letters
     (word list from the fr-henri4 corpus, words seen at least 5 times), by a DP segmentation that
     maximises covered characters; the same measure on the shuffled keys gives the chance baseline
  4. the calibration on Baluze 155 f. 79 (Lasry's decipherment), recomputed with difflib as they describe

Run: PYTHONUTF8=1 python targets/sabran1633/measure.py > targets/sabran1633/measure.txt
"""
import os, sys, re, random, difflib, collections
HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, os.path.join(HERE, '..', '..'))
from lang import lm

C = os.path.join(HERE, 'contributed')

def load_key(path):
    k = {}
    for l in open(path, encoding='utf-8'):
        if l.startswith('#') or not l.strip(): continue
        f = l.rstrip('\n').split('\t')
        k[f[0]] = (f[1], f[2])
    return k

def load_tr(path):
    rows = []
    for l in open(path, encoding='utf-8'):
        if l.startswith('#') or not l.strip(): continue
        i, s = l.rstrip('\n').split('\t', 1)
        rows.append((i, s.split()))
    return rows

def decode(toks, key, keep_gaps=True):
    """Letter-run plaintext; word codes spelled out; unknown signs -> '#'."""
    out, prev = [], ''
    for t in toks:
        if t.startswith('[') or t == '|':
            out.append('#'); prev = ''; continue
        t0 = t.rstrip('?') if t != '?' else t
        v = key.get(t0)
        if v is None:
            out.append('#'); prev = ''; continue
        val, kind = v
        if kind == 'double': out.append(prev); continue
        if kind == 'word':
            w = re.sub(r'[^a-z]', '', val.split('/')[0]); out.append(w); prev = ''; continue
        out.append(val); prev = val
    return ''.join(out)

key = load_key(os.path.join(C, 'data', 'key.tsv'))
rows = load_tr(os.path.join(C, 'data', 'transcription.tsv'))
leaves = collections.OrderedDict()
FOL = {'c100': 'f. 46v', 'c108': 'f. 50v', 'c115': 'f. 54r', 'c121': 'f. 57r', 'c122': 'f. 57v',
       'c139': 'f. 66r', 'c140': 'f. 66v', 'c146': 'f. 69v', 'c154': 'f. 73v'}
for i, toks in rows:
    leaf = i.split('_')[0]
    if leaf not in FOL: continue          # c100_L28... duplicates at file end are a later re-check block
    if '_L' in i: continue
    leaves.setdefault(leaf, []).append(toks)

model = lm.load('fr-1600-letters', spaces=False)

# vocabulary
corp = open(os.path.join(HERE, '..', '..', 'lang', 'corpora', 'fr-henri4.txt'), encoding='utf-8').read()
cnt = collections.Counter(lm.norm(corp, 'early').split())
VOC = {w for w, n in cnt.items() if n >= 5 and len(w) >= 3}
MAXW = 16

def covered(s):
    """max characters of s covered by vocabulary words (3+ letters), DP"""
    n = len(s); best = [0] * (n + 1)
    for i in range(1, n + 1):
        b = best[i - 1]
        for L in range(3, min(MAXW, i) + 1):
            if s[i - L:i] in VOC:
                b = max(b, best[i - L] + L)
        best[i] = b
    return best[n]

def leaf_text(lines, k):
    return '#'.join(decode(t, k) for t in lines)

def lm_score(text):
    parts = [p for p in text.split('#') if len(p) >= 3]
    s = ''.join(parts)
    return model.per_char(s) if s else float('nan')

def coh(text):
    parts = [p for p in text.split('#') if p]
    tot = sum(len(p) for p in parts)
    return sum(covered(p) for p in parts), tot

letter_signs = [s for s, (v, kd) in key.items() if kd == 'letter']
letter_vals = [key[s][0] for s in letter_signs]

def shuffled(rng):
    vals = letter_vals[:]; rng.shuffle(vals)
    k = dict(key)
    for s, v in zip(letter_signs, vals): k[s] = (v, 'letter')
    return k

rng = random.Random(1633)
SH = [shuffled(rng) for _ in range(1000)]

print('# sabran1633 re-measure, 21 Oct 2026 (measure.py)')
print('# leaf  signs valued  LM(real)  LM shuffled median/max  >=real/1000  coherent(real)  coherent shuffled median/max')
T = V = CH = CT = 0
allsh = [[0, 0] for _ in SH]
for leaf, lines in leaves.items():
    sy = [t for toks in lines for t in toks if not t.startswith('[') and t != '|']
    val = sum(1 for t in sy if (t.rstrip('?') if t != '?' else t) in key)
    T += len(sy); V += val
    real = leaf_text(lines, key)
    r_lm = lm_score(real)
    c, ct = coh(real); CH += c; CT += ct
    lms, cohs = [], []
    for j, k in enumerate(SH):
        tx = leaf_text(lines, k)
        lms.append(lm_score(tx))
        a, b = coh(tx); cohs.append(a / max(1, b)); allsh[j][0] += a; allsh[j][1] += b
    lms.sort(); cohs.sort()
    ge = sum(1 for x in lms if x >= r_lm)
    print(f'{FOL[leaf]:7s} {len(sy):4d} {val:4d}  {r_lm:7.3f}  {lms[500]:7.3f}/{lms[-1]:7.3f}  {ge:4d}  '
          f'{c}/{ct}={c/max(1,ct):.3f}  {cohs[500]:.3f}/{cohs[-1]:.3f}')
shc = sorted(a / b for a, b in allsh)
print(f'total   {T:4d} {V:4d}  valued {V/T:.3f}; coherent {CH}/{CT} = {CH/CT:.3f}; '
      f'shuffled-key coherent median {shc[500]:.3f}, max {shc[-1]:.3f}')
print(f'# coherent above chance (real - shuffled median) / (1 - shuffled median) = '
      f'{(CH/CT - shc[500]) / (1 - shc[500]):.3f}')

# calibration
lasry = {}
for l in open(os.path.join(C, 'calib', 'lasry_plain.tsv'), encoding='utf-8'):
    if l.startswith('#') or not l.strip(): continue
    k, t = l.rstrip('\n').split('\t'); lasry[k] = re.sub(r'[^a-z]', '', t.lower())

def calib(path):
    F = collections.defaultdict(list)
    for l in open(path, encoding='utf-8'):
        if l.startswith('#') or '\t' not in l: continue
        n, s = l.rstrip('\n').split('\t', 1); m = re.match(r'(?:b79_)?(L\d+)', n.strip())
        if not m: continue
        s = re.sub(r'\?\{[^}]*\}', '?', s); s = re.sub(r'\[[^\]]*\]', '', s)
        F[m.group(1)].append([t.split('/')[0] for t in s.split()])
    tot = mt = 0
    for k, ref in lasry.items():
        seq = []
        for f in F.get(k, []):
            kk = 0
            for n in range(min(5, len(seq), len(f)), 0, -1):
                if seq[-n:] == f[:n]: kk = n; break
            seq += f[kk:]
        pl = decode(seq, key).replace('#', '')
        sm = difflib.SequenceMatcher(None, ref, pl, autojunk=False)
        tot += len(ref); mt += sum(b.size for b in sm.get_matching_blocks())
    return mt, tot

for f in ('transcription_f79.tsv', 'opus_first.tsv'):
    mt, tot = calib(os.path.join(C, 'calib', f))
    print(f'calibration {f}: {mt}/{tot} = {mt/tot:.3f}')
