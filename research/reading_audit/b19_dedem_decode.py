"""b19 (dedem1788): decode R2122 and R2131 group by group with the codebook values read from NA 1.02.20 inv. 785
("Kroll. Un Chiffre"), targets/dedem1788/key/kroll785_values.tsv. Writes tx/<doc>_decode.txt: one line per cipher line,
each group as code=value; clear passages kept in «»; '?' groups flagged.

    python research/reading_audit/b19_dedem_decode.py
"""
import csv, pathlib, re
T = pathlib.Path(__file__).resolve().parents[2] / 'targets' / 'dedem1788'
K = {int(r['code']): r['value'] for r in csv.DictReader(open(T / 'key' / 'kroll785_values.tsv', encoding='utf8'), delimiter='\t')}
for doc in ('R2122', 'R2131'):
    out = ['# %s decoded with Kroll\'s codebook (NA 1.02.20 inv. 785), values in key/kroll785_values.tsv; b19, 23 Oct 2026.' % doc,
           '# code=value; «clear text of the letter»; <code?> = no value; ? = doubtful group in the transcription.']
    n = known = 0
    for line in open(T / 'tx' / ('%s_cipher.txt' % doc), encoding='utf8'):
        if line.startswith('#'):
            out.append(line.rstrip()); continue
        toks = []
        for t in re.findall(r'\[.*?\]|\S+', line):
            if t.startswith('['):
                toks.append('«' + t[1:-1] + '»'); continue
            c = int(re.sub(r'\D', '', t)); n += 1
            v = K.get(c)
            if v: known += 1
            toks.append('%s=%s' % (t, v.replace(' ', '_')) if v else '<%s>' % t)
        out.append(' '.join(toks))
    out.append('# %d groups, %d with a codebook value' % (n, known))
    (T / 'tx' / ('%s_decode.txt' % doc)).write_text('\n'.join(out) + '\n', encoding='utf8')
    print(doc, n, known)
