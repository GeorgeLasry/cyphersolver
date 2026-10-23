# Re-reading log, R292 (22 Oct 2026, Claude Opus 5.5; REREAD_BRIEF, batch b01)

## Starting point

Reading audit: "decoded, not read", clean share of the old decrypt 0.115. Four register pages, cipher with many clear
words; header "Di Vienna 18 di Agosto 1629", "All'Ill.mo Sig. Card. Barberini", "A. 43".

## What was done

1. **Existing text?** Kiewning 1897 **Nr. 160** (Wien 1629 Aug. 18, dechiffr. 6 Sept., Nunz. di Germania 119 fol.
   29-37), edition lines 23733-24170. **R292, R293 and R294 are one despatch** (R293 starts with the sentence R292 breaks
   off in, "Non hebbi tempo di parlarne con S. M.tà ..."; R294 ends with the Rarrach/baldachin passage that closes
   Nr. 160 on p. 299). The coordinator's note that the records are despatches of 11-18 Aug. is right for R291 (Nr. 157,
   11 Aug., "B.") and R292-R294 (all Nr. 160, 18 Aug., "A. 43"); Nr. 161/162 are not on these records.
2. **Print stretches**: `reread_b01/R292_align.txt` puts runs 9.0-9.6 and 23-89 on the print at 0.04-0.6 per letter.
   These are given in the print's wording with the OCR corrected (conclndersi, qnesto b, frk lodette = fra le dette,
   dis&rm&to, rt de Romani = re de Romani, deü f = dell', bnone, invemo, snssegnenti, m k anche = ma anche ...).
   Where the figures differ from the print: "ma ancora la parte" (733 = ancora; print "anche"), "con altre susseguenti"
   (print "altri"), "mandar suo {commissario}" (299; print "ambasciadore"), "dispositione di N. S." (577; print "S.
   S.tà"); the print's wording is kept, the figures are noted here.
3. **Regest stretches** read from the figures (token dump with codes) and checked on the scan where they broke:
   * opening paragraph and the Lorraine/Saarwerden paragraph (Kiewning: "Nachdem dem Herzog von Lothringen ... Saarwerden
     ... 500 französische Reiter");
   * "venuto di [525] tre giorni sono con lettere delli ventisei del passato, che il secretario, tornato d'Inghilterra" —
     scan: 497 (lettera) not 477, "secretario | tornato d' 472": `R292_corrections.tsv`;
   * "È uscito ancor dall'ambasciatore di Savoia che li [973] delle quattro città di Linguadoca siano di nuovo tornati a
     tumultuare ... non havendosene riscontro d'altrove, solo di qualche cosa di Montalbano. Alcuni pigliano occasione di
     credere ..." — the clear words read on the scan (DECODE had "fino? di mano? tornati", "eleuni? piglia?");
   * a sentence Kiewning omits: "Hora so che la detta [593] ha scritto di proprio pugno al Palatino di [966], che gli
     annuntiava la gran gratia ... da Dio della sua conversione";
   * the last two paragraphs (Kiewning: "Er unterlässt nicht darauf hinzuweisen ... die Befestigungen der Grenzen
     angezeigt ... Mit Eggenberg hat er darüber gesprochen ..."): the clear lines read on the scan, the cipher from the
     figures.

## Holes and why

* [443] "dar ogni maggior [443] […]": not settled (the regest has "in aller Eile"; 443 might be "fretta", the following
  "di a i a" does not resolve).
* [290] "i disegni di Francia e del [290]": by the regest Richelieu; left as a group.
* [372] "Il [372] dopo haver ottenuta": by the regest the Duke of Lorraine; left as a group.
* [797] "Franzesi vogliano [797] quei passi": regest "den Pass zu erzwingen" (sforzar?); left.
* [525] "venuto di [525]": regest "von Spanien"; 525 in the M range, probably Madrid; left as a group.
* [649] "a questo [649]": the batch value "Republica di Venetia" does not fit "scritta dall'ambasciatore d'Inghilterra a
  questo [649]"; the regest has "an den hiesigen venetianischen Residenten", so 649 is more likely "residente di
  Venetia" — proposed, not used.
* [973] "li [973] delle quattro città": regest "die Hugenotten"; 973 in the S-V range fits Ugonotti, but the same digits
  were also read by DECODE inside "[973]inatissima" (print: inclinatissima), so left open.
* [966] "Palatino di [966]": the Palatine of Hungary is meant (Catherine of Brandenburg, Bethlen's widow); 966 in the S-V
  range fits Ungheria; left as a group.
* "dove […] andò chiamato": a struck group and a broken "dove".
* Last paragraphs: [233], [690], [630], [274] unresolved; "[?l'adempimento]" uncertain on the scan.

## Group values proposed

* 352 = confini ("avanzamento di gente verso [352]", "avvicinati a quei [352]"; regest "gegen die Grenzen", "den
  Grenzen genähert").
* 472 = Inghilterra ("tornato d'[472]", "ambasciatore d'[472]"; regest "England").
* 427 = fortificatione ("circa la [427] delle sue frontiere"; regest "die Befestigungen der Grenzen").
* 593 = principessa ("la detta [593]", of Catherine of Brandenburg; 5xx P range).
* 263 = Gabor (print "moglie di Gabor").
* 309 = cattolico (print "dichiararsi cattolico", "altri cattolici"; also R291).
* 375 = dieta, 393 = elettione, 627 = Polonia, 404 = Fiandra, 590 = pontificato (from the alignments with the print).

## Result

Read (in part where groups are open): every paragraph builds sentences; clean-sentence share 0.786
(`docs/_check_reading.py --file`, was 0.115).
