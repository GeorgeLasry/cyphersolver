# Deboli → Stanisław August, St Petersburg cipher despatches, 1789 (Unsolved Catalogue 418)

Status: in progress

AGAD Warszawa, Zbiór Popielów (fonds 12), sygn. 17: "Deboli. 1789 (cyfry)", 106 cipher despatches of Antoni
Augustyn Deboli, Polish envoy at St Petersburg, to King Stanisław August, 2 January - 29 December 1789, k. 2-312
(AGAD's count is 113 pieces, k. 348). Scans on AGAD's own server:
http://agadd2.home.net.pl/metrykalia/12/album/17/index.html, letter list with image links
https://www.agad.gov.pl/inwentarze/ZbPop17.xml.

## Finding 1: the clear series holds the plaintext of 103 of the 106 despatches

ZbPop 419, "Deboli do króla 1789" (105 pieces, album 419 on the same server), is the Polish clear text of the same
despatches: 100 cipher despatches have a clear piece of the same date there (`pairs.tsv`). The clear texts of 22, 25
and 29 December 1789 are misfiled in ZbPop 417 (catalogued as 1788), nos. 114-116, with the January 1790 despatches.
Eleven pairs were transcribed in full and aligned group by group (`align.py`): 6 Jan, 1 May, 12 May, 4, 8, 11, 15,
18, 22, 25, 29 Dec. Each cipher reads as its clear letter from first word to last, at a steady 1.9 cipher groups per
clear word; words left in clear inside the cipher ("vulgo", "Vederemo", "per consequens", "Qui vult finem vult media",
"in statu quo") fall at the matching points of the clear letters. The 15 May pair is the exception: the clear letter
(about 1,780 words) is far longer than its cipher (1,441 groups), so the cipher carries only part of it; it was left
out of the key.

The clear pieces are in a secretary's hand, signed "Deboli", with the cabinet's reception note ("reçue le 17. / rep.";
on 15 Dec "reçue le 26. p. Mr du Hamel"). Whether they are clear duplicates sent by another route or the cabinet's
decipherments in fair copy is not settled. The 1782 edition (Zielińska & Danilczyk 2017, introduction p. 11-13)
shows the cabinet deciphered Deboli's letters on separate sheets, and Rolnik 2025 quotes ZP 415/420/421 as the
correspondence "after deciphering". Either way the text of 103 despatches has been in the archive since 1789-90 and is
quoted by historians (Łojek 1962, Rolnik 2025).

## Finding 2: the code, rebuilt from the pairs

A one-part syllabary (nomenclator) of about 2,200 numbered groups, Polish plaintext, dotted number groups, "Sire!" and
the French close in clear.

- Groups stand for letters, syllables, common words (8 do, 895 nie, 1353 się, 1489 tym, 1484 tych, 1681 że, 2004
  będzie, 1216 przez, 560 którzy, 1988 bo) and names and phrases (1182 posła, 1578 WKMci, 551 króla, 1307 Rossya,
  21a deputa-, 2148 currentis).
- Numbering follows the alphabet in two runs: 1 to about 1770 runs a ... z (461 ka, 466 ko, 623 lo, 692 mi, 780 n, 895
  nie, 961 on, 1262 ru, 1559 w, 1560 wa, 1678-1764 z words); 1775-1788 are nulls; numerals near 1790-1860; a second run
  from about 1870 starts again at a (1873 a, 1900 aby, 1926 ale, 1988 bo, 2004 będzie, 2059 by, 2076-2177 c, cz).
- Nulls: the whole band 1775-1788 (about 1,250 occurrences in the transcriptions; 1786 alone 649, absent on 6 Jan and
  the commonest group in December). `seed.tsv` fixes them.
- Letters written under a group (355a, 403a/b, 873c, z, e) mark variants; most fall back on the base value. A
  7-shaped first digit with a z under it (7601, 7678) is a marked form of 1601, 1678. Framed runs "4000 9933 ... 9933
  4000" with groups 2300-3409 in the 22 and 29 Dec letters are a second table, not read.
- Probably the "Cyfra polska" sent to Deboli on 8 March 1783 (ZbPop 444), not online.

`key_pass.tsv` is the key rebuilt on the eleven pairs: 630 anchored groups (aligned at least twice, consistently),
1,736 groups seen. `key_8pairs.tsv` is the eight-pair key used for the control.

## Finding 3: the three despatches with no clear text

| no. | date | k. | groups | state |
|---|---|---|---|---|
| 024 | 25 Mar 1789 | 77 | 288 | cipher addition "Ajouté au Duplicata seul, le 25. Mars"; hand-read, 95.5% (`reading/c024_1789-03-25.txt`) |
| 042 | 10 May 1789 | 138-142v | 4,393 | key gives 97.6% a value; not yet checked by hand |
| 104 | 14 Dec 1789 | 296-298v | 1,222 | mixed cipher and 39 clear Polish passages; first half checked by hand, 93.3% so far |

The 25 March addition (Postscriptum to the duplicate): Deboli will ask in every letter what Hetman Branicki is doing;
Prince Nassau-Siegen writes that Branicki is one of the most devoted to Russia; Nassau had no time for the King's
answer; Russia wants no new war. The 14 December letter: Potemkin had his courier tell the Empress he met rudeness and
had to fight for horses crossing Poland; Russian couriers given escorts in Poland "dla bezpiecznieyszego przeiazdu";
Stackelberg's reports against Deboli; Deboli asks the King for discretion and a reply he can show.

## Method and controls

- `align.py`: banded/beam DP aligning each cipher group with 0-10 letters of the clear text, cost from the
  alphabetical order of known groups, iterated anchors. `decode.py`: key-only decoding with the alphabetical bracket for
  unknown groups. `read.py`: token-level reading with hand overrides (`reading/*.fix.tsv`), counts tokens read.
- Control 1 (failed, 27 Oct): filling unknown groups from a Polish LM inside their alphabetical bracket (`fill.py`).
  Held-out 18 Dec letter, 171 hidden groups: 5-8 exact. Not used for any reading.
- Control 2 (worked, 27 Oct): key from seven pairs without 18 Dec; the 18 Dec cipher decoded blind gets a value for
  95.6% of its groups, and 91.4% of the decoded letters fall in the order of the real clear text.
- Language model: `lang` pl-1790 (pl-gutenberg respelled to 1780s conventions plus the clear despatches), added for
  this target; `lm.norm` fixed to keep Polish ł as l.

## Prior work

- AGAD inventory: "Korespondencja polityczna tajna (pismo cyfrowe) ... Listy zapisane szyfrem"; no decipherment noted
  on ZbPop 17. No interlinear decipherment on the cipher letters (pages sampled across ZbPop 17, 428, 4, 5, 416).
- Zielińska & Danilczyk, Korespondencja polityczna Stanisława Augusta: Augustyn Deboli 1781 (2015), 1782 (2017):
  printed from the cabinet's registers AKP 265/266 (Archiwum Królestwa Polskiego), not from ZbPop. Later years unedited.
- D. Rolnik 2025 (Ignatianum, Rozprawy, 2025.3103.14) and J. Łojek, Misja Debolego w Petersburgu (1962) used the
  clear series. Not on DECODE; not in this repository before.

## Remaining gaps

- c042 (10 May): hand check of the 4,393-group decode against sense, marking groups that do not read. Not blocked.
- c104 (14 Dec): hand check of k.297r-298v; 54 groups without a value. Not blocked.
- c024 (25 Mar): 13 groups open (1407, 518, 437, 108, 2140b and fragments that do not read): scattered codes.
- The 4000/9933 framed runs in c107 and c109 (a second table): their clear text is in ZbPop 417, so they can be paired
  with the clear words at those points.
- The 92 paired despatches not transcribed: their plaintext exists in ZbPop 419; only eleven were checked group by group.

## Escalation

1. Siblings: done. ZbPop 419 and 417 pair with 103 of 106 despatches; eleven pairs aligned.
2. Key sheet: ZbPop 444 (1783 Polish cipher) and 453/454 are not online.
3. Key rebuild from the pairs: done, 630 anchored groups; more pairs near May would close the remaining c042 groups.
4. Retry: LM gap-filling failed its control and was dropped.
