"""r2_fiesque helper: score a fiesque1567 reading body chunk by chunk (docs/_check_reading.py logic).
usage: python r2_fiesque_holes.py <file> [--holes] [--extra] [-v]
 --holes  only explicit holes ([...], [?word], [Dz]) count, every other word known (b17 HOLES=1 figure)
 --extra  add to the fr word list the words seen 3+ times in this target's other readings (read/*_reading.md except
          the file itself): Fiesque's own period spellings (estoict, unyon, crestienté ...); supplementary figure only
 (the header comment and any ## Notes section are cut off before scoring)
 -v       list each chunk with its unknown words"""
import sys, re, pathlib, collections, glob
ROOT = pathlib.Path(__file__).resolve().parents[2]
sys.path.insert(0, str(ROOT / 'docs')); sys.path.insert(0, str(ROOT))
import _check_reading as C
from lang import lm
f = sys.argv[1]; holes = '--holes' in sys.argv; extra = '--extra' in sys.argv; V = '-v' in sys.argv
raw = open(f, encoding='utf-8').read()
# body only: drop <!-- --> blocks and everything from a '## Notes' heading on
raw = re.sub(r'<!--.*?-->', ' ', raw, flags=re.S); raw = re.split(r'^## Notes', raw, flags=re.M)[0]
text = C.CODE.sub(' CODEWORD ', C.clean_text(raw))
lex = dict(C.lexicon('fr'))
if extra:
    c = collections.Counter()
    for g in glob.glob(str(ROOT / 'targets/fiesque1567/read/*_reading.md')):
        if pathlib.Path(g).resolve() == pathlib.Path(f).resolve(): continue
        body = C.clean_text(open(g, encoding='utf-8').read())
        body = re.sub(r'\[[^\]]*\]', ' ', body)
        c.update(lm.norm(body, 'early').split())
    lex.update({w: n for w, n in c.items() if n >= 3 and len(w) >= 3})
clean = n = 0
for s in C.sentences(text):
    ws = [(w, g) for t in s for w, g in C.words_of(t)]
    bad = [w for w, g in ws if g or (not holes and w not in lex and w != 'codeword')]
    ok = len(bad) <= max(1, len(ws) // 10); clean += ok; n += 1
    if V: print('OK ' if ok else 'BAD', len(ws), bad, '|', ' '.join(s)[:90])
print(f'{f}: clean {clean}/{n} = {clean/max(n,1):.2f}' + (' (holes only)' if holes else '') + (' (+target spellings)' if extra else ''))
