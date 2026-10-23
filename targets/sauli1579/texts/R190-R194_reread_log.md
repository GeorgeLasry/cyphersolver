# Re-reading log, R190-R194 (22 Oct 2026, Claude Opus 5.5; REREAD_BRIEF, batch "sauli")

## Starting point

Reading audit (22 Oct): all five records "decoded, not read". The repository held Lasry's sign-by-sign decryption of
Midas's transcription for R190/R191 and per-passage tables with gloss fragments and paraphrased clear-text summaries for
R192-R194; no continuous text.

## What was done

1. **Images.** The 22 DECODE page images (IMG_R190_I1219 ... IMG_R194_I1242, 2082x2904) fetched with the DECODE
   session cookie (targets/bordeaux/decode/cookie.txt, still valid); saved only in the session scratchpad
   (reread/sauli/), not in the repository (ASV images).
2. **Existing text?** Every cipher passage on the 22 pages carries the secretariat's interlinear decipherment, and
   R193 f. 238r is itself a deciphered copy in clear. No printed edition was found on 21 Sept (web search); none
   re-searched. So the reading is: the clear text transcribed in full, each cipher passage in its gloss, and the gloss
   checked against the key decode.
3. **Transcription.** Each page read in four horizontal strips at native resolution, with zoomed crops where the
   gloss was cramped (R190 ff. 92r, 94r; R191 ff. 99v, 101r; R192 f. 196r, 196v). Midas's clear-text transcription
   (DOC_R190_D1643, DOC_R191_D1644) used as a first draft for R190/R191 and corrected on the image (e.g. "Su.ma" ->
   "Ill.ma", "Hunzio" -> "Nuntio", "fudata" -> "fu data", "Cassa" -> "lassa", "riceuuta" -> "venuta", "smeries" ->
   "Smerick", "Conte d'Osmun" kept as written).
4. **Alignment with the key.** Gloss and key decode agree wherever the figures are legible. Points where they differ
   or the gloss is incomplete:
   - R191 f. 101r: the whole cipher (7 lines) is glossed only between lines 1-3; lines 4-7 decoded with the key
     ("[a]nselmo al qual li suoi ministri davano da 4000 scudi il mese di paga, et gli devono 4 o ver 6 mesate, et
     hora provedono 72 per sbrigarsene"); 72 = denari from the gloss line. Figures followed over gloss ("davano da
     4000" for "dovevano 4[m]").
   - R192 f. 196r: "alla rassegna sono stati 3 milia nel pagamento" fixed from the decode where the gloss is
     cramped; "di poco [53] mille" left open (gloss "dieci mille" struck; 53 is h).
   - R194 f. 281v: "condescendere a li ..." (00 75 05 03): the object is not written; a hole left.
5. **Code groups settled or narrowed** (key.md unchanged except as noted in NOTES):
   - 82 = navi (R191 f. 99r twice, "dui navi"; R192 f. 196v "la Regina d'Inghilterra navi"): replaces Lasry's
     "Hune", which was Midas's reading of the gloss "navi".
   - 72 = Regina (R190 ff. 93r, 94v; R192 f. 196v) and = denari (R191 f. 101r, R192 f. 197v, R194 f. 281r): two
     senses glossed; probably two groups written alike (72 / 7z?), not separable on the image.
   - 40 = cattolici (R190 f. 94v, R192 ff. 196r, 197r) and the decipherer's "guerra" over "in una 40" (R192 f. 197r,
     struck) and "de la ... 40" (R190 f. 94v): the context needs "guerra"; open.
   - 10 Italia / V.S. Ill.ma, 20/28 S.M.tà / Italiani: 0 and the looped 8 are one shape in this hand; two senses each
     on the glosses, not separable on the images.
   - 60 = Duca (R191 f. 99v twice), 77 9 00 = il Marchese (R192 f. 195r), 30 also "armata" once (R190 f. 94v).
   - Unexplained four-digit prefixes 6371/7771/7361/7761 + 9 0 before "per"/"de la" (R193, R194): no gloss word
     corresponds; recorded, not read.
6. **Dates and authors corrected.** R190 f. 92r is Riario's letter to the Earl of Desmond, Elvas 12 January 1581.
   R191 is Riario to the Secretary, mid-January 1581 (encloses that copy). R192's letter is dated "Hoggi li 4 di
   genaro" (1581), the copy 29 Nov 1580. R193 = Badajoz 2 [Oct?] 1580 and Elvas 1[0] Dec 1580, both signed by Riario.

## Result

All five records read as continuous Italian, with English translations. _check_reading.py on the text bodies (notes
excluded): clean-sentence share R190 0.78, R191 0.80, R192 0.84, R193 0.79, R194 0.96; the "holes" counted are mostly
abbreviation-split fragments and old spellings outside the LM; the real holes are a few [...] per document (R190 3,
R191 2, R192 4, R193 1, R194 1). Remaining open: the code groups listed in 5, and three short illegible stretches of
clear text (R190 f. 93r, R192 ff. 196r, 197r).

## Alignment notes per record (moved from the reading files)

### R190

- The glosses and the decode agree passage by passage (digits read on the images; e.g. "pagamento" 77 81 63 00 65 03
  55 37 07, "la gente di Lisbona" 75 00 9 63 07 55 37 03 9 51 05 9 75 05 47 71 03 55 81, "tentarli" 37 07 55 37 81
  57 75 05, "di Generale" 51 05 9 63 03 55 07 57 00 75 03). The hand's 81 often looks like 01; Midas read several
  81 as 01 or 0?.
- Code groups: 30 "di S.S.tà" / "da S.B.ne" on f. 92r; 72 "la Regina" (ff. 93r, 94v); 40 "cattolici" (f. 94v,
  "a li cat.ci dell'Isola"); 24 "quell" ("di quelli soldati", f. 92r). On f. 94v "l'armata de la Regina" is
  75 9 30 9 51 07 9 75 81 9 72: the gloss gives "armata" for a group read 30 (S.S.tà elsewhere); and "guerra" is
  glossed over a short group ending 9 40 (40 = cattolici elsewhere). The reading follows the glosses; both groups
  are recorded as unresolved in the log.
- "Conte (di) Desmond/Osmon": the address and the two later mentions are enciphered with a short group before
  "esmun" that the key does not cover.
- "Smerick" (Smerwick, Dún an Óir): gloss "Smeriec", digits 47 75 9 47 65 03 57 05 61 53 (partly read).

### R191

- f. 101r is all cipher. The decipherer crammed the whole decipherment between the first three cipher lines; the
  four lines below carry no gloss of their own. Decoded with the key they continue the same text: "[a]nselmo al
  qualo suoi ministri / davano da 4000 scudi il mese di p/aga et gli devono 4 o[ver] 6 me/sate et hora provedono
  [d.] 72 / per sbrigarsene" (84 9 47 71 57 05 63 81 57 47 07 55 03). The gloss says "dovevano 4[m] sc."; the
  decode has "davano da 4000": the reading follows the figures. 72 is glossed "denari" here.
- Code groups confirmed here: 20/28 "Italiani" (f. 98r "quelli poveri Italiani", "li Italiani imbarcati", f. 98v
  "con Italiani"; the hand's 8 is a looped 0, so 20 and 28 cannot be told apart on these leaves); 28 "S.M.tà"
  (f. 100r "servire S.M.tà", f. 101r "S.M.tà sta"); 10 "Italia" (f. 98r "in Italia"); 16 "Inghilterra" (f. 98r);
  30 "S.S.tà" (f. 98v "nome di S.S.tà"); **82 "navi"** (f. 99r "dui navi", "le dui navi a la volta d'Irlanda": 51 27 03
  9 82, settles the R192 p. 4 question); 60 "Duca" (f. 99v "del Duca di Sora", "del Duca d'Alva"). "Conte" before
  "Desmon" is again a short group (9 0 9) not in the key.
- "Duara" is written so in clear (twice) and in the cipher of the f. 100r heading (51 27 81 57 00); not identified.

### R192

- Code groups, gloss against decode: 72 + 82 in "havendo la 72 82 et gente" = "la Regina d'Inghilterra navi"
  (82 = navi, as in R191; 72 = Regina, as in R190); but 72 "denari" in "alcuni 72" (copy) and in R191 f. 101r. 40
  "cattolici" ("a li 40", ff. 196r, 197r) but "guerra" in "in una 40" (f. 197r; the decipherer wrote "guerra" and
  struck it, the sense needs it; R190 f. 94v has "de la guerra" over a group ending 40 too). 10 "Italia" (ff. 195r,
  195v "in Italia", 197v "a la volta d'Italia", gloss struck) but "V.S. Ill.ma" in "incaricandosi 10" (f. 197v): the
  hand's 0 and looped 8 coincide, so 10/18 and 20/28 cannot be separated on the image. 20/28 "S.M.tà" (ff. 195r,
  195v) and "Italiani" (ff. 196r, 196v, 197r). 30 S.S.tà, 16 Inghilterra, 36 Francia confirmed.
- "Il Marchese" is the group 77 9 00 (f. 195r), glossed, not in the key; the tail 75 71 63 after "dubbio che ha
  S.S.tà" (f. 195r) is unglossed and does not decode (a closing flourish/null).
- "alla rassegna sono stati 3 milia nel pagamento": the decode (57 20 47 03 63 55 81 9 47 03 55 03 9 47 37 81 37 05 9
  3 9 65 05 57 75 05 81 9 55 07 75 9 77 00 63 81 65 03 55 37 03) fixes the half-legible gloss. "di poco 53 9 65 05
  75 75 07": the gloss "dieci mille" is struck; 53 is not a numeral group; left open.

### R193

- Three passages begin with a four-digit run and a 0 before 84 "per": 63 71 9 0 84 ("per tale impresa"),
  77 71 9 0 84 ("per la Fiandra"), 73 61 9 0 84 ("per Irlanda li Italiani"). The glosses give no word for the runs,
  so the reading follows the glosses; the runs (and 77 61 in R194) are recorded as unexplained prefixes, perhaps a
  marker or nulls. "Irlanda" is spelled 05 55 77 57 01 55 51 00 (77 for 57, 01 for 81: transcription slips).
- 16 "Inghilterra" ("in 16", f. 237r), 20/28 "Italiani" ("li Italiani", f. 236r), "1300" in plain numerals.
- The year of letter 1 reads 1580; the month is written over an erased word (Badajoz was Philip II's base until
  early December 1580).

### R194

- "gran provisione di denari": 63 57 00 55 / 77 57 07 27 05 47 05 03 55 07 9 07 37 9 72; the key gives "et" (07 37)
  where the gloss has "di", and 72 = "denari" (as in R191 f. 101r and R192's copy).
- "della tregua": 77 61 9 51 07 / 75 00 9 37 57 07 63 01 00 (struck through and rewritten); the leading 77 61 is the
  same unexplained prefix as in R193.
- "per mantenimento della religione cattolica in Fiandra": 75 01 9 0[?] 0 9 05 55 9 73 05 00 55 51 57 00, i.e.
  "la [code] in fiandra"; the code group for "religione cattolica" is the short run between 9s, not in the key.
- "a li": the gloss over 00 75 05 03 reads "a li" (or "a lei"); the decode is "a lio"; the object of
  "condescendere" is not written in the cipher or the gloss, so the reading leaves a hole. Margin of f. 281v: "li capitani" with 51 9 75 05 (the first passage repeated).
