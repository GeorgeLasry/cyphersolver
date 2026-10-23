"""Re-read brief (REREAD_BRIEF.md), batch b09: nuncio1566 (R85-R90).

Targeted profile edits with the splice saver of relabel_r0.py (only changed spans are rewritten), one change per save.
fraction_read is set separately with set_fraction.py.

    python research/reading_audit/reread_b09.py texts|outcome|steps
"""
import sys
import pathlib

sys.path.insert(0, str(pathlib.Path(__file__).parent))
from relabel_r0 import load, save  # noqa: E402

DATE = '2026-10-22'
BY = 'Claude Opus 5.5'
F = 'nuncio1566'

READ = {
    'R85': ('B', 'No decipherment or print found; read word by word on the figures with the key as extended by the R87 '
                 'decipherment and the R88-R90 copies, eight transcription labels corrected on the image '
                 '(texts/R85_transcription_corrected.txt); 169 of 190 words carried (b09_align.py), the rest dotted '
                 'zeros the transcription lost or bracketed. Holes: codes 3050, 3020 (this use), one blotted group, one '
                 'ticked run.',
            'Rome, 8 Jan 1567: the Pope wants to know whether the King\'s journey will go ahead, because he would then '
            'meet him wherever suits him; the Queen Mother and the King of France wish Philip to invite them to a '
            'parley; the Pope distrusts "words of women" but urges the King to admit, even seek, the meeting, leaving '
            'it to his prudence, and offers to act as common father.'),
    'R86': ('B', 'No decipherment or print found; read word by word on the figures, three labels corrected on the image '
                 '(texts/R86_transcription_corrected.txt; row 1 "di N.S., per dirlo a V.S."); 155 of 164 words carried. '
                 'Open: code 2020, "[?quel] fatto", "[?havere]" (8090), "[?via]".',
            'Rome, 25 July - 2 Aug 1567, Milan jurisdiction case: the Pope means, in confidence, to proceed with '
            'spiritual arms against the authors of the outrage, above all the Senate; the governor is to make them obey '
            'the monitories; the Holy See\'s dignity requires action at least against the Capitano di giustizia, the '
            'fiscal and some senators; the King should deprive his two ministers of office.'),
    'R87': ('A', 'Contemporary decipherment on f. 251r of the same file (texts/R87_decifrato_f251r.txt; its top lines '
                 'lost, it stops at "resistere") transcribed and aligned with the figures: 437 of 448 words carried; '
                 'figures followed where they differ (dal qual, ma perché, esso pretenso arcivescovo, o dependente). '
                 'The last four rows rest on the figures alone.',
            'About 2 Aug 1567: the Pope wants the King to go to Flanders soon, to restore religion there, in France and '
            'Germany; the Queen Mother of France wishes to be invited to a meeting, which the King should grant; the '
            'archbishop-elect of Cologne, unconfirmed and allied with the Duke of Cleves, is to be deprived, and the '
            'King should see that the chapter does not choose a suspect successor.'),
    'R88': ('B', 'No decipherment; read word by word on the figures (326 of 361 words carried), the damaged figures '
                 '(rows 10-17 of each page) read from R89, a second cipher copy of the same text. Covering letter in '
                 'clear, Rome 4 Nov 1567 (ff. 299r-302r). One group (7 3 8) unread.',
            'Rome, 4 Nov 1567, a chapter of a letter from France passed on to the nuncio: the Queen Mother is timid, '
            'trusts the Chancellor, Morvillier, Limoges and l\'Aubespine, and keeps the kingdom divided to rule; not a '
            'Huguenot but a bad Christian; if the King imprisoned the Constable and his son until Condé and the Admiral '
            'laid down arms, the troubles would end.'),
    'R89': ('B', 'No decipherment; read word by word on the figures (336 of 349 words carried) and against R88, the '
                 'other cipher copy, and R90, which continues it; the R87 decipherment fixes the codes (8010 Regina, '
                 '4010 S.M.).',
            'Second copy of the R88 text (the chapter of a letter on the Queen Mother and the French court), ending '
            '"da persona molto bene", continued in R90.'),
    'R90': ('A', 'Read on the figures (45 of 48 words carried); it continues R89 word for word and its second sentence '
                 'is written in clear on f. 302r of the R88 copy of the letter (texts/R90_clear_f302r.txt).',
            'End of the same text: the writer is well informed of the French court and the Queen Mother; the King '
            'should let the Queen know that her counsellors, unfaithful to God, will be little faithful to her.'),
}


def texts():
    p = load(F)
    for t in p['outcome']['texts']:
        rec = t['doc']
        grade, note, summary = READ[rec]
        t['state'] = 'read'
        t.pop('note', None)
        t['reading'] = 'texts/%s_reading.md' % rec
        t['translation'] = 'texts/%s_en.md' % rec
        t['language'] = 'it'
        t['summary'] = summary
        t['reading_review'] = {'grade': grade, 'by': BY, 'date': DATE, 'note': note}
    save(F, p)


def outcome():
    edits = [
        ('class', 'read'),
        ('method', 'read with known key'),
        ('method_basis', 'George Lasry\'s 2020 reconstructed key was attached to every DECODE record R85-R90 before the '
                         'attempt; it is polyphonic (each digit two letters, zero a null). The beam search under it gave '
                         'fragments only. On 22 Oct 2026 the contemporary decipherment of R87 (f. 251r, a DECODE '
                         'cleartext image) was transcribed and aligned with the figures, and the three cipher copies of '
                         'the 4 Nov 1567 letter (R88, R89, R90, with the clear sentence on f. 302r) were read against '
                         'each other; they fixed the code values (8010 Regina [di Francia], 4010 S.M., 1020 essere, 1040 '
                         'lettera, 8030 religione, 8070 ugonotta, 8080 heretici, 8090 havere), with which all six were '
                         'read word by word on the figures, twelve transcription labels corrected on the images.'),
        ('contribution', ['decipherment with ambiguous key', 'transcription', 'key extended or corrected',
                          'sender or date identified', 'catalogue correction']),
        ('verification', ['contemporary decipherment', 'independent clear copy', 'key confirms',
                          'historical consistency']),
        ('notes', 'R85-R90 read word by word on the figures with Lasry\'s key as extended by the R87 decipherment '
                  '(f. 251r) and the three copies R88/R89/R90; holes marked in texts/R8x_reading.md (codes 3050, 3020 '
                  'in R85, 2020 in R86; a few partly carried words). 22 Oct 2026: reading audit decoded, not read; same '
                  'day re-read (batch b09, texts/R85-R90_reread_log.md) and class back to read. Serrano 1914 not '
                  'reached (HathiTrust 403, not on archive.org).'),
        ('parts', [{'label': 'R85-R90 (Lasry\'s key, extended by the R87 decipherment and the R88-R90 copies)',
                    'records': 'DECODE R85-R90', 'method': 'read with known key', 'extent': 'complete',
                    'basis': 'Lasry\'s key (24 Oct 2020) extended on 22 Oct 2026 from the contemporary decipherment of '
                             'R87 (f. 251r) and the three copies of the 4 Nov 1567 cipher; read word by word on the '
                             'figures with the images checked at every break (texts/R85-R90_reread_log.md).'}]),
        ('credits', None),
    ]
    for k, v in edits:
        p = load(F)
        o = p['outcome']
        if k == 'credits':
            o['credits'] = o.get('credits', []) + [
                {'who': 'contemporary', 'role': 'key or decipherment used',
                 'note': 'decifrato of R87 on f. 251r, bound after the cipher in the nunciature file; clear text of the '
                         'R90 sentence in the 4 Nov 1567 letter, f. 302r',
                 'date': '1567', 'source': 'DECODE R87 and R88 cleartext images'}]
        else:
            o[k] = v
        save(F, p)


STEPS = [
    {'date': DATE, 'kind': 'access',
     'what': 'Re-read under REREAD_BRIEF (batch b09): the 10 DECODE cipher images of R85-R90 and their 29 cleartext images '
             '(folios around each cipher) fetched with the DECODE session cookie (research/reading_audit/b09_fetch.py), '
             'kept out of the repository.',
     'result': 'worked'},
    {'date': DATE, 'kind': 'literature search',
     'what': 'Contemporary texts looked for among the cleartext images: R87\'s decipherment is f. 251r (top lines lost, '
             'stops at "resistere"); R90\'s second sentence is in clear on f. 302r (end of the 4 Nov 1567 letter with '
             'R88); R88, R89, R90 are three cipher copies of one text. No decipherment for R85, R86, R88, R89 (clear '
             'covering letters only). Serrano 1914 not reached (HathiTrust 403).',
     'result': 'partial'},
    {'date': DATE, 'kind': 'transcription',
     'what': 'Decipherment f. 251r and clear passage f. 302r transcribed from the images (texts/R87_decifrato_f251r.txt, '
             'R90_clear_f302r.txt). Cipher transcriptions checked on the images at every break: twelve labels corrected '
             '(texts/R85-R90_corrections.tsv; corrected files for R85, R86, R87), e.g. R86 row 1 2020 -> 1010 (N.S.) and '
             '4 0 2 0 9 -> 4 0 1 0 9 0 (a V.S.), R85 row 2 four spurious figures removed.',
     'result': 'worked', 'technique': ['manual reconstruction']},
    {'date': DATE, 'kind': 'verification',
     'what': 'Decipherment of R87 aligned with the figures (reread_b09_align.py, edit-distance DP over the two-letter '
             'figure sets) and R88/R89/R90 aligned with each other and with f. 302r. Code values fixed: 8010 = [la] '
             'Regina [di Francia] (Lasry "Re di Francia"), 4010 = S.M. (Lasry "Sua Santità"), 1020 essere, 1040 lettera, '
             '8030 religione, 8070 ugonotta, 8080 heretici, 8090 havere, 3040 Fiandra; 3 0^. 9 = qua; "colospo" = '
             'colloquio (colo + 509 qui + o); 209 = "chi" as a syllable (richiesti). The decipherer misread in four '
             'places, where the figures are followed.',
     'result': 'worked', 'technique': ['crib testing', 'plaintext matching', 'key-structure hypothesis']},
    {'date': DATE, 'kind': 'reading',
     'what': 'All six read word by word on the figures from a first draft by the extended beam decoder '
             '(reread_b09_decode.py --rows), every word aligned with its figures (research/reading_audit/b09_align.py: '
             'R85 169/190, R86 155/164, R87 437/448, R88 326/361, R89 336/349, R90 45/48 words carried); words not '
             'carried bracketed. English translations written. _check_reading.py on the reading bodies: 1.00, 1.00, '
             '1.00, 0.93, 0.92, 1.00 clean. Failed or open: R85 codes 3050 and 3020 (this use), a blotted group and a '
             'ticked run; R86 code 2020; R88 group 7 3 8. State decoded, not read -> read for all six; class not read -> '
             'read, method not solved -> read with known key.',
     'result': 'worked', 'technique': ['beam/DP decoding', 'language-model scoring', 'contextual inference',
                                        'manual reconstruction']},
]


def steps():
    for s in STEPS:  # one step per save: the splice saver cannot insert two list items at one point
        p = load(F)
        p['solution'].append(s)
        save(F, p)


if __name__ == '__main__':
    {'texts': texts, 'outcome': outcome, 'steps': steps}[sys.argv[1]]()
