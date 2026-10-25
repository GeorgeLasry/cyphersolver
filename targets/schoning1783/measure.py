"""Measure the decipherment of the letters without a clear copy (dec_*.tsv: token TAB reading).

A token counts as read if its reading is a letter, a doubled letter or a known code value; bracketed codes and '?'
are counted separately. Word dividers ('|') are left out. Usage: python measure.py
"""
import glob, os, re

HERE = os.path.dirname(os.path.abspath(__file__))
tot = {'tokens': 0, 'read': 0, 'bracket': 0, 'unread': 0, 'codes': 0, 'codes_known': 0}
for f in sorted(glob.glob(os.path.join(HERE, 'dec_*.tsv'))):
    c = dict.fromkeys(tot, 0)
    for line in open(f, encoding='utf8'):
        if line.startswith('#') or '\t' not in line:
            continue
        tok, val = line.rstrip('\n').split('\t')[:2]
        val = val.strip()
        if val == '|':
            continue
        c['tokens'] += 1
        is_code = bool(re.fullmatch(r'\d+', tok.strip()))
        c['codes'] += is_code
        if val.startswith('[bracket'):
            c['bracket'] += 1
        elif val in ('', '?') or val.endswith('?') and len(val) <= 2:
            c['unread'] += 1
        else:
            c['read'] += 1
            c['codes_known'] += is_code
    for k in tot:
        tot[k] += c[k]
    share = c['read'] / c['tokens'] if c['tokens'] else 0
    print(f"{os.path.basename(f)}: {c['tokens']} tokens, {c['read']} read ({share:.1%}), {c['bracket']} bracketed, "
          f"{c['unread']} unread; codes {c['codes_known']}/{c['codes']} known")
share = tot['read'] / tot['tokens'] if tot['tokens'] else 0
print(f"TOTAL: {tot['tokens']} tokens, {tot['read']} read ({share:.1%}), {tot['bracket']} bracketed, {tot['unread']} unread;"
      f" codes {tot['codes_known']}/{tot['codes']} known")
