# Re-reading log, R297 (22 Oct 2026, Claude Opus 5.5; REREAD_BRIEF, batch b01)

## Starting point

Reading audit: "decoded, not read" (clean share of the old decrypt 0.239). Four pages of cipher (IMG_R297_I2523-2526),
headed "Di Vienna 25 di Agosto 1629 / All'Ill.mo Sig. Card. Padrone / A / 67", page 3 numbered 68. The only clear words
are "L'ultime lettere dell'Imperio" above the first groups.

## What was done

1. **Despatch**: Kiewning 1897 Nr. 164 (Wien 1629 August 25, dechiffr. 13 September; Nunz. di Germania 119 fol. 53-57),
   edition lines 24393-24525. Mostly German regest; Italian only for "col pretesto di procurar la restitutione del
   Palatino e la conservatione della libertà di Germania e dell'Imperio" (run 5.12, 0.60) and "e se bene si trovano
   frustrati ... non lasciano di sollecitar le loro genti verso Italia" (runs 5.16-5.20, 0.14-0.96). Those follow the
   print; the rest of the reading is from the figures.
2. **Read through the decode** run by run with the codes (`reread_b01_show.py`) and a locator that maps a decoded
   stretch onto its line on the scan (line positions from the page images, digit offsets from the DECODE
   transcription). Breaks checked on the scans: "trattenendo", "facendo", "fusse per", "l'effettuar", "maggior",
   "e che […] sia", "consumar e […]", "il veder […] risoluto", "la [?lega]", "gravissimi […]", "et io non […] contento",
   "esser si [?dato] ordine". Many decoder breaks are only mis-segmentations of spelled-out words (Aitona, Niuers,
   passaggio, Magdeburgh, Gratz, finestra, giorno), corrected in `R297_corrections.tsv`.
3. The regest checks each paragraph: Wallenstein at Halberstadt; Collalto's commissary to Milan; Aytona; Gabor; the
   three French gentlemen and Strasbourg; Nevers, the Venetians, the French and the Huguenots; Wallenstein's order to
   leave Magdeburg; Aytona's secretary to Spain; Aytona to stay "bis auch der englische Handel geregelt sei"; Flanders and
   Count Henry in the Veluwe; Herzogenbusch; the Uskok captain and the chamber of Graz; the plenipotentiary; the French
   nuncio's despatches to be put to Savelli; the legate; the Duke of Neuburg's precedence and the Madonna day in the
   Jesuit church.

## Group values (proposals; extra_groups.json not edited)

* 406 = esercito: six contexts in this record ("il grosso del 406", "con gran 406", "potentissimo 406", "406 formato
  dell'imperatore"), R289 "numeroso 406".
* 734 = ancorché: "si accomodi, 734 con poco avvantaggio" (Kiewning "wenn auch mit einigem Nachteil"); "734 io celebrando
  pontificalmente ... non restassi pregiudicato" (Kiewning "obwol er celebrierte"); R296 "734 il signor cardinale mostri
  inclinar". Alphabetically between 733 ancora and 735 bene.
* 750 = havuto: "il marchese d'Aitona ha 750 ordine"; R298 "il discorso 750 col signor di Thun" (7xx after 747
  havere, 749 havendo).
* 764 = poco: "con 764 avvantaggio" (7xx between 763 però and 765 poiché).
* 507 = Milano? (Kiewning "einen Commissar nach Mailand"; one context). 424 = Fiandra? ("delle cose di 424", Kiewning
  "Aus Flandern"). 574 = Olandesi? ("contro 574"). 427 = fortificationi? ("le inespugnabili 427 delli assedianti",
  Kiewning "uneinnehmbaren Befestigungen"). 472 = Inghilterra? ("questo negotio d' 472", Kiewning "der englische
  Handel"). 964 = Venetiani? (four contexts: "non ardissero dichiararsi", "contro 964 et altri", "per infestar 964").
  695 = segretario? ("il 695 del marchese d'Aitona", Kiewning "der Sekretär Aytonas"). 596 = principe Savelli? ("dovendosi
  dir al 596 per comunicarlo poi qua a S. M.tà", Kiewning "da sie offiziell Savelli vorgetragen werden"; next to 595
  principe d'Echembergh). 553 = Nuntio? ("Monsignore 553", Kiewning "des französischen Nuntius"). 220 / 722 =
  arciduchi / arciduchesse? ("luogo sopra l' 220 e 722", Kiewning "Vorrang vor den Erzherzogen und Erzherzoginnen").
  These are marked `[?word]` in the reading; one context each, so not established.

## Holes and why

* Unidentified groups with no print: 446 ("da quel 446"), 665 973 (Kiewning: "die auch durch die Hugenotten beschäftigt
  sind", perhaps Rohan and the Huguenots), 939 207, 963, 652, 255, 336 (twice, "un tal 336 Francesco ... 336 principale
  d'Uscochi", capitano/capo), 929, 233, 390, 320, 349 920, 726, 590.
* Not resolved on the scan: "consumar e […]"; "che […] sia per sostituir" (the right margin of p. 1 is cut on the scan,
  DECODE's comment says so too); "il veder […] risoluto" (a struck figure); "ne' stati di […] e Monferrato" (40 09);
  "gravissimi […]" (a blot); "et io non […] contento" (752 63 33 70 752); "Bo[…] [255]" (Herzogenbusch, spelled
  "bo 66 3 ..."); "S[…]inich" (the Uskok's name); "allo [233] […] con altre [390]"; "servir[…]" (406 in "a servi 406
  alla caccia" cannot be esercito).
* `[?word]` that rest partly on the regest: Milano, Venetiani, Fiandra, Olandesi, Inghilterra, segretario, Nuntio,
  principe Savelli, arciduchi/arciduchesse, Gesuiti (the church of "pp. ?4i"), fortificationi, tornar, non.

## Result

Read in part, the sentences mostly hold: clean-sentence share 0.798 (`docs/_check_reading.py --file`), 1572 words.
Blockers: unidentified nomenclator groups (above), with no Italian print to align them, and the cut right margin of p. 1.
The sheet stops at "pregiudica-": the continuation is on another sheet (see R299).
