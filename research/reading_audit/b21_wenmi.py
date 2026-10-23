"""b21 (REREAD_BRIEF): numeric1916 gongmi / rongmi readings from Brice Dudout's proposed readings, checked group by group.

    python -I research/reading_audit/b21_wenmi.py <messages.json> <family> <out_dir>

messages.json is his current solver/numeric1916/data/messages.json (github.com/bdudout/wenmi, CC BY 4.0), fetched into
the session scratchpad. For each telegram of the family:
  * the digit groups are decoded with targets/numeric1916/decode.py (our independent decoder, his key statements);
  * his 'reading_published' is cut into units: a plain character, {x} (his replacement of an anomalous character),
    〔x〕 (kept, unresolved), punctuation; the units are aligned one to one with the decoded groups (difflib where the
    counts differ);
  * every plain character is checked against the decode (it must be the figure's own value);
  * every {x} is tested: does a variant of the cipher group differing in one digit decode to x? -> 'one-digit
    alternate' (the character rests on a look-alike reading of one digit, kept unbracketed and counted); else
    'contextual' -> [x] (supplied, nothing in the figures carries it);
  * 〔x〕 -> [?x]; □ or … -> […].
Writes <out_dir>/<family>_reading_body.txt (one block per telegram), <family>_align.tsv (group, cipher, decode, reading
unit, kind) and prints the counts.
"""
import difflib, json, re, sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
sys.path.insert(0, str(ROOT / 'targets' / 'numeric1916'))
import decode as D  # noqa: E402

REV = {}
for code, ch in D.CTC.items():
    REV.setdefault(ch, set()).add(code)

# b21 changes to his proposed reading, each a one-digit variant of the group (checked by one_digit):
OVERRIDE = {
    # N24 '〔滠〕日唐宅開會': 2530 -> 2520 灰 (tens 三 read for 二, the kanji numerals' look-alike; 灰 = day code of the
    # 10th, the day after the '佳日' (9th) of the same sentence). Adopted as a look-alike alternate; sense-checked only.
    ('N24', 22): ('alt', '灰', 'tens 3 -> 2, 灰日 = the 10th after 佳日 = the 9th; sense-only, for review'),
    # V4E '〔圉〕{已}入京': 8063 -> 8053 垣 (one digit, 六/五, not a look-alike pair): 曉垣 entered Beijing in V4D
    # ('汝驪已於昨夕偕張范王〔豆〕及曉垣〔岊〕入京'); kept as [?垣], partly carried.
    ('V4E', 23): ('part', '垣', 'tens 6 -> 5 gives 垣; V4D has 曉垣 going to Beijing; sense-only'),
}

UNIT = re.compile(r'\{([^}]*)\}|〔([^〕]*)〕|([㐀-鿿\U00020000-\U0002ffff□])|(.)', re.S)


def units(reading):
    out = []
    for m in UNIT.finditer(reading):
        if m.group(1) is not None:
            for ch in m.group(1) or '':
                out.append(('emend', ch))
        elif m.group(2) is not None:
            inner = m.group(2)
            if inner in ('…', '...', '□', ''):
                out.append(('open', '…'))
            else:
                for ch in inner:
                    out.append(('open', '…') if ch in '□…' else ('doubt', ch))
        elif m.group(3) is not None:
            out.append(('open', '…') if m.group(3) == '□' else ('plain', m.group(3)))
        else:
            out.append(('punct', m.group(4)))
    return out


def one_digit(fam, g, target):
    hits = []
    if not (g.isdigit() and len(g) == 4):
        cands = [g.replace('?', d, 1) for d in '0123456789'] if g.count('?') == 1 else []
        return [c for c in cands if D.glyph(D.decode(fam, c)) == target]
    for i in range(4):
        for d in '0123456789':
            if d == g[i]: continue
            v = g[:i] + d + g[i + 1:]
            if D.glyph(D.decode(fam, v)) == target: hits.append(v)
    return hits


def main(src, fam, out_dir):
    msgs = json.loads(Path(src).read_text(encoding='utf-8'))['messages']
    out_dir = Path(out_dir)
    body, rows = [], ['tel\tn\tcipher\tdecode\treading\tkind\tvariant']
    tot = dict(chars=0, plain=0, alt=0, ctx=0, doubt=0, open=0, mismatch=0)
    for mid, m in msgs.items():
        if m['family'] != fam: continue
        gs = [x['cipher'] for x in m['groups']]
        dec = [D.glyph(D.decode(fam, g)) for g in gs]
        us = units(m['reading_published'] or '')
        nonp = [u for u in us if u[0] != 'punct']
        # align reading units with decoded groups
        a = [u[1] if u[0] in ('plain', 'doubt') else '#' for u in nonp]
        sm = difflib.SequenceMatcher(None, dec, a, autojunk=False)
        pos = {}
        for tag, i1, i2, j1, j2 in sm.get_opcodes():
            if tag == 'equal' or (tag == 'replace' and i2 - i1 == j2 - j1):
                for k in range(j2 - j1): pos[j1 + k] = i1 + k
        t = dict(chars=0, plain=0, alt=0, ctx=0, doubt=0, open=0, mismatch=0)
        txt, j = [], 0
        for u in us:
            kind, ch = u
            if kind == 'punct':
                txt.append(ch); continue
            gi = pos.get(j); j += 1
            g = gs[gi] if gi is not None else ''
            d = dec[gi] if gi is not None else ''
            t['chars'] += 1
            ov = OVERRIDE.get((mid, None if gi is None else gi + 1))
            if ov and ov[0] == 'alt':
                assert one_digit(fam, g, ov[1]), (mid, gi, ov)
                t['alt'] += 1; txt.append(ov[1])
                rows.append(f'{mid}\t{gi + 1}\t{g}\t{d}\t{ov[1]}\tone-digit alternate (b21, {ov[2]})\t{",".join(one_digit(fam, g, ov[1]))}')
                continue
            if ov and ov[0] == 'part':
                t['doubt'] += 1; txt.append(f'[?{ov[1]}]')
                rows.append(f'{mid}\t{gi + 1}\t{g}\t{d}\t{ov[1]}\tpartly carried (b21, {ov[2]})\t{",".join(one_digit(fam, g, ov[1]))}')
                continue
            if kind == 'plain':
                if ch == d:
                    t['plain'] += 1; txt.append(ch); k = 'figure'; var = ''
                else:
                    t['mismatch'] += 1; txt.append(ch); k = 'MISMATCH'; var = ''
            elif kind == 'doubt':
                t['doubt'] += 1; txt.append(f'[?{ch}]'); k = 'doubtful (figure value, no sense)'; var = ''
            elif kind == 'open':
                t['open'] += 1; txt.append('[…]'); k = 'open'; var = ''
            else:
                hits = one_digit(fam, g, ch) if g else []
                if hits:
                    t['alt'] += 1; txt.append(ch); k = 'one-digit alternate'; var = ','.join(hits)
                else:
                    t['ctx'] += 1; txt.append(f'[{ch}]'); k = 'contextual (supplied)'; var = ''
            rows.append(f'{mid}\t{"" if gi is None else gi + 1}\t{g}\t{d}\t{ch}\t{k}\t{var}')
        for k in tot: tot[k] += t[k]
        body.append((mid, m, ''.join(txt), t, len(gs)))
        print(mid, len(gs), t)
    print('TOTAL', tot)
    with open(out_dir / f'{fam}_reading_body.txt', 'w', encoding='utf-8') as f:
        for mid, m, txt, t, n in body:
            f.write(f'### {mid}\t{m["dir"]}\t{m["date_note"] or m["date"]}\t{n} groups\t{json.dumps(t)}\n{txt}\n\n')
    (out_dir / f'{fam}_align.tsv').write_text('\n'.join(rows) + '\n', encoding='utf-8')


if __name__ == '__main__':
    main(*sys.argv[1:4])
