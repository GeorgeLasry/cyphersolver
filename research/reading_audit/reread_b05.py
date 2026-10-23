"""Re-read brief (REREAD_BRIEF.md), batch b05: schenck1706 (Vienna agent "Sidon" to Baron Schenck, DECODE R7486-R7500).

Targeted profile edits with the splice saver of relabel_r0.py; one save per appended solution step. All fifteen
outcome.texts entries share doc "R7486-R7500", so they are told apart by the record number at the head of the label.

    python research/reading_audit/reread_b05.py
Helpers: b05_fetch.py (DECODE images to the scratchpad), b05_crop.py (page strips), b05_dec.py (run decoder),
b05_align.py (word-by-word check of each reading), b05_score.py (clean-sentence share of a reading body).
"""
import re
import sys
import pathlib

sys.path.insert(0, str(pathlib.Path(__file__).parent))
from relabel_r0 import load, save  # noqa: E402

F = 'schenck1706'
DATE = '2026-10-22'
BY = 'Claude Opus 5.5'
BASIS = ('the transcription transcr/R74xx.txt re-read line by line on the full-resolution DECODE images (22 Oct 2026, '
         'corrections in reading/R74xx_corrections.tsv), the letter table of key.py for the runs and the code values of '
         'codes_key.json; aligned word by word with the transcription, the corrections and the run decodes '
         '(research/reading_audit/b05_align.py), supplied words bracketed. No contemporary decipherment, clear copy or '
         'edition exists. Log: reading/R7486-R7496_reread_log.md')

READ = {
    'R7491': ('B', 'Vienna, 22 May 1706. Schenck\'s letters of 12 and 15 May arrived; Radomsky\'s Liegnitz proposal; the '
                   'imperial court\'s caution towards Sweden; how future letters to [181] are to be named; Herr von '
                   'Heinisch\'s thanks; the Viennese newspapers (Mercurius, Diarium); Hagenau lost, Barcelona relieved, '
                   'Alcantara taken, Galloway before Madrid; the Bishop of Raab\'s palace; the Emperor back from '
                   'Laxenburg. Clean share 0.609 (0.674 with dates counted as words). Holes: person codes (181, 187, 190, '
                   '122, 134, 231, 233, 262, 349, 81 ...), the signs 3., d., e., c., oo, and a faded P.S.'),
    'R7494': ('B', 'Vienna, 5 June 1706. Progress in Brabant, profitable for King Augustus, a blow to Swedish designs; '
                   '[187]\'s excuses for writing little; [258]\'s talk of a rumour about the King; P.S. an enclosure for '
                   'Court Referendary Pfingsten. Clean share 0.611. Holes: person codes (187, 181, 258, 157, 166, 208, '
                   '268 ...), the signs d., e., oo, and three probable words.'),
}

UNREAD = {
    'R7486': 'clean share 0.29: the clear German now reads (corrections: "abermahls", "zu dero Wagen", the P.S. "nec '
             'superiorem, nec parem, aut inferiorem"), but most sentences hold two to four open codes or signs (190, 181, '
             '187, 166, 3., e., oj ...) and three runs give no word (gutswor, sollwiglaufeenden, contair)',
    'R7488': 'clean share 0.556: the clear text and runs now read ("auf morgen oder übermorgen festgestellet", "Plessen", '
             '"eine convoy"); one sentence ("Es seÿ 181 dei präsumption ob wir ... 254 e 352 ... 526") stays a string '
             'of codes and short words',
    'R7489': 'clean share 0.545, 0.636 with the clear-text numerals (6000, 25 m., 400 ...) counted as words: almost all '
             'clear German, read on the images (the Lehen affair, the battle at Montechiaro, Rákóczi, Denmark and '
             'Sweden, the Bavarian and Cologne ban patents); holes are the codes 166, 187, 190, 562, 181, 131 and a few '
             'faded words at the foot of p. 2 and p. 3',
    'R7490': 'clean share 0.551: the clear German reads (Landau, Haguenau, Barcelona, Leake, King Charles, Glogau, '
             'Ogilvy, Baron Kleinburg, the malevoli), but the cipher passages on pp. 4-6 are strings of open codes and '
             'signs (181 e 340, 3. 452, 28 o 61 3. ... 526 d. 341) and four lines on p. 2 and the marginal P.S. are '
             'faded',
    'R7492': 'clean share 0.371: the clear text reads (the "âmes ignobles, basses et rampantes" insult, Agent Bell, '
             'Barcelona, the cardinal in pectore, Radoniski and Liegnitz, the Duke of Courland), but its sentences are '
             'dense with open codes and signs (189 o. 187, c. 157 527 d. 349, 3. 355 d. 349, 206, 500)',
    'R7493': 'clean share 0.23: the upper halves of all eight pages now read (Mazarin and Richelieu, the baronial '
             'diploma, Barcelona, Toulouse, Anjou, Berwick, Galloway in Madrid, the Pressburg congress), but the '
             'tide-marked lower halves of ff. 303v-304 and the faded feet of ff. 305v-306v stay unread on the DECODE '
             'images',
    'R7496': 'clean share 0.421: the letter reads as German (the Emperor\'s resolve to live free of vanities, the '
             'advice to choose a confidant under the seal of silence, the French and the Great Elector as examples); '
             'the holes are the codes 132, 181, 193, 187, 307, 809, 180, 166, the signs e. and a., and Latin and French '
             'words outside the German word list',
}


def rec_of(t):
    return re.match(r'(R\d{4})', t['label']).group(1)


STEPS = [
    {'date': DATE, 'kind': 'access',
     'what': 'Re-read (REREAD_BRIEF, batch b05): the 32 DECODE page images of R7486, R7488-R7494 and R7496 fetched with '
             'the project cookie (research/reading_audit/b05_fetch.py; scratchpad only, not in the repository). No '
             'contemporary decipherment beyond the recipient\'s superscripts (R7486) and gloss (R7493), no clear copy, '
             'no edition (searched 9 Oct 2026).',
     'result': 'worked', 'technique': ['other']},
    {'date': DATE, 'kind': 'transcription',
     'what': 'The [?] words of the nine letters re-read line by line on page strips at 1,700 px (b05_crop.py; margins '
             'rotated, one contrast-enhanced crop): about 170 corrections in reading/R74xx_corrections.tsv. The earlier '
             '"illegible" was mostly a hard hand, not lost ink: R7489 and R7493 read largely; only some page feet are '
             'faded. Code 131 (not 181) in R7489; runs re-decoded with the key unchanged (R7488 "morgen oder '
             'übermorgen", "Plessen", "eine convoy"; R7496 "von vanitäten").',
     'result': 'worked', 'technique': ['manual reconstruction']},
    {'date': DATE, 'kind': 'reading',
     'what': 'Readings built sentence by sentence for the nine letters (reading/R74xx_reading.md, English R74xx_en.md) '
             'and checked word by word against the transcription, the corrections and the run decodes '
             '(b05_align.py), which caught normalised or invented words, all corrected (e.g. R7491 "also sinister": the '
             'figures give the end of "proposition"; R7490 "cauta" for the written "Cives"). Clean share of the reading '
             'bodies (b05_score.py): R7491 0.609, R7494 0.611 (read); R7486 0.29, R7488 0.556, R7489 0.545 (0.636 with '
             'clear-text numerals counted as words), R7490 0.551, R7492 0.371, R7493 0.23, R7496 0.421 (decoded, not '
             'read: open person codes and dotted signs in most sentences; R7493 also faded).',
     'result': 'partial', 'technique': ['manual reconstruction', 'contextual inference', 'language-model scoring']},
]


def main():
    p = load(F)
    o = p['outcome']
    for t in o['texts']:
        r = rec_of(t)
        if r in READ:
            g, note = READ[r]
            t['state'] = 'read'
            t.pop('note', None)
            t['reading'] = 'reading/%s_reading.md' % r
            t['translation'] = 'reading/%s_en.md' % r
            t['language'] = 'de'
            t['reading_review'] = {'grade': g, 'by': BY, 'date': DATE, 'note': note + ' Rests on ' + BASIS + '.'}
        elif r in UNREAD:
            t['reading'] = 'reading/%s_reading.md' % r
            t['translation'] = 'reading/%s_en.md' % r
            t['note'] = ('Re-read 22 Oct 2026 (batch b05; reading/%s_reading.md, _en.md, R7486-R7496_reread_log.md): '
                         % r) + UNREAD[r] + '. Blocker: ' + (
                'illegible (faded, tide-marked lower halves on the DECODE images) and no-key-material (codes).'
                if r == 'R7493' else 'no-key-material for the person codes and signs.')
    o['fraction_read'] = 0.458
    o['fraction_read_method'] = 'estimated'
    o['fraction_read_source'] = (
        '22 Oct 2026, re-read batch b05: cipher numbers of the letters that read / all, counted as every standalone '
        'number on the transcription lines of transcr/R7486-R7500.txt (comments and bracketed notes left out; a rough '
        'count, dates included): 640 / 1,397 (R7487, R7491, R7494, R7495, R7497-R7500 read). Before: 0.34 (estimated, '
        'reading audit, 663 of 1,956 on a looser count). Withdrawn as a reading figure: 0.636 (measure.py, numbers in '
        'runs giving sense plus valued codes and signs over 1,361 cipher tokens) and fraction_coherent 0.935.')
    o['fraction_coherent'] = 0.458
    new_gaps = [
        {'item': 'Schenck letters: R7486, R7488, R7489, R7490, R7492, R7496 decoded, not read (clear text read on the '
                 'images 22 Oct 2026; clean share 0.29-0.556)', 'blocker': 'no-key-material',
         'detail': 'the sentences break on the open person codes and dotted signs listed above; R7489 reaches 0.636 '
                   'when its clear-text numerals are counted as words'},
        {'item': 'Schenck letters: R7493 lower halves of ff. 303v-304 and feet of ff. 305v-306v', 'blocker': 'illegible',
         'detail': 'faded and tide-marked on the DECODE images; the original (Archiwum Narodowe w Krakowie, AKM 21 '
                   'plik 30/1) might read better'},
    ]
    save(F, p)
    for g in new_gaps:  # one save per appended item (the saver misorders several appends to one list)
        p = load(F)
        if any(x['item'] == g['item'] for x in p['outcome']['gaps']):
            continue
        p['outcome']['gaps'].append(g)
        save(F, p)
    for s in STEPS:
        p = load(F)
        if any(x.get('what') == s['what'] for x in p['solution']):
            continue
        p['solution'].append(s)
        save(F, p)
    print('done')


if __name__ == '__main__':
    main()
