"""Re-read brief (REREAD_BRIEF.md), batch aless: alessandrino1568 (R94, R95, R100, R101).

Targeted profile edits with the splice saver of relabel_r0.py (only changed spans are rewritten).

    python research/reading_audit/reread_aless.py

Applied 22 Oct 2026 in stages (the texts, then each outcome field, then the steps): the splice saver refused the
one-line "contribution" list in a single pass, so that line was edited by hand. Re-running main() is not needed.
"""
import sys
import pathlib

sys.path.insert(0, str(pathlib.Path(__file__).parent))
from relabel_r0 import load, save  # noqa: E402

DATE = '2026-10-22'
BY = 'Claude Opus 5.5'
F = 'alessandrino1568'

READ = {
    'R94': ('A', 'Contemporary decipherment on f. 45r of the same file (texts/R94_decifrato_f45r.txt) transcribed and '
                 'aligned with the figures (reread_aless_align.py): 157 of 167 words carried; figures followed where '
                 'they differ (liberamente, N.S., de fatto, non con forze, et viva). Two short gaps the decipherer '
                 'also left open.',
            'Covering letter Rome 7 Nov 1567 ("Con questa un poco di cifra"): the Pope does not mean to revoke the '
            'King\'s ancient privileges but to remove abuses grown through his ministers; the nuncio is to say so '
            'at a suitable moment, once the King is out of the trouble of the funerals; if the King strips the Holy '
            'See of its authority, the Pope will resist with spiritual arms "usque ad effusionem sanguinis".'),
    'R95': ('B', 'Contemporary decipherment on f. 58r (texts/R95_decifrato_f58r.txt), a fast draft, read together '
                 'with the figures; where it is illegible or differs the figures decide. Holes: [08.] (the Crusade?), '
                 'one word after "detto", the person "[3.]" who pressed the request, and one verb.',
            'The French ambassador\'s claim about raising troops in the State of Milan would give the King cause to '
            'withdraw his protection; the crusade alms: the Pope acted so that Christian discipline should not '
            'slacken in Spain, not to deny the indulgence, and will grant a new concession; he grieves more for '
            'the King\'s soul than for any human respect; the nuncio is to speak in this sense.'),
    'R100': ('A', 'Contemporary decipherment written under the cipher on f. 280r (texts/R100_decifrato_f280r.txt), '
                  'aligned with the figures: 73 of 79 words carried; figures followed for "quella", "sia rimessa", '
                  '"sì che".',
             'The King\'s ministers mean to deceive the nuncio over the Inquisition of Catalonia and keep people '
             'from coming to him for absolution; the ambassador presses for the case to be referred to the King; '
             'without waiting for another resolution the nuncio is to execute the brief when the parties ask.'),
    'R101': ('B', 'No decipherment or print found; read word by word on the figures with the key as extended by the '
                  'R94/R95/R100 decipherments (9 = con, dotted 0 = z, 0^.0 = et, 209 = chi, 8090 havere), checked '
                  'with reread_aless_align.py (158 of 168 and 73 of 74 words carried on the two pages). Holes: three '
                  'places under burns or a hole in the paper, codes 9090, 6020, 8020.',
             'The Pope accepted the hackney and the St Peter\'s day dues with the fisc\'s protest, not as census but '
             'as fruits of a fief of the Holy See, and claims devolution under the investitures of Julius II and '
             'Julius III; the King\'s ministers have raised a schism in Naples, imprisoning the bishops\' notaries '
             'and executors (an aged doctor died in prison); God will punish who troubles His Church, and the Pope '
             'will have to take measures if the King does not remedy it.'),
}


def main():
    p = load(F)
    for t in p['outcome']['texts']:
        rec = t['doc']
        if rec not in READ:
            continue
        grade, note, summary = READ[rec]
        t['state'] = 'read'
        t.pop('note', None)
        t['reading'] = 'texts/%s_reading.md' % rec
        t['translation'] = 'texts/%s_en.md' % rec
        t['language'] = 'it'
        t['summary'] = summary
        t['reading_review'] = {'grade': grade, 'by': BY, 'date': DATE, 'note': note}
    o = p['outcome']
    o['class'] = 'read'
    o['contribution'] = ['decipherment with ambiguous key', 'transcription', 'key extended or corrected',
                         'sender or date identified']
    o['fraction_read'] = 1.0
    o['key_file'] = 'texts/key.md'
    o['fraction_read_source'] = ('22 Oct 2026, re-read (batch aless): the four letters labelled decoded, not read '
                                 '(R94, R95, R100, R101; 3,519 of the 10,555 items) now build sentences and are '
                                 'translated (texts/R94-R101_reading.md, _en.md; _check_reading.py on the reading '
                                 'bodies 1.00, 0.94, 1.00, 0.84 clean). Items of letters that read / all = 10,555 / '
                                 '10,555 = 1.0. Open inside the readings: about 15 words (two gaps in R94, four in '
                                 'R95, five in R101) and the codes 9090, 6020, 8020, [08.], [3.].')
    o['method_basis'] = ('George Lasry\'s 2020 reconstructed key was attached to every DECODE record R93-R102 and R115 '
                         'before the attempt; it is polyphonic (each digit two letters, zero a null), so the text was '
                         'chosen by a beam search scored with an Italian language model. On 22 Oct 2026 the '
                         'contemporary decipherments of R94 (f. 45r), R95 (f. 58r) and R100 (under the cipher, f. '
                         '280r), on DECODE as cleartext images, were transcribed and aligned with the figures; they '
                         'extended the key (9 = con, dotted 0 = z, 0^.0 = et, codes 1040 lettere, 3020 quando, 3060 '
                         '-mente, 4020 come, 4040 Milano, 4080 et, 5070/6050 Imbasciatore, 6060 Inquisitione, 8090 '
                         'havere), with which R101 was read on the figures.')
    o['notes'] = ('R93, R96-R99, R102, R115: beam-search readings under Lasry\'s key, sense continuous, single letters '
                  'model choices. R94, R95, R100: read from the contemporary decipherments checked against the '
                  'figures. R101: read on the figures with the extended key. 22 Oct 2026, reading audit: R94, R95, '
                  'R100, R101 decoded, not read; same day re-read (batch aless) and class back to read. Serrano 1914 '
                  'not reached (HathiTrust 403, not on archive.org).')
    o['gaps'] = []
    o['credits'] = o.get('credits', []) + [
        {'who': 'contemporary', 'role': 'key or decipherment used',
         'note': 'decifrati of R94 (f. 45r), R95 (f. 58r) and R100 (f. 280r), bound in the nunciature file',
         'date': '1567-1569', 'source': 'DECODE R94, R95, R100 cleartext images'}]
    save(F, p)
    steps = [
        {'date': DATE, 'kind': 'access',
         'what': 'Re-read under REREAD_BRIEF (batch aless): the DECODE cipher images of R94, R95, R100, R101 and their '
                 '45 cleartext images (folios around each cipher) fetched with the DECODE session cookie, kept out of '
                 'the repository.',
         'result': 'worked'},
        {'date': DATE, 'kind': 'literature search',
         'what': 'Contemporary decipherments found among the "cleartext" images: R94 on f. 45r (with the covering letter '
                 'of Rome 7 Nov 1567, f. 44r, "Con questa un poco di cifra"), R95 on f. 58r, R100 written under the '
                 'cipher on f. 280r; none for R101 (286v-293v are clear letters). Serrano, Correspondencia '
                 'diplomatica ... Pio V (1914): not on archive.org, HathiTrust full text 403 from here.',
         'result': 'partial'},
        {'date': DATE, 'kind': 'transcription',
         'what': 'The three decipherments transcribed from the images (texts/R94_decifrato_f45r.txt, '
                 'R95_decifrato_f58r.txt, R100_decifrato_f280r.txt); R95\'s is a fast draft, read partly with the '
                 'figures. R101 transcription: a stray DECODE comment line that the parser read as five illegible '
                 'items removed (texts/R101_transcription_corrected.txt).',
         'result': 'worked', 'technique': ['manual reconstruction']},
        {'date': DATE, 'kind': 'verification',
         'what': 'Decipherments aligned with the figures letter by letter (reread_aless_align.py, edit-distance DP over '
                 'the two-letter figure sets). Agreement 89-94% of words; the disagreements located the key\'s gaps: '
                 '9 also = con, dotted 0 = z, 0^.0 = et, X0Y0 codes often written X0Y, doubled letters enciphered '
                 'once, code values 1040 lettere (Lasry "Regina di Francia?"), 3020 quando, 3060 -mente, 4020 come, '
                 '4040 Milano, 4080 et, 5070/6050 Imbasciatore, 6060 Inquisitione; 6090 a demonstrative (questa/e).',
         'result': 'worked', 'technique': ['crib testing', 'key-structure hypothesis']},
        {'date': DATE, 'kind': 'reading',
         'what': 'R94, R95, R100 read from the decipherments with the figures deciding where they differ; R101 re-decoded '
                 'with the extended key (reread_aless_decode.py) and read word by word on the figures and the image '
                 '(chinea, protesta del fisco, devolutione, Iulio secondo et Iulio terzo, notarii, carcerati; 8090 = '
                 'havere, 209 = chi). English translations written. _check_reading.py on the bodies: 1.00, 0.94, 1.00, '
                 '0.84 clean. State decoded, not read -> read for all four; class read in part -> read.',
         'result': 'worked', 'technique': ['beam/DP decoding', 'language-model scoring', 'contextual inference',
                                            'manual reconstruction']},
    ]
    for s in steps:  # one step per save: the splice saver cannot insert two list items at one point
        p = load(F)
        p['solution'].append(s)
        save(F, p)


if __name__ == '__main__':
    main()
