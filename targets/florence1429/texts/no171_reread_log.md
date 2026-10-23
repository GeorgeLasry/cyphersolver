# Re-reading log, no. 171 (DECODE R3754) (23 Oct 2026, Claude Opus 5.5; REREAD_BRIEF, batch b27)

## Starting point

Reading audit (22 Oct): "decoded, not read". The cipher runs were deciphered on 24 Sept (97 of 99 tokens valued with
Gabbrielli's 1863 key extended from the glossed siblings, `cipher171.tsv`), but the clear Italian around them was a
first pass of 18 Sept with gaps and (?) in nearly every sentence (`texts/no171_decryption.md`).

## 1. Is there a text already?

* DECODE R3754 fetched with the project cookie (`research/reading_audit/b25_fetch.py`, scratchpad): one file,
  IMG_R3754_I23011_P.jpg; no DOC_ attachment, no comment block, status "Non-decrypted", languages given as Latin
  (it is Italian).
* The only decipherment is Gabbrielli's interlinear glosses of 1863 (already used). No contemporary decipherment, no
  print (Guasti's *Commissioni*, Meister 1902 and Somogyi 2016 give the key only; NOTES, Prior art). The holding
  archive's key is Gabbrielli's own volume (ASF "Alfabeti ...", filmed by Ilardi, reel 58, and on DECODE as R5687-
  R5690), already the key here; nothing further in the inventory.

## 2. Read on the image

The 18 Sept strips were cut horizontally, but the lines fall about 3% to the right, so the right half of each strip
held parts of two lines; that is where most of the first-pass gaps came from. Line crops were cut again following the
slope (scratchpad `reread/florence/P*.jpg`, `q*.jpg`, `z*.jpg`) and each line re-read. Corrections in
`texts/no171_corrections.tsv`; the main ones:

* l. 1 "per lungo rattivo della piena grazia" -> "pel tempo cattivo della piena grande" (bad weather, the great flood);
* l. 2 "non n'averano e parlato però" -> "venne a vedermi e parlato [?seco]"; "sterino" -> "stemo";
* l. 3 "che uvera coprido lantechore" -> "che un'ora, scoprendo l'intentione";
* l. 5 "emotivare de tragionamento" -> "a motivare de' ragionamenti";
* l. 10 "cresse loro opro che notasseno" -> "dessi loro opera che [?metassono]";
* l. 12 "dico esse sarssone" -> "essi farebbono"; "(co)ntradido" -> "conchiudendo";
* a date line under the last line, never transcribed: "[?In] Castello, a dì viij di settembre" (sette with the
  -mbre stroke). This does not fit the "early 1425" of the profile summary; corrected there (year not written).

No cipher label changed; no key value changed (the cipher words are the 24 Sept decipherment). Look-alike readings
in the cipher words: 6 letters (L2a 8 without strokes = O; L3b 9 with a straight tail = N; the cup ᴗ = C in L3b and
L12b, D elsewhere; L12b # = I, L elsewhere; L7f ʓ = S, close to a null).

## 3. Alignment

Every unbracketed word of `texts/no171_reading.md` is either on the image (clear text, as re-read) or in the
24 Sept decipherment (CAPITALS). Supplied: [A] (MADONN), [è], [e] (between PARENTI and CITADINI), and the cover-word
meanings [i Dieci], [ambasciatore], [cavalli] from Gabbrielli's table; word signs in [CAPITALS]. "Et" before "anno"
is the & sign at the end of l. 7.

## 4. Score and judgement

`b17_score.py`, LANG_=it, reading body: 0.478 (11/23); explicit holes (HOLES=1) 0.609 (14/23). Before: 0.00 (the
audit's judgement; the old text could not be parsed). The middle of the letter holds (Paolo's visit; the advice that
a private person open the talks rather than that the Dieci send an ambassador, because Madonna is after all a woman
and suspicious; the plan that her kin and the citizens bind themselves secretly to do what the Count wants), but
the opening (ll. 1-4: twelve words partly or not carried), the sentence "O detto ..." (l. 9: four guessed words) and
the close before the date (ll. 12-13) do not build sentences. Below the bar: kept **decoded, not read**.

## Open, and why

* About a dozen clear words in ll. 1-4, 9, 12-13: illegible at the DECODE resolution (faded, fast cursive); the
  original (ASF, Dieci di Balìa, Responsive 2, no. 171, old 168) would settle them.
* ⊀ ψ before SOSPETOSA: too-short (one occurrence, no gloss).
* ⊡ before "sia" (il Papa?) and E before "dicesse" (ella?): no-key-material (not in Gabbrielli's nomenclator).

One sentence: "perché dice che MADONNA [è] PURE FEMINA E […] SOSPETOSA" (because he says that Madonna is after all a
woman and suspicious).
