"""Check and apply Brackx's R1128 transcription repairs (issue #121) to t1519.txt; writes t1519_r1128_repaired.txt."""
import json, re, sys
sys.stdout.reconfigure(encoding='utf-8')
rep = json.load(open('brackx/r1128_transcription_repairs.json', encoding='utf-8'))
lines = {}
order = []
for l in open('t1519.txt', encoding='utf-8'):
    m = re.match(r'^R1128 (L\d+): (.*)$', l.rstrip('\r\n'))
    if m: lines[m.group(1)] = m.group(2).split(); order.append(m.group(1))
bad = 0
for r in rep:
    toks = lines[r['line']]
    cur = toks[r['column'] - 1]
    if cur != r['old']:
        bad += 1; print('MISMATCH', r['line'], r['column'], 'file', cur, 'old', r['old'])
    toks[r['column'] - 1] = r['new']
print(len(rep), 'repairs,', bad, 'mismatches; lines touched', sorted({r['line'] for r in rep}))
with open('t1519_r1128_repaired.txt', 'w', encoding='utf-8') as f:
    for k in order: f.write(f'R1128 {k}: ' + ' '.join(lines[k]) + '\n')
