"""Apply code values found in the sibling files (code_values_new.tsv) to the bracketed code tokens of dec_*.tsv.

A token whose reading is "[bracket: ...]" and whose number has a high- or medium-confidence value in
code_values_new.tsv gets that value, written as "<value> {sib}" so the source stays visible. Low-confidence values
and conflicts are left bracketed. Prints what changed. Usage: python apply_values.py [--dry]
"""
import glob, os, re, sys

HERE = os.path.dirname(os.path.abspath(__file__))
vals = {}
for line in open(os.path.join(HERE, 'code_values_new.tsv'), encoding='utf8'):
    if line.startswith('#') or line.startswith('number') or '\t' not in line:
        continue
    parts = line.rstrip('\n').split('\t')
    if len(parts) < 4:
        continue
    num, value, src, conf = parts[:4]
    conf = conf.strip().lower()
    if not num.strip().isdigit() or conf.startswith('low'):
        continue
    value = value.split('|')[0]
    value = re.sub(r'\(no gloss\)|\([^)]*\)', '', value).strip()
    if not value or '?' in value:
        continue
    vals[num.strip()] = value

dry = '--dry' in sys.argv
changed = 0
for f in sorted(glob.glob(os.path.join(HERE, 'dec_*.tsv'))):
    out = []
    for line in open(f, encoding='utf8'):
        if not line.startswith('#') and '\t' in line:
            tok, rest = line.split('\t', 1)
            if rest.startswith('[bracket') and tok.strip() in vals:
                line = f"{tok}\t{vals[tok.strip()]} {{sib}}\n"
                changed += 1
                print(os.path.basename(f), tok.strip(), '->', vals[tok.strip()])
        out.append(line)
    if not dry:
        open(f, 'w', encoding='utf8').writelines(out)
print(changed, 'bracketed tokens given a sibling value;', len(vals), 'values usable')
