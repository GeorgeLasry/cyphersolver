# Re-reading log, R298 (22 Oct 2026, Claude Opus 5.5; REREAD_BRIEF, batch b01)

## Starting point

Reading audit: "decoded, not read" (clean share of the old decrypt 0.08). Three pages (IMG_R298_I2527-2529), headed
"Vienna ij. Agosto 1629 / All'Ill.mo Sig. Card. Padrone / D / 62". Mostly clear text with cipher runs for names and
delicate words; DECODE's transcription of the clear text is partly guessed.

## What was done

1. **Despatch and date**: the content is Kiewning 1897 Nr. 158 (Wien 1629 August **11**, dechiffr. 6 September; Nunz.
   di Germania 119 fol. 44-46), edition lines 23636-23690. The heading on the scan reads "ij. Agosto", i.e. 11 August;
   the record's date "18 Agosto" (DECODE "i?j?") is wrong. Kiewning gives a German regest of the first part and prints
   from "perché dar questo titolo come dovuto alli re d'Ungharia" to the end in Italian.
2. **Clear text** re-read on full-resolution crops of the three pages (DECODE's version: "*uerv*e? difficoltà",
   "servendo?", "mentì preciso/presso?", "e con altrettranta?" etc.). Points settled: "e di restarne obligatissimo",
   "rilasciarsi(?) immediatamente", "restarne provisto ex nunc", "né di servitii e meriti presso", "scrivendo",
   "acciò o gli paresse men strana la negativa, o stimasse tanto più la gratia", "possa tanto quanto vuole", "si conta
   quella delle", "et altre simili prerogative e confidenze straordinarie", "Oltre alli motivi accennati di sopra",
   "Si conceda che trattanto e fino che venga il caso pur di vacanza".
3. **Cipher runs** read from the decode and checked on the scans (`R298_corrections.tsv`): "del Re d'Ungheria" (643)
   twice, "del re di Francia" (639), "la Religione" (654), "p. Magno" (62 99 96), "e come quello", "e V. S. Ill.ma",
   "di già mandato", "havuto col", "ne trattasse meco".
4. **Printed stretch**: the figures and clear words agree with Kiewning's Italian; the print's OCR is corrected
   ("Ungharia" kept as Kiewning, "nnmero" -> numero, "rignardo" -> riguardo, "snoi" -> suoi ...). Where the page has
   "de regno di [966]" the print has "de regni d'Ungharia"; the print's plural is kept.

## Group values established here

* 654 = religione: "meriti presso la 654" (the Order of Malta, "la Religione"), "in benefitio e servitio della medesima
  654"; and R296 "contro una 654 come quella de' [440]". Next to 655 religione cattolica.
* 750 = havuto: "il discorso 750 col signor di Thun"; R297 "il marchese d'Aitona ha 750 ordine di trattenersi".
* 966 = Ungheria (print, three times); 260 = Boemia, 239 = Austria, 457 = heresia (print). 260 = Boemia also reads R296
  "li beni di [260]" as "li beni di Boemia".
* 643 = Re d'Ungheria and 639 = re di Francia are in the key and confirmed here where the decoder had split them.

## Holes and why

* `[590]` ("in più [590]"), `[620]` and `[226]` ("la corrispondenza [620] e [226]"): unidentified groups.
* "quella delle [?cappe] di Olmitz, dell'abbatia di Ber[…]": figures 90 8 32 02 22 90 (e-c-a-p-e) and "ber [995] i le";
  the privileges are not named in the regest.
* "[?rilasciarsi]" (clear word partly legible), "il gran [?mastro]" (figures 746 + 60 90 367, not resolved), "[?coadiutoria]"
  (figures "cau [906] toria"), "o [?vero]" (06 90 352), "[…] [?portar] della croce" (the words after "vacanza" at the line
  end), "la ricuperatione […] del priorato" (33 97 25 ... not read).

## Result

Read: the sentences hold; clean-sentence share 0.812 (`docs/_check_reading.py --file`), 1041 words. The coordinator should
correct the record's date to 11 August 1629 (Kiewning Nr. 158).
