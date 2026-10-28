# Ellis to Forsyth, Mexico, 26 Oct 1836 (catalogue 653): the coded passage as sentences

English, so no translation. Groups: `ellis1836oct26_transcription.txt` (90 groups, M97 roll 8 frames 0323 and the top
line of 0324). Decode: `python decode.py ellis1836oct26_transcription.txt` (`../jqa/code_table.tsv`, unchanged), 85 of
90 groups with a value. This is the one coded passage of Ellis's 1836-40 despatches with no decipherment on the film;
Bosch García (*Documentos de la relación de México con los Estados Unidos* III, UNAM 1984) prints the text, ending at
"succor from that power". The reading below follows the groups and agrees with the print; where the groups add or
lack a word, it is noted.

## Reading

[Clear, frame 0323: "... penetrate into the enemy's country, and of changing the plan of operations heretofore
adopted into a guerilla system of warfare."]

However confident the officers may be of their success in the ensuing campaign, there is no doubt but that a panic
already prevails among the soldiers; and an [285] evident disappointment is manifested both by the government and
the people, because of recent information received from England, which leaves them no hope to anticipate[?] succour
from that power.

[Clear, frame 0324: "So far as I can ascertain perfect tranquility reigns throughout the Republic. There is nothing
doing in Congress." Signed Powhatan Ellis.]

## Groups and values

| line | groups | read as |
|---|---|---|
| 0323.01 | 4 | however |
| 0323.02 | 114 369 1385 1576 | confide-nt the of- |
| 0323.03 | 330 1021 627 1310 | -fi-cer(s) may be |
| 0323.04 | 1576 1386 385 1022 | of their suc-ces(s) |
| 0323.05 | 1426 1385 545 387 | in the en-sue- |
| 0323.06 | 1429 1004 1102 1418 | -ing cam-pa-ig- |
| 0323.07 | 401 1261 1391 1436 | -n , there is |
| 0323.08 | 352 799 1301 1361 | no doubt b(u)-t |
| 0323.09 | 1384 1501 1106 1404 | that a pa(n)-ic |
| 0323.10 | 1535 733 208 453 | al-ready pre-vail(s) |
| 0323.11 | 1548 1385 249 1452 | among the so-l(l)- |
| 0323.12 | 833 269 1262 668 | -di-ers ; and |
| 0323.13 | 1549 285 824 845 | an [285] (evi)dent dis- |
| 0323.14 | 675 1149 637 1436 | -ap-point-ment is |
| 0323.15 | 614 520 1349 792 | manifest-ed both by |
| 0323.16 | 1385 1229 637 668 | the govern-ment and |
| 0323.17 | 1122 1261 1315 1576 | people , because of |
| 0323.18 | 731 1019 1426 981 | re-cen(t) in-for- |
| 0323.19 | 625 736 999 1290 | -mation received from England |
| 0323.20 | 1176 587 458 1387 | which lea-ve(s) them |
| 0323.21 | 352 195 569 1549 560 | no hope to an-ti- |
| 0323.22 | 1028 1114 501 385 1053 | -ci-pat[?]-e suc-cour(t) |
| 0324.01 | 999 1384 205 | from that power |

Notes on single groups:

- **401** = *n* (table: *sian*). Ellis uses it for *n* in 1839 as well (fron-n-tier, know-n, America-n; NOTES.md) and
  Brackx found it in 1836 (an-nou-n-cing, Sa-n-ta).
- **1261** comma, **1262** semicolon: the punctuation groups (1261 fixed by the 1839 clear copy; 1262 by Brackx from
  19 May 1836). The table has no value for them.
- **1301 1361** = *b-t*, read as "but": "no doubt but that". The print has "no doubt that"; the groups have the word.
- **1106** = *pa* (M) gives "pa-ic": Ellis's code drops the *n* of "panic" or 1106 is *pan* here.
- **285** has no value in the table and stands where "evi-" would go before 824 *dent*. Brackx takes it as a null
  (it also stands where the print has no word on 19 May, "stop to this [285] by"). Left open.
- **1114** = *pat* is Brackx's value (des-pat-ches, 3 Aug 1836); it has no value in the table. Marked [?].
- **1053** = *court* (C), read *cour* in "succour". The group carries a tick under it, as 285 does; what the ticks mean
  is not established.
- **614** = *manifest* (table, C) is right here ("manifested" in the print). Brackx's tentative value *know* for 614
  (ac-know-ledge, one context) would give "known": it is a second value at most, not a replacement.
- The marks under 1021, 1022, 453, 736 and 458 (diamond, cross, caret) all fall on groups whose table value already
  reads; they may be Ellis's own signs for -s or for a plural (officer-s, succes-s, prevail-s, leave-s), but that rests
  on four cases and is not used.

## Measure

90 groups. 85 have a value in the table; with the three punctuation and Ellis values (401 *n*, 1261, 1262) and 1114
*pat* [?], 89 of 90 give sense in the reading. Open: 285 (one group). Read share 89/90 = 0.989 (0.978 without
1114). Wrong-key controls (`python decode.py ellis1836oct26_transcription.txt --controls`): function-word rate 0.26
for the table, 0.01-0.07 for shifted groups and permuted tables.
