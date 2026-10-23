"""b16: list the words _check_reading counts as holes in a reading (lexicon misses and explicit gaps), with counts.
python b16_holes.py <reading> [lang]"""
import sys, pathlib, collections, re
sys.path.insert(0, str(pathlib.Path(__file__).resolve().parents[2] / 'docs'))
import _check_reading as C
raw = open(sys.argv[1], encoding='utf-8').read(); lang = sys.argv[2] if len(sys.argv) > 2 else 'es'
text = C.CODE.sub(' CODEWORD ', C.clean_text(raw)); lex = C.lexicon(lang)
miss, gaps = collections.Counter(), 0
for s in C.sentences(text):
    for tok in s:
        for w, gap in C.words_of(tok):
            if gap: gaps += 1
            elif w != 'codeword' and w not in lex: miss[w] += 1
sys.stdout.reconfigure(encoding='utf-8')
print('gaps', gaps, 'lexicon misses', sum(miss.values()))
print(' '.join(f'{w}:{n}' if n > 1 else w for w, n in miss.most_common()))
