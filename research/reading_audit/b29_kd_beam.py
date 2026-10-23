"""b29: Kauderbach R1954 -- decode the transcription choosing between look-alike digits by a French LM.

    cd targets/kauderbach1754 && PYTHONUTF8=1 python ../../research/reading_audit/b29_kd_beam.py trans/R1954.txt [beam]

The transcription marks an uncertain digit with '?' after it (TRANSCRIBE_BRIEF: 5/7 'zeta', 8/9 open-top y,
4/11 u-shape; also 1/7 and 0/6). Each marked digit becomes a slot with its look-alike alternative; unmarked digits are
taken as written. Digits 5 and 8 are nulls (NOTES item 4); the rest pair into 2-digit codes (key.json); a digit may be
skipped as a stray at a penalty (as decode.py). A beam search over the alternatives and the pair phase is scored by a
French 5-gram model (lang fr-modern, no spaces) plus a small bonus for the transcriber's first choice.
Prints, per cipher chunk: the decode with code boundaries, and every slot where the alternative was taken.
"""
import json, re, sys, os
sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__)), '..', '..'))
from lang import lm

K = json.load(open('key.json'))
M = lm.load('fr-modern', order=5, spaces=False)
A = M.A; IDX = M.index; LP = M.lp; O = M.order
BEAM = int(sys.argv[2]) if len(sys.argv) > 2 else 600
FIRST_BONUS, SKIP_PEN, UNK_PEN = 0.7, float(os.environ.get("SKIP", 7.0)), float(os.environ.get("UNK", 9.0))
ALT = {'5': '7', '7': '5', '8': '9', '9': '8', '4': '11', '1': '7', '6': '0', '0': '6'}


LINE_OF = {}
RES = []
ALTL = []


def slots_of(chunk, line0=0):
    """chunk text -> list of (primary, alternative or None); LINE_OF[id(list)] gives the file line of each slot"""
    out = []; lines = []; i = 0; s = chunk; ln = line0
    while i < len(s):
        c = s[i]
        if c == '\n': ln += 1
        if not c.isdigit(): i += 1; continue
        lines.append(ln)
        if s[i:i + 3] == '11!':
            out.append(('11*', None)); i += 3; continue
        if i + 1 < len(s) and s[i + 1] == '!':
            out.append((c + '*', None)); i += 2; continue
        if s[i:i + 3] == '11?':
            out.append(('11', '4')); i += 3; continue
        if i + 1 < len(s) and s[i + 1] == '?':
            out.append((c, ALT.get(c))); i += 2; continue
        out.append((c, None)); i += 1
    LINE_OF[id(out)] = lines
    return out


def lp_text(ctx, text):
    """incremental log-prob of text after ctx (tuple of char indices)"""
    sc = 0.0; ctx = list(ctx)
    for ch in text:
        if ch not in IDX: continue
        x = IDX[ch]
        if len(ctx) >= O - 1:
            k = 0
            for c in ctx[-(O - 1):]: k = k * A + c
            sc += float(LP[k * A + x])
        else:
            sc += -3.0
        ctx.append(x)
    return sc, tuple(ctx[-(O - 1):])


def step_digit(state, d, si=0, alt=False):
    """yield new states after feeding one digit"""
    score, buf, ctx, out, alts = state
    if d in '58':
        yield (score, buf, ctx, out, alts); return
    yield (score - SKIP_PEN, buf, ctx, out + [('{' + d + '}', si, alt)], alts)      # stray digit
    if buf is None:
        yield (score, (d, alt), ctx, out, alts)
    else:
        code = buf[0] + d; a2 = alt or buf[1]
        if code in K:
            t = K[code]; s2, c2 = lp_text(ctx, t)
            yield (score + s2, None, c2, out + [(t.upper() if a2 else t, si, a2)], alts)
        else:
            yield (score - UNK_PEN, None, ctx, out + [('<' + code + '>', si, a2)], alts)


def decode_chunk(chunk, ctx0=(), line0=0):
    sl = slots_of(chunk, line0)
    beam = [(0.0, None, ctx0, [], [])]
    for si, (p, a) in enumerate(sl):
        cand = []
        for st in beam:
            for choice, bonus in ((p, FIRST_BONUS), (a, 0.0)):
                if choice is None: continue
                sts = [(st[0] + bonus, st[1], st[2], st[3], st[4] + ([(si, p, choice)] if choice != p else []))]
                flag = choice != p or choice.endswith('*')   # '*' = look-alike alternative fixed in the b29 file ('d!')
                for d in choice.rstrip('*'):
                    sts = [n for s_ in sts for n in step_digit(s_, d, si, flag)]
                cand.extend(sts)
        best = {}
        for c in cand:
            key = (c[1], c[2])
            if key not in best or c[0] > best[key][0]: best[key] = c
        beam = sorted(best.values(), key=lambda x: -x[0])[:BEAM]
    b = max(beam, key=lambda x: x[0])
    return b, sl


if __name__ == '__main__':
    t = open(sys.argv[1], encoding='utf-8-sig').read()
    t = re.sub(r'#[^\n]*', '', t)
    parts = re.split(r'(<CLEARTEXT[^>]*>)', t)
    ctx = (); total_alt = 0; line = 1
    for p in parts:
        if p.startswith('<CLEARTEXT'):
            print('[' + p[13:-1].strip()[:70] + ']'); line += p.count('\n'); continue
        if not re.search(r'\d', p): line += p.count('\n'); continue
        b, sl = decode_chunk(p, ctx, line)
        if os.environ.get('RESOLVE'):
            chosen = {si: ch for si, pr, ch in b[4]}
            RES.append((p, sl, chosen))
        line += p.count('\n')
        ctx = b[2]
        lines = {}
        for tok, si, a2 in b[3]:
            lines.setdefault(LINE_OF[id(sl)][si], []).append(tok)
        for ln in sorted(lines): print('L%02d  ' % ln + '.'.join(lines[ln]))
        nalt_letters = sum(len(tok) for tok, si, a2 in b[3] if a2 and not tok.startswith(('{', '<')))
        print('   letters resting on an alternative here:', nalt_letters); ALTL.append(nalt_letters)
        for si, pr, ch in b[4]:
            print('   alt slot %d: %s -> %s' % (si, pr, ch))
        total_alt += len(b[4])
    print('alternatives taken:', total_alt, 'letters resting on an alternative:', sum(ALTL))
    if os.environ.get('RESOLVE'):
        # rewrite the transcription with every '?' slot resolved: 'd!' = the look-alike alternative was taken, 'd' = kept
        out = []; k = 0
        for p in parts:
            if p.startswith('<CLEARTEXT') or not re.search(r'\d', p) or k >= len(RES) or RES[k][0] is not p:
                out.append(p); continue
            _, sl, chosen = RES[k]; k += 1
            buf = []; i = 0; si = 0; s_ = p
            while i < len(s_):
                c = s_[i]
                if not c.isdigit(): buf.append(c); i += 1; continue
                if s_[i:i + 3] == '11?': n = 3
                elif i + 1 < len(s_) and s_[i + 1] == '?': n = 2
                else: n = 1
                if n == 1: buf.append(c)
                else: buf.append(chosen[si] + '!' if si in chosen else s_[i:i + n - 1] + '=')
                si += 1; i += n
            out.append(''.join(buf))
        open(os.environ['RESOLVE'], 'w', encoding='utf-8').write(''.join(out))
