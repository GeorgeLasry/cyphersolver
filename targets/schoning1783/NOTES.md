# Schöning's secret mission to Berlin, 1783-84 (KHA A32-603)

Status: in progress (scans fetched and being surveyed)

## Source

Koninklijk Huisarchief, The Hague, A32-603: "Correspondentie van G. von Schöning vanuit Potsdam met prinses
Wilhelmina en advocaat-fiscaal Van der Hoop, met ontcijfering van zijn brieven door Van der Hoop", 1783-1784, 212 scans
via the Koninklijke Verzamelingen rendition API (`scan_ids.json`; `img/` git-ignored). Part of A32-599-604, the file on
Schöning's secret mission to the Prussian court on Princess Wilhelmina's behalf. Found by the Nationaal Archief sweep,
KHA lead K4.

## Survey (25 Oct 2026, `survey.md`, subagent; counts estimated at ~1100 px)

- 43 letters by Schöning, 28 July 1783 - 10 July 1784: 34 to Van der Hoop (French, one Dutch), 9 to Princess
  Wilhelmina (German). Also her note, two notes of Frederick II, Larrey's memoranda.
- The system: running text in a symbol alphabet (hook and stroke signs, one per letter, word gaps), with names and
  titles as 2-3 digit code numbers followed by ":;." (61, 65, 66, 69, 70, 857, 880, 446, 191, 343, 155 ...).
- 24 letters (all to Van der Hoop) contain cipher: 6 partly glossed (No. 4 of 12 Aug 1783 interlined; the 25 Nov 1783
  copy glosses ~45 of 52 codes), 18 unglossed with about 400 code numbers (26 Jan 1784 alone ~100).
- 10 clear copies by the decipherer (No. 4, No. 5, 23/25/28 Nov, 13 Dec 1783, 3/6/19 Jan 1784, fragment 19-20 Dec):
  they write out the symbol text but leave the code numbers as numbers, except the 25 Nov copy.
- Larrey's memorandum (s180) lists a "Lettre déchiffrée de S. à Mr van der Hoop"; on 26 Jan 1784 Schöning says
  Van der Hoop could not read his last letter for numbers missing from his alphabet.
- Code values from context and glosses: 857 = S.M., 446 = Hertzberg, 914 = Thulemeier, 66/70 = Altesse / Altesse
  Sérénissime, 862 = Schöning; 450, 106 uncertain.

## Plan

1. Symbol alphabet from the copy/original pairs (10 pairs): label the signs in ASCII (the output filter stops long
   runs of unusual characters), align, and fix the letter table.
2. Code table from the 25 Nov 1783 glosses plus context across all letters.
3. Read the 14 letters with no clear copy and the unglossed codes; measure. Related keys to try on unglossed numbers: R1024 "Grand Chiffre" (Van Reede, Berlin
1787, `../vanreede1787/`).

## Prior work

No edition of these letters found on the web (25 Oct 2026); not on DECODE.
