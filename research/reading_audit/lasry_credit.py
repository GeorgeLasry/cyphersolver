"""Insert the Lasry credit line after the first heading (or at the top) of reading/English files. Idempotent."""
import sys, pathlib
LINE = "Credit: George Lasry (decryption on DECODE, used with his permission, 24 Oct 2026)"
for f in sys.argv[1:]:
    p = pathlib.Path(f); s = p.read_text(encoding='utf8')
    if 'used with his permission, 24 Oct 2026' in s: continue
    L = s.split('\n')
    i = next((k for k, l in enumerate(L) if l.startswith('# ')), -1)
    L.insert(i + 1, ('\n' if i >= 0 else '') + LINE + ('' if i >= 0 else '\n'))
    p.write_text('\n'.join(L), encoding='utf8', newline=''); print('credited', f)
