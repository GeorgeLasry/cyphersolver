"""Token-level reading of a Deboli cipher letter that has no clear text.

Every cipher token gets a value from the key rebuilt on the pairs (key_pass.tsv), a null, a clear word written in the
cipher, or a hand reading from reading/<stem>.fix.tsv (token index TAB value TAB note; value '?' marks a key value that
does not make sense in place, any other value is a reading from context and the alphabetical bracket, graded I).
Output: reading/<stem>.tsv (index, folio line, token, value, source) and a count of tokens read.

usage: python read.py c024_1789-03-25 [c042_1789-05-10 ...] [--key key_pass.tsv]
       python read.py --validation c024_1789-03-25 c042_1789-05-10 c104_1789-12-14   (writes validation.tsv)
"""
import argparse, os, re, sys

HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, HERE)
from align import read_cipher  # noqa: E402
from decode import load_key  # noqa: E402


def reading(stem, key):
    toks = read_cipher(os.path.join(HERE, 'transcription', stem + '.txt'))
    fix = {}
    fp = os.path.join(HERE, 'reading', stem + '.fix.tsv')
    if os.path.exists(fp):
        for line in open(fp, encoding='utf-8'):
            if line.startswith('#') or not line.strip():
                continue
            p = line.rstrip('\n').split('\t')
            fix[int(p[0])] = p[1]
    rows = []
    for i, (v, loc, unsure) in enumerate(toks):
        base = re.sub(r'[a-z]+$', '', v)
        if i in fix:
            val, src = fix[i], ('open' if fix[i] == '?' else 'context')
        elif v.startswith('='):
            val, src = v[1:], 'clear'
        elif v in key or base in key:
            val = key[v] if v in key else key[base]
            src = 'null' if val == '' else 'key'
        else:
            val, src = '?', 'open'
        rows.append((i, loc, v, val, src))
    return rows


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument('stems', nargs='+')
    ap.add_argument('--key', default='key_pass.tsv')
    ap.add_argument('--validation', action='store_true')
    ap.add_argument('--show', action='store_true', help='print each manuscript line: first index, then values joined by |')
    a = ap.parse_args()
    key = load_key(os.path.join(HERE, a.key))
    os.makedirs(os.path.join(HERE, 'reading'), exist_ok=True)
    allrows = []
    for st in a.stems:
        rows = reading(st, key)
        allrows.append((st, rows))
        with open(os.path.join(HERE, 'reading', st + '.tsv'), 'w', encoding='utf-8') as f:
            f.write('# index\tline\ttoken\tvalue\tsource (key = key rebuilt from the pairs; null; clear = written in clear;'
                    ' context = read from context and alphabetical bracket; open = unread)\n')
            for r in rows:
                f.write('\t'.join(str(x) for x in r) + '\n')
        if a.show:
            line, buf, i0 = None, [], 0
            for i, loc, v, val, src in rows + [(len(rows), None, '', '', '')]:
                if loc != line:
                    if buf:
                        print(f'{line} [{i0}]: ' + '|'.join(buf))
                    line, buf, i0 = loc, [], i
                if loc is None:
                    break
                buf.append('' if src == 'null' else ('{' + v + '}' if src == 'open' else (val.upper() if src == 'clear' else val)))
        n = len(rows)
        read = sum(1 for r in rows if r[4] != 'open')
        by = {s: sum(1 for r in rows if r[4] == s) for s in ('key', 'null', 'clear', 'context', 'open')}
        print(f'{st}: {read}/{n} tokens read ({100 * read / n:.1f}%)  ' + ' '.join(f'{k}={v}' for k, v in by.items()))
    if a.validation:
        with open(os.path.join(HERE, 'validation.tsv'), 'w', encoding='utf-8') as f:
            f.write('# model: pl-1790\n# source: reading/*.tsv (the three despatches without a clear text)\n')
            f.write('# note: values from the key rebuilt on the pairs plus context readings; clear words in the cipher left out\n')
            for st, rows in allrows:
                f.write(f'# {st}\n')
                for i, loc, v, val, src in rows:
                    if src == 'clear':
                        continue
                    f.write(f'{v}\t{"-" if src == "null" else ("?" if src == "open" else val)}\n')


if __name__ == '__main__':
    main()
