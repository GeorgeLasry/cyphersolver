"""Show the codes behind a decoded stretch: python reread_b01_show.py R286 'col {Signor} di' [n_tokens]"""
import os, sys
HERE = os.path.dirname(os.path.abspath(__file__)); sys.path.insert(0, HERE)
import reread_b01_decode as D
rec, pat = sys.argv[1], sys.argv[2]; n = int(sys.argv[3]) if len(sys.argv) > 3 else 25
for si, (k, v) in enumerate(D.decode_doc(rec)):
    if k != 'cipher': continue
    r = D.render(v)
    # find token index whose render prefix contains pat
    acc = ''
    for ti in range(len(v)):
        acc = D.render(v[:ti + 1])
        if pat in acc:
            st = max(0, ti - 8)
            print(f'run {si} tok {ti}:', ' '.join(f"{c}={t if t else ('|' if kk=='null' else '?')}" for kk, c, t in v[st:st + n]))
            break
