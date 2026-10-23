# Constantin Turculeț(?) to Hetman Sieniawski(?), news from Bender, 1709 (DECODE R7481, R7482)

Status: read (contemporary interlinear decipherment transcribed and checked; written up 9 Oct 2026 in sieniawski1708, own entry 14 Oct 2026)

**Split on 14 Oct 2026** from `sieniawski1708` under the one-key rule (George Lasry, 14 Oct 2026). These two letters
are in key B, the key Kaczka (2012, fn. 22) gives for Constantin Turculeț; the other letters once filed with them are
in other keys and have their own entries and pages (a different cipher in each): [`sieniawski1708`](../sieniawski1708/NOTES.md)
(Brâncoveanu/Cantacuzino, key A, including the nr 5 postscript R7483), [`r7475`](../r7475/NOTES.md),
[`chomentowski1713`](../chomentowski1713/NOTES.md) and [`schenck1706`](../schenck1706/NOTES.md). The work was done on
9 Oct 2026; the files `R7481*.txt`, `R7482*.txt` moved here from `sieniawski1708/sien/` on 14 Oct 2026.

## The documents

Archiwum Narodowe w Krakowie, Zbiór Dzieduszyckich 26/32 nr 5 pp. 1-3 and 5-6 (DECODE R7481, R7482; "Listy z
Wołoszczyzny do A. M. Sieniawskiego, pisane szyfrem z wiadomościami z Benderu o Szwedach, Czerkiesach i Turkach",
1709; status N/A, no decipherment attached). Not printed by Kaczka, who announced the Turculeț letters for a separate
edition (not found).

- **R7481** (pp. 1-3): Polish news from Bender: 700 Swedes with Colonel Gyllenkrook to Suceava, the King and Mazepa to
  go to Rákóczi ("Stąd to occurrit, siedmset Szwedów bez oręża z pułkownikiem Gilenkrukiem przeszło do Soczawy").
  Page 3 is a word-for-word fair copy of the decipherment of pp. 1-2 in another hand.
- **R7482** (pp. 5-6): a Latin letter on the same news ("Hinc tantum haec occurrunt novalia ...").

## The cipher

Comma-separated numbers, full interlinear decipherment. Key B (Kaczka fn. 22): a=37 b=51 c=71 d=100 e=1 f=10 g=9 h=13
i=4 k=88 l=62 m=30 n=14 o=91 p=2 q=11 r=48 s=12 t=65 u=8 w/y=6 x=7 z=27; 407 and 700 unglossed nulls.

## Check (9 Oct 2026, pass 2)

Token by token against gloss and key (`R7481_pass2.txt`, `R7482_pass2.txt`, readings `R74xx_reading.txt`): R7481
520 of 522 (99.6%; the two open are the nulls 407 and 700), R7482 355 of 355. Encipherment slips settled (68 for 65 in
"tam", 62 for 65 in "ivit", the dropped z of "Rakoczego"). 875 of 877 = 99.8%.

**23 Oct 2026, verification 5 (plain bar; research/reading_audit/VERIFY5_BRIEF.md)**: the letter is Polish of 1709 (not French): explicit-hole bar. R7481_reading.txt body: explicit 1.0, plain 0.222 (small Polish word list, Latin phrases, names). The reading is in modernised Polish (9 Oct 2026); not redone here. Rescored with research/reading_audit/v2_score.py (plain word-list share and explicit-hole share); both figures are in each entry's reading_review note. Keeps read.

**23 Oct 2026, v6 spelling check (research/reading_audit/v6_spelling_files.txt; REREAD_BRIEF step 3-4: no modern spelling in a reading)**: R7482_reading.txt said 'normalised spelling'. Put back into the writer's Latin from R7482.txt (figures and gloss): hæc and quæcunque (the clear &/æ sign in the groups), occurunt, expectat, Tarlo, Soczaviæ. Explicit holes 0.929 -> 0.864 (the new header paragraph is scored with the body; the letter itself has no hole). R7481_reading.txt says 'modernised Polish' and is the profile's reading for the pair; it was not in the v6 list and is still to be done.

## Remaining gaps
- none: the two open tokens are nulls by design

## Escalation
- [x] siblings: the nr 5 and nr 13 records opened; R7483 is a Brâncoveanu postscript in key A
- [x] clear-pages: R7481 p. 3 is the fair copy of the decipherment, used
- [x] known-keys: Kaczka's key B
- [x] print: Kaczka 2012 prints the key, not these letters
- [n/a] key-rebuild: the key is printed and the decipherment complete
- [n/a] retry: nothing open
