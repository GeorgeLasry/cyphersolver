"""Apply the reciprocal Rosamonde substitution (Brice Dudout's key) to ciphertext_checked.txt."""
import pathlib, sys
PAIRS = 'au bg cs eo fj hy ir kz lt mw nv qx'.split()
KEY = {c: c for c in 'dp'}
for a, b in PAIRS:
    KEY[a], KEY[b] = b, a
assert len(KEY) == 26
src = pathlib.Path(sys.argv[1] if len(sys.argv) > 1 else pathlib.Path(__file__).with_name('ciphertext_checked.txt'))
for line in src.read_text(encoding='utf-8').splitlines():
    if line.startswith('#') or not line.strip():
        print(line); continue
    print(' '.join(''.join(KEY.get(ch, ch) for ch in w) for w in line.split()))
