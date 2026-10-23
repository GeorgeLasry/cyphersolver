# Re-reading log, Clairambault 357 f. 167 interlinear part (23 Oct 2026, Claude Opus 5.5; REREAD_BRIEF, batch b26)

## Starting point

Reading audit (22 Oct): the second outcome.texts entry (f. 167r from the cross mark and f. 167v) "decoded, not read":
the glosses were transcribed as fragments ("... des [⊖] ... de la court ...", "Cambaronne [?]", "Coride [?]") and the
verso was not read word by word. The f. 168r clear copy (the first entry) already reads.

## What was done

1. **Existing text?** Yes: the contemporary interlinear decipherment on the leaf itself (the decipherer's words over
   the figure groups), and the writer's own clear stretches between the cipher lines. No DECODE record of this
   letter; no print (NOTES). No other copy in Clair. 357 round ff. 167-168 (NOTES, siblings).
2. **Images.** Full-resolution Gallica canvases 331-332 (3507 x 5722, 3392 x 5743) from the main checkout's `img/`
   (git-ignored), copied to the session scratchpad and cut into line strips and zooms.
3. **Transcription.** Every line from the cross mark to the date transcribed: clear text, glosses and figure groups,
   `f167_interlinear_transcription.txt`. The part after the cross mark is mostly the writer's clear text, with cipher
   lines (glossed) for the names and the sensitive clauses; it is not solid cipher, which is why the earlier pass
   read only the glossed words.
4. **Figures decoded** with Tomokiyo's table as extended in `key.md` (`research/reading_audit/b26_clair_dec.py`) to
   check the glosses and to fill unglossed or cut glosses: "si vous y voulliez entendre", "il se promectoit mener",
   "avec moy se negoce a bonne fin", "couleur d'autre voyage il vous fourniroit d'autant", "l'embarquement"
   (51 20 19 16 14 43 85 24 28 64 28 19 26), "le feu admiral a la Floride", "Rendan les lettres", "neantmoings on se
   servira de ceste occasion a conclure la paix", "aux Huguenotz". 73 = d confirmed ("45 31 73 D" glossed
   "d'Angleterre"; Tomokiyo had "73?"); no other key value changed. Digit strings where the strokes run together
   (e.g. under "ne pourroit procurer", which decodes "ne s…roict") are recorded but not used to change the reading.
5. **Corrections to the earlier fragments:** "Cambaronne [?]" is "l'embarquement"; "Coride [?]" is "a la Floride"
   (after "le feu admiral", i.e. Coligny's Florida venture); "Saisonne" is "vaisseaulx"; the sign before "envoyant"
   is glossed "la Royne mere"; R is glossed "Nerac" and ✝o "la court"; "Il se trouvera [?]" is "Il se promectoit";
   "la bonne proposée" is "la bonne propose[r?]"; "et en … c'est bien si avant" is "et en est bien sy avant depuis dix
   jours"; recto "et que luy" runs on into verso "Fumée, si luy voulliez commettre cette charge soubz couleur d'autre
   voyage".
6. **Alignment.** Word by word against the transcription: words carried by neither a gloss, a clear word nor the
   figures are bracketed ([de], [advis], [sur la], [vous], [J'ay], [Il]); doubtful glosses or decodes are [?word].
   Letters resting on a look-alike alternate: 0 (the reading follows glosses and clear text; where figures were used,
   the digit misreadings are listed as doubtful, not chosen between look-alikes).
7. **Score** (b17_score.py, fr, reading body): 0.758 (25/33); explicit holes (HOLES=1) 0.909 (30/33). Before: the
   fragments in `f167_decryption.md` (not scored as a reading). Reader's judgement: the sentences hold (Fumée's
   reconciliation proposal from Navarre; the plan to open the war in England with Fumée providing ships; the
   comparison with Coligny's Florida venture; the letters to the Queen of Navarre through Randan; Villeroy's letter on
   satisfying Mayenne, the withdrawal of the reiters and Swiss, peace with the Huguenots and the ruin of the country).
   Doubtful: "son [?edit] a premier de son [?retour]", the last cipher line ("[?des lettres] de M^r de la Forest"),
   "[?je suis vostre serviteur]".

## Result

Read from the contemporary interlinear decipherment and the clear text, checked against the figures (grade B: a few
doubtful words and one cut gloss).

## Open

- Unglossed figure strings where the digits are not secure (under "ne pourroit procurer", the last line before the
  date, the line "si porte bien …"): blocker **illegible** (strokes run together at full resolution; the gloss is cut
  or faint).
- The sender's signs at the foot of f. 167v (8 X X 8): **no-key-material**.
