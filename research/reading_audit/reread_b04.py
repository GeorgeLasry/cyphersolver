"""Re-read brief (REREAD_BRIEF.md), batch b04: nunzio1736 (ASV Segr. Stato Spagna 423, DECODE R26, R179-R188).

Targeted profile edits with the splice saver of relabel_r0.py (only changed spans are rewritten); one save per
appended solution step (the saver misorders several appends to one list in a single save).

    python research/reading_audit/reread_b04.py
Helpers: b04_fetch.py (DECODE images to the scratchpad), b04_seg.py (re-segmentation and decode, --write),
b04_align.py (word-by-word alignment of each reading with its decode), b04_render.py (Lasry's segmented file).
"""
import sys
import pathlib

sys.path.insert(0, str(pathlib.Path(__file__).parent))
from relabel_r0 import load, save  # noqa: E402
import b04_seg  # noqa: E402

F = 'nunzio1736'
DATE = '2026-10-22'
BY = 'Claude Opus 5.5'
BASIS = ('the DECODE transcription re-segmented (research/reading_audit/b04_seg.py) and decoded with Lasry\'s key as '
         'corrected 22 Oct 2026 (25 = che, 30 = ta, 69 = z, 93 = nel) and the nomenclator of key_extra.txt with '
         'texts/b04_key_additions.txt; aligned word by word with the decode (b04_align.py), supplied words bracketed. '
         'No contemporary decipherment, clear copy or edition exists')

READ = {
    '423/2': ('B', 'Rome, 21 July 1736. Molina\'s part in the deception of the King and Queen; the Pope will not use '
                   'Molina, a serving minister of Madrid, to treat the Holy See\'s interests; Guiccioli to try every '
                   'road to enlighten the Court. Holes: 4 unvalued groups (dates, 1200, 1335, 1695), several probable '
                   'values in [?]; ends mid-sentence.'),
    '423/4': ('B', 'Rome, 4 August 1736. No good to be hoped while ministers like Mons. [1513] (Molina) have influence '
                   'and the papal ministers are absent; only God can enlighten the Pope and move the princes. Holes: '
                   '1668, 1513, 1695, 1405, a date group, two unread figures.'),
    '423/5': ('B', 'Rome, September 1736. If Madrid expels the nuncio, Guiccioli is to ask for time to inform the Pope '
                   'and, refused after a second request, to leave. Lasry\'s segmented file lacked 40 of the 177 tokens '
                   'of this page; all now read; holes are probable values only.'),
    '423/6': ('B', 'Rome, 29 September 1736. Whether Madrid will send an envoy to Portugal; the new regulation dividing '
                   'Don Diego de Mendoza\'s offices among three secretaries, and the old claim that the nuncio visit him '
                   'first. Holes: 1555, 1582, 1204; "[?stra]nieri" against the figures.'),
    '423/7': ('B', 'Rome, 29 September 1736. The junta on the patronage and the new junta against the Dataria; the Pope '
                   'writes a Brief to Philip V (sent through his confessor), to all the bishops, to the Queen and '
                   'another. Six figures corrected on the images. Holes: 1449, 1942, 1698, 1232, 1469; ends at the foot '
                   'of f. 388v.'),
    '423/8': ('B', 'Rome, autumn 1736 (cipher page undated). Guiccioli to keep the Briefs quiet, pass copies to [1601] '
                   'of Avila and report their effect on the bishops, the Court and the people. Holes: 1636, 1845, 1601; '
                   'begins mid-sentence.'),
    '423/9': ('B', 'Rome, 6 October 1736. Three more Briefs: a rebuke to the Patriarch of the Indies over the royal '
                   'cedula on canonries, an exhortation to Mons. [1544] against regalist doctrines, an admonition to '
                   'Mons. [1513] (Molina) as head of the junta. Holes: 1544, 1499, 1449, 1845, 1601, 27 28 42 and the '
                   'end of one verb.'),
    '423/10': ('B', 'Rome, 15 December 1736. The Dataria decree issued on false reports (the riots, the Ostia affair, '
                    'pensions through figureheads); the Pope keeps his liberty to grant graces; Molina is not earning '
                    'the hat. Six unclear figures resolved (three seen blotted on the images). Holes: 1957, 1844, 58, '
                    '1235, 1843, 1864, two unread figures.'),
    '423/11': ('B', 'Rome, 22 December 1736. Briefs on the patronage; Molina\'s conduct; no Spanish cardinal while the '
                    'rupture lasts; the Secretary of the royal patronage and the abbeys; what would follow if the '
                    'Cruzada, millones and excusado were suspended. Two figures corrected on the image. Holes: 1664, '
                    '1964, 1204, 1544, 1248, 1206, 1864, 1862, 1502, 1449, 1808, 1840, 1535, 1696, 1844 and one '
                    'unread phrase ("le la mede ... consaputi libri").'),
}

STEPS = [
    {'date': DATE, 'kind': 'access',
     'what': 'Re-read (REREAD_BRIEF, batch b04): the 26 DECODE page images of R26 and R179-R188 fetched with the project '
             'cookie (research/reading_audit/b04_fetch.py; scratchpad only, not in the repository) and R26\'s '
             'transcription DOC_R26_D1635 (NiLan 2017) saved to decode/keep/. The pages carry no interlinear or margin '
             'decipherment; the clear text in the margins of some images is the facing leaf of other letters. A web '
             'search found no edition of the 1736 ciphers to Guiccioli; the minutes would be in the Madrid '
             'nunciature archive (not digitised).',
     'result': 'partial', 'technique': ['other']},
    {'date': DATE, 'kind': 'transcription',
     'what': 'The DECODE transcriptions re-segmented with Lasry\'s rules (7 null outside groups, 1xxx nomenclator, '
             'else pairs; b04_seg.py) instead of Lasry\'s segmented file, which leaves out whole runs (423/5: 137 of '
             '177 non-null tokens; about 20% in all). Fifteen unclear or struck figures resolved on the images and '
             'by sense (texts/423_b04_corrections.tsv); per-letter decodes in texts/423-<n>_decode_b04.txt.',
     'result': 'worked', 'technique': ['manual reconstruction']},
    {'date': DATE, 'kind': 'key from source',
     'what': 'Key corrected and extended from the documents (texts/b04_key_additions.txt): two-digit 25 = che (Lasry ";"), '
             '30 = ta (not to), 69 = z (not t), 93 = nel (not quel); nomenclator 1234 = qual (was Ministr/Nunzi), '
             '1205 = com (was che), 1241 = tant (was molt), 1210 = esser (was restar), each tested on every '
             'occurrence; 34 new firm values (medesim, cont, aver, fatt, Mons., ben, letter, part, issim, interess, '
             'relazion, pubblic, spagnuol, dett, parlar, Regn, volt, tre, due, ordinari, riguard, tropp, ragion, '
             'present, qualch, manier, liber, aggrav, ordin, avvis, procur, scriv, molt, Nunzi) and about 30 probable '
             'ones printed [?x].',
     'result': 'worked', 'technique': ['contextual inference', 'key-structure hypothesis']},
    {'date': DATE, 'kind': 'reading',
     'what': 'Readings built sentence by sentence for 423/2, 423/4-11 (texts/423-<n>_reading.md, English _en.md) and '
             'aligned word by word with the decode (b04_align.py): every unbracketed word is carried by figures or a '
             'nomenclator value; supplied words bracketed. _check_reading.py on the bodies (abbreviations de-dotted): '
             'clean-sentence share 0.47-0.71 (the strict count treats every [?x] probable value as a hole).',
     'result': 'worked', 'technique': ['manual reconstruction', 'contextual inference', 'language-model scoring']},
    {'date': DATE, 'kind': 'reading',
     'what': '423/1 (R26, 14 July 1736) read through on NiLan\'s weaker transcription (texts/423-1_reading.md, _en.md): '
             'the sentences of the riots, the Ostia and Trastevere enlistments, Acquaviva and Montemar build, but about '
             'a dozen runs do not decode (clean share 0.31); not re-transcribed from the images in this session.',
     'result': 'partial', 'technique': ['manual reconstruction', 'contextual inference']},
]


def tokens():
    return {n: sum(1 for t in b04_seg.segment(b04_seg.digits(n)) if t != '7') for n in range(1, 12)
            if n in b04_seg.DOC} | {3: sum(1 for t in b04_seg.segment(b04_seg.digits(3)) if t != '7')}


def main():
    tk = tokens()
    total = sum(tk.values())
    read_docs = ['423/%d' % n for n in range(2, 12)]
    read_tok = sum(tk[n] for n in range(2, 12))
    frac = round(read_tok / total, 3)
    p = load(F)
    o = p['outcome']
    for t in o['texts']:
        d = t['doc']
        n = int(d.split('/')[1])
        if d in READ:
            g, note = READ[d]
            t['state'] = 'read'
            t.pop('note', None)
            t['reading'] = 'texts/423-%d_reading.md' % n
            t['translation'] = 'texts/423-%d_en.md' % n
            t['language'] = 'it'
            t['decryption'] = ['texts/423-%d_decode_b04.txt' % n] + [x for x in t['decryption']
                                                                     if x != 'texts/423-%d_decode_b04.txt' % n]
            t['reading_review'] = {'grade': g, 'by': BY, 'date': DATE, 'note': note + ' Rests on ' + BASIS + '.'}
        elif d == '423/1':
            t['reading'] = 'texts/423-1_reading.md'
            t['translation'] = 'texts/423-1_en.md'
            t['decryption'] = ['texts/423-1_decode_b04.txt'] + [x for x in t['decryption']
                                                               if x != 'texts/423-1_decode_b04.txt']
            if 'decode/keep/DOC_R26_D1635_1635.txt' not in t['transcription']:
                t['transcription'] = t['transcription'] + ['decode/keep/DOC_R26_D1635_1635.txt']
            t['note'] = ('Re-read 22 Oct 2026 (batch b04; texts/423-1_reading.md, _en.md, 423_b04_reread_log.md): with '
                         'the corrected key most sentences build (the riots, the enlistments, Acquaviva, Montemar), but '
                         'about a dozen runs of NiLan\'s 2017 transcription do not decode and several sentences keep '
                         'two or three holes (clean share 0.31). Workable, not an outside blocker: re-transcribe the five '
                         'R26 pages from the DECODE images (IMG_R26_I145-I149) and re-read.')
    o['fraction_read'] = frac
    o['fraction_read_method'] = 'measured'
    o['fraction_read_source'] = (
        '22 Oct 2026, re-read batch b04: tokens of the documents that read / all, non-null tokens of the DECODE '
        'transcriptions re-segmented by research/reading_audit/b04_seg.py: %d / %d (423/2-11 read; 423/1, %d tokens, '
        'decoded, not read). Before: 0.016 (423/3 only, reading audit). Withdrawn earlier: 0.953 (tokens valued).'
        % (read_tok, total, tk[1]))
    o['notes'] = ('Solved by Lasry in 2020 except the nomenclator, which his key leaves unvalued. Re-read 22 Oct 2026: '
                  'four two-digit values and four nomenclator values of the earlier key corrected, about 65 groups '
                  'valued from context (texts/b04_key_additions.txt), ten of the eleven letters read and translated; '
                  '423/1 waits for a re-transcription. About 60 groups, mostly seen once, stay open.')
    o['key'] = 'partial'
    o['gaps'] = [
        {'item': '423/1 (R26, 1,641 tokens), decoded, not read', 'blocker': 'not-attempted',
         'detail': 'about a dozen runs of the 2017 transcription do not decode; re-transcribe the five R26 pages from '
                   'the DECODE images and re-read texts/423-1_reading.md'},
        {'item': 'about 60 nomenclator groups, mostly single occurrences (dates, 1513, 1449, 1664, 1844 ...)',
         'blocker': 'no-key-material', 'detail': "Lasry's key has no nomenclator; no other text in this code is known"},
        {'item': '423/9 "[..] danno"; 423/11 "le la mede [..] consaputi libri", "ben [..]giata"',
         'blocker': 'not-attempted', 'detail': 'checked in the decode only, not on the images'},
        {'item': 'the minutes of these letters (Archivio della Nunziatura di Madrid)', 'blocker': 'needs-physical-access'},
    ]
    if 'transcription' not in o.get('contribution', []):
        o['contribution'] = o['contribution'] + ['transcription']
    save(F, p)
    for s in STEPS:
        p = load(F)
        if any(x.get('what') == s['what'] for x in p['solution']):
            continue
        p['solution'].append(s)
        save(F, p)
    print('fraction_read', frac, read_tok, total, tk)


if __name__ == '__main__':
    main()
