"""Re-read brief (REREAD_BRIEF.md), batch b07: lopehurtado1523 (Lope Hurtado de Mendoza, Rome 1523-24, DECODE R9667-R9869).

Targeted profile edits with the splice saver of relabel_r0.py; one save per appended item.

    python research/reading_audit/reread_b07.py
Helpers: b07_crop.py (image crops to the scratchpad), b07_score.py (clean-sentence share of a reading body),
b07_corrections.py (the <doc>_corrections.tsv tables). Log: targets/lopehurtado1523/R9667-R9869_reread_log.md.
"""
import sys
import pathlib

sys.path.insert(0, str(pathlib.Path(__file__).parent))
from relabel_r0 import load, save  # noqa: E402

F = 'lopehurtado1523'
DATE = '2026-10-22'
BY = 'Claude Opus 5.5'
LOG = 'R9667-R9869_reread_log.md'
BASIS = ('the clear text checked on the full-resolution DECODE images and the cipher runs decoded with the merged '
         '1523-24 key (key_merged.tsv, rebuilt from R9846\'s f. 133r clear), every run re-read sign by sign on the '
         'images with the look-alike signs resolved word by word (%s_corrections.tsv: the ß-like a transcribed as '
         'ʇʇ, y ʇʇ = ɣ̶ g, m̶ = f or c, ʒ = p); aligned word by word with the decode, supplied words bracketed. No '
         'contemporary decipherment, clear copy or edition exists. Log: ' + LOG)

READ = {
    'R9866': ('B', 'Clean share 0.667 (b07_score.py, reading body). The French mean to stay this side of the Alps; the '
                   'Emperor must not grant peace or truce while they hold a palm of ground, must drive them out ("si no '
                   'son vencidos, quedan vencedores"), and should have Naples pay the army; Beaurain will report. Holes: '
                   'the codes xer, tas, yab, tol-type groups, R3 "[?] por pocos", R9 opening, R14 middle.'),
    'R9868': ('B', 'Clean share 0.638. The Datary must be rewarded; the archbishop of Capua\'s absence will not help; '
                   'the Pope\'s servants who stayed are very mistrustful; naturalisations for two or three closest to '
                   'the Pope; the protectorship better with Colonna, whom Vespasiano obeys as he did his father Prospero; '
                   'he could complain with cause if forgotten. Holes: zid, ʃug, yic, toc, R14, the last word of R13.'),
    'R9869': ('B', 'Clean share 0.622. The Pope will fulfil the rest of the money offered to Beaurain but pleads need; '
                   'Florence undecided; if the archbishop finds the army ready, the Pope\'s deeds will match what he '
                   'offered when elected; any help with money is good; the clear (f. 444v transcribed in full): Easter '
                   'news of Hungary and the Turk, the Legate at Nuremberg, too few letters from the Emperor. Holes: '
                   'R1 (what Beaurain was sent), R5, parts of R9-R11.'),
}

UNREAD = {
    'R9867': ('clean share 0.389 (wholly cipher): Beaurain leaves the Pope content; the Emperor must not show need of '
              'money; if the French stay in Italy …; Hurtado will do as ordered and asks to be paid what is owed him '
              '"alla"; but about half the sentences break on open codes (rub, ʃug, tol, xer, xal, xir, ʃal, co, ℮, ʃφ). '
              'Blocker: open-codes, no crib'),
    'R9683': ('the clear text reads and the whole-letter share is 0.636, but the cipher passage does not: only "de '
              '[?Theodorico] que sol[o] el …", "el [?duque] esta bienquisto de Su Sd. … para con su [?servicio]" and "para '
              'que la [?cruzada] …" hold. The 1523 hand uses letter signs of the 1522 notation not in the 1524 key, and '
              'there is no 1523 crib. Blocker: open-codes'),
    'R9667': ('the clear text reads (whole-letter share 0.767), but of the six cipher runs only C ("que era del que mas '
              'se [?sospechava]", with CSP 548\'s topic) and pieces of A ("el papa no se declare") and B ("[?franceses] '
              'que [?pensava]") read. The contemporary decipherment CSP Spain ii 548 was made from is not on the DECODE '
              'images. Blockers: open-codes (1523 sign set unkeyed) and needs-physical-access (RAH Salazar A-28)'),
    'R9695': ('not attempted further on 22 Oct 2026 (batch b07): autograph draft with struck cipher lines in the 1523 '
              'sign set, clear transcription incomplete; same blocker as R9683/R9667 (open-codes, no 1523 crib)'),
}

STEPS = [
    {'date': DATE, 'kind': 'access',
     'what': 'Re-read (REREAD_BRIEF, batch b07). Existing text sought: no contemporary decipherment on any DECODE image '
             'of the seven unread letters (CSP Spain ii 548 says R9667 had one, not imaged); CSP calendars only R9667 '
             'and R9846; web search 22 Oct found nothing. The RAH Biblioteca Digital answers only through an Anubis '
             'proof-of-work bot check, not passed, so better images of Salazar A-28/A-30 were not checked.',
     'result': 'failed', 'technique': ['other']},
    {'date': DATE, 'kind': 'transcription',
     'what': 'Every cipher run of R9866, R9867, R9868, R9869, R9683 and R9667 re-read on full-resolution crops of the '
             'DECODE images (b07_crop.py), and the f. 444v clear of R9869 transcribed in full. Look-alikes resolved '
             'word by word (<doc>_corrections.tsv): the ß-like a was transcribed ʇʇ (r) in a dozen words; y ʇʇ is one '
             'sign ɣ̶ (g: coligados, enemigos, colegio, alargar); m̶ is f or c, ʒ is p; xab -> rab, ʒul -> zul, zaf -> '
             'yaf, y m̶ -> ym (fue) in R9869.',
     'result': 'worked', 'technique': ['manual reconstruction']},
    {'date': DATE, 'kind': 'hypothesis',
     'what': 'Code groups from new contexts (probable, key files unchanged): zm = como (R9867 l21, R9866 R14), ʃeg = '
             'tengo (R9866 R14 "como tengo escrito", R9869 R7), zub = alla (1522 value; R9866 R5 "la costa de alla", '
             'R9867 l23), zad probably a look-alike of zed = arçobispo (R9868 R7 after the clear "partida del señor '
             'arçobispo de Capua"). In R9683/R9667 the 1522 sign values & = o, H = e, ɭb = p, ∠ = v give "Theodorico", '
             '"servi[ci]o", "pensava", "declare", "era del que mas se".',
     'result': 'partial', 'technique': ['contextual inference', 'key matching']},
    {'date': DATE, 'kind': 'reading',
     'what': 'Readings built sentence by sentence (<doc>_reading.md, English <doc>_en.md) and aligned word by word with '
             'the decodes (words fixed: R9869 bueno -> [?bueno], R9868 a -> [?a], R9866 como/tiene -> [?…]). Clean '
             'share of the reading bodies (b07_score.py): R9866 0.667, R9868 0.638, R9869 0.622 (read, grade B); R9867 '
             '0.389 (decoded, not read); R9683 0.636 and R9667 0.767 on the whole letter but kept decoded, not read '
             'because their cipher passages do not build sentences; R9695 not attempted further. English for R9846 '
             '(read since the audit) written: R9846_en.md.',
     'result': 'partial', 'technique': ['manual reconstruction', 'contextual inference', 'language-model scoring']},
]


def main():
    p = load(F)
    o = p['outcome']
    for t in o['texts']:
        d = t['doc']
        if d in READ:
            g, note = READ[d]
            t['state'] = 'read'
            t.pop('note', None)
            t['reading'] = '%s_reading.md' % d
            t['translation'] = '%s_en.md' % d
            t['language'] = 'es'
            t['reading_review'] = {'grade': g, 'by': BY, 'date': DATE, 'note': note + ' Rests on ' + (BASIS % d) + '.'}
        elif d in UNREAD:
            if d != 'R9695':
                t['reading'] = '%s_reading.md' % d
                t['translation'] = '%s_en.md' % d
            t['note'] = ('Re-read 22 Oct 2026 (batch b07; %s): ' % ((d + '_reading.md, ' + d + '_en.md, ' + LOG)
                                                                    if d != 'R9695' else LOG)) + UNREAD[d] + '.'
        elif d == 'R9846':
            t['translation'] = 'R9846_en.md'
    o['method'] = 'key recovered based on adjacent plaintext'
    o['method_basis'] = ('The key rebuilt from R9846\'s contemporary clear on f. 133r (key recovered based on adjacent '
                         'plaintext) reads three of the 1524 letters (R9866, R9868, R9869) after a sign-by-sign re-read '
                         'on the images; R9846 ff. 130r-v reads from that clear itself; R9667, R9683, R9695 (1523 sign '
                         'set) and R9867 stay decoded, not read.')
    o['parts'] = [
        {'label': 'R9866, R9868, R9869 (1524, clear with cipher runs)', 'records': 'DECODE R9866, R9868, R9869',
         'method': 'key recovered based on adjacent plaintext', 'extent': 'partial',
         'basis': 'the 1524 key rebuilt from the R9846 f. 133r alignment, the runs re-read on the DECODE images with '
                  'the look-alike signs resolved word by word (22 Oct 2026, batch b07); readings with scattered holes '
                  '(open codes), clean share 0.62-0.67'},
        o['parts'][0],
        {'label': 'R9667, R9683, R9695, R9867 (decoded, not read)', 'records': 'DECODE R9667, R9683, R9695, R9867',
         'method': 'not solved', 'extent': 'none',
         'basis': 'R9867 (wholly cipher) breaks on about fifteen open codes; the three 1523 letters use letter signs '
                  'of the 1522 notation not in the 1524 key and have no crib, and R9667\'s contemporary decipherment '
                  '(CSP Spain ii 548) is not imaged. Their clear text reads.'},
    ]
    o['notes'] = ('Two letters already abstracted by Bergenroth (CSP Spain ii 548, 617). Key rebuilt from R9846\'s bound '
                  'clear; on 22 Oct 2026 three 1524 letters (R9866, R9868, R9869) read with it after a sign-by-sign '
                  're-read on the images; R9867 and the three 1523 letters stay decoded, not read (open codes, 1523 '
                  'sign set unkeyed, R9667\'s decipherment not imaged).')
    o['fraction_read'] = 0.66
    o['fraction_read_method'] = 'estimated'
    o['fraction_read_source'] = (
        '22 Oct 2026, re-read batch b07: cipher tokens of the documents that read / all, counted by decode_merged.py '
        'over the transcriptions (R9667 152, R9683 91, R9695 249, R9846 764, R9866 624, R9867 467, R9868 353, R9869 '
        '339 = 3,039) plus R9846\'s untranscribed ff. 131-132 (124, from the notes\' count of 888): read R9846 ff. '
        '130r-v 764 + R9866 624 + R9868 353 + R9869 339 = 2,080 / 3,163 = 0.66 (estimated: R9846\'s untranscribed '
        'share and the 1523 counts come from different transcriptions). Before: 0.23 (reading audit, R9846 only).')
    save(F, p)
    gap_drop = {'R9683 (June 1523), decoded, not read', 'R9866 (28 Feb 1524), decoded, not read',
                'R9868 (20 Mar 1524), decoded, not read', 'R9869 (28 Mar 1524), decoded, not read'}
    p = load(F)
    p['outcome']['gaps'] = [g for g in p['outcome']['gaps']
                            if not g['item'].startswith('About 30 code groups')]
    save(F, p)
    new_gaps = [
        {'item': 'About 20 code groups (rub, ʃug, zid, tol, tid, zib, xer, xir, xal, ʃal, yab, tas, toc, yic, co ...) '
                 'across the 1524 letters', 'blocker': 'open-codes',
         'detail': 'no crib; they leave the holes in R9866/R9868/R9869 and most of R9867 unread (22 Oct 2026, b07)'},
        {'item': 'R9867 (4 Jan 1524, wholly cipher), decoded, not read (clean share 0.389)', 'blocker': 'open-codes',
         'detail': 'about half its sentences hold; the rest break on the open codes above'},
        {'item': 'R9683, R9667, R9695 (1523), cipher passages decoded, not read', 'blocker': 'open-codes',
         'detail': 'the 1523 hand uses letter signs of the 1522 notation not in the 1524 key; no 1523 crib; R9695 not '
                   'attempted further; R9667\'s contemporary decipherment (CSP 548) not imaged (RAH Salazar A-28; the '
                   'RAH digital library is behind a bot check)'},
    ]
    for g in new_gaps:
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
