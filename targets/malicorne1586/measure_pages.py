"""Per-page measure of Brackx's raw aligned decodes (issue #92): signs, letters, letters on multi-valued labels,
unvalued signs, and the share of decoded letters covered by French lexicon words of four letters or more (best
segmentation by dynamic programming, dividers ignored, u/v and i/j merged), against the same letters shuffled (five
shuffles, min-max). Short words are left out because with them any letter string is almost fully covered.

    python targets/malicorne1586/measure_pages.py
"""
import gzip, json, pathlib, random, re

HERE = pathlib.Path(__file__).resolve().parent
ROOT = HERE.parents[1]
PAGES = ['aligned_f162r.txt', 'aligned_f163r.txt', 'aligned_f162v.md', 'aligned_c171.md', 'aligned_c172l.md',
         'aligned_c172r.md']


def key():
    multi = set()
    for l in (HERE / 'brackx2026' / 'key_r2.txt').read_text(encoding='utf8').splitlines():
        if '=' in l and not l.lstrip().startswith('#'):
            lab, val = l.split('=', 1)
            if '/' in val: multi.add(lab.strip())
    return multi


def norm(w):
    return w.replace('v', 'u').replace('j', 'i')


def lexicon():
    d = json.load(gzip.open(ROOT / 'lang' / 'lexicons' / 'fr.json.gz'))
    return {norm(w) for w in d if len(w) >= 4}


def covered(s, lex, maxlen=16):
    """Letters of s covered by lexicon words, best segmentation."""
    best = [0] * (len(s) + 1)
    for i in range(1, len(s) + 1):
        best[i] = best[i - 1]
        for j in range(max(0, i - maxlen), i):
            if s[j:i] in lex: best[i] = max(best[i], best[j] + i - j)
    return best[-1]


def page(path, multi, lex):
    signs = letters = multi_letters = unvalued = 0
    text = ''
    for l in path.read_text(encoding='utf8').splitlines():
        m = re.match(r'\s*V:\s*(.*)', l)
        if not m: continue
        for tok in m.group(1).split():
            if '=' not in tok: continue
            lab, val = tok.split('=', 1)
            if lab in ('|', '='): continue
            signs += 1
            if val.startswith('['): unvalued += 1; text += '#'; continue
            if val == 'null': continue
            v = re.sub(r'[^a-z]', '', val.lower())
            letters += len(v); text += v
            if lab in multi: multi_letters += len(v)
    runs = [norm(r) for r in text.split('#')]
    cov = sum(covered(r, lex) for r in runs)
    shuf = []
    for k in range(5):
        rnd = random.Random(k)
        letters_all = list(''.join(runs)); rnd.shuffle(letters_all)
        shuf.append(covered(''.join(letters_all), lex))
    return signs, letters, multi_letters, unvalued, cov, min(shuf), max(shuf)


if __name__ == '__main__':
    multi, lex = key(), lexicon()
    print('page\tsigns\tletters\tmulti-valued letters\tunvalued signs\tlexicon coverage\tshuffled')
    for p in PAGES:
        s, n, mv, u, c, lo, hi = page(HERE / 'brackx2026' / p, multi, lex)
        print(f'{p}\t{s}\t{n}\t{mv} ({mv / n:.1%})\t{u}\t{c / n:.1%}\t{lo / n:.1%}-{hi / n:.1%}')
