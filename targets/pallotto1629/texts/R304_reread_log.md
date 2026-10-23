# Re-reading log, R304 (22 Oct 2026, Claude Opus 5.5; REREAD_BRIEF, batch b01)

## Starting point

Reading audit: "decoded, not read" (clean share of the old decrypt 0.125). Three pages (IMG_R304_I2539-2541), headed
"Vienna 25 di Agosto 1629 / All'Ill.mo Sig. Cardinal Padrone / B / 86", one clear line over the first cipher line; p. 3
has two lines of cipher ending with a line-filling stroke. No `_align.txt`.

## What was done

1. **Despatch**: the heading reads 25 August, but the first sentence refers to "la lettera di sabato circa la
   Carolina" (Saturday = 25 August 1629; that is R301, despatch "C 76") and to what Valeriano did "il giorno seguente".
   Kiewning Nr. 168 (Wien 1629 August 28, dechiffr. 13 September; Nunz. di Germania 119 fol. 66-68) has exactly this:
   "Trotz ihrer Verabredungen hat P. Valeriano am 26. August dem Kaiser ein Schreiben und die Schrift Slavata, einem
   der Deputierten, übergeben und an Barberini Copie gesandt." Register letter B (Nr. 167 = "A 79" = R302+R303). The
   "25" on the sheet is a slip of the register's copyist or a misreading; the coordinator should date R304 28 August.
   Kiewning has nothing more than these three lines: the rest is read from the figures alone.
2. **Cipher** read with the codes (dump script in the scratchpad); the clear heading line is repeated in the cipher
   (760 = non ostante). Mis-segmentations resolved by sense: "senza dirmi altro" ({Casale} 340), "Conte S[?la]vata"
   (293 + s-s-u-a-t-a, checked on the scan), "con lettere credentiali" (53 for 52, {tuttavia} 779 = -ali), "t[ermine]"
   ({Baviera} 366 + [345]), "haverei potuto provveder" ([933]), "esentioni da' nuntii", "Archiepiscopi Pragensis".
3. Not checked on the scan beyond the heading, the first line and "Slavata": the decode's figures are DECODE's.

## Holes and why

* First paragraph: "havendolo sa[…]" (270 699), "dice […] mandato copia" (56 06 29 290 96 72 35 36 20), "haver dato
  […]" (755), "alla congregatione […] scrittura" (53 06), "non si possa […] indietro […]" (43 362 90 236 ... 92 775 775),
  "[667]", "[549]" (probably "negotio" or "nuntio"), "[…] che, date dette scritture" (00 36 70), "e s[e] […] subito"
  (06 90 330 92 433 70), "l'[566] […] di costà" (00 37 90 39 00 93), "perché […] e non ricevere scacco" (67 66 67 36 09),
  "mentre lui [690] l'habbia […]" (33 09 293 53 675): the figures there do not resolve; Kiewning has no Italian.
* "l'efficacia e […] di l[ui] [650]": 32 09 36 06 09 665 5.
* "senza […]na subordinatione": [223][206] (the first-wave lesson: 223 may be 22 36 "pr").
* "e [966] in [?questi] giorni": 966 (Ungheria in extra_groups) does not fit; 774 (quello) before "giorni".
* "Sì che […] mi resta": 47 62 37 75 63.
* "per […]ma": [222][650]; "costà [?trovate]": 93 53 670 04 20 35 09; "come si pr[…]": [277] 79 05 90.
* "non [?haverei] detto": 797 not identified; "[?sa]rebbe": 302.
* "pura[mente] […] principio [326]": 767 22 36 97 32 50 22 94 326; "fonda[ta]mente […]".
* "scrivermi […]": 53 22 50 60 23 06 90 54 293 26.
* "requisito consensu […]": 53 69 43 09 20 32 33 90 29 25 09 59 737 (non di se ac dente nel come), and "[…]nti[i]
  Coloniensis" (02 906 29 25 50 400): the Latin formula is not recovered.
* "del [552]", "a questa [559]", "questa [550]": three N-range groups, probably nuntio / nuntiatura (cf. 549).
* "di […]" (06 245 69 46 90 7 534), "[?per me]", "[?né]", "[?prima]", "[…] dal so[l]o eccesso", "[679]", "[967]",
  "congregatione […] è restata": unresolved figures.
* "qu[…]": the cipher ends with 27 (qu) and a stroke filling the line; the left edge of p. 3 is cut in the scan.

## Group values (proposals; extra_groups.json not edited)

* 760 = non ostante (the clear line above the cipher; 7xx between 759 nondimeno and 763 però).
* 293 = Conte confirmed ("al Signor [293] Slavata"). 549/550/552/559: N range, nuntio / nuntiatura (contexts above).

## Result

Read in part: the frame of every paragraph is read (Valeriano's breach of the agreement, Pallotto's policy of
persuasion, the Father's privileges, the patents for Upper Germany and Bohemia, the dignity of the nunciature); the
first paragraph's middle has several holes. Clean share 0.526 (`docs/_check_reading.py --file`, 40 of 76 sentences),
from 0.125. The blocker for the holes is unresolved figures with no print to check them against; a scan check of
each break (not done for lack of time) is the next step.
