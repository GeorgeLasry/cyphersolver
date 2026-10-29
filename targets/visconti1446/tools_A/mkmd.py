"""work.txt + plain.txt -> per-line md block (stdout) + tokens tsv + stats (stderr).
usage: mkmd.py work.txt plain.txt out_tokens.tsv
plain.txt lines: 'Lnn: plain text'"""
import sys, re
def parse(t):
    k = t.rfind('=')
    if k == len(t) - 1: k = t.rfind('=', 0, k)
    if k <= 0: k = t.index('=', 1)
    return t[:k], t[k + 1:]
plain = {}
for ln in open(sys.argv[2], encoding='utf-8'):
    m = re.match(r'(L\d+):\s*(.*)', ln.rstrip('\n'))
    if m: plain[m.group(1)] = m.group(2)
out = open(sys.argv[3], 'w', encoding='utf-8'); out.write('line\tsign\tvalue\n')
tot = rd = nul = unr = unc = 0
for ln in open(sys.argv[1], encoding='utf-8'):
    m = re.match(r'(L\d+):\s*(.*)', ln.strip())
    if not m: continue
    L = m.group(1); toks = [parse(t) for t in m.group(2).split(' ') if '=' in t[1:] or t.count('=') > 1]
    print(f'### {L}\n\nsigns: ' + ' | '.join(f'{s}={v}' for s, v in toks))
    raw = ''.join('' if v.startswith('{') else ('[..]' if v.startswith('[..]') else re.sub(r'\[.*?\]|\(.*?\)', '', v)) for s, v in toks)
    print(f'\nraw: `{raw}`\n\nplain: {plain.get(L, "")}\n')
    for s, v in toks:
        out.write(f'{L}\t{s}\t{v}\n'); tot += 1
        if v.startswith('{null'): nul += 1
        elif v.startswith('[..]'): unr += 1
        else:
            rd += 1
            if '[?]' in v: unc += 1
print(f'tokens {tot}, read {rd} ({unc} uncertain), nulls {nul}, unread {unr}; read share of non-null {rd/(tot-nul):.1%}', file=sys.stderr)
