"""verify1 (sauli1579): append the word-by-word verification to each text's reading_review.note in profile.json
(string splice, the rest of the file untouched).    python research/reading_audit/verify1_sauli_profile.py"""
import json, pathlib
P = pathlib.Path(__file__).resolve().parents[2] / 'targets' / 'sauli1579' / 'profile.json'
ADD = {  # note prefix -> appended sentence
    'Clear text transcribed from the DECODE images (Midas 2017': ' Verified word by word 22 Oct 2026: 0 words bracketed, 0 replaced.',
    'Clear text transcribed from the images, cipher passages from the interlinear decipherments, checked with the key; the unglossed': ' Verified word by word 22 Oct 2026: 0 words bracketed, 0 replaced.',
    'Clear text transcribed from the images, every cipher passage from its interlinear decipherment': ' Verified word by word 22 Oct 2026: 2 words bracketed (partly carried: "guerra", struck in the gloss over group 40; "per" before "porti", no 84 in the figures), 1 replaced ("tale" -> "tali", gloss and figures).',
    'Clear text transcribed from the images, cipher passages from the interlinear decipherments, checked with the key; f. 238r': ' Verified word by word 22 Oct 2026: 0 words bracketed, 0 replaced.',
    'Clear text transcribed from the images, cipher passages from the interlinear decipherments, checked with the key; one hole': ' Verified word by word 22 Oct 2026: 0 words bracketed, 1 replaced ("della" -> "la" before "religione cattolica", gloss and figures).',
}
s = P.read_text(encoding='utf8')
for pre, add in ADD.items():
    i = s.index('"note": "' + pre)
    j = i + len('"note": "')
    # end of the JSON string
    k = j
    while True:
        k = s.index('"', k)
        if s[k - 1] != chr(92): break
        k += 1
    assert s.count('"note": "' + pre) == 1, pre
    s = s[:k] + add.replace('"', '\\"') + s[k:]
    P.write_text(s, encoding='utf8', newline='')
json.loads(s)
print('ok')
