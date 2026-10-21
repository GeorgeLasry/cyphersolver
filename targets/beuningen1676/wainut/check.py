"""Reproduce every number in the WAINUT section of ../NOTES.md (Python standard library only).

Run from the repository root or from anywhere:
    python3 targets/beuningen1676/wainut/check.py
It reads this target's key and gloss files (../key/*.tsv, ../transcription/tx/*.tsv, ../evidence/ext2/hits.tsv,
../transcription/june1676_tx.txt) and the transcriptions in transcription/, writes readings/<crop>.txt and prints:
  1. the size of key A and key B;
  2. the calibration on 249 scan 131R against june1676_tx.txt;
  3. coverage per crop with key A and key B;
  4. the shuffle control T (character 5-gram), with whole-key, codes-only and letters-only shuffles;
  5. the letter numbers absent from key_letters.tsv that occur in the eye-checked crops;
  6. the codes and colon words that key B does not give, per crop.

Key A = key_letters.tsv, key_words.tsv, key_codes.tsv overridden by corrections.tsv, as scripts/decode.py applies them,
except that a correction whose reading is bracketed or '?' (t218, s439) leaves the table value as it is.
Key B = key A plus the code and colon-word glosses in transcription/tx/*.tsv (tokconf H or M; H counts 2, M 1; the most
frequent gloss wins) and evidence/ext2/hits.tsv. Key A wins where both have a value.
"""
import collections, csv, difflib, glob, math, os, random, re

HERE = os.path.dirname(os.path.abspath(__file__))
T = os.path.dirname(HERE)                      # targets/beuningen1676
TX = os.path.join(HERE, 'transcription')
OUT = os.path.join(HERE, 'readings')
SEED, NSHUF = 1675, 200

# ---------------------------------------------------------------- key


def _load(fn):
    d = {}
    for l in open(os.path.join(T, 'key', fn), encoding='utf8'):
        if l.startswith('#') or not l.strip():
            continue
        p = l.rstrip('\n').split('\t')
        d[p[0]] = p[1]
    return d


def key_a():
    L, W, C = _load('key_letters.tsv'), _load('key_words.tsv'), _load('key_codes.tsv')
    for row in csv.DictReader(open(os.path.join(T, 'key', 'corrections.tsv'), encoding='utf8'), delimiter='\t'):
        if row['reading'].startswith('[') or row['reading'] == '?':
            continue
        (W if row['code'].endswith(':') else C)[row['code'].rstrip(':')] = row['reading']
    return {'L': L, 'W': W, 'C': C}


def key_b():
    K = key_a()
    votes = collections.defaultdict(collections.Counter)
    for fn in sorted(glob.glob(os.path.join(T, 'transcription', 'tx', '*.tsv'))):
        for l in open(fn, encoding='utf8'):
            if l.startswith('#') or not l.strip():
                continue
            p = l.rstrip('\n').split('\t')
            if len(p) < 5:
                continue
            tok, gl, cf = p[2].strip(), p[3].strip(), p[4].strip()
            if not gl or gl == '?' or cf not in ('H', 'M'):
                continue
            w = 2 if cf == 'H' else 1
            m = re.match(r'^([a-zA-Z])\.?\s*(\d+)(?:\^\w+)?$', tok)
            if m:
                votes[('C', m.group(1).lower() + m.group(2))][gl.lower()] += w
                continue
            m = re.match(r'^(\d+):-?$', tok)
            if m:
                votes[('W', m.group(1))][gl.rstrip('-').lower()] += w
    for row in csv.DictReader(open(os.path.join(T, 'evidence', 'ext2', 'hits.tsv'), encoding='utf8'), delimiter='\t'):
        c = (row.get('code') or '').strip().lower()
        if re.match(r'^[a-z]\d+$', c) and row.get('gloss'):
            votes[('C', c)][row['gloss'].strip().lower()] += 2
    for (kind, code), cnt in votes.items():
        if code not in K[kind]:
            K[kind][code] = cnt.most_common(1)[0][0]
    return K

# ---------------------------------------------------------------- tokens and decoding


TOK = re.compile(r'~[^~]*~|\{[^}]*\}(?:\^\w+)?|\d+:-?(?:\^\w+)?|[a-zA-Z]\d+(?:\^\w+)?')


def kind(t):
    if t.startswith('~'):
        return 'clear'
    if t.startswith('{'):
        return 'seq'
    return 'word' if re.match(r'\d+:', t) else 'code'


def merge(lines):
    """join a line with the next while a {...} or ~...~ is open"""
    out, buf = [], ''
    for l in lines:
        buf = (buf + ' ' + l).strip() if buf else l
        if buf.count('{') > buf.count('}') or buf.count('~') % 2:
            continue
        out.append(buf)
        buf = ''
    if buf:
        out.append(buf)
    return out


def seq_nums(t):
    return [n.strip().strip('-').strip() for n in re.match(r'\{([^}]*)\}', t).group(1).split(',') if n.strip().strip('-').strip()]


def decode(t, K):
    """(text, status): status ok / part / none / clear"""
    k = kind(t)
    if k == 'clear':
        return t[1:-1], 'clear'
    if k == 'seq':
        nums = seq_nums(t)
        sfx = re.match(r'\{[^}]*\}(?:\^(\w+))?', t).group(1) or ''
        s = ''.join(K['L'].get(n, '?') for n in nums)
        unk = s.count('?')
        return s + sfx, 'ok' if unk == 0 else ('none' if unk == len(nums) else 'part')
    if k == 'word':
        m = re.match(r'(\d+):(-?)(?:\^(\w+))?$', t)
        v = K['W'].get(m.group(1))
        return (v + m.group(2) + (m.group(3) or ''), 'ok') if v else (f'[{m.group(1)}:]', 'none')
    m = re.match(r'([a-zA-Z])(\d+)(?:\^(\w+))?$', t)
    v = K['C'].get(m.group(1).lower() + m.group(2))
    return (v + ('+' + m.group(3) if m.group(3) else ''), 'ok') if v else (f'[{m.group(1).lower()}{m.group(2)}]', 'none')


def read_tx(path):
    return [l.split(' ', 1)[1].rstrip() for l in open(path, encoding='utf8') if not l.startswith('#') and ' ' in l]


def decode_lines(lines, K):
    out, st = [], collections.Counter()
    for line in merge(lines):
        res = []
        for t in TOK.findall(line):
            txt, s = decode(t, K)
            if s == 'clear':
                res.append(txt)
                continue
            st['n'] += 1
            st[s] += 1
            res.append(txt.upper() if s in ('ok', 'part') else txt)
        out.append(' '.join(res))
    return out, st

# ---------------------------------------------------------------- control T


def clear_text(lines):
    return [c for l in lines for c in re.findall(r'~([^~]*)~', l)]


def gloss_text():
    seq = []
    for fn in sorted(glob.glob(os.path.join(T, 'transcription', 'tx', '*.tsv'))):
        for l in open(fn, encoding='utf8'):
            if l.startswith('#') or not l.strip():
                continue
            p = l.rstrip('\n').split('\t')
            if len(p) > 3 and p[3].strip() and p[3].strip() != '?':
                seq.append(p[3].strip())
    return ' '.join(seq)


class NGram:
    """character 5-gram with simple interpolation; the same model scores every key"""
    N, V = 5, 27

    def __init__(self, text):
        text = re.sub(r' +', ' ', re.sub(r'[^a-z ]+', ' ', text.lower()))
        self.size = len(text)
        self.c = [collections.Counter() for _ in range(self.N + 1)]
        for i in range(len(text)):
            for n in range(1, self.N + 1):
                if i + n <= len(text):
                    self.c[n][text[i:i + n]] += 1

    def lp(self, ctx, ch):
        p = 1.0 / self.V
        for n in range(1, self.N + 1):
            if n > 1 and len(ctx) < n - 1:
                break
            c = ctx[-(n - 1):] if n > 1 else ''
            den = self.c[n - 1][c] if n > 1 else self.size
            if den:
                lam = den / (den + 3.0)
                p = lam * (self.c[n][c + ch] / den) + (1 - lam) * p
        return math.log(p)


def spans(lines, K):
    """runs of fully decoded cipher tokens; clear text and undecoded tokens break a run"""
    out, cur = [], []
    for l in merge(lines):
        for t in TOK.findall(l):
            txt, st = decode(t, K)
            if st != 'ok':
                if cur:
                    out.append(cur)
                cur = []
                continue
            cur.append(re.sub(r'[^a-z ]', '', txt.lower().replace('+', '')))
    if cur:
        out.append(cur)
    return [' '.join(s) for s in out if s]


def score(lm, lines, K):
    tot = n = 0
    for s in spans(lines, K):
        s = ' ' + re.sub(r' +', ' ', s).strip() + ' '
        for i in range(1, len(s)):
            tot += lm.lp(s[max(0, i - lm.N + 1):i], s[i])
            n += 1
    return (tot / n if n else float('nan')), n


def shuffled(K, rng, tables):
    out = {}
    for t, tab in K.items():
        if t in tables:
            ks = list(tab)
            vs = [tab[k] for k in ks]
            rng.shuffle(vs)
            out[t] = dict(zip(ks, vs))
        else:
            out[t] = tab
    return out

# ---------------------------------------------------------------- main


def main():
    A, B = key_a(), key_b()
    print('1. KEYS')
    print(f"   key A: {len(A['L'])} letter numbers, {len(A['W'])} colon words, {len(A['C'])} codes")
    print(f"   key B: {len(B['L'])} letter numbers, {len(B['W'])} colon words, {len(B['C'])} codes")

    crops = {os.path.basename(f)[:-4]: read_tx(f) for f in sorted(glob.glob(os.path.join(TX, '*.txt')))}

    # 2. calibration
    print('\n2. CALIBRATION, 249 scan 131R: model transcription against ../transcription/june1676_tx.txt (131R lines)')

    def ctoks(lines):
        return [re.sub(r'-', '', t.replace(' ', '')) if t.startswith('{') else t.replace(' ', '')
                for l in merge(lines) for t in TOK.findall(l) if kind(t) != 'clear']
    gold_lines = [l.split(' ', 1)[1] for l in open(os.path.join(T, 'transcription', 'june1676_tx.txt'), encoding='utf8')
                  if l.startswith('131R.')]
    gold, ours = ctoks(gold_lines), ctoks(crops['249_p131R'])
    sm = difflib.SequenceMatcher(a=gold, b=ours, autojunk=False)
    eq = sum(b.size for b in sm.get_matching_blocks())
    print(f'   june1676_tx.txt 131R: {len(gold)} cipher tokens; model: {len(ours)}; identical: {eq} ({100 * eq / len(gold):.1f}%)')
    for op, i1, i2, j1, j2 in sm.get_opcodes():
        if op != 'equal':
            print(f'     {" ".join(gold[i1:i2]) or "-"}  ->  {" ".join(ours[j1:j2]) or "-"}')
    dg = [decode(t, A)[0].lower() for t in gold]
    do = [decode(t, A)[0].lower() for t in ours]
    eq2 = sum(b.size for b in difflib.SequenceMatcher(a=dg, b=do, autojunk=False).get_matching_blocks())
    print(f'   decoded with key A, identical decoded tokens: {eq2}/{len(gold)}')

    # 3. coverage and readings
    print('\n3. COVERAGE (cipher tokens fully decoded / partly decoded / total)')
    os.makedirs(OUT, exist_ok=True)
    print(f"   {'crop':11s} {'tokens':>6s}  {'key A full':>10s} {'part':>4s}  {'key B full':>10s} {'part':>4s}")
    for cid, lines in crops.items():
        da, sa = decode_lines(lines, A)
        db, sb = decode_lines(lines, B)
        print(f"   {cid:11s} {sb['n']:6d}  {sa['ok']:10d} {sa['part']:4d}  {sb['ok']:10d} {sb['part']:4d}")
        with open(os.path.join(OUT, cid + '.txt'), 'w', encoding='utf8', newline='\n') as f:
            f.write(f'# {cid}: decode of transcription/{cid}.txt by check.py. UPPER CASE = given by the key; '
                    '[x123] / [NN:] = code not in the key; ? = letter number not in key_letters.tsv. '
                    'Clear text is the model transcription, not proofread in full.\n')
            f.write('## Key B (key A plus the glosses in ../transcription/tx and ../evidence/ext2/hits.tsv)\n')
            f.write('\n'.join(db) + f"\n# {sb['n']} cipher tokens: {sb['ok']} full, {sb['part']} partly, {sb['none']} not in the key\n\n")
            f.write('## Key A (../key tables with ../key/corrections.tsv)\n')
            f.write('\n'.join(da) + f"\n# {sa['n']} cipher tokens: {sa['ok']} full, {sa['part']} partly, {sa['none']} not in the key\n")

    six = ('248_p190R', '248_p238R', '248_p239L', '249_p118R', '249_p218R', '250_p086L')
    st6 = collections.Counter()
    for cid in six:
        st6.update(decode_lines(crops[cid], B)[1])
    print(f"   the six pages with readings: {st6['n']} cipher tokens, key B full {st6['ok']}, "
          f"not fully decoded {st6['n'] - st6['ok']} ({100 * (st6['n'] - st6['ok']) / st6['n']:.1f}%)")

    # 4. control T
    corpus = []
    for lines in crops.values():
        corpus += clear_text(lines)
    corpus += clear_text(read_tx(os.path.join(T, 'transcription', 'june1676_tx.txt')))
    lm = NGram('  '.join(corpus) + '  ' + gloss_text())
    print(f'\n4. CONTROL T: mean log-probability per character of the key-B decoded runs, character 5-gram trained on clear text only'
          f'\n   (clear passages of these crops and of june1676_tx.txt, and the glosses in ../transcription/tx; {lm.size} characters).'
          f'\n   {NSHUF} shuffles per column, seed {SEED}; a shuffle permutes the values inside a table. Count = shuffles scoring >= the real key.')
    print(f"   {'crop':11s} {'chars':>5s} {'real':>7s} {'shuf mean':>9s} {'shuf max':>8s}  {'whole key':>9s} {'codes only':>10s} {'letters only':>12s}")
    rng = random.Random(SEED)
    for cid, lines in crops.items():
        real, nch = score(lm, lines, B)
        res = {}
        for name, tabs in (('all', 'LWC'), ('codes', 'WC'), ('letters', 'L')):
            xs = [score(lm, lines, shuffled(B, rng, tabs))[0] for _ in range(NSHUF)]
            xs = [x for x in xs if not math.isnan(x)]
            res[name] = (sum(xs) / len(xs) if xs else float('nan'), max(xs) if xs else float('nan'),
                         sum(x >= real for x in xs), len(xs))
        m, mx = res['all'][0], res['all'][1]
        print(f"   {cid:11s} {nch:5d} {real:7.3f} {m:9.3f} {mx:8.3f}  "
              f"{res['all'][2]:>5d}/{res['all'][3]:<3d} {res['codes'][2]:>6d}/{res['codes'][3]:<3d} {res['letters'][2]:>8d}/{res['letters'][3]:<3d}")

    # 5. letter numbers absent from the table
    print('\n5. LETTER NUMBERS NOT IN key_letters.tsv, in the eye-checked crops (spelled groups decoded with key A)')
    seen = collections.defaultdict(list)
    for cid in ('248_p190R', '248_p238R', '248_p239L', '249_p118R', '249_p218R', '250_p086L'):
        for l in merge(crops[cid]):
            for t in TOK.findall(l):
                if kind(t) == 'seq':
                    nums = seq_nums(t)
                    for n in nums:
                        if n not in A['L']:
                            seen[n].append(f"{cid} {{{','.join(nums)}}} = {''.join(A['L'].get(x, '?') for x in nums)}")
    for n in sorted(seen, key=int):
        print(f'   {n:>3s}: ' + '; '.join(seen[n]))

    # 6. open codes
    print('\n6. CODES AND COLON WORDS NOT IN KEY B, per crop (in order of occurrence)')
    for cid, lines in crops.items():
        miss = [t for l in merge(lines) for t in TOK.findall(l) if kind(t) in ('code', 'word') and decode(t, B)[1] == 'none']
        print(f"   {cid:11s} {len(miss):3d}: {' '.join(miss)}")


if __name__ == '__main__':
    main()
