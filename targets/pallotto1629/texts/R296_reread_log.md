# Re-reading log, R296 (22 Oct 2026, Claude Opus 5.5; REREAD_BRIEF, batch b01)

## Starting point

Reading audit: "decoded, not read" (clean share of the old decrypt 0.125). Three pages (IMG_R296_I2520-2522), headed
"Vienna 18 Agosto 1629 / All'Ill.mo Card. Padrone / C / 57" (third page numbered 58). About half the text is in clear,
which DECODE transcribed mostly as asterisks; no `_align.txt` exists for this record.

## What was done

1. **Despatch found** by date and content: Kiewning 1897 Nr. 162 (Wien 1629 August 18, dechiffr. 6 September; Nunz. di
   Germania 119 fol. 41-48), edition lines 24202-24230 and 24256-24266. Kiewning prints paragraph 1 ("Quel che V. S.
   Ill.ma si è compiaciuta accennarmi circa la persona del padre Magno ... li sensi di N. S.re e di V. S. Ill.ma") and the
   last paragraph ("Lasciai di scriver ... fatto il contrario") in Italian; the rest is a four-line regest.
2. **Clear text** re-read on full-resolution crops of all three pages (about 60 crops). The page's own clear words were
   kept where they differ from the print in order ("Lasciai di scriver con le passate a V. S. Ill.ma").
3. **Cipher runs** read group by group with a dump of the decode (`reread_b01_decode.decode_doc`) and checked on the
   scan where the decode broke (`R296_corrections.tsv`, 24 places). Main points: "Magno" is spelled 62 99 96 (the
   decoder's "[629]{V.S. Ill.ma}" every time); "Valeriano" 06 72 90 46 50 20 96; "lor zelo gli detta"; "di questo
   negotio"; "per hora"; "molto"; "con le quali"; "tediarla"; "pensasse V. S. Ill.ma"; "per mia volontà"; the
   interlinear insertion "ha veduto"; "e servirlo"; "di vedersi"; "ministri gravi".
4. The regest checks the sense of paragraphs 3-5: Bohemian church property and bishoprics (the "primo de li due [957]",
   "farne tre"), P. Valeriano's paper on the Carolina given without the nuncio's participation, "without an order of the
   Pope and the Congregation", "the ministers wonder at it" ("ad alcuni ministri gravi, che me n'hanno parlato con
   maraviglia").

## Holes and why

* `[275]` (twice, "al signor [275]"): a person; from the two contexts (the salt-revenue commission with P. Valeriano and
  the nuncio; "per quel che tocca al signor [275] il tutto è aggiustato") almost certainly Cardinal Harrach, the
  archbishop of Prague, but the group is not the plain 267 cardinale that the same page uses in "col signor cardinale".
  Left as a group.
* `[957]` "il primo de li due [957]": a plural noun in the S-V part of the nomenclator; the regest's "Errichtung von
  Bistümern" suggests "vescovati", not established.
* 734 = ancorché, established while reading R297 ("si accomodi, ancorché con poco avvantaggio"; "ancorché io
  celebrando pontificalmente", Kiewning "obwol er celebrierte"), fits here with the subjunctive "mostri".
* `[593]` ("più [593] di quel che conviene"): a group without a value; contexts in other records
  (`reread_b01_ctx.py`) do not settle it.
* 260 = Boemia ("li beni di 260"), established on R298 where Kiewning prints "Boemia, Austria e Moravia" for 260 239 534.
* `[?S. S. Ill.ma]` for 677 (twice): extra_groups.json gives 677 = Sua Santità, but here the subject "s'è chiarita ... ha
  veduto e toccato con mani quello che passa, et è restato sincerato affatto" is someone in Vienna (the cardinal), and the
  nuncio serves him "solennemente per mia volontà". Proposed: 677 = S. S. Ill.ma (Sua Signoria Illustrissima), to be
  checked against the R2xx contexts where Kiewning printed "N. S.re".
* `ordinatione` for 567 ("non [567] di N. S.re o della sacra congregatione"): the sense needs "order/instruction"; the
  6956 key has 567 = ordinatione, extra_groups.json changed it to occasione. Both readings need checking across the batch.
* 654 = religione, established on R298 ("meriti presso la 654", "servitio della medesima 654": the Order of Malta).
  `[?Gesuiti]` (440) stays a conjecture: "contro una religione come quella de [440]"; the Carolina quarrel set
  Valeriano against the Jesuits, but the group has no other context.
* `[?accertai]`, `[?accordato]` (clear, partly legible), `[?ministri]` (509 if DECODE's 4 is a 5), `[?supponendo]`
  (ink blot), `[?tener]`, `[?sillogistici]` (the figures give "llogistici"), `[?dell']`, `[?d'approvarla]` (blot),
  `[?impuntare]` (figures "d'imp-ntare"), `[?haver]`: partly carried.
* `[…]`: the clear word after "farne tre, e"; "perché […] nella sua volontà" (75 9 8 under a blot); "la risposta di
  […]" (69 1 21 5); "in questo medesimo […]" (clear word not read); "che non è punto […]" (54 at the line end);
  "[…] e servirlo" (69 25 06 23 62 75 not read); "servi[…], […] quando" (clear word at the line break); "si poteva […]"
  (74 70 8 69 1 62 32 07); "receduto, […] che" (a struck group and "a co-to"); "non so […] approvare" (clear word not
  read).

## Result

Read in part, the sentences mostly hold: clean-sentence share 0.779 (`docs/_check_reading.py --file`), 1170 words. The
holes above are single words or groups; no stretch longer than about eight words is unread. What blocks the rest:
unidentified nomenclator groups (275, 957, 593, 440) with no print to align them, and three ink blots.
