"""Re-read brief (REREAD_BRIEF.md), batch b20: isabella1531 (R9955, R9956), kaa4591 (R9409, R9427), kaa4591b (R9417, R9323).

Targeted profile edits with the splice saver of relabel_r0.py; one save per change.

    python research/reading_audit/reread_b20.py isabella
Helpers: b20_fetch.py (DECODE record files to the scratchpad), b20_crop.py (strips at native resolution).
"""
import sys
import pathlib

sys.path.insert(0, str(pathlib.Path(__file__).parent))
from relabel_r0 import load, save  # noqa: E402

REV = dict(by='Claude Opus 5.5', date='2026-10-22')


def mark_read(t, doc, fields, grade, note):
    p = load(t)
    e = [x for x in p['outcome']['texts'] if x.get('doc') == doc]
    assert len(e) == 1, doc
    e = e[0]
    e.pop('note', None)
    e['state'] = 'read'
    e.update(fields)
    e['reading_review'] = dict(grade=grade, **REV, note=note)
    save(t, p); print('read', t, doc)


def set_note(t, doc, note, **fields):
    p = load(t)
    e = [x for x in p['outcome']['texts'] if x.get('doc') == doc]
    assert len(e) == 1, doc
    e[0]['note'] = note
    e[0].update(fields)
    save(t, p); print('note', t, doc)


def add_step(t, step):
    p = load(t)
    p['solution'].append(step)
    save(t, p); print('step', t)


def set_outcome(t, **kw):
    for k, v in kw.items():
        p = load(t)
        p['outcome'][k] = v
        save(t, p)
    print('outcome', t, list(kw))


def set_doc(t, doc, **kw):
    for k, v in kw.items():
        p = load(t)
        e = [x for x in p['documents'] if x.get('id') == doc][0]
        e[k] = v
        save(t, p)
    print('doc', t, doc, list(kw))


# ---------------------------------------------------------------- isabella1531
def isabella():
    T = 'isabella1531'
    mark_read(T, 'R9955', {
        'transcription': ['texts/R9955_reading.md'],
        'decryption': 'texts/R9955_reading.md',
        'reading': 'texts/R9955_reading.md', 'translation': 'texts/R9955_en.md', 'language': 'es',
        'summary': "Charles V at Regensburg to the Empress Isabella, 30 April 1532 (DECODE: Isabella to Charles, 1531): he has taken a loan of 100,000 escudos from Ansaldo de Grimaldo, Genoese, to be repaid in 1533 by bills of exchange on Alonso de Baeza, secured by a juro on Castilian revenues, with a life grant in Naples; the cipher passages explain that the 100,000 ducats for his departure are not enough and press her to have the bills accepted at once. Read from the contemporary decipherment (doc. 196, on the DECODE images); also printed by Luo (2021) pp. 285-287."},
        'A', "Read 23 Oct 2026 (b20): clear text of doc. 195 and the contemporary decipherment of its three cipher passages (doc. 196, DECODE image P3, never transcribed before) transcribed from the images; figures spot-checked against the doc. 112 key printed by Luo (2021) p. 601 ('las necesidades'). No word supplied. Body 0.744 clean sentences (29/39), explicit holes 1.00; the unclean sentences are period spellings and names.")
    mark_read(T, 'R9956', {
        'transcription': ['texts/R9956_reading.md'],
        'decryption': 'texts/R9956_reading.md',
        'reading': 'texts/R9956_reading.md', 'translation': 'texts/R9956_en.md', 'language': 'es',
        'label': "R9956, Francisco de los Cobos to his nephew Juan Vázquez, Brussels 11 Jan 1531 (AGS Estado 496 ff. 205-206)",
        'summary': "Francisco de los Cobos (signed 'Covos comendador mayor') to his nephew Juan Vázquez [de Molina], secretary, Brussels, 11 January 1531 (DECODE: Isabella to Charles V). Clear: Benavides's departure, the courier of the archdeacon of Segovia about the Toledo regimiento. Cipher: news for the Empress: the Emperor is well and busy with the Low Countries; Monsieur de Praet gone to France; no answer yet to the Protonotary Gambara on the council, pending the King of the Romans' opinion; Italy quiet, the Siena exiles restored and the Spanish infantry kept nearby; the Pope as before; contradictory reports of the Turk coming by Hungary and Italy. Read from the contemporary decipherment (doc. 206, on the DECODE images)."},
        'A', "Read 23 Oct 2026 (b20): clear text of f. 205 and the contemporary decipherment of the cipher passage (doc. 206 recto and verso, DECODE images P4/P8, never transcribed before) transcribed from the images; figures spot-checked against the doc. 112 key (Luo 2021 p. 601): 'despachandose este correo de mercaderes ... sazon'. No word supplied; four doubtful words [?] and the line 'De hebrero [...]'. Body 0.714 clean sentences (10/14), explicit holes 1.00.")
    set_doc(T, 'R9955', read='read', pages=6, cleartext_in_document='separate passages',
            plaintext={'location': ['separate folio'], 'source': "Contemporary decipherment of the three cipher passages on a separate sheet, AGS Estado leg. 496 doc. 196 (DECODE image P3), transcribed 23 Oct 2026; also printed in Luo (2021) pp. 285-287.", 'partial': False},
            transcription={'by': 'llm from images', 'source': 'Claude Opus 5.5, 23 Oct 2026: clear text and decipherment sheet transcribed from the DECODE images (texts/R9955_reading.md); the cipher signs not transcribed', 'image_quality': 'good', 'notes': 'Images P1, P4 = doc. 195 ff. 1r-1v; P3 = doc. 196 (decipherment); P6 = address leaf; P2, P5 blank.'})
    set_doc(T, 'R9956', read='read', pages=8, cleartext_in_document='separate passages',
            route='Francisco de los Cobos (Brussels) to his nephew Juan Vázquez [de Molina], secretary',
            plaintext={'location': ['separate folio'], 'source': "Contemporary decipherment of the cipher passage on a separate sheet, AGS Estado leg. 496 doc. 206 (DECODE images P4, P8), transcribed 23 Oct 2026; not known in print.", 'partial': False},
            transcription={'by': 'llm from images', 'source': 'Claude Opus 5.5, 23 Oct 2026: clear text and decipherment sheet transcribed from the DECODE images (texts/R9956_reading.md); the cipher signs not transcribed', 'image_quality': 'good', 'notes': 'Archive order: P3 = f. 205r, P2 = f. 205v, P1 = address, P4/P8 = doc. 206 (decipherment); P5-P7 blank.'})
    add_step(T, {'date': '2026-10-23', 'kind': 'access', 'what': "Re-read (REREAD_BRIEF, b20): every file on DECODE R9955 (6 images) and R9956 (8 images) fetched with the shared cookie into the session scratchpad (b20_fetch.py); no DOC_* or other attachments. R9955 P3 is doc. 196, the contemporary decipherment of the letter's three cipher passages; R9956 P4/P8 are doc. 206, the contemporary decipherment of its cipher passage. Never opened before (closed 21 Sept from Tomokiyo).", 'result': 'worked'})
    add_step(T, {'date': '2026-10-23', 'kind': 'transcription', 'what': "Clear text of both letters and both decipherment sheets transcribed from native-resolution strips (b20_crop.py); doubtful places zoomed. R9956's address reads 'Al muy noble señor mi sobrino Juan Vazquez, secretario de Su Mag.t', confirming Tomokiyo's guess at the recipient; signature Cobos.", 'result': 'worked'})
    add_step(T, {'date': '2026-10-23', 'kind': 'control', 'technique': ['plaintext matching'], 'what': "Figures spot-checked against the general cipher AGS Estado leg. 1.1.1 doc. 112 printed (as images) by Luo (2021) p. 601: R9955 'las necesidades' (la-s-ne-ce-si-da-de-s), R9956 'despachandose este correo de mercaderes ... sazon'. Agree; not decoded sign by sign. R9956's sheet ends 'a x[?] de hebrero' where the letter's clear date is 'a xj de enero de 1531'; the reading follows the letter.", 'result': 'partial'})
    add_step(T, {'date': '2026-10-23', 'kind': 'reading', 'technique': ['plaintext matching'], 'what': "Readings written from the clear text and the decipherments (texts/R9955_reading.md, R9956_reading.md; English R9955_en.md, R9956_en.md; log R9955-R9956_reread_log.md); no word supplied. b17_score.py on the bodies (es): R9955 0.744 (29/39), explicit holes 1.00; R9956 0.714 (10/14), explicit holes 1.00; before: no text. Both set read, grade A.", 'result': 'worked'})
    set_outcome(T,
        method_basis="Both letters were deciphered at the time on separate sheets (AGS Estado leg. 496 docs. 196 and 206), which are on the DECODE images and were transcribed here on 23 Oct 2026 with the clear text; the figures were spot-checked against the general cipher doc. 112 (Luo 2021 p. 601). Tomokiyo identified both; R9955 is also printed in Luo (2021) pp. 285-287.",
        notes="DECODE metadata corrected (R9955 direction and date; R9956 sender Cobos, recipient his nephew Juan Vázquez, from the address). Catalogue entry 200 removed; no write-up. 22 Oct 2026, reading audit: neither letter's text was in the repository. 23 Oct 2026 (b20): both read from their contemporary decipherment sheets on the DECODE images, with the clear text (texts/).",
        fraction_read=1.0, fraction_read_method='measured',
        fraction_read_source="23 Oct 2026, re-read (b20): both documents of outcome.texts read (2 of 2) from their contemporary decipherments; the unread words inside them (R9956: four [?] words and the line 'De hebrero [...]') are named in gaps.",
        gaps=[
            {'item': "R9956: four doubtful words of the decipherment ('me a[b?] / sazon' read [?avise], 'se ha ropto' read [?scripto], [?gracias], [?Yo]) and the clear line after the date, 'De hebrero [...]'",
             'blocker': 'illegible', 'detail': "cramped abbreviations in the decipherer's hand and the writer's postscript line; the cipher signs under [?avise] (20 n ρ) are not settled by a glance at the printed key"},
            {'item': "R9955, R9956: the cipher not decoded sign by sign against doc. 112 (spot checks only)",
             'blocker': 'not-attempted', 'detail': "not needed for the reading (contemporary decipherments); the key is printed as images in Luo (2021) p. 601"},
        ])



# ---------------------------------------------------------------- kaa4591b
def kaa4591b():
    T = 'kaa4591b'
    mark_read(T, 'R9417', {
        'transcription': ['sysB/R9417_signs.txt', 'sysB/R9417_p1.tsv', 'sysB/R9417_p2.tsv', 'sysB/R9417_signs_b20.tsv', 'sysB/R9417_corrections.tsv'],
        'decryption': ['sysB/decoded.txt', 'sysB/R9417_reading.md'],
        'reading': 'sysB/R9417_reading.md', 'translation': 'sysB/R9417_en.md', 'language': 'la',
        'summary': "Łaski to the dukes' secretary Waisenfelder, Kraków 16 June [1530]: concord best made through the imperial princes; Nicolaus Minkuics sent to the King of France and to meet the dukes' envoys at Coburg on 4 July (the roads were beset); the Sultan, persuaded to a year's truce, will receive whom King John names and will come next summer by land and sea unless there is concord; the King of Poland's daughter: the match starts coldly while someone presses through Sigismund Herberstein for Frederick the Count Palatine; the dukes should send to Charles V to hold back his brother from attacking King John. Signed 'Lask', in his own hand."},
        'B', "Read 23 Oct 2026 (b20): P2 ll. 15-29 and P1 read sign by sign at the image; the transcription had stopped at l. 21 and coded the two circle and two cross shapes the other way round from the glossed lines (gloss: dotted circle a, plain circle m, plain x r, starred x e, the R9403 exchange); ll. 1-14 follow the decode and the gloss. Every word carried by its signs or the gloss; 16 doubtful words [?], one owl word sign and one word unread. b17_score.py la: 0.250 (7/28) on the full list (it lacks carissime, arripere, nominabit, -cia spellings, names), explicit holes 0.893 (25/28).")
    mark_read(T, 'R9323', {
        'transcription': ['sysB/R9323_signs.txt', 'sysB/R9323_p1.tsv', 'sysB/R9323_corrections.tsv'],
        'decryption': ['sysB/R9323_decoded.txt', 'sysB/R9323_reading.md'],
        'reading': 'sysB/R9323_reading.md', 'translation': 'sysB/R9323_en.md', 'language': 'la',
        'summary': "Latin note from Łaski's circle to the Bavarian secretary: [FLW] loves the Duke of Bavaria; Łaski wants concord between King John and Ferdinand, for without it Bohemia will perish and the Turks will consume it and Austria; the other princes' lands have nothing to fear by his pact with the Turk unless the Imperial estates aid Ferdinand against [FLW]; the Turks are not to be despised; he would have sent horses to the Sultan; commends himself to the dukes."},
        'B', "Read 23 Oct 2026 (b20): re-read word by word at the image; l. 3 begins with the Ferdinand word sign (not an unknown XC), Ƶ = q, the I-sign = b, the dagger = n; 11 transcription corrections (R9323_corrections.tsv). Two faint words of l. 10 unread; three doubtful. b17_score.py la: 0.111 (1/9) on the full list, explicit holes 0.889 (8/9).")
    set_doc(T, 'R9323', read='read')
    add_step(T, {'date': '2026-10-23', 'kind': 'access', 'what': "Re-read (REREAD_BRIEF, b20): every file on DECODE R9417 (2 images) and R9323 (1 image) fetched with the shared cookie (b20_fetch.py; scratchpad only). No attachments or DOC_* texts; the only contemporary text is the faint interlinear gloss (R9417 P2 ll. 1-14 and P1 ll. 5-7, R9323 ll. 1-3 and 11).", 'result': 'worked'})
    add_step(T, {'date': '2026-10-23', 'kind': 'transcription', 'technique': ['plaintext matching'], 'what': "R9417 P2 image has 29 cipher lines; the transcription held 21. Lines 15-29 and P1 read sign by sign on native crops (sysB/R9417_signs_b20.tsv). The decode's 'm for a, e for r' slips were coding slips: on ll. 15-21 the dotted/plain circles and plain/starred crosses had been coded the other way round from the glossed lines 12-14, where the gloss fixes dotted circle a, plain circle m, plain x r, starred x e (the R9403 exchange). R9323 re-read word by word (11 corrections, sysB/R9323_corrections.tsv): l. 3 begins with the Ferdinand word sign; Ƶ = q, I-sign = b, dagger = n.", 'result': 'worked'})
    add_step(T, {'date': '2026-10-23', 'kind': 'reading', 'technique': ['plaintext matching', 'contextual inference'], 'what': "Readings and translations written (sysB/R9417_reading.md, R9323_reading.md, _en.md; log sysB/R9417-R9323_reread_log.md); every word carried by its signs or the gloss, doubtful words [?]. b17_score.py la: R9417 0.250 full list / 0.893 explicit holes, R9323 0.111 / 0.889 (the checker's Latin list lacks common words, -cia spellings and names). Both set read, grade B. New content: Minkuics to meet the dukes' envoys at Coburg on 4 July; the Polish king's daughter sought through Sigismund Herberstein for Frederick the Count Palatine; the dukes to ask Charles V to hold back Ferdinand.", 'result': 'worked'})
    set_outcome(T,
        fraction_read=1.0, fraction_read_method='measured',
        fraction_read_source="23 Oct 2026, re-read (b20): all four letters of outcome.texts read as sentences: R9322 445 + R9403 416 (measure_sysb.py) + R9417 333 + R9323 113 (words of the reading bodies, b17_score.py) = 1,307 of 1,307 words in letters that read. Holes inside them are named in gaps (R9417 one word sign and one word, R9323 two words). Earlier figures: 0.693 (22 Oct audit, R9417 and R9323 not read), 0.953 (machine decodes, withdrawn).",
        notes="22 Oct 2026 audit: R9322 and R9403 read; R9417 and R9323 decoded, not read. 23 Oct 2026 (b20): R9417 read in full at the image (8 lines never transcribed; circle and cross codes corrected from the glosses) and R9323 re-read word by word; all four letters read. FLW (probably the king's title) and R9417's owl word sign are not settled.",
        gaps=[
            {'item': "FLW word sign (R9322, R9323)", 'blocker': 'no-key-material', 'detail': "probably King John's title; three occurrences, no gloss over them and no key sheet"},
            {'item': "R9417: the owl-shaped word sign (P2 l. 27), 'queiter' (l. 16), [?anestris], [?sies] and the 6-shaped sign read k (Cubergk, Minkuics)", 'blocker': 'no-key-material', 'detail': "one occurrence each; the gloss stops at l. 14"},
            {'item': "R9323: two words before 'ducere noluit' (l. 10)", 'blocker': 'illegible', 'detail': "faint signs on the image"},
            {'item': "R9403 P3 l.11-12 two words and P1 l.4 insertion", 'blocker': 'illegible'},
            {'item': "R9322 16 words with doubtful signs", 'blocker': 'illegible', 'detail': "'?' signs in the transcription"},
        ])


# ---------------------------------------------------------------- kaa4591
def kaa4591():
    T = 'kaa4591'
    set_note(T, 'R9409', "Re-read 23 Oct 2026 (b20), still decoded, not read: no gloss, decipherment or edition (DECODE files all opened); partial reading r9409/R9409_reading.md (the 5 Oct hand reading in the brief's notation, words unchanged). b17_score.py de: 0.323 full list, 0.658 explicit holes; but P1 and P3 are broken syntax with [...] runs, and 'da' stands 53 times where no word forms (the lone c+ sign, probably a title sign 'Mt.', not adopted: gender varies, no key sheet; flagged for review). Blocker: no-key-material. Log r9409/R9409-R9427_reread_log.md.",
             reading='r9409/R9409_reading.md')
    set_note(T, 'R9427', "Re-read 23 Oct 2026 (b20), still decoded, not read: the faint gloss re-checked on contrast-enhanced crops gives only the salutation ('genedig[isten] [herren]'); partial reading r9427/R9427_reading.md. b17_score.py de: 0.196 full list, 0.451 explicit holes; P1.01-P1.21 (the Württemberg affair) is [...] in nearly every line. Blockers: illegible (gloss) and no-key-material (unsettled signs). Log r9409/R9409-R9427_reread_log.md.",
             reading='r9427/R9427_reading.md')
    add_step(T, {'date': '2026-10-23', 'kind': 'access', 'what': "Re-read (REREAD_BRIEF, b20): every file on DECODE R9409 (8 images) and R9427 (2 images) fetched with the shared cookie (b20_fetch.py; scratchpad only). No attachments or DOC_* texts; the only outside text is R9427's faint interlinear gloss (P1 ll. 1-5, 7-10).", 'result': 'partial'})
    add_step(T, {'date': '2026-10-23', 'kind': 'verification', 'technique': ['plaintext matching'], 'what': "R9427 gloss re-checked on contrast-enhanced native crops: l. 1 gives '... sten her...' after 'genedig' (read genedig[?isten] [?herren]); ll. 2-4, 7-10 show nothing beyond gloss.txt.", 'result': 'failed'})
    add_step(T, {'date': '2026-10-23', 'kind': 'reading', 'technique': ['language-model scoring', 'contextual inference'], 'what': "Partial readings in the brief's notation (r9409/R9409_reading.md, r9427/R9427_reading.md; b20_kaa_md.py, words unchanged). b17_score.py de: R9409 0.323 full list / 0.658 explicit holes (0.634 with 'der/die da' counted as holes); R9427 0.196 / 0.451. Reader's judgement: R9409 P1 and P3 do not build sentences, R9427 P1 does not; both stay decoded, not read. Hypothesis, not adopted (sense only, flagged for review): the lone c+ sign read 'da' after ir/irer/der/die (53 places in R9409) is a title sign, probably 'Mt.'.", 'result': 'failed'})
    p = load(T)
    gaps = [g for g in p['outcome']['gaps'] if not g['item'].startswith('R9409 and R9427 decoded, not read')]
    gaps = [dict(g) for g in gaps]
    for g in gaps:
        if g['item'].startswith('R9409') or g['item'].startswith('R9427'):
            g['blocker'] = 'no-key-material'
            g['detail'] = (g.get('detail', '') + ' Re-read 23 Oct 2026 (b20): still decoded, not read; no key sheet or gloss settles these signs.').strip()
    gaps.insert(0, {'item': "R9409 and R9427 decoded, not read (P1/P3 of R9409; P1.01-P1.21 of R9427; the lone c+ 'da' sign, 53 places in R9409)", 'blocker': 'no-key-material', 'detail': "re-read 23 Oct 2026 (b20): all DECODE files opened, no decipherment or edition; System A' has no key sheet and the per-letter keys do not settle the signs; R9427's gloss over P1 ll. 1-10 is illegible beyond the salutation"})
    p['outcome']['gaps'] = gaps
    save(T, p); print('gaps', T)


if __name__ == '__main__':
    globals()[sys.argv[1]]()
