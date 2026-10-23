# r2n re-read log: the thirteen located cipher passages (23 Oct 2026, Claude Opus 5.5)

Method: NA 3.01.18 inv. 401 scans fetched full size (scratchpad only); each cipher line cut at native size and read group
by group (`research/reading_audit/r2n_line.py`-style strips); codes looked up on the key scans of NA 1.10.29 inv. 1209
with `research/reading_audit/r2n_keylook.py` (one code) and `research/reading_audit/r2n_allblocks.py` (one number in all
fifteen blocks, used when the mark is unclear: the block is chosen by the sense). New key rows in `key/dict/r2n.tsv`.
Token files `tokens/s<scan>_r2n.txt`.

## 2 Jan 1687, 35R/36L (interlinear decipherment of the time)

- Interlinear in a second hand over most groups; hard to read, often shifted one group to the right of its figures.
- Key and interlinear agree: 3:937 dat, 11:431 seggen, 6:374 in, 8:718 niemant, 4:161 die, 9:653 op (bar hidden under a
  paper repair), 6:5 het, 10:925 remedieren, 7:109 Koninginne, 4:439 duysent, 10:278 pistolen, 14:421 voor, 4:547 een,
  8:733 nieuwjaar, 5:469 geven, 11:678 soo, 13:171 veel, 14:242 vinden, 14:175 vierhondert, 12:413 Syne Majesteyt, 1:738 al,
  13:112 van, 8:296 nabuyren, 4:526 dwingen, 7:336 laat, 13:226 veranderen, 8:725 niettemin, 6:297 ick, 13:144 vast,
  8:146 moeten, 4:293 doen; letter runs woude, heeft, konnen, weduwe, gehadt, pragmatica, sullen, men, gaern sigh.
- Disagreements: 10:703 is "rabat" in the key; the clerk wrote "in een" with a word in the margin I cannot read.
  5:331 is "geloof" in the key (5:330 gelooft); the clerk wrote "gelooft".
- Not resolved: 35R 1:273 (interlinear 'van'?), 437 and 254 (interlinear "sy persoon"; no block gives persoon at 437),
  361 448 (interlinear unread), 484, 405 308 (interlinear "[?] jaeren"), 74ø, the whole of the last line 1 121 54 577
  alle 216 35 409 (interlinear "... alle soorten ..."), 36L 280 761 (interlinear "[?] ook").
  The clerk's hand is readable for most words at native size; the reading follows the key where they agree and the clerk
  where the key gives no sense (marked in readings/r2n/1687-01-02_reading.md).

## The other twelve passages

| passage | groups | key work | result |
|---|---:|---|---|
| 13 Mar 1687 54R | 130 | 3:776 contenteren, 15:428 wegh, 6:704 Napels, 4:810 esloigneren, 4:573 eerste, 2:750 beyde | read; 886 open |
| 13 Mar 1687 55R | 50 | 6:880 Keyserinne, 3:892 daarnaar, 15:513 weynigh, 7:442 gelegen, 11:581 slechten, 3:249 brengen | read; 2:888 blank row |
| June 1687 67L | 34 | 11:679 sooals, 13:377 verdrucken, 6:807 kanten, 11:454 self, 12:493 tegen, 9:336 onderdanen, 11:212 met sak en pak | decoded, not read (letter run t-e-s-m-o-g-n-e-r-e-n) |
| July 1687 69L | 34 | r2j l. 3 re-read: 843 struck = 11:843 de Indien (12:843 trevis no sense), 925 with the bar = 9:925 overeenkomen; 6:796 konde, 12:478 te vrede zyn | read |
| Aug 1687 73R | 34 | 13:229 veranderlyke, 15:567 werk, 7:810 mainteneren, 5:895 heeren | decoded, not read (one sentence, 2 small holes) |
| 11 Sept 1687 78R | 60 | 11:794 president v. Castille, 11:791 Connestable, 11:951 spreken; first run 4:260, 11:117, 1:779, 8:60 no sense | read (second run) |
| 25 Sept 1687 80R | 55 | 4:482 Weenen, 4:446 den Keyser, 11:783 den Coninge, 14:531 voorslagen, 11:788 Medina Celi, 10:367 poort, 1:767 allebeyde | decoded, not read |
| 18 Dec 1687 93R/94L | 219 | 8:302 nadat, 10:872 regiment, 15:703 winter, 11:708 soecken, 8:416 Nederlandt, 7:248 krygh, 10:710 raadt, 9:675 opdragen, 10:445 preferéren | read |
| 18 Dec 1687 94R after l. 5 | 82 | 9:624 oorsaak, 6:596 introduceren, 11:216 saken | decoded, not read |
| 1 Jan 1688 95R | 23 | 15:325 wat, 10:403 post | read; 11:861 row illegible on the crop |
| Jan 1688 99L | 85 | 15:548 welk, 9:594 ook; third run 886, 688, 878, 214, 154, 980 no sense | decoded, not read |
| 26 Feb 1688 102L | 54 | 2:825 Biecht-Vader (interlinear 'Biechtvader'), 15:540 welsprekende, 11:760 sonder twyffel | decoded, not read; interlinear too faint |
| 11 Mar 1688 103R | 30 | 4:471 Hertogh van Holsteyn, 4:357 dragen | read |

Corrections to the r2j drafts: 69L l. 3 (above); 102L l. 1 '825 547' = 2:825 Biecht-Vader, 4:547 een. 93R: groups read
489 in three places are 12:409 syn (Battier's 0 with a loop); 94L 4:447/4:448 ('idem') where 4:446 den Keyser fits:
left [?den Keyser].

Failures: 80R 9x9 smudged; 93R 888 + 'o a', 178, 883; 94L 212, 256; 35R 361, 448 and the last run; 99L third run;
102L seven codes; 78R first run (the marks may be misread, the four candidate rows give no sense).

Scores (research/reading_audit/v2_score.py, explicit holes; the plain _check_reading word list scores every passage
0.0-0.25 because it does not know 17th-c. Dutch): 2 Jan 1687 0.778, 54R 1.0, 55R 1.0, 67L 0.0 (one sentence), 69L 1.0,
73R 0.0 (one sentence), 78R 0.75, 80R 0.60, 93R/94L 0.85, 94R tail 0.50, 95R 1.0, 99L 0.75, 102L 0.40, 103R 1.0.
Look-alike letters (0/8 struck o; 409/489) rest on the key word in fewer than 3% of letters in every read passage.
