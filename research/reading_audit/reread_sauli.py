"""Re-read brief (REREAD_BRIEF.md), batch sauli: sauli1579 (R190-R194).

Targeted profile edits with the splice saver of relabel_r0.py (only changed spans are rewritten).

    python research/reading_audit/reread_sauli.py sauli1579
"""
import sys
import pathlib

sys.path.insert(0, str(pathlib.Path(__file__).parent))
from relabel_r0 import load, save  # noqa: E402

DATE = '2026-10-22'
BY = 'Claude Opus 5.5'

READ = {
    'R190': ('B', 'Clear text transcribed from the DECODE images (Midas 2017 draft corrected) and every cipher passage '
                  'given in its interlinear decipherment, checked against the key decode. Three short clear-text '
                  'stretches on f. 93r and f. 94r left as holes; Desmond letter dated Elvas 12 Jan 1581.',
             'Riario to the Earl of Desmond, Elvas 12 January 1581: the papal fort in Ireland is reported lost; aid is '
             'being sought. A news note: the viceroy put the garrison to the sword without resistance. A memorial to '
             'Philip II on the Italian infantry (3,037 paid, about 1,000 fit), the offer of 2,000 under the Pope\'s '
             'name for 4 months, and a commissary to hand them to Desmond.'),
    'R191': ('B', 'Clear text transcribed from the images, cipher passages from the interlinear decipherments, checked '
                  'with the key; the unglossed lines 4-7 of f. 101r decoded with the key. Two short holes.',
             'Riario to the Secretary, mid-January 1581: the second report of the Smerwick massacre; Alba writes that '
             'the 700 Italians embarked are sick, unarmed and deserting; Philip II will not send them to slaughter '
             'and sends two ships to Ireland; Riario writes to Desmond and his brother; the Duke of Sora\'s affairs; '
             'an extract from the Grand Duke; Anselmo to be discharged (4,000 scudi a month owed).'),
    'R192': ('A', 'Clear text transcribed from the images, every cipher passage from its interlinear decipherment, '
                  'checked with the key; the cramped gloss "alla rassegna sono stati 3 milia" fixed from the decode. '
                  'Four short holes.',
             'Riario to the Secretary, 4-5 January 1581: Philip II thanks the Pope for the warning about the Piedmont '
             'plot (Ayamonte, the Anselmi, Huguenots of the Dauphiné) and will not let Italy be disturbed; the '
             'English enterprise, the Italian troops and the news that has cooled the ministers. With a copy of 29 '
             'November 1580: Flanders first, the Italians embarked at Lisbon offered for Ireland or sent home.'),
    'R193': ('B', 'Clear text transcribed from the images, cipher passages from the interlinear decipherments, checked '
                  'with the key; f. 238r is a deciphered copy in clear with the formerly enciphered words underlined. '
                  'Four-digit prefixes before "per" carry no gloss word.',
             'Riario to the Cardinal of Como, Badajoz 2 [Oct?] 1580: Idiáquez says the King cannot undertake the '
             'English enterprise until he is master of Flanders and offers the Italians for Ireland; the nuncio will '
             'not take charge of the 1,300 badly armed soldiers. Elvas, December 1580: the President is "pietra '
             'scandali" and hostile to the Roman Court.'),
    'R194': ('A', 'Clear text transcribed from the images, cipher passages from the interlinear decipherments, checked '
                  'with the key; one hole where the object of "condescendere" is not written.',
             'Riario to the Secretary: Philip II has good will for the enterprise but needs money, will attend to '
             'Flanders first; no truce yet; he bears the weight of Christendom and has spent a fortune maintaining '
             'the Catholic religion in Flanders.'),
}


def sauli1579():
    p = load('sauli1579')
    for t in p['outcome']['texts']:
        rec = t['label'].split(',')[0]
        grade, note, summary = READ[rec]
        t['state'] = 'read'
        t['reading'] = 'texts/%s_reading.md' % rec
        t['translation'] = 'texts/%s_en.md' % rec
        t['language'] = 'it'
        t['summary'] = summary
        t['reading_review'] = {'grade': grade, 'by': BY, 'date': DATE, 'note': note}
        t['note'] = ('Re-read 22 Oct 2026 (texts/R190-R194_reread_log.md, R190-R194_corrections.tsv): the reading is the '
                     'clear text transcribed in full from the DECODE images and the secretariat\'s interlinear '
                     'decipherment of each cipher passage, aligned with the key decode.')
    o = p['outcome']
    o['class'] = 'read'
    o['method'] = 'read from existing decipherment'
    o['method_basis'] = ('Every cipher passage on the 22 pages carries the secretariat\'s contemporary interlinear '
                         'decipherment (R193 f. 238r is a deciphered copy in clear); transcribed in full from the DECODE '
                         'images on 22 Oct 2026 with the clear text and checked against Lasry\'s key (DECODE, Oct 2020).')
    o['contribution'] = ['transcription', 'key extended or corrected', 'sender or date identified', 'catalogue correction']
    o['fraction_read'] = 1.0
    o['fraction_read_source'] = ('22 Oct 2026, re-read (batch sauli): all five records build sentences and are '
                                 'translated (texts/R19*_reading.md, _en.md). Tokens of documents that read / all = '
                                 'all / all = 1.0 (the R192-R194 group count was never measured; both document groups '
                                 'read). Holes inside the readings: about a dozen words in all, plus the code-group '
                                 'ambiguities 10, 20/28, 40, 72 that the glosses resolve case by case.')
    o['notes'] = ('Read from the contemporary decipherments, checked with the key. Open: the four-digit prefixes '
                  '6371/7771/7361/7761 (no gloss word), the code group for "religione cattolica" (R194), the double '
                  'senses of 10, 20/28, 40, 72 (0 and looped 8 one shape in this hand).')
    for part in o.get('parts', []):
        part['label'] = 'R190-R194 (contemporary interlinear decipherments, transcribed in full)'
        part['extent'] = 'complete'
        part['basis'] = ('interlinear decipherments of the time on every passage, transcribed with the clear text '
                         'from the DECODE images on 22 Oct 2026 (texts/R19*_reading.md); Lasry\'s key agrees with them '
                         'where the figures are legible.')
    p['conditions']['last_date'] = DATE
    p['conditions']['sessions'] = 2
    steps = []
    steps.append({
        'date': DATE, 'kind': 'access',
        'what': 'Re-read under REREAD_BRIEF (batch sauli): the 22 DECODE page images of R190-R194 fetched again with '
                'the DECODE session cookie (full resolution, kept out of the repository).',
        'result': 'worked'})
    steps.append({
        'date': DATE, 'kind': 'transcription',
        'what': 'All 22 pages transcribed in full: clear text (Midas 2017 draft corrected on the image for R190/R191) '
                'and every interlinear decipherment, page by page at native resolution with zoomed crops; '
                'corrections in texts/R190-R194_corrections.tsv.',
        'result': 'worked', 'technique': ['manual reconstruction']})
    steps.append({
        'date': DATE, 'kind': 'verification',
        'what': 'Glosses aligned with the key decode: agreement wherever legible; R191 f. 101r lines 4-7 (unglossed) '
                'decoded with the key; R192 f. 196r cramped gloss fixed from the decode. Code groups: 82 = navi '
                '(Lasry\'s "Hune" was a misread gloss), 72 Regina / denari, 60 Duca, 77 9 00 il Marchese; 10, 20/28, 40 '
                'keep two glossed senses; the four-digit prefixes stay unexplained.',
        'result': 'partial', 'technique': ['crib testing']})
    steps.append({
        'date': DATE, 'kind': 'reading',
        'what': 'Readings and English translations written for R190-R194 (texts/R19*_reading.md, _en.md); '
                '_check_reading.py on the text bodies 0.78-0.96 clean sentences (the remainder mostly abbreviation '
                'fragments). Dates fixed: R190 Elvas 12 Jan 1581, R191 mid-Jan 1581, R192 letter 4-5 Jan 1581 with a '
                'copy of 29 Nov 1580. State decoded, not read -> read for all five; class not read -> read.',
        'result': 'worked', 'technique': ['manual reconstruction', 'language-model scoring']})
    save('sauli1579', p)
    for s in steps:  # one step per save: the splice saver cannot insert two list items at one point
        p = load('sauli1579')
        p['solution'].append(s)
        save('sauli1579', p)


if __name__ == '__main__':
    globals()[sys.argv[1]]()
