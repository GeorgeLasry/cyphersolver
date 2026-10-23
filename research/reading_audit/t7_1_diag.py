"""v7 list 1: show the unknown words of each failing sentence of a reading (v2_score holes applied).
    python research/reading_audit/t7_1_diag.py <file> <lang>"""
import sys, pathlib
sys.path.insert(0, str(pathlib.Path(__file__).parent))
import v2_score as v
cr = v.cr
f, lang = sys.argv[1], sys.argv[2]
b = v.holes(v.body_of(pathlib.Path(f).read_text(encoding='utf8')))
lex = cr.lexicon(lang)
text = cr.CODE.sub(' CODEWORD ', cr.clean_text(b))
import re
for s in cr.sentences(re.sub(r'\|[^|\n]*\|', ' [?] ', text)):
    ws = [(w, g) for tok in s for w, g in cr.words_of(tok)]
    unk = [w if not g else '[?]' for w, g in ws if g or (w not in lex and w != 'codeword')]
    if len(unk) > max(1, len(ws) // 10): print(len(ws), unk)
