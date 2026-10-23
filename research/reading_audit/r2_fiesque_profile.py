"""r2_fiesque: round-2 reread of fiesque1567 (23 Oct 2026) written into profile.json by targeted edits (layout kept)."""
import sys, json, re, pathlib
sys.path.insert(0, str(pathlib.Path(__file__).resolve().parent))
from relabel_edit_r2 import Prof

D = '2026-10-23'
def rv(grade, note):
    return {'grade': grade, 'by': 'Claude Opus 5.5', 'date': D, 'note': note}

p = Prof('fiesque1567')
cur = json.loads(p.s)['outcome']['texts']

# 0: 11 Oct 1567, view 6 right now transcribed and read
p.entry(0,
        label='11 Oct 1567 (docket "11 octob. 1567"), to the Queen Mother (v006r, transcribed here 23 Oct 2026; v007l, v007r, v008l, v008r)',
        transcription=['read/r2/transcription_v006r.txt'] + cur[0]['transcription'],
        note=cur[0]['note'] + ' Round 2, 23 Oct 2026: view 6 right (the first cipher page, 23 lines, 816 signs) transcribed from the Gallica image and read (read/r2/transcription_v006r.txt, read/r2/v006r_reread_log.md); v007l c01 closed ("et aveugles a leur interest"). Body score 0.61 plain, 0.92 explicit holes only; look-alike alternates on view 6 right 3.3% (31/940 letters), at the limit, not confirmed by any other text.',
        reading_review=rv('B', 'built word by word from the key decode of the contributed transcription (views 7-8, image check of v007l c01) and from a single AI transcription of view 6 right made here on native-resolution crops (816 signs; Dz valued "con" from four words on the page). Look-alike alternates on view 6 right 3.3% of its letters; no contemporary decipherment. Holes: v006r c05-c06 (two words), v008l c19-c24 fragments, about ten [?] words.'))

# 1: 15 Nov 1567, view 23 left now transcribed
p.entry(1,
        transcription=cur[1]['transcription'] + ['read/r2/transcription_v023l.txt'],
        note=cur[1]['note'] + ' Round 2, 23 Oct 2026: view 23 left (13 lines, 446 signs) transcribed and decoded (read/r2/transcription_v023l.txt, read/r2/v023l_reread_log.md); with a re-reading of the decipherment it corrects three readings of 22 Oct ("il s\'en va a Prague", "ceste lettre", "je n\'ay eu responce de celles que vous ay envoyées par Suisse": no Chantonnay here). Body score 0.91 (0.88 before).',
        reading_review=rv('A', 'follows the contemporary decipherment on view 23 right (f. 19r) for view 22 right (83.8% letter agreement with the decode, calib.txt); view 23 left now rests on its own cipher, transcribed and decoded here (1.7% look-alike alternates), checked against the decipherment, which abridges it. Open: the bearer\'s name (9 signs) and about 17 signs before "court".'))

# 17: 10 Sep 1569 -> read
p.entry(17,
        state='read',
        note='Re-read 22 Oct 2026 (batch b02) and 23 Oct 2026 (round 2: image check of view 150 left c14-c23 on native crops, read/1569-09-10_reread_log.md): read/1569-09-10_reading.md, read/1569-09-10_en.md. Clean share (body only) 0.54 -> 0.61 plain, 0.94 explicit holes only, 0.71 with the target\'s own spellings; docs/_check_reading.py with the header 0.57. Look-alike upper bound 4.1% of letters, 3.0% without the y-shape s/p class (labelled by context in the contributed transcription).',
        reading_review=rv('B', 'built word by word from the key decode of the contributed transcription (Tomokiyo\'s key), reading through the known sign confusions; view 150 left c14-c23 checked on native-resolution crops: three label corrections (1 3y = code 18; "zo" = code 20; Dz = con, from view 6 right). Codes left open: [H#], [ffx-3y] (by sense the King of Spain). Holes: [?conclurre], [?cest], [?Gennes], [?saultier] and single words. Look-alike rate at the 3% limit (3.0% without the y-shape class); no contemporary decipherment; reader\'s judgement: the sentences hold.'))

# other letters touched in round 2: notes appended
for i, txt in ((3, 'Round 2, 23 Oct 2026: v038l c03-c04 and c17-c18 checked on native crops ("par quelque bon [?appoinctement]"; "que [?elles] ne pourront prandre bonne fin"); body score 0.80 -> 0.83.'),
               (4, 'Round 2, 23 Oct 2026: f. 39r c21-c29 checked on native crops ("[con]me il vous semble"; "que ces gens eussent vuydé le royaume, et vos forces françoises demeurassent entieres"; "Et mesmes [∞], qui me tint jeudy dernier [ung] long propos"); body score 0.72 kept.'),
               (8, 'Round 2, 23 Oct 2026: f. 79v and f. 80 checked on native crops (view 84): f. 79v c06-c08 read ("pour [con]soler et adoulcir ce peuple, qui est si malcontant"); f. 79v c01-c03 and f. 80 c01, c08 not settled; body score 0.71 kept.'),
               (11, 'Round 2, 23 Oct 2026: f. 100r c16-c27 checked on native crops (view 105 right): "mais que [pp] desiroict d\'estre mediateur", "en quoy il ne pouvoict nier de luy", "affin de ne luy [...] celle de vostre intention, [...] l\'alliance qu\'avez ensemble, tenant son filz", "Sur cela il me [?dict] que bien tost il envoyeroict en Espaigne"; body score 0.71 -> 0.75.')):
    p.entry(i, note=cur[i]['note'] + ' ' + txt)

p.outcome('gaps', [
    {'item': 'View 6 right (11 Oct 1567) c05-c06, two words ("que [...] bien qu\'il estoict necessaire"), and about ten [?] words on that page',
     'blocker': 'no-key-material',
     'detail': 'transcribed and checked sign by sign on native crops 23 Oct 2026; the sign groups give no word under the key\'s values and no contemporary decipherment or print of this letter exists'},
    {'item': 'View 23 left (15 Nov 1567): the bearer\'s name (9 signs) and about 17 signs between "Flandres" and "court"',
     'blocker': 'no-key-material',
     'detail': 'decoded 23 Oct 2026; a name not in the key, and the contemporary decipherment abridges and is cramped at that line'},
    {'item': 'Phrase holes left after round-2 image checks: f. 79v c01-c03 and f. 80 c01, c08 (17 Jul 1568); f. 100r c18 end, c24-c26 three words (4 Sep 1568); v038l c17 subject (15 Feb 1568); f. 39r c08, c22-c23 end, c29 verb (6 Mar 1568); v150l [?conclurre], [?cest] (10 Sep 1569)',
     'blocker': 'no-key-material',
     'detail': 'each checked on native-resolution crops 23 Oct 2026 (read/<doc>_reread_log.md, round 2); the groups fit no word under the key\'s values and no contemporary decipherment, clear copy or print exists for these letters'},
    {'item': 'Single-word holes in the letters not re-checked in round 2 (1568-01-21, 03-27, 06-04, 06-12, 08-14, 08-21, 09-04q, 11-06, 12-02; 1569-01-14, 03-02, 10-01, 10-15, 10-20, 10-29, 11-04; v007r-v008l of 11 Oct 1567)',
     'blocker': 'not-attempted',
     'detail': 'about 60 isolated [?] or [...] words across 17 letters, each needing its own crop; left for a later pass because every one of these letters already reads (0.58-1.0 clean share) and the round-2 time went to the untranscribed pages and the phrase holes'},
    {'item': 'Lone signs and groups standing as codes, values not settled: ϖ (l\'Empereur or le Roy), ∞ alone (le Roy / l\'Empereur), =ii, pp/ꝥ (the King of Spain by sense), H# alone, the group ffx-3y (10 Sep 1569), arrow, "lele"; 16 = ce or vostre (vostre in the letters to the King and in 4 Sep 1568)',
     'blocker': 'open-codes',
     'detail': 'not in Tomokiyo\'s table; read from context in read/*_reread_log.md; key.tsv unchanged. Dz = con is now settled from 11 words in five letters (read/r2/v006r_reread_log.md)'},
])

p.step('Round 2 (23 Oct 2026): view 6 right, the untranscribed first cipher page of the 11 Oct 1567 letter, transcribed from native-resolution IIIF crops (23 lines, 816 signs, read/r2/transcription_v006r.txt) and read: the Emperor complains of the disorders in Christendom and blames the disunion of the Christian princes. Single AI transcription, 3.3% look-alike alternates; letter body score 0.61 plain, 0.92 holes only.', result='worked', technique=('manual reconstruction', 'contextual inference'))
p.step('Round 2: the contributor\'s unvalued sign Dz (ꝺʒ) valued "con" (congé, conmandements, condition on view 6 right; conclusion, conditions, contanter, conservation in 1569; comme in 1568; consoler in Jul 1568): eleven words in five letters.', result='worked', technique=('key-structure hypothesis', 'contextual inference'))
p.step('Round 2: view 23 left (15 Nov 1567) transcribed (13 lines, 446 signs, read/r2/transcription_v023l.txt) and decoded; with a re-reading of the contemporary decipherment on view 23 right it corrects three readings of 22 Oct ("il s\'en va a Prague", "ceste lettre", "je n\'ay eu responce"). Bearer\'s name and about 17 signs left open.', result='partial', technique=('plaintext matching', 'manual reconstruction'))
p.step('Round 2: 10 Sep 1569 view 150 left c14-c23 checked on native crops; label corrections (1 3y = code 18, "zo" = code 20) and Dz = con close the c17-c23 passage ("lesquelz il tient pour faictz", "de la conclusion", "quelques conditions", "pour cest effect, jusques au retour duquel"). Body score 0.54 -> 0.61; look-alike 3.0% without the y-shape class (4.1% upper bound). State decoded, not read -> read (B).', result='worked', technique=('manual reconstruction', 'contextual inference'))
p.step('Round 2: phrase holes checked on native crops: 4 Sep 1568 f. 100r c16-c27 (mostly read; [pp] = King of Spain as mediator), 17 Jul 1568 f. 79v c06-c08 (read) and c01-c03, f. 80 c01/c08 (not settled), 15 Feb 1568 v038l c03-c04 (read) and c17-c18 (subject open), 6 Mar 1568 f. 39r c21-c29 (mostly read; ∞ code found).', result='partial', technique=('manual reconstruction', 'contextual inference'))

# fix step dates (Prof.step writes 2026-10-22)
n = 5
idx = p.s.index('"outcome"')   # steps sit in solution, before outcome
for _ in range(n):
    idx = p.s.rindex('"date": "2026-10-22"', 0, idx)
    p.s = p.s[:idx] + '"date": "2026-10-23"' + p.s[idx + len('"date": "2026-10-22"'):]

o = json.loads(p.s)['outcome']
p.outcome('notes', o['notes'] + ' 23 Oct 2026 (round 2): view 6 right and view 23 left transcribed and read, the 10 Sep 1569 letter now reads (all 23 letters read), Dz = con settled; class stays read in part: open codes and phrase holes remain inside the readings, and the transcription is AI-only with no human check.')
p.save()
print('saved')
