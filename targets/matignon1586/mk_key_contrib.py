"""Build key_contrib.json: key.json plus the values Michael Brackx proposed in issues #64, #68, #69, #70, #71
(Oct 2026), so measure.py can be run with them (python measure.py --key key_contrib.json --control).

Letter values marked as sets are his: the transcription merges figures there, so a token stands for a small set of
letters and the decoder chooses. Codes 33-hash are fixed by the contemporary clear copies ff. 155-157 (#70, checked
here on canvases 162-164 on 21 Oct 2026); 68 rests on context only and is tentative. Not adopted: BOX = u (in this
transcription BOX also marks illegible figures), 44 = Sire (withdrawn by him), 79 = pour (one weak context).
"""
import json, os

HERE = os.path.dirname(os.path.abspath(__file__))
k = json.load(open(os.path.join(HERE, 'key.json'), encoding='utf-8'))
CHANGES = {
    # letters (#64, #68, #69, #71); q = s is also implied by this folder's own f. 196 head crib
    'q': ['s', 'o', 'a'], 'f': ['c', 'u', 'h'], 'T=': ['m', 'mm', 'r'], 'U': ['u', 'e', 'a'], 'd': ['s', 'c'],
    '4+': ['m', 'n'], '8': ['g', 'e'], 'a': ['a', 'm'], 'c': ['p', 'l'], 'b': ['e', 'i'], 'T': ['r'], '4': ['m'],
    # codes fixed by the clear copies ff. 155-157 (#70)
    '33': ['vostre'], '36': ['toutesfois'], '40': ['bien'], '49': ['comme'], '53': ['affin'], '54': ['aussi'],
    '62': ['peut'], '88': ['monsieurdumayne'], '104': ['mil'], 'hash': ['coustume'],
    # code from context only (#64), tentative
    '68': ['vostremajeste'],
}
k.update(CHANGES)
json.dump(k, open(os.path.join(HERE, 'key_contrib.json'), 'w', encoding='utf-8'), ensure_ascii=False, indent=0)
print(len(CHANGES), 'values changed or added;', len(k), 'entries')
