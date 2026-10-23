"""Re-read brief (REREAD_BRIEF.md), batch b19: dedem1788, deswart1782, foix1563.

Targeted profile edits with the splice saver of relabel_r0.py; one save per change.

    python research/reading_audit/reread_b19.py <target> <step>
Helpers: b19_fetch.py (DECODE record files), b19_na_fetch.py (Nationaal Archief scans), b19_crop.py, b19_keylook.py
(dedem: codebook look-up montages on NA 1.02.20 inv. 785), b19_dedem_decode.py, b19_wordcheck.py (every unbracketed
reading word carried by the decode or the clear text), b17_score.py (clean-sentence share of a reading body).
"""
import sys
import pathlib

sys.path.insert(0, str(pathlib.Path(__file__).parent))
from relabel_r0 import load, save  # noqa: E402

REV = dict(by='Claude Opus 5.5', date='2026-10-22')
D = '2026-10-23'


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


def set_note(t, doc, note, fields=None):
    p = load(t)
    es = [x for x in p['outcome']['texts'] if x.get('doc') == doc]
    for e in es:
        e['note'] = note
        if fields: e.update(fields)
        save(t, p); p = load(t)
    print('note', t, doc, len(es))


def add_step(t, step):
    p = load(t)
    p['solution'].append(step)
    save(t, p); print('step', t)


def set_outcome(t, **kw):
    for k, v in kw.items():
        p = load(t)
        if isinstance(v, list) and len(v) > 1:
            p['outcome'][k] = v[:1]; save(t, p)
            for x in v[1:]:
                p = load(t); p['outcome'][k].append(x); save(t, p)
            continue
        p['outcome'][k] = v
        save(t, p)
    print('outcome', t, list(kw))


# ---------------------------------------------------------------- dedem1788
DE_FIELDS = {
    'DECODE R2122': {'decryption': ['tx/R2122_decode.txt', 'tx/R2122_reading.md'], 'reading': 'tx/R2122_reading.md',
                     'translation': 'tx/R2122_en.md', 'language': 'nl'},
    'DECODE R2131': {'decryption': ['tx/R2131_decode.txt', 'tx/R2131_reading.md'], 'reading': 'tx/R2131_reading.md',
                     'translation': 'tx/R2131_en.md', 'language': 'nl'},
}
DE_NOTE = {
    'DECODE R2122': "Read 23 Oct 2026 (b19) with the codebook itself, 'Kroll. Un Chiffre', Nationaal Archief 1.02.20 (legatie Turkije) inv. 785: every group looked up on the scans (key/kroll785_values.tsv), the cipher re-read on the DECODE images, clear salutation and close transcribed; the whole letter reads (Van Dedem's demarches after the resolution of 2 October, the Porte's wish for a loan negotiation in the Republic passed to the Prussian envoy, his distrust of the English ambassador, a Swedish subsidy). Holes: 1230, 1330 (twice), 80, 760 (twice), 4414 (no such code), 3928, 1605, 1463 give no sense where they stand. Clean-sentence share of the body 0.222 on the checker's modern Dutch list, 0.933 counting explicit holes only (period spelling, as for battier1686).",
    'DECODE R2131': "Read 23 Oct 2026 (b19) with the codebook 'Kroll. Un Chiffre' (NA 1.02.20 inv. 785): the Ottoman Porte bound itself to the Prussian envoy the day before yesterday to stay neutral in the war with the French and make no further alliance with that nation. Transcription corrected on the DECODE image (2261 -> 2262, 311 -> 317?); open: 319 (Son Altesse where 'alle' is needed), 591 ('g' after 'verbond'). Clean-sentence share 0.200 on the checker's modern Dutch list, 0.800 counting explicit holes only.",
}
DE_STEPS = [
    {'date': D, 'kind': 'access', 'what': "Re-read (REREAD_BRIEF, b19): DECODE R2122 and R2131 re-fetched with the project cookie (b19_fetch.py): images only (2 and 4), no attachment, transcription or comment; every image opened, no contemporary decipherment. Sibling records with solutions (R1948-R1952, R2132-R2134, R2141) fetched and listed.", 'result': 'partial'},
    {'date': D, 'kind': 'key from source', 'technique': ['key matching'], 'what': "The legation inventory (NA 1.02.20, targets/roell1809/turk_inv.txt) lists under Kroll (1784-85) inv. 785 'Sleutel geheimschrift'. Its 6 scans on the Nationaal Archief site (b19_na_fetch.py) are a bound codebook headed 'Kroll. Un Chiffre': 500-group pages of five columns of 100, words alphabetical across the rows, letters and syllables in a table at the foot of each column, names and titles in 3001-3500, a Nota on noun and preterite forms. It is this code: the slot model's A-grade values recur (2 aan, 17 als, 86 de, 238 belang, 541 en, 1124 het, 1764 oorlog, 3273 Porta). inv. 686 (De Weiler, 1775) holds the Berigt on begin/einde des briefs markers and nulls.", 'result': 'worked'},
    {'date': D, 'kind': 'transcription', 'what': "All 238 distinct groups of R2122 and R2131 looked up on the codebook scans (b19_keylook.py; key/kroll785_values.tsv); 237 found, 4414 does not exist. The cipher re-read on the DECODE images: R2131 2261 -> 2262 (sig), 311 -> 317? (als dat); R2122 clear salutation and close added (tx/*_corrections.tsv). The slot model's values differ from the book at 16, 194, 526, 675, 1455 (instructie, not interest), 1069, 3610 (de Envoyé van Pruissen).", 'result': 'worked'},
    {'date': D, 'kind': 'reading', 'technique': ['key matching', 'contextual inference'], 'what': "R2122 and R2131 decoded with the codebook (b19_dedem_decode.py) and read sentence by sentence, joining words the code spells in pieces (el+der+s, du+r+ven, ver+ne+der+ing); every unbracketed word checked as carried (b19_wordcheck.py). Readings tx/R2122_reading.md and tx/R2131_reading.md with English. Clean-sentence share: checker's modern Dutch list 0.222 and 0.200; explicit holes only 0.933 and 0.800. Open: 1230, 1330, 80, 760 (twice, after an infinitive: probably the Nota's example number copied for a 'g' character, not adopted), 4414, 3928, 1605, 1463, 319, 591.", 'result': 'worked'},
]


def dedem(step):
    t = 'dedem1788'
    if step == 'texts':
        for d in ('DECODE R2122', 'DECODE R2131'):
            mark_read(t, d, DE_FIELDS[d], 'B', DE_NOTE[d])
    elif step == 'steps':
        for s in DE_STEPS:
            add_step(t, s)
    elif step == 'outcome':
        set_outcome(t,
                    key='recovered', key_file='key/kroll785_values.tsv', **{'class': 'read'},
                    method_basis="R2120 is read from its contemporary clear decipherment, filed as R2121 pp. 2-4; R2122 and R2131 are read with the codebook itself, 'Kroll. Un Chiffre', found in the legation archive (NA 1.02.20 inv. 785), every group looked up on its scans.",
                    gaps=[{'item': 'R2122 and R2131: 14 groups whose codebook value gives no sense where they stand (1230, 1330 x2, 80, 760 x2, 3928, 1605, 1463, 2622 in R2122; 319, 591 in R2131) and 4414 (no such code)', 'blocker': 'too-short', 'detail': 'each occurs once or twice, too few occurrences to establish a different value; probably clerk slips (319 for 314 alle; 760 copied from the Nota example); named in the readings'},
                          {'item': 'R2120: English translation of the contemporary decipherment not yet written', 'blocker': 'not-attempted'}],
                    parts=[{'label': 'R2120, read from its contemporary decipherment (R2121)', 'records': 'R2120, R2121', 'method': 'read from existing decipherment', 'extent': 'complete'},
                           {'label': "R2122 and R2131, read with Kroll's codebook (NA 1.02.20 inv. 785)", 'records': 'R2122, R2131', 'method': 'read after matching with key from external sources', 'extent': 'complete', 'basis': 'the codebook was filed in the legation archive under Kroll, not tied to these letters before'}])
        p = load(t)
        if 'key from archive' not in p['conditions']['inputs']:
            p['conditions']['inputs'].append('key from archive'); save(t, p)
        p = load(t); p['conditions']['last_date'] = D; save(t, p)


# ---------------------------------------------------------------- deswart1782
DS_FIELDS = {
    'R1036': {'decryption': ['R1036_decode.txt', 'R1036_machine_decipherment.txt'], 'reading': 'R1036_reading.md',
              'translation': 'R1036_en.md', 'language': 'nl'},
    'R1040': {'decryption': ['R1040_part2_decode.txt', 'R1040_second_key_machine_decipherment.txt'], 'reading': 'R1040_part2_reading.md',
              'translation': 'R1040_part2_en.md', 'language': 'nl',
              'summary': "De Swart's despatch of 29 November 1787, coded with two codebooks. The 1765-key segment (image 5459 from group 180 to image 5473, 5,625 groups) reports evidence of an Austrian-French alliance, the attention of the Prussian and British representatives at St Petersburg, Kaunitz, the Bavarian exchange and the Duke of Zweibruecken, the German League, the fleet and the Turkish war. The first 1,928 groups and image 5474 (331 groups, 2,259 in all) use a missing Rechteren-family code and are not deciphered."},
}
DS_NOTE = {
    'R1036': "Read 23 Oct 2026 (b19): the 30 Sept 2026 key and transcription corrections applied in decode_1765.py (the leading dash, 47^_ k, 54^\" alhoewel, 191 ens ...), two high scan readings (52^o sedert eenigen, 71^\" appuyeeren) and the b19 context values (617^\" courier, 341^_ mari, 343^_ me, 316^\" belang ...) adopted; DECODE's key-transcription letter confusions normalised where constant (R1038_key_misreadings.tsv); the whole despatch normalised group by group with clear opening and close (R1036_reading.md, every unbracketed word carried, b19_wordcheck.py). Clean-sentence share of the body 0.09 on the checker's modern Dutch list, 0.769 counting explicit holes only (period spelling). Open: 38 groups without a value and the line cut off at the top of image 5417.",
    'R1040': "Second part read 23 Oct 2026 (b19): context pass on its unread groups (28 values in R1040_B19, each fitting every occurrence here and in R1036), segment corrected to image 5459 group 180 - image 5473 (5,625 groups; 5474 is back in the missing code), normalised reading R1040_part2_reading.md (every unbracketed word carried). Clean-sentence share 0.038 on the checker's modern Dutch list, 0.666 counting explicit holes only; the French quotations read only in part. The first part (2,259 groups) is in a missing code and is not read.",
}
DS_STEPS = [
    {'date': D, 'kind': 'access', 'what': "Re-read (REREAD_BRIEF, b19): DECODE R1036 and R1040 re-fetched: one DOC attachment each (DECODE's ciphertext transcriptions, already in the folder); every image opened (R1036 9, R1040 23, main checkout): no interlinear, margin or slip decipherment, no clear copy. Nationaal Archief: 1.01.02 inv. 7408, 3.01.25 inv. 610, 1.02.13 inv. 114 and 158 have no scans online. No edition known.", 'result': 'failed'},
    {'date': D, 'kind': 'transcription', 'what': "The 30 Sept 2026 corrections applied in decode_1765.py (R1036_SEPT30): the '^_' DECODE puts after a comma dropped as a mark (a dash after the previous group), key entries re-read on the scans (54^\" alhoewel, 314^\" behalven, 941^_ observeeren, 47^_ k, 327 el, 92^_ houden, 121 die, 862^^ het, 448^\" con, 223^o veele, 743 dat, 853^_ niet, 559 gehad, 80 eeren, 135 barred-circle zoek, 299 favoriet, 231^o verder) and the interlinear group 191 (ens, not 19) added on image 5416; 52^o sedert eenigen and 71^\" appuyeeren adopted from the 'high' scan readings (R1038_scan_readings.tsv).", 'result': 'worked'},
    {'date': D, 'kind': 'hypothesis', 'technique': ['contextual inference', 'key-structure hypothesis'], 'what': "Context pass on R1040 part 2 (b19_kwic.py): 28 values adopted only where they fit every occurrence in R1040 part 2 and R1036 (R1040_B19: 34^_ in, 21^^ of, 78 eenen (W-eenen), 15^_ het hof van, 81^_ honderd, 213^o twee, 922 Hertog, 343^_ me, 341^_ mari, 495^_ mede, 800^_ omstandigheden, 617^\" courier, 178 eerst ...; DECODE key misreadings 161 t, 801^\" deel, 777^_ niet, 227^\" atie, 689 formeeren, 316^\" belang); rejected after test: 120, 969^\", 940, 851, 690^_, 226, 7^_, 79^o, 761^^, 40^_, 265^_, 5^^, 831^_ (R1040_part2_reread_log.md). Image 5474 found to be in the first, missing code (its marks ^' and ^__, 69% coverage, nonsense after the last words of 5473): the 1765 segment is 5,625 groups.", 'result': 'worked'},
    {'date': D, 'kind': 'reading', 'technique': ['key matching', 'contextual inference'], 'what': "R1036 and R1040 part 2 normalised group by group into readings with the figures' spelling and DECODE's constant key-transcription letter confusions corrected (R1038_key_misreadings.tsv: hot hof, chi che, cerd eerd, ock ook, hetten hebben ...); every unbracketed word checked as carried (b19_wordcheck.py). Clean-sentence share on the bodies: checker's modern Dutch list 0.09 and 0.038; explicit holes only 0.769 and 0.666. Both set read (grade B); the French quotations of R1040 and the first 2,259 groups stay open.", 'result': 'worked'},
]


def deswart(step):
    t = 'deswart1782'
    if step == 'texts':
        for d in ('R1036', 'R1040'):
            mark_read(t, d, DS_FIELDS[d], 'B', DS_NOTE[d])
    elif step == 'steps':
        for s_ in DS_STEPS:
            add_step(t, s_)
    elif step == 'outcome':
        set_outcome(t, **{'class': 'read in part'}, method='read after matching with key from external sources',
                    method_basis="DECODE said the codebook could not be identified; the 1765 Croiset codebook of the Russia legation (DECODE R1038, a separate key record) was found here to fit R1036 and the second segment of R1040, and with values read from its scans and fitted on every occurrence both read as continuous Dutch (23 Oct 2026). The first 2,259 groups of R1040 are in a missing code.",
                    notes="Two keys in R1040 (one-key review, 14 Oct 2026): parts per key. R1036 and the 1765-key segment of R1040 (5,625 groups, image 5459 group 180 to 5473) read 23 Oct 2026 after the 30 Sept corrections, a context pass and a normalised reading (b19); the first 1,928 groups and image 5474 (2,259 groups) in a missing Rechteren-family code, not solved.",
                    parts=[{'label': 'Croiset 1765 Russia-legation codebook (DECODE R1038)', 'records': 'R1036 (whole, 1,719 groups); R1040 from group 180 of image 5459 to image 5473 (5,625 groups)', 'method': 'read after matching with key from external sources', 'extent': 'complete', 'basis': '23 Oct 2026 (b19): R1036 1,681/1,719 and R1040 segment 5,386/5,625 groups with a value after the 30 Sept corrections and the b19 context values; both normalised into readings that build sentences (explicit-hole clean-sentence share 0.769 and 0.666); the French quotations of R1040 read only in part'},
                           {'label': 'missing Rechteren-family nomenclator', 'records': 'R1040 images 5453-5458, the first 179 groups of image 5459, and image 5474 (2,259 groups)', 'method': 'not solved', 'extent': 'none', 'basis': 'neither the 1765 key nor the 1803 Croiset relative fits; crib transfers from R2032, R2051, R2052 (1784-86) cover 2-3% and give no prose; the key is probably Nationaal Archief 1.02.13 inv. 158, not online; image 5474 assigned to this code on 23 Oct 2026 (its marks and 69% 1765-key coverage)'}],
                    gaps=[{'item': 'R1040 first part, 2,259 groups (images 5453-5458, 5459 groups 1-179, and 5474)', 'blocker': 'needs-physical-access', 'detail': 'a different, missing Rechteren-family code, probably NA 1.02.13 inv. 158, not scanned online; crib transfers from R2032/R2051/R2052 cover 2-3%'},
                          {'item': 'R1040 second part: about 240 groups without a value, and the French quotations (about 8% of the segment) read only in part', 'blocker': 'illegible', 'detail': 'the R1038 cells for these codes are lost in the binding shadow or too faint on the photographs; codes seen once or twice cannot be fixed from context; the 1765 key covers French poorly'},
                          {'item': 'R1036: 38 groups without a value (rare codes) and the line cut off at the top of image 5417', 'blocker': 'illegible', 'detail': 'R1038 cells lost in the binding shadow or too faint; the first line of image 5417 is cut off in the photograph'}])
        p = load(t); p['conditions']['last_date'] = D; save(t, p)
        p = load(t)
        if 'claude-opus-5-5' not in p['conditions']['models']:
            p['conditions']['models'].append('claude-opus-5-5'); save(t, p)


# ---------------------------------------------------------------- foix1563
FX_ENTRY = {'doc': 'R9241', 'label': "R9241: combined re-reading, Beck's key with the 1565 word signs (b19, 23 Oct 2026)",
            'note': "Re-read 23 Oct 2026 (b19): Beck's transcription and key v13 with the word signs of de Foix's 1565 cipher for the numbers he left open (10 dict, 26 bien, 34 tant, 40 faict, 70 toute, 82 ceulx, 37 me/car) and f = u twice; every trouble spot checked on the DECODE photographs (no label changed). Passages (2)-(4) build sentences with scattered holes; passage (1) breaks twice mid-sentence (A2, A14-A16), and B3, D7 and the closing name stay unread. Clean-sentence share of the body 0.361 on _check_reading.py (fr), 0.609 counting explicit holes only: below the bar, so decoded, not read, with the partial reading kept (texts/R9241_reading.md). Blocker: no-key-material (no 1563 decipherment of a de Foix letter; the open signs have no value in the 1565 chart).",
            'transcription': 'texts/beck_transcription.txt', 'decryption': ['texts/R9241_decode.txt', 'texts/R9241_reading.md'],
            'reading': 'texts/R9241_reading.md', 'translation': 'texts/R9241_en.md', 'state': 'decoded, not read', 'language': 'fr'}
FX_STEPS = [
    {'date': D, 'kind': 'access', 'what': "Re-read (REREAD_BRIEF, b19): DECODE R9241 re-fetched: two images, no attachment, transcription or comment; both opened, no decipherment (Forbes copied only the cipher passages); neighbouring copies on ff. 148-149 are other letters (Coligny, Throckmorton). Print searched before (Forbes, CSP Foreign vi, La Ferriere).", 'result': 'failed'},
    {'date': D, 'kind': 'sibling key', 'technique': ['key matching'], 'what': "Beck's key v13 combined with the 1565 cipher's word signs for the numbers he left open (10 dict, 26 bien, 34 tant, 40 faict, 70 toute, 82 ceulx, 37 me/car; each fits every occurrence) and the 1565 polyvalence f = u at two places (aussi, roiaulmes); b19_foix_decode.py, texts/R9241_decode.txt.", 'result': 'partial'},
    {'date': D, 'kind': 'verification', 'technique': ['manual reconstruction'], 'what': "Every trouble spot checked on the DECODE photographs with Beck's line coordinates (A2, A4, A8, A12, A14-A16, B1, B3, C1-C2, D0, D6-D8): the signs are as Beck transcribed (his 20 in A8 is written 'zo'); no label changed. New: 'et ioue durant noz trouble le personnaige que vous scauez assez', 'aiant faict les [beaulx] [auancemens] de la [guere]', 'langaige accompaignee'. A2, A14-A16, B3, D7 and the closing name build no words under Beck's, the 1565 or Nur's fitted values.", 'result': 'partial'},
    {'date': D, 'kind': 'reading', 'technique': ['contextual inference', 'language-model scoring'], 'what': "Reading texts/R9241_reading.md with English (every unbracketed word carried, b19_wordcheck.py). Clean-sentence share: _check_reading.py 0.361; explicit holes only 0.609. Below the bar (French documents at 0.47-0.56 kept unread): R9241 stays decoded, not read, with this partial reading.", 'result': 'failed'},
]


def foix(step):
    t = 'foix1563'
    if step == 'texts':
        p = load(t)
        if not any(x.get('label', '').startswith('R9241: combined re-reading') for x in p['outcome']['texts']):
            p['outcome']['texts'].append(FX_ENTRY); save(t, p)
        p = load(t)
        for e in p['outcome']['texts']:
            if e.get('label', '').startswith("R9241, Catherine de' Medici to Paul de Foix, 15 Jan 1563: Lawrence Beck"):
                e['note'] = "Beck's proposed reading: passages B and D give connected clauses, but A and C have gaps or unresolved letter strings in most sentences (reading audit, 22 Oct 2026). Used 23 Oct 2026 (b19) as the base of the combined re-reading (third entry), which also stays below the bar."
        save(t, p)
        p = load(t)
        for e in p['outcome']['texts']:
            if e.get('label', '').startswith("R9241: Feyseel Nur"):
                e['note'] = "Nur's graded rendering with the 1565 key: dictionary fragments between ellipses, with conflicting values (r m/d, z p/i, Yb l/u) unresolved; no passage builds sentences (reading audit, 22 Oct 2026). Its frozen 1565 word signs (10, 26, 34, 40, 70, 82) are used in the b19 combined re-reading (third entry)."
        save(t, p)
    elif step == 'steps':
        for s_ in FX_STEPS:
            add_step(t, s_)
    elif step == 'outcome':
        set_outcome(t, gaps=[{'item': 'R9241 passages (1)-(4): the combined re-reading builds sentences in (2)-(4) but breaks twice in (1) (A2 "prolizgnaulx", A14-A16) and leaves B3, D7 and the closing name unread; clean-sentence share 0.361 (explicit holes 0.609)', 'blocker': 'no-key-material', 'detail': 'the open signs have no value in the 1565 chart (Tomokiyo, BnF fr. 15971) and no decipherment of a de Foix letter of 1563 is known; de Foix changed his key in early 1564; signs checked on the photographs, no label in doubt'}])
        p = load(t); p['conditions']['last_date'] = D; save(t, p)


if __name__ == '__main__':
    {'dedem1788': dedem, 'deswart1782': deswart, 'foix1563': foix}[sys.argv[1]](sys.argv[2])
