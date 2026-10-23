"""Re-read brief (REREAD_BRIEF.md), batch b13: lopehurtado (R9634, R9645, R9646, R9656) and cobham1588 (R8490, R8492,
R8495, R8496).

Targeted profile edits with the splice saver of relabel_r0.py; one save per change.

    python research/reading_audit/reread_b13.py lopehurtado|cobham1588
Helpers: b13_crop.py, b13_enhance.py (image crops to the scratchpad), b13_score.py (clean-sentence share of a reading
body). Logs: targets/lopehurtado/texts/R9634-R9656_reread_log.md, targets/cobham1588/texts/R8490-R8496_reread_log.md.
"""
import sys
import pathlib

sys.path.insert(0, str(pathlib.Path(__file__).parent))
from relabel_r0 import load, save  # noqa: E402

DATE = '2026-10-22'

LOPE = {
    'R9646': 'Re-read 22 Oct 2026 (batch b13; texts/R9646_reading.md, texts/R9646_en.md, texts/R9634-R9656_reread_log.md): '
             'clean share 0.727 on the whole letter, carried by the clear; of the five cipher runs, 1-3 read (the Pope '
             'concerted with Ferrara, en lo de la [?decima]); run 4 (abia miedo que oviese de [...] en [...]) and run 5 '
             '(ofrecer [...] al papa para sus necesidades ... por dinero [?hara] toda [...]) keep their holes, so what the '
             'Pope feared and what was to be offered are lost. Blockers: no-key-material (zip, zob, ʃof seen once) and '
             'needs-physical-access (an unkeyed looped sign opens ð∠89&Ho and ð∠47; DECODE has no larger image, the RAH '
             'library is behind a bot check).',
    'R9656': 'Re-read 22 Oct 2026 (batch b13; texts/R9656_reading.md, texts/R9656_en.md, texts/R9656_corrections.tsv): '
             'clean share 0.564. f. 334v now reads (lo de [?Ostia]: &δϑα7 o-s-t-i-a; y como [?assi] se [?tomaran]; the '
             'Don Juan sentence in full); f. 334r ll. 4-6 and 13-17 still break on ɲ4∠&ɣ̊t, ɣαδ8, teɡ∂ ϯ∠8ɣ̊oo, ϙ8, 8x&, '
             'ßϑ7 and code 30. Blockers: no-key-material (codes seen once), needs-physical-access (signs at the scan\'s '
             'limit), illegible (the left half of the f. 335r clear copy, re-enhanced).',
    'R9645': 'Re-read 22 Oct 2026 (batch b13; texts/R9645_reading.md, texts/R9645_en.md, texts/R9645_corrections.tsv): '
             'clean share 0.528. f. 243r now reads to l. 12 (que abia tomado assiento con el duque de Ferrara; the feudo '
             'Alexander VI [?solto] con el [?casamiento] de su [?fija]; no league con [?ningun] [?principe] ni [?señoria] '
             'save the Pope and the Emperor); r13-r17 and upper f. 243v break on #ʇʇHoε97, xωt74, tec, zuf, ʃen, '
             'ɣ7∠8ϑ9Ho, tep, 8&ɣ̊98, ϑωε7ϙ. Blockers: no-key-material, needs-physical-access.',
    'R9634': 'Re-read 22 Oct 2026 (batch b13; texts/R9634_reading.md, texts/R9634_en.md): the line readings written out '
             'as continuous text with the f. 14r clear opening; clean share 0.506, carried by the clear; holes in most '
             'cipher sentences (about 45 codes seen once, the spelled place names of 14r12, 14v03). Blockers: '
             'no-key-material, needs-physical-access.',
}

LOPE_GAPS_DROP = ('R9645 (73% read)', 'R9656 (61% read)', 'R9634 (71% read)', 'R9634 spelled words', 'R9646 (80% read)')
LOPE_GAPS = [
    {'item': 'R9646 (decoded, not read; runs 4-5): zip, zob, ʃof and the spelled ð∠89&Ho, 8ʒtoo, ð∠47 ɣ?8δHo',
     'blocker': 'no-key-material',
     'detail': 'codes seen once in 21 letters, no crib; the looped sign opening ð∠89&Ho and ð∠47 is keyed nowhere and '
               'needs a better image (re-read 22 Oct 2026, b13)'},
    {'item': 'R9656 (decoded, not read): ɲ4∠&ɣ̊t (l. 6), ɣαδ8 (l. 9), teɡ∂ ϯ∠8ɣ̊oo (l. 13), ϙ8, 8x& (l. 14), zarɣ̊, '
             'ßϑ7, code 30',
     'blocker': 'no-key-material',
     'detail': 'single-occurrence codes and spelled words with one doubtful sign; the f. 335r clear copy is illegible in '
               'the left half of every line even after background subtraction (22 Oct 2026, b13)'},
    {'item': 'R9645 (decoded, not read): f. 243r r13-r17 and f. 243v ll. 1-10 (#ʇʇHoε97, xωt74, tec, zuf, ʃen, tep, '
             'ɣ7∠8ϑ9Ho, 8&ɣ̊98, ϑωε7ϙ)',
     'blocker': 'no-key-material',
     'detail': 'no gloss above these lines; codes seen once; f. 243r ll. 1-12 now read (22 Oct 2026, b13)'},
    {'item': 'R9634 (decoded, not read): about 45 code groups seen once and the spelled place names (14r12, 14v03, '
             '14v16, 15r11, 15v05, 15v12)',
     'blocker': 'no-key-material',
     'detail': 'no clear version, no duplicate, nothing in CSP Spain ii or Sanuto XXXIII'},
    {'item': 'Doubtful signs in the spelled words of R9634, R9645, R9646, R9656 (8/ϑ, ∂ s/p/t, ε l/g, the looped sign)',
     'blocker': 'needs-physical-access',
     'detail': 'DECODE has no larger file; the RAH Biblioteca Digital (Salazar A-26) is behind a proof-of-work bot check '
               'and needs Daniel in a browser'},
]

LOPE_STEPS = [
    {'date': DATE, 'kind': 'transcription',
     'what': 'Re-read (REREAD_BRIEF, batch b13). Existing text sought again: R9645 has glosses only at the foot of f. '
             '243v; R9656\'s faded f. 335r clear copy re-enhanced (b13_enhance.py, background subtraction): still only '
             'the right half of each line; no copy for R9634 or R9646. The unread stretches of all four letters cropped '
             'at 1-4x from the DECODE images (b13_crop.py). Labels corrected (texts/<doc>_corrections.tsv): the crossed '
             't-form is m (R9645 r01 ϑ&t7 xm = tomado; R9656 v01 tomaran), the 8-form stands for ϑ t (R9656 vB1 &δϑα7 = '
             'Ostia), R9656 v01 zuc not zil, R9645 v07 xod ɣ3& = fecho. The lopehurtado1523 look-alike lessons (ß-like '
             'a written ʇʇ, y ʇʇ = g) tried on every unread word: no gain.',
     'result': 'partial', 'technique': ['manual reconstruction']},
    {'date': DATE, 'kind': 'hypothesis',
     'what': 'Context readings, bracketed as probable: R9645 r05 los dineros del feudo que el papa Alexandro le [?solto] '
             'con el [?casamiento] de su [?fija] (Alexander VI lowered Ferrara\'s census at Lucrezia Borgia\'s marriage); '
             'r07-08 con [?ningun] [?principe] ni [?señoria] pudiese confederarse; R9656 vB1 lo de [?Ostia] (R9649\'s '
             'subject). Codes zip, zob, ʃof, tec, zuf, ʃen, tep, 30 and the looped sign of R9646 ð∠89&Ho / ð∠47 stay open.',
     'result': 'partial', 'technique': ['contextual inference']},
    {'date': DATE, 'kind': 'reading',
     'what': 'Continuous readings with English (texts/R9634_reading.md ... R9656_en.md), aligned word by word with the '
             'decodes, supplied words bracketed. Clean share of the reading bodies (b13_score.py): R9646 0.727 (carried '
             'by the clear; cipher runs 4-5 keep their holes), R9656 0.564, R9645 0.528, R9634 0.506. All four stay '
             'decoded, not read: the cipher sentences do not hold.',
     'result': 'failed', 'technique': ['manual reconstruction', 'language-model scoring']},
]


def lope():
    F = 'lopehurtado'
    for doc, note in LOPE.items():
        p = load(F)
        t = [x for x in p['outcome']['texts'] if x.get('doc') == doc][0]
        t['note'] = note
        t['reading'] = 'texts/%s_reading.md' % doc
        t['translation'] = 'texts/%s_en.md' % doc
        save(F, p)
    p = load(F)
    p['outcome']['gaps'] = [g for g in p['outcome']['gaps'] if not g['item'].startswith(LOPE_GAPS_DROP)]
    save(F, p)
    for g in LOPE_GAPS:
        p = load(F)
        if not any(x['item'] == g['item'] for x in p['outcome']['gaps']):
            p['outcome']['gaps'].append(g)
            save(F, p)
    for s in LOPE_STEPS:
        p = load(F)
        if not any(x.get('what') == s['what'] for x in p['solution']):
            p['solution'].append(s)
            save(F, p)
    print('lopehurtado done')


COB = {
    'R8490': 'Re-read 22 Oct 2026 (batch b13; texts/R8490_reading.md, texts/R8490_en.md, texts/R8490_corrections.tsv, '
             'texts/R8490-R8496_reread_log.md): the clear of ff. 80r-80v transcribed as running text; the "armada(s)" of '
             '21 Sept is "treaties" / "treaty of [?Breda]" (the third sign is the 7-form e, not ∽ m), so the hostages '
             'passage reads (Touching hostages, yt ys honorable for [7] to [...] their surety to these termes, as usuall '
             'yn all treaties ...) and so does the f. 80v run (22 hath a desire to retourne from theym); the runs of ll. '
             '8-11 and 31-34 keep holes in most words. Clean share 0.114 (0.514 with Elizabethan spellings mapped). '
             'Blocker: no-key-material (unglossed signs W, the square, codes 22 and 27; polyphonic signs).',
    'R8492': 'Re-read 22 Oct 2026 (batch b13; texts/R8492_reading.md, texts/R8492_en.md): the f. 88r runs re-checked on '
             'the image; only the haven, there, Italians, Antonio and a few probable words read; the 21 Sept guesses (of '
             'Rain, spoil, Naples as certain) withdrawn. Blocker: no-key-material (signs K, ɔ and the polyphonic set '
             'glossed nowhere).',
    'R8495': 'Re-read 22 Oct 2026 (batch b13; texts/R8495_reading.md, texts/R8495_en.md): the clear news of f. 92r '
             'transcribed as running text (Armada at Lisbon, Gonzaga at Watten, armour to Cambrai, Casimir, Guise); the '
             'ten cipher lines give scattered probable words only ([?Bruges], [?charge], [?letters], Newport, in [?prison]). '
             'Blocker: no-key-material.',
    'R8496': 'Re-read 22 Oct 2026 (batch b13; texts/R8496_reading.md, texts/R8496_en.md): f. 96v transcribed (cipher, '
             'close, postscript); f. 97r is blank, so there are no f. 97r runs; f. 96r (wholly clear) not transcribed. '
             'The f. 96v runs give scattered probable words ([?passed], [?Within] [?France], [?servants], [?priests], of '
             '[?letters] for the [?people]). Blocker: no-key-material.',
}

COB_GAPS = [
    {'item': 'R8490 (ff. 80r-80v), decoded, not read: runs c∪ǂǂ8ϕ, WLϕΛ, Xd+c:·87, ∞7γǂǂcL and the 22/27 passage of ll. '
             '31-34 (-··XLΛ, -Tcw7Λ, ӾcH ΛcVIw7, VcL##ΛϕcIΛ); codes 22, 27 and the square',
     'blocker': 'no-key-material',
     'detail': 'the signs W and the square and the codes 22, 27 are glossed in no sibling (R8481, R8488, R8489, R8493); the '
               'hostages passage and the f. 80v run now read (22 Oct 2026, b13)'},
    {'item': 'R8492 (f. 88r), decoded, not read: the name after "captain", the words after "haven of", ll. 3-11 and the '
             'cipher words of ll. 12-20',
     'blocker': 'no-key-material',
     'detail': 'signs K, ɔ/Q, upsilon, rho glossed nowhere; polyphonic signs (caret s/t/a, γ r/y, c o/a/e, ϕ l/t/p) leave '
               'several readings with nothing to choose between them'},
    {'item': 'R8495 (f. 92r), decoded, not read: runs 92a-c and the ten cipher lines below "Dunkergh: 4 sent by"',
     'blocker': 'no-key-material',
     'detail': 'same unglossed and polyphonic signs; the solver finds no word with two edits'},
    {'item': 'R8496 (f. 96v), decoded, not read: all runs but a few probable words',
     'blocker': 'no-key-material',
     'detail': 'same signs; f. 97r is blank (no runs there)'},
    {'item': 'Clear text: f. 96r (R8496) and the bracketed secretary-hand words of ff. 80, 88, 92, 96v',
     'blocker': 'not-attempted',
     'detail': 'f. 96r is wholly clear and outside the cipher; not transcribed on 22 Oct 2026'},
]

COB_STEPS = [
    {'date': DATE, 'kind': 'transcription',
     'what': 'Re-read (REREAD_BRIEF, batch b13). No decipherment, clear copy or print found again (neighbouring records '
             'R8491, R8493, R8494 checked; f. 97r of R8496 is blank). The clear of ff. 80r-80v, 92r and 96v transcribed '
             'as running text from the 7,200 px DECODE images in strips (f. 88r re-checked, f. 96r not transcribed); the '
             'cipher runs re-read at 0.5-1.0x (b13_crop.py). Relabelled (texts/R8490_corrections.tsv, '
             'texts/runs_corrected.txt): f. 80r AVmATA/AVmAT -> AV7ATA/AV7AT (7-form e, not ∽): treaties, treaty of '
             '[?Breda] (not armada); l. 18 ϸcAAUӾLA hostages; the l. 19-20 run divided into eight barred words (A··VA⊥ '
             'surety).',
     'result': 'partial', 'technique': ['manual reconstruction']},
    {'date': DATE, 'kind': 'reading',
     'what': 'Partial readings with modern English (texts/R8490_reading.md ... R8496_en.md), every cipher word graded: '
             'plain only with all signs at their glossed values, [?word] for one doubtful sign or one solver edit, the '
             '21 Sept guesses (Rain, spoil, Portugals, noblemen, Roper, Iohn) withdrawn to holes. Clean share (b13_score.py, '
             'en; E=1 maps Elizabethan spellings): R8490 0.114/0.514, R8492 0.0/0.118, R8495 0.0/0.074, R8496 0.2/0.35. '
             'All four stay decoded, not read: only R8490\'s hostages passage and f. 80v run build cipher sentences.',
     'result': 'failed', 'technique': ['manual reconstruction', 'language-model scoring']},
]


def cob():
    F = 'cobham1588'
    for doc, note in COB.items():
        p = load(F)
        t = [x for x in p['outcome']['texts'] if x.get('doc') == doc][0]
        t['note'] = note
        t['reading'] = 'texts/%s_reading.md' % doc
        t['translation'] = 'texts/%s_en.md' % doc
        save(F, p)
    p = load(F)
    p['outcome']['gaps'] = []
    save(F, p)
    for g in COB_GAPS:
        p = load(F)
        p['outcome']['gaps'].append(g)
        save(F, p)
    for s in COB_STEPS:
        p = load(F)
        if not any(x.get('what') == s['what'] for x in p['solution']):
            p['solution'].append(s)
            save(F, p)
    print('cobham1588 done')


if __name__ == '__main__':
    {'lopehurtado': lope, 'cobham1588': cob}[sys.argv[1]]()
