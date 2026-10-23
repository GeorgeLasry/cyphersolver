"""b18 (ceva1632): re-decode R75 and R84 as one stream each (run2.py settings, --unvalued=-5) with the key
changes adopted on 22-23 Oct 2026 from the two contemporary decipherments (R75 f. 82r, R84 f. 136r), applied in
memory only (cipher.py is left as the second pass left it):

  88  quel -> del     every R75/R84 occurrence = del/della/dello in the decipherments; fits Lasry's 28 (la pieta ~ , a dano ~ Francia)
  33  (dead) -> gli   R75 per ~ interessi, compor ~ esterni, chi ~ li, contro ~ infedeli, ne ~ affari; Lasry 346/5 'lege a ~ altri'
  541 armi            R75 x3 (decipherment 'l'armi', 'le medesime armi', 'l'armi di Francia'); was parsed io<128>, io{1}
  171 Regno           R75 x2, R84 x2 (decipherments 'del Regno'); was parsed i<129>, i{1}, i<124>
  473 mentre          R75 x2 ('sottoposto mentre hanno', 'Però mentre vi è tema')
  497 tutto           R75 'da tutti', R84 'tutto quello'; Lasry 'abbino a ridurre ~ le difficoltà', 'conferito con ... ~ quello'
  491 quello          R75 'quello dell'unione', 'di quello che sia stato'; R84 'tutto quello che'; Lasry 'a ~ unione', 'in ~ piazza'
  104 Olandesi        R75 decipherment 'de gli Olandesi', 1632 interlinear 'Oland.si' (was Svedesi, a guess)
  129 dropped         its two R75 hits were 171 + null 29
Writes targets/ceva1632/r75.tokens3.json, r84.tokens3.json, r75.read3.txt, r84.read3.txt.
"""
import sys, os, json
T = os.path.join(os.path.dirname(os.path.abspath(__file__)), '..', '..', 'targets', 'ceva1632')
T = os.path.abspath(T)
sys.path.insert(0, T); sys.path.insert(0, os.path.dirname(os.path.dirname(T)))
import cipher
cipher.KEY['88'] = 'del'
cipher.KEY['33'] = 'gli'
cipher.NOMEN.pop('129', None)
cipher.NOMEN.update({'541': 'armi', '171': 'regno', '473': 'mentre', '497': 'tutto', '491': 'quello', '104': 'olandesi'})
import decode as D
D.DEAD = {'%02d' % i for i in range(100)} - set(cipher.KEY) - cipher.NULLS
import indomain
D.P_NOMEN_KNOWN, D.P_NOMEN_NEW, D.P_NULL = -1.5, -20.0, 0.0
D.P_NOMEN_UNVALUED = -5.0

def lines_of(tag):
    p = os.path.join(T, tag + '.retrans.txt')
    return [''.join(c for c in l if c.isdigit()) for l in open(p, encoding='utf-8') if any(c.isdigit() for c in l)]

model, n = indomain.build(w=0.6)
nomen = D.load_nomen() | set(cipher.NOMEN)
for tag in sys.argv[1:] or ('r75', 'r84'):
    lines = lines_of(tag)
    _, text, toks = D.decode(''.join(lines), model, nomen, beam=600, w_lm=0.4)
    out, cur, k, b, bounds, acc = [], [], 0, 0, [], 0
    for l in lines: acc += len(l); bounds.append(acc)
    for t in toks:
        cur.append(t); k += len(t.lstrip('#?'))
        if b < len(bounds) and k >= bounds[b]: out.append(cur); cur = []; b += 1
    if cur: out.append(cur)
    json.dump(out, open(os.path.join(T, tag + '.tokens3.json'), 'w'), indent=0)
    def r(t):
        if t == '6': return ' '
        if t.startswith('#'): return cipher.NOMEN[t[1:]].upper() if t[1:] in cipher.NOMEN else '<%s>' % t[1:]
        if t.startswith('?'): return '{%s}' % t[1:]
        if t in cipher.NULLS: return ''
        return cipher.KEY[t]
    open(os.path.join(T, tag + '.read3.txt'), 'w', encoding='utf-8').write('\n'.join(''.join(r(t) for t in l) for l in out) + '\n')
    print(tag, 'done')
