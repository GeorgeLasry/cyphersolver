# Re-reading log, R312 (22 Oct 2026, Claude Opus 5.5; REREAD_BRIEF, batch b01)

## Starting point

Reading audit: "decoded, not read" (clean share of the old decrypt 0.247). Four pages (IMG_R312_I2563-I2566), no heading;
cipher with clear-text lines; the last page ends with "Di Vienna 29 7mbre 1629", the register letter "A" and the Roman
docket "Decifr. a 18" (deciphered 18 October, as Kiewning gives). DECODE's November dating is wrong.

## What was done

1. **Which despatch**: the first words "giustificate in tutto o in parte, ma lasciandone il giuditio ..." continue
   R311, which ends "le pretensioni de gl'interess-" with the catchword "per". R311 + R312 = Kiewning 1897 Nr. 184 (Wien
   1629 September 29), edition lines 26802-26956 for this sheet.
2. **Alignment** (`reread_b01/R312_align.txt`): every cipher chunk lands on the print at 0.09-0.67 cost per letter; the
   clear-text lines (DECODE "non exou quà", "Ale*i bem' potcus c*ponden", "a'quolla piú partio*laú", "cllandu pani*enó
   copu di una *ena", "fatta da lidi fabran in Geneva", "sodisfan ... con honore", "gatnir á concordia") are the print's
   words ("non trovo qua", "Al che se bene potevo risponder", "a quello più particolare", "Mando parimente copia di una
   scrittura", "fatta dal signor di Sabran in Genova", "sodisfattione e ne resterà con honore", "pattuir a concordia",
   the last checked on the scan, p. 4).
3. **Reading** = the print, OCR corrected ("ginstificate", "Sapposto", "lopossono", "qaalche", "pradenza", "toraava",
   "rü Catt 00", "non ab" = "non so" ...); footnote markers removed.

## Figures against the print

* "Dal parlar di questi [232]": 232 = ambasciadori di Spagna (plural); supports the 6956 key value and R310's "alli
  [232]".
* "non si cava dispositione" (figures) vs print "non so cavar": print kept.
* "che [695] addictissimo a Spagnuoli": 695 = Echembergh (the bare name; 595 = principe d'Echembergh).
* "parlando con l'[462]" (twice): 462 = imperatrice — new.
* "il [503] per non tornar in [424]": 503 = marchese Spinola, 424 = Fiandra (also "accidenti di [424]") — new. In R310
  the decode has "dal [603] e Colalto" where the regest names Spinola: likely the same group misread (5/6).
* "verso il [357] di Michelburgh", "verso detto [357]": 357 = ducato — new.
* "Franzesi e [964]", "Danimarca, [964] et [574]": 964 = Venetia/Venetiani, 574 = Olandesi — new (574 from one
  alignment only).
* "con quella [647]": 647 = republica (649 is "Republica di Venetia") — new.
* "[546] del Questembergh": 546 = negotiato — new.
* "copia della [479] [233]rita da [699]": 479 = lettera? (the print: "copia della lettera scritta da Svizzeri"); 699 =
  Svizzeri. 479 also in R310 ("della [479] scrittale") where it fits "lettera". 497 is the 6956 "lettera": 479 may be the
  writer's or transcriber's transposition, or a second group.
* "de [203] li quali": 203 = consiglieri (print "de consiglieri, li quali").
* "per [394] il generale": print "perciò"; conflicts with R311, where 394 = elettori by alignment; left open.

## Holes

None: the whole sheet is carried by the print and the figures; "[per]" at the head is R311's catchword.

## Result

Read: clean-sentence share 0.902 (`docs/_check_reading.py --file`; 112 sentences, 101 clean).
