"""Turn a work file (Lnn: sign=value ...) into md sign lines + tokens tsv + stats.
usage: emit.py work.txt out_tokens.tsv  (prints md fragment to stdout)"""
import sys, re
rows = []
for ln in open(sys.argv[1], encoding='utf-8'):
    m = re.match(r'(L\d+):\s*(.*)', ln.strip())
    if not m: continue
    toks = []
    for t in m.group(2).split(' '):
        if '=' not in t: continue
        i = t.index('=', 1) if t.startswith('=') else t.index('=')
        # signs may contain '=' (b̶=, ꝗ=): split on the LAST '=' that is followed by a value
        k = t.rfind('=')
        if k == len(t) - 1: k = t.rfind('=', 0, k)
        s, v = t[:k], t[k + 1:]
        if s == '' : s, v = t[:k+1], t[k+1:]
        toks.append((s, v))
    rows.append((m.group(1), toks))
out = open(sys.argv[2], 'w', encoding='utf-8')
out.write('line\tsign\tvalue\n')
tot = rd = nul = fil = unr = 0
for L, toks in rows:
    print(f'**{L}** ' + ' | '.join(f'{s}={v}' for s, v in toks))
    plain = ''.join('' if v.startswith('{') else ('[..]' if v.startswith('[..]') else re.sub(r'\[.*?\]|\(.*?\)', '', v)) for s, v in toks)
    print(f'\n> {plain}\n')
    for s, v in toks:
        out.write(f'{L}\t{s}\t{v}\n'); tot += 1
        if v == '{null}': nul += 1
        elif v == '{filler}': fil += 1
        elif v.startswith('[..]'): unr += 1
        else: rd += 1
print(f'<!-- stats: tokens {tot}, read {rd}, nulls {nul}, filler(unread) {fil}, unread {unr} -->', file=sys.stderr)
