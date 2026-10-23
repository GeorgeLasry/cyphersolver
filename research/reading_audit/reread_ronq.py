"""Re-read brief (REREAD_BRIEF.md), batch ronq: ronquillo1676 (DECODE R966-R984, R1001).

Targeted profile edits with the splice saver of relabel_r0.py (only changed spans are rewritten).

    python research/reading_audit/reread_ronq.py
"""
import sys
import pathlib

sys.path.insert(0, str(pathlib.Path(__file__).parent))
from relabel_r0 import load, save  # noqa: E402

DATE = '2026-10-22'
BY = 'Claude Opus 5.5'
F = 'ronquillo1676'

M = 'the contemporary decipherment in the left margin, transcribed from the DECODE images, aligned word by word with the key decode'
# rec: (grade, review note, summary, corrected label or None, doc)
READ = {
    'R966': ('A', f'Rests on {M}. f. 1 margin badly faded; one hole ("debiéndolo [...] creer", group qe).',
             'Salinas to Fuenmayor, London 21 Aug 1676: Charles II tells Salinas that an invasion of France would harm the peace and that the Maastricht and Philippsburg sieges will end the campaign; the King is in a bad humour over German successes; on the passports he favours the Münster precedent against the princes\' new claims (Lorraine); no treaty talk until the campaign ends.',
             None, 'margined'),
    'R969': ('A', f'Rests on {M}; margin clear and complete. Nothing unread.',
             'Salinas to Fuenmayor, London 8 Sep 1676: after the fall of Maastricht peace talk grows and Van Beuningen leans to it; Salinas\'s orders are too limited to negotiate; Lorraine\'s minister to be treated as ambassador (precedent of Serinchamps); the other princes\' claims depend on the Emperor; France\'s answer awaited.',
             None, 'margined'),
    'R967': ('B', f'Rests on {M}. Two single-word holes ("[...] en uno y otro", "con [?esto]").',
             'Salinas to Fuenmayor, London 8 Dec 1676: France has the English court bewitched; Parliament is awaited and may be prorogued; Salinas\'s memorial against levies for France was answered harshly, then patched up and both memorials suppressed; he holds firm, as Molina did.',
             None, 'margined'),
    'R968': ('A', f'Rests on {M}. One hole where the f. 1 margin is faded. Dated 6 Oct 1676 in its clear text (DECODE: 8 Dec).',
             'Salinas to Fuenmayor, London 6 Oct 1676: The Hague fixes a day for the Nijmegen congress; William of Orange is expected in London this winter with powers to treat, and his marriage to York\'s daughter is talked of; Charles II\'s dealings would harm the Dutch and Spain alike.',
             'R968, Salinas, 6 Oct 1676', 'margined'),
    'R971': ('A', f'Rests on {M}; every cipher line has its margin. Same letter as R972 (the seven images are pixel-identical). Open: [?nuestra] lira, [?proyectado], [?menagero].',
             'Salinas to Fuenmayor, London 26 Jan 1677 (same letter as R972): Temple\'s mission to The Hague won Orange over to the peace; Salinas fears the Anglo-Dutch project sacrifices Burgundy; Charles II says the peace must be made and that Flanders keeps frontiers; recruiting for France stopped in England but goes on in Scotland; Amerongen and Van Beuningen differ over a truce; a 2-3 month suspension of arms may be proposed.',
             'R971, Salinas, 26 Jan 1677 (= R972)', 'margined'),
    'R972': ('A', f'Rests on {M}. Same letter as R971 (images pixel-identical); this transcription is the cleaner one.',
             'Salinas to Fuenmayor, London 26 Jan 1677 (same letter as R971): Temple, Orange and the peace; fears for Burgundy; Charles II on the peace and the frontiers of Flanders; recruiting for France; Amerongen and Van Beuningen; a proposed suspension of arms.',
             None, 'margined'),
    'R973': ('A', 'Rests on the contemporary decipherment in the left margin (DECODE recorded it only in a comment, so the letter was listed as unmargined), transcribed from the images, and the key decode; B = s fixed on the images (key coverage 85.9% -> 95.4%). Nothing unread.',
             'Salinas to Fuenmayor, London 2 Mar 1677: Parliament\'s first steps on recalling the English troops from France look promising; with money more could be done, since "todo va de cabeza y de limosna"; talk of the Spanish negotiations has calmed; if Louis XIV left on Sunday the march from Paris is made.',
             None, 'margined'),
    'R970': ('A', 'Rests on the contemporary decipherment in the left margin of ff. 2-4 (DECODE recorded it only in a comment), transcribed from the images, and the key decode with image-checked labels. Nothing unread.',
             'Salinas to Fuenmayor, London 15 Sep 1676: after the fall of Maastricht nothing can be expected of Orange and England drifts towards peace; Salinas watches Van Beuningen; the Danish envoy fears him and Bergeyck and has asked the King of Denmark to keep Salinas in London.',
             None, 'margined'),
    'R984': ('B', 'Read on the images (no margin on any page), labels corrected (read/R984_corrections.tsv, txi/R984.txt), key values from the margined siblings. About 12 code groups unidentified (138, 91, 113, 460, cus, 600 ...): no key material.',
             'Ronquillo to Fuenmayor, Nijmegen 26 Feb 1678: on the assembly of the northern allies at Copenhagen; everything hangs on England\'s resolution; praises Fuenmayor for stopping the allies\' ministers threatening the States General; the allies complain of Spanish subsidies paid in monthly instalments; a Hanover intrigue (a marriage to the Duchess of Celle\'s daughter; Estrades dealing with Hanover).',
             None, 'unmargined'),
    'R982': ('B', 'Read on the images (no margin), second-pass re-transcription in txi/R982.txt (about 35 labels changed). Opening groups and about 12 phrase-level holes: soft scan (4/7/9 and tall signs not distinguishable) and no key material for dul, al, lop, fin, 109, bc.',
             'Ronquillo to Fuenmayor, Nijmegen 19 Mar 1678: after the loss of Ghent Flanders is near despair; England stays irresolute; he hopes the allies drop their quarrels to defend the Low Countries and the North; Königsmarck\'s incursion should press the Brunswick princes; nothing worth reporting from the congress.',
             None, 'unmargined'),
    'R976': ('B', f'Rests on {M}. Open: [?treguas], a verb under ink blots, and the noun after "el nuevo" (gap in margin and cipher).',
             'Ronquillo to Fuenmayor, Nijmegen 10 Apr 1677: the negotiations worsen; the Dutch handed the mediators new full powers; rumours of separate Spanish talks and royal marriages worry the allies; Saint-Omer and Cambrai expected as the first article of an armistice; the Brunswick guarantee; Hanover to mediate a separate treaty with Sweden and Denmark.',
             None, 'margined'),
    'R977': ('B', f'Rests on {M}; DECODE had merged two cipher rows and dropped one, restored from the image (txi/R977.txt). Open: [?mensaje], [?paces], groups 703, 225, 138.',
             'Ronquillo to Fuenmayor, Nijmegen 17 Apr 1677: Windischgrätz revealed Fuenmayor\'s secret to the Brandenburg minister; Vienna is jealous of the allies\' progress in the North and the English peace terms favour Sweden; Ronquillo had a reply sent to the Emperor before they are presented; the allies are unreliable (declaration at Celle).',
             None, 'margined'),
    'R975': ('A', f'Rests on {M} on six pages; no label fixes needed. Only single uncertain words ([?suecos], [?altivez]).',
             'Ronquillo to Fuenmayor, Nijmegen 28 Dec 1676: the Dutch press for peace; Kinsky\'s sciatica excuse; full powers handed to the mediators; objections to the Swedish and French powers (Westphalia clause, Fürstenberg\'s release, the Pope\'s mediation); Münster and Wolfenbüttel over Bremen; France denies Lorraine and the princes the jus legationis.',
             None, 'margined'),
    'R978': ('A', f'Rests on {M}; DECODE\'s margin transcription had missed a sentence. Nothing unread. Dated 10 Feb 1677 in clear (DECODE: 20 Feb), signed by Bernardo Navarro for Ronquillo.',
             'Ronquillo to Fuenmayor, Nijmegen 10 Feb 1677: the full-powers dispute (the Danish plenipotentiary insists on Latin, French or Danish); the Dutch furious at Kinsky; Ronquillo fears they will force a treaty on Spain; Windischgrätz\'s declaration; Orange waits on the imperial army; Lira stays in Brussels.',
             'R978, Ronquillo, 10 Feb 1677', 'margined'),
    'R979': ('A', f'Rests on {M}. Two holes (group 934 where the margin stops; "[?quedan]").',
             'Ronquillo to Fuenmayor, Nijmegen 9 Jan 1677: backs Fuenmayor\'s proposed course; the Emperor aims at Breisach and Alsace, not Flanders; the English mediators passed on the Franco-Swedish draft; the Dutch are eager for peace and Kinsky does not grasp Spain\'s plight.',
             None, 'margined'),
    'R974': ('A', f'Rests on {M}. One uncertain word ([?himeneo]). Dated 21 Sept 1676 at The Hague in clear (DECODE: 1676Dec21).',
             'Ronquillo to Fuenmayor, The Hague 21 Sep 1676: Stralsund and Philippsburg; the Münster and Celle troops better sent to Pomerania; mocks the Council of State; France\'s declaration of war on Denmark; the Bremen assembly; remittances must be in Antwerp by 10 November or "Maese Luis" will cook the peace.',
             'R974, Ronquillo, 21 Sep 1676', 'margined'),
    'R1001': ('A', f'Rests on {M}. One supplied verb; the opening figures not rendered by the margin.',
              'Ronquillo to Fuenmayor, Nijmegen 6 Feb 1677: the plenipotentiary preliminary; Dutch haste and Beverningh; Lira absent in Brussels; talk of a Dutch-Swedish separate peace; an "interim" proposal at the Bremen assembly that will "go up in smoke".',
              None, 'margined'),
    'R980': ('A', f'Rests on {M}, which also runs across the page feet. One overwritten margin line decided by the figures. Not the same letter as R981 (images differ).',
             'Ronquillo to Fuenmayor, Nijmegen 27 Jan 1677: Brunswick and Münster pull out of the Bremen assembly; rumours of a Dutch-Swedish separate peace; the suspension-of-arms argument with Amerongen; a separate Swedish peace a precipice; Kinsky wastes time; the French show no wish for peace.',
             None, 'margined'),
    'R981': ('A', f'Rests on {M}. Open: [?Wesel], [?Mulle], [?menajero]. Dated 4 Mar 1677 in clear (not 27 Jan).',
             'Ronquillo to Fuenmayor, Nijmegen 4 Mar 1677: the Swedish separate peace; Denmark and Scania; Brandenburg\'s claim to Pomerania and the Emperor\'s objection; the Celle minister\'s demand for ambassadorial passports; the allies\' proposals ask for restoration to the state of 1665.',
             'R981, Ronquillo, 4 Mar 1677', 'margined'),
    'R983': ('B', f'ff. 2-7 rest on {M}; the f. 1 margin is faded almost to nothing, so f. 1 rests on the key decode alone and keeps many holes (illegible margin; groups l, c, 1q, L2, pA, 11, 300 not in the key). The reply to Jenkins on f. 6 is under a blot.',
             'Ronquillo to Fuenmayor, Nijmegen 22 May 1677: Fuenmayor\'s papers and the Bremen conference; Bremen and Verden; the Baltic squadron; the northern alliances; an army needed in Flanders after the battle of Saint-Omer (Cassel), Villahermosa with hired mules; written versus verbal answers through the mediators (Jenkins).',
             None, 'margined'),
}

NOTE = ('Re-read 22 Oct 2026 (batch ronq): read/{r}_reading.md and read/{r}_en.md, log read/{r}_reread_log.md; '
        'decryption read/{r}.dec.txt (key decode cut into words, page by page, spaced.py).')


def main():
    p = load(F)
    for t in p['outcome']['texts']:
        rec = t['label'].split(',')[0]
        grade, note, summary, label, doc = READ[rec]
        if label:
            t['label'] = label
        t['doc'] = doc
        t['state'] = 'read'
        t['decryption'] = 'read/%s.dec.txt' % rec
        t['reading'] = 'read/%s_reading.md' % rec
        t['translation'] = 'read/%s_en.md' % rec
        t['language'] = 'es'
        t['summary'] = summary
        t['note'] = NOTE.format(r=rec)
        t['reading_review'] = {'grade': grade, 'by': BY, 'date': DATE, 'note': note}
    d0, d1 = p['documents']
    d0['shelfmark'] = ("AGR Brussels, Secrétairerie d'État et de Guerre 2559 (DECODE R966-R981, R983, R1001; "
                       "R971 and R972 are one letter)")
    d0['length']['tokens'] = 20644 + 663 + 199
    d0['date'] = 'Aug 1676 - May 1677'
    d1['shelfmark'] = 'AGR Brussels, SEG 2559 (DECODE R982, R984)'
    d1['length']['tokens'] = 813 + 1144
    d1['date'] = 'Feb - Mar 1678'
    d1['read'] = 'read'
    d1['transcription']['notes'] = 'R982 and R984 re-transcribed from the images (txi/).'
    o = p['outcome']
    o['class'] = 'read in part'
    o['method'] = 'read from existing decipherment'
    o['method_basis'] = ('Eighteen of the twenty letters carry a contemporary decipherment in the left margin (R970 and '
                         'R973 too: DECODE recorded theirs only in a comment). On 22 Oct 2026 the margins were '
                         'transcribed from the DECODE images and aligned word by word with the decode of the Balbases '
                         '1677 key (rebuilt earlier in this project for sibling letters in the same volume). The two '
                         'letters without a margin, R982 and R984, were read on the images with that key.')
    newcon = ['transcription', 'key extended or corrected', 'sender or date identified', 'catalogue correction']
    o['fraction_read'] = 1.0
    o['fraction_read_source'] = ('22 Oct 2026, re-read (batch ronq): all twenty letters build sentences and are '
                                 'translated (read/R*_reading.md, _en.md; grades 13 A, 7 B). Tokens of letters that '
                                 'read / all = 23,463 / 23,463. Holes remain inside the readings: R983 f. 1 (faded '
                                 'margin), R982 and R984 (unglossed code groups, soft scan of R982) and single words '
                                 'elsewhere; docs/_check_reading.py clean share per reading 0.50-0.86 (the Notes '
                                 'sections included; reading bodies about 0.62-1.0).')
    o['notes'] = ('22 Oct 2026, re-read: all twenty letters read and translated, eighteen from their contemporary '
                  'margins. Class stays read in part: about 60 code values found in the margins (NOTES.md) are not '
                  'yet entered into keyx.py, and with them R982, R984 and R983 f. 1 can be retried.')
    steps = []
    o['gaps'] = [
        {'item': 'R983 f. 1 passage (many holes)', 'blocker': 'illegible',
         'detail': 'the f. 1 margin is faded almost to nothing on the DECODE scan; groups l, c, 1q, L2, pA, 11, 300 not in the key'},
        {'item': 'R982 opening groups and about 12 phrase-level holes; R984 about 12 code groups', 'blocker': 'open-codes',
         'detail': 'no margin; codes 138, 91, 113, 460, cus, 600, dul, al, lop, fin, 109, bc have no gloss in the margined letters read so far; R982 soft scan'},
        {'item': 'single words in R966, R967, R968, R971/R972, R976, R977, R979, R981, R1001', 'blocker': 'illegible',
         'detail': 'margin faded or blotted at that word and the figures alone do not settle it'},
        {'item': 'about 60 code values read from the margins not yet in keyx.py', 'blocker': 'not-attempted',
         'detail': 'list in NOTES.md (22 Oct block); enter them, re-decode, and retry the holes of R982, R984 and R983 f. 1'},
    ]
    steps.append({'date': DATE, 'kind': 'transcription',
                          'what': 'Contemporary margin decipherments of eighteen letters transcribed from the DECODE images (R970 and R973 found to have one: DECODE put it in a comment); cipher labels checked on full-resolution crops where margin and key decode disagreed; corrected transcriptions txi/R966-R970, R973, R977, R982, R984.',
                          'result': 'worked', 'technique': ['manual reconstruction']})
    steps.append({'date': DATE, 'kind': 'reading',
                          'what': 'Each letter built into normalised Spanish from the key decode (spaced.py, words cut by DP over lang/ Spanish) aligned with its margin, and translated (read/R*_reading.md, _en.md); R982 and R984 read on the images alone. All twenty read (13 grade A, 7 B); about 60 code values recovered from the margins.',
                          'result': 'worked', 'technique': ['plaintext matching', 'beam/DP decoding', 'contextual inference']})
    steps.append({'date': DATE, 'kind': 'verification',
                          'what': 'Images compared: R971 and R972 are pixel-identical (one letter, 26 Jan 1677); R980 and R981 differ. Dates corrected from the clear text: R968 6 Oct 1676, R974 21 Sep 1676 (The Hague), R978 10 Feb 1677, R981 4 Mar 1677.',
                          'result': 'worked', 'technique': ['other']})
    steps.append({'date': DATE, 'kind': 'verification',
                          'what': 'R983 f. 1 margin enhanced crops: faded beyond reading on the DECODE scan; R982 second-pass labels cannot separate 4/7/9 on the soft scan.',
                          'result': 'failed', 'technique': ['manual reconstruction']})
    save(F, p)
    # the splice saver mis-orders several appends to one list in a single save: append one per save
    for c in newcon:
        p = load(F); p['outcome']['contribution'].append(c); save(F, p)
    for st in steps:
        p = load(F); p['solution'].append(st); save(F, p)


if __name__ == '__main__':
    main()


def keystep():
    """Second pass: the margin code values entered into keyx.py (not-attempted gap closed)."""
    p = load(F)
    o = p['outcome']
    o['gaps'] = [g for g in o['gaps'] if not g['item'].startswith('about 60 code values')]
    o['notes'] = ('22 Oct 2026, re-read: all twenty letters read and translated, eighteen from their contemporary '
                  'margins; the code values found in the margins entered into keyx.py (key coverage 93.6% -> 95.4%, '
                  'sense 83.3% -> 85.4% by dec2.py). Read in part: holes remain in R983 f. 1 (faded margin), R982 and '
                  'R984 (unglossed codes, soft scan) and single words elsewhere, each with an outside blocker.')
    save(F, p)
    p = load(F)
    p['solution'].append({'date': DATE, 'kind': 'sibling key',
                          'what': 'About 60 code values read from the margins added to keyx.py where the group had no value (conflicting groups 97, do, 59, 67, 51, 112, 120, 135, 163, 170, 11, bi left as they were); dec2.py over all twenty: in key 93.6% -> 95.4%, sense 83.3% -> 85.4%. The readings of R982 and R984 already used these values; no further hole closed.',
                          'result': 'worked', 'technique': ['plaintext matching']})
    save(F, p)
