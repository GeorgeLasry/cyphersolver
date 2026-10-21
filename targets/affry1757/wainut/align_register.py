"""Align the ciphertexts of this folder with the clear text of the same letters in the Fagel registers
(NA 1.10.29 inv. 5186 and 5187, transcription in register_clear.txt), using this folder's key.

Key = ../key_M.json + ../overrides.json + H/M rows of ../key_X.tsv + H/M rows of ../read/*_new.tsv (first value,
key_M first), as measure_sense.py uses it; 105 and 107 are nulls. Ciphertext = ../transcr/<R>.txt where it exists,
otherwise ../cipher_U.txt (with view.py's split of run-together groups).

Alignment: semi-global dynamic programming per cipher segment against the whole register text of the letter
(letters, accents removed, lower case). Scores:
  keyed group whose value stands at this point of the clear text   +len(value)
  keyed group whose value does not stand there                     -3, takes 1-8 characters
  group without a key value                                        -1, takes 1-10 characters (its reading)
  group left without clear text                                    -2
  clear-text character not covered by any group                    -0.6
Control: the same alignment with value-shuffled keys (the same groups keep a value, values permuted at random).

Run from this folder:  python align_register.py [n_shuffles, default 10]
Writes align/<R>.tsv, pool.tsv, key_conflicts.tsv, open_groups.tsv; prints every number quoted in ../NOTES.md
(section "Contribution by WAINUT"). Python 3 standard library and numpy."""
import collections, glob, json, os, random, sys, unicodedata
import numpy as np

HERE = os.path.dirname(os.path.abspath(__file__))
T = os.path.dirname(HERE)  # targets/affry1757
NULLS = {105, 107}
# Bourdeau record -> register pages (inventory, scan, side of the opening)
LETTERS = {
    'R1072': [('5186', 13, 'R'), ('5186', 14, 'L')],
    'R1076': [('5186', 16, 'R'), ('5186', 17, 'L')],
    'R1073': [('5186', 42, 'R')],
    'R1064': [('5186', 62, 'R'), ('5186', 63, 'L'), ('5186', 63, 'R')],
    'R1067': [('5186', 148, 'R'), ('5186', 149, 'L'), ('5186', 149, 'R'), ('5186', 150, 'L')],
    'R1068': [('5186', 181, 'L')],
    'R1054': [('5186', 248, 'R'), ('5186', 249, 'L')],
    'R1070': [('5186', 255, 'R'), ('5186', 256, 'L')],
    'R2067': [('5187', 14, 'R'), ('5187', 15, 'L')],
    'R1074': [('5187', 15, 'L'), ('5187', 15, 'R')],
}
# groups listed as open in ../NOTES.md (5 Oct 2026), plus the two clashes named there
OPEN = [970, 869, 109, 651, 731, 708, 1191, 1020, 1082, 890, 431, 373, 724, 993, 426, 427, 1022, 307, 1080]


def p(*a):
    return os.path.join(T, *a)


def load_key():
    key = {int(k): v for k, v in json.load(open(p('key_M.json'), encoding='utf8')).items()}
    key.update({int(k): v for k, v in json.load(open(p('overrides.json'), encoding='utf8')).items()})
    for line in open(p('key_X.tsv'), encoding='utf8').read().splitlines()[1:]:
        f = line.split('\t')
        if len(f) >= 3 and f[0].isdigit() and f[2][:1] in 'HM':
            key[int(f[0])] = f[1]
    for fn in sorted(glob.glob(p('read', '*_new.tsv'))):
        for line in open(fn, encoding='utf8'):
            f = line.rstrip('\n').split('\t')
            if len(f) >= 3 and f[0].strip().isdigit() and f[2].strip()[:1] in 'HM':
                key.setdefault(int(f[0].strip()), f[1].split('/')[0].strip())
    return key


def shuffled(key, seed):
    r = random.Random(seed)
    ks = list(key); vs = list(key.values()); r.shuffle(vs)
    return dict(zip(ks, vs))


def norm(s):
    s = unicodedata.normalize('NFD', s.lower())
    return ''.join(c for c in s if 'a' <= c <= 'z' or c.isdigit())


def register_pages():
    pages, cur = {}, None
    for line in open(os.path.join(HERE, 'register_clear.txt'), encoding='utf8'):
        line = line.rstrip('\n')
        if line.startswith('@ '):
            inv, sc = line[2:].split()
            cur = (inv, int(sc[:-1]), sc[-1]); pages[cur] = []
        elif cur and line and not line.startswith(('#', '%', 'MARGIN')):
            pages[cur].append(line)
    return pages


def split_runs(g, km):
    """view.py fix(): a number above 1199 is two groups run together; split where the parts have key values"""
    out = []
    for x in g:
        if x <= 1199:
            out.append(x); continue
        s = str(x); best = None
        for i in range(1, len(s)):
            a, b = s[:i], s[i:]
            if a[0] == '0' or b[0] == '0' or int(a) > 1199 or int(b) > 1199:
                continue
            sc = (a in km) + (b in km)
            if best is None or sc > best[0]:
                best = (sc, int(a), int(b))
        out += [best[1], best[2]] if best and best[0] >= 1 else [x]
    return out


def cipher(rec):
    f = p('transcr', rec + '.txt')
    segs = [[]]
    if os.path.exists(f):
        for line in open(f, encoding='utf8'):
            if line.startswith('#'):
                if segs[-1]:
                    segs.append([])
                continue
            for t in line.split():
                t = t.split('|')[0]
                if t.isdigit():
                    segs[-1].append(int(t))
    else:
        km = json.load(open(p('key_M.json'), encoding='utf8'))
        cur = None
        for line in open(p('cipher_U.txt'), encoding='utf8'):
            if line.startswith('#'):
                cur = line[2:].strip()
            elif cur == rec:
                segs = [split_runs([int(x) for x in line.split()], km)]
    return [s for s in segs if s]


def align(groups, P, key):
    n, m = len(groups), len(P)
    NEG = -1e9
    S = np.full((n + 1, m + 1), NEG); S[0, :] = 0.0
    BT = np.zeros((n + 1, m + 1), dtype=np.int16)  # 0 no text, 1..8 mismatch, 20+L match, 40+k open
    J = np.arange(m + 1); SRC = [None]
    for i, g in enumerate(groups):
        old = S[i]; new = old - 2.0; bt = np.zeros(m + 1, dtype=np.int16)
        v = '' if g in NULLS else (norm(key[g]) if g in key else None)
        if v:
            L = len(v)
            ok = np.array([P[j:j + L] == v for j in range(m + 1 - L)])
            c = np.full(m + 1, NEG); c[L:] = np.where(ok, old[:m + 1 - L] + L, NEG)
            b = c > new; new[b] = c[b]; bt[b] = 20 + L
            for k in range(1, 9):
                c = np.full(m + 1, NEG); c[k:] = old[:m + 1 - k] - 3.0
                b = c > new; new[b] = c[b]; bt[b] = k
        elif v is None:
            for k in range(1, 11):
                c = np.full(m + 1, NEG); c[k:] = old[:m + 1 - k] - 1.0
                b = c > new; new[b] = c[b]; bt[b] = 40 + k
        a = new + 0.6 * J; cm = np.maximum.accumulate(a)
        arg = np.maximum.accumulate(np.where(a == cm, J, 0))
        moved = cm - 0.6 * J > new + 1e-9
        SRC.append(np.where(moved, arg, J))
        S[i + 1] = np.where(moved, cm - 0.6 * J, new); BT[i + 1] = bt
    j = int(np.argmax(S[n])); out = []
    for i in range(n, 0, -1):
        j = int(SRC[i][j]); code = int(BT[i][j])
        if code == 0: k, st = 0, 'nochar'
        elif code < 20: k, st = code, 'mismatch'
        elif code < 40: k, st = code - 20, 'match'
        else: k, st = code - 40, 'open'
        out.append((groups[i - 1], P[j - k:j], st)); j -= k
    out.reverse()
    return out


def run(rec, key, P):
    rows = []
    for s in cipher(rec):
        rows += align(s, P, key) + [None]
    real = [r for r in rows if r]
    keyed_all = [r for r in real if r[0] not in NULLS and r[0] in key]
    keyed_al = [r for r in keyed_all if r[2] != 'nochar']
    match = sum(r[2] == 'match' for r in keyed_al)
    long_ = [r for r in keyed_al if len(norm(key[r[0]])) >= 3]
    return dict(rows=rows, groups=len(real), keyed_all=len(keyed_all), keyed_al=len(keyed_al), match=match,
                long=len(long_), long_match=sum(r[2] == 'match' for r in long_),
                nochar=sum(r[2] == 'nochar' for r in real), open=sum(r[2] == 'open' for r in real))


def main():
    sys.stdout.reconfigure(encoding='utf-8', errors='replace')
    nsh = int(sys.argv[1]) if len(sys.argv) > 1 else 10
    key = load_key(); pages = register_pages()
    print(f'key: {len(key)} groups with a value')
    os.makedirs(os.path.join(HERE, 'align'), exist_ok=True)
    seqs = {}; tot = [0, 0, 0]
    print('letter  groups  keyed  aligned  match  match/aligned  3+letters  match/keyed | shuffled keys match/keyed: mean (max)')
    for rec, pg in LETTERS.items():
        P = norm(' '.join(' '.join(pages[x]) for x in pg))
        r = run(rec, key, P); seqs[rec] = r['rows']
        with open(os.path.join(HERE, 'align', rec + '.tsv'), 'w', encoding='utf8', newline='\n') as f:
            f.write('i\tgroup\tkey\tregister\tstatus\n'); i = 0
            for x in r['rows']:
                if x is None:
                    f.write('#seg\n'); continue
                f.write(f'{i}\t{x[0]}\t{key.get(x[0], "")}\t{x[1]}\t{x[2]}\n'); i += 1
        ctl = []
        for s in range(nsh):
            c = run(rec, shuffled(key, s), P); ctl.append(c['match'] / c['keyed_all'])
        print(f"{rec}  {r['groups']:5d}  {r['keyed_all']:5d}  {r['keyed_al']:5d}  {r['match']:5d}  "
              f"{r['match'] / r['keyed_al']:.3f}  {r['long_match']}/{r['long']} = {r['long_match'] / r['long']:.3f}  "
              f"{r['match']}/{r['keyed_all']} = {r['match'] / r['keyed_all']:.3f} | "
              f"{sum(ctl) / len(ctl):.3f} ({max(ctl):.3f})  [groups without clear text: {r['nochar']}]", flush=True)
        tot[0] += r['match']; tot[1] += r['keyed_all']; tot[2] += r['groups']
    print(f'all ten letters: {tot[2]} groups; keyed groups matching the register {tot[0]}/{tot[1]} = {tot[0] / tot[1]:.3f}')

    # pool every group's occurrences over the ten letters
    occ = collections.defaultdict(list)
    for rec, rows in seqs.items():
        for i, x in enumerate(rows):
            if x:
                occ[x[0]].append((rec, i, x[1], x[2]))
    with open(os.path.join(HERE, 'pool.tsv'), 'w', encoding='utf8', newline='\n') as f:
        f.write('group\tkey\tn\tmatch\tmismatch\topen\tno text\tregister pieces where not matched (letter:piece)\n')
        for g in sorted(occ):
            o = occ[g]; c = collections.Counter(x[3] for x in o)
            f.write(f"{g}\t{key.get(g, '')}\t{len(o)}\t{c['match']}\t{c['mismatch']}\t{c['open']}\t{c['nochar']}\t"
                    + '; '.join(f'{x[0]}:{x[2]}' for x in o if x[3] in ('mismatch', 'open')) + '\n')
    conf = [g for g in sorted(occ) if g in key and g not in NULLS
            and sum(x[3] == 'mismatch' for x in occ[g]) >= 2
            and sum(x[3] == 'mismatch' for x in occ[g]) > sum(x[3] == 'match' for x in occ[g])]
    with open(os.path.join(HERE, 'key_conflicts.tsv'), 'w', encoding='utf8', newline='\n') as f:
        f.write('# keyed groups that disagree with the register at least twice and more often than they agree.\n'
                '# Many are spelling or abbreviation (premiers/premier, roi/roy, faut/faudroit); see NOTES.md.\n')
        f.write('group\tkey\tmatch\tmismatch\tregister pieces at mismatches (letter:piece)\n')
        for g in conf:
            o = occ[g]
            f.write(f"{g}\t{key[g]}\t{sum(x[3] == 'match' for x in o)}\t{sum(x[3] == 'mismatch' for x in o)}\t"
                    + '; '.join(f'{x[0]}:{x[2]}' for x in o if x[3] == 'mismatch') + '\n')
    opn = [g for g in sorted(occ) if g not in key and g not in NULLS and g <= 1199
           and any(x[3] == 'open' for x in occ[g])]
    with open(os.path.join(HERE, 'open_groups.tsv'), 'w', encoding='utf8', newline='\n') as f:
        f.write('# groups without a key value: the register piece the alignment gives them at each occurrence.\n'
                '# Automatic; a piece can be a syllable too long or too short at its edges. Single occurrences are weak.\n')
        f.write('group\toccurrences\tregister pieces (letter:piece)\n')
        for g in opn:
            o = [x for x in occ[g] if x[3] == 'open']
            f.write(f"{g}\t{len(o)}\t" + '; '.join(f'{x[0]}:{x[2]}' for x in o) + '\n')
    print(f'\nkey_conflicts.tsv: {len(conf)} keyed groups; open_groups.tsv: {len(opn)} groups without a key value')

    def ctx(rec, i, w=5):
        rows = seqs[rec]; out = []
        for j in range(max(0, i - w), min(len(rows), i + w + 1)):
            x = rows[j]
            if not x:
                continue
            s = x[1] if x[2] != 'nochar' else '_'
            out.append(f'**{x[0]}={s}**' if j == i else s)
        return ' '.join(out)
    print('\nopen groups of NOTES.md (5 Oct 2026) and the two clashes, every occurrence with its register context:')
    for g in OPEN:
        print(f"== {g} (key: {key.get(g, '-')})")
        for rec, i, piece, st in occ.get(g, []):
            print(f'   {rec}#{i} [{st}] {ctx(rec, i)}')
    print('\nR1068 decoded with the key:', ' '.join(key.get(g, f'[{g}]') for s in cipher('R1068') for g in s if g not in NULLS))


if __name__ == '__main__':
    main()
