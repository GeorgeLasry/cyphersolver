"""Reproduce the numbers in the WAINUT section of targets/vanreede1793/NOTES.md.

Inputs (all relative to this folder):
  runs.json        116 (cipher run, clear span) pairs from the 44 letters in NA 1.01.02 inv. 6695
  letters.json     scan references of each cipher original and its registered clear copy
  code_marks.json  the code rebuilt from all 44 letters (em.fit on runs.json, 12 iterations)
  loo_marks.tsv    per-letter leave-one-letter-out scores (written by the full LOO run, see --loo)
  ../ciphertext_R1893.txt  this folder's transcription of R1893 (read only)

usage:  python3 check.py          (about 1 minute: R1893 decode, controls, crib, LOO summary,
                                   order test on three held-out letters)
        python3 check.py --loo    (also re-runs the full leave-one-letter-out, about 12 minutes)
Writes r1893_reading.tsv (one row per group). Standard library plus numpy (em.py)."""
import collections, json, math, os, random, re, statistics, sys

HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, HERE)
import em  # noqa: E402

P = lambda f: os.path.join(HERE, f)
MAP = {'~': 'm', 'v': 'v', '¨': 'd', '=': 'B', '+': 'p'}


def r1893_tokens():
    out = []
    for raw in open(P('../ciphertext_R1893.txt'), encoding='utf8').read().split():
        n = re.sub(r'\D', '', raw)
        if n:
            out.append({'n': n, 'm': ''.join(sorted(set(MAP[c] for c in raw if c in MAP))), 'raw': raw})
    return out


def lm_train(texts, n=5):
    c, ctx, V = collections.Counter(), collections.Counter(), set()
    for t in texts:
        t = '^' * (n - 1) + t
        for i in range(n - 1, len(t)):
            c[t[i - n + 1:i + 1]] += 1; ctx[t[i - n + 1:i]] += 1; V.add(t[i])
    return c, ctx, len(V), n


def lm_score(lm, s):
    c, ctx, V, n = lm
    s = '^' * (n - 1) + s
    lp = sum(math.log((c[s[i - n + 1:i + 1]] + 0.1) / (ctx[s[i - n + 1:i]] + 0.1 * V)) for i in range(n - 1, len(s)))
    return lp / max(1, len(s) - n + 1)


def text(dec):
    return ''.join(d for d in dec if d)


def order_test(name, toks, model, lm, nperm=200):
    s = lm_score(lm, text(em.decode(model, toks, em.key_marks)))
    ps = []
    for seed in range(nperm):
        t2 = toks[:]; random.Random(seed).shuffle(t2)
        ps.append(lm_score(lm, text(em.decode(model, t2, em.key_marks))))
    mu, sd = statistics.mean(ps), statistics.pstdev(ps)
    print(f'  {name}: true order {s:.3f}; permuted mean {mu:.3f} (sd {sd:.3f}), best {max(ps):.3f}; '
          f'z {(s - mu) / sd:.1f}; rank {sum(p >= s for p in ps)}/{nperm}', flush=True)


runs = [r for r in json.load(open(P('runs.json'), encoding='utf8')) if r['groups'] and r['plain']]
letters = json.load(open(P('letters.json'), encoding='utf8'))
code = json.load(open(P('code_marks.json'), encoding='utf8'))
model = {'counts': code}
print(f'pairs: {len(letters)} letters, {len(runs)} runs, {sum(len(r["groups"]) for r in runs)} groups, '
      f'{sum(len(r["plain"]) for r in runs)} words; code: {len(code)} group forms, '
      f'{sum(1 for c in code.values() if sum(c.values()) >= 2)} seen at least twice')

# 1. R1893 decoded with the code from all 44 letters
T = r1893_tokens()
dec = em.decode(model, T, em.key_marks)
read = tent = unk = 0
with open(P('r1893_reading.tsv'), 'w', encoding='utf8') as f:
    f.write('i\tkey\treading\tsupport\ttotal\tstatus\n')
    for i, (t, d) in enumerate(zip(T, dec)):
        k = em.key_marks(t); c = code.get(k)
        if not c:
            unk += 1; f.write(f'{i}\t{k}\t?\t0\t0\tunknown\n'); continue
        sup, tot = c[d], sum(c.values())
        ok = sup >= 2 and sup / tot >= 0.5
        read += ok; tent += not ok
        f.write(f'{i}\t{k}\t{d}\t{sup}\t{tot}\t{"read" if ok else "tentative"}\n')
print(f'R1893: {len(T)} groups; in code {len(T) - unk} ({(len(T) - unk) / len(T):.3f}); read {read}, '
      f'tentative {tent}, unknown {unk}')

# 2. controls for R1893: shuffled codes and order permutation (5-gram model trained on the clear copies)
lm = lm_train([''.join(r['plain']) for r in runs])
s_true = lm_score(lm, text(dec))
keys = list(code); vals = [code[k] for k in keys]; sh = []
for seed in range(200):
    vs = vals[:]; random.Random(seed).shuffle(vs)
    sh.append(lm_score(lm, text(em.decode({'counts': dict(zip(keys, vs))}, T, em.key_marks))))
mu, sd = statistics.mean(sh), statistics.pstdev(sh)
print(f'shuffled-code control: true {s_true:.3f}; 200 shuffled codes mean {mu:.3f} (sd {sd:.3f}), best {max(sh):.3f}; '
      f'z {(s_true - mu) / sd:.1f}; rank {sum(x >= s_true for x in sh)}/200')
print('order-permutation control (same code, groups permuted):')
order_test('R1893', T, model, lm)

# 3. the Potocki crib: R1893's only cipher 3-grams shared with a training letter
seq = ['773m', '319v', '442B', '751B']
rk = [em.key_marks(t) for t in T]
grams = lambda ks: {tuple(ks[i:i + 3]) for i in range(len(ks) - 2)}
shared = collections.defaultdict(set)
for r in runs:
    for g in grams([em.key_marks(t) for t in r['groups']]) & grams(rk):
        shared[g].add(r['letter'])
print('cipher 3-grams shared by R1893 and the training runs:', {' '.join(g): sorted(v) for g, v in shared.items()})
for r in runs:
    ks = [em.key_marks(t) for t in r['groups']]
    for i in range(len(ks) - 3):
        if ks[i:i + 4] == seq:
            ctx = ' '.join(ks[max(0, i - 3):i + 4])
            m = em.Run(r); sg, _ = m.viterbi(ks, code, em._Tot(code))
            print(f'  {r["letter"]} run {r["run"]}: {ctx} -> {" ".join(sg[max(0, i - 3):i + 4])}')
i = next(i for i in range(len(rk) - 3) if rk[i:i + 4] == seq)
print(f'  R1893 groups {i}-{i + 3}: {" ".join(t["raw"] for t in T[i:i + 4])} -> {" ".join(d or "?" for d in dec[i:i + 4])}')

# 4. leave-one-letter-out summary (loo_marks.tsv), weighted by groups and by plaintext length
plen = collections.Counter(); ng = collections.Counter()
for r in runs:
    plen[r['letter']] += len(''.join(r['plain'])); ng[r['letter']] += len(r['groups'])
rows = [l.rstrip('\n').split('\t') for l in open(P('loo_marks.tsv'), encoding='utf8')][1:]
G = sum(int(r[1]) for r in rows); Lsum = sum(plen[r[0]] for r in rows)
wg = lambda j: sum(float(r[j]) * int(r[1]) for r in rows) / G
wl = lambda j: sum(float(r[j]) * plen[r[0]] for r in rows) / Lsum
print(f'LOO ({len(rows)} letters, {G} groups): coverage {wg(2):.3f}; exactly right {wg(3):.3f} '
      f'(shuffled {wg(4):.3f}, rotated {wg(5):.3f}); char similarity {wl(6):.3f} (shuffled {wl(7):.3f}, rotated {wl(8):.3f})')
print(f'  letters beating both controls on char similarity: {sum(float(r[6]) > max(float(r[7]), float(r[8])) for r in rows)}'
      f'/{len(rows)}; weakest {min(rows, key=lambda r: float(r[6]))[0]} ({min(float(r[6]) for r in rows):.3f})')

# 5. order test on three held-out letters (code and language model built without the letter)
print('order-permutation control on held-out letters:')
for L in ['1793-03-12PS', '1792-01-21PS', '1793-06-29']:
    train = [r for r in runs if r['letter'] != L]
    mx = em.fit(train, em.key_marks, iters=12)
    order_test(L, [t for r in runs if r['letter'] == L for t in r['groups']], mx,
               lm_train([''.join(r['plain']) for r in train]))

if '--loo' in sys.argv:
    print('full leave-one-letter-out re-run:')
    for L in sorted(set(r['letter'] for r in runs)):
        mx = em.fit([r for r in runs if r['letter'] != L], em.key_marks, iters=10)
        n = cov = ok = 0; ch = ln = 0.0
        for r in [r for r in runs if r['letter'] == L]:
            run = em.Run(r); ks = [em.key_marks(t) for t in r['groups']]
            seg, _ = run.viterbi(ks, mx['counts'], em._Tot(mx['counts']))
            d = em.decode(mx, r['groups'], em.key_marks)
            n += len(ks); cov += sum(x is not None for x in d); ok += sum(a == b for a, b in zip(d, seg))
            ch += em.score(d, run.s) * len(run.s); ln += len(run.s)
        print(f'  {L}\t{n}\t{cov / n:.3f}\t{ok / n:.3f}\t{ch / ln:.3f}', flush=True)
