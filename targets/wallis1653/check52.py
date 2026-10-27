"""Token-align letter52_davys.txt: build Davys's key from his reading, flag clashes, count read share."""
import re, sys, collections
L = open(sys.argv[1] if len(sys.argv) > 1 else 'letter52_davys.txt', encoding='utf8').read().splitlines()
def toks(s):  # bracketed clear text counts as one non-cipher item
    return re.findall(r'\[[^\]]*\]|\S+', s)
key = collections.defaultdict(collections.Counter); n = unread = 0; bad = []
for i, line in enumerate(L):
    if not line.startswith('C '): continue
    c, d = toks(line[2:]), toks(L[i + 1][2:])
    if len(c) != len(d): bad.append((L[i - 1], len(c), len(d))); continue
    for a, b in zip(c, d):
        if a.startswith('['): continue
        n += 1
        if b == '?': unread += 1
        else: key[int(a)][b] += 1
for b in bad: print('LENGTH MISMATCH', b)
print(f'cipher groups {n}, read {n-unread} ({100*(n-unread)/n:.1f}%), unread {unread}')
print('distinct groups', len(key) )
for k in sorted(key):
    if len(key[k]) > 1: print('CLASH', k, dict(key[k]))
val = collections.defaultdict(list)
for k in sorted(key): val[key[k].most_common(1)[0][0]].append(k)
print('key:', '; '.join(f'{k}={key[k].most_common(1)[0][0]}' for k in sorted(key)))
print('homophones:', {v: ks for v, ks in sorted(val.items()) if len(ks) > 1})
