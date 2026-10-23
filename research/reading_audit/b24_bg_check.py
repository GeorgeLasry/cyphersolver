"""b24 (bergamo1585): word check of R16_reading.md against the b24 decode (letters, u=v, 29 'et' or 'che', 26ꜧ che/chi)."""
import re, pathlib, unicodedata
T = pathlib.Path(__file__).resolve().parents[2] / 'targets' / 'bergamo1585'
def nz(s):
    s = unicodedata.normalize('NFD', s); s = ''.join(c for c in s if not unicodedata.combining(c)).lower()
    return re.sub(r'[^a-z]', '', s).replace('v', 'u')
dec = (T / 'R16_decode_b24.txt').read_text(encoding='utf8').split('\n')[0]
stream = nz(dec.replace('che', 'chi|').replace('|', ''))  # allow chi for che
stream2 = nz(dec)
t = (T / 'R16_reading.md').read_text(encoding='utf8')
body = re.search(r'^## Reading[^\n]*\n(.*?)(?=^## |\Z)', t, re.S | re.M).group(1)
miss, n = [], 0
for w in re.findall(r"\[[^\]]*\]|[A-Za-zÀ-ÿ']+", body):
    if w.startswith('['): continue
    for part in w.split("'"):
        x = nz(part)
        if not x: continue
        n += 1
        if x not in stream and x not in stream2: miss.append(part)
print('words', n, 'not in decode stream', len(miss), miss)
