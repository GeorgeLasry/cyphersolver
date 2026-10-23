import json
R = 'readings/r2n/'
REV = dict(by="Claude Opus 5.5", date="2026-10-23")
OUT = r'C:/Users/dbour/AppData/Local/Temp/claude/C--Users-dbour-cypher/6b6912a8-0ad3-4eda-b63e-c79291f1bcc5/scratchpad/reread/r2n_meta/actions.json'


def ent(doc, label, tok, state, summary, grade, note):
    e = dict(doc=doc, label=label, transcription=['tokens/' + t for t in tok], decryption=R + doc + '_reading.md',
             summary=summary, language='nl')
    if state == 'read':
        e.update(state='read', reading=R + doc + '_reading.md', translation=R + doc + '_en.md',
                 reading_review=dict(grade=grade, **REV, note=note))
    else:
        e.update(state='decoded, not read', note=note)
    return e


T = [
    ent('1687-01-02', '2 Jan 1687 (scans 35R, 36L)', ['s035R_r2n.txt'], 'read',
        "Battier to Fagel: nobody at court thinks of remedying affairs; the King could not find a thousand pistoles for the Queen's New Year; Spain will not let its neighbours force it to change the pragmatic, yet will have to.",
        'B', "r2n 23 Oct 2026: 156 groups read on the NA scan, every code looked up on the key scans; aligned with the interlinear decipherment of the time (30 codes and the letter runs agree; 10:703 rabat against the clerk's 'een'; 11:484 ses = 'ses jaeren'). [?als], [?sy] [?persoon], [?jaeren], [?begrypen], [?saecken] rest on the interlinear only; 361, 448 and the end of the 35R run unread. v2_score explicit holes 0.778 (7/9); plain word list 0.0 (17th-c. Dutch)."),
    ent('1687-03-13a', '13 Mar 1687, first letter (scan 54R)', ['s054R_r2n.txt'], 'read',
        "Oropesa is to speak for Cogolludo, Melgar and Balbases: Cogolludo's son to be sent to Rome and Naples, Melgar if that fails, Balbases to get him away.",
        'A', 'r2n 23 Oct 2026: 130 groups read on the NA scan and decoded with the key (new rows in key/dict/r2n.tsv). Open: 886; 2:750 [?beyde]. Explicit holes 1.0 (4/4). No contemporary decipherment.'),
    ent('1687-03-13b', '13 Mar 1687, second letter (scan 55R)', ['s055R_r2n.txt'], 'read',
        'The Empress says it matters little whether Spain, in so poor a state, joins or not; for the consequence Spain will not be brought to it.',
        'A', "r2n 23 Oct 2026: 50 groups read and decoded; 2:888 is a blank key row (the verb is missing). Continues WAINUT's 55L. Explicit holes 1.0 (3/3)."),
    ent('1687-06-10', 'June 1687 (scan 67L)', ['s067L_r2n.txt'], 'decoded, not read',
        "One is oppressed on all sides and cannot act against the subjects (67L; 67R is WAINUT's).", None,
        'r2n 23 Oct 2026: 34 groups read and decoded (13:377 verdrucken, 11:212 met sak en pak, 6:794 kan, 3:894 daarom); the verb spelled t-e-s-m-o-g-n-e-r-e-n is not settled and the passage is one sentence fragment: explicit holes 0.0 (0/1; 3 holes in 24 words). Kept decoded, not read.'),
    ent('1687-07', 'July 1687 (scan 69L)', ['s069L_r2n.txt'], 'read',
        'One could not be content with the declaration and must insist in England; agreement with the articles of the Indies; the explanation to the Emperor.',
        'B', 'r2n 23 Oct 2026: the r2j pilot line 3 re-read (843 struck = 11:843 de Indien; 925 with the bar = 9:925 overeenkomen); all 34 groups decode; one stray cipher letter e. Explicit holes 1.0 (4/4).'),
    ent('1687-08', 'Aug 1687 (scan 73R)', ['s073R_r2n.txt'], 'decoded, not read',
        'The Hofmeister is very changeable and will have trouble maintaining himself unless the Jesuits make it their business.', None,
        'r2n 23 Oct 2026: 34 groups read and decoded; the sentence builds, but 90 carries an unexplained backslash mark and a stray letter g stands after moeyte: 2 holes in 24 words, explicit holes 0.0 (0/1). Kept decoded, not read by the bar; one sentence only.'),
    ent('1687-09-11', '11 Sept 1687 (scan 78R)', ['s078R_r2n.txt'], 'read',
        'The President and the Constable of Castile, formerly against him, now speak for him, since Spain is thinking of the son of the Palatine.',
        'B', 'r2n 23 Oct 2026: 60 groups in two runs; the second (51 groups) reads; the first (9 groups: 260, 117, 779, 60) gives no sense with the marks as read. Explicit holes 0.75 (3/4).'),
    ent('1687-09-25', '25 Sept 1687 (scan 80R)', ['s080R_r2n.txt'], 'decoded, not read',
        "Letters from Vienna and the Palatinate delayed; if the Emperor proposed the Palatine's son Spain would agree; if Medinaceli came in by one gate, [the President of Castile] would go out by another.", None,
        "r2n 23 Oct 2026: 55 groups in four runs read and decoded; 894, 9x9, 548, 432, 422, 379, 756 give no sense and two runs break in the middle: explicit holes 0.60 (6/10), hole rate 0.14; kept decoded, not read on the reader's judgement."),
    ent('1687-12-18', '18 Dec 1687 (scans 93R, 94L)', ['s093R_r2n.txt', 's094L_r2n.txt'], 'read',
        'The Grand Master wrote to his agent Don Pedro Alvares that he would go to Vienna; he was unwell and could not follow the Emperor to Pressburg; he is thought to hold back on the Netherlands to see whether he gets the presidency of the war council.',
        'B', "r2n 23 Oct 2026: 219 groups read on the NA scan, all codes looked up; open 888, 178, 883, 675, 212, 256; 4:447/4:448 read where 4:446 den Keyser fits ([?den Keyser]). Explicit holes 0.85 (17/20). 94R ll. 1-5 are WAINUT's; 94R after l. 5 is a separate entry."),
    ent('1687-12-18b', '18 Dec 1687 (scan 94R after l. 5)', ['s094R_r2n.txt'], 'decoded, not read',
        'French refugees: Mr Schonenberg; the main cause; orders given. Letter runs in part only.', None,
        'r2n 23 Oct 2026: 82 groups read and decoded; 406, 706, 238, 116, 653, 724, 312, 830 without sense: explicit holes 0.50 (3/6). Kept decoded, not read.'),
    ent('1688-01-01', '1 Jan 1688 (scan 95R)', ['s095R_r2n.txt'], 'read',
        'Battier could not learn what the Grand Master [did] by this post, the holy days having prevented him from speaking to everyone.',
        'B', 'r2n 23 Oct 2026: 23 groups; 11:861 (struck) not legible on the key crop. Explicit holes 1.0 (2/2).'),
    ent('1688-01-29b', 'Jan 1688 (scan 99L)', ['s099L_r2n.txt'], 'decoded, not read',
        '60 thousand guilders, not pounds Flemish; the confessor, Nuñez Botello and Carnero did most; the Councils made no mention of the money.', None,
        'r2n 23 Oct 2026: scan 99 (failed in r2j) used from the b17 download; 85 groups in three runs; runs 1-2 read, run 3 (33 groups) has 886, 688, 878, 214, 154, 980 without sense: explicit holes 0.75 (6/8) but the third run does not build. Kept decoded, not read.'),
    ent('1688-02-26b', '26 Feb 1688 (scan 102L)', ['s102L_r2n.txt'], 'decoded, not read',
        "The confessor, a Theatine; conferences with ministers on behalf of the Grand Master.", None,
        "r2n 23 Oct 2026: 54 groups read (supersedes the r2j draft); 2:825 Biecht-Vader and the letters 'theatin' agree with the faint interlinear; 420, 335, 499, 114, 603, 800, 505 without sense and the interlinear too faint to supply them: explicit holes 0.40 (2/5). Kept decoded, not read."),
    ent('1688-03-11', '11 Mar 1688 (scan 103R)', ['s103R_r2n.txt'], 'read',
        'The Grand Master affair is off again; Melgar offers money; the Duke of Holstein desists; or the Grand Master is to marry the Infanta and receive the government of the Netherlands.',
        'A', 'r2n 23 Oct 2026: 30 groups in three runs, all decode (4:471 Hertogh van Holsteyn, 4:357 dragen). Explicit holes 1.0 (10/10).'),
]
src = ('Estimated. 22 Oct 2026 reading audit: 2,078 tokens of the letters that read, volume about 4,200 tokens (from the earlier 55% estimate). '
       '22-23 Oct (b17): 4 Dec 1687 and 12 Feb 1688 read: 2,560 of about 4,200 = 0.61. 23 Oct 2026 (r2n): the thirteen located passages read on the scans '
       '(1,046 groups, tokens/s*_r2n.txt, counted with scripts/decode.py); eight entries read (702 groups: 2 Jan 1687 156, 13 Mar 1687 54R 130 and 55R 50, '
       'July 1687 34, 11 Sept 1687 60, 18 Dec 1687 93R/94L 219, 1 Jan 1688 23, 11 Mar 1688 30), six decoded, not read (344). 2,560 + 702 = 3,262 of about 4,200 = 0.78 '
       "(estimated; WAINUT's contributed 1,389 groups still not counted).")
steps = [
    dict(date='2026-10-23', kind='transcription', technique=['other'], what='r2n: the thirteen located cipher passages (35R/36L, 54R, 55R, 67L, 69L, 73R, 78R, 80R, 93R, 94L, 94R after l. 5, 95R, 99L, 102L, 103R) read group by group on the full-resolution NA scans (scan 99 from the b17 download): 1,046 groups in tokens/s*_r2n.txt.', result='worked'),
    dict(date='2026-10-23', kind='key from source', technique=['key matching'], what='r2n: about 150 codes looked up on the key scans of inv. 1209 (research/reading_audit/r2n_keylook.py; r2n_allblocks.py cuts one number in all fifteen blocks when the mark is unclear); new rows in key/dict/r2n.tsv with the scan reference, non-fitting rows marked (not adopted).', result='worked'),
    dict(date='2026-10-23', kind='crib', technique=['plaintext matching'], what="r2n: 2 Jan 1687 (35R/36L) aligned with the interlinear decipherment of the time: 30 codes and the letter runs agree; 10:703 (key rabat) against the clerk's 'een'; 11:484 ses confirmed by 'ses jaeren'; five words carried by the interlinear only. 102L: 2:825 Biecht-Vader and 'theatin' agree with the faint interlinear.", result='worked'),
    dict(date='2026-10-23', kind='reading', technique=['key matching'], what='r2n: readings built and aligned word by word (readings/r2n/*_reading.md, _en.md); v2_score explicit holes: read 2 Jan 1687 (0.78), 13 Mar 1687 54R (1.0) and 55R (1.0), July 1687 (1.0), 11 Sept 1687 (0.75), 18 Dec 1687 93R/94L (0.85), 1 Jan 1688 (1.0), 11 Mar 1688 (1.0).', result='worked'),
    dict(date='2026-10-23', kind='reading', technique=['key matching'], what='r2n: kept decoded, not read: June 1687 67L (unresolved letter run, one sentence), Aug 1687 73R (one sentence, two small holes), 25 Sept 1687 80R (0.60, groups without sense), 94R after l. 5 (0.50), 99L (third run), 102L (0.40, interlinear too faint).', result='partial'),
]
json.dump(dict(add_texts=T, steps=steps, outcome=dict(fraction_read=0.78, fraction_read_source=src)),
          open(OUT, 'w', encoding='utf-8'), ensure_ascii=False, indent=1)
print('ok', len(T))
