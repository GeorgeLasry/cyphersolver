"""b08: word-by-word check of a malsburg1637 reading against its decode (brief step 3).

    python b08_align.py <reading.md> <f0NN.txt> [...]

Every word of the '## Reading' body that is not inside [ ], { }, < > or the clear-text marks ⟨ ⟩ (or *...* for the
French letter, where only the italics are cipher) is looked up in the decode of the transcription files: letters only,
u/v and i/j/y merged, umlauts folded, the clear words of the transcription included. A word is found when it (or the
writer's form it was normalised from, b08_norm.MAP) occurs in that stream. Words not found are printed: each must be
bracketed in the reading or explained in its notes.
"""
import re, sys, pathlib, unicodedata
sys.path.insert(0, str(pathlib.Path(__file__).parent))
from b08_dec import load, dec  # noqa
from b08_norm import MAP  # noqa

INV = {}
for k, v in MAP.items():
    INV.setdefault(v, []).append(k)


def fold(s):
    s = unicodedata.normalize('NFKD', s.lower())
    s = ''.join(c for c in s if not unicodedata.combining(c))
    s = s.replace('v', 'u').replace('j', 'i').replace('y', 'i').replace('ß', 'ss')
    return re.sub(r'[^a-z]', '', s)


rd, files = sys.argv[1], sys.argv[2:]
T = pathlib.Path(__file__).resolve().parents[2] / 'targets' / 'malsburg1637'
stream = ''
for f in files:
    for line in load(T / f):
        if line.startswith('#'):
            continue
        d, _ = dec(line)
        stream += fold(re.sub(r'\[[^\]]*\]', '', d))
t = pathlib.Path(rd).read_text(encoding='utf8')
body = re.search(r'^## Reading[^\n]*\n(.*?)(?=^## |\Z)', t, re.S | re.M).group(1)
italic = '*' in body
if italic:
    body = ' '.join(re.findall(r'\*([^*]+)\*', body))
body = re.sub(r'⟨[^⟩]*⟩|\[[^\]]*\]|\{[^}]*\}|<[^>]*>', ' ', body)
miss = []
for w in re.findall(r"[^\W\d_]+", body):
    forms = [w] + INV.get(w, [])
    if not any(fold(x) and fold(x) in stream for x in forms):
        miss.append(w)
print(rd, 'words not found in the decode:', len(miss))
print(' '.join(miss))
