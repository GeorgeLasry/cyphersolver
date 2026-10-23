"""verify2 (smith1562): append the word-by-word verification result to reading_review.note of each checked document in
profile.json (targeted text splice; the rest of the file untouched). No state changes: every document checked stays
at or above 0.60 clean sentences on its reading body except no. 15, which was already decoded, not read.

    python research/reading_audit/verify2_smith_profile.py
"""
import json
import pathlib

P = pathlib.Path(__file__).resolve().parents[2] / 'targets' / 'smith1562' / 'profile.json'
V = 'verified word by word 22 Oct 2026'
A = f'{V} (verify2_smith_align.py: reading aligned with Forbes\'s print, the source; OCR garbles checked on a second OCR)'
B = f'{V} (verify2_smith_mark.py: passages checked against the glyph strings and, where unsettled, the DECODE image and key sheet)'
ADD = {  # doc: note
    '01': f'{A}: 0 words bracketed, 0 replaced; 0.968 clean on the body (unchanged).',
    '03': f'{A}: 0 words bracketed (the existing [?musters] kept), 0 replaced; 1.0 clean (unchanged).',
    '04': f'{A}: 0 words bracketed, 0 replaced; 0.984 clean (unchanged).',
    '05': f'{A}: 0 words bracketed, 0 replaced; 0.895 clean (unchanged).',
    '19': f'{A}: 0 words bracketed, 0 replaced; 0.833 clean (unchanged).',
    '20': f'{A}: 0 words bracketed, 0 replaced; 1.0 clean (unchanged).',
    '06': f'{B}: 0 words bracketed, 0 replaced; 1.0 clean (unchanged).',
    '08': f'{B}: 4 words bracketed (1 supplied: [The] Lord of Murray, passage 7 has no article; 3 partly: [?The Earl of] Huntly, passage 14, the first sign is not on the key sheet), 1 replaced (passage 10 "that way" -> "that wise", .T ξπ9:L); clean 0.913 -> 0.870, stays read.',
    '09': f'{B}: 0 words bracketed, 0 replaced (two names; no sentence to score).',
    '11': f'{B}: 0 words bracketed, 1 replaced (passage 4 "Into" -> "In", the sign is ! = in); 0.889 clean (unchanged).',
    '13': f'{B}: 0 words bracketed, 0 replaced; 1.0 clean (unchanged).',
    '15': f'{B}: 0 words bracketed, 1 replaced (passage 6 "All the" -> "All that", A: ·T); 0.50 clean (unchanged), stays decoded, not read.',
    '16': f'{B}: 1 word bracketed (supplied: [the] French, passage 7 is :F alone), 0 replaced; 0.80 clean (unchanged).',
    '17': f'{B}: 0 words bracketed, 0 replaced ("be in that" is the second line of passage 5, ! ·T); 0.941 clean (unchanged).',
    '18': f'{B}: 0 words bracketed, 0 replaced; 0.667 clean (unchanged).',
    '22': f'{B}: 0 words bracketed, 1 replaced (l. 4 "of that same matter" -> "of the same matter", T. = the); 0.714 clean (unchanged).',
}


def main():
    s = P.read_text(encoding='utf8')
    for doc, add in ADD.items():
        i = s.index(f'"doc": "{doc}"')
        j = s.index('"reading_review"', i)
        nxt = s.find('"doc": "', i + 10)
        assert nxt == -1 or j < nxt, doc
        k = s.index('"note": ', j)
        start = k + len('"note": ')
        val, end = json.decoder.scanstring(s, start + 1)
        if V in val:
            print('already', doc); continue
        new = val.rstrip() + ('' if val.rstrip().endswith('.') else '.') + ' ' + add[0].upper() + add[1:]
        s = s[:start] + json.dumps(new, ensure_ascii=False) + s[end:]
        print(doc, 'ok')
    P.write_text(s, encoding='utf8', newline='')


if __name__ == '__main__':
    main()
