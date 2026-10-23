"""b06: list the sentences of a reading body that _check_reading.py counts as not clean, with their hole words.
    python research/reading_audit/b06_diag.py <body-file> [lang]
"""
import os, re, sys
sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__)), '..', '..', 'docs'))
import _check_reading as C
raw = open(sys.argv[1], encoding='utf-8').read(); lang = sys.argv[2] if len(sys.argv) > 2 else 'de'
text = C.CODE.sub(' CODEWORD ', C.clean_text(raw)); lex = C.lexicon(lang)
others = [C.lexicon(lg) for lg in C.languages() if lg != lang]
from collections import Counter
miss = Counter()
for s in C.sentences(text):
    ws = [(w, g) for tok in s for w, g in C.words_of(tok)]
    known = lambda lx: sum(1 for w, g in ws if not g and (w in lx or w == 'codeword'))
    best = max([lex] + others, key=known) if known(lex) < len(ws) else lex
    bad = [w for w, g in ws if g or not (w in best or w == 'codeword')]
    if len(bad) > max(1, len(ws) // 10):
        miss.update(w for w, g in ws if not g and w not in best and w != 'codeword')
        print('X', ' '.join(s)[:150], '\n    ->', bad)
print('\nunknown words:', miss.most_common(60))
