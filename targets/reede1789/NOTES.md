# Van Reede's cipher to Princess Wilhelmina, Berlin 1789-95 (KHA A32-545-548)

Status: in progress

Koninklijk Huisarchief, The Hague, A32 Wilhelmina van Pruisen, inv. A32-542-549: letters of Arend Willem baron van
Reede, States envoy in Berlin, to Princess Wilhelmina, 1786-1814. Found in the KHA sweep (research/nationaal_archief,
lead K8, survey of 25 Oct 2026; flags in research/nationaal_archief/k89/flags_a32.tsv).

## Two systems in the file

- **1789-92 letters to Wilhelmina:** cipher runs of 1-3 digit groups ended by a dot, with marks on single digits
  (single, double, triple and wavy underlines, primes, '+'), and a contemporary decipherment written above the runs
  on about 37 pages (`interlined.txt`). Examples (scan 122, id 170613, 14 Apr 1789): 313 = Bi(schoffswerder);
  "225 140 297 735 775 305 249 178" = "la mort de la Ingenheim"; "353 258" = "deja gagne".
- **Solid pages of plain 4-digit groups (up to about 2000)** with no decipherment: 171282 (17 Jan 1792), 171359 (30
  Jun 1792), 171376, 171405 (2 Nov 1792), 179084 (Nov 1792), A32-548 171596 (Jan 1793), 171534 (Apr 1795), 171548
  (12 May 1795), 171568-69 (Jun 1795). Not the 1782 Grand Chiffre: decoding 171282's first 23 groups with DECODE key
  R1024 (vanreede1787) gives nonsense ("Conseil d'Etat extremement jamais Audience particuliere soit im our ...").

## Link to vanreede1787 R1893

R1893 (24 Mar 1793, Van Reede to the Secret Committee, Dutch, DECODE) is three-digit groups with marks under and on
single digits, the same look as the 1789-92 letters to Wilhelmina (its DECODE image `rot_IMG_R1893_I9360_P1.png` in
targets/vanreede1787/decode is stored upside down). The plan: rebuild the marked 3-digit code from the glossed runs,
then try it on R1893 and on the solid pages.

## The 1789-92 table (25 Oct)

Two agents transcribed the 37 glossed pages (`pairs_a.txt` 162 runs, `pairs_b.txt` 108 runs, about 1,900 groups;
CT with every mark and its digit, PT the decipherment, AL a first alignment). `table.py` votes them into
`table.tsv`: 386 numbers (7-856), 242 with at least 60% agreement; 492 marked forms.

- A mixed nomenclator: syllables in the low hundreds and the 500s (24 au, 26 pe, 97 trou, 130 co, 224 ma, 583 bi,
  593 te, 595 s ...), words and names in the 300s-490s (320 la guerre, 404 conduite, 415 tout, 420 faire, 433 plus,
  435 rien, 442 Republique, 463 Roi, 465 le Pr. Henri, 466 Hertzberg, 468/469 ministre, 470 le Prince, 472 la
  Hollande, 475' Greffier, 476 Spiegel, 483 Reede, 484 France, 489 l'Empereur, 492 Prusse, 493/495 l'Angleterre),
  function words in the 700s-800s (732/735 de, 777 le, 779/780 les, 789/790 que, 793/794 qui, 809 c', 814 est).
- Marks change the value: an underline under a given digit makes a plural or variant (207 de / 207 underlined on
  digit 3 des; 199 le / les; 420 faire / fait / faisant); a prime switches between two entries (475 d'Orange /
  475' Greffier; 225' la / 225 a syllable). An overlined 3 before name groups is unglossed: a name marker or null.
- The lemon-juice postscript of 9 Oct 1790 (scan 302) is glossed "en citron le reste non valeur".

## Tests on R1893 and the solid pages (25 Oct)

- **R1893** (vanreede1787; DECODE image turned the right way: headed "Wel Edele Gestrenge Heer", 24 Mar 1793,
  Dutch). Its marks are bars, tildes and v's ABOVE digits, where the 1789-92 letters use underlines. Decoded with
  `table.tsv` on bare numbers: 281 of 696 groups get a value (40%, about the table's share of the range), giving
  French words and syllables with no sense in a Dutch letter. Not this code.
- **Solid 4-digit pages 1792-95** (17 Jan 1792 page, first 23 groups): every fixed offset -2000..2000 onto the
  table; best 9 of 23 groups, nonsense. A third code, no key in the file.

## Remaining gaps

- R1893: not read; blocker: no-key-material (a different marked code; not the 1789-92 table).
- Solid 4-digit pages of 1792-95 (171282, 171359, 171376, 171405, 179084, 171596, 171534, 171548, 171568-69): not
  read; blocker: no-key-material.
- The 1789-92 table: about 140 numbers below 60% agreement; the alignments are first passes.

## Escalation

- [x] siblings: the glossed 1789-92 letters used to rebuild the table
- [x] known-keys: R1024 Grand Chiffre and the 1789-92 table (with offsets) tried on the solid pages; table on R1893
- [ ] retry: use the table to read the unglossed 1789-92 number passages ("numbers in text" in flags_a32.tsv)
- [ ] print: Colenbrander Gedenkstukken I-II for Van Reede's 1792-95 despatches (would give cribs for the solid pages)

## Log

- 25 Oct 2026: target opened; 37 glossed pages transcribed; table voted (table.tsv); R1893 and the solid 1792-95
  pages tested and not read.
