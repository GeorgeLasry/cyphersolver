"""verify2 (ronquillo1676): append the word-by-word verification result to reading_review.note of each letter in
profile.json outcome.texts (entries found by their "reading" path; targeted text splice, the rest of the file as it
is). No state changes: every letter stays above 0.60 clean sentences on its reading body.

    python research/reading_audit/verify2_ronquillo_profile.py
"""
import json
import pathlib

P = pathlib.Path(__file__).resolve().parents[2] / 'targets' / 'ronquillo1676' / 'profile.json'
V = 'verified word by word 22 Oct 2026'
# doc: (supplied, partly, replaced, clean before, clean after)
RES = {
    'R966': (0, 0, 0, 0.885, 0.885), 'R967': (0, 0, 0, 0.844, 0.844), 'R968': (0, 0, 0, 0.913, 0.913),
    'R969': (0, 0, 0, 0.88, 0.88), 'R970': (0, 0, 0, 0.935, 0.935), 'R971': (2, 0, 0, 0.892, 0.89),
    'R972': (2, 0, 0, 0.892, 0.89), 'R973': (0, 0, 0, 1.0, 1.0), 'R974': (0, 0, 0, 0.718, 0.718),
    'R975': (0, 0, 0, 0.746, 0.746), 'R976': (0, 0, 0, 0.708, 0.708), 'R977': (0, 0, 0, 0.76, 0.76),
    'R978': (0, 0, 0, 0.746, 0.746), 'R979': (0, 2, 0, 0.762, 0.762), 'R980': (0, 0, 0, 0.786, 0.786),
    'R981': (0, 0, 0, 0.713, 0.713), 'R982': (0, 1, 0, 0.621, 0.621), 'R983': (0, 0, 0, 0.694, 0.694),
    'R984': (0, 1, 0, 0.708, 0.708), 'R1001': (0, 0, 0, 0.814, 0.814),
}
DETAIL = {
    'R971': ' ([de] [V.S.] in "solicitando siempre [de] [V.S.] las órdenes": neither the margin nor the figures have them)',
    'R972': ' ([de] [V.S.] in "solicitando siempre [de] [V.S.] las órdenes": neither the margin nor the figures have them)',
    'R979': ' ([?que] in "animosidades [?que] della", figures de; [?a] in "comunicaron [?a] daneses", figure 20=n)',
    'R982': ' ([?de] in "después [?de] la pérdida", figure 4=t)',
    'R984': ' ([?aquí] in "se halla [?aquí], que": the figures give ha-ll-a-que)',
}


def main():
    s = P.read_text(encoding='utf8')
    for doc, (sup, part, rep, b, a) in RES.items():
        r = s.index(f'"reading": "read/{doc}_reading.md"')
        start = s.rfind('"doc": "', 0, r)
        j = s.index('"reading_review"', start)
        assert j < r, doc
        k = s.index('"note": ', j)
        assert k < r, doc
        vs = k + len('"note": ')
        val, end = json.decoder.scanstring(s, vs + 1)
        if V in val:
            print('already', doc); continue
        add = (f'{V[0].upper() + V[1:]} (verify2_ronquillo_align.py: reading aligned with the margin decipherment and the '
               f'key decode of the corrected transcription): {sup + part} words bracketed ({sup} supplied, {part} partly)'
               f'{DETAIL.get(doc, "")}, {rep} replaced; clean sentences on the reading body {b} -> {a}.')
        new = val.rstrip() + ('' if val.rstrip().endswith('.') else '.') + ' ' + add
        s = s[:vs] + json.dumps(new, ensure_ascii=False) + s[end:]
        print(doc, 'ok')
    P.write_text(s, encoding='utf8', newline='')


if __name__ == '__main__':
    main()
