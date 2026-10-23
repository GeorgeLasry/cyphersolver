"""r2i: print the N.60 transcription lines likely inside a 4x proofreading band (page p, band k, 115-px step from y=150),
with each token's decode, for a sign-by-sign check against the band image.   python r2i_n60show.py <page> <band>"""
import sys, re, pathlib
T = pathlib.Path(__file__).resolve().parents[2] / 'targets' / 'vich1511'
sys.path.insert(0, str(T))
import decode as D
p, k = int(sys.argv[1]), int(sys.argv[2])
lines = [l for l in open(T / 'n60_transcription_v4.txt', encoding='utf8') if re.match(r'L%02d\d\d:' % p, l)]
B = {l.split(' | ')[0]: l.split(' | ',1)[1].strip() for l in open(T / 'n60_build.txt', encoding='utf8') if re.match(r'L\d{4} \|', l)}
lo, hi = max(0, 3 * k - 1), min(len(lines), 3 * k + 5)
for l in lines[lo:hi]:
    lab, toks = l.split(':', 1)
    out = []
    for t in toks.split():
        b = t.rstrip('?')
        v = D.CODE.get(b) or D.LET.get(b) or '?'
        out.append('%s=%s' % (t, v))
    print(lab, ' '.join(out))
    print('   >', B.get(lab, ''))
