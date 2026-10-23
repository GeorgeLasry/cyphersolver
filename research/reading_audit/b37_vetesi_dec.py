"""b37: decode R473 (vetesi1705) with Rákóczi's Hungarian key DECODE R446 (RAD_ARCH_Rakoczi_C64_4d2_25_6) and set
each group against the contemporary interlinear gloss.  python b37_vetesi_dec.py  -> targets/vetesi1705/R473_key_vs_gloss.tsv
Key: DECODE's transcription of R446 (targets/vetesi1705/key/DOC_R446_D2629_2629.txt) with corrections read on the R446
image (b37): 69 al, 71 an, 72 ar, 73 as, 74 at (DECODE: 69 ac, 71-74 shifted); 75-77 az; 106/107 és (DECODE: '107 - es iob');
80/32/58 = Ö and 70/33/59 = Ü (DECODE: O, U); 35 = LY, 36 = GY (DECODE: 36 twice); groups not in the key = nulls (9 and 8 head the
null columns 'x' on the key)."""
import re, pathlib
T = pathlib.Path(__file__).resolve().parents[2] / 'targets' / 'vetesi1705'
key = {}
for line in (T / 'key' / 'DOC_R446_D2629_2629.txt').read_text(encoding='utf-8-sig').splitlines():
    m = re.match(r'\s*([\d|]+)\s*-\s*(.+?)\s*$', line)
    if m:
        for c in m.group(1).split('|'):
            if c: key[c] = m.group(2).strip()
key.update({'69': 'al', '71': 'an', '72': 'ar', '73': 'as', '74': 'at', '75': 'az', '76': 'az', '77': 'az', '106': 'és', '107': 'és',
            '80': 'Ö', '32': 'Ö', '58': 'Ö', '70': 'Ü', '33': 'Ü', '59': 'Ü', '35': 'LY', '36': 'GY', '9': '(null x)', '8': '(null)',
            '2670': 'Nagyságod', '296': 'Belgium', '00': 'Kegyelmes', '1190': 'Kegyelmes Uram', '6670': 'Méltóságos', '262': 'Király'})
rows = ['page\tgroup\tkey R446\tgloss\tagree']
for page, line in [(m.group(0)[:0], l) for l in (T / 'R473_transcription.txt').read_text(encoding='utf8').splitlines() if not l.startswith('#') for m in [re.match('', l)]]:
    for run in re.finditer(r'\{([\dA-Z.()?]+)\s*=\s*([^}]*)\}', line):
        gs = run.group(1).split('.'); gl = run.group(2).split('|')
        if len(gl) != len(gs): gl = [run.group(2)] + [''] * (len(gs) - 1)
        for g, s in zip(gs, gl):
            g2 = re.sub(r'\(.*?\)', '', g)
            v = key.get(g2, '(not in key)')
            s = s.strip()
            a = '' if s in ('', '-') else ('yes' if re.sub(r'[^a-zöüőűéáíóú]', '', v.lower().replace('j', 'i')) [:len(re.sub(r'[^a-zöüőűéáíóú]', '', s.lower()))] == re.sub(r'[^a-zöüőűéáíóú]', '', s.lower().replace('j','i')) else 'NO')
            rows.append(f'\t{g}\t{v}\t{s}\t{a}')
(T / 'R473_key_vs_gloss.tsv').write_text('\n'.join(rows) + '\n', encoding='utf8')
n = sum(1 for r in rows[1:] if r.endswith('\tyes')); x = sum(1 for r in rows[1:] if r.endswith('\tNO'))
# running decode per run, for the reading
out = []
for l in (T / 'R473_transcription.txt').read_text(encoding='utf8').splitlines():
    if l.startswith('#'): continue
    def dec(m):
        vals = []
        for g in m.group(1).split('.'):
            g2 = re.sub(r'\(.*?\)', '', g); v = key.get(g2)
            vals.append('·' if v is None or v.startswith('(null') else v.lower())
        return '<' + ''.join(vals) + '>'
    out.append(re.sub(r'\{([\dA-Z.()?]+)\s*=\s*[^}]*\}', dec, l))
(T / 'R473_decode_R446.txt').write_text('# R473 decoded with key R446 (b37_vetesi_dec.py); <...> = a cipher run, . = null/not in key' + chr(10) + chr(10).join(out) + chr(10), encoding='utf8')
print('groups', len(rows) - 1, 'gloss agrees', n, 'disagrees', x)
for r in rows[1:]:
    if r.endswith('NO'): print(r)
