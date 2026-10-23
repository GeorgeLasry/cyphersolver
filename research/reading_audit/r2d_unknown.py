"""r2d (23 Oct 2026): list the words of a reading body that the plain score counts as holes (word list misses).

    python research/reading_audit/r2d_unknown.py <reading.md> [lang]
"""
import collections, pathlib, re, sys
ROOT = pathlib.Path(__file__).resolve().parents[2]
sys.path.insert(0, str(ROOT / 'docs')); sys.path.insert(0, str(ROOT)); sys.path.insert(0, str(ROOT / 'research' / 'reading_audit'))
import _check_reading as cr
from v2_score import body_of, holes

f, lang = sys.argv[1], (sys.argv[2] if len(sys.argv) > 2 else 'it')
t = cr.clean_text(holes(body_of(pathlib.Path(f).read_text(encoding='utf8'))))
lex = cr.lexicon(lang)
c = collections.Counter()
for s in cr.sentences(cr.CODE.sub(' CODEWORD ', t)):
    for tok in s:
        for w, gap in cr.words_of(tok):
            if not gap and w != 'codeword' and w not in lex: c[w] += 1
print(' '.join(f'{w}:{n}' for w, n in c.most_common()))
