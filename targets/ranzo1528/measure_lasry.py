"""Per-letter read fractions of George Lasry's Ranzo key (lasry/alignment.tsv), and, given Rosson's folder,
Rosson's key applied to the same (Biermann) transcription and the agreement of the two keys token by token.

    python measure_lasry.py [ROSSON_FOLDER]

Lasry's statuses: 'stronger working inference', 'tentative/speculative' (value ends in ?), 'presumed null'
(numbers 1-5), 'unresolved'. Rosson's classes: sure, probable, guess, null; his rule g>214 = s, t>196 = r is applied.
Agreement: the two values equal after lower-casing, dropping ?, accents and apostrophes and collapsing doubled letters,
or one a prefix of the other of three letters or more (the keys split stems and endings differently), or a
difflib ratio of 0.75 or more (period spelling variants: lettere/littere, scribe/scrive, aviso/adviso).
Read (bar measure), Lasry's key first and Rosson's second, as George Lasry put it on 16 Oct 2026 ("my key or
Rosson's key"): a token is read when it is a presumed null, a stronger inference of Lasry's, a tentative value of
Lasry's that Rosson's key matches, or a sure/probable value of Rosson's where Lasry has none."""
import csv, collections, sys, unicodedata, pathlib, re, difflib
HERE = pathlib.Path(__file__).resolve().parent

def norm(v):
    v = unicodedata.normalize('NFD', v.lower())
    return re.sub(r'(.)\1', r'\1', ''.join(ch for ch in v if ch.isalpha()))

def agree(a, b):
    a, b = norm(a), norm(b)
    if not a or not b: return False
    if a == b: return True
    s, l = sorted((a, b), key=len)
    return (len(s) >= 3 and l.startswith(s)) or difflib.SequenceMatcher(None, a, b).ratio() >= 0.75

ros = {}
if len(sys.argv) > 1:
    for line in open(pathlib.Path(sys.argv[1]) / 'key' / 'table.tsv', encoding='utf8').read().split('\n')[1:]:
        f = line.split('\t')
        if len(f) >= 3 and f[1]: ros[f[0]] = (f[1], f[2])

def rkey(code):
    L, N = code[0], int(code[1:])
    if L == 'L': L = 'l'
    if L == 'g' and N > 214: L = 's'
    if L == 't' and N > 196: L = 'r'
    return ros.get(L + str(N)) or ros.get(code)

rows = list(csv.DictReader(open(HERE / 'lasry' / 'alignment.tsv', encoding='utf-8'), delimiter='\t'))
per = collections.defaultdict(collections.Counter)
for r in rows:
    m = r['line'].split(':')[0]; c = per[m]; st = r['status']
    c['n'] += 1; c[st] += 1
    if not ros: continue
    rv = rkey(r['code']); rc = rv[1] if rv else 'none'
    c['ros_' + rc] += 1
    if st in ('stronger working inference', 'tentative/speculative') and rc in ('sure', 'probable', 'guess'):
        c['both'] += 1
        if agree(r['reading'], rv[0]):
            c['agree'] += 1
            if st == 'tentative/speculative': c['tent_agree'] += 1
            else: c['strong_agree'] += 1
    if st == 'presumed null' and rc == 'null': c['null_agree'] += 1
    if st == 'unresolved' and rc in ('sure', 'probable'): c['ros_fills'] += 1

pct = lambda a, b: f'{a}/{b} ({100*a/b:.1f}%)'
for m in sorted(per):
    c = per[m]; n = c['n']
    null, strong, tent = c['presumed null'], c['stronger working inference'], c['tentative/speculative']
    print(f'letter {m}: {n} occurrences; null {null}, strong {strong}, tentative {tent}, unresolved {c["unresolved"]}')
    print('  Lasry valued incl. tentative + nulls:', pct(null + strong + tent, n))
    print('  Lasry strong + nulls (tentative counted unread):', pct(null + strong, n))
    if ros:
        print('  Rosson valued (sure/probable/null):', pct(c['ros_sure'] + c['ros_probable'] + c['ros_null'], n),
              '| guess', c['ros_guess'], '| none', c['ros_none'])
        print('  both keys value it:', c['both'], '| agree', pct(c['agree'], c['both']) if c['both'] else 0,
              '| strong agree', c['strong_agree'], '| tentative agree', c['tent_agree'])
        print('  Lasry strong + nulls + tentative confirmed by Rosson:', pct(null + strong + c['tent_agree'], n))
        print('  READ (bar measure): the above + Rosson sure/probable where Lasry has no value:',
              pct(null + strong + c['tent_agree'] + c['ros_fills'], n))
tot = collections.Counter()
for c in per.values(): tot.update(c)
print('fr. 2988 (letters 1+2) bar measure:', pct(sum(per[m]['presumed null'] + per[m]['stronger working inference']
      + per[m]['tent_agree'] + per[m]['ros_fills'] for m in '12'), per['1']['n'] + per['2']['n']) if ros else '')
