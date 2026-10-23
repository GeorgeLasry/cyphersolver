"""Re-read brief (REREAD_BRIEF.md), batch b15: transylvania1645 (R4936, R4937, R4942) and revol1593 (f88, f146v, f157v).

Targeted profile edits with the splice saver of relabel_r0.py; one save per change.

    python research/reading_audit/reread_b15.py <target> <step>
Helpers: b15_align.py (reading vs figures, letter by letter), b15_body.py (join a line-by-line reading, hole count per
sentence), b15_score.py (_check_reading.py with the committed and a period Hungarian word list).
"""
import sys
import pathlib

sys.path.insert(0, str(pathlib.Path(__file__).parent))
from relabel_r0 import load, save  # noqa: E402

REV = dict(by='Claude Opus 5.5', date='2026-10-23')


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


def set_note(t, doc, note, fields=None):
    p = load(t)
    e = [x for x in p['outcome']['texts'] if x.get('doc') == doc][0]
    e['note'] = note
    if fields: e.update(fields)
    save(t, p); print('note', t, doc)


def add_step(t, step):
    p = load(t)
    p['solution'].append(step)
    save(t, p); print('step', t)


CHK = ("docs/_check_reading.py cannot score this Hungarian: its 'hu' word list (modern Gutenberg) gives genuine printed "
       "1645 letters from Szilagyi's Linz edition 0.07 and 0.0, and this reading {chk}; holes counted by the same rule "
       "on the bracketed words (b15_body.py) give {own}.")

TR_NOTE = {
    'R4936': "Read 23 Oct 2026 (b15) from our re-transcription of both pages (R4936-transcription-b15.txt, 215 label changes in "
             "R4936_corrections.tsv: the hand's g/q, c/e, i/n, a/v and minim counts) with the family key unchanged; aligned letter "
             "by letter (R4936_align.tsv): 1,932 reading letters, 1,794 on the figure's own value, 130 on the other member of a "
             "look-alike pair, 6 on another figure inside [?words], 2 supplied. Numbered instructions to Ferenc Bethlen at Warsaw "
             "(1645): persuading the King and the Respublica, 3,000 musketeers and 1,000 dragoons, money at Danzig, Bregy and "
             "Croissy. " + CHK.format(chk='0.03', own='0.94 (32 of 34 sentences)') +
             " Open: five [?words] and two [...] runs.",
    'R4937': "Read 23 Oct 2026 (b15) from a full transcription of the one page (R4937-transcription.txt, 34 lines; the old extract had "
             "25 and solver output only) with the family key unchanged; aligned (R4937_align.tsv): 847 letters, 839 on the "
             "figure's own value, 3 class-resolved, 4 inside [?words], 1 supplied. On the Emperor's diploma and the Evangelicals, "
             "keeping out of the King's war with the Turk, hiring 4,000 foot or 2,000 armed men. " +
             CHK.format(chk='0.05', own='0.90 (18 of 20 sentences)') + " Open: the run after 'megsegni' (l. 3) and the end of l. 13.",
    'R4942': "Read 23 Oct 2026 (b15): every cipher passage transcribed (R4942-transcription.txt: the 7-line block at the head of p. 2 "
             "and two words lower down), decoded with the family key and aligned (R4942_align.tsv: 249 letters, 236 on their own "
             "value); the DECODE record's image 3 is a clear slip with the same words, signed 'Sigis Rakoczi' and noted by Bethlen "
             "(R4942_slip.txt), so the reading also rests on a contemporary clear text. " +
             CHK.format(chk='0.0', own='1.00 (4 of 4 sentences)') + " Open: [?teliessegel] (one figure).",
}

TR_STEPS = [
    {'date': '2026-10-23', 'kind': 'access', 'what': "Re-read (REREAD_BRIEF, b15): the DECODE records R4936, R4937, R4942 have no document attachments (Documents 0); all their images (2, 1, 4) opened at full resolution from the main checkout. R4942's image 3 is a clear slip carrying the text of the p. 2 cipher block (signed 'Sigis Rakoczi', annotated 'Bethlen F.'), not used before. R4936 has a later pencil gloss under its first cipher line only.", 'result': 'worked'},
    {'date': '2026-10-23', 'kind': 'access', 'what': "Print searched for the letters: Lukinich, Keresdi baro Bethlen Ferencz (Szazadok 1908, second instalment) describes the 1645 and 1646-47 Warsaw missions and cites the originals 'partly in cipher' in the Keresd archive, no decipherment; Szilagyi, A linzi beke okirattara (1885) and Erdely es az eszakkeleti haboru I (MEK) grepped: no edition of R4936/R4937/R4942.", 'result': 'failed'},
    {'date': '2026-10-23', 'kind': 'transcription', 'what': "R4936 re-transcribed line by line from 2.4-3x crops of both pages (R4936-transcription-b15.txt); 215 label changes against the provisional transcription (R4936_corrections.tsv), mostly g/q, c/e, i/n and dropped or doubled minims. R4937 transcribed in full (34 lines, 869 letters) and R4942's cipher in full (252 letters); one R4942 label corrected (R4942_corrections.tsv).", 'result': 'worked'},
    {'date': '2026-10-23', 'kind': 'reading', 'technique': ['key matching', 'contextual inference'], 'what': "The family's reciprocal letter key (shared-key-hypothesis.json) applied unchanged to all three letters; R4937 and R4942 read at sight. R4936 read sentence by sentence with the look-alike pairs of the hand resolved by sense; R4937's hand confuses cipher l and r twice (hamis, ha szinte). Readings aligned letter by letter with the figures (b15_align.py): R4936 1,794 + 130 class-resolved of 1,932; R4937 839 + 3 of 847; R4942 236 + 6 of 249.", 'result': 'worked'},
    {'date': '2026-10-23', 'kind': 'reading', 'technique': ['language-model scoring'], 'what': "docs/_check_reading.py gives 0.03, 0.05 and 0.0 on the reading bodies, but also 0.07 and 0.0 on genuine printed Hungarian letters of 1645 (Szilagyi 1885): its modern 'hu' word list does not know 17th-c. spelling; with a period list from the 1640s prints added the controls reach 0.53-0.60 and the readings 0.05-0.25 (the cipher spelling: oe, cz, unaccented, run-on). Explicit holes only (b17_score.py HOLES=1): R4936 0.94 (32/34), R4937 0.90 (18/20), R4942 1.00 (4/4). All three set read, grade B, with that caveat.", 'result': 'partial'},
]


def tr(step):
    t = 'transylvania1645'
    if step == 'texts':
        f = {
            'R4936': {'transcription': ['R4936-transcription-b15.txt', 'R4936-transcription.txt'], 'decryption': ['R4936_reading_lines.txt', 'R4936_align.tsv', 'R4936-mechanical.txt'],
                      'reading': 'R4936_reading.md', 'translation': 'R4936_en.md', 'language': 'hu',
                      'summary': "Numbered instructions in the prince's 'we' to Ferenc Bethlen at Warsaw, 1645, with clear Hungarian links: the King must be persuaded and the Respublica should not disgrace itself or bow to the Turk; the King is asked to hire 3,000 musketeers and 1,000 dragoons (at least 2,000 and 1,000) for Transylvania; money at Danzig; recruits to Munkacs and Makovica; news of Bregy and Croissy."},
            'R4937': {'transcription': 'R4937-transcription.txt', 'decryption': ['R4937_reading_lines.txt', 'R4937_align.tsv'],
                      'reading': 'R4937_reading.md', 'translation': 'R4937_en.md', 'language': 'hu',
                      'summary': "1646, to 'edes Hokmester' (Bethlen): the Emperor will effect nothing of the diploma for the Evangelicals; the clergy rules him; keep secret from the King why Transylvania would not join a war on the Turk; hire 4,000 foot with officers, or 2,000 armed men, or at least 1,000 foot and 500 dragoons."},
            'R4942': {'transcription': ['R4942-transcription.txt', 'R4942_slip.txt'], 'decryption': ['R4942_reading_lines.txt', 'R4942_align.tsv'],
                      'reading': 'R4942_reading.md', 'translation': 'R4942_en.md', 'language': 'hu',
                      'label': 'R4942, Zsigmond Rakoczi to Ferenc Bethlen, 1648 (cipher block of p. 2 and two words)',
                      'summary': "Zsigmond Rakoczi, 1648: Bethlen's goodwill has reassured him though there is almost no hope for the present affair; the intermediaries must be used; his brother is so disposed with the plenipotentiary power that he can promise more. The p. 3 slip gives the same text in clear."},
        }
        for d in ('R4936', 'R4937', 'R4942'):
            mark_read(t, d, f[d], 'B', TR_NOTE[d])
    elif step == 'steps':
        for s in TR_STEPS: add_step(t, s)
    elif step == 'outcome':
        p = load(t); o = p['outcome']
        o['notes'] = o['notes'] + (" 23 Oct 2026, re-read (b15): R4936, R4937 and R4942 transcribed in full from the images and read with the family "
                                   "key unchanged (readings, English and letter alignments in the folder); R4942's image 3 is a clear slip of the same "
                                   "text. R4938 (clear with short cipher insertions) and R4939 (two pages of cipher in a different-looking script) "
                                   "still not transcribed.")
        o['method_basis'] = o['method_basis'].replace("R4937 and R4942 give fragments; R4938 and R4939 not yet inspected.",
                                                      "R4936, R4937 and R4942 transcribed in full and read with the same key on 23 Oct 2026 (R4942 also has a clear slip of its cipher block); R4938 and R4939 not yet transcribed.")
        o['gaps'] = [
            {'item': 'R4938 (1647), short cipher insertions in a clear letter', 'blocker': 'not-attempted', 'detail': 'images in hand (4); not transcribed'},
            {'item': 'R4939 (1648), two pages of cipher in a script unlike the family hand', 'blocker': 'not-attempted', 'detail': 'images in hand (3); not transcribed; may be a different cipher'},
            {'item': "R4936: five [?words] and two [...] runs (l. 9 'ngayioqfyi', l. 16 'vngqxvuv')", 'blocker': 'illegible', 'detail': 'figures checked at 3x; the letter shapes do not settle a word'},
            {'item': "R4937: the run after 'megsegni' (l. 3) and the end of l. 13", 'blocker': 'illegible', 'detail': 'figures decode to letter strings that are not words; checked at 2.2x'},
        ]
        o['class'] = 'read in part'
        save(t, p); print('outcome', t)


REV_STEPS = []




REVOL_STEPS = [
    {'date': '2026-10-23', 'kind': 'literature search', 'what': "Re-read (REREAD_BRIEF, b15): is there a text of ff. 88, 146v, 157v? Not DECODE records (BnF fr. 3985/3986 microfilm on Gallica); no interlinear decipherment on the three pages (canvas 287 re-checked at full resolution). Memoires de Nevers part 2 (bpt6k64451005): the four pages where Gallica's search had found 'Reuol' (pp. 324, 425, 453, 513) fetched through openapi IIIF and read: none prints a Nevers-Revol letter of 1593. Gallica ContentSearch now returns a Cloudflare block; archive.org has no copy.", 'result': 'failed'},
    {'date': '2026-10-23', 'kind': 'transcription', 'what': "f. 146v: canvas 287 fetched at full resolution (4949 x 6957, openapi IIIF v3) and the three full cipher lines re-read in native-resolution strips. The anchors hold ('nostre ... de l'absolution et que ... Je', 'nous [?au]rions et a la verite', 'Mr de Mercure'), but each of the copyist's forms still maps to two or three table entries and no clause between the anchors reads. ff. 88 and 157v not re-transcribed. All three kept decoded, not read; the next step is the glyph atlas from the interlined Instruction (fr. 3985 c. 264-268).", 'result': 'failed'},
]


def revol(step):
    t = 'revol1593'
    if step == 'steps':
        for s in REVOL_STEPS: add_step(t, s)
    elif step == 'gaps':
        p = load(t); o = p['outcome']
        for g in o['gaps']:
            if g['item'].startswith('fr. 3986 f. 146v'):
                g['blocker'] = 'not-attempted'
                g['detail'] = ("re-read on the full-resolution canvas 287 on 23 Oct 2026 (b15): signs legible, anchors hold, but the copyist's forms map to "
                               "two or three table entries; finish the glyph atlas from the interlined Instruction (fr. 3985 c. 264-268) and re-transcribe")
            elif g['item'].startswith('fr. 3985 f. 88r'):
                g['blocker'] = 'not-attempted'
                g['detail'] = ("bitonal microfilm canvases 176-177 and the contributor's transcription (variants at one sign in six); no text in print "
                               "(Memoires de Nevers ii checked 23 Oct 2026); re-transcribe against the finished glyph atlas")
        o['notes'] = o['notes'] + " 23 Oct 2026, re-read (b15): no contemporary or printed text of ff. 88, 146v, 157v; f. 146v re-read at full resolution without a reading; all three stay decoded, not read (texts/f88-f146v-f157v_reread_log.md)."
        save(t, p); print('gaps', t)


if __name__ == '__main__':
    {'transylvania1645': tr, 'revol1593': revol}[sys.argv[1]](sys.argv[2])
