"""Second-wave relabel (RELABEL_DOCS_BRIEF.md) for the targets in relabel_docs_1.txt, 22 Oct 2026.

Uses relabel_docs_1.py (a copy of relabel_docs_0.py: splices only the changed spans of each profile.json).
Run once:  PYTHONUTF8=1 python research/reading_audit/relabel_docs_1_run.py [folder ...]
"""
import sys
from relabel_docs_1 import relabel, BY, DATE

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


def entry_note(i, text, append=True):
    def f(p):
        e = p['outcome']['texts'][i]
        e['note'] = ((e.get('note', '').rstrip() + ' ') if append and e.get('note') else '') + text
    return f


def run(name):
    if name == 'esp318':
        relabel('esp318', lang='es', cls='not read', method='not solved',
                method_basis=('No. 92 was decoded with the Cifra general printed by Galende Diaz (1994), which Tomokiyo had '
                              'assigned to the letter; the assignment is proved against eight interlinear glosses on f. 116r. '
                              'The decode (f116_reading.md) is a line table of sign strings with a gloss column that leaves '
                              'holes in most cipher sentences, so no reading is claimed (reading audit, 22 Oct 2026); once the '
                              'letter is built into sentences the method is read with known key.'),
                fraction=0.0,
                fraction_source=('Reading audit, 22 Oct 2026: no. 92, the only document, is decoded, not read, so no tokens are '
                                 'in a document that reads. The earlier 0.75 (NOTES and f116_reading.md: "about three quarters '
                                 'of the words", estimated by line) is withdrawn as a reading figure.'),
                states={'no92': ('decoded, not read', (
                    'The clear opening (ll. 1-4) and the clear islands read, and some cipher lines build Spanish clauses '
                    '(f. 116r ll. 6-7, 15, 17, 22-25, 33; f. 116v ll. 3-9), but ll. 8-11, 16, 18-21, 26-31 and 34 are '
                    'sign strings with open codes (xob, zeb, zog, zems, bog) and unplaced letter runs, so most cipher '
                    'sentences have holes (' + A + '); fix: re-read those lines on full/f116r.jpg and f116v.jpg against the '
                    'Cifra general and write a normalised running text with a translation.'))},
                extra=chain(gaps_add(('no. 92 as a running text: decoded, not read', 'not-attempted',
                                      'the line table has holes in most cipher sentences; re-read ff. 116r ll. 8-11, 16, 18-21, '
                                      '26-31, 34 and f. 116v ll. 1-2, 10-11 on the full scans against the Cifra general, then '
                                      'write a normalised reading and an English translation')),
                            note_add('22 Oct 2026, reading audit: no. 92 decoded, not read (holes in most cipher sentences); '
                                     'class read in part -> not read, method -> not solved, fraction_read 0.75 -> 0.')),
                step=('Reading audit, per-document pass (George Lasry\'s sentence test): f116_reading.md read line by line. The '
                      'clear opening and several cipher lines build Spanish clauses, but about half the cipher lines are sign '
                      'strings with open codes and unplaced letters, so most cipher sentences have holes (docs/_check_reading.py '
                      '0.35 clean). Per-document grade C confirmed; no. 92 relabelled decoded, not read; class read in part -> '
                      'not read; method read with known key -> not solved; fraction_read 0.75 -> 0.'))

    elif name == 'esp318no94':
        relabel('esp318no94', lang='es', cls='not read', method='not solved',
                method_basis=('Michael Brackx recovered the 39-class homophonic alphabet ciphertext-only (annealing the letter '
                              'signs against a Spanish 5-gram, no crib), and it reproduces here from random starts; but about 90 '
                              'code groups are open and his provisional decryption (issue #62, not copied into the folder) has '
                              'holes in most sentences, so no reading is claimed (reading audit, 22 Oct 2026). With the code read '
                              'the method would be key recovered from ciphertext-only.'),
                fraction=0.0,
                fraction_source=('Reading audit, 22 Oct 2026: no. 94, the only document, is decoded, not read, so no tokens are '
                                 'in a document that reads. The earlier 0.929 (ct94_brackx.txt: 3,127 of 3,365 cipher tokens '
                                 'given a value or a firm code reading) is withdrawn as a reading figure.'),
                states={'no94': ('decoded, not read', (
                    'The repository holds only Brackx\'s sign transcription (ct94_brackx.txt); his provisional decryption is in '
                    'issue #62, and about 90 code groups are open, so most sentences carry "..." or [xxx] holes; the gist '
                    '(Seminara, the sack, prisoners, Portocarrero\'s death) is recoverable but few sentences are complete '
                    '(' + A + '); fix: copy the decryption into the folder, check it line by line on the scans, and read the '
                    'codes from context.'))},
                extra=chain(gaps_add(('no. 94 decryption: decoded, not read, and not in the folder', 'not-attempted',
                                      'Brackx\'s provisional decryption is only in issue #62; copy it into texts/, check it line '
                                      'by line against the scans (targets/esp318/full/f120r-f121v), and build sentences around the '
                                      'open codes')),
                            note_add('22 Oct 2026, reading audit: no. 94 decoded, not read (about 90 code groups open, holes in '
                                     'most sentences); class read in part -> not read, method -> not solved; the ciphertext-only '
                                     'alphabet stands.')),
                step=('Reading audit, per-document pass (George Lasry\'s sentence test): the repository holds only the sign '
                      'transcription; Brackx\'s provisional decryption (issue #62) has holes in most sentences around about 90 '
                      'open code groups. Per-document grade D confirmed; no. 94 relabelled decoded, not read; class read in part '
                      '-> not read; method -> not solved; fraction_read 0.929 -> 0. The ciphertext-only alphabet recovery is '
                      'unaffected.'))

    elif name == 'eugenie1859':
        relabel('eugenie1859', lang='fr',
                states={2: ('not prose', (
                    'Jozef Krajcovic\'s list of proposed token corrections and verification notes (issue #39), not a '
                    'decipherment text (' + A + ').'))},
                reviews={0: ('B', (
                    'Overturns the per-document C. The token values, taken in order per folio, build French sentences: f9r "en '
                    'sortant avec le roi tous les pretres m\'ont baise les mains, les femmes s\'agenouillaient, les hommes '
                    'etaient exaltes au dela de toute expression ... mais nous avons de la peine a trouver du pain"; f17r "nous '
                    'esperons une bataille sur Chiese, mais l\'ennemi parait decidement se retirer derriere le Mincio". One run '
                    'of ? on f15r. Raw (one value per row, syllables split), so B.')),
                         1: ('A', (
                    'The three excerpts of Lasry\'s report (ff. 19r, 35r, 27r) are coherent French with an English translation; '
                    'one "?" in f27r.'))},
                fraction=0.31, fraction_method='estimated',
                fraction_source=('Estimated, reading audit 22 Oct 2026: what the repository shows of Lasry\'s reading is the token '
                                 'table of ff. 9r, 15r, 17r, 18r (135 of its 145 tokens with a value = 0.307 of the 440 elements) '
                                 'plus three short excerpts (ff. 19r, 35r, 27r) not tokenised. Lasry\'s own figure, 370 of 440 '
                                 'elements identified (0.841), is withdrawn as a reading figure here: his full decipherment is '
                                 'not in the repository.'),
                extra=chain(entry_note(0, 'Excerpt only: four of the eleven cipher pages; the full decipherment is George Lasry\'s '
                                          '(BnF cipher research, 10 Oct 2026), not in the repository (' + A + ').', append=False),
                            entry_note(1, 'Excerpt only: the full decipherment is George Lasry\'s (BnF cipher research, 10 Oct '
                                          '2026), not in the repository (' + A + ').', append=False),
                            gaps_add(('Lasry\'s full decipherment of the eleven cipher pages, not in the repository',
                                      'not-attempted', 'ask George Lasry for his transcription and decryption files; only four '
                                      'pages of tokens and three excerpts are here')),
                            note_add('22 Oct 2026, reading audit: the token table (four pages) and the report excerpts read; '
                                     'Krajcovic\'s corrections are not prose; fraction_read 0.841 (Lasry\'s figure) -> about '
                                     '0.31, what the repository shows.')),
                step=('Reading audit, per-document pass (George Lasry\'s sentence test): the token table of ff. 9r, 15r, 17r, '
                      '18r read in order builds French sentences (C overturned to B); the report excerpts read (A); '
                      'Krajcovic\'s corrections file is not prose. fraction_read 0.841 (Lasry\'s identified elements, his full '
                      'text not in the repository) -> about 0.31, estimated from what the repository holds.'),
                step_result='partial')

    elif name == 'exea1408':
        relabel('exea1408', lang='la',
                states={0: ('decoded, not read', (
                    'Not in the repository: the reading is Puig y Puig\'s print (Pedro de Luna, 1920, app. LXIV, pp. 500-503), '
                    'linked on Google Books, which blocks automated access; nothing of the letter is here, so it is not counted '
                    'as a reading (' + A + ').'))},
                extra=chain(gaps_add(('Puig\'s printed text of the letter (pp. 500-503), not in the repository',
                                      'needs-physical-access',
                                      'Google Books blocks automated access (403/CAPTCHA); HathiTrust 100676638 is behind a '
                                      'Cloudflare challenge; a copy of the book is needed')),
                            note_add('22 Oct 2026, reading audit: no text of the letter is in the repository; decoded, not read. '
                                     'Class kept: the text exists in print (Puig 1920).')),
                step=('Reading audit, per-document pass (George Lasry\'s sentence test): the only text is a Google Books link '
                      'that is blocked to scripts; nothing of the letter is in the repository. Relabelled decoded, not read; '
                      'class already solved kept because the decipherment is in print.'),
                step_result='partial')

    elif name == 'ghinucci1527':
        relabel('ghinucci1527', lang='la',
                states={'worcester-R8589': ('not prose', (
                            'A glyph-to-letter alignment worksheet (token=value pairs, struck nulls) used to build the key; '
                            'the Latin of the passage is printed in L&P iv 5282 (' + A + ').')),
                        'worcester-R8476': ('not prose', (
                            'A glyph transcription with token=value alignments and a glyph legend, used as key source; its '
                            'decipherment is printed in State Papers VI 552 (' + A + ').'))},
                step=('Reading audit, per-document pass (George Lasry\'s sentence test): R8613 reads (A); the R8589 and R8476 '
                      'files are key-building worksheets, relabelled not prose. Claim unchanged.'),
                step_result='worked')

    elif name == 'haga1620':
        relabel('haga1620', lang='nl', cls='read in part', fraction=0.48, fraction_method='estimated',
                fraction_source=('Estimated, reading audit 22 Oct 2026, by words of the two reading files: R2113_reading.md '
                                 '(1,249 words) reads, R2115_reading.md (1,337) is decoded, not read: 0.48. No token count of '
                                 'the cipher spans exists. The field was "unknown" before.'),
                states={'R2115': ('decoded, not read', (
                    'P3\'s clear opening reads, but the file is a partial reading: clear passages are given as [...] where not '
                    'transcribed, and on P2 and P4 the cipher spans are strings of {?...} and bare codes ([43], [62]) with a '
                    'sentence rarely complete (' + A + '); fix: transcribe P2 and P4 in full, re-read the cipher spans with the '
                    'R2118 key (m = 4), and fix the codes from R2113 and the decrypted R2114.'))},
                reviews={'R2113': ('B', ('Line-numbered Dutch with cipher spans in braces; the argument about Hungary, Bohemia '
                                         'and the Porte builds in sentences with a few ? and unresolved codes (per-document B).'))},
                extra=chain(gaps_add(('R2115: decoded, not read', 'not-attempted',
                                      'clear passages on P2 and P4 not transcribed and cipher spans with uncertain letters; '
                                      'transcribe the four pages in full from the DECODE images (decode/, git-ignored) and '
                                      're-read with the R2118 key')),
                            note_add('22 Oct 2026, reading audit: R2115 decoded, not read; class read -> read in part.')),
                step=('Reading audit, per-document pass (George Lasry\'s sentence test): R2113_reading.md builds Dutch sentences '
                      '(B); R2115_reading.md calls itself partial, and P2/P4 are strings of [...], {?...} and bare codes. '
                      'R2115 relabelled decoded, not read; class read -> read in part; fraction_read unknown -> about 0.48 (words).'))

    elif name == 'harley287':
        relabel('harley287', lang='en',
                reviews={'20mar': ('B', (
                    'Overturns the per-document C. R8485 and R8486, the two full pages of the letter, read as English sentences '
                    'with a few ellipses; R8487 is the end of the letter with three short cipher runs and holes ("hath '
                    'assured means to a special service, ... being ... as I wrote unto you"), a small share of the document; '
                    'its holes are listed as gaps.'))},
                step=('Reading audit, per-document pass (George Lasry\'s sentence test): READING.md for 20 March read. R8485 and '
                      'R8486 build sentences; R8487 holds three short runs with holes. Per-document C overturned to B (the '
                      'holes are on the short last page); claim unchanged (read in part).'),
                step_result='worked')

    elif name == 'hesse1672':
        relabel('hesse1672', lang='de',
                reviews={'HCPortal 494': ('B', (
                    'Overturns the per-document C. The letter is clear German with 26 code numbers and two short letter-cipher '
                    'passages; reading.txt gives every cipher item in its clause, and each clause builds (passage 1 '
                    '"Totaliter disgustirt und ?? in Holstein, nun sowohl als in Dennemarck Adell, Burger und Bauern ... in '
                    'plainten combiniret"; passage 2 "Gott geb das all wol ablauff"). What is missing is the clear text '
                    'between the cipher items, which is not cipher; one five-sign word is open.'))},
                fraction=0.922,
                fraction_source=('reading.txt over ct.txt (38 letter-cipher signs) and codes.txt (26 code numbers): 59 of the 64 '
                                 'cipher tokens read as sense (0.922); the earlier 1.0 (all 64 given a value) is withdrawn as a '
                                 'reading figure (' + A + ').'),
                extra=chain(entry_note(0, 'Excerpt only: the cipher items with their clauses; the full letter (clear German) is on '
                                          'the HCPortal images (media 1385-1387, images/f2-f4.jpg, git-ignored), not transcribed '
                                          '(' + A + ').'),
                            note_add('22 Oct 2026, reading audit: the cipher parts read (C overturned to B); fraction_read 1.0 '
                                     '(values given) -> 0.922 (read as sense).')),
                step=('Reading audit, per-document pass (George Lasry\'s sentence test): reading.txt gives the cipher items in '
                      'their clauses; each builds except the five-sign word of passage 1. Per-document C (no connected letter) '
                      'overturned to B: the missing context is clear text, not cipher. fraction_read 1.0 -> 0.922 (read as '
                      'sense, as fraction_coherent already said); excerpt note added.'),
                step_result='worked')

    elif name == 'hm1645':
        why = ('Lasry\'s interlinear plaintext ({}) is on the DECODE record, behind its login, and was kept out of the repository '
               'as his work; no copy is in any checkout, so nothing of the letter can be read here (' + A + '); fix: re-fetch it '
               'with the shared DECODE cookie and check it with apply_key.py.')
        relabel('hm1645', lang='en',
                states={'R785': ('decoded, not read', why.format('D3060/D3061')),
                        'R790': ('decoded, not read', why.format('D3065/D3066')),
                        'R923': ('decoded, not read', why.format('D3069/D3070'))},
                fraction=0.0,
                fraction_source=('Reading audit, 22 Oct 2026: none of the three letters\' text is in the repository (Lasry\'s '
                                 'files were git-ignored and are no longer in any checkout), so no tokens are in a document '
                                 'that reads here. The earlier 0.9099 (apply_key.py: 3,069 of 3,373 groups with a value in '
                                 'Lasry\'s key, 14 Oct 2026) is withdrawn as a reading figure.'),
                extra=chain(gaps_add(('R785, R790, R923: Lasry\'s plaintext not in the repository', 'not-attempted',
                                      'his interlinear and plaintext files are on the DECODE records (reachable with the shared '
                                      'cookie); fetch them into decode/ (git-ignored, his work), grade them as sentences, and ask '
                                      'him whether a reading copy may be kept')),
                            note_add('22 Oct 2026, reading audit: no text of the three letters is in the repository; all three '
                                     'decoded, not read. Class kept: Lasry\'s decipherment exists on DECODE (2020).')),
                step=('Reading audit, per-document pass (George Lasry\'s sentence test): Lasry\'s plaintexts of R785, R790, R923 '
                      'are on DECODE only (git-ignored copies no longer in any checkout); nothing could be read. All three '
                      'relabelled decoded, not read; class already solved kept (Lasry\'s published decipherment); fraction_read '
                      '0.9099 -> 0.'),
                step_result='partial')

    elif name == 'isabella1531':
        relabel('isabella1531', lang='es',
                states={'R9955': ('decoded, not read', (
                            'No transcription or decipherment in the repository; the full decipherment is printed in Wanruo Luo, El lenguaje cifrado de Isabel de Portugal (thesis, Universitat de Valencia '
                            '2021, RODERIC), p. 285, and the contemporary decipherment is on a separate sheet on the DECODE '
                            'images (' + A + '); fix: copy Luo\'s text, or transcribe the sheet.')),
                        'R9956': ('decoded, not read', (
                            'No transcription or decipherment in the repository; the contemporary decipherment is on a separate '
                            'sheet on the DECODE images, not fetched or transcribed, and not known in print (' + A + '); fix: '
                            'fetch the images with the shared DECODE cookie and transcribe the sheet.'))},
                extra=chain(gaps_add(('R9955: Luo\'s printed decipherment (2021, p. 285) not in the repository', 'not-attempted',
                                      'the thesis is on RODERIC (Universitat de Valencia); the contemporary decipherment sheet is '
                                      'on the DECODE images'),
                                     ('R9956: the contemporary decipherment sheet, not transcribed', 'not-attempted',
                                      'DECODE images reachable with the shared cookie; not fetched yet')),
                            note_add('22 Oct 2026, reading audit: neither letter\'s text is in the repository; both decoded, not '
                                     'read. Class already solved kept: R9955 is in print (Luo 2021) and both were deciphered at '
                                     'the time.')),
                step=('Reading audit, per-document pass (George Lasry\'s sentence test): no text of R9955 or R9956 is in the '
                      'repository (decipherment sheets on the DECODE images; R9955 printed by Luo 2021). Both relabelled decoded, '
                      'not read; class already solved kept (in print).'),
                step_result='partial')

    elif name == 'it1583':
        relabel('it1583', lang='it', fraction=0.514,
                fraction_source=('Reading audit, 22 Oct 2026: f. 68 (R7898, 425 cipher tokens, lasry2026/cipher_tokens.txt) '
                                 'reads; f. 70 (402 tokens) is decoded, not read: 425 of 827 = 0.514. The earlier 0.9432 '
                                 '(edition.json via measure_sense.py: 780 of 827 tokens assigned) is withdrawn as a reading '
                                 'figure.'),
                states={'f70': ('decoded, not read', (
                    'Lines 6-8 read ("tamen per fare mio debito ne adviso ..., mediolani die qvarto mai"), but lines 1-5 have '
                    'one to three ? holes in each clause ("a adviso vi l ? se mono ad fare contra cremona", "revnito ? ? ? da ? '
                    'ad tvte le ?") and the signature is unread (' + A + '); fix: re-read the open signs of lines 1-5 against '
                    'the images and the f. 68 key, and work the signature against Mazzatinti\'s attribution.'))},
                reviews={'R7898': ('B', (
                    'Overturns the per-document C. The edited text and Lasry\'s English translation build sentences from line 2 '
                    'to line 11 (Zorzo del Maino\'s report, the count\'s obligations, "la secvreza nostra", eight or ten '
                    'names); the ? runs sit at line openings and ends, where NOTES and the gap list take them for nulls or '
                    'titles, and two mid-sentence holes (l. 10 "?intita", l. 11) are scattered.'))},
                extra=chain(gaps_add(('f. 70: decoded, not read (lines 1-5)', 'not-attempted',
                                      'one to three unread signs in every clause of lines 1-5; re-read them on the image with the '
                                      'shared key, and look for the sibling 1446 letters for more occurrences')),
                            note_add('22 Oct 2026, reading audit: f. 68 reads (C overturned to B); f. 70 decoded, not read; '
                                     'fraction_read 0.9432 (assigned) -> 0.514 (tokens in the letter that reads).')),
                step=('Reading audit, per-document pass (George Lasry\'s sentence test): edited.txt, companion/edited.txt and '
                      'full_letter.md read. f. 68 builds sentences with holes at line openings (C overturned to B); f. 70 has '
                      'holes in every clause of lines 1-5 (C confirmed), relabelled decoded, not read. Class read in part '
                      'kept; fraction_read 0.9432 -> 0.514.'),
                step_result='partial')

    elif name == 'kauderbach1754':
        relabel('kauderbach1754', lang='fr', cls='read in part', fraction=0.81,
                fraction_source=('Reading audit, 22 Oct 2026, code groups per letter (documents[].length): the nine letters that '
                                 'read hold 6,891 of 8,512 groups (0.810); R1954 (1,621) is decoded, not read. The earlier 0.998 '
                                 '(groups given a value by the key) is withdrawn as a reading figure.'),
                states={'R1954': ('decoded, not read', (
                    'Self-declared about 65% read on a weak transcription; the long paragraph has [...] and bracketed guesses '
                    'in most sentences and some clauses do not parse (' + A + '); fix: re-transcribe R1954 from the DECODE '
                    'images and decode it again with key.json.'))},
                extra=chain(gaps_add(('R1954 (March 1756, 1,621 groups): decoded, not read', 'not-attempted',
                                      'weak transcription; re-transcribe from the DECODE images and re-decode with key.json')),
                            note_add('22 Oct 2026, reading audit: R1954 decoded, not read; class read -> read in part; '
                                     'fraction_read 0.998 -> 0.81.')),
                step=('Reading audit, per-document pass (George Lasry\'s sentence test): the ten hand readings read; nine build '
                      'French sentences (A); read/R1954.txt (about 65% read on a weak transcription) has holes in most '
                      'sentences (D confirmed). R1954 relabelled decoded, not read; class read -> read in part; fraction_read '
                      '0.998 -> 0.81 (groups in letters that read).'))

    elif name == 'lee1526':
        relabel('lee1526', lang='en', fraction=0.445,
                fraction_source=('Reading audit, 22 Oct 2026, cipher tokens per document (documents[].length): R8566 (100), R8465 '
                                 '(28) and R8473 (238) read, 366 of 823 (0.445); R8533 (457) is decoded, not read. The earlier 1 '
                                 'is withdrawn as a reading figure.'),
                states={'R8533': ('decoded, not read', (
                    'A sign-level worksheet: f. 109v ll. 5-16 and much of f. 110r build sentences against the clear text, but '
                    'f. 109v ll. 1-4 and 17-22, many f. 109r lines (not re-viewed in pass 2) and the name codes are open or '
                    'rest on the L&P crib, so several sentences have holes (' + A + '); fix: the full-resolution pass on f. 109r '
                    'and f. 110r, then a running text. Tuke\'s contemporary decipherment is calendared in L&P IV 3055.'))},
                extra=chain(gaps_add(('R8533: decoded, not read (f. 109r, f. 109v ll. 1-4 and 17-22, name codes)', 'not-attempted',
                                      'f. 109r and f. 110r not re-read at full resolution (pass 2 stopped at the image viewer\'s '
                                      'limit); re-read them on the DECODE images and write a running text')),
                            note_add('22 Oct 2026, reading audit: R8533 decoded, not read; fraction_read 1 -> 0.445. Class already '
                                     'solved kept: every run was deciphered at the time (L&P IV).')),
                step=('Reading audit, per-document pass (George Lasry\'s sentence test): R8566, R8465 and R8473 read; '
                      'r8533_reading.txt is a worksheet with holes in several sentences and f. 109r not re-read (C confirmed). '
                      'R8533 relabelled decoded, not read; fraction_read 1 -> 0.445; class already solved kept.'))

    elif name == 'maisse1593':
        why = ('Not in the repository: the content was read from the contemporary clear copy in Brienne 13 (NAF 6984, {}), '
               'which was never transcribed, and the cipher leaf itself was not deciphered; nothing of the letter is here '
               '(' + A + '); fix: fetch the Brienne 13 page and the cipher leaf through the Gallica IIIF (openapi.bnf.fr) and '
               'transcribe the copy.')
        relabel('maisse1593', lang='fr', cls='not read', method='not solved',
                method_basis=('The content of both letters is known from contemporary clear copies in fonds Brienne 13 (BnF NAF '
                              '6984), located through the Harlay piece numbers and Berger de Xivrey, but neither copy is '
                              'transcribed in the repository, so no reading is claimed (reading audit, 22 Oct 2026). Once the '
                              'copies are transcribed the method is read from existing decipherment.'),
                fraction=0.0,
                fraction_source=('Reading audit, 22 Oct 2026: neither letter\'s text is in the repository, so no tokens are in a '
                                 'document that reads. The earlier 1.0 is withdrawn as a reading figure.'),
                states={'f406': ('decoded, not read', why.format('fol. 171r, canvas 176')),
                        'f410': ('decoded, not read', why.format('fol. 193v, canvas 199'))},
                extra=chain(gaps_add(('ff. 406 and 410: the Brienne 13 clear copies, not transcribed', 'not-attempted',
                                      'Gallica btv1b100904592 canvases 176 and 199, reachable through the IIIF at openapi.bnf.fr; '
                                      'transcribe them, then check them against the cipher leaves (btv1b90074656 canvases 457, '
                                      '461) and f. 404\'s interlinear decipherment')),
                            note_add('22 Oct 2026, reading audit: the Brienne copies are not transcribed; both letters decoded, '
                                     'not read; class read -> not read, method -> not solved until they are.')),
                step=('Reading audit, per-document pass (George Lasry\'s sentence test): no text of f. 406 or f. 410 is in the '
                      'repository (images and links only). Both relabelled decoded, not read; class read -> not read; method '
                      'read from existing decipherment -> not solved, until the Brienne 13 copies are transcribed.'))

    elif name == 'mauclerc1593':
        relabel('mauclerc1593', lang='fr', cls='not read', method='not solved',
                method_basis=('Read at the time (interlinear decipherments and a clear summary in the 1593 register fr. 3983 f. '
                              '140r, reported by Brice Dudout), but none of it is transcribed in the repository, so no reading is '
                              'claimed (reading audit, 22 Oct 2026). Once transcribed the method is read from existing '
                              'decipherment.'),
                states={'fr3985f20': ('decoded, not read', (
                    'No text and no link in the repository: the interlinear decipherment is on the Gallica images '
                    '(btv1b90606498, views 6-13), never transcribed (' + A + '); fix: fetch them through the Gallica IIIF '
                    '(openapi.bnf.fr) and transcribe the interlinear text.'))},
                extra=chain(gaps_add(('fr. 3985 f. 20: the interlinear decipherment, not transcribed', 'not-attempted',
                                      'Gallica btv1b90606498 views 6-13, reachable through the IIIF at openapi.bnf.fr (scripted '
                                      'downloads from gallica.bnf.fr were refused on 20 Oct 2026); also fr. 3983 f. 140r, the '
                                      'register summary')),
                            note_add('22 Oct 2026, reading audit: nothing of the letter is transcribed here; decoded, not read; '
                                     'class already solved -> not read, method -> not solved until it is.')),
                step=('Reading audit, per-document pass (George Lasry\'s sentence test): no text or link for fr. 3985 f. 20 is in '
                      'the repository. Relabelled decoded, not read; class already solved -> not read; method read from '
                      'existing decipherment -> not solved, until the interlinear decipherment is transcribed.'))

    elif name == 'marechaux1520':
        relabel('marechaux1520', lang='fr', cls='read in part', fraction=0.5, fraction_method='estimated',
                fraction_source=('Estimated, reading audit 22 Oct 2026: f. 41v reads (1,339 of 1,341 letter tokens given a value, '
                                 'f41v_letters.txt); f. 41r, a full page of the same cipher, is Lasry\'s reading on overlay '
                                 'images and is not transcribed here, so about half the cipher of the leaf is in a document that '
                                 'reads in the repository. The earlier 0.998 (f. 41v only) is withdrawn as a figure for the leaf.'),
                states={0: ('decoded, not read', (
                    'Excerpt only: read by George Lasry (24 May 2022); his decipherment is drawn on overlay images on cryptiana '
                    'GL.htm (copies in the main checkout targets/marechaux1520/prior/GL_BnFfr3081_f41_decipher1-3.png), and no '
                    'text of it is in the repository (' + A + '); fix: transcribe the overlays into texts/.'))},
                extra=chain(gaps_add(('f. 41r: Lasry\'s reading, on overlay images only', 'not-attempted',
                                      'transcribe his three overlay crops (main checkout prior/, git-ignored; cryptiana GL.htm) '
                                      'into a text file and join it to the f. 41v running text')),
                            note_add('22 Oct 2026, reading audit: f. 41r decoded, not read here (Lasry\'s reading exists only as '
                                     'overlay images); class read -> read in part.')),
                step=('Reading audit, per-document pass (George Lasry\'s sentence test): texts/f41v_decryption.md reads (A); '
                      'f. 41r points only to Lasry\'s overlay images, with no text in the repository. f. 41r relabelled decoded, '
                      'not read (excerpt only); class read -> read in part; fraction_read 0.998 -> about 0.5 (estimated).'))

    elif name == 'matignon1586c3':
        relabel('matignon1586c3', lang='fr', fraction=0.305,
                fraction_source=('Reading audit, 22 Oct 2026, signs per document: f. 276 (734) and fr. 15571 f. 179 (509) read, '
                                 '1,243 of 4,079 signs (0.305); fr. 15573 ff. 379-381 (2,836) is decoded, not read. The earlier '
                                 '0.9118 (3,719 of 4,079 signs in sense runs, f276/scripts/measure.py, 21 Oct 2026) is withdrawn '
                                 'as a reading figure.'),
                states={'fr15573-f379-381': ('decoded, not read', (
                    'A word-divided but unpunctuated machine decode (~1,139 words, 87 bracketed non-words; the file estimates one '
                    'sign in twenty wrong): stretches build (the Garonne places, the artillery of Navarre), but nearly every '
                    'sentence has a garbled word, and there is no translation (' + A + '); fix: repair the sentences on the '
                    'images (views 740-745), punctuate, and translate.'))},
                extra=chain(gaps_add(('fr. 15573 ff. 379-381: decoded, not read', 'not-attempted',
                                      'machine decode with a garbled word in most sentences; repair on the Gallica images '
                                      '(btv1b90618780 views 740-745), punctuate and translate')),
                            note_add('22 Oct 2026, reading audit: fr. 15573 ff. 379-381 decoded, not read; fraction_read 0.9118 '
                                     '-> 0.305 (signs in the two slips that read).')),
                step=('Reading audit, per-document pass (George Lasry\'s sentence test): f. 276 and f. 179 read from SOLUTION.md '
                      '(A); fr. 15573 ff. 379-381 (Burford v0.5) has a garbled word in nearly every sentence and no translation '
                      '(C confirmed). Relabelled decoded, not read; class read in part kept; fraction_read 0.9118 -> 0.305.'))

    elif name == 'mayenne1586c2':
        relabel('mayenne1586c2', lang='fr', fraction=0.404,
                fraction_source=('Reading audit, 22 Oct 2026, tokens per document: ff. 218-219 (2,138) read, 2,138 of 5,293 '
                                 '(0.404); f. 120 (1,103) and f. 385 (2,052) are decoded, not read. The earlier 0.861 (4,560 '
                                 'of 5,293 tokens in sense runs, measured 21 Oct 2026) is withdrawn as a reading figure.'),
                states={'fr15573-f120': ('decoded, not read', (
                            'Punctuated French with [?] holes: c05-c08 and c12-c15 read cleanly, but c01-c05, c15-c19, c28-c31 '
                            'and f. 120v c03-c05 have holes in most sentences (' + A + '); fix: re-read those lines on the '
                            'image (view 246-247) sign by sign; no person has checked the transcription.')),
                        'fr15573-f385': ('decoded, not read', (
                            'Self-declared partial (v0.2): the French is unspaced with decoder word breaks and many unresolved '
                            'stretches; only isolated clauses translate, and the English file is a gist with ellipses '
                            '(' + A + '); fix: the open stretches on the image (views 752-753), then a normalised reading.'))},
                extra=chain(gaps_add(('fr. 15573 f. 120: decoded, not read', 'not-attempted',
                                      'holes in most sentences of c01-c05, c15-c19, c28-c31, 120v c03-c05; re-read on Gallica '
                                      'btv1b90618780 views 246-247'),
                                     ('fr. 15573 f. 385: decoded, not read', 'not-attempted',
                                      'v0.2 partial, unspaced; resolve the open stretches on views 752-753 and normalise')),
                            note_add('22 Oct 2026, reading audit: f. 120 and f. 385 decoded, not read; fraction_read 0.861 -> '
                                     '0.404 (tokens in ff. 218-219).')),
                step=('Reading audit, per-document pass (George Lasry\'s sentence test): ff. 218-219 read (A); f. 120 has holes '
                      'in most sentences of several paragraphs, and f. 385 is a self-declared partial unspaced decode (both C '
                      'confirmed). Both relabelled decoded, not read; class read in part kept; fraction_read 0.861 -> 0.404.'))

    elif name == 'mellon136':
        relabel('mellon136', lang='de',
                states={2: ('decoded, not read', (
                    'Excerpt only: Christof Rieber\'s blog comment of 10 March 2022, a numbered list for pp. 24-76 with many '
                    'entries cut short by "(..)"; not in the repository; the full comment is on Schmeh\'s post. The same '
                    'passages are read in full in the first entry (' + A + ').'))},
                extra=entry_note(1, 'Excerpt only: nothing of the 2022 text is in the repository; the full decipherment is on '
                                    'Schmeh\'s Cipherbrain post (4 March 2022). The p. 24 passage is read in the first entry '
                                    '(' + A + ').'),
                step=('Reading audit, per-document pass (George Lasry\'s sentence test): reading.txt (all 31 passages) reads; '
                      'Rieber\'s 2022 comment, a pointer with partial entries, relabelled decoded, not read; excerpt note on the '
                      '2022 p. 24 pointer. Claim unchanged.'),
                step_result='worked')

    elif name == 'meryvic1589':
        def parts(p):
            for pt in p['outcome'].get('parts', []):
                if pt['label'] == "Lasry's reading":
                    pt['method'] = 'not solved'
                    pt['extent'] = 'none'
                    pt['basis'] = ('George Lasry, BnF cipher research, 10 Oct 2026: key recovered ciphertext-only, 523 of 545 '
                                   'elements identified, "Partly deciphered"; the repository holds only his excerpts, with holes '
                                   'in every sentence (reading audit, 22 Oct 2026).')
        relabel('meryvic1589', lang='fr', cls='not read', method='not solved',
                method_basis=('George Lasry reports a key recovered from the ciphertext only (81 symbols; 523 of 545 elements '
                              'identified) and calls the letter "Partly deciphered"; only his report excerpts are in the '
                              'repository and they have holes in every sentence, so no reading is claimed here (reading audit, '
                              '22 Oct 2026). With his full decipherment the method would be key recovered from ciphertext-only.'),
                fraction=0.0,
                fraction_source=('Reading audit, 22 Oct 2026: the only document is decoded, not read in the repository (excerpts '
                                 'with holes in every sentence). Lasry\'s 0.96 (identified elements / elements) is withdrawn as '
                                 'a reading figure.'),
                states={0: ('decoded, not read', (
                    'Excerpt only: both excerpts in Lasry\'s entry have ? holes in each sentence (a leading missing word, '
                    '"hommes? de pied?") and his report says "Partly deciphered"; the gist (troops near Limoges, declared '
                    'loyalties) translates. The full decipherment is George Lasry\'s (BnF cipher research, 10 Oct 2026), not '
                    'in the repository (' + A + ').'))},
                extra=chain(parts, gaps_add(('Lasry\'s full decipherment, not in the repository', 'not-attempted',
                                             'ask George Lasry for his transcription and decryption files (report: 6/6 pages '
                                             'transcribed, partly deciphered)')),
                            note_add('22 Oct 2026, reading audit: the excerpts have holes in every sentence; decoded, not read; '
                                     'class already solved -> not read, method -> not solved; Lasry\'s key recovery is recorded '
                                     'in method_basis.')),
                step=('Reading audit, per-document pass (George Lasry\'s sentence test): lasry_entry.md read; both excerpts have '
                      'holes in every sentence (C confirmed) and the report says partly deciphered. Relabelled decoded, not '
                      'read; class already solved -> not read; method -> not solved; fraction_read 0.96 -> 0.'))
    else:
        raise SystemExit('unknown ' + name)
    print('done', name)


if __name__ == '__main__':
    for n in sys.argv[1:]:
        run(n)
