"""v2 (23 Oct 2026): copy of b23_sessa_align.py that also lists the words carrying a look-alike letter other than
the attested second value 3 = i (written to argv[2], one normalised word per line).

b23: align the sessa1524 readings (r9873_reading.md, r9898_reading.md) word by word with what carries them.

    python -X utf8 research/reading_audit/b23_sessa_align.py r9873|r9898

Carried text, from the working file targets/sessa1524/<doc>_cipher.txt, folio by folio ("==== f.NNN" sections):
  * the (b)/(d) decode lines: "[x=value]" / "[x=value?]" -> value, an open "[x]" -> OPEN, spelled letters joined
    ("de-s-ha-z-e-r-se" -> deshazerse; a word broken over two decode lines by a trailing/leading hyphen is joined),
    "->" comments and "(...)" glosses dropped;
  * the clear text quoted in the (a)/(c) cipher lines, the "Clear:" lines and the "M:" margin decipherments (R9898).
Reading words: the body under "## Reading", folio by folio ("### f. NNN"); a token holding "[" or "]" is a marked word
(supplied, partly carried, unread, open group) and is not checked. Words are normalised (lower case, accents off,
j=i, v=u, y=i, ç=c, z=c, doubled letters single).
Alignment: difflib over the two word sequences of a folio; an unbracketed reading word left unmatched is accepted when
the same word (or two adjacent carried words joined, or a carried word it begins or ends) stands within 40 words of the
aligned position, or when it is in MENDED (a word whose spelling the reading mends from the figures; each one is in
the reread log); otherwise it is reported (an invented word, to be bracketed).

Look-alike count: on every (a)/(b) line pair whose signs and (b) letters pair one to one, each sign of LOOK whose
letter in (b) is not its first value is counted, if the word it falls in stands unbracketed in the reading.
"""
import collections, difflib, re, sys, unicodedata
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
T = ROOT / 'targets' / 'sessa1524'
doc = sys.argv[1]
SRC = (T / f'{doc}_cipher.txt').read_text(encoding='utf-8').splitlines()
READ = (T / f'{doc}_reading.md').read_text(encoding='utf-8')

# reading words that mend the (b) spelling from the figures (logged in texts/r9873-r9898_reread_log.md)
MENDED = {'r9873': ['atajar', 'demostracion', 'teniendose', 'jamas', 'huvo', 'esas', 'fronteras', 'ynresolucion',
                    'ynreparable', 'halla', 'porque', 'ynposibilidad', 'haze', 'veniesse', 'averle', 'me',
                    'dezir', 'servidores'],   # b23 adopted reb = dezi-, dis = servido (log section 3)
          'r9898': ['embiado', 'sea', 'asegurarlo']}[doc]
LOOK = {'ꝍ': 'r', '3': 'r', 'x': 'e', 'tt': 'c', 'Ɉ': 'd', '⅄': 'z', 'tto': 'b', '9': 'e', '∠': 'ñ', 'Є': 'h', 'ε': 'h'}
NL = '\n'


def norm(w):
    w = unicodedata.normalize('NFD', w.lower())
    w = ''.join(c for c in w if unicodedata.category(c) != 'Mn')
    w = w.replace('j', 'i').replace('v', 'u').replace('y', 'i').replace('ç', 'c').replace('z', 'c')
    w = re.sub(r'[^a-z]', '', w)
    return re.sub(r'(.)\1+', r'\1', w)


def bline(s):
    s = s.split('->')[0]
    s = re.sub(r'\([^)]*\)', ' ', s)
    s = re.sub(r'\[([^\]=]*)=([^\]]*)\]', lambda m: m.group(2).replace('?', ''), s)
    s = re.sub(r'\[[^\]]*\]', ' OPEN ', s)
    s = re.sub(r'"([^"]*)"', r' \1 ', s)
    return s.replace('/', ' ').replace('¶', ' ').replace('...', ' ').replace('…', ' ')


def words(q):
    return [w.strip('.') for w in re.split(r'[\s/,;:]+', q.replace('...', ' ')) if w.strip('.') and not w.startswith('(')]


SEC = collections.defaultdict(list)          # folio -> carried words
key, pending = 'start', ''
for ln in SRC:
    st = ln.strip()
    if st.startswith('===='):
        mm = re.search(r'f\.\s*(\d+[rv])', st)
        if mm: key = 'f' + mm.group(1)
        for q in re.findall(r'"([^"]*)"', st):
            SEC[key] += words(q)
        continue
    if not st or st.startswith('#'):
        continue
    if st.startswith('Clear:') or re.match(r'^M\d?\b|^M \(|^M:', st) or st.startswith('"'):
        for q in re.findall(r'"([^"]*)"', st) or [st.split(':', 1)[-1]]:
            SEC[key] += words(q)
        continue
    m = re.match(r'^\d+([a-d])\s(.*)$', st)
    if not m:
        SEC[key] += words(st)
        continue
    kind, body = m.groups()
    if kind in 'ac':                         # cipher lines: only their quoted clear text
        for q in re.findall(r'"([^"]*)"', body):
            SEC[key] += words(q)
        continue
    toks = bline(body).split()
    for i, t in enumerate(toks):
        if t.startswith('-') and pending:
            t = pending + t; pending = ''
        elif pending:
            SEC[key].append(pending.replace('-', '')); pending = ''
        if t.endswith('-') and i == len(toks) - 1:
            pending = t.rstrip('-'); continue
        SEC[key].append(t.replace('-', ''))
if pending: SEC[key].append(pending)

body = re.search(r'^## Reading[^\n]*\n(.*?)(?=^## |\Z)', READ, re.S | re.M).group(1)
RSEC = collections.defaultdict(list)
rkey = 'start'
for l in body.split(NL):
    if l.startswith('#'):
        mm = re.search(r'f\.\s*(\d+[rv])', l)
        if mm: rkey = 'f' + mm.group(1)
        continue
    RSEC[rkey] += l.replace('[clear text not transcribed]', ' ').split()

MN = {norm(x) for x in MENDED}
tot = collections.Counter()
unc, allw = [], []
for rk, rtoks in RSEC.items():
    cw = SEC.get(rk) or [w for v in SEC.values() for w in v]
    cn = [c for c in map(norm, cw) if c]
    rw = []
    for t in rtoks:
        marked = '[' in t or ']' in t
        n = norm(t)
        if n or marked: rw.append((t, n, marked))
    allw += rw
    rn = [w[1] if not w[2] else '#' for w in rw]
    sm = difflib.SequenceMatcher(None, rn, cn, autojunk=False)
    matched = {}
    for a, b, size in sm.get_matching_blocks():
        for k in range(size): matched[a + k] = b + k
    last = 0
    for i, (t, n, marked) in enumerate(rw):
        if i in matched: last = matched[i]; tot['inorder'] += 1; continue
        if marked: continue
        win = cn[max(0, last - 40): last + 41]
        pairs = {win[j] + win[j + 1] for j in range(len(win) - 1)}
        if n in win or n in pairs or n in MN or (len(n) >= 4 and any(c.startswith(n) or c.endswith(n) for c in win)):
            tot['near'] += 1; continue
        unc.append((rk, t, ' '.join(w[0] for w in rw[max(0, i - 5): i + 5])))
plain = sum(1 for w in allw if not w[2])
print(doc, 'reading words', len(allw), 'unbracketed', plain, 'matched in order', tot['inorder'], 'matched nearby',
      tot['near'], 'NOT CARRIED', len(unc))
for rk, t, ctx in unc:
    print('  -', rk, t, '|', ctx)

# look-alike letters
plain_words = {w[1] for w in allw if not w[2]}
LW = []
look = collections.Counter(); paired = unpaired = 0
lines = [l.strip() for l in SRC]
for k, l in enumerate(lines):
    m = re.match(r'^(\d+)a\s(.*)$', l)
    if not m or k + 1 >= len(lines): continue
    m2 = re.match(r'^' + m.group(1) + r'b\s(.*)$', lines[k + 1])
    if not m2: continue
    a = re.sub(r'"[^"]*"', ' ', m.group(2)).replace('f~', ' ').replace('...', ' ').split()
    b = m2.group(1).split('->')[0]
    b = re.sub(r'\([^)]*\)', ' ', b); b = re.sub(r'"[^"]*"', ' ', b).replace('...', ' ').replace('/', ' ').replace('¶', ' ')
    pieces, wop = [], []
    for w in b.split():
        wn = norm(re.sub(r'\[[^\]]*=([^\]]*)\]', r'\1', w).replace('-', ''))
        for p in re.findall(r'\[[^\]]*\]|[^-\[\]]+', w):
            if p.startswith('['):
                inner = p[1:-1].split('=')[0].split()
                pieces += ['#'] * max(1, len(inner)); wop += [wn] * max(1, len(inner))
            else:
                pieces.append(p); wop.append(wn)
    if a[:2] == ['v', 'db']: a = a[2:]
    if len(a) != len(pieces):
        unpaired += 1; continue
    paired += 1
    for s, p, wn in zip(a, pieces, wop):
        if s in LOOK and p != '#' and p.lower() != LOOK[s] and wn in plain_words:
            look[(s, p.lower())] += 1
            if not (s == '3' and p.lower() == 'i'): LW.append((wn, s, p))
print('look-alike letters (line pairs paired %d, not paired %d):' % (paired, unpaired), sum(look.values()),
      ', '.join(f'{s}->{p} {n}' for (s, p), n in look.most_common()))

NLC = chr(10)
Path(sys.argv[2]).write_text(NLC.join(w + chr(9) + s + chr(9) + p for w, s, p in LW), encoding='utf-8')
print('unattested look-alike words', len(LW))
