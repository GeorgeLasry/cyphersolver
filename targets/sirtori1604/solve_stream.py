"""Ciphertext-only tests on the Gomez Hernandez (2012) sign stream of BNE Mss/994 ff. 85-86v.

The stream has no word divisions and none of the dots, commas or arcs (see NOTES.md). Two readings of the
stream are tested: raw (27 signs) and with F3/B3 merged into single signs (the '3' is the tall stroke that
stands over F and B, 84 of 85 times). Each is attacked as a many-to-one substitution (homophones allowed)
scored on a letters-only order-4 model, in two plaintext forms:

  full      the language as written (es-golden-age, it-cinquecento, la)
  skeleton  the same corpus with the vowels a e i o u deleted: the hypothesis that the dots and commas
            the 2012 transcription dropped carry the vowels

Controls: a passage of the same corpus, same length, enciphered the same way (27 symbols, homophones for
the commonest letters), must be recovered before any output on the real stream means anything.

    python targets/sirtori1604/solve_stream.py            # all runs, writes results/stream_runs.json
"""
import os, re, sys, json, random, math
import numpy as np
HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, os.path.join(HERE, '..', '..'))
from lang import lm, corpora

STREAM = open(os.path.join(HERE, 'transcription', 'gomez2012_stream.txt')).read().split()
STREAM = ''.join(STREAM)
MODELS = {'es': 'es-golden-age', 'it': 'it-cinquecento', 'la': 'la'}
CACHE = os.path.join(HERE, 'results', 'lmcache')


ROMAN = set('ivxlcdmu')   # after the 'early' norm v is u


def corpus(lang):
    """Letters-only corpus with Roman numerals dropped (they make 'iiii' the best decrypt)."""
    spec = lm.registry()[0][MODELS[lang]]
    words = lm.norm(corpora.text(spec['sources'])[:8_000_000], spec['norm'], spaces=True).split()
    words = [w for w in words if not (set(w) <= ROMAN and re.search('[ixu]{2}|[xlcdm]{2}|^x', w))]
    return ''.join(words), spec['norm']


def model(lang, form):
    os.makedirs(CACHE, exist_ok=True)
    path = os.path.join(CACHE, f'{lang}-{form}.o4')
    alpha = lm.alphabet(lm.registry()[0][MODELS[lang]]['norm'], spaces=False)
    if form == 'skeleton':
        alpha = ''.join(c for c in alpha if c not in 'aeiou')
    if os.path.exists(path + '.json'):
        return lm.DenseLM(np.load(path + '.npy'), 4, alpha)
    text, _ = corpus(lang)
    if form == 'skeleton':
        text = ''.join(c for c in text if c not in 'aeiou')
    m = lm.DenseLM.build(text, 4, alpha)
    m.save(path)
    return m


def unigram(lang, form):
    text, _ = corpus(lang)
    if form == 'skeleton':
        text = ''.join(c for c in text if c not in 'aeiou')
    from collections import Counter
    c = Counter(text[:2_000_000])
    return [ch for ch, _ in c.most_common()], c


def initial_key(ct, letters, counts, m):
    """Give each cipher symbol a letter so that letter totals follow the language's frequencies."""
    from collections import Counter
    syms = [s for s, _ in Counter(ct).most_common()]
    tot = sum(counts.values())
    want = {ch: counts[ch] / tot * len(ct) for ch in letters}
    have = {ch: 0.0 for ch in letters}
    key = {}
    cnt = Counter(ct)
    for s in syms:                       # greedy: commonest symbol to the letter with most unmet frequency
        ch = max(letters, key=lambda x: want[x] - have[x])
        key[s] = m.index[ch]
        have[ch] += cnt[s]
    return key


def anneal(ct, m, letters, counts, iters=40000, restarts=10, seed=0):
    """Many-to-one substitution from a frequency-matched start: swaps, plus reassignment of one symbol to any
    letter (30% of moves), so the number of homophones per letter is free."""
    rng = random.Random(seed)
    syms = sorted(set(ct))
    si = {s: i for i, s in enumerate(syms)}
    c = np.array([si[s] for s in ct])
    k0 = initial_key(ct, letters, counts, m)
    tot = sum(counts.values())
    cap = np.array([2 * counts.get(ch, 0) / tot + 0.02 for ch in m.alpha]) * len(ct)  # no letter above 2x its share
    w = np.bincount(c, minlength=len(syms))

    def ok(key):
        return (np.bincount(key, weights=w, minlength=m.A) <= cap).all()

    base = np.array([k0[s] for s in syms])
    # spare letters a symbol can be re-assigned to (letters not in the multiset), for the rare letters
    best_all = (-1e18, None)
    for r in range(restarts):
        key = base.copy()
        if r:                             # restart 0 starts from the frequency-matched key itself
            rng.shuffle(key)
        cur = m.score_idx(key[c])
        best = (cur, key.copy())
        for it in range(iters):
            T = 1.5 * (1 - it / iters) + 0.02
            i = rng.randrange(len(syms))
            if rng.random() < 0.3:        # reassign one symbol (homophone counts are not known in advance)
                j, old = None, key[i]
                key[i] = rng.randrange(m.A)
            else:
                j = rng.randrange(len(syms))
                if key[i] == key[j]:
                    continue
                key[i], key[j] = key[j], key[i]
            s = m.score_idx(key[c]) if ok(key) else -1e18
            if s >= cur or rng.random() < math.exp((s - cur) / T):
                cur = s
                if s > best[0]:
                    best = (s, key.copy())
            elif j is None:
                key[i] = old
            else:
                key[i], key[j] = key[j], key[i]
        if best[0] > best_all[0]:
            best_all = best
    s, key = best_all
    pt = ''.join(m.alpha[key[si[x]]] for x in ct)
    return s / max(1, len(ct) - 3), pt, {x: m.alpha[key[si[x]]] for x in syms}


def control_ct(lang, form, n, nsym, seed=1):
    text, _ = corpus(lang)
    rng = random.Random(seed)
    start = rng.randrange(len(text) // 2, len(text) - 20000)
    t = text[start:start + 3 * n]
    if form == 'skeleton':
        t = ''.join(ch for ch in t if ch not in 'aeiou')
    t = t[:n]
    letters = sorted(set(t), key=lambda ch: -t.count(ch))
    # one symbol per letter, extra symbols as homophones of the commonest letters, up to nsym
    hom = {ch: [ch.upper()] for ch in letters}
    extra = nsym - len(letters)
    i = 0
    while extra > 0 and letters:
        hom[letters[i % 4]].append(f'{letters[i % 4]}{i}'); i += 1; extra -= 1
    ct = [rng.choice(hom[ch]) for ch in t]
    return t, ct


def accuracy(a, b):
    return sum(x == y for x, y in zip(a, b)) / len(a)


def main():
    raw = list(STREAM)
    merged, i = [], 0
    while i < len(STREAM):
        if STREAM[i] in 'FB' and i + 1 < len(STREAM) and STREAM[i + 1] == '3':
            merged.append(STREAM[i] + '3'); i += 2
        else:
            merged.append(STREAM[i]); i += 1
    out = {'stream_len_raw': len(raw), 'stream_len_merged': len(merged), 'runs': []}
    for lang in ('es', 'it', 'la'):
        for form in ('full', 'skeleton'):
            m = model(lang, form)
            letters, counts = unigram(lang, form)
            for name, ct in (('raw', raw), ('merged', merged)):
                nsym = len(set(ct))
                truth, cct = control_ct(lang, form, len(ct), nsym)
                cs, cpt, _ = anneal(cct, m, letters, counts)
                rs, rpt, rkey = anneal(ct, m, letters, counts)
                row = dict(lang=lang, form=form, stream=name, n=len(ct), nsym=nsym,
                           control_acc=round(accuracy(cpt, truth), 3), control_score=round(cs, 3),
                           real_score=round(rs, 3), real_pt=rpt, key=rkey,
                           control_truth=truth[:80], control_pt=cpt[:80])
                print(lang, form, name, 'control acc', row['control_acc'], 'ctl', row['control_score'],
                      'real', row['real_score'], rpt[:70], flush=True)
                out['runs'].append(row)
    os.makedirs(os.path.join(HERE, 'results'), exist_ok=True)
    json.dump(out, open(os.path.join(HERE, 'results', 'stream_runs.json'), 'w'), indent=1, ensure_ascii=False)


if __name__ == '__main__':
    main()
