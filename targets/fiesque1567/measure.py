"""Project re-measure of Harumi-Matsuba's fiesque1567 reading (issue #52), 21 Oct 2026.

Decodes every contributed transcription (contributed/data/transcription_*.txt) with the contributed key
(contributed/data/key.tsv, Tomokiyo's table + inferred values) by our own decoder, then per page:
  - signs (tokens other than the '|' separator) and signs with a value;
  - mean log-prob per character under the shared model fr-1530-despatches (order 5, no spaces), for the
    true key and for 200 keys with the single-letter values shuffled among the single-letter signs;
  - a sense measure: the decoded letter stream is segmented by dynamic programming into words of a French
    lexicon (fr-henri4 + fr-1520s-diplomatic, words seen >= 5 times, 'early' normalisation); the share of
    letters covered by lexicon words of length >= 4, plus a short list of function words, is the coverage.
    The same coverage is computed for the shuffled-key decodes as a baseline.
Coverage is a lexical screen, not a reading: it counts letters that fall in real words, whether or not the
words make the sentence the contributor gives. It is reported as the project's measure next to the
contributor's inter-model agreement.

Run: PYTHONUTF8=1 python targets/fiesque1567/measure.py > targets/fiesque1567/measure.txt
"""
import os, re, sys, glob, random, collections, math
HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, os.path.join(HERE, '..', '..'))
from lang import lm

DATA = os.path.join(HERE, 'contributed', 'data')
CORP = os.path.join(HERE, '..', '..', 'lang', 'corpora')

def load_key():
    key, src = {}, {}
    for ln in open(os.path.join(DATA, 'key.tsv'), encoding='utf-8'):
        if ln.startswith('#') or not ln.strip(): continue
        p = ln.rstrip('\n').split('\t')
        key[p[0]], src[p[0]] = p[1], p[2]
    return key, src

def load_lines(path):
    out = []
    for ln in open(path, encoding='utf-8'):
        m = re.match(r'(c[\w]+):\s*(.*)', ln)
        if m: out.append(m.group(2).split())
    return out

def norm_tok(t): return t[:-1] if t.endswith('?') and len(t) > 1 else t

def decode(lines, key):
    """letters-only stream; unknown signs -> '', code values take their first alternative."""
    out = []
    for toks in lines:
        for t in toks:
            if t == '|': continue
            v = key.get(norm_tok(t))
            if v is None or v in ('(null)', '?'): continue
            v = v.split('/')[0]
            out.append(re.sub(r'[^a-z]', '', lm.norm(v, 'early')))
    return ''.join(out)

FUNC = set('a y de le la les et en il ne se ce ie sa si ou qu que qui du au un une par pour pas mon ma ses son est ont luy vous nous sur peu bien tout dont mais plus ny sy lon dit fut ia ces aux'.split())

def lexicon():
    cnt = collections.Counter()
    for f in ('fr-henri4.txt', 'fr-1520s-diplomatic.txt'):
        txt = lm.norm(open(os.path.join(CORP, f), encoding='utf-8', errors='replace').read(), 'early')
        cnt.update(re.findall(r'[a-z]+', txt))
    return {w for w, c in cnt.items() if c >= 5 and len(w) >= 4} | FUNC

def coverage(s, lex, maxlen=16):
    n = len(s)
    best = [0] * (n + 1)          # best covered letters in s[:i]
    for i in range(1, n + 1):
        b = best[i - 1]           # letter i-1 uncovered
        for L in range(1, min(maxlen, i) + 1):
            w = s[i - L:i]
            if w in lex and best[i - L] + L > b: b = best[i - L] + L
        best[i] = b
    return best[n] / n if n else 0.0

def main():
    key, src = load_key()
    single = [k for k, v in key.items() if src[k] == 'table' and len(v) == 1 and v.isalpha()]
    m = lm.load('fr-1530-despatches', spaces=False)
    lex = lexicon()
    rng = random.Random(1567)
    files = sorted(glob.glob(os.path.join(DATA, 'transcription_*.txt')))
    tot = collections.Counter()
    print('page\tsigns\tvalued\tlm_true\tlm_shuf_best\tlm_shuf_mean\tcov_true\tcov_shuf_mean\tcov_shuf_max')
    for f in files:
        page = os.path.basename(f)[len('transcription_'):-4]
        lines = load_lines(f)
        toks = [norm_tok(t) for l in lines for t in l if t != '|']
        valued = sum(1 for t in toks if t in key and key[t] != '?')
        s = decode(lines, key)
        lt = m.per_char(s); ct = coverage(s, lex)
        lsh, csh = [], []
        for i in range(200):
            vals = [key[k] for k in single]; rng.shuffle(vals)
            k2 = dict(key); k2.update(zip(single, vals))
            s2 = decode(lines, k2)
            lsh.append(m.per_char(s2))
            if i < 20: csh.append(coverage(s2, lex))
        print(f'{page}\t{len(toks)}\t{valued}\t{lt:.3f}\t{max(lsh):.3f}\t{sum(lsh)/len(lsh):.3f}\t{ct:.3f}\t{sum(csh)/len(csh):.3f}\t{max(csh):.3f}')
        tot['signs'] += len(toks); tot['valued'] += valued
        tot['letters'] += len(s); tot['cov'] += ct * len(s); tot['covsh'] += (sum(csh) / len(csh)) * len(s)
        tot['beaten'] += sum(1 for x in lsh if x >= lt)
    print(f"# total signs {tot['signs']}, valued {tot['valued']} ({tot['valued']/tot['signs']:.1%})")
    print(f"# shuffled keys scoring >= true key (LM): {tot['beaten']} of {200*len(files)}")
    print(f"# lexical coverage, letter-weighted: true {tot['cov']/tot['letters']:.3f}, shuffled-key baseline {tot['covsh']/tot['letters']:.3f}")
    print(f"# letters decoded {tot['letters']}")
    # reference: clean French with the spaces removed, from fr-gutenberg (not in the lexicon)
    ref = re.sub(r'[^a-z]', '', lm.norm(open(os.path.join(CORP, 'fr-gutenberg.txt'), encoding='utf-8',
                 errors='replace').read()[2000000:2040000], 'early'))
    chunks = [ref[i:i + 800] for i in range(0, 8000, 800)]
    print(f"# reference, ten 800-letter stretches of fr-gutenberg (clean French, spaces removed): "
          f"LM {sum(m.per_char(c) for c in chunks)/10:.3f}, coverage {sum(coverage(c, lex) for c in chunks)/10:.3f}")

if __name__ == '__main__':
    main()
