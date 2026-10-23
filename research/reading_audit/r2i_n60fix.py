"""r2i: apply the 23 Oct 2026 sign-by-sign proofread of N.60 pp. 4-14 (n60_corrections_r2i.tsv) to
n60_transcription_v4.txt -> n60_transcription_v5.txt. Rules: line/old/new/nth (nth = occurrence of the token sequence
`old` in the v4 line, counted on v4); ALL (every 'oo X' -> 'oo T'); OX_H / OX_GO / PENSION list their lines in the nth
column. new '-' deletes the tokens. Prints each changed line before/after with its decode."""
import re, sys, pathlib
T = pathlib.Path(__file__).resolve().parents[2] / 'targets' / 'vich1511'
sys.path.insert(0, str(T)); import decode as D
rules = [l.rstrip('\n').split('\t') for l in open(T / 'n60_corrections_r2i.tsv', encoding='utf8')][1:]
src = open(T / 'n60_transcription_v4.txt', encoding='utf8').read().splitlines()
def dec(toks): return ''.join((D.CODE.get(t.rstrip('?')) or D.LET.get(t.rstrip('?')) or '['+t+']') for t in toks)
def occ(toks, seq):
    return [i for i in range(len(toks)-len(seq)+1) if [t for t in toks[i:i+len(seq)]] == seq]
out, n = [], 0
for line in src:
    m = re.match(r'(L\d{4}):(.*)', line)
    if not m: out.append(line); continue
    lab, toks = m.group(1), m.group(2).split()
    edits = {}
    for r in rules:
        key, old, new, nth = r[0], r[1], r[2], r[3]
        if key == 'ALL':
            for i in occ(toks, ['oo', 'X']): edits[i+1] = (1, ['T'])
        elif key in ('OX_H', 'OX_GO', 'PENSION'):
            labs = []
            for p in nth.split(','):
                mm = re.match(r'(L\d{4})(?:x(\d))?', p); labs.append(mm.group(1))
            if lab in labs:
                seq = old.split()
                for i in occ(toks, seq):
                    edits[i] = (len(seq), new.split())
        elif key == lab and old != '-':
            seq = old.split(); o = occ(toks, seq); k = int(nth) - 1
            if k < len(o): edits[o[k]] = (len(seq), [] if new == '-' else new.split())
            else: print('!! no occurrence', r)
    if edits:
        new_t, i = [], 0
        while i < len(toks):
            if i in edits:
                ln, rep = edits[i]; new_t += rep; i += ln
            else: new_t.append(toks[i]); i += 1
        if new_t != toks:
            n += 1
            if '-v' in sys.argv: print(lab, dec(toks), '\n     ->', dec(new_t))
        toks = new_t
    out.append('%s: %s' % (lab, ' '.join(toks)))
hdr = '# r2i (23 Oct 2026): sign-by-sign proofread of pp. 4-14 on 4x bands; n60_corrections_r2i.tsv applied to v4 by research/reading_audit/r2i_n60fix.py\n'
open(T / 'n60_transcription_v5.txt', 'w', encoding='utf8').write(hdr + '\n'.join(out) + '\n')
print('lines changed', n)
