"""b15: score a reading body with docs/_check_reading.py, once with the committed 'hu' word list and once with that list
plus a period word list counted from 1640s Hungarian letters in print (Szilagyi, A linzi beke okirattara 1885;
Erdely es az eszakkeleti haboru I; Lukinich's Bethlen correspondence 1907), to show how far the modern list misses
17th-c. spelling. Controls: genuine printed 1645 letters from the same edition.

    python research/reading_audit/b15_score.py <period_counts.json> <file> [<file> ...]
"""
import collections, json, pathlib, sys
ROOT = pathlib.Path(__file__).resolve().parent.parent.parent
sys.path[:0] = [str(ROOT / 'docs'), str(ROOT)]
import _check_reading as cr

counts = collections.Counter(json.load(open(sys.argv[1], encoding='utf-8')))
files = sys.argv[2:]
base = {f: cr.score_text(open(f, encoding='utf-8').read(), 'hu') for f in files}
for w, n in cr.lexicon('hu').items(): counts[w] += n
lex = {w: n for w, n in counts.items() if n >= cr.LEX_MIN_COUNT and len(w) >= 3}
lex.update({w: counts[w] for w in [w for w, _ in counts.most_common() if len(w) <= 2][:cr.SHORT_KEEP]})
cr._LEX['hu'] = lex
for f in files:
    p = cr.score_text(open(f, encoding='utf-8').read(), 'hu')
    print(f'{pathlib.Path(f).name}: committed list {base[f]["clean_share"]} (holes {base[f]["hole_rate"]}); '
          f'with period list {p["clean_share"]} (holes {p["hole_rate"]}), {p["sentences"]} sentences')
