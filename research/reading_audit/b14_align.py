"""b14: check a hm1645 reading against the key decode, letter by letter: reading words supplied in [brackets] are
dropped, {code}/[?code] values kept, everything lower-cased to letters; difflib lists the stretches of the reading the
decode does not carry (spelling modernisations and the corrected slips show up here and are checked by eye).

    python research/reading_audit/b14_align.py <DOC dir> <section> <reading.md>
"""
import re, sys, subprocess, difflib, pathlib
D, sec, rf = sys.argv[1:4]
out = subprocess.run([sys.executable, str(pathlib.Path(__file__).with_name('b14_hm.py')), D, sec], capture_output=True, text=True, encoding='utf8', errors='replace', env={**__import__('os').environ, 'PYTHONUTF8': '1'}).stdout
dec = ' '.join(l.split('K:', 1)[1].split('  **')[0] for l in out.splitlines() if ' K: ' in l)
dec = re.sub(r'<[^>]*>', ' ', dec).replace('{', '').replace('}', '')
t = pathlib.Path(rf).read_text(encoding='utf8')
body = re.search(r'^## Reading[^\n]*\n(.*?)(?=^## |\Z)', t, re.S | re.M).group(1)
body = re.sub(r'\[\?([^\]]+)\]', r'\1', body)
body = re.sub(r'\[[^\]]*\]', ' ', body).replace('{', '').replace('}', '')
a = re.sub(r'[^a-z]', '', body.lower()); b = re.sub(r'[^a-z]', '', dec.lower())
sm = difflib.SequenceMatcher(None, a, b, autojunk=False)
n = 0
for op, i1, i2, j1, j2 in sm.get_opcodes():
    if op == 'equal': continue
    n += 1
    print('%-7s reading %-22r decode %-22r  ...%s...' % (op, a[i1:i2][:22], b[j1:j2][:22], a[max(0, i1 - 15):i2 + 5]))
print('matched letters %d of reading %d (%.3f); diff spans %d' % (sum(x.size for x in sm.get_matching_blocks()), len(a), sum(x.size for x in sm.get_matching_blocks()) / len(a), n))
