"""Beam decode with the key as extended by the contemporary decipherments (reread batch "aless", 22 Oct 2026).

Same search as decrypt.py (shared Italian model, it-cinquecento, no spaces), with what the decifrati of R94 (f. 45r),
R95 (f. 58r) and R100 (f. 280r) showed about the system:
  * 9 also stands for the syllable "con" (concesso, conscientia, contenta, comprende written conprende);
  * the dotted group 0^.0 (00.) is "et";
  * a code X0Y0 is often written X0Y when the next group starts at once (5 0 2 = per, 2 0 9 = che);
  * 3 0 9 without the dot is "qua" (quale, qua);
  * a doubled letter is enciphered once (pasato, alegati);
  * code values attested by the decipherments: 1040 lettere, 3020 quando, 3060 -mente, 4020 come, 4080 et,
    5070 and 6050 Imbasciatore, 6060 Inquisitione, 2050 Spagna; 6090 is a demonstrative (questa/queste).
usage: python reread_aless_decode.py <transcription> [image]
"""
import os, re, sys

HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, HERE)
import decrypt as D

NOM2 = dict(D.NOM)
NOM2.update({'1040': 'lettere', '3020': 'quando', '3060': 'mente', '4020': 'come', '4080': 'et',
             '5070': 'imbasciatore', '6050': 'imbasciatore', '6060': 'inquisitione', '2050': 'spagna',
             '6090': 'questa'})
DOTTED2 = {'00': 'et', '39': 'qua'}


def decode(items, beam=400):
    enc, step, A, MOD = D.enc, D.step, D.A, D.MOD
    start = 0
    for x in enc('ente'):
        start = (start * A + x) % MOD
    n = len(items)
    states = [dict() for _ in range(n + 1)]
    states[0][start] = (0.0, None)
    for p in range(n):
        if not states[p]:
            continue
        best = sorted(states[p].items(), key=lambda kv: -kv[1][0])[:beam]
        for ctx, (sc, _) in best:
            it = items[p]
            moves = []
            if isinstance(it, tuple):
                g = DOTTED2.get(it[1])
                moves.append((1, g if g is not None else '[' + it[1] + '.]', enc(g) if g else [],
                              0.0 if g is not None else -4.0))
            elif it == '?':
                moves.append((1, '?', [], -3.0))
            elif it == '0':
                moves.append((1, '', [], D.NULL_COST))
            else:
                for ch in D.POLY[it]:
                    moves.append((1, ch, enc(ch), 0.0))
                    moves.append((1, ch + ch, enc(ch + ch), -0.7))
                if it == '9':
                    moves.append((1, 'con', enc('con'), -0.5))
                seg = items[p:p + 4]
                if len(seg) == 4 and all(isinstance(x, str) for x in seg):
                    code = ''.join(seg)
                    if code in NOM2:
                        pt = NOM2[code]
                        moves.append((4, '[' + pt.upper() + ']', enc(pt), D.NOM_BONUS))
                    elif seg[1] == '0' and seg[3] == '0' and seg[0] not in '0?' and seg[2] not in '0?':
                        moves.append((4, '[' + code + ']', [], -6.0))
                seg = items[p:p + 3]
                if len(seg) == 3 and all(isinstance(x, str) for x in seg) and seg[1] == '0':
                    code = ''.join(seg)
                    if code == '309':
                        moves.append((3, 'qua', enc('qua'), 0.5))
                    if code + '0' in NOM2:
                        pt = NOM2[code + '0']
                        moves.append((3, '[' + pt.upper() + ']', enc(pt), 0.3))
            for L, txt, chars, pen in moves:
                nctx, s = step(ctx, chars)
                ns = sc + s + pen
                q = p + L
                old = states[q].get(nctx)
                if old is None or ns > old[0]:
                    states[q][nctx] = (ns, (p, ctx, txt))
    end = max(states[n].items(), key=lambda kv: kv[1][0])
    out, q, ctx = [], n, end[0]
    trace = []
    while states[q][ctx][1] is not None:
        p, pctx, txt = states[q][ctx][1]
        out.append(txt)
        trace.append((p, txt))
        q, ctx = p, pctx
    decode.trace = list(reversed(trace))
    return ''.join(reversed(out)), end[1][0] / max(1, n)


def row_items(path, img):
    out, cur = [], None
    for line in open(path, encoding='utf-8', errors='replace'):
        m = re.match(r'#IMAGE NAME:\s*(\S+)', line)
        if m:
            cur = m.group(1); continue
        if line.startswith('#') or cur != img or not re.search(r'\d', line):
            continue
        import tempfile
        with tempfile.NamedTemporaryFile('w', suffix='.txt', delete=False, encoding='utf-8') as f:
            f.write('#IMAGE NAME: x\n' + line)
        n = sum(len(it) for _, it in D.parse(f.name))
        os.unlink(f.name)
        out.append(n)
    return out


if __name__ == '__main__':
    for img, items in D.parse(sys.argv[1]):
        if len(sys.argv) > 2 and img != sys.argv[2]:
            continue
        txt, per = decode(items)
        print('== %s (%d items, %.2f/item)' % (img, len(items), per))
        if '--rows' in sys.argv:
            # row boundaries: count items per transcription line
            rows = row_items(sys.argv[1], img)
            k = 0
            bounds = []
            for r in rows:
                k += r; bounds.append(k)
            cur, r, line, figs = 0, 0, [], []
            for p, t in decode.trace:
                while r < len(bounds) and p >= bounds[r]:
                    print('%2d | %s' % (r + 1, ''.join(line))); line = []; r += 1
                line.append(t if t else '.')
            print('%2d | %s' % (r + 1, ''.join(line)))
        else:
            print(txt)
