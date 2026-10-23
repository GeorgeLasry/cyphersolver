"""Re-read brief (REREAD_BRIEF.md), batch mix1: castelcicala1816, selve1535, walsingham1585, nevers1593, nevers1574.

Targeted profile edits with the splice saver of relabel_r0.py (only changed spans are rewritten).

    python research/reading_audit/reread_mix1.py <folder>
"""
import sys
import pathlib

sys.path.insert(0, str(pathlib.Path(__file__).parent))
from relabel_r0 import load, save  # noqa: E402

DATE = '2026-10-22'
BY = 'Claude Opus 5.5'


def step(p, what, result, kind='reading', technique=('manual reconstruction', 'crib testing')):
    p['solution'].append({'date': DATE, 'kind': kind, 'what': what, 'result': result,
                          'technique': list(technique)})


def texts(p, doc, label_part=None):
    out = []
    for t in p['outcome']['texts']:
        d = t.get('doc')
        if d == doc and (label_part is None or label_part in t.get('label', '')):
            out.append(t)
    return out


def nevers1593():
    p = load('nevers1593')
    t, = texts(p, 'f168')
    t['transcription'] = ['ct_3986_f168.txt', 'ct_3986_f168_r2.txt', 'texts/f168_corrections.tsv']
    t['decryption'] = ['decode_f168.txt', 'texts/f168_reading.md', 'texts/f168_en.md']
    t['note'] = ('Re-read 22 Oct 2026 (texts/f168_reread_log.md): figures re-read on the IIIF image, 14 corrections '
                 '(bars mis-assigned, segmentation; ct_3986_f168_r2.txt). Lines 1-3 and 6-7 now read as sentences '
                 '("Je luy ay demandé come [...] le Pape voloit que j\'y alase; elle m\'a dit n\'avoir autre charge, ne '
                 'me declarans que j\'y alle ou non"; "Ce qu\'il faict tenir segret, et le faire savoir a [Gondi]"); '
                 'lines 4, 5 and the last line keep holes (about half the sentences hold; _check_reading 0.30 on the '
                 'reading text). Blocker: the figures are legible but the register copy is corrupt there (dropped and '
                 'swapped figures, 24 for 34, 27 for 29), and there is no second witness (no decipherment, original or '
                 'edition) to restore them.')
    o = p['outcome']
    o['fraction_read_source'] = (o['fraction_read_source'] + ' Re-read 22 Oct 2026 (batch mix1): f. 168 improved but '
                                 'still decoded, not read, so the figure is unchanged.')
    step(p, 'Re-read of f. 168 under REREAD_BRIEF (batch mix1): no decipherment, original or edition of the letter; '
            'figures re-read on the openapi.bnf.fr IIIF image at 1.4-2.2x, 14 transcription corrections (bars over 38 '
            'ne, 56 je, 68 faire, 26+52 par-le-r, 36 non; 18 not 1 0 8; 57 12 not 58 71), copy slips identified (24 '
            'for a, 27 for 29). Lines 1-3 and 6-7 read as sentences; lines 4, 5 and the last line keep holes in '
            'corrupt figures. Stays decoded, not read (texts/f168_reading.md, f168_en.md, f168_reread_log.md).',
         'partial')
    save('nevers1593', p)


def nevers1574():
    p = load('nevers1574')
    t, = texts(p, 'f15')
    t['state'] = 'read'
    t.pop('note', None)
    t['transcription'] = ['f15_signs.tsv', 'f15_gloss.md']
    t['decryption'] = 'f15_reading.md'
    t['reading'] = 'f15_reading.md'
    t['translation'] = 'f15_en.md'
    t['language'] = 'fr'
    t['summary'] = ('The duchess tells her husband that Pignerol and Savillan have been handed to the Duke of Savoy, to '
                    'the contentment of the King and the Queen Mother, so that Nevers is left without his government; '
                    'her exchange with the Queen Mother (who first approves warning him, then says he does not lose '
                    'his government) and her tears; a report to the King that Nevers had written of a league of four '
                    'or five near the King; promises of the next vacant government (Picardy, Languedoc); his friends '
                    'say he would harm himself by keeping the reduced government. Cipher continues on f. 16r (19 '
                    'lines), then a clear closing: it is midnight, she would rather be in paradise.')
    t['reading_review'] = {
        'grade': 'B', 'by': BY, 'date': DATE,
        'note': ('f15_reading.md: the contemporary interlinear gloss (f15_gloss.md) and a mechanical decode of the '
                 'cipher signs (f15_signs.tsv, alphabet f15_key.md rebuilt from gloss-sign alignment) agree word for '
                 'word on f. 15r and f. 16r; 70 cipher lines. f. 15r and the f. 16r cipher read as continuous French '
                 '(4 holes in 402 tokens); f. 15v ll. 2-5 are overwritten and their gloss faded (illegible), with a '
                 'dozen single groups open further down, 50 holes in 224 tokens. _check_reading on the reading body: '
                 '46 of 57 sentences clean (0.81).')}
    o = p['outcome']
    o['class'] = 'read in part'
    o['key'] = 'recovered'
    o['key_file'] = 'f15_key.md'
    o['method_basis'] = ("f. 21 was read from the complete contemporary clear copy under Birago's cipher flap. f. 15 "
                         "(with its continuation on f. 16r) was read from its contemporary interlinear decipherment, "
                         "checked against a mechanical decode with the alphabet rebuilt from gloss-sign alignment "
                         "(close to, but not, the 1584 Nevers no. 2 alphabet: e=F, q and s=9, d=b-shape, m=+, t=4, a "
                         "doubling sign, name signs for Roy, Royne mere, Royne).")
    # several items appended to a one-line list in one save come out reversed (relabel_r0 splice), so one per save
    for c in ('transcription', 'key recovered'):
        if c not in o['contribution']:
            o['contribution'].append(c)
            save('nevers1574', p)
    o['fraction_read'] = 0.94
    o['fraction_read_method'] = 'measured'
    o['fraction_read_source'] = ('22 Oct 2026, re-read (batch mix1): both documents now read. Tokens: f. 21 clear copy '
                                 '271 words, all read; f. 15-16 cipher 626 tokens in f15_reading.md (70 cipher lines; '
                                 'the 84 words of the clear closing excluded), of which 54 are [...] holes (50 on f. '
                                 '15v). (271 + 572) / (271 + 626) = 0.94. Withdrawn: 0.3 (page-weighted estimate of '
                                 'the reading audit, before f. 15 was read).')
    o['notes'] = ('Both leaves preserve their own reading aids: f. 21 a clear copy under the flap, f. 15 an interlinear '
                  'decipherment, used with a rebuilt alphabet. f. 15v ll. 2-5 stay illegible on the best image.')
    o['verification'] = ['contemporary decipherment', 'independent clear copy', 'key confirms']
    o['gaps'] = [
        {'item': 'f. 15v ll. 2-5 and the gloss-only line at its head (about 70 words)', 'blocker': 'illegible',
         'detail': 'the decipherer wrote over the cipher signs and the gloss above is faded or struck; the original or '
                   'a multispectral image might recover them'},
        {'item': 'about a dozen single groups on f. 15v (ll. 7, 10, 12-16, 20-23) and f. 16r (ll. 1, 14)',
         'blocker': 'illegible', 'detail': 'neither the signs nor the faded gloss settle them'},
        o['gaps'][2]]
    step(p, 'Re-read of f. 15 under REREAD_BRIEF (batch mix1): the interlinear gloss transcribed line by line on the '
            'Gallica native images (f15_gloss.md), the cipher signs transcribed (f15_signs.tsv, 70 lines; f. 16r '
            'lines 1-19 found to continue the cipher) and decoded with an alphabet rebuilt from gloss-sign alignment '
            '(f15_key.md). Gloss and decode agree word for word on f. 15r and f. 16r; f. 15v ll. 2-5 illegible. '
            'f. 15 relabelled read (f15_reading.md, f15_en.md, f15_reread_log.md).', 'worked',
         technique=('crib testing', 'manual reconstruction', 'plaintext matching'))
    save('nevers1574', p)


def selve1535():
    p = load('selve1535')
    t, = texts(p, 'R3697', 'runs struck through')
    new = {
        'doc': 'R3697',
        'label': ('R3697, BnF fr. 3091 f. 25r-v: the struck runs glossed by the King’s decipherer (f. 25r A, B, C1 '
                  'with the head of C2; f. 25v T2)'),
        'transcription': 'R3697_signs.txt',
        'decryption': 'READING_R3697_struck.md',
        'reading': 'READING_R3697_struck.md',
        'translation': 'R3697_struck_en.md',
        'summary': ('Read from the decipherer’s interlinear and marginal glosses, checked against the struck signs '
                    'where they separate from the strike: "au marchant"; "ung sansacque cy prochain"; "Il a consumé '
                    'ses facultez et la plus part de ses amys [...] et grand du T[urc]"; "amiablement pour la charge '
                    'qu’il a de Vesprim de la guerre en luy".'),
        'reading_review': {
            'grade': 'B', 'by': BY, 'date': DATE,
            'note': ('READING_R3697_struck.md: the four glossed runs (169 signs) read as French clauses from the '
                     'contemporary glosses; signs agree where visible (A 11/11, B prochain 8/8, C2 head by the key, T2 '
                     'about 50 of 64); C1 rests on the gloss alone (the strike hides its signs); one blurred group in '
                     'the C1 gloss stays a hole.')},
        'language': 'fr',
        'state': 'read'}
    t['label'] = ('R3697, BnF fr. 3091 f. 25r-v: the struck runs with no legible gloss (C2 after "et gran[d]", C3, T1, '
                  'T3; 135 signs)')
    t['decryption'] = 'READING_R3697_struck.md'
    t['note'] = ('Re-read 22 Oct 2026 (R3697_struck_reread_log.md): the glossed struck runs were split off and read '
                 'from the decipherer’s glosses; these 135 signs have no gloss, or a gloss that is illegible where '
                 'they need it (f. 25v margin lines 1-2, 6-7), and the strike crosses the x-height of every sign on '
                 'the only (film) image. Fragments only: "avoit", "on fait ... contre ses", "-tretienent". Blocker: '
                 'illegible; a colour or multispectral image, or the original, would separate the lighter strike ink.')
    o = p['outcome']
    o['fraction_read'] = 0.946
    o['fraction_read_source'] = ('22 Oct 2026, re-read (batch mix1): non-null signs in R3697_signs.txt and '
                                 'R4232_signs.txt in documents that read: R4232 1,430, R3697 unstruck 747, R3697 '
                                 'struck runs read from the decipherer’s glosses (A, B, C1, C2 head, T2) 169; the '
                                 'other struck runs (135) are decoded, not read. 2,346 of 2,481 = 0.946. Withdrawn: '
                                 '0.877 (reading audit, before the glossed struck runs were counted as read from the '
                                 'glosses); 0.899 (sense.py, 5 Oct 2026).')
    o['gaps'][0] = {'item': 'R3697 struck runs with no legible gloss: C2 tail, C3, T1, T3 (135 signs)',
                    'blocker': 'illegible',
                    'detail': ('the decipherer’s ruling runs through every sign on the only (film) images and the '
                               'f. 25v margin gloss is illegible where these runs need it; a colour image or the '
                               'original would separate the lighter strike ink. The glossed runs A, B, C1, T2 are '
                               'read from the glosses (READING_R3697_struck.md).')}
    p['outcome']['texts'].append(new)
    step(p, 'Re-read of the R3697 struck runs under REREAD_BRIEF (batch mix1): the decipherer’s glosses taken as the '
            'contemporary decipherment they are; C1 gloss re-read on native_f27.jpg (one blurred group left); the '
            'glossed runs A, B, C1 + C2 head, T2 (169 signs) set out as text and checked against the pass-3 sign '
            'alignments, split off as read (READING_R3697_struck.md, R3697_struck_en.md); C2 tail, C3, T1, T3 (135 '
            'signs) stay decoded, not read (no legible gloss, strike over every sign).', 'partial',
         technique=('crib testing', 'plaintext matching'))
    save('selve1535', p)


def walsingham1585():
    p = load('walsingham1585')
    t, = texts(p, 'R4844')
    t['transcription'] = ['reading_R4844.txt', 'reading_R4844_r2.txt', 'texts/R4844_sign_words.md']
    t['decryption'] = ['reading_R4844_r2.txt', 'clear_gaps_pass2.md']
    t['note'] = ('Re-read 22 Oct 2026 (texts/R4844_reread_log.md): no decipherment exists (Wotton’s interlinear '
                 'one is blotted), CSP Scotland viii does not calendar the letter, and the DECODE images are behind '
                 'the login and not in the checkout. The 14 Oct gap readings (clear_gaps_pass2.md) were merged into '
                 'reading_R4844_r2.txt (_check_reading 0.45 -> 0.50), but every sentence of the body still carries a '
                 'sign word (11 groups, about 120 signs, homophonic with nulls, no crib, no key: too short) or an '
                 'open name code (13, 14, 23, 30, 32, 37). Fragments only.').encode().decode('unicode_escape')
    step(p, 'Re-read of R4844 under REREAD_BRIEF (batch mix1): no decipherment, edition or calendar entry; DECODE '
            'images out of reach; the unmerged 14 Oct gap readings merged into reading_R4844_r2.txt (sentence check '
            '0.45 -> 0.50). Sign words and open codes still in nearly every sentence: stays decoded, not read.',
         'failed', technique=('manual reconstruction',))
    save('walsingham1585', p)


def castelcicala1816():
    p = load('castelcicala1816')
    common = ('Re-read 22 Oct 2026 (reread_log.md): no contemporary gloss on this record (only R9566 p. 3, R9569, R9571, '
              'R9589 have one), no edition, no code book online. key.tsv gives a value to {share} of its groups and '
              'the longest run of known groups is {run}, so an unknown group falls inside nearly every clause; a hand '
              'retry on the best unglossed stretch (R9566 p. 3 ll. 10-14) fixed no new value. Blocker: '
              'no-key-material (the 1816-19 Cifra della Segreteria di Stato, ASNa Esteri).')
    stats = {'R9553': ('0.40', 5), 'R9554': ('0.49', 14), 'R9555': ('0.43', 5), 'R9556': ('0.42', 5),
             'R9557': ('0.38', 5), 'R9558': ('0.21', 5), 'R9559': ('0.43', 9), 'R9560': ('0.19', 3),
             'R9561': ('0.40', 12), 'R9562': ('0.36', 5), 'R9563': ('0.51', 9), 'R9564': ('0.50', 10),
             'R9565': ('0.53', 12), 'R9567': ('0.58', 12), 'R9570': ('0.56', 5), 'R9579': ('0.49', 8),
             'R9582': ('0.46', 5), 'R9583': ('0.60', 11), 'R9584': ('0.63', 4), 'R9585': ('0.44', 5),
             'R9587': ('0.27', 3)}
    for t in p['outcome']['texts']:
        d = t['doc']
        if t.get('state') != 'decoded, not read':
            continue
        if d in stats:
            sh, run = stats[d]
            t['note'] = common.format(share=sh, run=run)
        elif d == 'R9566':
            t['note'] = ('Re-read 22 Oct 2026 (reread_log.md): the contemporary gloss covers only p. 3 ll. 1-9, one '
                         'sentence (Decazes, Onís, the Floridas and Cuba); the other five pages (with the fragment in '
                         'another hand) have no gloss and key.tsv gives a value to 0.56 of the groups. A hand retry on '
                         'the unglossed continuation (p. 3 ll. 10-14: "desidera della Francia [..] e la [..] ... la '
                         'Spagna ...") left 17 of 37 groups open and fixed no new value. Blocker: no-key-material.')
        elif d == 'R9569':
            t['note'] = ('Re-read 22 Oct 2026 (reread_log.md): the gloss of p. 1 ll. 8-16 gives one sentence through '
                         'the decipherer’s syllable splits ("... ed io ho motivo di credere di no, e che [...] la '
                         'suddetta elezione la Francia gli darebbe l’esclusiva"); p. 1 ll. 1-7 and p. 2 (out of '
                         'focus) have no gloss and decode at the usual half coverage (0.68 overall). One sentence of '
                         'about ten. Blocker: no-key-material.')
    step(p, 'Re-read of the 23 decoded-not-read despatches under REREAD_BRIEF (batch mix1): every transcript checked '
            'for a gloss (none beyond R9566 p. 3, R9569, R9571, R9589), no edition, code book not online; coverage '
            'and longest known run measured per document (0.19-0.68; runs of 3-14 groups outside the glosses); hand '
            'retry on R9566 p. 3 ll. 10-14 against the Floridas crib fixed no new value (17 of 37 groups open). All '
            '23 stay decoded, not read; blocker no-key-material (reread_log.md).', 'failed',
         technique=('crib testing', 'contextual inference'))
    save('castelcicala1816', p)


if __name__ == '__main__':
    globals()[sys.argv[1]]()
