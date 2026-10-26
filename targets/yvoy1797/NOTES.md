# d'Yvoy's cipher despatches, London 1797-99 (KHA A35-1450-1452)

Status: in progress

Koninklijk Huisarchief, The Hague, A35 Willem I (as Hereditary Prince), inv. A35-1448-1458: letters of Maximiliaan
Louis van Hangest baron d'Yvoy van Mijdrecht, Orangist emigre and confidant of the Hereditary Prince, 1794-1808.
Scanned: A35-1450 (1797, 317 scans), -1451 (1798, 175), -1452 (Jan-Jul 1799, 220), -1453 (Aug-Dec 1799, 317). Found
in the KHA sweep (research/nationaal_archief, lead K9; flags in research/nationaal_archief/k89/flags_a35.tsv, 28
pages in A35-1450-1452, judged from thumbnails; more cipher pages are likely among the unflagged ones).

## The code

A Dutch numerical code, groups of 1-4 digits up to about 1,400, among clear French or Dutch, with a decipherment
written above the numbers on many pages. Checked on 147529 (letter to d'Yvoy, July 1799, "pag. 1"): 1341 = Zeeland,
"101 1216 723" = "in Hamptoncourt men", "1137 95 1341 582" = "Holland en Zeeland".

## Print

Colenbrander, *Gedenkstukken* (Huygens retroboeken full text, downloaded to `gs3/`, git-ignored):
- GS II (1795-98) prints d'Yvoy to the Erfprins of 1795-96 (nos. 697, 717, 751, 754, 760; one note "De eerste
  alinea uit het cijfer"); none of 1797-98 in its index.
- GS III (1798-1801) prints: 676 Erfprins to d'Yvoy 16 Mar 1799; d'Yvoy to the Erfprins 16 Apr (681), 27 Apr (686),
  11 May (691), 14 Aug (742), 19 Aug (750), 18 Sept (781) 1799, 22-23 Oct 1801 (889-890); to Hendrik Fagel 26 June
  (705) and 27 Oct 1799 (811); to Henry Dundas 19 Aug 1799 (751). Cribs and contamination for the 1799 letters.

## Transcription and tables (25-26 Oct)

- `runs_a.txt`, `runs_b.txt`: the 28 pages flagged in the sweep (145 runs, about 1,500 numbers); every run glossed.
- `more_pages.tsv`: a second pass over all 1,029 scans of A35-1450-1453 found 196 pages with code numbers (93 marked
  unglossed at thumbnail size; outgoing letters to d'Yvoy are scanned three times, as mounted original, faint
  tissue copy and photocopy). `runs_c.txt`, `runs_d.txt`: the 79 unglossed non-photocopy pages (202 runs, about
  1,700 numbers); many turned out glossed after all.
- **Two codes.** L = London 1797-98 (d'Yvoy's despatches and the Prince's letters to him: 46 de, 85 en, 106 dat,
  1073/1113 van, 683 men, 1055 te, 1081 zal, 1107 Engeland, 1117 Pruissen, 1137 Vrankryk, 1167 Rusland, 661
  Keizer, 631 Koning, 1056 Berlyn, 1124 Pitt, 1156 Hamptoncourt, 1226 Parys, 1283 Vreede, 1488 Malmesbury);
  E = 1799 (Emmerich, Munster, letters to d'Yvoy: 95 en, 161 in, 723 men, 743 met, 1038 Erfprins, 1137 Holland,
  1157 Engeland, 1341 582 Zeeland, 1366 Nymegen, 1085 1071 Tuyll, 1236 's Bosch). The same number means different
  things in the two (1137 Vrankryk / Holland). A Dutch word code with whole words and names plus syllable numbers
  for spelling (15 505 512 Tollius, 528 17 1015 99 tractaat).
- `tables.py` builds `table_L.tsv` (102 numbers) and `table_E.tsv` (50) by vote from the AL lines. Leave-one-page-
  out: L 79% of decoded words found in the run's own gloss vs 26% in another's (65 pages, 1,174 words); E 81% vs 27%.

## The unglossed runs (26 Oct)

`decode.py` -> `reading_unglossed.txt`. 49 runs have no decipherment (282 numbers, 47% decoded by the tables).
Almost all are one stock phrase in d'Yvoy's despatches, "hier [229] is wat" / "hier [229] is [43 609]" / "op ...
drie is wat", glossed on 147205, 147351, 147226 and 147412 as "hier achter is (wat) geschreven" (229 = achter;
43 609 or 43 669 = geschreven): a pointer to text written on the back of the leaf in sympathetic ink. Read from the
glossed instances. The one substantial unglossed text is 147107, a mirror-image tissue copy of the Prince's letter
No. 22 to d'Yvoy (Schonhausen 22 Sept 1797): about 40% of its numbers decode ("... Tollius ... te Hamptcourt ...");
not read.

## Remaining gaps

- 147107 (No. 22, 22 Sept 1797, mirror-image copy): about 40% of numbers decoded; blocker: open-codes and faint copy
  (no better copy among the scans; the mounted original was not found).
- Syllable numbers of both codes are thin (102 and 50 numbers in the tables); the 1799 letters printed in
  Colenbrander GS III (681, 686, 691, 742, 750, 781) are not yet aligned as cribs.

## Escalation

- [x] siblings: all 196 code pages of A35-1450-1453 listed; glossed runs used for the tables
- [x] retry: unglossed runs decoded; the stock pointer phrase read from its glossed instances
- [ ] print: align the GS III 1799 letters with their cipher pages to extend table E
- [ ] clear-pages: look for the mounted original of No. 22 (A35-1450 around 147105-147107)

## Log

- 25 Oct 2026: target opened; GS II/III searched; two agents transcribing the 28 flagged pages (`BRIEF.md`,
  `runs_a.txt`, `runs_b.txt`).
- 26 Oct 2026: second pass (196 pages); 79 unglossed pages transcribed; two codes, tables built and tested
  leave-one-page-out; unglossed runs found to be the sympathetic-ink pointer phrase; 147107 not read.
