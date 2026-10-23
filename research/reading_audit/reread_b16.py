"""Re-read brief (REREAD_BRIEF.md), batch b16: vich1511 (N.45, N.57, N.60). wotton1585 was done by b16_wotton_profile.py.

Targeted profile edits with the splice saver of relabel_r0.py; one save per change.

    python research/reading_audit/reread_b16.py <step>      steps: texts, docs, outcome, steps
Helpers: b16_vich_dec.py (compact decode), b16_vich_kwic.py (group in context over the corpus), b16_vich_fix.py
(corrections tsv -> transcription), b16_vich_align.py (build vs decode, word by word), b16_vich_make.py (build ->
reading: render + b16_vich_modern.py), b16_holes.py / b16_sents.py (what _check_reading counts as holes).
"""
import sys
import pathlib

sys.path.insert(0, str(pathlib.Path(__file__).parent))
from relabel_r0 import load, save  # noqa: E402

T = 'vich1511'
REV = dict(by='Claude Opus 5.5', date='2026-10-23')


def entry(p, doc):
    e = [x for x in p['outcome']['texts'] if x.get('doc') == doc]
    assert len(e) == 1, doc
    return e[0]


def texts():
    p = load(T)
    e = entry(p, 'N.45')
    e.pop('note', None)
    e.update(transcription=['n45_pp03-09_v3.txt', 'n45_pp10-15_v3.txt'],
             decryption=['n45_pp03-09_v3_decoded.txt', 'n45_pp10-15_v3_decoded.txt', 'n45_build.txt'],
             state='read', language='es', reading='n45_reading.md', translation='n45_en.md')
    e['reading_review'] = dict(grade='B', **REV, note=(
        "No decipherment, copy or edition found (PARES record and all 16 images opened; Terrateig 1963 unseen). Read "
        "line by line on the figures with the 1511-12 key extended in b16 (key.md 'b16 additions': goe, gix, goi, sid, hoe, "
        "fet, Vs, gid, sas, ree, sue, men; gid carried by 8714 N.39's decipherment, the rest by sense at every occurrence), "
        "33 labels corrected on the images (fid/fud merged 17x, plix = plirt 7x; n45a/n45b_corrections.tsv); built in "
        "n45_build.txt in the figures' spelling, the reading modernised in orthography only. Aligned word by word "
        "(n45_align.tsv): 3,984 unbracketed words, 3,968 carried, 16 checked by eye. _check_reading on the body 0.601 "
        "(224/373; raw decode 0.213). Holes: ~424 [..], densest on pp. 3, 4 and 7 (unkeyed groups hno, hug, mun, myn, "
        "moy, cx, pie, pog, hng, sab, reg ...; number signs); the fac dichas/dar split flagged."))
    save(T, p); print('N.45 read')

    p = load(T)
    e = entry(p, 'N.57')
    e.pop('note', None)
    e.update(transcription='n57_transcription_v3.txt',
             decryption=['n57_transcription_v3_decoded.txt', 'n57_build.txt'],
             state='read', language='es', reading='n57_reading.md', translation='n57_en.md')
    e['reading_review'] = dict(grade='B', **REV, note=(
        "No decipherment found (PARES record and all 4 images opened). Read line by line on the figures with the 1511-12 "
        "key extended in b16 (here aca, governar, son, fue), 11 labels corrected on the half-line strips "
        "(n57_corrections.tsv: oto in 'segun quan', plort/plart, and the tilde-d = a six times, flagged for review); "
        "built in n57_build.txt, modernised in orthography only. Aligned word by word (n57_align.tsv): 433 unbracketed "
        "words, 431 carried, 2 two-letter words checked by eye. _check_reading on the body 0.600 (21/35; raw decode 0.30-"
        "0.32). Holes: 24 [..] (hno, rih, poh, fap, rar, mon, mug, sig x2, dup, pih, phi x2, sab, feg, for, pub, gud and "
        "three stray letter runs) and 8 [?words]."))
    save(T, p); print('N.57 read')

    p = load(T)
    e = entry(p, 'N.60')
    e.update(transcription='n60_transcription_v4.txt',
             decryption=['n60_transcription_v4_decoded.txt', 'n60_build.txt'],
             reading='n60_reading.md', translation='n60_en.md')
    e['note'] = ("Decoded, not read: re-read 22-23 Oct 2026 (b16; n60_reading.md kept as a partial reading, n60_en.md, "
                 "n60_reread_log.md). Built line by line on the figures (n60_build.txt) with the b16 key values and 5 labels "
                 "corrected on the images (n60_corrections.tsv); 5,074 unbracketed words, 5,026 carried. The body reaches "
                 "0.504 clean sentences (raw decode 0.197): about 600 unread groups (phi 34x, reg 18x, pub, for, pog, pir, "
                 "gox, geb ...) occur in no deciphered sibling and take no single value at all their occurrences "
                 "(no-key-material); fug/entre, fer dio/Fe- and b = a/i look-alikes need sharper images than PARES serves; "
                 "L1525-L1527 illegible (holes in the paper); a sign-by-sign proofread of pp. 4-14 not attempted.")
    save(T, p); print('N.60 note')


def docs():
    p = load(T)
    for d in p['documents']:
        if d['id'] == 'N.45':
            d['length']['file'] = 'n45_pp03-09_v3.txt'
            d['transcription']['notes'] = ("Sum of the two files measured with --drop-first (5,633 + 4,326). Pages 3-15. b16 (23 Oct "
                                           "2026): 33 labels corrected on the images, n45_pp03-09_v3.txt / n45_pp10-15_v3.txt.")
        if d['id'] == 'N.57':
            d['length'].update(tokens=986, distinct=142, file='n57_transcription_v3.txt')
            d['transcription']['notes'] = ("Measured with --drop-first. b16 (23 Oct 2026): 11 labels corrected on the half-line "
                                           "strips (n57_corrections.tsv), two tokens merged or dropped: 988 -> 986.")
        if d['id'] == 'N.60':
            d['length'].update(file='n60_transcription_v4.txt')
            d['transcription']['notes'] = d['transcription']['notes'] + " b16 (23 Oct 2026): 5 labels corrected, n60_transcription_v4.txt."
    save(T, p); print('documents')


def outcome():
    p = load(T)
    o = p['outcome']
    o['method'] = 'key recovered based on adjacent plaintext'
    o['method_basis'] = (
        "The nomenclator was rebuilt by aligning N.46 and N.52BIS, sibling letters in the same Vich file (AHN Estado 8715) "
        "that carry the clerk's decipherment on the following leaves, with their cipher, and extended from N.41, 8714 N.39 "
        "and N.12 (also deciphered at the time). Re-read 22-23 Oct 2026 (b16): N.45 and N.57 built into sentences on that "
        "key with twelve more group values recovered from their occurrences across the letters (one, gid amor, carried by "
        "N.39's decipherment); N.60 stays decoded, not read.")
    o['class'] = 'read in part'
    o['gaps'] = [
        dict(item='N.60 decoded, not read (0.504 clean sentences)', blocker='no-key-material',
             detail=("about 600 unread groups (phi, reg, pub, for, pog, pir, gox, geb ...) absent from the deciphered siblings "
                     "and without one value at all their occurrences; Terrateig 1963 (unseen, not online) may print the decipherment")),
        dict(item='N.60 sign-by-sign proofread of pp. 4-14', blocker='not-attempted',
             detail='b16 checked the lines where the decode broke sense and L1522-L1530 only'),
        dict(item='8 no-bar q tokens in N.45, 2 q1 missing from the transcription', blocker='illegible',
             detail='qwork/q_decisions.tsv'),
        dict(item='look-alike signs: tilde-d a / b, fug senor / entre, fer dio / Fe-, fac dichas / dar, b a / i (N.60)',
             blocker='illegible', detail='same shape at the PARES zoom-10 resolution; flagged for review in key.md'),
        dict(item='N.45 and N.57 holes (~424 and 24 [..])', blocker='no-key-material',
             detail='unkeyed groups (hno, hug, mun, myn, sig, phi, sab ...) and number signs; none occurs in a deciphered sibling'),
    ]
    extra = o['gaps'][3:]
    o['gaps'] = o['gaps'][:3]  # the splice saver appends one list item per save in order; the rest follow below
    o['notes'] = o['notes'] + (" 23 Oct 2026 (re-read b16): N.45 and N.57 read (0.601 and 0.600 clean sentences on the reading "
                               "bodies; grade B), N.60 kept decoded, not read (0.504) with its partial reading; key extended by "
                               "goe, gix, goi, sid, hoe, fet, Vs, gid, sas, ree, sue, men and the marks gz/ang (key.md).")
    save(T, p); print('outcome')
    for g in extra:
        p = load(T); p['outcome']['gaps'].append(g); save(T, p); print('gap', g['item'][:40])


STEPS = [
    {'date': '2026-10-22', 'kind': 'access', 'what': "Re-read (REREAD_BRIEF, b16): all PARES images of N.45 (16), N.57 (4) and N.60 (16) opened, including the wrappers, blank pages and addresses not looked at before: no decipherment, interlinear or slip on any record; N.57's last three cipher lines and clear subscription are on f. 1v. A PARES search for neighbouring records returned HTTP 429.", 'result': 'failed'},
    {'date': '2026-10-22', 'kind': 'transcription', 'what': "Doubtful spots re-checked on the line strips at every break of sense: N.57 11 label corrections (oto in 'segun quan', plort/plart, the tilde-d = a six times), N.45 33 (the transcriber's fid merged fid despues and fud dicho, 17x; plix is plirt ni, 7x), N.60 5 (n57/n45a/n45b/n60_corrections.tsv; corrected files n57_transcription_v3, n45_pp*_v3, n60_transcription_v4).", 'result': 'worked'},
    {'date': '2026-10-22', 'kind': 'hypothesis', 'technique': ['contextual inference'], 'what': "Open groups resolved where one value fits every occurrence across N.45/N.57/N.60 and the siblings (b16_vich_kwic.py; key.md 'b16 additions'): goe aca (11), gix capitan (8; 'el gran capitan' x3), goi aquel (16), sid son (12), hoe governar (3), fet fue (15), Vs ss (17); gz and ang classed as clause marks. Rejected for a contradicting occurrence: pih querer, fob fortaleza, plix o, 7o rr, phi, reg, sil, sig.", 'result': 'worked'},
    {'date': '2026-10-23', 'kind': 'hypothesis', 'technique': ['contextual inference', 'plaintext matching'], 'what': "From the N.45 and N.60 re-reads: gid amor (carried by 8714 N.39's decipherment 'palabras de grande amor'), sas ver, ree poder, sue saber, men menester, each fitting all occurrences; soi, dup, fez, dop, pog, hug, pie, dax proposed and not adopted.", 'result': 'worked'},
    {'date': '2026-10-23', 'kind': 'reading', 'technique': ['contextual inference'], 'what': "Each letter built line by line into words in the figures' spelling (n45/n57/n60_build.txt), the reading generated with orthography modernised (b16_vich_make.py) and aligned word by word with its decode (b16_vich_align.py): N.45 3,968 of 3,984 words carried, N.57 431 of 433, N.60 5,026 of 5,074 (the rest checked by eye). Translations n45/n57/n60_en.md.", 'result': 'worked'},
    {'date': '2026-10-23', 'kind': 'reading', 'technique': ['language-model scoring'], 'what': "_check_reading.py on the reading bodies: N.45 0.601 (raw decode 0.213), N.57 0.600 (0.30-0.32), N.60 0.504 (0.197). N.45 and N.57 set read, grade B; N.60 stays decoded, not read, its reading kept as partial (about 600 unkeyed groups).", 'result': 'partial'},
]


def steps():
    for st in STEPS:  # one per save: the splice saver keeps the order of a single appended item
        p = load(T)
        p['solution'].append(st)
        save(T, p); print('step', st['kind'])


if __name__ == '__main__':
    {'texts': texts, 'docs': docs, 'outcome': outcome, 'steps': steps}[sys.argv[1]]()
