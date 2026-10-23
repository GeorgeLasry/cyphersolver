# Re-reading log, R9952 and R9957 (22-23 Oct 2026, Claude Opus 5.5; REREAD_BRIEF, batch b18)

## Starting point

Reading audit (22 Oct): both records "decoded, not read". R9957 was in the repository only as fragments of its
contemporary decipherment quoted in NOTES and two first-pass sign transcriptions (`trans_p1-9.txt`, `trans_p10-18.txt`)
whose sign boundaries did not match the syllable system; R9952 had no text at all. Clean-sentence share: none to score
(no reading file).

## 1. Is there a text already?

- **DECODE records.** `rec9952.htm` and `rec9957.htm` (saved 21 Sept) list page images only: 20 for R9952, 18 for
  R9957; no transcription, plaintext, key file or comment block. All 38 images are in the main checkout
  (`targets/charles1536/img/`, git-ignored) and were opened (contact sheets, then strips at native resolution).
- **R9952.** The contemporary decipherment, "del Emperador a Su Al[teza]", is complete on images P12, P13, P15-P18,
  P20 (ff. 13-14 bis; P14 is the address leaf, P19 blank). It gives only the ciphered passages and marks each return to
  clear with "/ lo otro claro /" or "/ claro /". Transcribed line by line: `R9952_decifrado_ff13-14.txt`. Not in print
  as far as checked (Tomokiyo, cryptiana spanish2C: "Deciphered in the margin. The cipher matches Charles V-Prince
  Philip Cipher (1545)", with six code words).
- **R9957.** (a) The contemporary decipherment of the last cipher passage (ff. 273v-274r) is on stamp 0017 below the
  date and signature and runs onto 0018: transcribed, `R9957_decifrado_f274.txt`. (b) The whole letter is printed by
  Wanruo Luo, thesis, Universitat de València 2021, pp. 287-290, with the key AGS Estado leg. 1.1.1 doc. 169 reproduced
  on pp. 603-606. The PDF was already in the main checkout (`targets/caracciolo1537/prior/luo2021.pdf`, not committed;
  RODERIC itself now sits behind an Anubis bot check and was not used). Her edition is in copyright: used as a check
  only, cited, not copied.

## 2. R9952: checking the decipherment against the figures

No key of this cipher (Tomokiyo's "Charles V - Prince Philip Cipher (1545)") is in the repository, so the runs were
not decoded sign by sign. Checked instead on the letter's own images (P3-P11): the clear words the cipherer left inside
the cipher runs stand in the same order and place in the decipherment on every page checked (P5, P6, P9, P11:
"las quales son", "tener continuament para la conservacion", "venir adelante de seguirse algun gran inconviniente
por", "la qual para las cosas que tenemos en las manos podeys bien juzgar si nos seria necessaria y la reputacion",
"con este respeto", "por ventura podrian yndusirse", "y pudiesemos conservar alguna parte", "podriamos con la ayuda de
nuestro Señor haver nuestra", "entre su", "dignidad imperial nos trae", "difficultad dexandolo a las espaldas
podrian", "con mas facilidad y mejor se podria hazer", "respondemos al dicho principe", "le remitimos que haga tomar
en Seçilia y Napoles o donde", "siendo menester se ha de buscar y proveer en qualquier manera que se pueda hazer
assi", "Assimismo que provea de algunas naves ... de otra manera"), and Tomokiyo's code words stand where the
decipherment has their words (go = para before "la conservacion" and "la utilidad"; pi = enemigos after "nros"; xu =
dinero in "alguna parte del dinero"). One disagreement: the figures' clear "dexandolo" where the decipherer wrote
"dexando"; the reading follows the figures. Alignment of the reading with the decipherment
(`research/reading_audit/b18_align.py`): 1,917 of 1,919 words carried; the two others are that "dexandolo" and the
decipherer's "ex" + "periencia" written as one word.

## 3. R9957: reading the figures with the doc. 169 key

- Key summarised from Luo's images in `R9957_key169.md` (letters with three homophones each, syllables as base sign +
  vowel mark or the numbers 32-91, codes 92-211 and graphic code signs, dotted signs and numbers from 212 nulls).
  Calibrated on the last line of the first run (stamp 0001): "se gra[?…] e de manera que no se pierda".
- The cipher of stamps 0001-0014 was read run by run on crops at 1.6-2.4x native resolution, in three parts
  (0001-0006, 0007-0011, 0012-0014); each run's sign transcription, decode and comparison with Luo are in
  `R9957_runs_A.md`, `R9957_runs_B.md`, `R9957_runs_C.md`. A spot check of run B2 (stamp 0007 l. 2) on the image
  confirmed the sign labels ("todavia esten apercebidos las gentes que have-"). 52 runs; about 1,600 words.
- Key observations (no value changed; each holds at every occurrence met unless noted): e+ (te) is drawn like a hooked
  4; ŧ̲ (ma) has a long bar like ŧ+; the key's nn sign stands for ñ (año, señora, empeñando, cuños); 28 (rr) is used
  for initial r (rreynos, rresolutos); L# is zi (dozientos, hizieron) and Lp go or zo (the g and z bases share a
  shape); dotted signs are nulls; "alla" is written 4 31 with a small 3. Recorded, not adopted: dinero(s) has 52 (na)
  on stamps 0005-0006 and 53 (ne) on 0007-0014; 5 for b three times on stamps 0009-0011 (key: d); a sign 7° in
  "a[?yu]da" and "cu[?yo]" (Luo reads vo there, "avoda", "cuvo", both "(sic.)"); ŧ with two cross-strokes read mi in
  mill/mismo but standing where me is wanted in "menos", "menester".
- The last passage (stamps 0016-0017) was taken from its contemporary decipherment; the cipher was not re-read sign by
  sign (code 97, Antonio de Leyva, stands where the decipherment has "Antonio").
- Figures against Luo (figures followed, each in the run files): "En lo de los cinco mil" (her "En los"),
  "apercebimientos", "que le scrivimos", "aquella frontera", "deura", "pongo" (her "ponpo"), "aquela", "toda las",
  "asientos de trezientos" (her "asi en todo de"), "asienten", "seyscientos", "haver haver havido", "me embien" (her
  "ma (sic.) enbien"), "pl[ata]" (her "lata"); "Gonçalo de Ayora" (stamp 0005) is cipher that she prints as clear; on
  stamp 0009 there are about 14 cipher signs where she prints none (run B16, unread).

## Result

| record | before (audit) | after: clean-sentence share of the reading body | rests on |
|---|---|---|---|
| R9952 | no text, decoded, not read | 0.683 (114/167); explicit holes only 1.00 (167/167) | contemporary decipherment ff. 13-14, checked against the clear words and code words of the figures |
| R9957 | fragments only, decoded, not read | 0.629 (146/232); explicit holes only 0.953 (221/232) | the figures under the doc. 169 key (ff. 270r-273v) and the contemporary decipherment (f. 274r); Luo 2021 as a check |

The checker's Spanish word list does not know much of the period spelling (necessidades, haviendo, conviniente,
dezir, rreynos), which is where most of its "holes" fall; the readings keep the spelling the figures give.

## Open

- R9952: "paresce […]" before "claro" (f. 13 bis v) and a short word after "scripto" at the end (f. 14 bis r):
  illegible (cramped hand); "[?viendo]", "[?vee a]", "[?el]", "[?movimiento]": partly legible.
- R9957: run 1, a tear after "bien de" and "se [?gra…] e" (82 r ꝝ makes no word); run B16 (stamp 0009, about 14 signs,
  no sentence, no second text); the dense blocks B25 and B28 (stamp 0011) partly carried; C2 (stamp 0013) a faded fold
  and two figures with no value ([43], [6]); C5 a tear at l. 17. Blockers: illegible (tears, fold, cramped blocks) and
  no-key-material (B16, [43], [6], 7°: no second text in this key gives their value).
