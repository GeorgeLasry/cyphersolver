"""Second-wave relabel (RELABEL_DOCS_BRIEF.md) for the targets in relabel_docs_2.txt, 22 Oct 2026.

Uses relabel_docs_2.py (a copy of relabel_docs_0.py: splices only the changed spans of each profile.json).
Run once:  PYTHONUTF8=1 python research/reading_audit/relabel_docs_2_run.py [folder ...]
"""
import sys
from relabel_docs_2 import relabel, BY, DATE

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


def setkey(k, v):
    def f(p):
        p['outcome'][k] = v
    return f


STEP = 'Reading audit, per-document pass (George Lasry\'s sentence test): '


def run(name):
    if name == 'navarre1586':
        relabel('navarre1586', lang='fr',
                reviews={'f333': ('B', (
                    'Overturns the per-document C. texts/f333_decryption.md is the raw decoder output, but the normalised '
                    'reading in NOTES.md (section f. 333) builds French sentences: "[162] desire fort d\'avoir des nouvelles '
                    'de [204] de [189] [190] ... et leur advis sur le chemin [qu\'i]l doit tenir ... [167] assurer qu\'aussi '
                    'tost que les reistres marcheront il montera a cheval; [166] et son frere sont de bonne volonte; il fault '
                    'avancer la levee et la faire marcher". The holes are the five name codes (no key material) and one '
                    'run after [190]; the clear text is abridged with ellipses.'))},
                step=(STEP + 'f. 333 read on the raw decode and on the normalised reading in NOTES.md. The cipher runs build '
                      'French sentences with the five name codes open (blocked: no key material); per-document C overturned to '
                      'B. Claim unchanged.'),
                step_result='worked')

    elif name == 'norfolk1570':
        relabel('norfolk1570', lang='en', cls='not read', method='not solved',
                method_basis=('Tomokiyo\'s key for the Mary-Norfolk series (from ff. 66/69/75, checked on f. 66r against its '
                              'decipherment) was applied to 23 line strips of f. 74r. The line-by-line reading has [..] holes or '
                              'unkeyed signs in about half the lines, so no reading is claimed (reading audit, 22 Oct 2026); once '
                              'the lines are re-read into sentences the method is read with known key.'),
                fraction=0.0,
                fraction_source=('Reading audit, 22 Oct 2026: f. 74r, the only document, is decoded, not read, so no tokens are '
                                 'in a document that reads. The field was "unknown" before.'),
                states={'f74r': ('decoded, not read', (
                    'Mary\'s Scots-English reads in places, but lines 1, 4-6, 8-10 and 12-17 carry [..] holes, a stain or '
                    'unkeyed nomenclator signs, so about half the sentences do not build (' + A + '); fix: re-read those '
                    'lines on the line strips (view/Lnn*.jpg, from the BL IIIF images) and settle the six unkeyed signs from '
                    'the sibling letters ff. 66, 69, 75, then write a running text with a modern English version.'))},
                extra=chain(gaps_add(('f. 74r as a running text: decoded, not read', 'not-attempted',
                                      're-read lines 1, 4-6, 8-10, 12-17 on the BL IIIF strips (fetch.py/strips.py) against '
                                      'Tomokiyo\'s key; place the signs ⊕, ⊘, ø, ⊗ and the dash signs from ff. 66/69/75'),
                                     ('unkeyed nomenclator signs ⊕, ⊘, ø, ⊗, {a—}, {o—}', 'open-codes',
                                      'not in Tomokiyo\'s key; each occurs once or twice')),
                            note_add('22 Oct 2026, reading audit: f. 74r decoded, not read (holes in about half the lines); '
                                     'class read -> not read, method -> not solved.')),
                step=(STEP + 'the f. 74r reading (texts/f74r_decryption.md, copied from NOTES) read line by line: about half the '
                      'lines carry [..] holes or unkeyed signs and the argument builds only in part. Per-document C confirmed; '
                      'f. 74r relabelled decoded, not read; class read -> not read; method read with known key -> not solved; '
                      'fraction_read unknown -> 0.'))

    elif name == 'numeric1916':
        fix = ('fix: copy Brice Dudout\'s edited texts and translations from his Wenmi pages into texts/, check the garbled '
               'groups against groups.tsv and the JACAR scans, and repair them.')
        relabel('numeric1916', lang='zh', fraction=0.11,
                fraction_source=('Reading audit, 22 Oct 2026: of the three codebooks only 辰密 (chenmi) reads in the repository; '
                                 '共密 and 容密 are decoded, not read. Contributor\'s counts (email 19 Oct 2026), chenmi 232 of '
                                 '239 groups read, over the 2,100 groups measured here: 232/2,100 = 0.11. The earlier 0.9238 '
                                 '(1,940/2,100, all three codebooks) is withdrawn as a reading figure.'),
                fraction_method='measured',
                states={'gongmi': ('decoded, not read', (
                            'Verbatim decoder output: N17, N18, N23 are near-clean classical Chinese, but N32, N33 and N35 '
                            'carry strings of wrong characters (代噸 for 代表, 圄會 for 國會) so whole clauses fail, and no '
                            'translation is in the folder (' + A + '); ' + fix)),
                        'rongmi': ('decoded, not read', (
                            'Most telegrams (N08, N11, N14, N19a) read, but N19b, N21 and V4D have clusters of mis-decoded '
                            'characters (圄會, 恢徨) and N21\'s second half is garbled; verbatim decoder output, no translation '
                            'in the folder (' + A + '); ' + fix))},
                extra=chain(gaps_add(('共密 and 容密 telegrams: decoded, not read', 'not-attempted',
                                      'the raw decode has garbled clusters (gongmi N32, N33, N35; rongmi N19b, N21, V4D); '
                                      'Dudout\'s Wenmi pages (bdudout.github.io/wenmi, reachable) carry translations; copy them '
                                      'in and repair the groups')),
                            note_add('22 Oct 2026, reading audit: gongmi and rongmi decoded, not read (garbled clusters in '
                                     'several telegrams, no translation in the folder); chenmi reads; fraction_read 0.9238 -> '
                                     '0.11.')),
                step=(STEP + 'the three decode files read telegram by telegram: chenmi reads; gongmi (N32, N33, N35) and rongmi '
                      '(N19b, N21, V4D) carry garbled character clusters that break whole clauses. Per-document C confirmed for '
                      'both; relabelled decoded, not read; class read in part kept; fraction_read 0.9238 -> 0.11.'))

    elif name == 'nunzio1718':
        relabel('nunzio1718', lang='it', fraction=0.889,
                fraction_source=('Reading audit, 22 Oct 2026: digit groups counted in lasry/364D-*.txt (the DECODE files with '
                                 'Lasry\'s decode rows): 34,678 groups, of which R154 (364D-1, 3,067) and R173 (364D-20, 770) are '
                                 'in documents decoded, not read: (34,678 - 3,837)/34,678 = 0.889. The earlier 0.9789 (groups '
                                 'given a value over the whole of 364D) is withdrawn as a reading figure.'),
                states={'R154': ('decoded, not read', (
                            'Lasry\'s decode rows, joined, start well ("l\'orrenda calunnia che il vicario ... sia stato '
                            'complice") but most later sentences carry runs of unread two-digit groups (70?, 00?, 11?, 80?) '
                            'and unresolved codes, so holes fall in most sentences (' + A + '); fix: re-read the two-digit '
                            'groups on the DECODE images (cookie) and fill the codes from key_extra.txt.')),
                        'R173': ('decoded, not read', (
                            'The despatch on the closing of the nunciature can be followed, but about half its sentences '
                            'carry unread groups or unresolved codes (<4238>, <4437>, 66?, 80?) (' + A + '; per-document D '
                            'softened to C, still failing); fix: re-read the groups on the DECODE images and fill the codes.'))},
                reviews={'R166': ('B', (
                            'Overturns the per-document C. Joined, the decode rows build Italian sentences: "io non ripeto le '
                            'ragioni ... il N.S. sostiene et l\'impegno da lui contratto col l\'Imp.re per [ec]citarlo alla '
                            'Guerra contro il Turco rendono cio indispensab[ile] alla N.S."; the holes are scattered codes, '
                            'and R168 (its duplicate) fills them.')),
                         'R168': ('B', (
                            'Overturns the per-document D (the reviewer\'s note was shared with three other letters). The '
                            'decode rows read as continuous Italian: "si manda il presente dispaccio con l\'espresso che '
                            'spedisce costi il Sig. Card. Acquaviva ... un Breve sospensivo di tutti gli indulti ... rendono '
                            'cio indispensabile alla N.S., la quale pronta a soffrir tutt[o] ma non mai la taccia di non avere '
                            'tentate tutte le strade"; a few groups open.')),
                         'R170': ('B', (
                            'Overturns the per-document D. Most sentences build ("non potendosi cio piu sperare mentre vedonsi '
                            'proseguire costi gli stessi disegni non meno nocivi alla Christianita per l\'impedimento che '
                            'recano alla continuazione della Guerra contro il Turco ..."); one stretch near the middle '
                            '(ripet.5?8.?) and a few codes are open.'))},
                extra=chain(gaps_add(('R154 and R173: decoded, not read', 'not-attempted',
                                      'runs of unread two-digit groups and open codes in most sentences; re-read the groups on '
                                      'the DECODE images (cookie at targets/bordeaux/decode/cookie.txt) and fill the codes from '
                                      'key_extra.txt, then write a running text with a translation')),
                            note_add('22 Oct 2026, reading audit: R154 and R173 decoded, not read; R166, R168, R170 overturned to '
                                     'B; fraction_read 0.9789 -> 0.889. Class already solved kept (Lasry\'s decryption, 2020).')),
                step=(STEP + 'the five flagged despatches read on Lasry\'s decode rows, joined into running text. R154 (D) and R173 '
                      '(C) have holes in most or half their sentences: relabelled decoded, not read. R166, R168 and R170 build '
                      'Italian sentences with scattered open groups: overturned to B. Class already solved kept; fraction_read '
                      '0.9789 -> 0.889 (groups in documents that read).'))

    elif name == 'orbais':
        relabel('orbais', lang='fr', cls='not read', method='not solved',
                method_basis=('The cipher runs of no. 62 were decoded with the key of the letter\'s own volume (fr. 3413) and '
                              'scored with the fr-1600-letters model, but the clear text of the letter is not transcribed, so '
                              'the runs stand as isolated groups ("la protect", "Cassin", "j\'ay veu ung advis") and no sentence '
                              'can be built (reading audit, 22 Oct 2026); with the clear text written out around them the method '
                              'is read with known key.'),
                fraction=0.0,
                fraction_source=('Reading audit, 22 Oct 2026: no. 62, the only document, is decoded, not read, so no tokens are '
                                 'in a document that reads. The earlier 0.824 (75 of 91 cipher signs in runs that read as sense, '
                                 'decode62.py) is withdrawn as a reading figure.'),
                states={'no62': ('decoded, not read', (
                    'One line per cipher group, not running text: the groups read as words, two are "(no sense)", and the '
                    'letter\'s clear text is not transcribed, so no connected sentence can be built (' + A + '); fix: '
                    'transcribe ff. 126r-127r from Gallica (btv1b52510705j, canvases 259-261) and set the cipher runs in '
                    'their clauses, with a translation.'))},
                extra=chain(gaps_add(('no. 62 as a running text: clear text not transcribed', 'not-attempted',
                                      'transcribe the clear text of ff. 126r-127r from Gallica (reachable through openapi.bnf.fr '
                                      'IIIF) and place the 14 cipher runs in it')),
                            note_add('22 Oct 2026, reading audit: no. 62 decoded, not read (cipher groups without their clear '
                                     'context); class read in part -> not read, method -> not solved, fraction_read 0.824 -> 0.')),
                step=(STEP + 'texts/no62_decryption.md is one line per cipher group with no clear text around it; the groups '
                      'read as words but no sentence can be built. Per-document D confirmed; no. 62 relabelled decoded, not read; '
                      'class read in part -> not read; method read with known key -> not solved; fraction_read 0.824 -> 0.'))

    elif name == 'papai1706':
        relabel('papai1706', lang='hu',
                reviews={'R795': ('B', (
                    'Overturns the per-document C. The middle dots in R795_read2.txt are not holes: decode_nulls.py prints '
                    'the groups above 322 as "·", and R795 has 251 such nulls (NOTES table), against a handful in the other '
                    'letters. With the nulls dropped the text is the same unspaced Hungarian as the ten letters that pass '
                    '("pénz a [Fejedelem] adot kezembe ... vélem Horváth Ferenc urammal").'))},
                step=(STEP + 'R795 re-read: its "·" marks are the 251 declared nulls (groups above 322), not gaps; without them '
                      'the letter reads like the other ten. Per-document C overturned to B. Claim unchanged.'),
                step_result='worked')

    elif name == 'poyntz1527':
        relabel('poyntz1527', lang='en', fraction=0.38, fraction_method='estimated',
                fraction_source=('Estimated, reading audit 22 Oct 2026, by cipher runs: R8567\'s three runs (plaintext.txt, 44 '
                                 'words) are in the repository and read; R8565\'s five bands of Tuke\'s decipherment are not '
                                 'transcribed here: 3 of about 8 runs = 0.38. No token count of the cipher exists. The earlier 1 '
                                 'is withdrawn as a reading figure.'),
                states={'R8565': ('decoded, not read', (
                    'Nothing of the decipherment is in the repository: only three calendar paraphrases in NOTES.md (' + A +
                    '). Excerpt only: the full decipherment is Tuke\'s, interlinear on the DECODE images of R8565 and printed '
                    'in italics in Letters and Papers IV ii no. 3271 (British History Online, pp. 1483-1486); fix: transcribe '
                    'the five bands from the DECODE images (cookie) and check them against L&P.'))},
                extra=chain(gaps_add(('R8565: Tuke\'s decipherment not transcribed', 'not-attempted',
                                      'the five bands of interlinear decipherment are on the DECODE images (cookie at '
                                      'targets/bordeaux/decode/cookie.txt) and in L&P IV 3271 on British History Online; '
                                      'transcribe them and check against the signs with Tomokiyo\'s Lee-Worcester key')),
                            note_add('22 Oct 2026, reading audit: R8565 decoded, not read (no text of it in the repository); '
                                     'class already solved kept (Tuke\'s decipherment, in print); fraction_read 1 -> about 0.38.')),
                step=(STEP + 'R8567\'s plaintext.txt reads; R8565 has no text in the repository (calendar paraphrases only). R8565 '
                      'relabelled decoded, not read, with an excerpt note pointing to the DECODE images and L&P IV 3271, both '
                      'reachable; class already solved kept; fraction_read 1 -> about 0.38 (estimated by runs).'),
                step_result='partial')

    elif name == 'r1212':
        relabel('r1212', lang='la',
                reviews={'R1212': ('B', (
                    'Overturns the per-document C. On pp. 3-4 the bracketed cipher runs, taken in order, are themselves a '
                    'continuous Latin text: "horum omnium motuum et perniciosarum factionum unicus author et certissimus est '
                    'Franciscus Kendi ... desperatus de defensione sacre maiestatis vestre posteaquam intellexerunt arces '
                    'Babolchia et alias amissas esse ... et me sub quodam praetextu alliciebat blandiciis suis in isto '
                    'Episcopatu debere permanere sed quod Albam cederem ... Hec sunt verba Francisci Kendi ad me in Vasarhel '
                    'sub comiciis"; the clear words between them are separate scraps. Holes: one run [...] and nine unkeyed '
                    'codes.'))},
                step=(STEP + 'reading_p3-4.md re-read: the cipher runs of pp. 3-4, read in order, make continuous Latin sentences '
                      '(the clear words between them do not belong to them); pp. 1-2 read already. Per-document C overturned to B. '
                      'Claim unchanged.'),
                step_result='worked')

    elif name == 'r2242':
        relabel('r2242', lang='nl',
                reviews={'R2242 p3': ('B', (
                            'Overturns the per-document C. Divided into words the unspaced Dutch builds sentences: "men heeft de '
                            'offeciers en de trouppes zoo wel uit malkander gelegen ... ook is er geen de minste saamenhang '
                            'tussen dezelve; zy zijn geheel verstrooyd en zonder hooft ... men heeft de ratificatie van ons met '
                            'frankrijk gepubliceert ofschoon de ratificatie zelve nog niet gekoomen was". The holes are single '
                            'word signs with no key material (<Δ>, <%>, <T with bar>), heaviest in the two sentences of lines '
                            '8-10.')),
                         'R2242 p4': ('B', (
                            'Overturns the per-document C. "Als engeland maar blyft persisteern om het tegenwoordig gouvernement '
                            'niet te erkennen dan zoo zy geen robespierrismus durven te introduseeren, daar <%> zeer veel '
                            'dispositie is" builds; the holes are single word signs and the ink-blotted P.S.'))},
                step=(STEP + 'decrypt_p3.txt and decrypt_p4.txt divided into words and read: the Dutch builds sentences; the open '
                      'tokens are single word signs with no key material and two ink blots. Per-document C overturned to B for '
                      'both pages. Claim unchanged.'),
                step_result='worked')

    elif name == 'r9416':
        relabel('r9416', lang='de',
                states={1: ('decoded, not read', (
                    'The contemporary interlinear gloss of f. 262: page B (15 lines) reads as German with a few holes, but '
                    'page A (25 lines) has "..." and [?] in most lines and A09-A11 carry no visible gloss, so the first page '
                    'does not build sentences (' + A + '); fix: transcribe the f. 262 signs and key them from page B\'s full '
                    'gloss, then read page A from its signs.'))},
                extra=chain(entry_note(0, 'Excerpt only: recto lines 11-16 are read (reading_p3_11-16.txt, 199 of 3,313 codes); '
                                          'the rest of f. 263 is a working decrypt, not counted (' + A + ').'),
                            gaps_add(('f. 262 page A from its signs', 'not-attempted',
                                      'the f. 262 signs are not transcribed; page B\'s gloss covers every line and gives a key; '
                                      'transcribe both pages from the DECODE images (cookie) and read page A where the gloss is '
                                      'faint')),
                            note_add('22 Oct 2026, reading audit: f. 262 decoded, not read (page A gloss faint); the f. 263 '
                                     'entry counts only recto ll. 11-16 (excerpt note). Claim unchanged.')),
                step=(STEP + 'gloss.txt (f. 262) read: page B builds, page A does not; relabelled decoded, not read. The f. 263 '
                      'entry is read only on recto ll. 11-16, which is what fraction_read 0.06 counts; excerpt note added. '
                      'Claim unchanged.'),
                step_result='partial')

    elif name == 'rakoczi1704':
        fix = ('fix: re-read the groups on the images (img/, DECODE cookie) against R639 and write a normalised French text '
               'with word division and a translation.')
        relabel('rakoczi1704', lang='fr', cls='read in part', fraction=0.182,
                fraction_source=('Reading audit, 22 Oct 2026: groups counted in tr/ (comment lines excluded): R852 523, R912 '
                                 '1,630, R922 722. R912 and R922 are decoded, not read, so only R852, read from its clear copy, '
                                 'counts: 523/2,875 = 0.182. The earlier 0.974 (2,290 of 2,352 R912/R922 groups keyed) is '
                                 'withdrawn as a reading figure.'),
                states={'R922': ('decoded, not read', (
                            'The image read is syllable-split with stray capitals and code numbers; after the first lines the '
                            'sentences break ("que La ve N te On donne A tion en au Oit est E fait"), with misreadings in nearly '
                            'every line (' + A + '); ' + fix)),
                        'R912': ('decoded, not read', (
                            'Same syllable-split read: isolated clauses (the King of Sweden, the Cossacks, Muscovy) can be '
                            'guessed, but most lines are corrupted ("arme donne E au le Palitin de ki O vi D Ja Y A P P ri S") '
                            '(' + A + '); ' + fix))},
                extra=chain(gaps_add(('R912 and R922: decoded, not read', 'not-attempted',
                                      'the image reads are syllable-split with misreadings in most lines; re-read the groups on '
                                      'the images (img/, DECODE cookie) with the R639 key and write normalised French with a '
                                      'translation')),
                            note_add('22 Oct 2026, reading audit: R912 and R922 decoded, not read; R852 reads (clear copy); '
                                     'class read -> read in part; fraction_read 0.974 -> 0.182.')),
                step=(STEP + 'R912_image_read.txt and R922_image_read.txt read: syllable-split output with misreadings in most '
                      'lines; no coherent sentences after the openings. Per-document D confirmed for both; relabelled decoded, '
                      'not read; R852 reads from its clear copy; class read -> read in part; fraction_read 0.974 -> 0.182.'))

    elif name == 'rakoczi1711':
        relabel('rakoczi1711', lang='la', cls='not read', method='not solved',
                method_basis=('The clerk\'s contemporary interlinear decipherment covers every ciphered stretch (2,524 of 2,531 '
                              'groups) and the key was rebuilt from it, but the merged text in R483_clerk.txt interleaves clear '
                              'and cipher lines out of reading order with doubts and alternatives on most lines, so no reading is '
                              'claimed (reading audit, 22 Oct 2026); once it is written out as a running Latin text the method '
                              'is read from existing decipherment.'),
                fraction=0.0,
                fraction_source=('Reading audit, 22 Oct 2026: R483, the only document, is decoded, not read, so no tokens are in '
                                 'a document that reads. The earlier 0.997 (2,524 of 2,531 groups under the clerk\'s interlinear) '
                                 'is withdrawn as a reading figure.'),
                states={'R483': ('decoded, not read', (
                    'The themes (the "Pax Caroliana", the Palatine, the Diet) can be followed, but most lines carry "?" doubts '
                    'or alternatives (latens?/haerens?), a struck stretch and unreadable words, and the clear passages are '
                    'interleaved line by line rather than in reading order, so many sentences are only half secure (' + A +
                    '); fix: re-read the clear text and the interlinear on the images (DECODE cookie) and write one running '
                    'Latin text, checked with the rebuilt key, with a translation.'))},
                extra=chain(gaps_add(('R483 as a running text: decoded, not read', 'not-attempted',
                                      'write the clerk\'s decipherment and the clear passages out in reading order from the '
                                      'images (DECODE cookie), settle the doubtful words with the rebuilt key, translate')),
                            note_add('22 Oct 2026, reading audit: R483 decoded, not read (doubts on most lines, text not in '
                                     'reading order); class read -> not read, method -> not solved until it is written out.')),
                step=(STEP + 'R483_clerk.txt read: most lines carry doubts or alternatives and the clear passages are interleaved '
                      'out of order, so many sentences are only half secure. Per-document C confirmed; relabelled decoded, not '
                      'read; class read -> not read; method read from existing decipherment -> not solved; fraction_read 0.997 '
                      '-> 0.'))

    elif name == 'ranzo1528':
        relabel('ranzo1528', lang='it', fraction=0.717,
                fraction_source=('Reading audit, 22 Oct 2026: letter 4 (fr. 4050, 1,559 of the 6,428 occurrences in '
                                 'lasry/alignment.tsv) is decoded, not read. The bar measure per letter applied to the four '
                                 'letters that read: fr. 2988 f. 2 96.2% of 818, ff. 9-10 97.0% of 1,781, fr. 3022 no. 20 94.4% '
                                 'of 1,314, fr. 6638 89.0% of 956 = 4,606 of 6,428 = 0.717. The earlier 0.929 (all five letters) '
                                 'is withdrawn as a reading figure.'),
                states={'fr4050': ('decoded, not read', (
                    'The opening and closing (the cipher received; Madrid, 10 March 1528) read, but 54 of 128 lines carry an '
                    'unresolved {code} on top of "?" guesses, and in the middle runs of codes break most sentences ("{a205} '
                    '{t72} e re sol a menti a {p334} i di se g ni", "{a307} era a {s388} a re {q46}") (' + A + '); fix: check '
                    'the codes against the fr. 4050 images and the four sibling letters.'))},
                extra=chain(gaps_add(('letter 4 (fr. 4050): decoded, not read', 'not-attempted',
                                      '54 of 128 lines carry an open code; read the codes from context across the five letters '
                                      'and check them on the Gallica images of fr. 4050 ff. 79-81')),
                            note_add('22 Oct 2026, reading audit: letter 4 (fr. 4050) decoded, not read; fraction_read 0.929 -> '
                                     '0.717.')),
                step=(STEP + 'texts/lasry_decode_letter4.txt read: the opening and closing build Italian sentences, but the '
                      'middle has runs of open codes in most sentences. Per-document C confirmed; letter 4 relabelled decoded, '
                      'not read; class read in part kept; fraction_read 0.929 -> 0.717.'))

    elif name == 'richelieu':
        relabel('richelieu', lang='fr',
                states={0: ('decoded, not read', (
                    'The recovered key applied to Tomokiyo\'s partial transcription: cipher letters run together, the clear '
                    'text only in part, so the lines do not join into sentences on their own (' + A + '); the reading is '
                    'the Avenel entry.'))},
                reviews={1: ('A', (
                    'Avenel\'s printed text with the codes resolved reads and translates; it is abridged with ellipses.'))},
                extra=chain(entry_note(1, 'Excerpt only: the full printed text is Avenel, Lettres de Richelieu III (1858), nos. '
                                          'CXCIX and CCV (' + A + ').'),
                            gaps_add(('the full text of ff. 87 and 89', 'not-attempted',
                                      'only an abridged copy of Avenel\'s text is in texts/; copy nos. CXCIX and CCV in full from '
                                      'Avenel, Lettres de Richelieu III (1858), on Gallica or archive.org')),
                            note_add('22 Oct 2026, reading audit: the raw key decode is decoded, not read; Avenel\'s text reads '
                                     '(excerpt). Class already solved kept.')),
                step=(STEP + 'the two entries read: the raw decode of the partial transcription does not join into sentences '
                      '(decoded, not read); Avenel\'s printed text reads (A, excerpt note added). Class already solved kept.'),
                step_result='partial')

    elif name == 'rome1536':
        relabel('rome1536', lang='fr', fraction=0.91,
                fraction_source=('Estimated, reading audit 22 Oct 2026: the letter-weighted figure for the seven fr. 3053 records '
                                 '(about 18,240 of 19,202 signs, 0.95, see below) over a denominator that now includes fr. 3071 '
                                 'no. 4 (about 840 signs), which is decoded, not read: 18,240/20,042 = 0.91. Before: letter-weighted '
                                 'after pass 5 on the fr. 3053 records: R4233 1,904/2,006; R4234 ~0.94 of 5,369; R4235 '
                                 '2,035/2,108; R4238 767/812; R4239 ~0.94 of 4,925; R4240 829/842; R4247 3,098/3,140; CER against '
                                 'contemporary clear copies 3-8%. The 0.95 is withdrawn as the target figure.'),
                states={'macon1537': ('decoded, not read', (
                    'The file itself says only 35-40% of the cipher is read confidently: the continuous reading has good '
                    'sentences (Novara, the Cosimo marriage, the council of Mantua) between runs of "..." and [---], and the '
                    'f. 9v part is fragments (' + A + '); fix: re-transcribe f. 9r ll. 3-25 by sign shape from the Gallica '
                    'scan, as pass 5 did for fr. 3053, and read f. 9v against the slip f. 9bis.'))},
                reviews={'R4234': ('B', (
                            'Overturns the per-document C. The pass-5 running reading of ff. 16r-17v builds long French '
                            'sentences (the soldiers raised for Parma and Piacenza, the Milan plan, Contarini); the [?] holes '
                            'are scattered, densest on f. 16v, and f. 18r\'s elisions are in the clear passages, not the cipher.')),
                         'R4239': ('B', (
                            'Overturns the per-document C. Letter 2 (f. 36r-v) and the second paragraph of letter 1 (Ridolfi, '
                            'the duke of Urbino) read in whole sentences; the first paragraph of letter 1 is summarised with '
                            'elisions and f. 38r ll. 5-14 are read only in part (listed as gaps).'))},
                extra=chain(gaps_add(('fr. 3071 no. 4 (11 Apr 1537): decoded, not read', 'not-attempted',
                                      'about 35-40% of its cipher read; re-transcribe f. 9r ll. 3-25 by sign shape from the '
                                      'Gallica native scan and decode with macon_decode.py, then read f. 9v with the slip f. 9bis'),
                                     ('R4239 letter 1, f. 35r-v first paragraph, as a running text', 'not-attempted',
                                      'the running reading is summarised with elisions there; write it out from the per-line '
                                      'record in pass5/R4239_pass5.md')),
                            note_add('22 Oct 2026, reading audit: R4234 and R4239 overturned to B; fr. 3071 no. 4 decoded, not '
                                     'read; fraction_read 0.95 -> about 0.91.')),
                step=(STEP + 'R4234 and R4239 pass-5 running readings read: both build French sentences with scattered holes '
                      '(C overturned to B); fr. 3071 no. 4 is read only 35-40% by its own count and relabelled decoded, not '
                      'read. Class read in part kept; fraction_read 0.95 -> about 0.91.'))

    elif name == 'rupert':
        note = ('Not deciphered: the file is the ciphertext ({what}); no key of Add MS 72438 fits, so the entry is listed as '
                'a ciphertext, not a reading (' + A + ').')
        relabel('rupert', lang='en',
                states={'maurice1645': ('decoded, not read', note.format(what='numeric groups from Warburton iii. 133')),
                        'addms72438-f9': ('decoded, not read', note.format(what='number groups with a few clear words')),
                        'addms72438-f10': ('decoded, not read', note.format(what='number groups with a few clear words')),
                        'r8433-trevor1645': ('decoded, not read', note.format(
                            what='clear English with undeciphered number groups')),
                        'addms72438-f104': ('decoded, not read', note.format(what='an all-numeric sheet'))},
                step=(STEP + 'the five numeric documents carry no state and so counted as read by default; each is an '
                      'undeciphered ciphertext and is now marked decoded, not read. Claim unchanged (fraction_read already '
                      'counts them at 0).'),
                step_result='worked')

    elif name == 'sabran1633':
        relabel('sabran1633', lang='fr',
                states={1: ('decoded, not read', (
                            'A partial decryption with two crib values only; the file says "Not a reading": most lines are '
                            '"?" strings inside brackets and only the opening clause translates (' + A + '); blocked: another '
                            'key, 136 signs, too short to break alone.')),
                        2: ('not prose', (
                            'A 17-sign marginal run of two words ("[c]a d\'avoir / [s]antimant"), the words of the clear text '
                            'at the "+" mark (' + A + ').'))},
                step=(STEP + 'Baluze 156 f. 157r (two crib values, "not a reading" by its own heading) relabelled decoded, not '
                      'read; the f. 218r margin (two words) relabelled not prose. Claim unchanged: f. 157r was already counted '
                      'unread and its gap is blocked (too-short).'),
                step_result='worked')

    elif name == 'santacruz1399':
        relabel('santacruz1399', lang='la',
                extra=chain(setkey('texts_withheld', (
                                'The only text is Puig y Puig\'s print: Sebastián Puig y Puig, Pedro de Luna, último papa de '
                                'Aviñón (Barcelona 1920), appendix XXIX, pp. 469-470, deciphered passages in italics. It was '
                                'read on Google Books (CuOlkxWnk-EC) on 23 Sept 2026; Google Books and HathiTrust now block '
                                'scripted access and archive.org has no copy, so nothing of the letter is in the repository '
                                '(' + A + ').')),
                            entry_note(0, 'Not in the repository: Google Books blocks scripted access (' + A + ').'),
                            gaps_add(('Puig\'s printed text of the letter (pp. 469-470), not in the repository',
                                      'needs-physical-access',
                                      'Google Books blocks automated access; HathiTrust is behind a Cloudflare challenge; '
                                      'archive.org has no copy; a copy of the book is needed')),
                            note_add('22 Oct 2026, reading audit: no text of the letter is in the repository; texts_withheld set '
                                     'with the citation. Class already solved kept (the text exists in print).')),
                step=(STEP + 'the only text is a Google Books link, now blocked to scripts, and archive.org has no copy of Puig '
                      '1920; outcome.texts_withheld set with the citation, class already solved kept.'),
                step_result='partial')

    elif name == 'segur':
        relabel('segur', lang='fr',
                reviews={'f288v': ('B', (
                    'Overturns the per-document C. reading.md\'s notes resolve most word signs from context ({gne} = Je, '
                    '{na} = nouvelles/affaires, {Ra} = faictes, {qu} = vous), and with them the slip reads: "Je suis en '
                    'extreme peine de n\'avoir eu de vos nouvelles ...; je ne sçay [par où vous] escrire, ne à qui, ne en '
                    'quel estat sont nos affaires ... faictes s\'il vous est possible la plus grande levée qui ayt esté '
                    'faite". Open: the date sign {e}, the name signs {H} {L}, {pe} {pu} and {qua}.'))},
                step=(STEP + 'f. 288v re-read with the word-sign values given in reading.md\'s notes: the slip builds French '
                      'sentences with scattered open name and date signs. Per-document C overturned to B. Claim unchanged.'),
                step_result='worked')

    elif name == 'siena11':
        relabel('siena11', lang='it',
                reviews={'R4800': ('B', (
                    'Overturns the per-document C. Both blocks of Lasry\'s decryption build Italian sentences with an English '
                    'translation; the "?" fall in one sentence of block A, around one sign lost in a hole in the paper '
                    '(illegible), and in five single words of a 393-sign text (too short to settle), both outside blockers.'))},
                step=(STEP + 'lasry_report.md read: both cipher blocks build sentences and translate; the doubts are one holed '
                      'sign and five words, with outside blockers. Per-document C overturned to B. Claim unchanged.'),
                step_result='worked')
    else:
        raise SystemExit('no entry for ' + name)
    print('ok', name)


if __name__ == '__main__':
    for n in sys.argv[1:]:
        run(n)
