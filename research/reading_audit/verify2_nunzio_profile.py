"""Verification pass 2 (22 Oct 2026), nunzio1736: append the word-by-word result to each Spagna 423 document's
reading_review.note (or, for a document decoded, not read, which has no reading_review, to its note) in profile.json,
by a targeted text splice; the rest of the file is untouched. No state changes: every document read stays above 0.60
clean sentences on its reading body.

    python research/reading_audit/verify2_nunzio_profile.py
"""
import json
import pathlib

P = pathlib.Path(__file__).resolve().parents[2] / 'targets' / 'nunzio1736' / 'profile.json'
V = 'verified word by word 22 Oct 2026'
# doc: (supplied, partly, replaced, clean before, clean after)
R = {
    '423/1': (0, 2, 0, 0.447, 0.426), '423/2': (0, 0, 0, 0.824, 0.824), '423/4': (0, 0, 0, 0.8, 0.8),
    '423/5': (0, 0, 0, 0.0, 0.0), '423/6': (0, 0, 0, 0.727, 0.727), '423/7': (0, 0, 0, 0.682, 0.682),
    '423/8': (0, 0, 0, 0.625, 0.625), '423/9': (0, 0, 0, 0.727, 0.727), '423/10': (0, 1, 0, 0.667, 0.641),
    '423/11': (1, 0, 1, 0.639, 0.639),
}


def main():
    s = P.read_text(encoding='utf8')
    for doc, (sup, part, rep, b, a) in R.items():
        i = s.index(f'"doc": "{doc}"')
        nxt = s.find('"doc": "', i + 10)
        nxt = len(s) if nxt == -1 else nxt
        j = s.find('"reading_review"', i, nxt)
        k = s.index('"note": ', j if j != -1 else i)
        assert k < nxt, doc
        start = k + len('"note": ')
        val, end = json.decoder.scanstring(s, start + 1)
        if V in val:
            print('already', doc); continue
        sc = f'{b:.3f}' if a == b else f'{b:.3f} -> {a:.3f}'
        add = (f'{V[0].upper()}{V[1:]} (verify2_nunzio_align.py, reading aligned with texts/423-{doc[4:]}_decode_b04.txt):'
               f' {sup + part} words bracketed ({sup} supplied, {part} partly), {rep} replaced; clean sentences on the'
               f' reading body {sc}.')
        new = val.rstrip() + ('' if val.rstrip().endswith('.') else '.') + ' ' + add
        s = s[:start] + json.dumps(new, ensure_ascii=False) + s[end:]
        print(doc, 'ok')
    P.write_text(s, encoding='utf8', newline='')


if __name__ == '__main__':
    main()
