"""b13: clean-sentence share of the reading body only (between '## Reading' and the next '## ' heading).

    python b05_score.py targets/schenck1706/reading/R7486_reading.md [...]
    V=1  list the sentences that are not clean, with their holes
    N=1  supplementary figure: Arabic numerals of the clear text (not bracketed codes) counted as words
    E=1  supplementary figure for Elizabethan English: common old spellings mapped to modern ones before scoring
         (ys is, yt it, yf if, yn in, hys his, yow you ...; the map is ENMAP below); the plain figure is the one used
"""
import os, sys, pathlib, re
ROOT = pathlib.Path(__file__).resolve().parents[2]
sys.path.insert(0, str(ROOT / 'docs')); sys.path.insert(0, str(ROOT))
import _check_reading as cr

LANG = os.environ.get('LANG_', 'es')
ENMAP = dict(w.split(':') for w in (
    'ys:is yt:it yf:if yn:in hys:his hym:him yow:you yowr:your theym:them owt:out dowt:doubt wynde:wind wylle:will '
    'wyll:will muste:must myght:might begyn:begin delyver:deliver doo:do see:sea lande:land boothe:both ony:any '
    'mony:many wekes:weeks boottes:boats drawe:draw bestowe:bestow chaunges:charges hether:hither usuall:usual '
    'termes:terms saufgarde:safeguard subiect:subject subiects:subjects sycke:sick doynge:doing satisfyed:satisfied '
    'proceedinges:proceedings rendevous:rendezvous forwarde:forward openning:opening retourne:return cumfort:comfort '
    'kepe:keep meanes:means commyt:commit allmyghtye:almighty frend:friend wyth:with whych:which sayde:said '
    'beyng:being nowe:now hath:has doth:does lettres:letters knowen:known yeare:year goyng:going praye:pray '
    'forgett:forget maye:may sayles:sails soldiers:soldiers latte:late tyme:time thys:this lyke:like haue:have '
    'gyve:give dayly:daily encrease:increase myne:mine shalbe:shall sayeth:saith').split())
NUM = re.compile(r'(?<![\[\d<])\b\d+\b(?![\]\d>])')

for f in sys.argv[1:]:
    t = pathlib.Path(f).read_text(encoding='utf8')
    m = re.search(r'^## Reading[^\n]*\n(.*?)(?=^## |\Z)', t, re.S | re.M)
    body = m.group(1)
    if os.environ.get('N'):
        body = NUM.sub('{n}', body)
    if os.environ.get('E'):
        body = re.sub(r"[A-Za-z]+", lambda m: ENMAP.get(m.group(0).lower(), m.group(0)), body)
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
