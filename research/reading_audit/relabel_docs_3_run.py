"""Second-wave relabel (RELABEL_DOCS_BRIEF.md) for the targets in relabel_docs_3.txt, 22 Oct 2026.

Uses relabel_docs_3.py (a copy of relabel_docs_0.py: splices only the changed spans of each profile.json).
Run once:  PYTHONUTF8=1 python research/reading_audit/relabel_docs_3_run.py [folder ...]
"""
import sys
from relabel_docs_3 import relabel

A = 'reading audit, 22 Oct 2026'
STEP = 'Reading audit, per-document pass (George Lasry\'s sentence test): '
COOKIE = 'the shared DECODE cookie (targets/bordeaux/decode/cookie.txt)'


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


def sp106(folder, rec, lang, fr_old, groups):
    why = ('Lasry\'s interlinear plaintext of {} is on the DECODE record, behind its login, and was kept out of the '
           'repository as his work; no copy is in any checkout, so nothing of the letter can be read here (' + A + '); fix: '
           're-fetch it with ' + COOKIE + ' and check it with apply_key.py.').format(rec)
    relabel(folder, lang=lang, states={rec: ('decoded, not read', why)},
            fraction=0.0,
            fraction_source=('Reading audit, 22 Oct 2026: the letter\'s text is not in the repository (Lasry\'s files were '
                             'git-ignored and are in no checkout), so no tokens are in a document that reads here. The '
                             'earlier ' + fr_old + ' (apply_key.py: ' + groups + ' with a value in Lasry\'s key) is withdrawn '
                             'as a reading figure.'),
            extra=chain(gaps_add((rec + ': Lasry\'s plaintext not in the repository', 'not-attempted',
                                  'his interlinear and plaintext files are on the DECODE record (reachable with ' + COOKIE +
                                  '); fetch them into decode/ (git-ignored, his work), grade them as sentences, and ask him '
                                  'whether a reading copy may be kept')),
                        note_add('22 Oct 2026, reading audit: no text of the letter is in the repository; decoded, not read. '
                                 'Class kept: Lasry\'s decipherment exists on DECODE (2020).')),
            step=(STEP + 'Lasry\'s plaintext of ' + rec + ' is on DECODE only (git-ignored copy in no checkout); nothing '
                  'could be read. Relabelled decoded, not read; class already solved kept (Lasry\'s decipherment); '
                  'fraction_read ' + fr_old + ' -> 0.'),
            step_result='partial')


def run(name):
    if name == 'soglia1848':
        relabel('soglia1848', lang='it',
                reviews={'dispatch': ('B', (
                    'Overturns the per-document C. texts/plaintext.md builds Italian sentences throughout and its English '
                    'translates every sentence: the holes are the date of the earlier letter (five code groups), Lützow\'s '
                    'title [8227] and four single code words ([8704], [8093][8102], [8136], [8131]) in a one-part code with '
                    'no key, and the parenthesised words are code values bracketed by the code\'s alphabetical order. '
                    'Scattered codes, no clause unbuilt.'))},
                step=(STEP + 'texts/plaintext.md read: every sentence builds and the English translates; the open items are '
                      'single code groups and one date. Per-document C overturned to B. Claim unchanged.'),
                step_result='worked')

    elif name == 'soria1523':
        relabel('soria1523', lang='es',
                reviews={'R9491': ('B', (
                    'Overturns the per-document C, which was given on the superseded second pass (read_r9491_b.md). The '
                    '5 Oct 2026 re-read (measure/kb_r9491.txt, 476 of 529 units) builds the letter: "que el duque de [Sena] '
                    'quiere que se govierne por la republica ... rezia cosa es aver de hazerse qualquiera cosa por voto de '
                    'muchos ... piense en ello V. Señoria, porque [xif] importa a su Magestad el buen govierno de aquella '
                    'ciudad". Holes: the end of the first sentence ([taf], [tu] [pud]) and the run [zib] [a] [sib] ... in '
                    'the fourth, all single key-B code groups with no duplicate or sibling (open-codes).')),
                         'R9494/R9495/R9496': ('B', (
                    'Overturns the per-document C, which was given on the first reading (read_r9494.md). The 5 Oct 2026 '
                    're-read with R9495/R9496 collated (measure/kb_r9494.txt, 328 of 357 units) builds every sentence: '
                    '"Beurren es el portador desta, al qual e informado de todo lo de aca ... con un correo piamontes ... '
                    'provea como se an de [dar veinte] y ocho mil escudos al dotor Prantener en Costancia para pagar '
                    'ciertos [suizos] ... y [otros] doze mil al tesorero Vionet en Geneva". Holes: a destination, a day '
                    'count and single code groups (te, per, zu, tol), spelled the same in all three copies.'))},
                extra=chain(entry_note(1, 'read_r9491_b.md is the superseded second pass; the reading is measure/kb_r9491.txt (5 Oct 2026).'),
                            entry_note(3, 'read_r9494.md is the first reading; the collated reading is measure/kb_r9494.txt (5 Oct 2026).')),
                step=(STEP + 'R9491 and R9494-96 re-read on the 5 Oct 2026 measured readings (kb_r9491.txt, kb_r9494.txt); '
                      'the per-document grades had been given on the superseded read_r9491_b.md and read_r9494.md. Both '
                      'build sentences with single code groups open; per-document C overturned to B twice. Claim unchanged.'),
                step_result='worked')

    elif name == 'soria1527':
        relabel('soria1527', lang='es',
                states={'R9487': ('decoded, not read', (
                    'The Claro is torn: section A and the closing paragraph build sentences, but B and the start of C are '
                    'half-lines ending in [...] and cannot be assembled, so about half the page reads (' + A + '); fix: '
                    'transcribe the intact f. 31v cipher block and decode it with Soria\'s 1523 key B (targets/soria1523/'
                    'keyB.md) to fill the torn sections.'))},
                fraction=0.5, fraction_method='estimated',
                fraction_source=('Reading audit, 22 Oct 2026, estimated from claro.md: section A and the closing paragraph '
                                 'read (about half the lines of the Claro); B and the start of C are torn. No token count: '
                                 'the cipher is not transcribed.'),
                extra=chain(gaps_add(('Claro B and the start of C (torn): decoded, not read', 'not-attempted',
                                      'the f. 31v cipher block (9 intact lines) is on the DECODE images (decode/, '
                                      'git-ignored; reachable with ' + COOKIE + '); transcribe it and decode with key B '
                                      'from targets/soria1523/keyB.md'),
                                     ('last cipher lines of f. 31r and f. 33r', 'illegible', 'torn and faded')),
                            note_add('22 Oct 2026, reading audit: the Claro reads for section A and the closing paragraph only; '
                                     'decoded, not read. Class already solved kept (read at the time).')),
                step=(STEP + 'claro.md read: A and the closing paragraph build sentences, B and the start of C are torn '
                      'half-lines. R9487 relabelled decoded, not read; class already solved kept (contemporary '
                      'decipherment); fraction_read estimated 0.5; the f. 31v cipher with key B noted as a workable gap.'),
                step_result='partial')

    elif name == 'sp106r787':
        sp106('sp106r787', 'R787', 'fr', '0.9802', '1538 of 1569 groups')
    elif name == 'sp106r924':
        sp106('sp106r924', 'R924', 'en', '0.9195', '1850 of 2012 groups')
    elif name == 'sp106r929':
        sp106('sp106r929', 'R929', 'en', '0.842', '293 of 348 groups')

    elif name == 'sp106r927':
        relabel('sp106r927', lang='fr',
                states={'R927 f. 242': ('not prose', (
                    'Not a separate text: image P2 is f. 243 photographed with the paper flap folded down (WAINUT, PR #30). '
                    'Its re-transcription checks hand_p3.txt sign for sign; the words under the flap are [..] or restored '
                    'from f. 243, and the letter is read under the f. 243 entry (' + A + ').'))},
                step=(STEP + 'the f. 242 entry checked: it is the same leaf as f. 243 with the flap down, about half its lines '
                      'holes or restored from f. 243. Relabelled not prose (a transcription check, not a text); it was '
                      'already reported apart from fraction_read. Claim unchanged.'),
                step_result='worked')

    elif name == 'stowe166':
        frag = ('Overturns the per-document C. The cipher passage is {} inside Edmondes\'s clear despatch, which carries the '
                'sentence; the passage reads in full as English{}. A short cipher run, not a hole: nothing in it is unread{}.')
        relabel('stowe166', lang='en',
                reviews={'R7773': ('A', frag.format('one clause, "that his faith is not vendible", the King\'s words', '', '')),
                         'R7775': ('B', frag.format('one line, "{£2} execute an enterprise vppon rheins wch would be the '
                                                    'carryinge of the place and him"', '', ' but the person sign {£2} '
                                                    '(probably Guise), which has no key (no-key-material)'))},
                step=(STEP + 'R7773 and R7775 read in reading.txt: each is a single cipher clause inside a clear despatch and '
                      'reads in full (R7775 with one person sign open). Per-document C overturned (A, B). Claim unchanged.'),
                step_result='worked')

    elif name == 'swieten1759':
        relabel('swieten1759', lang='fr',
                states={'R957': ('decoded, not read', (
                    'The first and third sentences build, but "On promet (?) de toujours de la part des François" does not, '
                    'and "le prince de Con[...] [323 441] qui vous formez des prétensions" has a garbled clause, so half the '
                    'sentences have holes (' + A + '); fix: re-read runs 2 and 4 of R957 on the scans against the '
                    'alphabetical table. Excerpt only: the cipher runs are given in full, the clear text of the letter '
                    'around them in extract; the full letter is on the DECODE images (R957).'))},
                cls='read in part', fraction=0.597, fraction_method='estimated',
                fraction_source=('Reading audit, 22 Oct 2026: tokens in documents that read. R956 (343 groups) reads; R957 '
                                 '(210 groups) is decoded, not read. R956 has about 13 groups open (147 100 126 148, 170 271 '
                                 '289 337, 290 313 316 313 373), so about 330 of 553 groups = 0.597, counted by hand from '
                                 'READING.md. The earlier 0.962 (532 of 553 groups decrypted) is withdrawn as a reading figure.'),
                extra=chain(entry_note(1, 'Excerpt only: the cipher runs are given in full, the clear text around them in '
                                          'extract; the full letter is on the DECODE images (R956).'),
                            gaps_add(('R957 runs 2 and 4 ("On promet ... François"; "le prince de Con[...] ... qui vous formez '
                                      'des prétensions"): decoded, not read', 'not-attempted',
                                      're-read on the scans against the alphabetical table and the clear text around them')),
                            note_add('22 Oct 2026, reading audit: R956 reads; R957 is decoded, not read. Class read -> read '
                                     'in part; fraction_read 0.962 -> 0.597 (estimated, tokens in R956).')),
                step=(STEP + 'READING.md read per letter: R956 builds French sentences with scattered name groups open; R957 '
                      'has holes or garbled clauses in two of its four sentences. R957 relabelled decoded, not read; class '
                      'read -> read in part; fraction_read 0.962 -> 0.597 (estimated); excerpt notes added to both.'),
                step_result='failed')

    elif name == 'urquhart':
        relabel('urquhart', lang='en',
                states={'distich': ('decoded, not read', (
                    'Not deciphered: texts/distich_decryption.md records no decipherment, only a failed test of the '
                    'Proquiritation rule (34 of 64, chance); the construction and key text are unknown (' + A + ').'))},
                step=(STEP + 'the distich entry carried no state although outcome.parts has it not solved; relabelled '
                      'decoded, not read with the note "not deciphered". Claim (read in part, octastich read) unchanged.'),
                step_result='worked')

    elif name == 'vargas1552':
        relabel('vargas1552', lang='es',
                states={'R9967': ('decoded, not read', (
                    'Not deciphered here and nothing transcribed: the marginal decipherment of the time and the cipher are '
                    'on the DECODE images only (' + A + '); fix: fetch the 16 images with ' + COOKIE + ' and transcribe '
                    'the marginal decipherment, checking it with the Imperial Cipher of 1544-1554.'))},
                extra=chain(gaps_add(('R9967: the marginal decipherment, not transcribed', 'not-attempted',
                                      'DECODE R9967 images (16 pp.) reachable with ' + COOKIE + '; not fetched yet')),
                            note_add('22 Oct 2026, reading audit: no text of the letter is in the repository; decoded, not '
                                     'read. Class already solved kept (deciphered in the margin at the time, per Tomokiyo).')),
                step=(STEP + 'no transcription or decipherment of R9967 is in the repository; the marginal decipherment is on '
                      'the DECODE images (reachable with the shared cookie). Relabelled decoded, not read; class already '
                      'solved kept; a not-attempted gap recorded for the re-reading wave.'),
                step_result='partial')

    elif name == 'visconti1528':
        relabel('visconti1528', lang='it',
                reviews={'f154': ('B', (
                    'Overturns the per-document C. Read on final.md\'s Full text: the recto (1038 of the 1337 glyphs) builds '
                    'the council narrative sentence by sentence ("Il consiglio de heri fuo per tirare queli capitanei ... '
                    'a la opinione che no fuse andase a Milano ... E questa fuo inventione de Francesco, dita in secreto ha '
                    'queli de la Signoria ... aciò che se vincese la opinione de andare a Milano"), with holes at r07, r09 '
                    'and the r10-12 pairs; the verso translates in gist ("the Duke of Urbino and the proveditor have said '
                    'we will go to cut the road between Milan and Pavia") with v03 illegible and single signs open. The '
                    'holes are code groups (no key), blotted signs and one-off signs; 93.3% is below the read bar, which the '
                    'class read in part already says.'))},
                step=(STEP + 'final.md read: the recto builds sentences with scattered holes, the verso translates with one '
                      'illegible stretch (v03) and single signs open. Per-document C overturned to B; class read in part '
                      '(below the 95% bar) unchanged.'),
                step_result='worked')

    elif name == 'visconti1529':
        relabel('visconti1529', lang='it',
                reviews={'fr3045_f28': ('B', (
                    'Overturns the per-document C, which was given on the "Italian text" section of fr3045_f28_final.md: '
                    'that running text predates the push pass in the same file. With the push-pass readings (l.5 "in fora, '
                    'come batale perduta, ogniuno voleva andare ale stancie"; l.20 "che, obstante ogni mio mal tratamento, '
                    'sarà la fine de la mia"; l.2 "dico che lui proveda a tuto") the letter builds sentence by sentence; '
                    'holes remain in the l.12-15 "Designati ... as[.]sedio" clause and the l.18 place name, besides the code '
                    'groups [42] [rr] [qq] [ep] with no key. The running text should be rewritten with the push-pass readings.'))},
                step=(STEP + 'fr3045_f28_final.md read with its push-pass readings (95.2% measured): the letter builds '
                      'sentences, one clause (l.12-15) and a place name open besides keyless codes. Per-document C (given '
                      'on the pre-push running text) overturned to B. Claim unchanged.'),
                step_result='worked')

    elif name == 'walsingham1581':
        relabel('walsingham1581', lang='en',
                states={'no50I': ('decoded, not read', (
                    'Excerpt only: the full decipherment is Biermann and Lasry\'s (2023), unpublished; Tomokiyo prints only '
                    'the opening clause, "The beirar is domestik servand to the erle of shrevisbvry", and the glyph key '
                    '(cryptiana mary3.htm). Not deciphered here beyond that clause (' + A + '); fix: apply Tomokiyo\'s glyph '
                    'key to f. 138 (DECODE R3839 image P3) through a glyph-to-label concordance, or ask Lasry for the '
                    'plaintext.'))},
                fraction=0.09, fraction_method='estimated',
                fraction_source=('Share of the 562 tokens represented by the ten-word opening published by Tomokiyo, the only '
                                 'plaintext in the repository (approximate). Reading audit, 22 Oct 2026: the document is '
                                 'decoded, not read; the opening is an excerpt.'),
                extra=chain(gaps_add(('no. 50I beyond the published opening', 'not-attempted',
                                      'Tomokiyo\'s glyph key (mary_sp53_11_50b.png) and the f. 138 image (DECODE R3839, '
                                      'reachable with ' + COOKIE + ') are available; build the glyph-to-label concordance '
                                      'and apply the key, or ask Lasry for the Biermann-Lasry plaintext')),
                            note_add('22 Oct 2026, reading audit: only the opening clause is in the repository; decoded, not '
                                     'read (excerpt). Class already solved kept (Biermann and Lasry 2023).')),
                step=(STEP + 'the folder holds the numeric ciphertext and the one-clause opening Tomokiyo published; the full '
                      'plaintext is unpublished. no50I relabelled decoded, not read (excerpt only); class already solved '
                      'kept; fraction_read 0.09 marked estimated; the key application noted as a workable gap.'),
                step_result='partial')

    elif name == 'warsaw':
        relabel('warsaw', lang='it',
                reviews={'R1408': ('B', (
                    'Overturns the per-document C. The word-divided text in plaintext.txt is two long sentences and both '
                    'build and translate: "Mi ricordo che, fra li altri honori che [120] mi fece in Nicolspurg, mi confido '
                    'd\'hauer dato intentione a questa Serenissima [100] [113] de uoler conferire un canonicato d\'Olmiz ad '
                    'uno de li [123] suoi figli; hauendo io {03} saputo in [160] corte che tal uolonta di [120] non e [151] '
                    'stata messa in essecutione ... ho stimato oficio de deuoto seruitore ... di suplicarla ... a uoler far '
                    'effetuare [160] [223] [159], prima {04} si degni darne subito a me benigna risposta". The holes are '
                    'title and function-word codes (no key material) and the object of the request [223] [159]; every '
                    'spelled word reads. The filled-in version is not used.'))},
                step=(STEP + 'plaintext.txt word-divided text read: both sentences build and translate with word codes open '
                      '(no key material). Per-document C overturned to B. Claim unchanged.'),
                step_result='worked')

    elif name == 'windischgraetz1721':
        relabel('windischgraetz1721', lang='de',
                states={'R5029': ('decoded, not read', (
                    'Every letter-spelled passage decrypts, and p2 and p3L build sentences, but p3R, p4L and p4R have open '
                    'code numbers, «?» guesses and elided clear text ("Casse(?) ...", "durchschnid ... «102» ...") in most '
                    'clauses, so about half the sentences do not build (' + A + '); fix: transcribe the clear text of p3R-p5L '
                    'in full from the DECODE images and write a running German text with the open codes marked.'))},
                cls='not read', method='not solved',
                method_basis=('Jakub Mírka\'s reconstructed key (2023), attached to DECODE R5029, was applied unchanged and '
                              'decrypts every letter-spelled passage; with 19 nomenclator codes open and the clear text of the '
                              'later pages only excerpted, about half the sentences do not build, so no reading is claimed '
                              '(reading audit, 22 Oct 2026). The key and the decryption stand.'),
                fraction=0.0,
                fraction_source=('Reading audit, 22 Oct 2026: the one document is decoded, not read, so no tokens are in a '
                                 'document that reads. The earlier 0.856 (measure.py: 155 of 181 groups read as sense) is '
                                 'withdrawn as a reading figure.'),
                extra=chain(gaps_add(('R5029 as a running text (p3R, p4L, p4R, p5L): decoded, not read', 'not-attempted',
                                      'transcribe the clear text around the cipher passages in full from the DECODE images '
                                      '(fetched 5 Oct 2026; reachable with ' + COOKIE + ') and write a running German text '
                                      'with a translation')),
                            note_add('22 Oct 2026, reading audit: decoded, not read; class read in part -> not read, method -> '
                                     'not solved, fraction_read 0.856 -> 0.')),
                step=(STEP + 'dec.txt read: p2 and p3L build, but p3R-p4R have open codes, guesses and elided clear text in most '
                      'clauses. R5029 relabelled decoded, not read; class read in part -> not read; method read with known '
                      'key -> not solved; fraction_read 0.856 -> 0.'),
                step_result='failed')

    elif name == 'wotton1585':
        why = ('Clear English draft with numeric name codes ({}); no transcription is in the repository, only a summary and '
               'the code table (texts/key.md), so no running text can be read here (' + A + '). Checked on the image: the '
               'draft is clear prose. Fix: transcribe it from the DECODE images (local copies in the main checkout '
               'targets/wotton1585/decode/, git-ignored) and mark the code numbers.')
        relabel('wotton1585', lang='en',
                states={'R4841': ('decoded, not read', why.format('f. 167 "To Mr Secretary the 25th August", "Sir, 39. came to '
                                                                  'me yesterday"')),
                        'R4842': ('decoded, not read', why.format('f. 173 "To Mr Secretary the 30th of August 1585", "your H. '
                                                                  'of the 21th came to my handes"')),
                        'R4843': ('decoded, not read', why.format('f. 175 "To Mr Secretary the first of September", "for the '
                                                                  'better effectuating of the overture made by 39"'))},
                cls='not read', method='not solved',
                method_basis=('The three drafts are in clear English with a small numeric name code; the code numbers (19 '
                              'Arran, 39 Master of Gray, 10 King James and others) were identified from the clear text and '
                              'checked against CSP Scotland viii. No draft is transcribed in the repository, so no reading is '
                              'claimed (reading audit, 22 Oct 2026); the code table stands.'),
                fraction=0.0,
                fraction_source=('Reading audit, 22 Oct 2026: none of the three drafts is transcribed in the repository, so '
                                 'no tokens are in a document that reads.'),
                extra=chain(gaps_add(('R4841, R4842, R4843: the drafts, not transcribed', 'not-attempted',
                                      'DECODE images (4 pp. each) are in the main checkout targets/wotton1585/decode/ and '
                                      'reachable with ' + COOKIE + '; transcribe the three drafts with the code numbers '
                                      'marked')),
                            note_add('22 Oct 2026, reading audit: no draft is transcribed here; all three decoded, not read; '
                                     'class read -> not read, method -> not solved. The code identifications stand.')),
                step=(STEP + 'each of R4841-R4843 checked: the repository holds only summaries and texts/key.md; the images '
                      '(main checkout decode/) show clear drafts not transcribed. All three relabelled decoded, not read; '
                      'class read -> not read; method key from adjacent plaintext -> not solved; fraction_read unknown -> 0.'),
                step_result='failed')
    else:
        raise SystemExit('no entry for ' + name)
    print('ok', name)


if __name__ == '__main__':
    for n in sys.argv[1:]:
        run(n)
