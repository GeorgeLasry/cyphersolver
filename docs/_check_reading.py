"""Can the published decryption be read as sentences? (George Lasry, 22 Oct 2026, on matignon1586)

"The requirement should be that the LLM can build coherent sentences - that can later be translated to English ...
It is OK to have a few holes, but not holes in almost every sentence."

A token-run measure (measure.py: a run of corpus words counts as sense) lets a decode through when it is short
real words strung together ("la que le estoit"), so this check works on sentences. For every decryption file listed
in profile.json outcome.texts:

  * lines that are mostly one- and two-character tokens are cipher figures and are skipped, as are comment lines;
  * an unspaced decode is cut into words first (Viterbi over the language's word list);
  * the text is cut into sentences (at . ; : ! ? and blank lines; a stretch of more than 24 words with no stop is
    cut into 12-word windows, which is what a raw decode with no punctuation gets);
  * a word is a hole when it is an explicit gap ([...], [?], [nn], |...|, <...>, ?, a bare number) or when the
    period word list of the text's language does not know it (one- and two-letter words count only if among the
    language's 40 commonest). A resolved code word ([SUA MAESTA], {Bassa}) is not a hole;
  * a sentence is clean when at most one word in ten is a hole (one hole for a sentence of up to 19 words);
  * clean share = clean sentences / sentences. The language is the one whose word list covers the text best. Word
    lists are built from the corpora in lang/, so the check is the same for every language. Texts not in the Latin
    alphabet (Chinese, Japanese ...) are reported 'not scored' and need a reader.

It also reports the shape of the file: 'decode' when it is mostly upper case or carries the |...| marks of a raw
machine decode, 'unspaced' when its words run together, 'reading' otherwise; and whether the entry has an English
translation (outcome.texts[].translation).

    python docs/_check_reading.py <folder>          one target, per file
    python docs/_check_reading.py --audit [--csv F] every reading, worst first
    python docs/_check_reading.py --file PATH       one file
    python docs/_check_reading.py --build-lexicons  rebuild lang/lexicons/ from the corpora in lang/

The thresholds (READABLE, MARGINAL) are calibrated in research/reading_audit/README.md.
"""
import collections, csv, glob, json, math, os, pathlib, re, sys, unicodedata

ROOT = pathlib.Path(__file__).resolve().parent.parent
sys.path.insert(0, str(ROOT))
from lang import lm  # noqa: E402

READABLE = 0.70      # clean share at or above: sentences with scattered holes
MARGINAL = 0.45      # below: holes in most sentences, not a reading
LEX_MIN_COUNT = 3
SHORT_KEEP = 40      # the commonest one- and two-letter words of a language that count as words
CORPORA = [ROOT / 'lang' / 'corpora', ROOT.parent.parent / 'lang' / 'corpora', ROOT.parent / 'cypher' / 'lang' / 'corpora']

# a gap: [?] [...] [12] [nn.] [illegible] |doubtful| <...> ... ? a bare number
GAP = re.compile(r'\[(?:[\s\d.?…*+-]*|[^\]]*(?:illeg|lacun|unread|unknown|gap)[^\]]*)\]'
                 r'|\|[^|\n]*\||<[^>\n]*>|…|\.\.\.|\?+|\b\d+\b|_+', re.I)
# a resolved code word: [SUA MAESTA], {Bassa}
CODE = re.compile(r'\[[^\]\d?…]*[^\W\d_][^\]]*\]|\{[^}\n]+\}')
WORD = re.compile(r"[^\W\d_]+", re.U)


def _corpus_files(lang):
    seen = {}
    for d in CORPORA:
        for f in glob.glob(str(d / f'{lang}-*.txt')):
            seen.setdefault(os.path.basename(f), f)
    return sorted(seen.values())


_LEX = {}
LEXICONS = ROOT / 'lang' / 'lexicons'      # committed, so CI scores the same as a checkout with the corpora


def build_lexicon(lang):
    """{word: count} from the period corpora of a language, normalised 'early' (j=i, v=u, accents off), written to
    lang/lexicons/<lang>.json.gz. Words seen fewer than LEX_MIN_COUNT times are dropped, and short words (one or two
    letters) are kept only among the SHORT_KEEP commonest: a junk decode is full of stray letters."""
    import gzip
    c = collections.Counter()
    for f in _corpus_files(lang):
        with open(f, encoding='utf-8', errors='ignore') as fh:
            for line in fh:
                c.update(lm.norm(line, 'early').split())
    keep = {w: n for w, n in c.items() if n >= LEX_MIN_COUNT and len(w) >= 3}
    keep.update({w: c[w] for w in [w for w, _ in c.most_common() if len(w) <= 2][:SHORT_KEEP]})
    if keep:
        LEXICONS.mkdir(parents=True, exist_ok=True)
        with gzip.open(LEXICONS / f'{lang}.json.gz', 'wt', encoding='utf-8') as g:
            json.dump(keep, g, separators=(',', ':'), sort_keys=True)
    return keep


def lexicon(lang):
    if lang in _LEX: return _LEX[lang]
    import gzip
    path = LEXICONS / f'{lang}.json.gz'
    _LEX[lang] = json.load(gzip.open(path, 'rt', encoding='utf-8')) if path.exists() else build_lexicon(lang)
    return _LEX[lang]


def languages():
    have = {p.name.split('.')[0] for p in LEXICONS.glob('*.json.gz')}
    return sorted(have | {os.path.basename(f).split('-')[0] for d in CORPORA for f in glob.glob(str(d / '*-*.txt'))})


def clean_text(raw):
    """Drop comment lines, code fences, markdown headings, table rules and lines of cipher figures."""
    keep = []
    for line in raw.splitlines():
        s = line.strip()
        if s.startswith(('#', '```', '---', '|---', '<!--')): continue
        toks = s.split()
        if len(toks) >= 6 and sum(len(t) <= 2 or not WORD.search(t) for t in toks) / len(toks) > 0.7:
            continue
        keep.append(line)
    return '\n'.join(keep)


def script(text):
    letters = [c for c in text if c.isalpha()][:5000]
    if not letters: return 'none'
    latin = sum(c.isascii() or 'LATIN' in unicodedata.name(c, '') for c in letters)
    return 'latin' if latin / len(letters) > 0.8 else 'other'


def is_unspaced(text):
    ws = WORD.findall(GAP.sub(' ', CODE.sub(' ', text)))
    return bool(ws) and sum(map(len, ws)) / len(ws) > 12


def shape(text):
    sc = script(text)
    if sc != 'latin': return 'other script' if sc == 'other' else 'empty'
    if is_unspaced(text): return 'unspaced'
    letters = [c for c in text if c.isalpha()]
    upper = sum(c.isupper() for c in letters) / max(1, len(letters))
    bars = text.count('|') / max(1, len(text.split()))
    return 'decode' if upper > 0.6 or bars > 0.05 else 'reading'


def segment(run, lex):
    """Split an unspaced run into words (Viterbi over the word list's unigram counts)."""
    total = sum(lex.values()) or 1
    n = len(run); best = [0.0] + [math.inf] * n; back = [0] * (n + 1)
    for i in range(1, n + 1):
        for j in range(max(0, i - 18), i):
            w = run[j:i]
            cost = -math.log(lex[w] / total) if w in lex else 12.0 + 4.0 * len(w)
            if best[j] + cost < best[i]: best[i], back[i] = best[j] + cost, j
    out = []; i = n
    while i > 0: out.append(run[back[i]:i]); i = back[i]
    return out[::-1]


def sentences(text):
    out = []
    for block in re.split(r'[.;:!?]+(?=\s)|\n\s*\n', text):
        toks = block.split()
        if not toks: continue
        if len(toks) > 24:
            out += [toks[i:i + 12] for i in range(0, len(toks), 12)]
        else:
            out.append(toks)
    return [s for s in out if len(s) >= 3]


def words_of(tok):
    """A whitespace token -> list of (word, is_gap)."""
    if tok == 'CODEWORD': return [('codeword', False)]
    bare = tok.strip('.,;:!()"\'«»“”')
    if GAP.fullmatch(bare) or (GAP.search(tok) and not WORD.search(GAP.sub('', tok))):
        return [(tok, True)]
    return [(w, False) for w in lm.norm(GAP.sub(' ', tok), 'early').split()] + ([(tok, True)] if GAP.search(tok) else [])


def detect(text, langs=None):
    ws = [w for w in lm.norm(GAP.sub(' ', CODE.sub(' ', text)), 'early').split() if len(w) >= 3][:3000]
    if not ws: return None, 0.0
    best = (None, -1.0)
    for lg in langs or languages():
        lex = lexicon(lg)
        if not lex: continue
        cov = sum(w in lex for w in ws) / len(ws)
        if cov > best[1]: best = (lg, cov)
    return best


def detect_unspaced(text, langs=None):
    """Language of an unspaced text: the word list that segments it with the fewest unknown stretches."""
    runs = [lm.norm(r, 'early').replace(' ', '') for r in WORD.findall(GAP.sub(' ', CODE.sub(' ', text)))]
    sample = ''.join(runs)[:1500]
    best = (None, -1.0)
    for lg in langs or languages():
        lex = lexicon(lg)
        if not lex: continue
        ws = segment(sample, lex)
        cov = sum(len(w) for w in ws if w in lex and len(w) >= 3) / max(1, len(sample))
        if cov > best[1]: best = (lg, cov)
    return best


def score_text(raw, lang=None):
    text = clean_text(raw)
    shp = shape(text)
    empty = dict(lang=None, coverage=None, shape=shp, sentences=0, clean=0, clean_share=None, words=0, hole_rate=None)
    if shp in ('other script', 'empty'): return empty
    cov = None
    if shp == 'unspaced':
        if lang is None: lang, cov = detect_unspaced(text)
        lex = lexicon(lang) if lang else {}
        text = CODE.sub(' CODEWORD ', text)
        text = re.sub(r'[^\W\d_]{2,}', lambda m: ' '.join(segment(lm.norm(m.group(0), 'early').replace(' ', ''), lex))
                      if m.group(0) != 'CODEWORD' else m.group(0), text)
    else:
        if lang is None: lang, cov = detect(text)
        text = CODE.sub(' CODEWORD ', text)
    lex = lexicon(lang) if lang else {}
    # a raw decode's |...| marks a doubtful stretch: count it as one gap
    sents = sentences(re.sub(r'\|[^|\n]*\|', ' [?] ', text))
    clean = holes = nwords = 0
    for s in sents:
        h = n = 0
        for tok in s:
            for w, gap in words_of(tok):
                n += 1
                if gap or (w not in lex and w != 'codeword'): h += 1
        nwords += n; holes += h
        if n and h <= max(1, n // 10): clean += 1
    return dict(lang=lang, coverage=round(cov, 3) if cov is not None else None, shape=shp,
                sentences=len(sents), clean=clean, clean_share=round(clean / len(sents), 3) if sents else None,
                words=nwords, hole_rate=round(holes / nwords, 3) if nwords else None)


def verdict(share, shp):
    if shp == 'other script': return 'not scored'
    if share is None: return 'no text'
    if share >= READABLE and shp == 'reading': return 'readable'
    if share >= MARGINAL: return 'marginal'
    return 'not a reading'


def listify(v):
    return [] if v in (None, '') else v if isinstance(v, list) else [v]


def target_rows(folder):
    p = ROOT / 'targets' / folder / 'profile.json'
    if not p.exists(): return []
    prof = json.load(open(p, encoding='utf-8'))
    o = prof.get('outcome') or {}
    rows = []
    for t in o.get('texts') or []:
        has_tr = bool(listify(t.get('translation'))) or (t.get('language') or '').lower() == 'en'
        state = t.get('state') or 'read'
        for f in listify(t.get('decryption')) + listify(t.get('reading')):
            fp = ROOT / 'targets' / folder / f
            if str(f).startswith('http') or not fp.exists() or fp.suffix.lower() in ('.pdf', '.json'): continue
            try: raw = fp.read_text(encoding='utf-8', errors='ignore')
            except OSError: continue
            s = score_text(raw)
            rows.append(dict(folder=folder, method=o.get('method'), cls=o.get('class'), doc='/'.join(map(str, listify(t.get('doc')))),
                             file=f, translation=has_tr, state=state, verdict=verdict(s['clean_share'], s['shape']), **s))
    return rows


def target_summary(rows):
    """One figure per target: the best decryption file of each document entry, weighted by words; and the worst."""
    by_doc = collections.defaultdict(list)
    for r in rows: by_doc[r['doc']].append(r)
    nread = sum(v[0]['state'] == 'decoded, not read' for v in by_doc.values())
    counted = {k: v for k, v in by_doc.items() if v[0]['state'] == 'read'}
    by_doc = counted or by_doc
    best = [max(v, key=lambda r: (r['clean_share'] or 0, r['shape'] == 'reading')) for v in by_doc.values()]
    words = sum(r['words'] for r in best) or 1
    share = sum((r['clean_share'] or 0) * r['words'] for r in best) / words
    worst = min(best, key=lambda r: r['clean_share'] or 0)
    return dict(docs=len(best), clean_share=round(share, 3), worst_doc=worst['doc'], worst_share=worst['clean_share'],
                shapes=dict(collections.Counter(r['shape'] for r in best)), translated=sum(r['translation'] for r in best),
                not_scored=all(r['shape'] == 'other script' for r in best), decoded_not_read=nread)


def main(argv):
    if not argv:
        print(__doc__); return 1
    if argv[0] == '--build-lexicons':
        for lg in sorted({os.path.basename(f).split('-')[0] for d in CORPORA for f in glob.glob(str(d / '*-*.txt'))}):
            print(lg, len(build_lexicon(lg)))
        return 0
    if argv[0] == '--file':
        print(json.dumps(score_text(open(argv[1], encoding='utf-8', errors='ignore').read()), indent=1)); return 0
    if argv[0] == '--audit':
        out = []
        for p in sorted(glob.glob(str(ROOT / 'targets' / '*' / 'profile.json'))):
            folder = os.path.basename(os.path.dirname(p))
            rows = target_rows(folder)
            if rows: out.append((folder, rows, target_summary(rows)))
        out.sort(key=lambda x: (x[2]['not_scored'], x[2]['clean_share']))
        if '--csv' in argv:
            with open(argv[argv.index('--csv') + 1], 'w', newline='', encoding='utf-8') as fh:
                w = csv.writer(fh)
                w.writerow(['folder', 'method', 'docs', 'clean_share', 'worst_doc', 'worst_share', 'shapes', 'translated', 'not_scored'])
                for folder, rows, s in out:
                    w.writerow([folder, rows[0]['method'], s['docs'], s['clean_share'], s['worst_doc'], s['worst_share'],
                                ' '.join(f'{k}:{v}' for k, v in s['shapes'].items()), s['translated'], s['not_scored']])
        for folder, rows, s in out:
            shp = ' '.join(f'{k}:{v}' for k, v in s['shapes'].items())
            print(f"{s['clean_share']:.2f}  worst {s['worst_share'] or 0:.2f} ({s['worst_doc'][:20]})  [{shp}]  "
                  f"translated {s['translated']}/{s['docs']}  {folder}  [{rows[0]['method']}]")
        return 0
    rows = target_rows(argv[0])
    for r in rows:
        print(f"{r['verdict']:14} {r['clean_share']}  {r['clean']}/{r['sentences']} sentences  holes {r['hole_rate']}  "
              f"{r['lang']} {r['shape']}  tr={'y' if r['translation'] else 'n'}  {r['file']}"
              + ('' if r['state'] == 'read' else f"  [{r['state']}]"))
    if rows:
        s = target_summary(rows)
        print(f"target: clean share {s['clean_share']}, worst {s['worst_doc']} {s['worst_share']}, "
              f"shapes {s['shapes']}, translated {s['translated']}/{s['docs']}"
              + (f", plus {s['decoded_not_read']} decoded, not read" if s['decoded_not_read'] else ''))
    return 0


if __name__ == '__main__':
    sys.exit(main(sys.argv[1:]))
