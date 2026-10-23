"""v3 verify (b), matignon1586: how much freedom the Cipher-1 letter sets leave a hand-built reading.

    python research/reading_audit/v3b_matignon_sets.py [doc ...]

For each document, the reading is aligned letter by letter with the corrected figures and the leaf key
(verify1_matignon_align.align). Reported:
  carried     share of reading letters the figures carry (letter in the figure's set);
  single      share of carried letters resting on a figure with one value only;
  non-first   share of carried letters resting on a value other than the first in the figure's set (the key's
              principal value), i.e. where the reader chose between alternatives;
  bits        mean log2(set size) over the letter figures of the leaf: how many bits of choice a figure leaves.
Controls, same figures and key: (a) the reading's own words in a shuffled order (seeded); (b) another Cipher-1 leaf's
reading that follows a contemporary clear copy (f. 154, Brackx), cut to the same length. A reading that the figures
really carry should sit far above both controls.
"""
import math
import random
import re
import sys
import pathlib

sys.path.insert(0, str(pathlib.Path(__file__).parent))
import verify1_matignon_align as V  # noqa: E402


def stats(r, toks, key):
    credit, at = V.align(r, toks, key)
    car = sum(1 for c in credit if c == 1)
    single = nonfirst = 0
    for i, c in enumerate(credit):
        if c != 1 or at[i] is None:
            continue
        v = [x for x in key.get(toks[at[i]], []) if x not in ('+', '')]
        if len(v) == 1:
            single += 1
        else:
            # which value carried it: the first whose letters cover position i
            first = v[0] if v else ''
            if r[i] not in first.replace('v', 'u').replace('j', 'i'):
                nonfirst += 1
    return car / max(len(r), 1), single / max(car, 1), nonfirst / max(car, 1)


def bits(toks, key):
    b = [math.log2(len([x for x in key[t] if x not in ('+', '')])) for t in toks
         if t in key and any(x not in ('+', '') for x in key[t])]
    return sum(b) / max(len(b), 1)


def control_text(n):
    s = (V.T / 'texts' / 'reading_f154.md').read_text(encoding='utf8')
    s = s[s.find('\n## '):] if '\n## ' in s else s
    w = V.reading_words(s)
    r = ''.join(x[1] for x in w)
    return (r * 3)[:n]


def run(doc):
    rf, (a, b), spec, kname = V.DOCS[doc]
    words = V.reading_words(V.section(V.T / 'texts' / rf, a, b))
    toks, _ = V.figures(spec)
    key = V.key_for(kname)
    r = ''.join(w[1] for w in words)
    c, s1, nf = stats(r, toks, key)
    ws = [w[1] for w in words]
    random.Random(1).shuffle(ws)
    cs, _, _ = stats(''.join(ws), toks, key)
    cc, _, _ = stats(control_text(len(r)), toks, key)
    print(f'{doc}: {len(toks)} figures, {len(r)} letters; carried {c:.3f} (single-value {s1:.3f}, '
          f'non-first value {nf:.3f}); bits/figure {bits(toks, key):.2f}; '
          f'controls carried: shuffled words {cs:.3f}, f.154 text {cc:.3f}')


if __name__ == '__main__':
    for d in sys.argv[1:] or ['f173', 'f196v', 'f124v', 'f143v']:
        run(d)
