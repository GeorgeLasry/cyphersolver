"""Re-read brief (REREAD_BRIEF.md), batch b00: morosini1588 (35 enclosures, Meister no. 40 key).

Targeted profile edits with the splice saver of relabel_r0.py (only changed spans are rewritten).

    PYTHONUTF8=1 python research/reading_audit/reread_b00.py <stats.json>

stats.json comes from reread_b00_stats.py (items, clean share before/after, holes, corrections per record).
"""
import json
import sys
import pathlib

sys.path.insert(0, str(pathlib.Path(__file__).parent))
from relabel_r0 import load, save  # noqa: E402

DATE = '2026-10-22'
BY = 'Claude Opus 5.5'
F = 'morosini1588'

GRADE = dict(R17='B', R18='B', R19='B', R20='B', R21='A', R22='B', R27='B', R28='B', R29='B', R30='B', R31='B',
             R32='B', R33='B', R34='B', R36='B', R37='A', R38='B', R39='A', R40='B', R41='A', R42='B', R43='B',
             R44='A', R45='A', R46='A', R47='B', R48='B', R49='A', R51='B', R52='B', R55='A', R56='A', R57='B',
             R58='A')
NOT_READ = {'R35'}
EXTRA = {
    'R17': 'Pages 233r, 234r-235v (233v not imaged, so 234r starts mid-sentence).',
    'R20': 'Pages run together in the DECODE transcription; split by sense and image (88r-90r, then 87r-v).',
    'R27': 'The whole leaf compared with the images (about 60 transcriber "?" settled).',
    'R30': 'Reading order 162v, 162r, 161v, 161r, 160r (leaves bound reversed).',
    'R31': 'Reading order 173r-174v, then 172r-v.',
    'R32': '181r-v corroded by the ink: most holes are there (crops could not settle single figures).',
    'R34': '199v ll. 18-19 under show-through and a hole in the paper.',
    'R38': 'The weakest DECODE transcription of the series (a third of the groups carry a spurious dot); '
           'only 282r ll. 1-7 compared with the image.',
    'R42': 'Noisiest transcription (systematic 1/2 and 8/5 errors); no image crops; context corrections unchecked.',
    'R43': 'Reading order 308r-309v, then 307r-v.',
    'R45': 'Reading order from the catchwords: 359r, 359v, 360r, 360v, 358r, 358v, 361r, 361v, 357r (one letter).',
    'R46': 'A leaf is missing between 382v and 383r (catchword "[u]alor" does not match); DECODE line 12 of 382r '
           're-read from the image (texts/R46_transcription_corrected.txt).',
    'R47': 'Reading order 386r-v, then 385r-v; the leaf after 385v is missing.',
    'R48': 'No image checks.',
}
SUMMARY = {
    'R35': ('Copy, in Spanish, of a memorandum ("scritura") the Spanish ambassador gave the Queen Mother: Philip II '
            'answers her wish to see the two crowns in close friendship and good understanding, praises it as worthy '
            'of the mother of two kings, and urges union against the heretics. Not a letter of Philip II (the '
            'Italian heading in cipher says so).'),
}


def note_for(r, s):
    parts = [f"Figures (DECODE transcription) segmented into words by reread_b00_decode.py and every break re-parsed by "
             f"hand on the figures; {s['corr']} transcription corrections or re-parses in texts/{r}_corrections.tsv "
             f"({s['image']} checked on the image, {s['context']} resting on one figure plus context, the rest carried "
             f"by the transcribed figures, mostly spurious nomenclator dots); aligned word by word with "
             f"reread_b00_align.py and every word the figures do not carry bracketed. Holes: {s['unread']} unread "
             f"stretches, {s['partly']} partly carried words" + (f", {s['codes']} unidentified codes" if s['codes'] else '')
             + f". _check_reading.py on the reading body {s['after']} (was {s['before']} on the decode). No contemporary "
             f"decipherment on the DECODE images; Rome's decifrati (Francia 27) not imaged."]
    if r in EXTRA:
        parts.append(EXTRA[r])
    return ' '.join(parts)


def rec_of(t):
    return t['doc'] if t['doc'].startswith('R') else t['label'].split(',')[0]


def main():
    stats = json.load(open(sys.argv[1], encoding='utf-8'))
    p = load(F)
    tot = sum(s['items'] for s in stats.values())
    rd = sum(s['items'] for r, s in stats.items() if r not in NOT_READ)
    for t in p['outcome']['texts']:
        r = rec_of(t)
        s = stats[r]
        if r in SUMMARY:
            t['summary'] = SUMMARY[r]
        if r in NOT_READ:
            t['note'] = (f"Re-read 22 Oct 2026 (batch b00): word decode with a Spanish word list and hand re-parse "
                         f"(texts/R35_reading.md, _en.md, {s['corr']} corrections, 3 on the image); the memorandum "
                         f"builds sentences in large part, but {s['unread']} unread stretches and {s['partly']} partly "
                         f"carried words in {s['words']} words leave several sentences open (_check_reading.py "
                         f"{s['after']}, was {s['before']}). No outside blocker: a full image pass of the doubtful "
                         f"lines is the next step; the last line is on damaged paper.")
            t['reading'] = 'texts/R35_reading.md'
            t['translation'] = 'texts/R35_en.md'
            t['language'] = 'es'
            continue
        t['state'] = 'read'
        t.pop('note', None)
        t['reading'] = f'texts/{r}_reading.md'
        t['translation'] = f'texts/{r}_en.md'
        t['language'] = 'it'
        t['reading_review'] = {'grade': GRADE[r], 'by': BY, 'date': DATE, 'note': note_for(r, s)}
    o = p['outcome']
    o['class'] = 'read in part'
    o['method'] = 'read with known key'
    o['method_basis'] = ("Meister 1906 no. 40, the key printed for Morosini's nunciature (Lasry's partial "
                         "reconstruction on DECODE R18), applied to DECODE's volunteer transcriptions. The character "
                         "decode left garbled words in most lines; on 22 Oct 2026 a word-level decoder with a "
                         "transcription-slip model and a hand re-parse of every break on the figures (and on the "
                         "images where a figure was in doubt) turned 34 of the 35 enclosures into sentences, translated; "
                         "most garbles were spurious nomenclator dots in the transcriptions and the clerk's -mente "
                         "abbreviation (m + null 8). R35, a Spanish copy, still has too many holes.")
    o['contribution'] = ['decipherment with ambiguous key', 'transcription', 'catalogue correction',
                         'sender or date identified']
    o['fraction_read'] = round(rd / tot, 3)
    o['fraction_read_method'] = 'measured'
    o['fraction_read_source'] = (f"22 Oct 2026, re-read (batch b00): figures (transcription items) of the enclosures "
                                 f"that read as sentences / all = {rd} / {tot}; R35 ({stats['R35']['items']} items) "
                                 f"does not yet. Per record, texts/<R>_reading.md, _en.md; _check_reading.py on the "
                                 f"reading bodies 0.53-0.86 (the clerk's spellings count as holes; every reading was "
                                 f"also judged sentence by sentence). Holes inside the readings are listed per record "
                                 f"(reading_review notes, texts/<R>_reread_log.md). Earlier figures withdrawn: 0.998 "
                                 f"(key coverage, 14 Oct) and 0 (audit, 22 Oct).")
    o['gaps'] = [
        {'item': 'R35 (Spanish memorandum of the Spanish ambassador)', 'blocker': 'not-attempted',
         'detail': '17 unread stretches and 10 partly carried words in 531 words; full image pass of the doubtful lines '
                   'not done (only 202r ll. 6-8 cropped); last line on damaged paper'},
        {'item': 'short unread stretches inside the 34 readings (about 540 holes in 33,000 words: openings and '
                  'closings, one-to-eight-figure groups that no word parse fits)',
         'blocker': 'not-attempted',
         'detail': 'many checked on the image and found transcribed as written (encipherer slips); the rest not '
                   'cropped (R42, R48 none); Rome\'s decipherments in Segr. Stato Francia 27 would settle them'},
        {'item': "Rome's decipherments of these ciphers (ASV Segr. Stato, Francia 27; Hübner 1870 cites ff. 248-275, "
                 'deciphered 9 Jan - 9 Mar 1589)', 'blocker': 'needs-physical-access',
         'detail': 'not imaged online'},
        {'item': 'missing leaves: R46 between 382v and 383r, R47 after 385v; R17 233v and R22 last leaf not imaged',
         'blocker': 'needs-physical-access', 'detail': 'catchwords do not match / not on DECODE'},
        {'item': 'item 22/29', 'blocker': 'needs-physical-access',
         'detail': 'no DECODE record; not imaged; its key is not known'},
    ]
    o['notes'] = (o['notes'] + ' 22 Oct 2026, reading audit: all 35 decoded, not read (class not read). Same day '
                  're-read (batch b00): 34 read as sentences and translated, R35 not yet; class read in part. The '
                  'dotted codes outside Meister\'s list (162, 191, 250, 516, 617, 716, 770 ...) turned out to be '
                  'spurious dots on letter groups or real codes with the dot on the wrong figure; no new code value. '
                  'Abbreviations: m + 8 = -mente, 8 also after other short forms (bo. mem., S. Alt.).')
    o['codes_open'] = {'open': sum(s['codes'] for s in stats.values())}
    o['parts'] = [{
        'label': 'R17-R58, Meister no. 40 key (35 enclosures; 34 read as sentences, R35 not yet)',
        'records': 'DECODE R17-R22, R27-R49, R51, R52, R55-R58', 'method': 'read with known key', 'extent': 'partial',
        'basis': "Meister's printed key on DECODE's transcriptions; word-level decode and hand re-parse of the figures "
                 '(spurious dots, transcription slips), images checked where a figure was in doubt; 22 Oct 2026.'}]
    o['credits'] = o['credits'] + [
        {'who': 'tempesti', 'role': 'pointer',
         'note': "Storia della vita e geste di Sisto Quinto II (1754), books VI-XIII, paraphrases many of these "
                 "letters from Rome's decipherments; used to recognise names and sense, never as a source of words",
         'date': '1754', 'source': 'C. Tempesti, Storia della vita e geste di Sisto Quinto (Rome 1754), archive.org '
                                   'storiadellavitae02temp'},
        {'who': 'hubner', 'role': 'pointer',
         'note': "cites Rome's decipherments of Morosini's ciphers in ASV Francia 27 with their dates, and compared "
                 "Tempesti with them", 'date': '1870',
         'source': 'J. A. de Hübner, Sixte-Quint II (Paris 1870), pp. 209, 232-233'}]
    save(F, p)
    p = load(F)
    c = p['conditions']
    c['prior_solution']['where'] = (c['prior_solution']['where'] + ' Found 22 Oct 2026, after the readings: Rome '
                                    'deciphered these letters at the time (ASV Segr. Stato Francia 27, cited by Hübner '
                                    '1870, not imaged), and Tempesti 1754 paraphrases parts of many of them.')
    if 'images' not in c['inputs']:
        c['inputs'] = ['images'] + c['inputs']
    save(F, p)
    steps = [
        {'date': DATE, 'kind': 'access',
         'what': 'Re-read under REREAD_BRIEF (batch b00): the DECODE cipher images of all 35 records and their '
                 '"cleartext" images fetched with the DECODE session cookie into the session scratchpad (not the '
                 'repository).',
         'result': 'worked'},
        {'date': DATE, 'kind': 'literature search',
         'what': 'Is there a text already? The cleartext images are covering letters and address leaves, none a '
                 'decipherment; no interlinear glosses. Hübner, Sixte-Quint (1870) cites Rome\'s decipherments in ASV '
                 'Francia 27 (not imaged). Tempesti, Vita di Sisto V (1754) paraphrases many letters (R18-R22, R28, '
                 'R33, R43, R46, R48 ...) between quotation marks: used for names and sense only.',
         'result': 'partial'},
        {'date': DATE, 'kind': 'solver',
         'what': 'Word-level decoder research/reading_audit/reread_b00_decode.py: beam search over words (Nuntiaturberichte '
                 '+ Guicciardini vocabulary with single-for-double variants, word bigrams), Meister homophones, nulls 8 '
                 'and 8x, and a slip model (one figure substituted, dropped or added); texts/<R>_worddecode.txt. Most '
                 'garbles became words; about one word in ten still needed a hand re-parse.',
         'result': 'partial', 'technique': ['beam/DP decoding', 'language-model scoring']},
        {'date': DATE, 'kind': 'transcription',
         'what': 'Every remaining break re-parsed on the transcribed figures, and on image crops where a figure was in '
                 'doubt (reread_b00_crop.py); about 1,750 corrections in texts/<R>_corrections.tsv. Causes: spurious '
                 'nomenclator dots on letter groups (250 = "Bles", 150, 214, 712 ...), real codes with the dot on the '
                 'wrong figure or none, the -mente abbreviation m + 8, plain-figure numbers between null 8s, page '
                 'order (R30, R31, R43, R45, R47).',
         'result': 'worked', 'technique': ['manual reconstruction', 'contextual inference']},
        {'date': DATE, 'kind': 'verification',
         'what': 'Each reading aligned word by word with its figures (reread_b00_align.py, banded DP over Meister\'s '
                 'homophones and the slip costs) and every word the figures do not carry bracketed.',
         'result': 'worked', 'technique': ['beam/DP decoding']},
        {'date': DATE, 'kind': 'reading',
         'what': 'Readings and English translations written for all 35 (texts/<R>_reading.md, _en.md, _reread_log.md). '
                 '34 build sentences (state read; grades A 12, B 22); R35, the Spanish memorandum, keeps too many '
                 'holes (decoded, not read). Class not read -> read in part; method -> read with known key.',
         'result': 'partial', 'technique': ['manual reconstruction', 'contextual inference']},
    ]
    for s in steps:
        p = load(F)
        p['solution'].append(s)
        save(F, p)


if __name__ == '__main__':
    main()
