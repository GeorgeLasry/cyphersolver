"""Re-read brief (REREAD_BRIEF.md), batch b02: fiesque1567 (BnF fr. 15919, 23 letters).

Targeted profile edits with the splice saver of relabel_r0.py (only changed spans are rewritten); several appends to
one list are saved one at a time (the saver mis-orders them otherwise).

    python research/reading_audit/reread_b02.py
"""
import sys
import pathlib

sys.path.insert(0, str(pathlib.Path(__file__).parent))
from relabel_r0 import load, save  # noqa: E402

DATE = '2026-10-22'
BY = 'Claude Opus 5.5'
F = 'fiesque1567'

DEC = 'built word by word from the key decode of the contributed transcription (Tomokiyo\'s key), reading through the known sign confusions'
MARG = 'the contemporary decipherment in the left margin, read from native IIIF crops, aligned clause by clause with the key decode'
# doc: (grade, review note, before clean share, after clean share)
READ = {
    '1567-10': ('B', f'{DEC}; image check of view 6. Holes: v007l c01, v008l c19-c24 fragments. The letter\'s first cipher page (view 6 right, about 22 lines) is not transcribed, so the reading starts mid-sentence.', '0.0', '0.72'),
    '1567-11-15': ('A', 'Follows the contemporary decipherment on view 23 right (f. 19r, "deschiffre de la precedente"), aligned with the key decode of view 22 right (83.8% letters agree); the part on view 23 left rests on the decipherment alone (cipher untranscribed). One cramped line not made out.', '0.0', '0.78'),
    '1568-01-21': ('B', f'{DEC}. One verb before "maintenir" open.', '0.0', '1.0'),
    '1568-02-15': ('B', f'{DEC}; the two cipher lines of view 37 right have a contemporary margin decipherment, which agrees word for word. Open: v038l c03-c04, c17-c18.', '0.0', '0.80'),
    '1568-03-06': ('B', f'{DEC}; the contributor\'s line reading (READING.en.md) used as a check. Open: f039r c08, c22-c23, c25-c27, c29; f039v c06, c10, c14; sign arrow in "comte [arrow]".', '0.0', '0.82'),
    '1568-03-27': ('B', f'{DEC}. Open: c04 and c13-c14.', '0.11', '0.64'),
    '1568-06-04': ('A', f'Follows {MARG} (margin found in this pass). One cramped word.', '0.0', '0.50 (Notes section included)'),
    '1568-06-12': ('B', f'{DEC}. Open: sign Dz in c01; lone ϖ twice as a code.', '0.0', '0.95'),
    '1568-07-17': ('B', f'{DEC}; all three pages (f. 79r rebuilt and checked against READING.en.md). Open: the name of the "sieur … grand escuyer", f. 79r c07-c08, c17; f. 79v c01-c03, c06-c08 (several holes); f. 80 c01, c07-c08.', 'f. 79r READING.en.md; f. 79v/80 0.0', '0.61'),
    '1568-08-14': ('B', f'{DEC}; all three pages (f. 94r checked against READING.en.md). Open: "lele" (f. 94 c12/c14/c21), the person after "devers", the port "gixes", a code before "et vous", f. 95 c12.', 'f. 94r READING.en.md; f. 94v/95 0.0', '0.72'),
    '1568-08-21': ('A', f'Follows {MARG} (about 40 short lines; not read before). Open: one word after "a sa volunté" and the clause before "qu\'il partira le quatriesme de septembre".', '0.0', '0.70'),
    '1568-09-04k': ('B', f'{DEC}. Open: f. 100r c17-c27 (mostly fragments), scattered holes in f. 100v c09-c13, f. 101 c16/c21/c25, f. 101v c05/c14/c19. The cipher addresses "Madame" (feminine "preste"), so it is to the Queen Mother though the docket says "au Roy".', '0.0-0.09', '0.73'),
    '1568-09-04q': ('B', f'{DEC}; image check of view 109 right c01-c05. Open: v109r c10-c11, v110l c24-c25, v110r c03, c05, c08.', '0.0-0.09', '0.68'),
    '1568-11-06': ('A', f'Rests on the key decode, which reads almost straight, and {MARG}; the margin supplies the opening. One verb before "six mil reistres" open.', '0.0', '0.58 (Notes section included)'),
    '1568-12-02': ('B', f'{DEC}. Open: "au duc [P fu q9 a]" (v130l c02), v130l c06, codes =ii and Dz.', '0.0-0.10', '0.63'),
    '1569-01-14': ('B', f'{DEC}. Open: v140r c08, v141l c03-c04, "comte ?" (v141l c15), the senses of =ii.', '0.0', '0.73'),
    '1569-03-02': ('B', f'{DEC}. Open: c07 (the authors of the false news).', '0.0', '0.72'),
    '1569-09-10': ('B', f'{DEC}. Open: v150l c17-c23 (about 6 holes in 60 words) and single words elsewhere.', '0.0', '0.63'),
    '1569-10-01': ('B', f'{DEC}. Open: a second name after "Chantonnay" (c06-c07).', '0.0', '0.81'),
    '1569-10-15': ('B', f'{DEC}. Open: one word ("au prejudice du [?]").', '0.0', '0.83'),
    '1569-10-20': ('B', f'{DEC}; image check of view 159 right c01-c02. Open: c04, the name of the feared attacker.', '0.17', '0.60'),
    '1569-10-29': ('B', f'{DEC}; READING.en.md used as a check (its "encline a clemence" is not carried by the figures). Open: c05, c22-c23.', '0.0', '0.77'),
    '1569-11-04': ('B', f'{DEC}. No holes; four words partly carried.', '0.0', '0.85'),
}
MARGIN_DOCS = {'1568-06-04': 'view 65 right', '1568-08-21': 'view 103 right', '1568-11-06': 'view 125 right'}


def main():
    p = load(F)
    o = p['outcome']
    for t in o['texts']:
        d = t['doc']
        grade, note, before, after = READ[d]
        t['state'] = 'read'
        t['reading'] = f'read/{d}_reading.md'
        t['translation'] = f'read/{d}_en.md'
        t['language'] = 'fr'
        t['note'] = (f'Re-read 22 Oct 2026 (batch b02): read/{d}_reading.md, read/{d}_en.md, log read/{d}_reread_log.md. '
                     f'docs/_check_reading.py clean share before {before}, after {after} (header comment counted; '
                     'old spellings outside the word list count as holes).')
        t['reading_review'] = {'grade': grade, 'by': BY, 'date': DATE, 'note': note}
        if d == '1567-10':
            t['label'] = '11 Oct 1567 (docket "11 octob. 1567"), to the Queen Mother (v007l, v007r, v008l, v008r; first cipher page on view 6 right not transcribed)'
        if d == '1568-09-04k':
            t['label'] = '4 Sep 1568 (docket "au Roy"; the cipher addresses "Madame"), f100, f100v, f101, f101v'
    for doc in p['documents']:
        if doc['id'] == '1567-10':
            doc['date'] = '11 Oct 1567'
            doc['shelfmark'] = 'BnF fr. 15919, views 6 right (cipher not transcribed) and 7-8 (Gallica btv1b90573568)'
        if doc['id'] in MARGIN_DOCS:
            doc['plaintext'] = {'location': ['margin'],
                                'source': f'contemporary decipherment in the left margin of {MARGIN_DOCS[doc["id"]]}, read 22 Oct 2026 (batch b02)',
                                'partial': False}
        if doc['id'] == '1567-11-15':
            doc['plaintext']['partial'] = False
            doc['plaintext']['source'] = ('contemporary decipherment on view 23 right (f. 19r), "deschiffre de la precedente", '
                                          'read in full 21-22 Oct 2026 (covers view 22 right and view 23 left)')
    o['fraction_read'] = 0.97
    o['fraction_read_method'] = 'estimated'
    o['fraction_read_source'] = (
        '22 Oct 2026, re-read (batch b02): all 23 letters build French sentences and are translated (read/<doc>_reading.md, '
        '_en.md; grades 4 A, 19 B). Signs of letters that read: the 29,707 transcribed signs, plus view 23 left (about 600 '
        'signs, untranscribed, read through its contemporary decipherment); not read: the first cipher page of the 11 Oct '
        '1567 letter on view 6 right (about 800 signs, untranscribed). 30,300 / 31,100, so estimated. Holes remain inside '
        'the readings (Remaining gaps); docs/_check_reading.py clean share per reading 0.50-1.0 with header and notes counted. '
        'Earlier figures: 0.056 (audit, 22 Oct), 0.997 signs with a value (withdrawn as a reading figure).')
    o['method_basis'] = (
        "Tomokiyo's reconstructed key, published for the letters of this volume, applied by the contributor to their own "
        "transcription; the project re-applied it, calibrated one letter against the volume's contemporary decipherment "
        "(83.8% of letters), and on 22 Oct 2026 built every letter into French sentences from the decode; four letters "
        "(15 Nov 1567, 4 Jun, 21 Aug and 6 Nov 1568) follow contemporary decipherments found in the volume (view 23 right "
        "and the margins of views 65, 103 and 125 right).")
    o['notes'] = (
        'Contributed AI-only transcription (Claude + Codex), no human check. 22 Oct 2026: all 23 letters re-read into French '
        'sentences and translated (19 from the key decode, 4 after contemporary decipherments, three of them in margins '
        'not recorded before); class stays read in part: holes in several letters are workable by sign-level image checks, '
        'and the first cipher page of the 11 Oct 1567 letter (view 6 right) is untranscribed.')
    o['gaps'] = [
        {'item': 'View 6 right, first cipher page of the 11 Oct 1567 letter (about 22 lines, about 800 signs)', 'blocker': 'not-attempted',
         'detail': 'not in the contributed transcription; image good; transcribe and decode with the volume key'},
        {'item': 'View 23 left (f. 18v) cipher, second page of the 15 Nov 1567 letter', 'blocker': 'not-attempted',
         'detail': 'read through the contemporary decipherment on view 23 right; the cipher itself is untranscribed, and one cramped decipherment line ("gens de Flandres ... Chantonnay") would be closed by decoding it'},
        {'item': 'Phrase-level holes: f. 79v c01-c08 and f. 80 c07-c08 (17 Jul 1568); f. 100r c17-c27 (4 Sep 1568 k); v150l c17-c23 (10 Sep 1569); v038l c03-c04, c17-c18; f039r c22-c29; single words in the other letters (read/<doc>_reread_log.md)', 'blocker': 'not-attempted',
         'detail': 'AI-only transcription; workable by sign-level crops of those lines and re-decoding'},
        {'item': 'Lone signs standing as codes, values not settled: ϖ (l\'Empereur or le Roy), =ii (King of Spain / Landgrave / mm), Dz, mm, pp (King of Spain?), arrow, "lele"; code 16 = ce or vostre', 'blocker': 'open-codes',
         'detail': 'not in Tomokiyo\'s table; read from context in read/*_reread_log.md; key.tsv unchanged'},
    ]
    save(F, p)
    for c in ['sender or date identified']:
        p = load(F)
        if c not in p['outcome']['contribution']:
            p['outcome']['contribution'].append(c)
            save(F, p)
    p = load(F)
    v = p['outcome']['verification']
    if 'contemporary decipherment' not in v:
        v.append('contemporary decipherment'); save(F, p)
    steps = [
        {'date': DATE, 'kind': 'access',
         'what': 'Contact sheet of all 34 cipher views at reduced size (openapi.bnf.fr IIIF), then native crops of the margins: views 65, 103 and 125 right carry contemporary decipherments of their cipher in the left margin (65 not recorded before); view 37 right has a two-line margin decipherment; view 6 right holds an untranscribed first cipher page of the 11 Oct 1567 letter.',
         'result': 'worked', 'technique': ['manual reconstruction']},
        {'date': DATE, 'kind': 'transcription',
         'what': 'The rest of the contemporary decipherment on view 23 right (matching view 23 left) and the three margin decipherments (views 65, 103, 125 right) transcribed from native IIIF crops and aligned with the key decode; they agree clause by clause.',
         'result': 'worked', 'technique': ['plaintext matching', 'manual reconstruction']},
        {'date': DATE, 'kind': 'reading',
         'what': 'The other 19 letters built word by word into French from the key decode (decoded_*.txt), reading through the known sign confusions, with a few image checks (views 6, 37, 109, 159); translated. All 23 letters read (4 grade A, 19 B); docs/_check_reading.py clean share before 0.0-0.17 per page, after 0.50-1.0 per reading.',
         'result': 'worked', 'technique': ['contextual inference', 'manual reconstruction']},
        {'date': DATE, 'kind': 'hypothesis',
         'what': 'Sign values from the readings: a lone ϖ (and "pi") stands for l\'Empereur (confirmed by the margins of views 65 and 103) or le Roy; 16 fits "vostre" in the 1569 letters to the King; H# = ss in ambassadeur/commissaires/asseurer, o elsewhere; =ii stands for a person (King of Spain, once the Landgrave). Not entered in key.tsv.',
         'result': 'partial', 'technique': ['contextual inference']},
        {'date': DATE, 'kind': 'reading',
         'what': 'Phrase-level holes left open without image checks: 17 Jul 1568 f. 79v and f. 80, 4 Sep 1568 f. 100r c17-c27, 10 Sep 1569 v150l c17-c23, 15 Feb 1568 v038l c03-c04/c17-c18, 6 Mar 1568 f. 39r c22-c29.',
         'result': 'partial', 'technique': ['contextual inference']},
    ]
    for st in steps:
        p = load(F); p['solution'].append(st); save(F, p)


if __name__ == '__main__':
    main()
