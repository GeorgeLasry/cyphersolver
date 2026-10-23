"""Re-read brief (REREAD_BRIEF.md), batch b14: hm1645 (R785, R790, R923) and bonzagni1512 (R1123, R1124, R1125).

Targeted profile edits with the splice saver of relabel_r0.py; one save per change.

    python research/reading_audit/reread_b14.py <target> <step>
Helpers: b14_fetch.py (DECODE record files to the scratchpad), b14_hm.py (hm1645 key decode beside Lasry's plaintext),
b14_align.py (reading vs decode, letter by letter), b14_score.py (clean-sentence share of a reading body).
"""
import sys
import pathlib

sys.path.insert(0, str(pathlib.Path(__file__).parent))
from relabel_r0 import load, save  # noqa: E402

REV = dict(by='Claude Opus 5.5', date='2026-10-22')


def mark_read(t, doc, fields, grade, note):
    p = load(t)
    e = [x for x in p['outcome']['texts'] if x.get('doc') == doc]
    assert len(e) == 1, doc
    e = e[0]
    e.pop('note', None)
    e['state'] = 'read'
    e.update(fields)
    e['reading_review'] = dict(grade=grade, **REV, note=note)
    save(t, p); print('read', t, doc)


def add_step(t, step):
    p = load(t)
    p['solution'].append(step)
    save(t, p); print('step', t)


HM_NOTE = {
    'R785': "Read 22 Oct 2026 (b14) from the key decode of the DECODE transcription with Lasry's TNA SP 106 key (his plaintext D3061 compared line by line), two key corrections (292 = by, 435 = next) and nomenclator values proposed from the codebook's alphabetical bands (texts/hm1645_codes.tsv); aligned letter by letter with the decode (0.978 carried, b14_align.py); _check_reading.py on the body 0.841 (53/63). Signed A. Cowley; image 3 (f. 215) is a second letter in the same key. Open: 15 code groups (22 tokens), mostly names.",
    'R790': "Read 22 Oct 2026 (b14) as for R785 (Lasry's plaintext D3066 compared); aligned 0.980; _check_reading.py on the body 0.792 (19/24). Open: 469, 353, 525, 350, 545, 541, 486, 234; [?Pope] (221) and [?Ireland] (164) from context.",
    'R923': "Read 22 Oct 2026 (b14) as for R785 (Lasry's plaintext D3070 compared); 126 corrected to 127 (the Queen) and 'forrain [?succour]' (not Lasry's 'Lorrain support') checked on the image; aligned 0.959; _check_reading.py on the body 0.84 (21/25). Open: 529, 120, 424, 257, 300, 148, 489, the place 85 and 60; the postscript breaks off.",
}

HM_STEPS = [
    {'date': '2026-10-22', 'kind': 'access', 'what': "Re-read (REREAD_BRIEF, b14): every file on R785, R790, R923 fetched with the shared DECODE cookie into the session scratchpad (b14_fetch.py): Pettersson's transcriptions, Lasry's key, interlinear and plaintext files, 7 page images. No contemporary decipherment, gloss or clear copy on the records.", 'result': 'worked'},
    {'date': '2026-10-22', 'kind': 'verification', 'technique': ['key matching', 'contextual inference'], 'what': "Key decode of every cipher line (b14_hm.py) beside Lasry's plaintext, including the 17 lines apply_key.py skipped. Two key values corrected because every occurrence needs it: 292 = by (Lasry: because, 12 occurrences) and 435 = next (Lasry: of, 2).", 'result': 'worked'},
    {'date': '2026-10-22', 'kind': 'hypothesis', 'technique': ['key-structure hypothesis', 'contextual inference'], 'what': "The groups from 279 up form an alphabetical codebook (279 and ... 555 you); band plus contexts in the six letters of the key (including Lasry's French sections) fix 31 open groups: 295 business, 330 dispatch, 340 foot, 405 master, 446 particular, 502 she, 518 those, 548 who, 392+498 lord+ship, 475 religion, 476 rebel ... (texts/hm1645_codes.tsv); single-context values marked [?]. 541 (four contexts) does not resolve to one word.", 'result': 'partial'},
    {'date': '2026-10-22', 'kind': 'transcription', 'what': "Figures checked on the images where decode and sense disagreed: R785 'pertectly' is the writer's 10; R923 126 is 127 (7 over 6: the Queen); R923 554 your (4 over 5); R923 341 r a 382 497 = 'forrain [succour]', not Lasry's 'Lorrain support'. Other one-figure slips listed, not checked (texts/hm1645_corrections.tsv).", 'result': 'worked'},
    {'date': '2026-10-22', 'kind': 'reading', 'technique': ['language-model scoring'], 'what': "Readings written (texts/R785/R790/R923_reading.md, _en.md), aligned letter by letter with the decode (0.978, 0.980, 0.959 carried; b14_align.py); clean-sentence share on the bodies 0.841, 0.792, 0.84 (0.73, 0.54, 0.56 with the figures' own spellings, which the lexicon does not know). All three set read.", 'result': 'worked'},
]


def hm(step):
    t = 'hm1645'
    if step == 'texts':
        for d in ('R785', 'R790', 'R923'):
            mark_read(t, d, {'reading': f'texts/{d}_reading.md', 'translation': f'texts/{d}_en.md', 'language': 'en'}, 'B', HM_NOTE[d])
    elif step == 'outcome':
        p = load(t); o = p['outcome']
        o['contribution'] = ['catalogue correction', 'key extended or corrected']
        o['codes_open'] = {'open': 30, 'tokens_open': 40}
        o['gaps'] = [
            {'item': "three-figure nomenclator groups still open after the 22 Oct 2026 re-read (28: 120, 148, 208, 212, 228, 234, 237, 257, 300, 334, 344, 348, 350, 353, 424, 469, 486, 488, 489, 500, 507, 522, 525, 529, 535, 541, 543, 545) and the two-figure 85 (a place, R923) and 60",
             'blocker': 'no-key-material',
             'detail': "Names or words seen once or twice in the six letters of the key, with no context that fixes them (541's four contexts need different words). 31 others were fixed from the codebook's alphabetical bands and context (texts/hm1645_codes.tsv)."},
            {'item': 'one- and two-digit figures with no value in the key (78, 77, 16, 49, 59, 39, 30, 79 and three rarer ones: 11 distinct, 205 tokens)',
             'blocker': 'no-key-material',
             'detail': "They fall between words throughout and are read as separators; whether the writer meant them as nulls (Lasry's key file says there are none) is not settled by anything on the records."},
        ]
        o['notes'] = o['notes'] + " 22 Oct 2026, re-read (b14): the three letters read from the key decode with Lasry's key, two key corrections (292 = by, 435 = next) and 31 nomenclator values proposed from the codebook's alphabetical bands (texts/hm1645_codes.tsv); R785 is signed A. Cowley; R923's 'Lorrain support' is 'forrain [succour]'."
        save(t, p); print('outcome', t)
    elif step == 'steps':
        for s in HM_STEPS:
            add_step(t, s)


BZ_NOTE = {
    'R1124': "Read 22 Oct 2026 (b14): the eight cipher lines from the contemporary interlinear decipherment, transcribed from the DECODE image and aligned group by group with the cipher (texts/R1124_align.tsv), with the clear text of pp. 1-2 transcribed around them; _check_reading.py on the body 0.625 (20/32; misses mostly inventory words the Italian lexicon lacks: coppa, tazette, anelle, coramo). Holes: the torn right edge of p. 1 (ll. 12-19) and the end of cipher l. 5.",
    'R1125': "Read 22 Oct 2026 (b14): the 12-line cipher block of p. 3 from the decipherment slip filed with the letter (image 5), transcribed and aligned group by group with the cipher (texts/R1125_align.tsv); _check_reading.py on the body 0.857 (6/7). Open: the code word 'parte' (left blank by the slip) and the number .31.; the clear pp. 1-4 not transcribed here.",
}

BZ_STEPS = [
    {'date': '2026-10-22', 'kind': 'access', 'what': "Re-read (REREAD_BRIEF, b14): R1123-R1125 re-fetched from DECODE with the shared cookie (b14_fetch.py): page images only, no attachments or transcriptions; the Vestigia photographs (main checkout img/v/) are the same resolution.", 'result': 'worked'},
    {'date': '2026-10-22', 'kind': 'transcription', 'what': "R1125: the decipherment slip (image 5) transcribed and aligned group by group with the 12-line cipher block of p. 3: one slip word per group, letters repeating consistently; Latin-looking code words in the cipher found ('valent' = denaro, 'indigeo', 'parte' left blank by the slip) and a number .31. the slip omits.", 'result': 'worked'},
    {'date': '2026-10-22', 'kind': 'transcription', 'what': "R1124: the interlinear decipherment over the eight cipher lines transcribed and aligned with the cipher groups (texts/R1124_align.tsv); two more glossed cipher words in the clear text (tazze grande); the clear text of pp. 1-2 transcribed, with holes at the torn right edge.", 'result': 'worked'},
    {'date': '2026-10-22', 'kind': 'transcription', 'what': "R1123: the clear opening of p. 1, the first cipher block (ll. 5-9) and the start of the lower block transcribed from the glosses (texts/R1123_reading.md, partial); the gloss words checked against sign values from R1124/R1125 where legible (ducati, dona, del, fiorini, trecento, che). The rest of the lower block (an inventory of silver and sums, about eleven lines) and the cipher of p. 2 not finished: the brown gloss ink is faint at the scan's resolution, and the key was not rebuilt to decode the signs.", 'result': 'partial'},
    {'date': '2026-10-22', 'kind': 'reading', 'technique': ['language-model scoring'], 'what': "Clean-sentence share on the reading bodies: R1125 0.857, R1124 0.625 (inventory words outside the Italian lexicon), R1123 partial 0.632 on the part read. R1124 and R1125 set read; R1123 kept decoded, not read (most of its cipher unread).", 'result': 'partial'},
]


def bz(step):
    t = 'bonzagni1512'
    if step == 'texts':
        for d in ('R1124', 'R1125'):
            mark_read(t, d, {'reading': f'texts/{d}_reading.md', 'translation': f'texts/{d}_en.md'}, 'B', BZ_NOTE[d])
    elif step == 'r1123':
        p = load(t)
        e = [x for x in p['outcome']['texts'] if x.get('doc') == 'R1123'][0]
        e['note'] = ("Re-read 22 Oct 2026 (b14), partial: texts/R1123_reading.md and _en.md hold the clear opening of p. 1, the first cipher block (ll. 5-9, from the gloss: a thousand gold ducats gathered, the King of Hungary's order that the troops ride out by the August feast of Our Lady, 300 florins through Alberto Pratonerio's father) and the start of the lower block (madonna Beatrice's estate, sums in florins). "
                     "Not read: the rest of the lower block of p. 1 (about eleven glossed lines, an inventory of silver and sums) and the glossed cipher of p. 2 (ll. 2-4, 7). Blockers: illegible (the brown gloss ink is faint at the resolution of the DECODE and Vestigia photographs) and not-attempted (a key rebuilt from the R1124/R1125 alignments would decode the signs and settle the faint glosses).")
        e['reading'] = 'texts/R1123_reading.md'
        e['translation'] = 'texts/R1123_en.md'
        save(t, p); print('r1123 note')
    elif step == 'outcome':
        p = load(t); o = p['outcome']
        o['method'] = 'read from existing decipherment'
        o['method_basis'] = "R1124 and R1125 read from the contemporary decipherments (the interlinear glosses of R1124, the decipherment slip of R1125), transcribed and aligned with the cipher groups on 22 Oct 2026; R1123's glosses only partly transcribed."
        o['contribution'] = ['transcription']
        o['class'] = 'read in part'
        o['fraction_read'] = 0.46
        o['fraction_read_method'] = 'estimated'
        o['fraction_read_source'] = ("22 Oct 2026, re-read (b14): cipher word groups counted on the images (no sign transcription exists): R1124 about 71 (block 69 + 2 in the clear), R1125 about 98, R1123 about 200 (p. 1 upper block c. 43, lower block c. 135, p. 2 c. 20). Read: R1124 + R1125 = c. 169 of c. 369 = 0.46.")
        o['notes'] = o['notes'] + " 22 Oct 2026, re-read (b14): R1125's slip and R1124's glosses transcribed and aligned with the cipher; both read (texts/). R1123 read in part (p. 1 upper block); its lower block and p. 2 stay open. The cipher carries Latin-looking code words (potest = Re d'Ungaria, valent = denaro/argenti, indigeo, parte)."
        o['gaps'] = [
            {'item': 'R1123: the lower cipher block of p. 1 (about eleven glossed lines, an inventory of silver and sums) and the glossed cipher of p. 2 (ll. 2-4, 7)',
             'blocker': 'illegible',
             'detail': "the brown gloss ink is faint at the resolution of the DECODE and Vestigia photographs (both c. 3000 px for the whole sheet); partly legible words: coppe, dorate, tondi dodici, pesano, marche, oncie cinque, pesetti due"},
            {'item': 'R1123: key rebuild to decode the signs under the faint glosses',
             'blocker': 'not-attempted',
             'detail': "a substitution of invented signs with homophones for vowels and a few Latin-looking code words; R1124 and R1125 (texts/*_align.tsv) give about 170 aligned words to rebuild it from; then decode R1123's lower block and p. 2 and check the glosses"},
            {'item': "R1125: the code word 'parte' (cipher l. 7) and the number .31. (l. 10)",
             'blocker': 'no-key-material',
             'detail': 'the slip leaves the first blank and omits the second; seen once'},
            {'item': 'R1124: the torn right edge of p. 1 (ll. 12-19 of the clear text) and the end of cipher l. 5',
             'blocker': 'illegible',
             'detail': 'paper lost at the edge'},
        ]
        gaps = o['gaps']; o['gaps'] = gaps[:1]
        save(t, p); print('outcome', t)
        for g in gaps[1:]:            # one appended item per save: the splice saver reverses several inserts at one place
            p = load(t); p['outcome']['gaps'].append(g); save(t, p)
    elif step == 'steps':
        for s in BZ_STEPS:
            add_step(t, s)


if __name__ == '__main__':
    t, step = sys.argv[1], sys.argv[2]
    {'hm1645': hm, 'bonzagni1512': lambda s: bz(s)}[t](step)
