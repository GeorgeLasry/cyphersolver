"""b10 (rupert): targeted profile.json edits after the 22 Oct 2026 re-read (layout kept, file saved after each change).

    python research/reading_audit/reread_b10.py <step>

Steps: f104-entry, parts, gaps, outcome-text, steps, conditions, document. Each replaces one exact span and checks
that the file still parses.
"""
import json, pathlib, sys

P = pathlib.Path(__file__).resolve().parents[2] / 'targets' / 'rupert' / 'profile.json'


def splice(old, new):
    s = P.read_bytes().decode('utf-8')
    assert s.count(old) == 1, (s.count(old), old[:80])
    s = s.replace(old, new)
    json.loads(s)
    P.write_bytes(s.encode('utf-8'))
    print('ok', old[:60].replace('\n', ' '))


def j(x):
    return json.dumps(x, ensure_ascii=False)


STEPS = {}

STEPS['f104-entry'] = [(
    '''    "summary": "An all-numeric cipher sheet, marked 'Decrypted' on DECODE though no decipherment is on it; not deciphered.",''',
    '''    "decryption": "f104_reading.md",
    "translation": "f104_en.md",
    "summary": ''' + j("Charles I to the Prince of Wales (the endorsement '347 313 364' decodes as 'The King to the Prince of Wales'), a clerk's all-numeric fair copy, undated [1646?]: the King is content that the Prince has been referred to the Queen, and lays a command on him that no persuasion or threatening whatsoever make him [come into England?] before his father sends for him; a summons he has not really sent is to be judged by the Queen. Deciphered in part with George Lasry's key 'TNA SP106-8' (DECODE R924) and 35 values from R924's interlinear and this letter's contexts.") + ''','''
)]

STEPS['parts'] = [(
    '''   {
    "label": "Add MS 72438 f. 104 numeric letter and Add MS 18982 ff. 51-52 (Trevor to Rupert, [28] April 1645)",
    "method": "not solved",
    "extent": "none",
    "basis": "256 + 62 groups transcribed; no key fits; Trevor's 54 letter groups too few to rebuild",
    "records": "R8725, R8433"
   }''',
    '''   {
    "label": "Add MS 72438 f. 104, Charles I to the Prince of Wales [1646?]",
    "method": "read with known key",
    "extent": "partial",
    "basis": "matched 22 Oct 2026 to George Lasry's reconstructed key TNA SP106-8 (DECODE R924); 201 of 256 groups get a value from it unchanged; with 35 values added from R924's interlinear and the letter's contexts, 4 of 15 sentences hold (0.27); 21 nomenclator groups have no key material",
    "records": "R8725 (key: Lasry's SP106-8 on R924)"
   },
   {
    "label": "Add MS 18982 ff. 51-52 (Trevor to Rupert, [28] April 1645)",
    "method": "not solved",
    "extent": "none",
    "basis": "62 groups transcribed; no key fits (Lasry's five SP 106 keys added to the screen 22 Oct 2026); 54 letter groups too few to rebuild",
    "records": "R8433"
   }'''
)]

STEPS['gaps'] = [(
    '''   {
    "item": "Add MS 72438 f. 104 (R8725)",
    "blocker": "no-key-material",
    "detail": "no key tested fits; 256 groups"
   },''',
    '''   {
    "item": "Add MS 72438 f. 104 (R8725), 21 nomenclator groups and the opening line",
    "blocker": "no-key-material",
    "detail": "letter in Lasry's SP106-8 (R924); the groups 227, 312, 131, 124, 466, 543, 534, 668, 38, 330, 308, 307, 188, 643, 502, 161, 769, 96, 132, 56 and the first 192 are absent from R924 or unidentified there, and no other SP106-8 letter is known; 4 of 15 sentences hold"
   },'''
), (
    '''    "detail": "none of the 73 keys in the volume fits; 108 letter groups too few to rebuild"''',
    '''    "detail": "none of the 73 keys in the volume nor Lasry's five SP 106 keys (SP 106, -2, -3, -5, -8; 22 Oct 2026) fits; 108 letter groups too few to rebuild"'''
), (
    '''    "detail": "no key in the volume fits; 300 letter groups over ~99 homophones"''',
    '''    "detail": "no key in the volume nor Lasry's five SP 106 keys fits (22 Oct 2026); 300 letter groups over ~99 homophones"'''
), (
    '''    "detail": "key not in Add MS 72438 or on DECODE; 93 groups"''',
    '''    "detail": "key not in Add MS 72438 or on DECODE (Lasry's five SP 106 keys tried 22 Oct 2026); 93 groups"'''
)]

STEPS['outcome-text'] = [(
    '''the cryptiana items themselves (Maurice 1645, f. 9, f. 10) and f. 104 and R8433 are not solved, so the primary method describes a by-product of the search, not the targets as posed.''',
    '''the cryptiana items themselves (Maurice 1645, f. 9, f. 10) and R8433 are not solved, so the primary method describes a by-product of the search, not the targets as posed. f. 104 (R8725), Charles I to the Prince of Wales, was matched on 22 Oct 2026 to George Lasry's key TNA SP106-8 and deciphered in part (decoded, not read: 4 of 15 sentences hold).'''
), (
    '''    {"who": "contemporary", "role": "key or decipherment used", "note": "lower alphabet of the royalist key sheet f. 106 (DECODE R8727), and the partial interlinear gloss on f. 107 used as crib"}''',
    '''    {"who": "contemporary", "role": "key or decipherment used", "note": "lower alphabet of the royalist key sheet f. 106 (DECODE R8727), and the partial interlinear gloss on f. 107 used as crib"},
    {"who": "lasry", "role": "key or decipherment used", "note": "reconstructed key TNA SP106-8 and his interlinear decipherment of R924 (DECODE, 2020), which decipher f. 104 in part"}'''
)]

NEW_STEPS = [
    {"date": "2026-10-22", "kind": "sibling key", "what": "Reading audit b10: George Lasry's reconstructed keys of the sibling King/Queen 1645-46 targets (TNA SP 106, SP106-2, SP106-3, SP106-5 that read rupert1645, SP106-8), fetched from DECODE R785, R787, R929, R924 and goring1645, applied to all five numeric documents. f. 104 reads as English with SP106-8 (201 of 256 groups get a value; endorsement 347 313 364 = The King to the Prince of Wales); Maurice 1645, f. 9, f. 10 and Trevor 1645 give gibberish under all five.", "result": "partial", "technique": ["key matching"]},
    {"date": "2026-10-22", "kind": "literature search", "what": "Printed text of the f. 104 letter looked for: Clarendon State Papers ii (1773) and Bruce, Charles I in 1646 (1856) grepped on archive.org, two web searches; Petrie 1935 lending-only. Nothing found.", "result": "failed"},
    {"date": "2026-10-22", "kind": "reading", "what": "f. 104 transcription checked on the full-resolution image (no label changed); key gaps filled from Lasry's own interlinear of R924 (3, 7, 12, 30, 50 word spaces; 116 = can, not BROUGHT; 127 do, 207 may, 208 made, 320 upon, 334 what, 450 command, 513 express) and from the letter's contexts (f104_key_additions.tsv, f104_decode.py); reading built and aligned word by word (f104_reading.md, f104_en.md, f104_reread_log.md). Body scores 0.267 (4/15 sentences); 21 nomenclator groups have no key material, so it stays decoded, not read.", "result": "partial", "technique": ["contextual inference", "key-structure hypothesis", "language-model scoring"]},
]
STEPS['steps'] = None

STEPS['conditions'] = [(
    '''"last_date": "2026-10-09"''', '''"last_date": "2026-10-22"'''
), (
    '''"trevor_anneal.py (homophonic annealing with cribs, lang en-1640s)"''',
    '''"trevor_anneal.py (homophonic annealing with cribs, lang en-1640s)", "f104_decode.py (Lasry's SP106-8 key + f104_key_additions.tsv)"'''
)]

STEPS['document'] = [(
    '''   "source": "No decipherment on the sheet."''',
    '''   "source": "No decipherment on the sheet. Deciphered in part (22 Oct 2026) with George Lasry's key TNA SP106-8 (DECODE R924, 2020); no reading of this letter found on DECODE or in print."'''
)]


def add_steps():
    s = P.read_bytes().decode('utf-8')
    d = json.loads(s)
    i = s.index('"solution":')
    k = s.index('\n ]', i)  # end of the solution array (top-level indent 1)
    last = s.rfind('}', i, k)
    block = ''.join(',\n' + '\n'.join('  ' + l for l in json.dumps(st, indent=1, ensure_ascii=False).split('\n')) for st in NEW_STEPS)
    s2 = s[:last + 1] + block + s[last + 1:]
    d2 = json.loads(s2)
    assert d2['solution'][-len(NEW_STEPS):] == NEW_STEPS and len(d2['solution']) == len(d['solution']) + len(NEW_STEPS)
    P.write_bytes(s2.encode('utf-8'))
    print('ok steps', len(d2['solution']))


if __name__ == '__main__':
    step = sys.argv[1]
    if step == 'steps':
        add_steps()
    else:
        for old, new in STEPS[step]:
            splice(old, new)
