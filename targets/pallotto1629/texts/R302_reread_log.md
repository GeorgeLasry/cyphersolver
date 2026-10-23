# Re-reading log, R302 (22 Oct 2026, Claude Opus 5.5; REREAD_BRIEF, batch b01)

## Starting point

Reading audit: "decoded, not read" (clean share of the old decrypt 0.115). Two pages (IMG_R302_I2535, I2536), headed
"Vienna 28 Agosto 1629 / All'Ill.mo Sig. Card. Padrone / A / 79", clear "È partito Bruneo" over the first line; p. 2
ends with seven lines mixing clear and cipher. DECODE gives the year as 1627 and no day.

## What was done

1. **Despatch**: Kiewning Nr. 167 (OCR "107."; Wien 1629 August 28, dechiffr. 13 September; Nunz. di Germania 119 fol.
   61-66; edition lines 24602-24760). The automatic alignment found the one Italian passage (runs 4.10-4.11, the
   intercepted letter to Monterey, 0.21 and 0.49 per letter); everything else in Kiewning is German regest. The regest
   runs on past this sheet: its last third (Wallenstein's haste, Leopold Wilhelm's indult, the closed letter, the
   visitor for Aquileia, Savelli) is R303, which has no heading and starts where this sheet stops.
2. **Cipher** read run by run with the codes (dump script in the scratchpad). Mis-segmentations of spelled-out words
   resolved by sense: "Bolduch" (bo{Roma}emi[255] in the decode), "recuperar" ({Duca di Mantova} 360 = 36 0), "banda"
   ({Sua Altezza} 675), "mancamento", "giustitia" (giul[250]tia), "vederà" ({Marchese} 502), "piego"
   (p{ministri}go), "figlio" ([450]glio).
3. **Clear words** of p. 2 re-read on the scan (DECODE's transcription of them was mostly question marks):
   `R302_corrections.tsv`.
4. Kiewning's regest checked each paragraph; it confirms the readings "capitolationi" (Capitulation Frankreichs mit
   England), "Regina" (die Königin von Ungarn zur Hochzeit), "tregua" (einen langen Waffenstillstand), "colonnelli"
   (mit einigen Obersten), "Halberstadt", and the 21 July letter about Conti.

## Holes and why

* "haverà quello [?di] diminuir a l[u]i": the sense of the opening sentence stays unclear (the figures are clear).
* "[227]a[693] il corriero": two groups not identified (a verb: "brought").
* "le [?capitolationi] del [922] col [?Re d'Inghilterra]": 329 (C range) by the regest; 922 is "stato" in the key,
  which does not fit (France expected); 645 by the regest and R310 "la pace con [645]".
* "recuperatione del […] e voce elettor[…]": figures 62 65 90 06 70 32 90 / 90 74 93 36 729 05 00; the regest has
  "Wiedergewinnung des Palatinats und der Kurfürstenstimme".
* "si mostrò più tosto freddo che altri[menti]; […]": 75 54 (lo dal) not read.
* "a trat[tar] […] che tra tanto": 25 202 56 73 47 35 567 not read.
* "vi [652] poca speranza": 652 not identified (a verb).
* "al recuperar […] tutto ciò": figures 32 07 92 00 (costa).
* "il lor p[…]": 22 570 06 29 00.
* The Conti paragraph: groups 369, 250, 946, 624, 990, 652, 225, 237, 650, 736, 359, 555, 405, 537, 640, 623 not
  identified; several stretches ("ot-946 lettera che e-624-io di ma-267-r il piego", "a le di 990 ma dagnolo suo",
  "pro-770-990-r titolo", "con prou-506-perane laegrase e con s-522-a-922-die", "non f 640 ar a maegliofuse 623
  marito") do not resolve. Kiewning has only one line of regest for it, so there is no check. The paragraph reads as
  sentences at its frame (the two reasons, the decision to send the packet by a confidential person, the Hamburg
  illness, the paymaster on 30 July), the middle has holes.

## Group values (proposals; extra_groups.json not edited)

* 329 = capitolationi (regest "Capitulation"); 636 = Regina (R range between 635 Re and 637 regno; regest "die
  Königin von Ungarn"); 947 = tregua (T range; regest "einen langen Waffenstillstand"); 335 = colonnelli (C range;
  regest "mit einigen Obersten"); 645 = [?Re d'Inghilterra] (regest; R310 "la pace con [645]"); 424 = Fiandra (as in
  R300).

## Result

Read in part: the Bruneau, Spanish-aims, Aldringen and Monterey paragraphs read as sentences; the Conti paragraph is
read at its frame with holes in the middle. Clean share 0.64 (`docs/_check_reading.py --file`, 55 of 86 sentences),
from 0.115.
