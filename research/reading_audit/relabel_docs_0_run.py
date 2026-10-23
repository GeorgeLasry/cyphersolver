"""Second-wave relabel (RELABEL_DOCS_BRIEF.md) for the targets in relabel_docs_0.txt, 22 Oct 2026.

Uses relabel_docs_0.py (a copy of relabel_r0.py: splices only the changed spans of each profile.json).
Run once:  PYTHONUTF8=1 python research/reading_audit/relabel_docs_0_run.py [folder ...]
"""
import sys
from relabel_docs_0 import relabel, BY, DATE

A = 'reading audit, 22 Oct 2026'


def gaps_add(*gs):
    def f(p):
        o = p['outcome']
        o.setdefault('gaps', [])
        for item, blocker, detail in gs:
            if not any(g.get('item') == item for g in o['gaps']):
                o['gaps'].append({'item': item, 'blocker': blocker, 'detail': detail})
    return f


def chain(*fs):
    def f(p):
        for g in fs:
            g(p)
    return f


def note_add(text):
    def f(p):
        o = p['outcome']
        o['notes'] = (o.get('notes', '').rstrip() + ' ' + text).strip()
    return f


def run(name):
    if name == 'adfgvx':
        def split(p):
            t = p['outcome']['texts']
            e = t[0]
            e['label'] = ('22 ADFGVX messages, Childs pages 73-217 (Nov 1918): the nine read in full (pp. 100, 105, 109, '
                          '132, 146, 171, 176, 187 part 1 and its part 2 AFAFF)')
            e['state'] = 'read'
            e['reading_review'] = {'grade': 'B', 'by': BY, 'date': DATE, 'note': (
                'The nine full readings are German telegrams in capitals with X as stop (the 2017 Cipherbrain readers\'); '
                'each builds sentences and translates, e.g. p. 171 "In Ukraine und Polen Rubelkurse stark steigend infolge '
                'Bruches zwischen Deutschland und Sowjetregierung". The per-document audit graded the whole table C because '
                'the other thirteen messages are in the same file; they are now a separate entry.')}
            new = {k: e[k] for k in ('doc', 'transcription', 'decryption') if k in e}
            new['label'] = ('the same file: three messages read only in part (p. 164 F-G-X, p. 164 VFGAG, VGADA p. 215) and '
                            'ten with no reading (pp. 73, 152, 153 VFVAX and AXVAA, 158, 170, 176 GGDAA, 189, 198, 217)')
            new['summary'] = ('Thirteen of the 22 residue messages: three give fragments joined by "..." (Temesvar, Mirco, the '
                              'Entente fleet at Kertsch with New Zealand, English and French divisions); ten have no reading, '
                              'because no published period key fits them and several carry marked transmission gaps.')
            new['language'] = 'de'
            new['state'] = 'decoded, not read'
            new['note'] = ('Three partial readings with gaps in most sentences and ten messages with no reading at all '
                           '(shown as "-"); not counted as a reading (' + A + ').')
            t.insert(1, new)
        relabel('adfgvx', lang='de', cls='read in part', fraction=0.49,
                fraction_source=('texts/residue22_decryption.md, letters per message (marked gaps excluded): the nine messages '
                                 'that read hold 1,945 of the 3,966 letters (0.490); the three partial (531 letters) and ten '
                                 'open (1,490) count as unread. The earlier "unknown" left the field unmeasured.'),
                extra=chain(split, gaps_add(
                    ('ten open messages (pp. 73, 152, 153 x2, 158, 170, 176 GGDAA, 189, 198, 217; 1,490 letters)', 'no-key-material',
                     'no published period key fits, including Lasry\'s CHI key; the block-edit search allows two insertions or one '
                     'deletion; heavier mutilation or an unlisted key needs the Childs originals'),
                    ('three partly read messages (p. 164 F-G-X, p. 164 VFGAG, VGADA p. 215)', 'needs-physical-access',
                     'marked transmission gaps (44, 44 and 11 letters) in the printed transcription; the lost letters need the '
                     'Childs originals')),
                    note_add('22 Oct 2026, reading audit: the readings table split into two entries, the nine messages that '
                             'read (state read) and the thirteen partial or open ones (decoded, not read); class already solved '
                             '-> read in part, fraction_read 0.49 by letters.')),
                step=('Reading audit, per-document pass (George Lasry\'s sentence test): texts/residue22_decryption.md read '
                      'message by message. The nine full readings build German sentences; the three partial readings have '
                      '"..." gaps in most sentences and ten messages have no reading. The entry split into a read entry and a '
                      'decoded, not read entry; class already solved -> read in part; fraction_read unknown -> 0.49 (letters).'),
                step_result='partial')

    elif name == 'alessandrino1568':
        why = ('Beam-search output under Lasry\'s polyphonic key: {} (' + A + '); fix: re-read the letter against the images '
               'and DECODE transcription, constraining the digit choices word by word.')
        relabel('alessandrino1568', lang='it', cls='read in part', fraction=0.667,
                fraction_source=('texts/R*_decryption.txt, the "(N items" page headers: the seven letters that read (R93, R96, '
                                 'R97, R98, R99, R102, R115) hold 7,036 of the 10,555 items (0.667, padding runs included); '
                                 'R94, R95, R100 and R101 (3,519 items) are decoded, not read. The field was "unknown" before.'),
                states={'R94': ('decoded, not read', why.format('the jurisdiction theme reads at the opening, but words are '
                                                                  'corrupted mid-sentence (liberagemptume, masibennrianuareliabtsicresciutimenoi)')),
                        'R95': ('decoded, not read', why.format('about half intelligible; long noise stretches (laretscs[04.]c, '
                                                                  'desersaleaniosina) leave holes in most sentences')),
                        'R100': ('decoded, not read', why.format('a short page; the Catalonia theme is clear but most sentences '
                                                                   'have holes (dingaeldetpie) and it ends in ??????')),
                        'R101': ('decoded, not read', why.format('investiture and census prose on both pages, but corrupted '
                                                                   'runs (ttabetstatiing?elliznellidenari, unmannifestsobismain) '
                                                                   'in most sentences'))},
                extra=chain(gaps_add(('R94, R95, R100, R101: decoded, not read (3,519 items)', 'not-attempted',
                                      'polyphonic beam choices corrupt words in most sentences; re-read each against the '
                                      'images and the DECODE transcription, digit choices constrained word by word')),
                            note_add('22 Oct 2026, reading audit: R94, R95, R100, R101 decoded, not read; class read -> read in part.')),
                step=('Reading audit, per-document pass (George Lasry\'s sentence test): the eleven decryptions read through. '
                      'R93, R96-R99, R102, R115 build Italian sentences with scattered slips; R94, R95, R100 and R101 have '
                      'corrupted runs in most sentences (docs/_check_reading.py 0.75-0.89 clean, inflated by nomenclator words). '
                      'Four letters relabelled decoded, not read; class read -> read in part; fraction_read unknown -> 0.667 (items).'))

    elif name == 'army1902':
        relabel('army1902', lang='ja', cls='read in part', fraction=0.671,
                fraction_source=('decode_out.txt, digit pairs (end marks included): C09122911500 (36) and C09123116600 (13) read '
                                 'as sentences, 49 of 73 pairs (0.671). C09122909900 (12 pairs) is a heading-like noun phrase, '
                                 'not prose; C03020059400 (12) is decoded, not read. The earlier 1.0 (all 73 pairs take a value '
                                 'from the table) is withdrawn as a reading figure.'),
                states={'C09122909900': ('not prose', ('A twelve-kana noun phrase, カイグンエンシウケンガク "observation of the naval '
                                                       'exercise", the enciphered words of an otherwise clear telegram; the draft\'s '
                                                       'furigana give カイグン エンシウ, and pair 2 is written 17 (シ) for イ. Too short '
                                                       'for sentences (' + A + ').')),
                        'C03020059400': ('decoded, not read', ('Twelve pairs giving one noun phrase, シンテイアクゼウシレイブ read as '
                                                               '辛碇泊場司令部 (an anchorage command), with two pairs off the table '
                                                               '(10/12); the sense is a guess, not a sentence (' + A + '); fix: '
                                                               'the original form, or a sibling telegram naming the unit.'))},
                extra=note_add('22 Oct 2026, reading audit: C09122909900 not prose (a noun phrase), C03020059400 decoded, not '
                               'read; class read -> read in part, fraction_read 1.0 -> 0.671 (pairs in the two telegrams that read).'),
                step=('Reading audit, per-document pass (George Lasry\'s sentence test): texts/readings.md read per telegram. '
                      'C09122911500 and C09123116600 read as sentences; C09122909900 is a 12-kana noun phrase confirmed by '
                      'its draft (not prose); C03020059400 is a 12-kana phrase with two signs off the table whose sense is '
                      'guessed (decoded, not read). Class read -> read in part; fraction_read 1.0 -> 0.671.'))

    elif name == 'battier1686':
        relabel('battier1686', lang='nl', fraction=0.49, fraction_method='estimated',
                fraction_source=('Estimated, 22 Oct 2026 reading audit: the seven letters of outcome.texts that read hold 2,078 '
                                 'cipher tokens (tokens/*_groups.txt); 4 Dec 1687 (211) and 12 Feb 1688 (271) are decoded, not '
                                 'read. The earlier volume estimate (about 55% of the cipher in inv. 401, before 24 April 1687 '
                                 'was added) implies a volume of about 4,200 tokens, so about 49%; withdrawn: the 55% counted '
                                 'the two letters as read. Inventory: inv/orch_letters.tsv and inv/nw.tsv.'),
                states={4: ('decoded, not read', ('91R reads, but the 92L cipher block has holes in most sentences '
                                                  '("gesoubconneert(?) gouverneren(?)", "dat [dat] oude Sex(e)(?)", "[?] '
                                                  'consequentie") and the English gist guesses (' + A + '); fix: re-read 92L on '
                                                  'the image against the key, and the nearby decipherment sheets.')),
                        6: ('decoded, not read', ('99R reads; 100R has holes in most sentences ("sonder het [?] fundament", "te '
                                                  'doen na Madrid [?] het afgeseyt(?) [?]") and the gist is partly inferred (' + A +
                                                  '); fix: re-read 100R on the image against the key, and the nearby '
                                                  'decipherment sheets.'))},
                extra=chain(gaps_add(('4 Dec 1687 (92L) and 12 Feb 1688 (100R) cipher blocks: decoded, not read', 'not-attempted',
                                      'holes in most sentences; re-read on the images against the inv. 1209 key; the nearby '
                                      'decipherment sheets are unchecked')),
                            note_add('22 Oct 2026, reading audit: 4 Dec 1687 and 12 Feb 1688 decoded, not read; fraction_read '
                                     '0.55 -> 0.49 (estimated).')),
                step=('Reading audit, per-document pass (George Lasry\'s sentence test): readings/s091R-s092R and s099R-s100R '
                      'read through. 91R and 99R read; the 92L and 100R cipher blocks have (?) and [?] in most sentences, as '
                      'NOTES already said (neither passes the strict sense screen). Both letters relabelled decoded, not read; '
                      'fraction_read 0.55 -> 0.49 (estimated).'))

    elif name == 'benedict1399':
        def fix(p):
            e = p['outcome']['texts'][0]
            e['label'] = ('Ten letters, Puig app. XXVI-LII (22 Sep 1399 - 8 Feb 1403); in the repository only the facsimile '
                          'p. 475 (app. XXXV, 22 Jun 1400), checked word by word')
        relabel('benedict1399', lang='la',
                reviews={0: ('B', ('Excerpt only: src/plate475_check.tsv, taken in order, builds Latin clauses ("K cum duce '
                                   'burgundie et ideo est sic negocium tenendum in suspenso ... quod revertitur in siciliam, '
                                   'alii vero asserunt quod K factus cancellarius debet in catalonia"); line 4 is unchecked. '
                                   'The other nine letters are Puig\'s print and are not in the repository.'))},
                fraction_source=('src/plate475_check.tsv: share of the p. 475 plate\'s cipher letters (one page of app. XXXV) '
                                 'confirmed sign by sign against the rebuilt key. Not a share of the ten letters: their text is '
                                 'Puig y Puig\'s print (1920), which is not in the repository (reading audit, 22 Oct 2026).'),
                fraction=0.914,
                extra=chain(fix,
                            lambda p: p['outcome']['texts'][0].__setitem__('note', (
                                'Excerpt only: the full decipherment is Puig y Puig, Pedro de Luna (Barcelona 1920), app. '
                                'XXVI-LII, pp. 466-491 (Google Books CuOlkxWnk-EC, blocked for automated access; HathiTrust '
                                '100676638 behind Cloudflare). Read by Puig; the repository holds the p. 475 plate check only '
                                '(' + A + ').')),
                            gaps_add(('Puig\'s printed text of the ten letters, not in the repository', 'needs-physical-access',
                                      'Google Books blocks automated access (403/CAPTCHA) and HathiTrust 100676638 sits behind a '
                                      'Cloudflare challenge; the reading is Puig\'s and is not claimed here beyond the p. 475 plate')),
                            note_add('22 Oct 2026, reading audit: only the p. 475 plate check is in the repository; the reading '
                                     'of the ten letters is Puig\'s print, not copied here.')),
                step=('Reading audit, per-document pass (George Lasry\'s sentence test): the entry\'s text in the repository is '
                      'the p. 475 plate check, which builds Latin clauses; the ten letters are Puig\'s print (Google Books, '
                      'blocked). Kept read for the plate only, with an excerpt note; fraction_read_source restated as the '
                      'plate\'s sign-confirmed share.'),
                step_result='partial')

    elif name == 'bienvenut1590':
        relabel('bienvenut1590', lang='fr', cls='read in part', fraction=0.15, fraction_method='estimated',
                fraction_source=('Estimated, 22 Oct 2026 reading audit: texts/n23_decryption.md holds a sample of about 90 words '
                                 'of the two-page letter ff. 35r-v; the rest is not transcribed. The earlier 1.0 (26 of 26 code '
                                 'numbers on the key slip, codes.txt) is the share of codes resolved, withdrawn as a reading figure.'),
                reviews={0: ('A', ('Excerpt only: the sample reads as French sentences with the codes resolved ("[Mme de Nemours] '
                                   'me pourmena hyer par la gallerie du logis de la Reyne ..."); the rest of ff. 35r-v is not '
                                   'transcribed.'))},
                extra=chain(lambda p: p['outcome']['texts'][0].__setitem__('note', (
                                'Excerpt only: the full letter is the clear copy on BnF fr. 3623 ff. 35r-v (Gallica btv1b525245007, '
                                'canvases 79-80; copies in the main checkout\'s targets/champagne1590/img/), not yet transcribed '
                                '(' + A + ').')),
                            gaps_add(('n23, ff. 35r-v: the clear text beyond the sample, not transcribed', 'not-attempted',
                                      'Gallica btv1b525245007 canvases 79-80 (copies in the main checkout targets/champagne1590/img/); '
                                      'every code is on the key slip f. 36r, so transcription is all that is needed')),
                            note_add('22 Oct 2026, reading audit: only a sample of the letter is in the repository; class read -> '
                                     'read in part until ff. 35r-v are transcribed.')),
                step=('Reading audit, per-document pass (George Lasry\'s sentence test): texts/n23_decryption.md is a sample of '
                      'fragments joined by "..."; it reads, but most of the letter is not transcribed. Kept read for the sample '
                      'with an excerpt note; class read -> read in part; fraction_read 1.0 -> about 0.15 (estimated).'))

    elif name == 'bilia1527':
        relabel('bilia1527', lang='it',
                states={1: ('decoded, not read', ('Raw decoder output for the seven cipher lines of f. 102v: bracketed unknown '
                                                  'signs in every line and letter-level nonsense ("isoizde", "axaroaltn"); no '
                                                  'continuous sense (' + A + '); fix: a human sign-by-sign re-transcription '
                                                  'of f. 102v. The clear close is described in the summary but is not part of '
                                                  'this decryption.'))},
                extra=note_add('22 Oct 2026, reading audit: f. 102v decoded, not read (fraction_read already excluded it).'),
                step=('Reading audit, per-document pass (George Lasry\'s sentence test): decoded_ours_f102v.txt read; no '
                      'continuous sense in any of its seven lines. The f. 102v entry relabelled decoded, not read; class and '
                      'fraction_read unchanged (504/623 already counted f. 102v as unread).'))

    elif name == 'bizozola1520':
        relabel('bizozola1520', lang='it',
                reviews={0: ('B', ('Overturns the per-document C. reading_raw.txt is spaced, line-by-line decoder output with '
                                   'the key\'s systematic homophone slips (a/u, e/p: "dacato" ducato, "qaesta" questa, "rpg ione" '
                                   'ragione); read through, nearly every line builds Italian sense: the council\'s talk of '
                                   'dividing Milan among Savoy, Monferrato, Mantua and Ferrara, the Archbishop of Bari\'s view, '
                                   'the Emperor at the Certosa and the cardinals riding out to him, misser Iulio\'s affair, '
                                   'Attavante and Trivulzio\'s spenditore. Open: the date line (157v ll. 9-10) and about 35 '
                                   'doubtful signs (doubtful.txt). A normalised Italian text and a translation are still to '
                                   'be written.'))},
                extra=note_add('22 Oct 2026, reading audit: the per-document C overturned (B, raw but readable line by line); '
                               'a normalised text and translation are still to be written.'),
                step=('Reading audit, per-document pass (George Lasry\'s sentence test): reading_raw.txt read line by line '
                      'against NOTES\' summary and second-pass resolutions. The letter-level slips are the key\'s homophones '
                      'and normalise mechanically; the sentences build except in the doubtful stretches already listed. '
                      'Audit grade C overturned to B; class and fraction unchanged.'),
                step_result='worked')

    elif name == 'bonzagni1512':
        why = ('No transcription or decipherment text in the repository: the contemporary {} is on the DECODE images '
               '(main checkout targets/bonzagni1512/img/{}); not counted as a reading (' + A + '); fix: transcribe it.')
        relabel('bonzagni1512', lang='it', cls='not read', method='not solved',
                method_basis=('Read at the time (interlinear decipherments over R1123 and R1124, a decipherment slip for R1125), '
                              'but none of it is transcribed in the repository, so no reading is claimed (reading audit, 22 Oct '
                              '2026). Once the contemporary decipherments are transcribed the method is read from existing '
                              'decipherment.'),
                states={'R1123': ('decoded, not read', why.format('interlinear decipherment over every word', 'IMG_R1123_I5692_P1.png')),
                        'R1124': ('decoded, not read', why.format('interlinear decipherment', 'IMG_R1124_I5696_P1.png')),
                        'R1125': ('decoded, not read', why.format('decipherment slip (image 5; its first lines are quoted in NOTES)',
                                                                  'IMG_R1125_I5702_P5.png and the cipher on _P3'))},
                extra=chain(gaps_add(('R1123, R1124, R1125: the contemporary decipherments, not transcribed', 'not-attempted',
                                      'images fetched to the main checkout targets/bonzagni1512/img/ (git-ignored); transcribe '
                                      'the interlinear glosses (R1123 p. 1-2, R1124 p. 1) and the R1125 slip, and check them '
                                      'against the cipher')),
                            note_add('22 Oct 2026, reading audit: none of the three decipherments is transcribed here; all three '
                                     'entries decoded, not read; class already solved -> not read, method -> not solved until '
                                     'they are transcribed.')),
                step=('Reading audit, per-document pass (George Lasry\'s sentence test): no text of R1123, R1124 or R1125 is in '
                      'the repository (decode/*.htm are record pages; the decipherments are on the images only). All three '
                      'relabelled decoded, not read; class already solved -> not read; method read from existing decipherment '
                      '-> not solved, until the contemporary decipherments are transcribed.'))

    elif name == 'breves1603':
        relabel('breves1603', lang='fr',
                states={3: ('decoded, not read', (
                    'Summaries only, not the letters: berger/table_pp667-682.txt is the OCR of Berger de Xivrey\'s printed table '
                    '(one-paragraph abstracts of many letters 1603-1606). Excerpt only: the full clear text is in BnF fr. 4029 '
                    'ff. 118-128 (register of Henri IV\'s letters to Breves), not digitised; fr. 3541 is not digitised either '
                    '(' + A + ').'))},
                extra=chain(gaps_add(('The nine further letters of 1603 (ff. 69-104): only Berger\'s summaries in the repository',
                                      'needs-physical-access', 'the full clear text is in BnF fr. 4029 ff. 118-128 and the '
                                      'ciphertext in fr. 3541; neither volume is digitised')),
                            note_add('22 Oct 2026, reading audit: the nine summarised letters relabelled decoded, not read '
                                     '(summaries, not texts); the three printed in full stand.')),
                step=('Reading audit, per-document pass (George Lasry\'s sentence test): berger/table_pp667-682.txt is the '
                      'printed table of abstracts, not the nine letters. That entry relabelled decoded, not read (summaries '
                      'only); the three letters printed in full (ff. 60, 63, 66) read.'),
                step_result='partial')

    elif name == 'brulart1615':
        why = ('Tomokiyo\'s key is on the record, but no plaintext is in the repository or on his page (key image and '
               'remarks only){}; not counted as a reading (' + A + '); fix: fetch the record\'s pages with the DECODE '
               'cookie and read them with his key{}.')
        relabel('brulart1615', lang='fr', cls='not read', method='not solved',
                method_basis=('Satoshi Tomokiyo reconstructed the Brulart de Leon key (1615-18) and attached it to both DECODE '
                              'records, but no plaintext of either letter is published or in the repository, so no reading is '
                              'claimed (reading audit, 22 Oct 2026); with his key applied the method would be read with known key.'),
                states={'R2785': ('decoded, not read', why.format('; one page image (main checkout targets/louis1615/decode/'
                                                                   'IMG_R2785_I17344_P1.jpg) shows contemporary decipherments '
                                                                   'over most cipher runs', ' and the interlinear glosses')),
                        'R2786': ('decoded, not read', why.format('; only the address leaf was fetched', ''))},
                extra=chain(gaps_add(('R2785 and R2786: no plaintext in the repository', 'not-attempted',
                                      'DECODE pages (3 each) reachable with the shared cookie; R2785 has contemporary interlinear '
                                      'decipherments; Tomokiyo\'s key table is on both records (DOC_2785/2786 png)')),
                            note_add('22 Oct 2026, reading audit: no plaintext of either letter exists in the repository or on '
                                     'Tomokiyo\'s page; both decoded, not read; class already solved -> not read, method -> not solved.')),
                step=('Reading audit, per-document pass (George Lasry\'s sentence test): no text of R2785 or R2786 is in the '
                      'repository, and cryptiana louisxiii.htm gives the key and remarks on undeciphered symbols, not the '
                      'letters. Both relabelled decoded, not read; class already solved -> not read; method read from existing '
                      'decipherment -> not solved.'))

    elif name == 'charles1536':
        relabel('charles1536', lang='es',
                states={'R9957': ('decoded, not read', (
                            'Excerpt only: the full decipherment is Wanruo Luo, El lenguaje cifrado de Isabel de Portugal '
                            '(1530-1539), thesis, Universitat de Valencia 2021 (RODERIC), p. 287, key AGS Estado leg. 1.1.1 doc. '
                            '169; not in the repository. What the repository holds (first-pass transcriptions and fragments of the '
                            'contemporary decipherment on pp. 17-18 quoted in NOTES) has holes in most clauses (' + A + '); '
                            'fix: copy Luo\'s text, or transcribe the pp. 17-18 decipherment from the images.')),
                        'R9952': ('decoded, not read', (
                            'No transcription of the ciphertext or of the contemporary decipherment (margins of ff. 10-12, full on '
                            'ff. 13-14) is in the repository; the images are in the main checkout targets/charles1536/img/'
                            'r9952_p*.jpg (' + A + '); fix: transcribe ff. 13-14.'))},
                extra=chain(gaps_add(('R9957: Luo\'s printed decipherment (2021, p. 287) not in the repository', 'not-attempted',
                                      'the thesis is on RODERIC (Universitat de Valencia); the contemporary decipherment of the '
                                      'pp. 16-17 passages on pp. 17-18 is on the images (main checkout img/)'),
                                     ('R9952: the contemporary decipherment (ff. 10-14), not transcribed', 'not-attempted',
                                      'images in the main checkout targets/charles1536/img/r9952_p*.jpg')),
                            note_add('22 Oct 2026, reading audit: neither letter\'s text is in the repository (R9957 excerpt only, '
                                     'R9952 none); both decoded, not read. Class already solved kept: R9957 is in print (Luo 2021).')),
                step=('Reading audit, per-document pass (George Lasry\'s sentence test): R9957 is in the repository only as '
                      'fragments of its contemporary decipherment (Luo\'s print not copied); R9952 has no text at all. Both '
                      'relabelled decoded, not read; class kept already solved (R9957 printed by Luo 2021).'))

    elif name == 'chomentowski1713':
        relabel('chomentowski1713', lang='pl',
                reviews={1: ('A', ('Overturns the per-document C, which concerned the faint clear body of R7485 under the shared '
                                   'doc key. R7484_reading.txt builds Polish sentences throughout; 18 of 513 cipher tokens are '
                                   'marked [...] or (?).')),
                         2: ('A', ('Overturns the per-document C. The cipher passage of R7485 ("Seraskierowi Turcy wierzyc nie '
                                   'chca i Hanowi ...") reads in full; the [...] and (?) are in the writer\'s faint clear body, '
                                   'not in the cipher, and pp. 116-117 are clear text, not cipher.'))},
                extra=note_add('22 Oct 2026, reading audit: the per-document C on R7484-R7485 overturned (the holes are in R7485\'s '
                               'faint clear body, not its cipher).'),
                step=('Reading audit, per-document pass (George Lasry\'s sentence test): R7484_reading.txt and R7485_reading.txt '
                      'read. R7484 reads with scattered holes; in R7485 the cipher passage reads in full and the holes are in '
                      'the pale clear body (pp. 116-117 clear, not cipher). Audit grade C overturned to A for both; claim '
                      'unchanged.'),
                step_result='worked')

    elif name == 'cifuentes1534':
        relabel('cifuentes1534', lang='es', cls='not read', method='not solved',
                method_basis=('Read at the time: the decipherment is bound with the letter as f. 54 (DECODE R9963 image 5), but it '
                              'is not transcribed in the repository (NOTES quotes fragments only), so no reading is claimed '
                              '(reading audit, 22 Oct 2026). Once transcribed the method is read from existing decipherment.'),
                states={'R9963': ('decoded, not read', (
                    'No transcription or decipherment text in the repository; NOTES quote fragments of the f. 54 decipherment. '
                    'Image in the main checkout targets/cifuentes1534/decode/IMG_R9963_I46336_P5.jpg (' + A + '); fix: '
                    'transcribe f. 54 and check it against the cipher.'))},
                extra=chain(gaps_add(('R9963: the contemporary decipherment on f. 54, not transcribed', 'not-attempted',
                                      'image 5 in the main checkout targets/cifuentes1534/decode/ (git-ignored)')),
                            note_add('22 Oct 2026, reading audit: the f. 54 decipherment is not transcribed here; decoded, not '
                                     'read; class already solved -> not read, method -> not solved until it is.')),
                step=('Reading audit, per-document pass (George Lasry\'s sentence test): no text of R9963 is in the repository '
                      'beyond fragments quoted in NOTES. Relabelled decoded, not read; class already solved -> not read; method '
                      'read from existing decipherment -> not solved, until f. 54 is transcribed.'))

    elif name == 'clair357':
        def split(p):
            t = p['outcome']['texts']
            e = t[0]
            e['label'] = 'ff. 167-168, 28 Oct 1586: f. 168r, the contemporary clear copy of f. 167r ll. 1-30 (to the cross mark)'
            new = {k: e[k] for k in ('doc', 'transcription', 'decryption') if k in e}
            new['label'] = 'ff. 167-168, 28 Oct 1586: f. 167r from the cross mark and f. 167v, interlinear decipherment'
            new['summary'] = ('The rest of the letter, glossed word by word over the figures: Fume, vice-admiral of Guyenne and '
                              'Navarre\'s Catholic confidant, proposes a reconciliation; the Queen of England; Villeroy writes '
                              'about satisfying Mayenne.')
            new['language'] = 'fr'
            new['state'] = 'decoded, not read'
            new['note'] = ('The glosses are transcribed as fragments ("... des [⊖] ... de la court ...", "Il se trouvera [?] ... '
                           'mesme ... la guerre"); most sentences are only partly recoverable, and the verso glosses were not '
                           'read word by word (' + A + '); fix: read the glosses at full resolution (Gallica btv1b9001053r '
                           'canvases 331-332) and decode the unglossed figures with the key.')
            t.append(new)
        relabel('clair357', lang='fr', cls='read in part', fraction=0.5, fraction_method='estimated',
                fraction_source=('Estimated, 22 Oct 2026 reading audit: only the f. 168r clear copy (f. 167r ll. 1-30) reads as '
                                 'sentences, roughly half the letter; by words of texts/f167_decryption.md it is 383 of 667 (0.57), '
                                 'but the glossed part\'s "..." hide unread words. The field was "unknown" before.'),
                reviews={0: ('A', ('The f. 168r clear copy builds French sentences with scattered [?] and (…) holes; the '
                                   'last sentence is uncertain.'))},
                extra=chain(split, gaps_add(('f. 167r after the cross mark and f. 167v: interlinear decipherment read only in fragments',
                                             'not-attempted', 'Gallica btv1b9001053r canvases 331-332 (full-resolution copies in the '
                                             'main checkout img/); read the glosses word by word and decode unglossed figures '
                                             'with Tomokiyo\'s table as extended here')),
                            note_add('22 Oct 2026, reading audit: the entry split; the f. 168r copy reads, the f. 167 interlinear '
                                     'part is decoded, not read; class read -> read in part.')),
                step=('Reading audit, per-document pass (George Lasry\'s sentence test): texts/f167_decryption.md read. The f. 168r '
                      'clear copy builds sentences; the interlinear part (f. 167r after the cross, f. 167v) is fragments with '
                      'holes in most sentences. Entry split into a read part and a decoded, not read part; class read -> read in '
                      'part; fraction_read unknown -> about 0.5 (estimated).'))

    elif name in ('comuel1415', 'comuel1416'):
        pp = {'comuel1415': 'pp. 562-563', 'comuel1416': 'pp. 578-579'}[name]
        relabel(name, lang='la',
                states={0: ('decoded, not read', (
                    'Not in the repository: the reading is Puig y Puig\'s print (Pedro de Luna, 1920, ' + pp + '), linked on Google '
                    'Books, which blocks automated access; nothing of the letter is here, so it is not counted as a reading '
                    '(' + A + ').'))},
                extra=chain(gaps_add(('Puig\'s printed text of the letter (' + pp + '), not in the repository', 'needs-physical-access',
                                      'Google Books blocks automated access (403/CAPTCHA); HathiTrust 100676638 is behind a '
                                      'Cloudflare challenge; a copy of the book is needed')),
                            note_add('22 Oct 2026, reading audit: no text of the letter is in the repository; decoded, not read. '
                                     'Class kept: the text exists in print (Puig 1920).')),
                step=('Reading audit, per-document pass (George Lasry\'s sentence test): the only text is a Google Books link '
                      'that returns 403 to scripts; nothing of the letter is in the repository. Relabelled decoded, not read; '
                      'class already solved kept because the decipherment is in print.'),
                step_result='partial')

    elif name == 'deswart1782':
        def parts(p):
            for pt in p['outcome'].get('parts', []):
                if pt['label'].startswith('Croiset 1765'):
                    pt['method'] = 'not solved'
                    pt['extent'] = 'none'
                    pt['basis'] = ('22 Oct 2026, reading audit: the 1765 key fits (R1036 1,663/1,719 groups given a value; R1040 '
                                   'second part 5,256/5,956), but the machine decipherments do not build sentences, so nothing is '
                                   'counted as read. Earlier basis: ' + pt['basis'])
        relabel('deswart1782', lang='nl', cls='not read', method='not solved', fraction=0.0,
                fraction_source=('22 Oct 2026, reading audit: only documents that build sentences count; R1036 and R1040 are '
                                 'decoded, not read, so 0 (the normalised Greek-project passage in NOTES, tokens 239-466 and '
                                 '686-775, reads but is not a document). The earlier 0.967 (1,663 of 1,719 groups of R1036 given '
                                 'a value, R1036_codes.txt) is withdrawn as a reading figure.'),
                states={'R1036': ('decoded, not read', (
                            'Raw machine decipherment: words split into letters ("be trek ke lijk", "p r u y ss chi n"), bracketed '
                            'codes and "?" in almost every line, misreadings ("dak? se" = dat zij); the topic follows, the '
                            'sentences do not (' + A + '); fix: apply the 30 Sept corrections (leading-dash rule, 47^_ = k, the '
                            'key misreadings) and normalise line by line, as was done for the Greek passage.')),
                        'R1040': ('decoded, not read', (
                            'Same raw output with a bracketed code in most lines; the opening pages build partial sentences, the '
                            'last stretch is fragments of Dutch, French and unread codes (' + A + '); fix: the context pass on '
                            'its ~700 unread groups, then a normalised reading.'))},
                extra=chain(parts, gaps_add(
                    ('R1036: machine decipherment not yet built into sentences', 'not-attempted',
                     'apply the 30 Sept 2026 corrections to decode_1765.py, regenerate, and normalise line by line'),
                    ('R1040 second part: machine decipherment not yet built into sentences', 'not-attempted',
                     'context pass on its own unread groups, then a normalised reading')),
                    note_add('22 Oct 2026, reading audit: R1036 and R1040 decoded, not read; class read in part -> not read, '
                             'method -> not solved (the 1765 key match stands); fraction_read 0.967 -> 0.')),
                step=('Reading audit, per-document pass (George Lasry\'s sentence test): R1036_machine_decipherment.txt and '
                      'R1040_second_key_machine_decipherment.txt read through; words split into letters, bracketed codes and '
                      'query marks break nearly every sentence (docs/_check_reading.py 0.18 and 0.11 clean). Both relabelled '
                      'decoded, not read; class read in part -> not read; method read after matching with key from external '
                      'sources -> not solved; fraction_read 0.967 -> 0. The R1038 key match stands.'))

    elif name == 'dubellay':
        relabel('dubellay', lang='fr',
                states={'22oct1529': ('decoded, not read', (
                    'Excerpt only: the ciphered opening (the point of the entry) is printed by Scheurer, Correspondance du '
                    'cardinal Jean du Bellay t. I (1969) pp. 111-112, seen in Google Books snippets (first lines quoted in '
                    'NOTES); the repository holds Le Grand\'s clear part only, where the opening is "non dechiffre". The leaf '
                    'fr. 3005 f. 165 was not seen (' + A + '); fix: fetch it through the Gallica IIIF (openapi.bnf.fr) and '
                    'decipher the opening with key_p21.tsv.'))},
                extra=chain(gaps_add(('22 Oct 1529 opening (fr. 3005 f. 165): not in the repository', 'not-attempted',
                                      'the leaf is on Gallica, reachable through the IIIF at openapi.bnf.fr; decipher it with '
                                      'the 1529 key (key_p21.tsv) and compare with Scheurer\'s snippets')),
                            note_add('22 Oct 2026, reading audit: the 22 Oct 1529 entry is decoded, not read (its ciphered opening '
                                     'is not in the repository); class kept: Scheurer prints it.')),
                step=('Reading audit, per-document pass (George Lasry\'s sentence test): for 22 Oct 1529 the repository has only '
                      'Le Grand\'s clear part; the ciphered opening is Scheurer\'s (snippets). Relabelled decoded, not read; class '
                      'already solved kept (in print).'),
                step_result='partial')

    elif name == 'egmond':
        relabel('egmond', lang='fr',
                states={'ciphered-address': ('not prose', (
                    'A three-line address, "A mon bon cousin / Monsieur le grant maistre / de France": it reads, but it is a '
                    'title, not sentences (' + A + ').'))},
                step=('Reading audit, per-document pass (George Lasry\'s sentence test): the ciphered address is three lines of '
                      'title, not prose; relabelled not prose. Claim unchanged.'),
                step_result='worked')
    else:
        raise SystemExit('unknown ' + name)
    print('done', name)


if __name__ == '__main__':
    for n in sys.argv[1:]:
        run(n)
