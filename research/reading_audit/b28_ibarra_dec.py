"""b28: decode a Feria-Mansfeld transcription (keyM.tsv + fill68.json + extra codes) with marks applied.
    python research/reading_audit/b28_ibarra_dec.py <ct.txt> [codes.json]
Marks: N° -s, Nv -n, N. -r, N+ -l, +N -r- (after first consonant), N∞/x∞ -l-, N~ doubled consonant, Nr -h-/cho (13r)."""
import sys, json, re, pathlib
T = pathlib.Path(__file__).resolve().parents[2] / 'targets' / 'ibarra1593'
K = {}
for l in open(T / 'keyM.tsv', encoding='utf-8'):
    if l.startswith('#') or not l.strip(): continue
    a, b = l.split('\t'); K[a.strip()] = b.strip()
K.update({'x': 'a', '2': 'a', '3': 'e', 'p': 'e', 'r': 'o', 'n': 'u', '∂': 'y', 'R': 'a', '8': 'de'})
K.update(json.load(open(T / 'fill68.json', encoding='utf-8')))
if len(sys.argv) > 2: K.update(json.load(open(sys.argv[2], encoding='utf-8')))
def tok(t):
    if t.endswith('_'): return t[:-1]
    pre = ''
    m = re.match(r'^(\+?)([^°v.+∞~r⁘]+?)([°v.+∞~r⁘]*)$', t)
    if not m: return '[' + t + ']'
    plus, core, marks = m.groups()
    v = K.get(core)
    if v is None: return '[' + t + ']'
    if plus: v = v[0] + 'r' + v[1:]
    if '∞' in marks: v = v[0] + 'l' + v[1:]
    if '~' in marks: v = v[0] + v
    if 'r' in marks and core not in ('x',): v = v[0] + 'h' + v[1:] if core != '13' else 'cho'
    if '⁘' in marks: return 'V.E.'
    for mk, add in (('°', 's'), ('v', 'n'), ('.', 'r'), ('+', 'l')):
        if mk in marks: v += add
    return v
for l in open(sys.argv[1], encoding='utf-8'):
    if l.startswith('#') or '\t' not in l: continue
    n, t = l.rstrip('\n').split('\t', 1)
    t = re.sub(r'\[[^\]]*\]', ' | ', t)
    print(n, ' '.join(tok(x) if x != '|' else '|' for x in t.split()))
