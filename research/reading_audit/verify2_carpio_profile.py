"""verify2 (carpio1677): append the margin transcription and the re-check against it to each document's
reading_review.note in profile.json (targeted text edit, the rest of the file untouched). No state changes.

    python research/reading_audit/verify2_carpio_profile.py
"""
import json
import pathlib

P = pathlib.Path(__file__).resolve().parents[2] / 'targets' / 'carpio1677' / 'profile.json'
TAG = 'margin transcribed from the images to read/'
ADD = {
    'R1002': 'Margin transcribed from the images to read/R1002_margin.txt 22 Oct 2026; re-checked against it: 0 bracketed, 1 replaced ([?hable] -> [?hablase], margin "habla-/se", key "ha go la se"); 0.90 clean on the body (unchanged).',
    'R1003': 'Margin transcribed from the images to read/R1003_margin.txt 22 Oct 2026; re-checked against it: 0 bracketed, 1 replaced ("del parecer" -> "de parecer", margin and key); 0.923 clean (unchanged).',
    'R1006': 'Margin transcribed from the images to read/R1006_margin.txt 22 Oct 2026 (DECODE has none); re-verified against it: 0 bracketed, 0 replaced; the two place names stay illegible in the margin; 0.778 clean (unchanged).',
    'R1007': 'Margin transcribed from the images to read/R1007_margin.txt 22 Oct 2026 (DECODE has none); re-verified against it: 0 bracketed, 1 replaced ("quedo esperando" -> "por quedar esperando", margin, key "que da r"); the margin carries the earlier-bracketed en, corte, por, pide (brackets kept); 0.857 clean (unchanged).',
    'R1008': 'Margin transcribed from the images to read/R1008_margin.txt 22 Oct 2026; re-checked against it: 0 bracketed, 0 replaced (the margin carries the earlier-bracketed lleguen; bracket kept).',
    'R1009': 'Margin transcribed from the images to read/R1009_margin.txt 22 Oct 2026; re-checked against it: 0 bracketed, 0 replaced.',
    'R1010': 'Margin transcribed from the images to read/R1010_margin.txt 22 Oct 2026; re-checked against it: 0 bracketed, 0 replaced.',
    'R1011': 'Margin transcribed from the images to read/R1011_margin.txt 22 Oct 2026; re-checked against it: 0 bracketed, 0 replaced (the margin carries the earlier-bracketed trata/de and Civitavecchia; brackets kept; "pasando" and "sin reservar" kept with the key where the faint margin may read "pensando", "con reservar").',
}
s = P.read_text(encoding='utf8')
for doc, add in ADD.items():
    i = s.index(f'"doc": "{doc}"')
    j = s.index('"reading_review"', i)
    nxt = s.find('"doc": "', i + 10)
    assert nxt == -1 or j < nxt, doc
    k = s.index('"note": ', j) + len('"note": ')
    val, end = json.decoder.scanstring(s, k + 1)
    if TAG in val:
        print('already', doc); continue
    s = s[:k] + json.dumps(val.rstrip() + ' ' + add, ensure_ascii=False) + s[end:]
    print(doc, 'ok')
P.write_text(s, encoding='utf8', newline='')
