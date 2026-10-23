"""v8 (23 Oct 2026): VERIFY3 decisions on the read entries the translation wave could not translate.
Targeted profile edits through v8.py / relabel_r0.save (one change per save). Demotes go through set_state_idx.py.

    python research/reading_audit/v8_apply.py <folder>
"""
import subprocess
import sys
import pathlib

sys.path.insert(0, str(pathlib.Path(__file__).parent))
from relabel_r0 import load, save  # noqa: E402
import v8  # noqa: E402

HERE = pathlib.Path(__file__).parent
D = '2026-10-23'


def demote(T, idx, note):
    subprocess.run([sys.executable, str(HERE / 'set_state_idx.py'), T, str(idx), note], check=True)


def fraction(T, value, sentence):
    subprocess.run([sys.executable, str(HERE / 'set_fraction.py'), T, str(value), 'measured', sentence], check=True)


def outcome(T, **kw):
    for k, v in kw.items():
        p = load(T); p['outcome'][k] = v; save(T, p)


def gap_set(T, i, **kw):
    for k, v in kw.items():
        p = load(T); p['outcome']['gaps'][i][k] = v; save(T, p)


def gap_add(T, g):
    p = load(T); p['outcome']['gaps'].append(g); save(T, p)


def step(T, what, result, kind='verification', technique=('language-model scoring', 'contextual inference')):
    v8.add_steps(T, [dict(date=D, kind=kind, technique=list(technique), what=what, result=result)])


def entry_field(T, idx, k, v):
    p = load(T); p['outcome']['texts'][idx][k] = v; save(T, p)


def notes_append(T, s):
    p = load(T); p['outcome']['notes'] = p['outcome'].get('notes', '') + ' ' + s; save(T, p)


def rennes():
    T = 'rennes1563'
    base = ("Verify pass v8, 23 Oct 2026 (the translation wave could not translate it): back to decoded, not read. ")
    tail = (" Every glossed sibling in this cipher aligned and La Ferriere does not print the passage (Remaining gaps); "
            "blocker no-key-material. The partial reading is kept.")
    demote(T, 0, base + "The translator's partial reading f55_reading.md (aligned/f55.txt put into sentences, its '~' probable "
           "words counted as holes) scores 0.50 on explicit holes (4/8 sentences), 0.375 plain, hole rate 0.168: the holes in "
           "ll. 2, 4, 8-9 and 12 ([?vous] [?par], [?ayt] [?tenu], [?deliberay], [?monstrer] [?bonne], [?sessions]) break half "
           "the sentences." + tail)
    demote(T, 1, base + "The translator's partial reading c390_p357_p358_reading.md (aligned/p357.txt and p358.txt into "
           "sentences) scores 0.267 on explicit holes (4/15), 0.133 plain, hole rate 0.213: probable words and {n} runs in "
           "most clauses." + tail)
    demote(T, 3, base + "The translator's partial reading c392_p231_bourdin_reading.md (aligned/c392.txt into sentences) "
           "scores 0.167 on explicit holes (3/18), 0.167 plain, hole rate 0.232: probable words and unread runs in nearly "
           "every sentence." + tail)
    fraction(T, 0.0, "23 Oct 2026, verify v8: f. 55, pp. 357-358 and Colbert 392 p. 231 back to decoded, not read (0.50, "
             "0.27, 0.17 clean sentences on explicit holes, v2_score.py), with p. 139 already so: no letter reads, 0 of 2,311 "
             "tokens. Withdrawn as a reading figure: 0.658.")
    outcome(T, **{'class': 'not read'})
    outcome(T, method='not solved')
    outcome(T, parts=[dict(
        label="four letters (Tomokiyo's Rennes key applied; decoded, not read)",
        records='BnF fr. 3181 f. 55; 500 Colbert 390 pp. 139, 357-358; 500 Colbert 392 p. 231',
        method='read with known key', extent='partial',
        basis="Tomokiyo's reconstruction of the Bishop of Rennes' cipher, calibrated per hand on the glossed siblings, decoded "
              "with an LM lattice: 0.79 of tokens in sense words (measure.py, 5 Oct 2026), but holes in most sentences of every "
              "letter (0.50, 0.27, 0.17, 0.25 clean sentences on explicit holes; verify v8, 23 Oct 2026). Decoded, not read.")])
    gap_set(T, 0, item="fr. 3181 f. 55 decoded, not read (0.50 clean sentences on explicit holes, verify v8 23 Oct 2026): "
            "l.2 ꝥ, ɼ ᑲ; l.4 '10 ᑲ ɗ xy ee z r'; l.8 'ß La ᑲ ᑲ z 10 9 z'; l.9 '‡ G̃ ꜧ ᑲ ᑲ ɗ ᑲ ᑲ'; l.12 'h Ə'; slips in "
            "ayt tenu, deliberay, monstrrer, sessions")
    gap_set(T, 1, item="500 Colbert 390 pp. 357-358 decoded, not read (0.27 clean sentences on explicit holes, verify v8 23 Oct "
            "2026): p.357 l.3-4 'lennuieux ce me pleste', l.5, l.8 avoir/l'effect, p.358 s'offrira, esperer, gouvernement, "
            "lumiere, remects, de disposer")
    gap_set(T, 2, item="500 Colbert 392 p. 231 decoded, not read (0.17 clean sentences on explicit holes, verify v8 23 Oct 2026): "
            "maue, ſ λ ², ‡‡ ~, πꝫ (twice), ꞁꞁ ℌ z 9 ‡‡, La ƀ ſſ z, fc 7, conseil, comme en, leurs")
    step(T, "Verify v8: the translator's partial readings scored with v2_score.py (explicit holes): f. 55 0.50 (f55_reading.md), "
         "Colbert 390 pp. 357-358 0.27 (c390_p357_p358_reading.md), Colbert 392 p. 231 0.17 (c392_p231_bourdin_reading.md); "
         "holes in most sentences, every key source already tried. All three back to decoded, not read; with p. 139 no letter "
         "reads: class not read, method not solved (key applied as a part), fraction_read 0.", 'failed')


def selve():
    T = 'selve1535'
    v8.set_fields(T, '#0', dict(reading='R3697_reading.md'))
    v8.review(T, '#0', "Verify v8, 23 Oct 2026: the sweep's 0.57 scored READING_R3697.md as a whole, where the clear text, the "
              "decipherer's glosses and the struck runs sit in lower-case brackets and count as holes. The unstruck cipher written "
              "out as running text (R3697_reading.md, holes and doubtful words marked) scores 0.733 on explicit holes (11/15), "
              "0.667 plain, hole rate 0.089: the Swiss road, the Imperial ambassador's watch and his urging the merchant to go to "
              "the French court, the informants reporting to the Turk build sentences; holes at the blot and the cancelled name "
              "(Anthon[e] de Le...) and a few single signs. Rests on Tomokiyo's Selve key as extended in KEY.md.", 'B')
    step(T, "Verify v8: R3697 unstruck cipher written out as running text (R3697_reading.md) and scored: 0.733 explicit holes, "
         "0.667 plain (the sweep's 0.57 counted clear-text and gloss brackets as holes). Keeps read; reading pointed at the new "
         "file.", 'worked')


def sessa():
    T = 'sessa1593'
    demote(T, 0, "Verify pass v8, 23 Oct 2026 (the translation wave could not translate it): back to decoded, not read. The "
           "running text of sense.tsv's reading column (no45_reading.md, the 5 Oct 2026 re-transcription read with the office key "
           "BnF fr. 3995 f. 97) scores 0.50 on explicit holes (7/14 sentences), 0.357 plain, hole rate 0.158: the opening "
           "(con este achaque ... a costa de la bolsa), the residence passage and the close carry unresolved groups and "
           "nomenclature groups with no value ([ʃo], [9̈4], [ʒe], [Val], [ral], [ʃep:], [pir]). No contemporary decipherment of "
           "no. 45 exists; the groups are not on the f. 97 sheet: blocker no-key-material. no45_reading.md kept as a partial reading.")
    fraction(T, 0.75, "23 Oct 2026, verify v8: no. 45 back to decoded, not read (0.50 clean sentences on explicit holes); "
             "letters that read: no. 79 504 + no. 47 478 = 982 of 1,310 groups = 0.750. Withdrawn: 0.925.")
    gap_set(T, 1, blocker='no-key-material',
            detail='see sense.tsv unread column; doubtful syllables with no gloss or second copy to settle them (renamed from open-codes, 23 Oct 2026)')
    gap_add(T, dict(item='no. 45 decoded, not read (0.50 clean sentences on explicit holes, verify v8 23 Oct 2026): open groups in '
                         'the opening, the residence passage and the close',
                    blocker='no-key-material',
                    detail='nomenclature groups not on the f. 97 sheet (ʃo, 9̈4, ʒe, Val, ral, ʃep, pir) and unresolved syllables; '
                           'no contemporary decipherment of no. 45'))
    notes_append(T, "23 Oct 2026, verify v8: no. 45 back to decoded, not read (no45_reading.md 0.50 on explicit holes); nos. 79 "
                    "and 47 stay read; fraction_read 0.750.")
    step(T, "Verify v8: no. 45 running text (no45_reading.md, from sense.tsv's reading column) scored with v2_score.py: 0.50 "
         "explicit holes, 0.357 plain, hole rate 0.158; open nomenclature groups in most sentences, no decipherment of the letter. "
         "Back to decoded, not read; fraction_read 0.925 -> 0.750. Gap blocker open-codes renamed no-key-material.", 'failed')


def siena14():
    T = 'siena14'
    demote(T, 0, "Verify pass v8, 23 Oct 2026 (the translation wave could not translate it): back to decoded, not read. The "
           "running text of L01-L06 from the second reading pass (transcripts/no14_L01-L06_reading.md, its {?} words as [?word], "
           "{x} as [...]) scores 0.0 on explicit holes (0/7 sentences), 0.0 plain, hole rate 0.289: the gist holds (arrived "
           "safe, ready to follow your commands; Domenico with a servant of <7H>) but every sentence carries doubtful words "
           "resting on look-alike sign classes (Q/Q4, 8/TH, P/PHI) the DECODE image does not separate: blocker illegible. "
           "The partial reading is kept.")
    fraction(T, 0.0, "23 Oct 2026, verify v8: L01-L06 back to decoded, not read (0.0 clean sentences on explicit holes, hole rate "
             "0.289); no line of the letter reads: 0 of about 1,500 tokens. Withdrawn as a reading figure: 0.28.")
    outcome(T, **{'class': 'not read'})
    outcome(T, method='not solved')
    outcome(T, parts=[dict(
        label='no. 14 (key recovered ciphertext-only; decoded, not read)', records='DECODE R4802',
        method='key recovered from ciphertext-only', extent='partial',
        basis="homsolve2 reached the key with no crib (validation pass, z 6.1 against random keys); the decode gives the gist "
              "(arrival, Domenico's talk with a servant of <7H>, Tuscany and the three powers) but doubtful words in every "
              "sentence: L01-L06 0.0, L07-L26 0.143 clean sentences on explicit holes. Decoded, not read (verify v8, 23 Oct 2026).")])
    gap_add(T, dict(item='L01-L06 decoded, not read (0.0 clean sentences on explicit holes, hole rate 0.289; verify v8 23 Oct 2026)',
                    blocker='illegible',
                    detail='the doubtful words rest on look-alike sign classes (Q/Q4, 8/TH, P/PHI) that the DECODE image (about '
                           '15-20 px a sign) does not separate'))
    step(T, "Verify v8: L01-L06 running text (transcripts/no14_L01-L06_reading.md) scored with v2_score.py: 0.0 explicit holes "
         "(0/7), hole rate 0.289; doubtful words in every sentence. Back to decoded, not read; no line reads: class not read, "
         "method not solved (key recovered ciphertext-only as a part), fraction_read 0.", 'failed')


def sperantio():
    T = 'sperantio1534'
    v8.set_fields(T, '#1', dict(reading='r9411/R9411_reading.md'))
    v8.set_fields(T, '#2', dict(reading='r9411/R9412_reading.md'))
    v8.review(T, '#1', "Verify v8, 23 Oct 2026: rescored as running text (r9411/R9411_reading.md, written from "
              "reading_r9411.txt by v3b_lines.py: line numbers and comments cut, line-end breaks joined): 0.71 on explicit holes "
              "(22/31), 0.452 plain (Latin word list), hole rate 0.078; the sentences hold (the request to go first to the "
              "governor, the mines, Freiberger, the mining ordinance). Rests on the letter's own contemporary interlinear "
              "decipherment over every line, with the key rebuilt from it.", 'A')
    v8.review(T, '#2', "Verify v8, 23 Oct 2026: rescored as running text (r9411/R9412_reading.md, v3b_lines.py --conj, the <...> "
              "conjectures as holes): 0.648 on explicit holes (35/54), 0.389 plain (1534 German, which the word list does not "
              "know), hole rate 0.106; with the clear Latin cut 0.642, hole rate 0.114. Marginal: the opening (Werbőczy's "
              "peace, the towns to be handed over), QUARTO, the Schmalz and factor passage and the close build sentences; "
              "TERTIO (ll. 12-17) and ll. 31-41 do not. Rests on the R9411 key refitted on German; no contemporary "
              "decipherment of this letter; 27 cipher words unread.", 'B')
    step(T, "Verify v8: R9411 and R9412 rescored as running text (v3b_lines.py; R9411_reading.md, R9412_reading.md written and "
         "pointed at): R9411 0.71 explicit holes, hole rate 0.078; R9412 0.648 (0.642 without the clear Latin), hole rate "
         "0.106-0.114, marginal, TERTIO and ll. 31-41 do not build. Both keep read.", 'worked')


def visconti():
    T = 'visconti1529'
    v8.set_fields(T, '#0', dict(reading='fr3045_f28_v2_reading.md'))
    v8.review(T, '#0', "Verify v8, 23 Oct 2026: the sweep's 0.59 scored fr3045_f28_reading.md, the line-by-line first pass. "
              "Running text rewritten with the push-pass readings of fr3045_f28_final.md, as the 22 Oct review asked "
              "(fr3045_f28_v2_reading.md): 0.778 on explicit holes (14/18), 0.278 plain (the word list does not know 1528 "
              "Lombard spelling), hole rate 0.111. Marginal: Savona relieved, the loss of reputation 'come batale perduta', the "
              "adventurers gone for want of pay, the money in Puglia, the few late lances and the close build sentences; ll. 8-9 "
              "('et pur al tuto ... cum Urbino'), the 'quanto ci è' clause and ll. 14-15 ('Designati ... as[?]sedio') do not. "
              "Codes [42] [rr] [qq] [ep] have no key.", 'B')
    step(T, "Verify v8: fr. 3045 f. 28 running text rewritten with the push-pass readings (fr3045_f28_v2_reading.md) and scored: "
         "0.778 explicit holes, 0.278 plain, hole rate 0.111; three clauses do not build. Keeps read, marginal; reading pointed "
         "at the new file.", 'partial')


def soria():
    T = 'soria1523'
    demote(T, 3, "Verify pass v8, 23 Oct 2026 (the translation wave could not translate it): back to decoded, not read. "
           "R9494_reading.md (measure/kb_r9494.txt, the 5 Oct 2026 re-read with R9495/R9496 collated, joined into sentences) "
           "scores 0.583 on explicit holes (7/12 sentences), 0.333 plain, hole rate 0.118: the courier sentence ([aqo], [tep-] "
           "[-r], [aeze] dias) and the money sentence ([te], [dos] [per] y ocho mil, [zu-] [-es]) carry three holes each, and "
           "the R9496 paragraph breaks off. The holes are key-B nomenclature groups spelled the same in all three copies, with no "
           "attestation in the R9844 crib: blocker no-key-material. The reading is kept as a partial reading.")
    fraction(T, 0.873, "23 Oct 2026, verify v8: R9494-96 back to decoded, not read (0.583 clean sentences on explicit holes); "
             "3,412 - 328 = 3,084 of 3,533 units in letters that read = 0.873. Withdrawn: 0.966.")
    outcome(T, **{'class': 'read in part'})
    p = load(T); p['outcome']['parts'][1]['basis'] += (" 23 Oct 2026, verify v8: 26 July (R9494-96) decoded, not read "
                                                      "(0.583 on explicit holes).")
    save(T, p)
    gap_set(T, 3, item="R9494-96 decoded, not read (0.583 clean sentences on explicit holes, verify v8 23 Oct 2026): te, per, "
            "tep, zu, tol, the day count, and two phrases of R9496's extra paragraph", blocker='no-key-material',
            detail='three copies collated; they spell the same groups; not in the R9844 crib (was open-codes)')
    step(T, "Verify v8: R9494 reading (R9494_reading.md) scored with v2_score.py: 0.583 explicit holes (7/12), 0.333 plain, hole "
         "rate 0.118; two of four sentences carry three code-group holes. Back to decoded, not read; class read -> read in part; "
         "fraction_read 0.966 -> 0.873.", 'failed')


def siena8():
    T = 'siena8'
    v8.review(T, '#0', "Verify v8, 23 Oct 2026: a reading of fragments. The slip mixes clear words and four cipher runs; "
              "texts/no08_reading.md gives the runs only (the clear text between them is not transcribed). Scored 0.50 because "
              "the two resolved name signs were written lower-case ([duca di Milano]) and the run-edge '…' marks (clear text, "
              "not unread cipher) counted as holes; with the name signs capitalised and the marks dropped: 1.0 on explicit holes "
              "(4/4), 0.25 plain (1440 Sienese spelling), hole rate 0. Each run is a clause that holds (the league between the "
              "Duke of Milan and the Marquis of Ferrara; the Venetians and their league; Bianca given to Leonello; 'grandisimi "
              "fatti'), and every word is confirmed letter for letter by the contemporary memorandum on the same sheet "
              "(paragraphs 5-7). Not 'not prose' (it is running sentences), not decoded-only (no hole).", 'A')
    step(T, "Verify v8: no08_reading.md rescored after capitalising the resolved name signs and dropping the run-edge marks: "
         "1.0 explicit holes (4/4), hole rate 0; every word carried by the contemporary memorandum. Keeps read, as a reading of "
         "four fragments.", 'worked', kind='verification', technique=('plaintext matching', 'language-model scoring'))


def salviati():
    T = 'salviati1525'
    p = load(T); e = p['outcome']['texts'][0]
    e['note'] = e['note'] + (" Verify v8, 23 Oct 2026: the excerpt held here does not read on its own: v2_score.py 0.0 on explicit "
                             "holes and plain (0/2 sentences, a [?] in both, hole rate 0.152). The reading is George Lasry's "
                             "(3/8 pages deciphered in part, not in the repository); the state is left as his pointer.")
    save(T, p)
    step(T, "Verify v8: Lasry's f54r excerpt (lasry_entry.md) scored with v2_score.py: 0.0 explicit holes (0/2, a [?] in each "
         "sentence). State left as the pointer to Lasry's reading; note added that the excerpt held here does not read.",
         'partial', kind='verification', technique=('language-model scoring',))


if __name__ == '__main__':
    dict(rennes1563=rennes, selve1535=selve, sessa1593=sessa, siena14=siena14, sperantio1534=sperantio,
         visconti1529=visconti, soria1523=soria, siena8=siena8, salviati1525=salviati)[sys.argv[1]]()
