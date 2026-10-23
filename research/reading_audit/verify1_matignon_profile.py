"""Verification pass (22 Oct 2026), matignon1586: append the word-by-word result to reading_review.note of each
checked document in profile.json (targeted text splice; the rest of the file is left as it is). No state changes:
every document stays above 0.60 clean sentences on its reading body.

    python research/reading_audit/verify1_matignon_profile.py
"""
import json
import pathlib

P = pathlib.Path(__file__).resolve().parents[2] / 'targets' / 'matignon1586' / 'profile.json'
V = 'verified word by word 22 Oct 2026'
ADD = {
    'f173': f'{V} (verify1_matignon_align.py: reading aligned with the corrected figures and leaf key): 0 words bracketed, 0 replaced; 0.724 clean sentences on the reading body.',
    'f196': f'{V} against both encipherments (ff. 196 and 201): 0 words bracketed, 0 replaced; 0.794 clean on the body.',
    'f201': f'{V} against both encipherments (ff. 196 and 201): 0 words bracketed, 0 replaced; 0.794 clean on the body.',
    'f196v': f'{V}: 0 words bracketed, 0 replaced (code 63 = apres carried by f. 201\'s clear text); 0.697 clean on the body.',
    'fr15571-f177': f'{V}: 0 words bracketed, 0 replaced; 0.759 clean on the body.',
    'f110': f'{V}: 1 word bracketed (partly: [?effects] l. 17, the ff not carried), 1 replaced (l. 25 recongnoistre -> congnoistre, the figures have no re-); 0.72 clean on the body (unchanged).',
    'f123v': f'{V} (f. 123v section): 0 words bracketed, 0 replaced; 0.656 clean on the section.',
    'f124v': f'{V} (f. 124v section): 4 words bracketed (1 supplied: gens [de] guerre l. 27; 3 partly: [?qu\'il] l. 9, [?je] l. 19, [?d\'aller] l. 20), 0 replaced; clean 0.688 -> 0.656, stays read.',
    'f143v': f'{V} (reading_f143v_tail.md, ll. 26-35): 0 words bracketed, 0 replaced; 1.0 clean on the tail.',
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
        P.write_text(s, encoding='utf8', newline='')
        print(doc, 'ok')


if __name__ == '__main__':
    main()
