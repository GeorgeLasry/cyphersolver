"""b14: clean-sentence share of the reading body only (between '## Reading' and the next '## ' heading).

    python b05_score.py targets/schenck1706/reading/R7486_reading.md [...]
    V=1  list the sentences that are not clean, with their holes
    N=1  supplementary figure: Arabic numerals of the clear text (not bracketed codes) counted as words
"""
import os, sys, pathlib, re
ROOT = pathlib.Path(__file__).resolve().parents[2]
sys.path.insert(0, str(ROOT / 'docs')); sys.path.insert(0, str(ROOT))
import _check_reading as cr

LANG = os.environ.get('LANG_', 'es')
NUM = re.compile(r'(?<![\[\d<])\b\d+\b(?![\]\d>])')

for f in sys.argv[1:]:
    t = pathlib.Path(f).read_text(encoding='utf8')
    m = re.search(r'^## Reading[^\n]*\n(.*?)(?=^## |\Z)', t, re.S | re.M)
    body = m.group(1)
    if os.environ.get('N'):
        body = NUM.sub('{n}', body)
    r = cr.score_text(body, LANG)
    print(f, r['clean_share'], '%d/%d' % (r['clean'], r['sentences']), 'holes', r['hole_rate'], 'words', r['words'])
    if os.environ.get('V'):
        lex = cr.lexicon(LANG)
        text = cr.CODE.sub(' CODEWORD ', cr.clean_text(body))
        for s in cr.sentences(text):
            ws = [(w, g) for tok in s for w, g in cr.words_of(tok)]
            bad = [w for w, g in ws if g or (w not in lex and w != 'codeword')]
            if len(bad) > max(1, len(ws) // 10):
                print('  X', len(ws), bad)
