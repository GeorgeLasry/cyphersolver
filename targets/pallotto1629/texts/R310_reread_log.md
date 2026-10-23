# Re-reading log, R310 (22 Oct 2026, Claude Opus 5.5; REREAD_BRIEF, batch b01)

## Starting point

Reading audit: "decoded, not read" (clean share of the old decrypt 0.134). Four pages, all cipher (IMG_R310_I2555-I2558),
headed "Di Vienna 22 7mbre 1629", register "A", p. 109 (DECODE's November dating is wrong: 7mbre = September). Not a
continuation of R309; R311 begins with its own heading.

## What was done

1. **Despatch**: Kiewning 1897 Nr. 182 (Wien 1629 September 22, dechiffr. 11 Oct., Nunz. di Germania 119 fol. 99-107;
   edition lines 26273-26397, plus the two enclosures Fortiguerra-Pallotto 7 Sept. and Pallotto-Fortiguerra 19 Sept.,
   which are not on this sheet).
2. **Alignment** (`reread_b01/R310_align.txt`): chunks 4.8-4.11 (0.41-0.53 cost/letter) = "alla quale impresa ...
   astrologia"; 4.24-4.38 (0.24-0.68) = "che hora si può far la pace ... Guastalla" and "Parlai fin della settimana ...
   a loro interessi". These are the print, OCR corrected ("lnogo", "nccessario", "tencndo", "phischläfern" etc.).
   Figures against print: "del Sueco" (print "dello Sueco"), "numera sopra mille anni" (print has no "sopra"; figures
   kept), "S. M.tà poi non solo non inclina" (figures s-[5]-lo non; print "S. poi non inclina"; figures kept),
   "da brugo ..." where the print has "Broneo" (Bruneau), the name kept bracketed.
3. **The rest** read from the codes (dumped per token) with spot checks on the scans. Settled on the scan or from the
   digits: "duca di Neoburgh" (95 07 24 06 36 99 55; the regest has "mit Neuburg nicht an dritten Orten"), "in luoghi
   terzi", "lasciato di andarvi", "d'Aitona" (spelled out), "risposta", "trovino" (425 here is 4 + 25 = t), "terzi",
   "ingerirsi"-type splits, "Alberstat" (the decoder's {Duca di Nivers} in "Albe[369]a[235]" is 36 9.. = r s..).
4. Kiewning's regest checked for each unprinted paragraph: Fortiguerra's letter and the deposit; Wallenstein not going
   to Italy; Swedes and Mecklenburg; peace talk, Spanish courier, privy councillors away; Neuburg precedence; France to be
   lulled; Conti no answer; St Ursula commission. All agree with the reading.

## Holes and why

* "[404: ?espediente]" (presi per 404 rispondergli): E range of the nomenclator; also R292, R300, R303, R313 contexts
  ("parerà 404 per un interesse", "per 404 a loro interessi"), which fit "espediente"/"espediente". Proposed.
* "si [649]ar che non passerà": 649 is the uncertain "Republica di Venetia" group; here a verb is needed. Unread.
* "[347]" with Polonia: the regest has "Waffenstillstand" (truce); 347 sits in the C-E range (perhaps "concordia" or
  "conventione"); left as the number.
* "dello stato [di] Michelburgh": figures "stato e mi che l burgh"; the e may be part of the name.
* "senza specificar […]": 225 l 407 777 il mo gli: garbled.
* "un c[orriero]": only the c is written (or a group lost); the regest has "ein Courier aus Spanien".
* "[203: i consiglieri]": "essendo stati fuori 77 203 appresso S. M.tà"; regest: "da die geheimen Räte abwesend bei dem
  Kaiser sind"; 203 = consiglieri is established by R312 ("de 203 li quali" against Kiewning's printed "de consiglieri,
  li quali"); the stray 77 before it is unread.
* "funtione di […] dell'anello": figures a-di-ar-al-o-r-e-r: not understood.
* "[?invitato]": "invi" + 293 (Conte), a misparse.
* "[?passata]", "procurai [?non] pregiudicarmi" (figures 52 con … 92 st), "così sol[…] [?nelle]": garbled stretch at p. 2
  ll. 8-10, not resolved on the scan.
* "[232: ambasciatori di Spagna]": 6956 key "Ambassatore di Spagna(?)"; confirmed in R312 ("Dal parlar di questi 232"
  against the print's "ambasciadori di Spagna").
* "[?detto]" (figures p-et-to), "vo[ler]" (vo + 736), "se [900] aggiustano": slips.
* "ve[…] l'inimico", "[…]mente" (va com 667): unread.
* "[603: ?Spinola]": regest "Von Spinola und Collalto hört man nichts"; in R312 the marchese Spinola is 503 (print
  alignment), so 603 here is probably 503 misread (5/6) — not checked on the scan.
* "li suoi […] faranno [266]i sogni": regest "so ist für seine Verbündeten zu fürchten"; 266 unread (C range: "cattivi"?).
* "Dal signor D. [955]": regest "Von Conti hat er auf sein Schreiben noch keine Antwort" (Torquato Conti). 955 elsewhere
  is mostly the tail "…gh" of a spelled name (here in "Neoburgh"), so the name may be lost in a misreading.
* "[479]" (the thing written to him: lettera is 497; a transposition?), "di ce[200]", "signor [353] suo padre",
  "[329]ereo", "[…]se", "[?trovasse]", "[649] era": the courier sentence is only partly carried.
* Last paragraph (St Ursula): read in its frame, with several holes: "[…] uffitii", "supplico […] condonare al[l'] […]
  mia divotione", "di [659]sti[445]carle", "pratic[346]i", "ad […] inferiori", "di una se[…]ma", "il […] poco bene
  affetto". It is not printed; the regest only says he will carry out the St Ursula commission.

## Group values

* 460 Imperatore, 625 Palatino, 626 Palatinato, 239 Austria, 366 Baviera confirmed by the print.
* Not groups here: 950/955 (Neoburgh), 362 (terzi), 425 (t…), 503, 553 (altro), 620 (mando), 207 in "co-207-pia"
  (copia: the 207 here is a misparse, so it does not argue against 207 = consigliero), 365 in "risposta".
* 203 = consiglieri (R312 print alignment).
* Proposed: 404 = espediente; 603 = Spinola (regest only).

## Result

Read in part, most sentences hold: clean-sentence share 0.726 (`docs/_check_reading.py --file`; 113 sentences, 82 clean,
hole rate 0.10). The open places are the slips and unidentified groups listed above; the last paragraph is the weakest.
What would close them: more scan work on p. 2 ll. 3-10 and p. 4 ll. 1-12, and the Roman decipherment (Nunz. di Germania
119 fol. 99-107), which Kiewning used but did not print for these passages.
