"""b18 (copy of b17_score.py): clean-sentence share of the reading body only (between '## Reading' and the next '## ' heading).

    python b05_score.py targets/schenck1706/reading/R7486_reading.md [...]
    V=1  list the sentences that are not clean, with their holes
    N=1  supplementary figure: Arabic numerals of the clear text (not bracketed codes) counted as words
    HOLES=1  supplementary figure: only explicit holes ([...], [?word], [889]) count; every other word is taken as known
    EXTRA=<dir>  supplementary figure: add to the language's word list every word seen 3+ times in <dir>/*.txt (b17: a
         17th-century Dutch corpus, Vondel and Cats from Project Gutenberg, for the battier1686 letters; the checker's own
         nl list is modern Gutenberg Dutch). The figure without EXTRA is the checker's.
"""
import os, sys, pathlib, re
ROOT = pathlib.Path(__file__).resolve().parents[2]
sys.path.insert(0, str(ROOT / 'docs')); sys.path.insert(0, str(ROOT))
import _check_reading as cr

LANG = os.environ.get('LANG_', 'es')
if os.environ.get('EXTRA'):
    import collections, glob
    from lang import lm as _lm
    _c = collections.Counter()
    for _f in glob.glob(os.path.join(os.environ['EXTRA'], '*.txt')):
        for _line in open(_f, encoding='utf-8', errors='ignore'):
            _c.update(_lm.norm(_line, 'early').split())
    _lex = cr.lexicon(LANG)
    _lex.update({w: n for w, n in _c.items() if n >= 3 and len(w) >= 3 and w not in _lex})
NUM = re.compile(r'(?<![\[\d<])\b\d+\b(?![\]\d>])')

for f in sys.argv[1:]:
    t = pathlib.Path(f).read_text(encoding='utf8')
    m = re.search(r'^## Reading[^\n]*\n(.*?)(?=^## |\Z)', t, re.S | re.M)
    body = m.group(1)
    if os.environ.get('N'):
        body = NUM.sub('{n}', body)
    if os.environ.get('HOLES'):
        class _All(dict):
            def __contains__(self, k): return True
        cr._LEX[LANG] = _All()
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
