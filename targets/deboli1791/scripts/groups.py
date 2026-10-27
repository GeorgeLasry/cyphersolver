"""Extract code groups from the transcription files.
zbpop5: every token on an L-line is a group. zbpop415: only tokens inside <...>."""
import re, sys, collections
def norm(tok):
    tok = tok.strip('.—-,;:')
    m = re.match(r'^(\d+|\?\d*|\d*\?\d*)([a-z]{0,2})', tok)
    return m.group(1) + m.group(2) if m and re.search(r'\d', m.group(1)) else None
def groups_1791(path):
    out = []
    for line in open(path, encoding='utf8'):
        if not re.match(r'^L\d+:', line): continue
        body = re.sub(r'\{[^}]*\}', ' ', line.split(':', 1)[1])
        for t in body.split():
            if t.startswith('[del'): continue
            g = norm(t.replace('_u', ''))
            if g: out.append(g)
    return out
def groups_1792(path):
    out = []
    txt = ''.join(l.split(':', 1)[1] if re.match(r'^L\d+:', l) else '' for l in open(path, encoding='utf8'))
    for run in re.findall(r'<([^>]*)>', txt):
        run = re.sub(r'\{[^}]*\}', ' ', run)
        for t in re.split(r'[\s.]+', run):
            g = norm(t.replace('_u', '').replace('[?]', '?'))
            if g: out.append(g)
    return out
if __name__ == '__main__':
    a = groups_1791('transcription/zbpop5_001-003.txt'); b = groups_1792('transcription/zbpop415_1792_mixed.txt')
    base = lambda g: re.sub(r'[a-z?]', '', g)
    ca = collections.Counter(base(g) for g in a); cb = collections.Counter(base(g) for g in b)
    print(len(a), len(ca), len(b), len(cb))
    print('1791 top', ca.most_common(25)); print('1792 top', cb.most_common(25))
    print('1791 max', max(int(x) for x in ca if x), '1792 max', max(int(x) for x in cb if x))
    print('one-digit 1791', sum(v for k, v in ca.items() if len(k) == 1), '1792', sum(v for k, v in cb.items() if len(k) == 1))
    sh = set(ca) & set(cb); print('shared distinct', len(sh))
    # 1792 top groups' freq in 1791
    print([(g, cb[g], ca[g]) for g, _ in cb.most_common(20)])
