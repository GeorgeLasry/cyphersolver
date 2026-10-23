"""b06: score the body of a kurtz1639 reading (header comment and ## Notes cut off) with _check_reading.py's measure,
and list the sentences that are not clean with the words that count as holes.

    python research/reading_audit/b06_score.py R4625 [-v]
"""
import os, re, sys
ROOT = os.path.join(os.path.dirname(os.path.abspath(__file__)), '..', '..')
sys.path.insert(0, os.path.join(ROOT, 'docs')); sys.path.insert(0, ROOT)
import _check_reading as cr

rec = sys.argv[1]
t = open(os.path.join(ROOT, 'targets', 'kurtz1639', 'read', rec + '_reading.md'), encoding='utf-8').read()
t = re.sub(r'<!--.*?-->', ' ', t, flags=re.S).split('\n## ')[0]
t = '\n'.join(t.split('\n')[1:]) if t.lstrip().startswith('#') else t
t = re.sub(r'^\s*# .*$', '', t, flags=re.M)
r = cr.score_text(t)
print(rec, {k: r[k] for k in ('lang', 'sentences', 'clean', 'clean_share', 'words', 'hole_rate')})
if '-v' in sys.argv:
    text = cr.CODE.sub(' CODEWORD ', cr.clean_text(t))
    lexs = {lg: cr.lexicon(lg) for lg in cr.languages()}
    for s in cr.sentences(re.sub(r'\|[^|\n]*\|', ' [?] ', text)):
        ws = [(w, g) for tok in s for w, g in cr.words_of(tok)]
        best = max(lexs.values(), key=lambda lx: sum(1 for w, g in ws if not g and (w in lx or w == 'codeword')))
        bad = [w for w, g in ws if g or not (w in best or w == 'codeword')]
        if len(bad) > max(1, len(ws) // 10):
            print('  %2d/%2d  %s   || %s' % (len(bad), len(ws), ' '.join(s)[:150], ' '.join(bad)))
