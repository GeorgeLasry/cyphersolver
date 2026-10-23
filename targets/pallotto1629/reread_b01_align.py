"""Align each cipher run of a 6960 sheet with the Italian printed by Kiewning 1897 (reread batch b01).

Decode tokens (letters of 2-digit codes and key words; [nnn] unknown groups; ?d slips) are aligned to the edition's
letters in a window of lines, semi-globally (the run is consumed whole, the edition has free ends). An unknown group
may stand for 0-16 edition letters, a slip for 0-2; letters match, mismatch, or are inserted/deleted at a cost.

    python reread_b01_align.py R288 23240 23340      align R288 against edition lines 23240-23340
Writes reread_b01/<rec>_align.txt: per run, the score per letter, the decode and the edition text it lands on,
and every unknown group with the edition letters it covers.
"""
import json, os, sys
import numpy as np
HERE = os.path.dirname(os.path.abspath(__file__)); sys.path.insert(0, HERE)
import reread_b01_decode as D
from lang import lm

ED = os.path.join(HERE, 'ed', 'pallotto_bd2_1629.txt')
MIS, INS, DEL, UNK_PER, UNK_MAX, SLIP_MAX = 2.0, 1.6, 1.6, 0.15, 16, 2

def edition_window(a, b):
    lines = open(ED, encoding='utf-8').read().split('\n')[a - 1:b]
    raw = '\n'.join(lines)
    let = []; pos = []
    i = 0
    norm = lm.norm
    for i, ch in enumerate(raw):
        n = norm(ch, 'early', False)
        for c in n:
            let.append(c); pos.append(i)
    return raw, ''.join(let), pos

def tokens_of_run(toks):
    """Flatten to units: ('L', ch, tokidx) | ('U', code, tokidx) | ('S', d, tokidx)."""
    out = []
    for ti, (k, code, t) in enumerate(toks):
        if k in ('l', 'w'):
            for c in D.letters(t): out.append(('L', c, ti))
        elif k == 'u': out.append(('U', code, ti))
        elif k == 'slip': out.append(('S', code, ti))
        elif k == 'gap': out.append(('U', '…', ti))
    return out

def align(units, E):
    m = len(E); n = len(units)
    Ea = np.frombuffer(E.encode('ascii'), dtype=np.uint8)
    INF = 1e9
    Dm = np.zeros((n + 1, m + 1), dtype=np.float32)   # free start in the edition
    jj = np.arange(m + 1, dtype=np.float32)
    for i, (kind, val, _) in enumerate(units, 1):
        prev = Dm[i - 1]
        if kind == 'L':
            sub = prev[:-1] + np.where(Ea == ord(val), 0.0, MIS)
            cur = np.full(m + 1, INF, dtype=np.float32)
            cur[1:] = sub
            cur = np.minimum(cur, prev + DEL)              # decode letter not in edition
        else:
            mx = UNK_MAX if kind == 'U' else SLIP_MAX
            per = UNK_PER if kind == 'U' else 0.5
            base = 0.6 if kind == 'U' else 1.0
            cur = prev + base
            for k in range(1, mx + 1):
                c2 = np.full(m + 1, INF, dtype=np.float32); c2[k:] = prev[:-k] + base + per * k
                cur = np.minimum(cur, c2)
        # edition letters skipped inside the run (insertions): cur[j] = min(cur[j], cur[j-1] + INS)
        t = cur - jj * INS
        t = np.minimum.accumulate(t)
        cur = np.minimum(cur, t + jj * INS)
        Dm[i] = cur
    end = int(np.argmin(Dm[n])); score = float(Dm[n][end])
    # traceback
    path = []; i, j = n, end
    while i > 0:
        kind, val, _ = units[i - 1]; here = Dm[i][j]
        if kind == 'L':
            if j > 0 and abs(Dm[i - 1][j - 1] + (0.0 if E[j - 1] == val else MIS) - here) < 1e-3:
                path.append((i - 1, j - 1, j)); i -= 1; j -= 1; continue
            if abs(Dm[i - 1][j] + DEL - here) < 1e-3:
                path.append((i - 1, j, j)); i -= 1; continue
        else:
            mx = UNK_MAX if kind == 'U' else SLIP_MAX
            per = UNK_PER if kind == 'U' else 0.5
            base = 0.6 if kind == 'U' else 1.0
            done = False
            for k in range(0, mx + 1):
                if j - k >= 0 and abs(Dm[i - 1][j - k] + base + per * k - here) < 1e-3:
                    path.append((i - 1, j - k, j)); i -= 1; j -= k; done = True; break
            if done: continue
        # insertion
        j -= 1
    path.reverse()
    start = path[0][1] if path else end
    return score, start, end, path

CHUNK = 110
NL = chr(10)

def run(rec, a, b, minlen=12):
    raw, E, pos = edition_window(a, b)
    doc = D.decode_doc(rec)
    out = []; groups = []
    for si, (kind, val) in enumerate(doc):
        if kind != 'cipher':
            out.append(f'--- {kind.upper()}: {val}'); continue
        # long runs are cut into chunks of about CHUNK letters (at token boundaries) and aligned one by one,
        # because Kiewning often prints only part of a passage verbatim and gives the rest as German regest
        chunks = []; cur = []; nlc = 0
        for t in val:
            cur.append(t); nlc += len(D.letters(t[2])) if t[0] in ('l', 'w') else 0
            if nlc >= CHUNK: chunks.append(cur); cur = []; nlc = 0
        if cur:
            if chunks and nlc < CHUNK // 3: chunks[-1] += cur
            else: chunks.append(cur)
        for ci, ch in enumerate(chunks):
            _one(rec, si, ci, ch, E, raw, pos, a, out, groups, minlen)
    os.makedirs(os.path.join(HERE, 'reread_b01'), exist_ok=True)
    open(os.path.join(HERE, 'reread_b01', f'{rec}_align.txt'), 'w', encoding='utf-8').write(NL.join(out) + NL)
    json.dump(groups, open(os.path.join(HERE, 'reread_b01', f'{rec}_groups.json'), 'w', encoding='utf-8'),
              ensure_ascii=False, indent=0)
    return out, groups

def _one(rec, si, ci, val, E, raw, pos, a, out, groups, minlen):
    units = tokens_of_run(val)
    nl = sum(1 for u in units if u[0] == 'L')
    dec = D.render(val)
    if nl < minlen:
        out.append(f'### run {si}.{ci} (short, {nl} letters): {dec}'); return
    score, s, e, path = align(units, E)
    rate = score / max(1, nl)
    ed_txt = raw[pos[s]:pos[e - 1] + 1] if e > s else ''
    out.append(f'### run {si}.{ci}: {nl} letters, cost/letter {rate:.2f}, edition line ~{a + raw[:pos[s]].count(chr(10))}')
    out.append('DEC: ' + dec)
    out.append('ED : ' + ed_txt.replace(NL, ' / '))
    if rate < 0.75:
        for ui, j0, j1 in path:
            kind_u, code, ti = units[ui]
            if kind_u == 'U':
                seg = raw[pos[j0]:pos[j1 - 1] + 1] if j1 > j0 else ''
                c0 = raw[pos[max(0, j0 - 12)]:pos[j0]] if j0 > 0 else ''
                c1 = raw[pos[j1]:pos[min(len(pos) - 1, j1 + 12)]] if j1 < len(pos) else ''
                ctx = (c0 + '<' + seg + '>' + c1).replace(NL, ' ')
                groups.append({'rec': rec, 'run': f'{si}.{ci}', 'rate': round(rate, 2), 'code': code,
                               'ed': E[j0:j1], 'raw': seg.replace(NL, ' '), 'ctx': ctx})
                out.append(f'    [{code}] = {E[j0:j1]!r:20}  {ctx!r}')

if __name__ == '__main__':
    rec, a, b = sys.argv[1], int(sys.argv[2]), int(sys.argv[3])
    out, g = run(rec, a, b)
    print('\n'.join(out))
