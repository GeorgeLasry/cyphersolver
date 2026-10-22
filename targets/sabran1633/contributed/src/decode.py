# 記号名の書き起こしに key.tsv を当てる。
# 書き起こしの形式：1行＝1つの暗号の連なり。「ID<TAB>記号 記号 …」。? は読めない記号、[語] は平文の語、| は区切り。
import sys
def load_key(path):
    k = {}
    for l in open(path, encoding='utf-8'):
        if l.startswith('#') or not l.strip(): continue
        f = l.rstrip('\n').split('\t')
        k[f[0]] = (f[1], f[2])
    return k
def decode_tokens(toks, key):
    out = []; prev = ''
    for t in toks:
        t0 = t.rstrip('?') if t != '?' else t
        if t.startswith('['): out.append(t); prev=''; continue
        if t == '|': out.append(' | '); continue
        v = key.get(t0)
        if v is None: out.append('<%s>' % t); prev=''; continue
        val, kind = v
        if kind == 'double': out.append(prev); continue
        if kind == 'word': out.append('(%s)' % val); prev=''; continue
        out.append(val.upper() if t.endswith('?') and t!='?' else val); prev = val
    return ''.join(out)
def load_tr(path):
    rows = []
    for l in open(path, encoding='utf-8'):
        if l.startswith('#') or not l.strip(): continue
        i, s = l.rstrip('\n').split('\t', 1)
        rows.append((i, s.split()))
    return rows
if __name__ == '__main__':
    key = load_key(sys.argv[1])
    tot = val = 0
    for i, toks in load_tr(sys.argv[2]):
        sy = [t for t in toks if not t.startswith('[') and t != '|']
        tot += len(sy); val += sum(1 for t in sy if t.rstrip('?') in key)
        print(i, decode_tokens(toks, key))
    print('symbols', tot, 'valued', val, '%.1f%%' % (100*val/max(1,tot)))
