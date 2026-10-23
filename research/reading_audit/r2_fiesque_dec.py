"""r2_fiesque helper: decode a fiesque1567 transcription that uses name!x alternates (round 2 reread).
usage: python r2_fiesque_dec.py <transcription> [Dz=con]
Prints the decode per line (codes in caps, alternates as their read value), then counts:
signs, letters, alternates (letters resting on name!x), unexplained '?' signs."""
import sys, re, pathlib
D = pathlib.Path(__file__).resolve().parents[2] / 'targets/fiesque1567/contributed/data'
key = {}
for ln in open(D/'key.tsv', encoding='utf-8'):
    if ln.startswith('#') or not ln.strip(): continue
    p = ln.rstrip('\n').split('\t'); key[p[0]] = p[1]
extra = dict(a.split('=', 1) for a in sys.argv[2:] if '=' in a)
key.update(extra)
n_sign = n_let = n_alt = n_q = 0
for ln in open(sys.argv[1], encoding='utf-8'):
    m = re.match(r'(c\w+):\s*(.*)', ln)
    if not m: continue
    out = []
    for t in m.group(2).split():
        n_sign += 1
        if '!' in t and not t.startswith('a!'):
            nm, v = t.split('!', 1); out.append(v); n_alt += len(v); n_let += len(v); continue
        if t == 'a!' : out.append('e'); n_let += 1; continue
        nm = t.rstrip('?') if len(t) > 1 else t
        if nm == '?': out.append('[?]'); n_q += 1; continue
        v = key.get(nm)
        if v is None or v == '?': out.append(f'[{nm}]'); n_q += 1; continue
        if v == '(null)': continue
        if len(v) > 1 or nm.startswith('='): out.append(' ' + v.upper() + ' ')
        else: out.append(v)
        n_let += len(v.replace('/', ''))
    print(m.group(1), re.sub(r'\s+', ' ', ''.join(out)).strip())
print(f'# signs {n_sign}; letters {n_let}; alternates {n_alt} ({n_alt/max(n_let,1):.1%}); unexplained signs {n_q}')
