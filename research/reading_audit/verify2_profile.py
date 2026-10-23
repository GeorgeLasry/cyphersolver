"""verify2: append the word-by-word result to reading_review.note of checked documents and, where a document falls
below the clean-sentence rule, set its state to "decoded, not read" with a note. Targeted text splices; the entry is
found by "doc" plus a label substring (selve1535 has three R3697 entries, which set_state.py cannot tell apart).

    python research/reading_audit/verify2_profile.py
"""
import json
import pathlib

ROOT = pathlib.Path(__file__).resolve().parents[2] / 'targets'
V = 'Verified word by word 22 Oct 2026'
# (folder, doc, label substring or None, note to append, new state note or None)
EDITS = [
    ('alessandrino1568', 'R94', None, f'{V} (verify2_aless_align.py, reading aligned with the figures; disagreements looked up in the f. 45r decipherment): 0 words bracketed, 0 replaced; 1.0 clean sentences on the reading body.', None),
    ('alessandrino1568', 'R95', None, f'{V} (figures and the f. 58r decipherment): 0 words bracketed, 0 replaced; 0.944 clean on the body.', None),
    ('alessandrino1568', 'R100', None, f'{V} (figures and the decipherment on f. 280r): 0 words bracketed, 0 replaced; 1.0 clean on the body.', None),
    ('alessandrino1568', 'R101', None, f'{V} (figures of 291r and 291v aligned as one run; no decipherment exists): 0 words bracketed, 0 replaced; "patienza et" is 6 6 0^. 4 | 0^. 0 (z, a, then the dotted et), not a gap; 0.842 clean on the body.', None),
    ('nevers1574', 'f15', None, f'{V} (verify2_nevers_align.py: signs decoded with f15_key.md, gloss words aligned): 0 words bracketed beyond those already marked, 3 replaced (f. 15v l. 16 "desquoy elle m\'a dict [...] tesmoigner" -> "desquoy mesme [?pouvoit] tesmoigner": signs +F9+F (9886..74, gloss "mesme ... [?pouvoit]"); 0.807 clean on the body (unchanged).', None),
    ('selve1535', 'R3697', 'glossed by the King', f'{V}: every word of the four runs is carried by the glosses (A, B, C1) or the margin decipherment and the signs (T2); 0 words bracketed, 0 replaced. Scored on the reading body (the four runs): 0.25 clean sentences, below the 0.60 rule.',
     'Verified word by word 22 Oct 2026: the four glossed runs are clause fragments set in clear text (A two words, B and T2 without their clause, C1 with a hole after "amys"); 0.25 clean sentences on the reading body, below the 0.60 rule, so decoded, not read; READING_R3697_struck.md is kept as a partial reading. Blocker: the rest of each clause is under the decipherer\'s strike (C1 after "amys", the tail of B, the head of T1) and illegible on the film scan.'),
]


def find_entry(s, doc, label):
    i = 0
    while True:
        i = s.index(f'"doc": "{doc}"', i)
        nxt = s.find('"doc": "', i + 10)
        end = nxt if nxt != -1 else len(s)
        if label is None or label in s[i:end]:
            return i, end
        i = end


def main():
    for folder, doc, label, add, state_note in EDITS:
        p = ROOT / folder / 'profile.json'
        s = p.read_text(encoding='utf8')
        i, end = find_entry(s, doc, label)
        j = s.index('"reading_review"', i)
        assert j < end, (folder, doc)
        k = s.index('"note": ', j)
        start = k + len('"note": ')
        val, e = json.decoder.scanstring(s, start + 1)
        if V in val:
            print('already', folder, doc); continue
        new = val.rstrip() + ('' if val.rstrip().endswith('.') else '.') + ' ' + add
        s = s[:start] + json.dumps(new, ensure_ascii=False) + s[e:]
        if state_note:
            i, end = find_entry(s, doc, label)
            seg = s[i:end]
            assert seg.count('"state": "read"') == 1, (folder, doc)
            seg = seg.replace('"state": "read"', '"state": "decoded, not read",\n    "note": ' + json.dumps(state_note, ensure_ascii=False))
            s = s[:i] + seg + s[end:]
        json.loads(s)
        p.write_text(s, encoding='utf8', newline='')
        print(folder, doc, 'ok')


if __name__ == '__main__':
    main()
