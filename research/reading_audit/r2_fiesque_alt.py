"""r2_fiesque helper: upper bound on look-alike alternates in a reading: align the reading's letters (bracketed words,
header and notes cut) with the key decode's letters (codes expanded, QUEL/QUIL as quil) and count substituted letters.
Substitutions include transcription slips and spelling choices as well as look-alike readings, so this is an upper bound.
usage: python r2_fiesque_alt.py <reading.md> <decoded or r2 transcription files ...>"""
import sys, re, difflib, unicodedata, subprocess, pathlib
def letters(s):
    s = unicodedata.normalize('NFD', s.lower()); return re.sub(r'[^a-z]', '', s)
raw = open(sys.argv[1], encoding='utf-8').read()
raw = re.sub(r'<!--.*?-->', ' ', raw, flags=re.S); raw = re.split(r'^## Notes', raw, flags=re.M)[0]
raw = re.sub(r'^#.*$', ' ', raw, flags=re.M); raw = re.sub(r'⟨[^⟩]*⟩', ' ', raw)
raw = re.sub(r'\[[^\]]*\]', ' ', raw)   # bracketed words do not rest on figures
R = letters(raw.replace('j', 'i').replace('v', 'u'))
D = ''
for f in sys.argv[2:]:
    if 'transcription' in f:
        out = subprocess.run([sys.executable, str(pathlib.Path(__file__).with_name('r2_fiesque_dec.py')), f, 'Dz=con'],
                             capture_output=True, text=True, encoding='utf-8').stdout
    else:
        out = open(f, encoding='utf-8').read()
    for ln in out.splitlines():
        m = re.match(r'c\w+\s+(.*)', ln)
        if m: D += letters(m.group(1).replace('QUEL/QUIL', 'quil').replace('j', 'i').replace('v', 'u'))
sm = difflib.SequenceMatcher(None, R, D, autojunk=False)
sub = sum(max(i2 - i1, j2 - j1) for t, i1, i2, j1, j2 in sm.get_opcodes() if t == 'replace' and (i2 - i1) == (j2 - j1))
eq = sum(i2 - i1 for t, i1, i2, j1, j2 in sm.get_opcodes() if t == 'equal')
print(f'reading letters {len(R)}, decode letters {len(D)}, equal {eq}, one-for-one substitutions {sub} ({sub/max(len(R),1):.1%})')
