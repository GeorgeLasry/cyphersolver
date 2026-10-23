"""v3 verify (a), gilino1527: running text of reading_r8572.txt (P-lines in reading order) -> r8572_reading.md.
The normalised forms in [square brackets] are dropped (they gloss the deciphered spelling; the deciphered spelling is the
reading); <x> supplied letters become [x] part-word holes; word(?) stays (a hole); [tok] unread tokens stay [tok] holes;
{clear} written «clear».

    python research/reading_audit/v3a_gilino.py
"""
import re, pathlib
ROOT = pathlib.Path(__file__).resolve().parents[2]
T = ROOT / 'targets/gilino1527'
L = (T / 'reading_r8572.txt').read_text(encoding='utf8').splitlines()
out = ''
for l in L:
    m = re.match(r'^P\d+\.\d+\s+(.*)$', l)
    if not m: continue
    t = m.group(1).rstrip()
    t = re.sub(r'\s*\[(?:= ?)?[^\]\d]*[a-zà-ù][^\]]*\]', lambda mm: '' if not re.fullmatch(r'\s*\[\d+\]', mm.group(0)) else mm.group(0), t)
    t = re.sub(r'<([^>]*)>', r'[\1]', t)
    t = re.sub(r'\{([^}]*)\}', r'«\1»', t)
    if out.endswith('-'):
        out = out[:-1] + t.lstrip('-')
    else:
        out += ' ' + t.lstrip('-')
out = re.sub(r'\s+', ' ', out).strip()
head = """# R8572 - "el Gilino" to Francesco II Sforza, Paredes de Nava, 15 Sept 1527: reading in running text

Rests on: `reading_r8572.txt` (key DECODE R5258 plus context values, built by build_reading.py, 9 Oct 2026), joined
here into running text in its reading order (P1 P2 P7 P3 P5 P4 P6 P8 P9) for the v3 verification (23 Oct 2026). The
deciphered spelling is the reading; the normalised forms that reading_r8572.txt adds in [square brackets] are left out
(they gloss, they are not in the figures). Letters supplied there as <x> are [x] here (part-word holes); word(?) is a
doubtful word; [token] an unread token; «...» clear text in the manuscript.

## Reading

"""
(T / 'r8572_reading.md').write_text(head + out + '\n', encoding='utf8')
print(out[:1200])
