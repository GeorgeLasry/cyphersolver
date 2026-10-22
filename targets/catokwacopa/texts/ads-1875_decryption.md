# Line-by-line reading of the two W. advertisements (The Standard, 8 and 20 May 1875)

Output of `measure.py` (5 Oct 2026), saved 22 Oct 2026; run with the en-modern LM check stubbed out (the corpus was not cached), so only its English-score assertion was skipped. Readings in capitals are the published ones the letters force (Bosbach, Estes/'Dave', Ernst, Krajcovic); lines marked `--` are unread, with the reason.

```
ln  A / B                                       chars  read  reading / reason
1   str / umem                                      7     7  SUMMER TERM  [search top (sum term); same words]
2   53 / 18                                         4     4  1853  [numerals: year, cf. 22]
3   catokwacopa / poayatlgerty                     23    23  CAP TOOK AWAY AT COLLEGE PARTY  [search + beam top; at college/catalogue the only rival]
4   olcabrokorlested / dpeatcnrftin                28    28  OLD CAP BROKE AT CORNER LEFT INSTEAD  [search top]
5   coomemega / nvtinrdn                           17     0  -- CONINGTON MET ME IN GARDEN needs a misprint; searches give conviction/convention me me garden
6   sesipyyocashostikr / dmlurpinrtrcamnr          34    16  USED SIMPLY YOUR CAP  [head forced in both searches (side/used simply your cap; SAID needs a misprint); tail open]
7   rep / etd                                       6     6  REPEATED  [search + beam top]
8   itedconlec / atndngtnsurs                      22    22  I ATTENDED CONINGTON LECSURES  [name frame: Conington only]
9   mistrl / otenpu                                12     0  -- mistrl/otenpu: phrase LM gives mist often purely; no forced reading
10  hrsclam / etfdorshpxn                          18    18  HERTFORD SCHOLARSHIP EXAMINATION  [name frame: Hertford only]
11  54.3 / 18                                       5     5  1853 4  [numerals: year]
12  caselcluchozamot / ndtsfindseseo               29     0  -- phrase LM: case land clutch so find size ...; junk
13  1.6.9 / cotegr                                  9     0  -- 1.6.9 / cotegr: no reading
14  mopredisco / tsvlysdinlge                      22    17  MONTHS PREVIOUSLY DISCLOSED  [search + beam top for the head; adverb privately/previously; tail indulge/in college open]
15  contoladsemot / ngtndusdcndo                   25    25  CONINGTON TOLD US TO ADD A SECOND MOTTO  [name frame: Conington only]
16  iadfilisat / edrstneirs                        20    20  I ADDED FIRST LINE SATIRS  [search top + positional rule]
17  qft / ui                                        5     5  QUI FIT  [Latin search top (Horace)]
18  cagap / ndted                                  10    10  CHANGE ADOPTED  [search + beam top, exact]
19  balmnopsemsov / iolapstedttoc                  26     0  -- BALLIOL MAN POSTED needs 11 misprints; phrase LM junk
20  ap138 / ap138                                  10     0  -- A.P. 138: plain in both ads, meaning unknown
21  hodsam / yxn                                    9     0  -- HOLIDAYS EXAMINE vs how days examine vs hold say mixing: not decided
22  55.6 / 18.18                                    7     7  1855 6  [numerals: year]
23  iopotonrogfimsecharsenr / wtubtrfftrstendinhofsvmnr    48     0  -- phrase LM: with you but portion frog fit ...; junk
24  tolshr / dily                                  10    10  TOLD SHIRLEY  [name frame: Shirley only]
25  itedjolec / atdwtsurs                          18    18  I ATTENDED JOWETT LECSURS  [name frame: Jowett only]
26  mistrl / oatvpu                                12     0  -- mistrl/oatvpu: moist relative put; junk
27  ding / y                                        5     5  DYING  [exact, 0 omissions]
28  declon / arati                                 11    11  DECLARATION  [exact, 0 omissions]
29  ereflodbr / rileohmae                          18     0  -- terrible flowed to him bare; junk; Latin junk

8 May ad: 134/238 = 0.563   20 May ad: 123/232 = 0.530
overall: 257/470 characters read as sense = 0.547
```
