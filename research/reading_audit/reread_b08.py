"""Re-read brief (REREAD_BRIEF.md), batch b08: malsburg1637 (HStAM 4 h Nr. 1411, HCPortal 496-509).

Targeted profile edits with the splice saver of relabel_r0.py; one save per appended item.

    python research/reading_audit/reread_b08.py
Helpers: b08_crop.py (scan crops to the scratchpad), b08_dec.py (line decoder with group pairs), b08_norm.py (spelling
normalisation of the reading bodies), b08_align.py (word-by-word check against the decode), b05_score.py (clean-sentence
share of a reading body).
"""
import sys
import pathlib

sys.path.insert(0, str(pathlib.Path(__file__).parent))
from relabel_r0 import load, save  # noqa: E402

F = 'malsburg1637'
DATE = '2026-10-22'
BY = 'Claude Opus 5.5'
LOG = 'HCP496-509_reread_log.md'
BASIS = ('the transcription decoded with key.txt unchanged (research/reading_audit/b08_dec.py), breaks checked on the '
         'HCPortal original scans (fetched 22 Oct 2026, scratchpad only), spelling normalised in part '
         '(b08_norm.py), aligned word by word with the decode (b08_align.py), words the figures do not carry bracketed. '
         'No contemporary decipherment, clear copy or edition. Log: ' + LOG)

READ = {
    'HCPortal 496': ('B', 'f. 3, 5/15 Jan 1637, to the councillors at Kassel: no one knows where the garrisons\' upkeep '
                          '(grain and [201]) is to come from now that the contributions here and in [239] have ended; '
                          'the monthly ration in Kassel quarters; it is still time to approach the King of Hungary about '
                          'the peace talks and a safe-conduct for envoys to Cologne; [176] will not negotiate without '
                          '[140]; days of prayer are needed. Clean share 0.667 (6/9). Holes: codes 201, 239, 193, 273, 210, '
                          '144, 176, 140 and the signs +, f, 4#, H#; one clause (the monthly ration) is a string of codes.'),
}

UNREAD = {
    'HCPortal 502': ('HCP502', 'clean share 0.167 (3/18; before 0.143): the cipher now builds sentences in part (the '
                     'provisioning of Hermanstein under Lt-Col. Hoffman; the road from Cologne by Mülheim and Siegburg; '
                     'Jan de Werth; Hoffman back by Marburg, Korbach, Brilon), but nearly every sentence holds two to six '
                     'open codes or signs (145, 235, XX, 191, f, 193, o, 200, K, 4#, m, 262, 266, 189, +, 210, 215, 138, '
                     'SS) and the torn right edge has cut the last group of many lines. Blocker: open-codes (and the '
                     'torn edge)'),
    'HCPortal 503': ('HCP503', 'clean share 0.375 (9/24; before 0.389 on the raw decode): Beauregard\'s audience, Hoff\'s '
                     'reports, the recruiting patents, the ambassador\'s orders, "er redet aber nirgent von Fritmachen" '
                     'build as German, but most sentences hold several open codes (120, 122, 129, 193, 201, 202, 212, '
                     'XX) and signs (4#, A#, H#, +, f, 4H#, e), and the crossed H stands for ll in some words and tt in '
                     'others. Blocker: open-codes'),
    'HCPortal 507': ('HCP507', 'clean share 0.437 (31/71; before 0.271): read with the writer\'s duplicate (HCPortal '
                     '508) as a control, the letter builds German sentences throughout (the journey by land or by sea '
                     'and its four objections; the twelve-pounders without carriages; Wartenberg discharged; Uffel and '
                     'Karpf; the questions for the States; the conjunction at Cloppenburg or Vechta; the Reiderland; '
                     'Hohendorf and the Land of Hadeln), but about 40 open codes and signs (193, 212, 273, 200, 122, 129, '
                     '188 ...) and many place names outside the word list keep most 12-word windows unclean. Blocker: '
                     'open-codes'),
    'HCPortal 509': ('HCP509', 'clean share 0.545 (24/44, the French paragraph scored as French, 23/30; before 0.182): the '
                     'French letter of "232" (3 Apr 1637) transcribed from the scan and read with its cipher runs ("par '
                     'la lettre de nre ambassadeur extraordinaire qui est a Londres", "a Mons Sengel a Londres", "ledict '
                     'Sengell"); the German news extracts in the second hand (lower f. 32, f. 33) are given only as '
                     'decoded runs between the clear words of the 28 Sept transcription, which do not build sentences. '
                     'Blocker: not-attempted (the clear text of the second hand was not re-transcribed) and open-codes '
                     '(OO, AA, XX, GG, CC, KK, LL, 115, 123, 126, 129, 133, 148, 155, 156, 248)'),
}

DUP = ('duplicate of ff. 28-29 (excluded from the measure). Re-read 22 Oct 2026 (batch b08) together with HCPortal 507 '
       'as its control copy: where the two copies differ the reading of 507 follows the copy whose figures give a word '
       '(HCP507_corrections.tsv); its text and state are those of 507 (decoded, not read, clean share 0.437)')

STEPS = [
    {'date': DATE, 'kind': 'access',
     'what': 'Re-read (REREAD_BRIEF, batch b08): HCPortal records 496, 502, 503, 507, 508, 509 and their 12 original scans '
             'fetched from api.hcportal.eu (browser User-Agent and Origin header; scratchpad only). No contemporary '
             'decipherment on any leaf or address side, no clear copy, no edition (NOTES Escalation).',
     'result': 'worked', 'technique': ['other']},
    {'date': DATE, 'kind': 'reading',
     'what': 'Readings built sentence by sentence from the decodes with the group under each letter (b08_dec.py), the '
             'breaks checked on scan crops (b08_crop.py): HCP496/502/503/507/509_reading.md with English _en.md. ff. '
             '28-29 read against the writer\'s duplicate ff. 30-31 (HCP507_corrections.tsv: uberlant, Schieffe, wider '
             'Bestellung (the "128" of f. 28 is a w-group), Forstenau aber, Hohendorf, den Rest, Rantzo); f. 32 '
             'extraordin<Q>re (not mm), f032_corrected.txt; the French letter of "232" transcribed from the scan. '
             'Signs whose value is not one letter pair (the crossed H gives ll and tt; the lone 7 gives st, ö and b) '
             'left open. Spelling normalised in part (b08_norm.py) and every reading aligned word by word with its '
             'decode (b08_align.py), which caught "Verlusts", "Tractes", "itzigen" and unmarked slips, all corrected or '
             'bracketed.',
     'result': 'partial', 'technique': ['manual reconstruction', 'contextual inference']},
    {'date': DATE, 'kind': 'verification',
     'what': 'Clean-sentence share of the reading bodies (b05_score.py; before = the reading_segmented.txt blocks of the '
             'document): HCPortal 496 0.333 -> 0.667 (read, B); 502 0.143 -> 0.167; 503 0.389 -> 0.375; 507 0.271 -> '
             '0.437 (508 its duplicate); 509 0.182 -> 0.545 with the French paragraph scored as French (decoded, not '
             'read: the German extracts are not re-transcribed). fraction_read 0.436 -> 0.480.',
     'result': 'partial', 'technique': ['language-model scoring', 'statistical test']},
]

NEW_GAPS = [
    {'item': 'HCPortal 502, 503, 507 (with the duplicate 508): decoded, not read after the 22 Oct 2026 re-read (clean '
             'share 0.167, 0.375, 0.437)', 'blocker': 'open-codes',
     'detail': 'German sentences build around the codes, but most sentences hold two or more open three-digit codes or '
               'signs; f. 14 also has its right edge torn. Readings and translations: HCP502/503/507_reading.md, _en.md'},
    {'item': 'HCPortal 509: the German news extracts (lower f. 32, f. 33) in the second hand', 'blocker': 'not-attempted',
     'detail': 'the clear text between the cipher runs was not re-transcribed on the scan (22 Oct 2026); the French '
               'letter of "232" on the same leaf is read (HCP509_reading.md)'},
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
            t['reading'] = 'HCP496_reading.md'
            t['translation'] = 'HCP496_en.md'
            t['language'] = 'de'
            t['reading_review'] = {'grade': g, 'by': BY, 'date': DATE, 'note': note + ' Rests on ' + BASIS + '.'}
        elif d in UNREAD:
            stem, why = UNREAD[d]
            t['reading'] = stem + '_reading.md'
            t['translation'] = stem + '_en.md'
            t['note'] = ('Re-read 22 Oct 2026 (batch b08; %s_reading.md, _en.md, %s): ' % (stem, LOG)) + why + '.'
        elif d == 'HCPortal 508':
            t['note'] = DUP + '.'
    save(F, p)
    for g in NEW_GAPS:
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
