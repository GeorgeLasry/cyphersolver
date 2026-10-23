"""Reread batch b01 (22 Oct 2026): pallotto1629 profile.json update after the re-reading of R287-R313.
Uses relabel_r0's splice saver (one save per change of a list, see the brief's note)."""
import json, sys, pathlib
sys.path.insert(0, str(pathlib.Path(__file__).resolve().parent))
import relabel_r0 as R

F = 'pallotto1629'
BY = 'Claude Opus 5.5'
DATE = '2026-10-22'
T = 'texts/'

# rec: (label date/despatch, state, clean share, grade-or-None, rests-on note, summary)
P = 'Kiewning 1897 prints this sheet verbatim (Roman decipherment), its OCR corrected; the 6956-key decode aligns with it chunk by chunk'
DOCS = {
 'R287': ('4 Aug 1629, second half of Kiewning Nr. 153', 'read', .829, P + '; where the figures differ the reading follows the sheet.',
          "End of the 4 August despatch: Sabran's courier to the King, Spanish suspicion that the French aim at the Empire, the reasons the Emperor's ministers give for war in Italy."),
 'R288': ('4 Aug 1629, "B 24", Kiewning Nr. 154', 'read', .727, 'Two stretches from Kiewning\'s print; about three quarters read from the figures checked on the DECODE scans, and two clear passages read on the scans. One sentence and three groups unresolved.',
          'The new Bohemian bishoprics and the Emperor\'s complaints about P. Valeriano Magni\'s writings on the Carolina and his alchemy and mines; Pallotto asks for orders.'),
 'R289': ('10 Aug 1629, Kiewning Nr. 166 (first part)', 'read', .847, P + '.',
          "Pallotto's audience with Ferdinand II over the Emperor's written answer that blamed the Pope's offices; the date of the Pope's audience for the imperial ambassador."),
 'R290': ('10 Aug 1629, Kiewning Nr. 166 (second part)', 'read', .817, 'Paragraphs 1-3 Kiewning\'s print; paragraph 4 (regest only in Kiewning) read from the figures and the clear words on the DECODE scans.',
          "Questenberg and the revised imperial answer; Eggenberg on deciding the Mantuan case by justice and the Emperor's coronation in Bologna or Ferrara; Sabran's departure, Wallenstein's gout, Magdeburg, Saxony and the Edict of Restitution."),
 'R291': ('11 Aug 1629, "B", Kiewning Nr. 157', 'decoded, not read', .584, None,
          "The Duke of Neuburg's plans to remarry (a daughter of the Duke of Zweibrücken, a heretic ready to convert) and the Bavarian connection."),
 'R292': ('18 Aug 1629, "A 43", Kiewning Nr. 160 (first part)', 'read', .786, 'Most of the sheet Kiewning\'s print; the opening, the Lorraine/Saarwerden and Montauban passages and the last two paragraphs read from the figures and the clear words on the scans; some groups open.',
          'Italy and the war preparations; Lorraine and Saarwerden; England and the Palatine; the election of the King of the Romans; Saxony, Brandenburg and Gabor\'s wife.'),
 'R293': ('18 Aug 1629, Kiewning Nr. 160 (second part)', 'read', .78, 'Two thirds Kiewning\'s print; the opening and the Dohna paragraph read from the figures and the scan; several groups open.',
          'Provisions for the Church in the Empire, Cardinal Klesl\'s speech, the Dohna affair at Breslau.'),
 'R294': ('18 Aug 1629, Kiewning Nr. 160 (end)', 'read', .711, 'The end of Klesl\'s speech from the print; the rest read from the figures and the scan; three groups and the struck last line open.',
          'Cardinal Harrach, the Camaldolese foundation stone and the reform of the Augustinians.'),
 'R295': ('18 Aug 1629, "B 55", Kiewning Nr. 161', 'read', .727, 'The middle Kiewning\'s print; opening and close read from the figures; the first cipher line carries its own contemporary decipherment.',
          'How to raise difficulties through the imperial ambassador; Stralendorf and Halberstadt.'),
 'R296': ('18 Aug 1629, "C 57", Kiewning Nr. 162', 'read', .779, 'First and last paragraphs Kiewning\'s print; the middle four (regest only) read from the figures and about 60 scan crops; groups 275, 957, 593, 440 open.',
          "P. Valeriano Magni's control of the Bohemian church-property business and the danger it holds for the nunciature."),
 'R297': ('25 Aug 1629, "A 67", Kiewning Nr. 164', 'read', .798, 'Two stretches Kiewning\'s print; the rest read from the figures, each paragraph checked against the regest; about 20 groups open; ends at "pregiudica-".',
          'Wallenstein holding back from Italy; Savoy, the Venetians, the Spanish fleet; honours at court; the restitution of church property.'),
 'R298': ('11 Aug 1629, "D 62", Kiewning Nr. 158', 'read', .812, 'Mostly clear text re-read on the scans; the last paragraph Kiewning\'s print; cipher runs checked against the figures.',
          "The brief for Baron Thun's Hungarian priory of the Order of Malta and his demands for privileges."),
 'R299': ('25 Aug 1629, last leaf of R297 (Kiewning Nr. 164)', 'read', .636, 'The middle Kiewning\'s print; the opening and close read from the figures; three holes in about 150 Italian words (the score is pulled down by the header).',
          'End of the 25 August despatch "A 67".'),
 'R300': ('25 Aug 1629, "B 74", Kiewning Nr. 165 (regest only)', 'decoded, not read', .557, None,
          "Bruneau on Wallenstein's reluctance to go to Italy; a sum of 100,000 scudi; the promotion of Don Cesare."),
 'R301': ('25 Aug 1629, "C 76", Kiewning Nr. 166', 'decoded, not read', .606, None,
          "P. Valeriano's second writing on the Carolina; the Jesuits; breaks off mid-sentence."),
 'R302': ('28 Aug 1629, "A 79", Kiewning Nr. 167 (first part)', 'decoded, not read', .64, None,
          'Bruneau; Spanish aims; an intercepted letter to Monterrey; Aldringen and Strozzi; Conti and the Duca di Poli.'),
 'R303': ('28 Aug 1629, end of R302 (Kiewning Nr. 167)', 'read', .712, 'Read from the figures and the clear words re-read on the scans; single groups open (254, 564, 920, 930).',
          "Wallenstein's haste, the indult for Archduke Leopold Wilhelm, the visitor for Aquileia, Savelli and the promotion."),
 'R304': ('28 Aug 1629, "B 86", Kiewning Nr. 168', 'decoded, not read', .526, None,
          "P. Valeriano's privileges and patents and Count Slavata; the dignity of the nunciature."),
 'R305': ('1 Sept 1629, Kiewning Nr. 170', 'read', .722, 'Paragraphs 1-3 Kiewning\'s print; 4-6 (regest only) read from the clear lines on the scan and the figures; groups 277, 207, 907 open, some words cut at the scan edge.',
          'A long discourse with Eggenberg on the Mantuan war; Aldringen at the passes; the Grisons.'),
 'R306': ('15 Sept 1629, "A 93", Kiewning Nr. 176 (first part)', 'read', .938, P + '.',
          'Pallotto\'s offices for peace; the Palatine of Hungary and the Archbishop of Esztergom at court; Lamormain; the Duke of Nevers.'),
 'R307': ('15 Sept 1629, Kiewning Nr. 176 (end)', 'read', .851, P + '; "aiduchi", "liberissimamente", "ho esortato" follow the figures against the print.',
          'Hungary and Transylvania; the Carolina still undecided.'),
 'R308': ('15 Sept 1629, "B", Kiewning Nr. 177', 'read', .75, 'Clear text read on the scan and the figures; the on-page gloss "restati quà contenti della risolutione"; some words supplied only by the regest are marked [?].',
          'The visitor for the diocese of Aquileia; the man sent to negotiate died at Trieste.'),
 'R309': ('15 Sept 1629, Kiewning Nr. 178 (dated 16 Sept there)', 'read', .739, 'Mostly clear text read on the scans; the cipher runs from the codes; one stretch agrees with Kiewning\'s print.',
          'A hint to a privy councillor that a benefice had been promised to Tilly for a relative.'),
 'R310': ('22 Sept 1629, "A 109", Kiewning Nr. 182', 'read', .726, 'Three stretches Kiewning\'s print; the rest read from the figures with spot checks on the scans; groups 649, 347, 900, 266, 955, 479, 200, 353, 329 open, the last paragraph weakest.',
          "Wallenstein's astrology and reluctance to go to Italy; peace and Guastalla; the Duke of Neuburg."),
 'R311': ('29 Sept 1629, "A", Kiewning Nr. 184 (first part)', 'read', .879, P + '.',
          "Ferdinand II's complaints against the King of France for abasing the imperial dignity in Italy."),
 'R312': ('29 Sept 1629, Kiewning Nr. 184 (end)', 'read', .902, P + ', with the date and the Roman decipherment note.',
          'The Spanish ambassadors and Casale; the Empress; Spinola; Flanders and the Dutch.'),
 'R313': ('29 Sept 1629, "B", Kiewning Nr. 185', 'decoded, not read', .667, None,
          "Aquileia and the patriarchate; Eggenberg's remark that without an interim the main business cannot be settled."),
}
NOTREAD = {
 'R291': 'Reread 22 Oct 2026 (batch b01): texts/R291_reading.md is read in part (clean share 0.58 from 0.05): the Neuburg marriage passage and the regest\'s two Italian quotations read; a string of unidentified groups (750, 405, 796, 573, 557, 690, 697, 762, 279, 440, 966, 239, 469) and some garbled letter stretches stay open; Kiewning has only a German regest. Blocker: open codes. The sheet breaks off at the foot of p. 4.',
 'R300': 'Reread 22 Oct 2026 (batch b01): texts/R300_reading.md is read in part (0.56 from 0.17): p. 1 builds sentences with single-word holes; p. 2 was never transcribed by DECODE and was transcribed here (R300_p2_digits.txt), but 3/5/9, 2/7 and 6/8 are hard to separate on the scan, so it is read only at its frame. Kiewning has only a regest. Blockers: legibility of p. 2, open codes.',
 'R301': 'Reread 22 Oct 2026 (batch b01): texts/R301_reading.md is read in part (0.61 from 0.14): one passage is Kiewning\'s print, the rest read from the figures and the clear words re-read on the scans; single groups and some stretches whose figures do not resolve stay open, the right edge of p. 2 is cut off on the scan, and the sheet breaks off mid-sentence (its continuation, register p. 78, is not among the DECODE images). Blockers: open codes, image cut, missing leaf.',
 'R302': 'Reread 22 Oct 2026 (batch b01): texts/R302_reading.md is read in part (0.64 from 0.12): the intercepted letter to Monterrey is Kiewning\'s print and the paragraphs on Bruneau, Spain, Aldringen/Strozzi and Monterrey read as sentences; the Conti/Duca di Poli paragraph has holes in the middle (many unidentified groups, one line of regest). Blocker: open codes.',
 'R304': 'Reread 22 Oct 2026 (batch b01): texts/R304_reading.md is read in part (0.53 from 0.13): the frames (Valeriano breaking the agreement and giving the writing to Count Slavata; the Father\'s privileges and patents; the nunciature\'s dignity) read; the first paragraph\'s middle and the Latin "requisito consensu" formula do not; the breaks were not all checked on the scans. Kiewning has a three-line regest. Blocker: open codes; scan check not finished.',
 'R313': 'Reread 22 Oct 2026 (batch b01): texts/R313_reading.md is read in part (0.67 from 0.10): Eggenberg\'s closing remark is Kiewning\'s print, the rest read from the figures and the clear words, the regest agreeing sentence by sentence; groups 964, 209, 644, 665, 932, 552, 936 open and the seven-line clear paragraph on p. 2 (rapid, partly struck hand) read only at its frame. Blockers: open codes, a struck clear paragraph.',
}

def main():
    p = R.load(F)
    o = p['outcome']
    for t in o['texts']:
        r = t['doc']
        if r not in DOCS:
            continue
        lab, st, cs, basis, summ = DOCS[r]
        t['label'] = t['label'].split(' (DigiVatLib')[0] + f' (DigiVatLib pagination), {lab}'
        t['summary'] = summ
        dec = [T + f'{r}_decrypt.txt', 'reread_b01/' + f'{r}_dec.txt', 'ed/pallotto_bd2_1629.txt']
        t['decryption'] = dec
        t['reading'] = T + f'{r}_reading.md'
        t['translation'] = T + f'{r}_en.md'
        t['language'] = 'it'
        if st == 'read':
            t['state'] = 'read'
            t.pop('note', None)
            t['reading_review'] = {'grade': 'A', 'by': BY, 'date': DATE,
                                   'note': f'{basis} Clean-sentence share {cs:.2f} (docs/_check_reading.py). Log: texts/{r}_reread_log.md.'}
        else:
            t['state'] = 'decoded, not read'
            t['note'] = NOTREAD[r]
    # R286: translation added
    for t in o['texts']:
        if t['doc'] == 'R286':
            t['translation'] = T + 'R286_en.md'
    R.save(F, p)

    # fraction read: symbols of documents that read / all
    p = R.load(F); o = p['outcome']
    L = {d['id']: d['length']['tokens'] for d in p['documents'] if isinstance(d.get('length'), dict)}
    tot = sum(L.values())
    rd = [t['doc'] for t in o['texts'] if t.get('state') == 'read']
    nr = sum(L[x] for x in rd if x in L)
    o['fraction_read'] = round(nr / tot, 3)
    o['fraction_read_method'] = 'measured'
    o['fraction_read_source'] = (f'22 Oct 2026, reread batch b01: symbols (documents[].length) of the {len(rd)} records whose reading '
                                 f'builds sentences ({", ".join(rd)}) = {nr} of {tot} in the 28 records. The six records left '
                                 '"decoded, not read" (R291, R300, R301, R302, R304, R313) have partial readings in texts/ that are not counted.')
    o['method_basis'] = ('The 6956 key of Biermann and Bosbach (DECODE R215), extended in this batch with about 125 nomenclator groups '
                         'learnt from the Roman decipherments Kiewning printed in 1897, decodes the sheets; where Kiewning prints a '
                         'sheet verbatim the reading follows the print, elsewhere it is read from the figures checked on the DECODE scans.')
    o['parts'] = [
        {'label': 'Sheets Kiewning prints verbatim (R286, R287, R289, R306, R307, R311, R312; parts of R288, R290, R292-R299, R302, R305, R310)',
         'records': 'DECODE R286-R312', 'method': 'read from existing decipherment', 'extent': 'complete',
         'basis': 'Kiewning 1897 prints the Roman decipherments; the 6956-key decode aligns with the print chunk by chunk (reread_b01/R*_align.txt) and the figures were followed where they differ.'},
        {'label': 'Passages Kiewning gives only as German regest (most of R288, R291-R305, R308-R310, R313)',
         'records': 'DECODE R288-R313', 'method': 'read with known key', 'extent': 'partial',
         'basis': 'Read from the figures with the 6956 key plus groups learnt in batch b01 (reread_b01/extra_groups.json) and the clear words re-read on the DECODE scans; six sheets (R291, R300, R301, R302, R304, R313) stay read in part for open groups and illegible stretches.'},
    ]
    R.save(F, p)

    p = R.load(F)
    p['solution'].append({'date': DATE, 'kind': 'reading', 'result': 'worked',
        'what': ('Reread batch b01 (REREAD_BRIEF): new decoder (reread_b01_decode.py: nulls 1/8 never inside a group, segmentation by an '
                 'Italian 5-gram model, DECODE\'s uncertain digits and its 0-for-8 misreading as alternatives); every sheet matched to its '
                 'Kiewning number by 9-letter hits and aligned chunk by chunk with the print (reread_b01_match2.py, reread_b01_align.py); '
                 'about 125 nomenclator groups missing from the 6956 key learnt from the alignments and contexts, 776 = tutto and '
                 '567 = occasione corrected (reread_b01/extra_groups.json). Unknown groups in the decodes fell from about 5,000 to about 800 (125 groups in extra_groups.json).'),
        'technique': ['beam/DP decoding', 'language-model scoring', 'plaintext matching', 'contextual inference']})
    R.save(F, p)
    p = R.load(F)
    p['solution'].append({'date': DATE, 'kind': 'reading', 'result': 'partial',
        'what': ('Reread batch b01: the 27 sheets R287-R313 read one by one (R290 by the coordinator, the rest by six reader agents of '
                 'the same model), each with reading, English translation, log and DECODE digit corrections (texts/R*_reading.md, _en.md, '
                 '_reread_log.md, _corrections.tsv); clear text re-read on the DECODE scans (DECODE\'s clear-text transcriptions are mostly '
                 'unusable). 21 sheets build sentences (clean share 0.64-0.94), 6 stay read in part (0.53-0.67): R291, R300, R301, R302, '
                 'R304, R313. Sheets found to be parts of one despatch: R292-R294 (Nr. 160), R297+R299 (Nr. 164), R302+R303 (Nr. 167), '
                 'R306+R307 (Nr. 176), R311+R312 (Nr. 184); DECODE dates corrected (the volume runs 4 Aug-29 Sept 1629, not to November).'),
        'technique': ['manual reconstruction', 'plaintext matching', 'contextual inference']})
    R.save(F, p)
    print('fraction', o['fraction_read'])

if __name__ == '__main__':
    main()
