"""b5_generators.py -- the two pre-registered b5 candidates (b5_PREREG.md).

G  DriftCopist  meaningless: Timm & Schinner self-citation (a4.Autocopist) with per-section seed lines,
               page/section-local sources, exact reuse, and a per-scribe substitution habit.
C  SlotCipher   meaningful: verbose slot cipher of Latin (Pliny NH, books ordered by section), one table per
               Currier language, nomenclator for frequent words.  (Added in a later commit.)

Neither reads Voynich word types or frequencies.  Inputs: the glyph grammar in a4 (SIMILAR, FINAL_SUB,
PREFIX_OK, valid), the page skeleton and each page's hand / Currier language / section from the TSV header.
"""
import os, sys, random, collections
_HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, _HERE)
import a4_selfcitation as a4
from a4_selfcitation import tok, valid, pick, SIMILAR, FINAL_SUB, GALLOWS, COMBINABLE

ZL = os.path.join(_HERE, 'data', 'ZL3b-n.words.tsv')

# the five free parameters of G (b5_PREREG.md lists six; the line-initial gallows rate is dropped because
# its only targets, g_gal_init / g_gal_mid, are held-out items and cannot be tuned -- see Deviations)
G_DEFAULTS = {'p_reuse': 0.10, 'w_page': 1.0, 'w_sect': 0.0, 'habit': 0.0, 'p_n1': 0.30}


def page_meta():
    """folio -> (hand, lang, section) from the TSV columns, in manuscript order."""
    meta = collections.OrderedDict()
    with open(ZL, encoding='utf-8') as f:
        next(f)
        for l in f:
            c = l.rstrip('\n').split('\t')
            meta.setdefault(c[0], (c[4], c[3], c[5]))
    return meta


import functools
@functools.lru_cache(maxsize=None)
def _ttype(w):
    return a4.Autocopist.ttype(tok(w))


class DriftCopist(a4.Autocopist):
    def __init__(self, seed=19, **par):
        super().__init__(seed)
        self.p = dict(G_DEFAULTS, **par)
        self.sect_lines = collections.defaultdict(list)
        self.sect = None
        self.habits = {}                     # scribe -> {glyph: favourite replacement}
        self.habit = {}

    def set_page(self, hand, lang, section):
        key = (hand, section)
        if hand not in self.habits:          # each scribe's own fixed preferences, drawn once
            hr = random.Random(f'{self.rng.random()}-{hand}')
            self.habits[hand] = {g: hr.choice([v for _, v in tab]) for g, tab in list(SIMILAR.items()) + list(FINAL_SUB.items())}
        self.habit = self.habits[hand]
        if key != self.sect:
            self.sect = key
            if not self.sect_lines[key]:     # new section: seed line = morphs of the last line written
                base = self.all_lines[-1]
                seed = [h for g in base for h in (self.morph(list(g), list(g), False, False) or [list(g)])]
                self.sect_lines[key].append(seed)

    def suggest(self):
        """a4.Autocopist.suggest with the type of each word cached (same output; the original re-tokenises
        every type in the document on each call, which made high-reuse settings 100x slower)"""
        if self.stat_tot < 20: return None
        want = None
        if self.stat_i / self.stat_tot < 0.20: want = 'i'
        elif self.stat_dy / self.stat_tot < 0.25: want = 'dy'
        if not want: return None
        for src in (self.page_counts, self.doc_counts):
            for w, c in src.most_common():
                if _ttype(w) == want:
                    return tok(w)
        return None

    def choose_source(self, cur_line, line_initial):
        rng = self.rng; P = self.p
        pool = self.page_lines if (self.page_lines and rng.random() < P['w_page']) else None
        if pool is None:
            pool = self.sect_lines[self.sect] if rng.random() < P['w_sect'] and self.sect_lines[self.sect] else self.all_lines
        k = len(pool)
        line = pool[k - 1 - rng.randrange(max(2, k) - 1)] if k > 1 else pool[0]
        p_same = 14 if line_initial else 28
        if rng.randint(1, 100) <= p_same and len(cur_line) < len(line):
            pos = len(cur_line)
        else:
            pos = rng.randrange(len(line))
        g1 = line[pos]
        g2 = line[pos + 1] if pos + 1 < len(line) else (line[pos - 1] if pos > 0 else line[pos])
        return list(g1), list(g2)

    def replace(self, g, n):
        rng = self.rng
        if self.p['habit'] > 0 and rng.random() < self.p['habit']:
            for _ in range(4):               # the scribe's habitual substitution at one position
                pos = rng.randrange(len(g)); fav = self.habit.get(g[pos])
                if fav:
                    cand = g[:pos] + tok(fav) + g[pos + 1:]
                    if cand != g and valid(cand): return cand
        return super().replace(g, n)

    def morph(self, g1, g2, para_init, line_init):
        rng = self.rng
        if not (para_init and line_init) and rng.random() < self.p['p_reuse']:
            return [list(g1)]                # copied unchanged
        r = 0 if (para_init and line_init) else rng.randint(0, 100)
        if r <= 20:
            h = self.add(g1, para_init, line_init); return [h] if h else None
        if r <= 50:
            if rng.randint(1, 100) <= 50:
                h = self.combine(g1, g2)
                if h: self.combined.add(''.join(h)); return [h]
            s = self.split(g1)
            if s: return s
        p1 = self.p['p_n1']; rr = rng.random()
        n = 1 if rr < p1 else (3 if rr < p1 + (1 - p1) / 7 else 2)   # Timm's 30/10/60 split at p_n1 = 0.30
        h = self.replace(g1, n)
        if h is None and n > 1: h = self.replace(g1, 1)
        return [h] if h else None

    def generate(self, skel, metas):
        init = [tok(w) for w in 'pchal shal shorchdy okeor okain shedy pchedy qotchedy qotar ol lkar'.split()]
        self.all_lines.append(init)
        pages = []
        for pl, (hand, lang, sect) in zip(skel, metas):
            self.set_page(hand, lang, sect)
            self.page_lines = []; self.page_counts = collections.Counter()
            lines = []
            for (n, clen, ps) in pl:
                ln = self.gen_line(max(clen, 8), ps)
                self.page_lines.append(ln); self.all_lines.append(ln); self.sect_lines[self.sect].append(ln)
                lines.append({'words': [''.join(g) for g in ln], 'para_start': ps})
            pages.append({'folio': '', 'lang': lang, 'lines': lines})
        return pages


# ----------------------------------------------------------------------------------------- C: slot cipher
C_DEFAULTS = {'nomen': 80, 'p_single': 0.5, 'homo': 3, 'overlap': 0.3, 'p_null': 0.05}
# slot inventory (hand-built from the glyph grammar, as Timm's tables are); geometric weights 0.6**rank in
# this fixed order.  No Voynich frequencies are read.
PREFIX = ['', 'o', 'qo', 'ch', 'y', 'd', 'sh', 'ol', 's', 'a', 'l', 'x']
CORE = ['', 'k', 't', 'e', 'ee', 'ke', 'te', 'ckh', 'cth', 'p', 'f', 'eo', 'ch', 'sh']
SUFFIX = ['y', 'aiin', 'dy', 'ol', 'ar', 'or', 'al', 'ain', 'edy', 'eey', 'r', 'l', 'am', 'iin', 's', 'o', 'eedy', 'chy', 'ody']
PLINY = os.path.join(_HERE, 'data', 'corpora', 'pliny')
SECTION_BOOKS = {'H': 'herb', 'S': 'herb', 'T': 'herb', 'A': 'astro', 'Z': 'astro', 'C': 'astro', 'B': 'bal', 'P': 'pharm'}
STREAMS = {'herb': ['XX', 'XXI', 'XXII', 'XXIII', 'XXIV', 'XXV', 'XXVI', 'XXVII'], 'astro': ['II'],
           'bal': ['XXXI'], 'pharm': ['XXXII', 'XXXI']}


def pliny_words(book):
    import re
    t = open(os.path.join(PLINY, f'ws_{book}.txt'), encoding='utf-8').read()
    i = t.find('<div class=text>'); t = t[i:] if i >= 0 else t[t.find('}}') + 2:]
    t = re.sub(r'\{\{[^}]*\}\}|==[^=]*==|<[^>]*>|\[\[[^\]|]*\||\]\]|\[\[', ' ', t).lower()
    t = t.replace('j', 'i')
    return re.findall(r'[a-z]+', t)


def wsample(rng, seq):
    w = [0.6 ** i for i in range(len(seq))]
    return rng.choices(seq, w)[0]


class SlotCipher:
    def __init__(self, seed=19, **par):
        self.rng = random.Random(seed); self.p = dict(C_DEFAULTS, **par)
        self.streams = {k: [w for b in v for w in pliny_words(b)] for k, v in STREAMS.items()}
        allw = [w for v in self.streams.values() for w in v]
        bg = collections.Counter(a + b for w in allw for a, b in zip(w, w[1:]))
        self.bigrams = {b for b, _ in bg.most_common(60)}
        self.nomen = {w for w, _ in collections.Counter(allw).most_common(int(round(self.p['nomen'])))}
        units = sorted(set('abcdefghiklmnopqrstuvxyz') | self.bigrams) + sorted(self.nomen)
        used = set(); self.table = {'A': {}, 'B': {}}
        def fresh(longer):
            for _ in range(500):
                g = [x for x in (wsample(self.rng, PREFIX), wsample(self.rng, CORE), wsample(self.rng, SUFFIX)) if x]
                if longer: g = [x for x in (wsample(self.rng, PREFIX), wsample(self.rng, CORE)) if x] + g
                g = [h for x in g for h in tok(x)]
                s = ''.join(g)
                if valid(g) and s not in used:
                    used.add(s); return s
            return s
        h = max(1, int(round(self.p['homo'])))
        for u in units:
            nom = len(u) > 2
            a = [fresh(nom) for _ in range(h)]
            self.table['A'][u] = a
            self.table['B'][u] = a if self.rng.random() < self.p['overlap'] else [fresh(nom) for _ in range(h)]
        self.cursor = collections.Counter()

    def units(self, stream):
        """endless unit generator over a plaintext stream (greedy parse: nomenclator word, bigram, letter)"""
        ws = self.streams[stream]; rng = self.rng
        while True:
            w = ws[self.cursor[stream] % len(ws)]; self.cursor[stream] += 1
            if w in self.nomen:
                yield w; continue
            i = 0
            while i < len(w):
                if i + 1 < len(w) and w[i:i + 2] in self.bigrams and rng.random() >= self.p['p_single']:
                    yield w[i:i + 2]; i += 2
                else:
                    yield w[i]; i += 1

    def token(self, unit, lang):
        rng = self.rng
        if rng.random() < self.p['p_null']:
            return rng.choice(rng.choice(list(self.table[lang].values())))
        return rng.choice(self.table[lang][unit])

    def generate(self, skel, metas):
        gens = {}; pages = []
        for pl, (hand, lang, sect) in zip(skel, metas):
            lg = 'B' if lang == 'B' else 'A'
            st = SECTION_BOOKS.get(sect, 'herb')
            g = gens.setdefault(st, self.units(st))
            lines = [{'words': [self.token(next(g), lg) for _ in range(n)], 'para_start': ps} for (n, _, ps) in pl]
            pages.append({'folio': '', 'lang': lang, 'lines': lines})
        return pages


def make_C(seed, **par):
    real = real_pages()
    return SlotCipher(seed, **par).generate(a4.skeleton(real), [(p['hand'], p['lang'], p['sect']) for p in real])


def real_pages():
    pages = a4.load_zl(); meta = page_meta()
    for p in pages:
        h, l, s = meta[p['folio']]; p['lang'] = l; p['hand'] = h; p['sect'] = s
    return pages


def make_G(seed, **par):
    real = real_pages()
    return DriftCopist(seed, **par).generate(a4.skeleton(real), [(p['hand'], p['lang'], p['sect']) for p in real])
