"""Re-read brief (REREAD_BRIEF.md), batch b03: smith1562 (Add MS 4136, Smith's letters 1562-1566).

Targeted profile edits with the splice saver of relabel_r0.py (only changed spans are rewritten); one solution step
per save, because the saver misorders several appends to one list in a single save.

    python research/reading_audit/reread_b03.py smith1562
"""
import sys
import pathlib

sys.path.insert(0, str(pathlib.Path(__file__).parent))
from relabel_r0 import load, save  # noqa: E402

DATE = '2026-10-22'
BY = 'Claude Opus 5.5'
LOG = 'no01-no23_reread_log.md'

FORBES = ('Forbes, A Full View ii (1741), printed from the original with the deciphered words in italic; the cipher '
          'passages of Add MS 4136 aligned one to one with the italic stretches and checked on the glyphs with key '
          'R9261 (%s).' % LOG)
CSP = ('Cipher passages re-read on the DECODE image with key R9261 (%s, no01-no23_corrections.tsv). The clear text of '
       'the letter is not in print, so the reading is the passages themselves; the CSP Foreign summary gives their '
       'setting and agrees with them.' % LOG)

READ = {
    '01': ('A', FORBES + ' Forbes ii 287-289; all 13 passages checked. Not transcribed before.',
           'Smith to the Queen, Chartres, 17 Jan 1562/3 (Forbes ii 287-289): someone should be sent to the Admiral, '
           'now chief on the other side, and Mr Middlemore would be fit; the Guisians will make no agreement with the '
           'Queen; the Constable suspects the Guise and fears the ruin of the Châtillons; if the Admiral holds out, '
           'necessity will force an accord; the Queen should act with speed while the Huguenot faction is at her '
           'devotion. The 13 cipher passages of f. 157 are read as Forbes prints them.'),
    '03': ('A', FORBES + ' Forbes ii 350-351; 16 passages; "musters" carried by the print only.',
           'Smith to Cecil, Blois, 7 Mar 1562/3 (Forbes ii 350-351): the Guise\'s death has brought the French "even '
           'into my lap"; musters and captains, have all Normandy again this summer; no hostages or assurances for '
           'Calais, no quiet holding of Newhaven; the French confess their weakness and need of English friendship; '
           'Smith fears only the meddling of the Queen of Scots.'),
    '04': ('A', FORBES + ' Forbes ii 357-359; 58 passages, 1-24 checked glyph by glyph, f. 168 by sign class and '
                'spot checks. Not transcribed before.',
           'Smith to the Queen, Blois, 12 Mar 1562/3 (Forbes ii 356-359): a Spanish packet intercepted at Trent '
           'reveals a Spanish-Imperial plan against France; the Admiral holds out on the peace terms and is looked '
           'for at court; the Spanish ambassador sounds Smith on Caen, Calais and the forfeit crowns; Condé is won '
           'over and will help drive the English out of France; the Emperor will denounce war over Metz, Toul and '
           'Verdun.'),
    '05': ('A', FORBES + ' Forbes ii 385-386; the 12 passages of decipher_A Letter 2.',
           'Smith to Cecil, Amboise, 13 Apr 1563 (Forbes ii 384-386): Condé, sworn in his authority, is thought a new '
           'King of Navarre, won by the papists; to deal with the Admiral or d\'Andelot is vain, all must be done with '
           'the Queen Mother and the Prince; the Spanish ambassador says Philip will not meddle in a quarrel between '
           'England and France over Calais or Newhaven; Smith would take Calais.'),
    '06': ('B', CSP + ' CSP Foreign vi no. 1078.',
           'Smith to the Queen, [Valmont] 27/28 July 1563: the Earl of Warwick does not say whether he can keep '
           'Newhaven, for how long, or with how many men (CSP vi 1078 §5).'),
    '08': ('B', CSP + ' CSP Foreign vii no. 642. Open: four single signs ((2), (11), ẓ, ï).',
           'Smith to Cecil, Valence, 1 Sep 1564: the Scots-French practice against the amity of England and Scotland; '
           'the Lord of Murray and the lords favouring religion; Huntly; the bishops and the Pope\'s council; '
           'Lethington, his brother at Bruges, the Bishop of Glasgow and a French pension; the Queen of Scots and '
           'Lord Robert; the old Pope; the King of Spain and the Queen of Scots (CSP vii 642 §3).'),
    '09': ('B', CSP + ' CSP Foreign vii no. 650. Both passages are names.',
           'Smith to Cecil, Valence, 3 Sep 1564: Ninian Cockburn may come into England with Villeroy (CSP vii 650).'),
    '11': ('B', CSP + ' CSP Foreign vii no. 793. ·∂ read [?sea] from the calendar here and in no. 15; ⊙ read '
                '[?Dieppe]; two signs open.',
           'Smith to Cecil, Marseilles, 13 Nov 1564: never in so great a trouble; a post for Scotland goes by Dieppe or '
           'by sea, all by the Cardinal of Lorraine; the matter is hot, chiefly the marriage matter, who shall bear the '
           'bell away; his men in England by whom he dare speak (CSP vii 793).'),
    '13': ('B', CSP + ' CSP Foreign vii no. 808. Two passages; T: in the second unexplained.',
           'Smith to Cecil, Arles, 22 Nov 1564: the Emperor\'s house (the Archduke Charles) and a marriage with the '
           'Queen\'s Majesty (CSP vii 808).'),
    '15': ('B', CSP + ' CSP Foreign vii no. 916. Five single signs open (ʒ:, P̄, Γ̈⊓, Ꮚbo, ξ̣), each once.',
           'Smith to Cecil, Narbonne, 7 Jan 1564/5: posts out of Scotland, Mr Beton and Hume by land, by the Cardinal '
           'of Lorraine, by sea; the house of Guise earnest in the marriage between the Duke of Guise and the Queen of '
           'Scots (CSP vii 916).'),
    '16': ('B', CSP + ' CSP Foreign vii no. 979. The first five signs of (1) open.',
           'Smith to Cecil, Toulouse, 9 Feb 1564/5: congratulation and condolence; the French and the interview; the '
           'Queen\'s Majesty; the Emperor\'s house (Charles of Austria); this French offer (CSP vii 979).'),
    '17': ('B', CSP + ' CSP Foreign viii no. 208. 23 of 27 passages read; five single signs open.',
           'Smith to Cecil, Bourbon-l\'Archambault, 22 Mar 1565/6: not that crown; the young King and Queen of '
           'Scots; intelligence and practices in England and foreign realms; the Pope\'s and King of Spain\'s hands; '
           'privy dispatches and couriers out of Scotland; the ambassadors of Spain and Scotland and the Cardinal of '
           'Lorraine; the Bishop of Glasgow looks to be a cardinal; popery in Scotland and England; a fat Scottish '
           'woman, married, the conveyer of letters to Lady Lennox (CSP viii 208).'),
    '18': ('B', CSP + ' CSP Foreign viii no. 327. One sign open in (3).',
           'Smith to Cecil, Paris, 29 Apr 1566: Sturm\'s letter by Peter Clare, Almain; Albert de Rosemberg; a '
           'continuation with the princes of Almain for the recovery of Metz and Calais (CSP viii 327).'),
    '19': ('A', FORBES + ' Forbes ii 119; "secretary" = the key\'s secret sign + a-r-y, so every italic word is '
                'carried by the figures.',
           'Smith to Cecil, Paris, 15 Oct 1562 (Forbes ii 119): Scots report envoys sent to move the Queen of Scots '
           'to break with England and make war, and a plan to convey the hostages into Flanders; Secretary Rollet and '
           'Monsieur Villemort are gone.'),
    '20': ('A', FORBES + ' Forbes ii 123 (OCR line garbled; read on the page image). One short group (maбγ) has no '
                'value and carries no printed word.',
           'Smith to Cecil, Poissy, 20 Oct 1562 (Forbes ii 123): Newhaven is not so strong as men take it; in summer '
           'they would try to drive the English out with "a garden of chamillion upon the hill on this side"; the '
           'French works there are not finished.'),
    '22': ('B', CSP + ' CSP Foreign vi no. 1366. Every word now carried; "sent" for the copy\'s :b marked [?].',
           'Smith to the Queen, 4 Nov 1563: De Montaigne, whose carte of La Rochelle Smith sends; letters given him '
           'to Lord Robert and Mr Secretary; the other letters he carried himself; the feat Smith wrote of is most '
           'necessary at this time (CSP vi 1366).'),
}

NOTE23 = ('Re-read 22 Oct 2026 (batch b03, %s): the four lines re-read on the DECODE image R9236 with key R9261. (1) '
          'Monsieur de [ſ.]uy (ſ. not in the alphabet; the name unidentified); (2) the queen of Navarre; (3) "the queen" '
          '+ unread signs; the last line "[ξ]band that [K. of Navarre] and way with ..." without sense. Not in Forbes '
          '(no Smith advertisements of this date in vol. ii) nor in CSP Foreign vi; no clear or printed text exists, and '
          'the unknown signs occur once each. Blocker: no clear text and too short to fix the signs.' % LOG)


def smith1562():
    p = load('smith1562')
    o = p['outcome']
    for t in o['texts']:
        d = t['doc']
        if d in READ:
            grade, note, summary = READ[d]
            t['state'] = 'read'
            t.pop('note', None)
            if d in ('01', '04'):
                t['transcription'] = LOG
                t['decryption'] = 'no%s_reading.md' % d
            t['reading'] = 'no%s_reading.md' % d
            t['translation'] = 'no%s_en.md' % d
            t['language'] = 'en'
            t['summary'] = summary
            t['reading_review'] = {'grade': grade, 'by': BY, 'date': DATE, 'note': note}
        elif d == '23':
            t['note'] = NOTE23
    o['fraction_read'] = 0.99
    o['fraction_read_method'] = 'estimated'
    o['fraction_read_source'] = (
        '22 Oct 2026, re-read (batch b03): estimated by numbered cipher passages, since Forbes copied only the cipher '
        'stretches and no token counts exist. 23 letters, about 335 passages (01: 13, 02: 32, 03: 16, 04: 58, 05: 12, '
        '06: 2, 07: 1 block, 08: 31, 09: 2, 10: ~62, 11: 12, 12: 3, 13: 2, 14: 12 lines, 15: 7, 16: 10, 17: 27, 18: 5, '
        '19: 6, 20: 4, 21: 6, 22: 7 lines, 23: 4); the 22 letters that read hold about 331 of them, no. 23 (4) does '
        'not: about 0.99. Earlier: ~0.45 (reading audit, same day).')
    o['notes'] = (
        'Most passages read; code signs in the hooked-T family read from context. 22 Oct 2026, re-read (batch b03): '
        'nos. 01 and 04 aligned with Forbes\'s italics (Forbes prints the deciphered words in italic) and read; nos. 03, '
        '05, 19, 20 read in their printed sentences; nos. 06, 08, 09, 11, 13, 15-18, 22 re-read on the images (m̄ = '
        'marriage, ·∂ = sea, ‖ = i, key-sheet words checked on R9261) and read as the passages themselves, set by the CSP calendar. '
        'No. 23 (advertisements, 31 Jan 1562/3) stays decoded, not read: no clear text, unknown signs once each. '
        'Single unread signs remain in nos. 08, 11, 15, 16, 17, 18 (%s).' % LOG)
    o['key'] = 'partial'
    o['gaps'] = [
        {'item': 'single code signs in nos. 08, 11, 15, 16, 17, 18 (about 15 signs, one occurrence each)',
         'blocker': 'no-key-material',
         'detail': 'not on the key sheet R9261; the clear text of these letters (SP 70) is not in print, CSP Foreign '
                   'gives summaries only'},
        {'item': 'no. 23, advertisements from France, 31 Jan 1562/3 (R9236 f. 140), four short lines',
         'blocker': 'too-short',
         'detail': 'no clear or printed text (not in Forbes, not found in CSP Foreign vi); the unknown signs occur once'},
    ]
    p['conditions']['last_date'] = DATE
    p['conditions']['sessions'] = max(2, p['conditions'].get('sessions', 1) + 1)
    save('smith1562', p)
    steps = [
        {'date': DATE, 'kind': 'access',
         'what': 'Re-read under REREAD_BRIEF (batch b03): DECODE R9236 image fetched with the project cookie (the other '
                 'records were in the main checkout); Forbes, A Full View ii page images fetched from archive.org '
                 '(leaves 151, 155, 353-355, 416-425, 450-452), since the OCR garbles lines.',
         'result': 'worked'},
        {'date': DATE, 'kind': 'crib',
         'what': 'Found that Forbes sets every deciphered word in italic; the cipher passages of nos. 01, 03, 04, 05, '
                 '19, 20 align one to one with the italic stretches and were checked on the glyphs (01 all 13; 04 '
                 'passages 1-24 and spot checks on f. 168). Nos. 01 and 04, never transcribed, now read from the print '
                 'aligned with the figures.',
         'result': 'worked', 'technique': ['plaintext matching', 'crib testing']},
        {'date': DATE, 'kind': 'transcription',
         'what': 'Nos. 06, 08, 11, 13, 15-18, 22, 23 re-read passage by passage on full-resolution crops with key '
                 'R9261; label corrections in no01-no23_corrections.tsv. Values that hold across documents: m̄ = '
                 'marriage (nos. 11, 13, 15), ·∂ = sea (nos. 11, 15), ‖ = i on ff. 140/159; M̈ = my in no. 03 (my or '
                 'marry in no. 08); key-sheet words checked on R9261 p. 1 (secret, crown, carry, came, king, overmuch, '
                 'privy, she, woman, whom).',
         'result': 'worked', 'technique': ['manual reconstruction', 'contextual inference']},
        {'date': DATE, 'kind': 'reading',
         'what': 'Readings and English written for 16 letters (no<NN>_reading.md, _en.md); _check_reading.py clean '
                 'share 0.50-1.0 (15 lowest: short sentences with one hole). State decoded, not read -> read for nos. '
                 '01, 03, 04, 05, 06, 08, 09, 11, 13, 15, 16, 17, 18, 19, 20, 22; fraction_read ~0.45 -> ~0.99 '
                 '(estimated by passages).',
         'result': 'worked', 'technique': ['manual reconstruction', 'language-model scoring']},
        {'date': DATE, 'kind': 'reading',
         'what': 'No. 23 (advertisements from France, 31 Jan 1562/3) re-read on the image: only "Monsieur de [?]uy" and '
                 '"the queen of Navarre" read; not in Forbes or CSP Foreign vi, signs not in the key, each once. Left '
                 'decoded, not read.',
         'result': 'failed', 'technique': ['manual reconstruction']},
    ]
    for s in steps:  # one step per save
        p = load('smith1562')
        p['solution'].append(s)
        save('smith1562', p)


if __name__ == '__main__':
    globals()[sys.argv[1]]()
