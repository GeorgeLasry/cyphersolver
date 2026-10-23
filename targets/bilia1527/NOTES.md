# Jo. Antonio Bilia to Francesco II Sforza, Burgos, 22 November 1527 — BnF fr. 3013 no. 43 (catalogue 291, part)

Status: in progress. f. 102r is read in part from a contributed AI-only transcription (issue #55, Harumi-Matsuba),
checked here; f. 102v (seven cipher lines) has no confirmed reading and needs a human re-transcription; the name code
B.58 is open.
**22 Oct 2026, reading audit:** the f. 102v entry is *decoded, not read* in profile.json (raw decoder lines with no continuous sense), as the status above says; fraction_read already counted it as unread.


**Outcome: read with known key, read in part; contributed.** Harumi-Matsuba (GitHub issue #55, 20 Oct 2026; repository
https://github.com/Harumi-Matsuba/bilia1527-public, CC BY 4.0 data / MIT code) transcribed the cipher of f. 102r and
f. 102v from the Gallica images with Claude Opus 5.5, cross-checked by three independent OpenAI Codex transcriptions
and two rounds of AI image checks, and read f. 102r with the Sforza key DECODE R5258 ("Cum equite Bilie / extracta ex
cifris"), using this project's transcription of that key sheet (`targets/gilino1527`) and George Lasry's independent
recovery of the same key. **No human checked their transcription.** Their "complete reading" of f. 102r rests on 94.9%
value agreement with Codex and a shuffled-key control, not on this project's read bar. Checked here 21 Oct 2026 (below).

One key, one entry: no. 42 of the same volume (Bilia to Jo. Francesco Taverna, called Zaberna in the catalogue, the
Duke's ambassador, same date, ff. 99r-v) is in a **different cipher** (base letters M, A, K/H, R, B, a box sign and L
with numbers 1-29, mixed with clear Italian) that neither R5258 nor R5237 fits. It is not part of this target; it
stays open in the catalogue (cat. 291, narrowed). The same key R5258 reads "el Gilino"'s letter of 15 Sept 1527:
[`targets/gilino1527/`](../gilino1527/NOTES.md), page `gilino1527.html`.

## The letter

- BnF Français 3013 (letters 1501-1600), no. 43: "Lettre, en italien et en chiffre, de Jo. Antonio Bilia ... al
  signore duca de Milano ... De Burgos, XXII novembris 1527". Ink foliation ff. 102r-v (the BnF finding aid's
  "Fol. 105"). Gallica ark:/12148/btv1b9060138r: f. 102r = view 164 (30 lines, all cipher), f. 102v = view 165 (7
  cipher lines, then the clear close "De Burgos XXII nobris 1527", a clear postscript "Sua M.ta ha disposito l'andata
  sua ad Valentia como facto Natale" and the signature "Humill.mus servus Jo. Ant.s Bilia"), address view 167.
  Images fetched here through the BnF IIIF service (openapi.bnf.fr; gallica.bnf.fr answered with a Cloudflare page).
- Writer: Giovanni Antonio Bilia, "Cavaliere Bilia", the Sforza agent at Charles V's court; the R5287 nomenclator
  (cart. 1591 no. 53) lists "Cavallero billia" and "Ghilino" as two people (`targets/gilino1527/key_R5258.md`).
- No DECODE record for fr. 3013 was found in the harvest list (`research/catalogue_harvest/decode/list.json`).

## The key

DECODE R5258 = ASMi Carteggio Sforzesco cart. 1591 no. 24, docket "Cum equite Bilie / extracta ex cifris": the key
of this correspondent, so the method is *read with known key*. Barred base letters G (written like 6), B, D (the
contributor calls it o for numbers 51-65) and o with two-digit numbers for syllables in ordered rows (B.31-50 ba..gu,
B.51-55 fa..fu, D.51-65 la..nu, G.56-80 pa..tu, o.33-47 va..zu), bare numbers and signs for letters with homophones,
a few word codes (H.27 che, H.28 come, R.23 con, R.28 ancora), a nomenclator of names, and nulls. Our transcription
of the sheet: `targets/gilino1527/key_R5258.md`, `dec.py`, `key_r8572.tsv`, `key_extra.tsv`. The contributor added
values for five signs not found on the sheet transcription (ß r, £ l, F c, tt t, qx ss; 41 signs, 8.1% of f. 102r).

## Checks made here (21 Oct 2026)

1. **Our key, applied independently** (`decode_check.py`, output `measure.txt`, `decoded_ours_f102r.txt`). Their sign
   names were mapped to ours (G.nn = our 6.nn, o.51-65 = D.nn, φ = bf, θ = th, ÷ = dots, 3p = xp, zd = sq). Of the
   505 signs of f. 102r, our key gives a value to 459 (90.9%); where both keys give one, 440 of 459 agree (95.9%).
   The 19 disagreements are all of three kinds: the crossed x (our Gilino key: null; theirs: s, 15 times), θ (ours a,
   theirs o, 2) and the plain o sign (ours z from the Gilino context, theirs o, 1), plus 3p u/v (1). On the R5258 sheet
   image (DECODE PDF, rendered at 200 dpi) the crossed x stands in the **s** column and the θ-like sign in the **o**
   column, so the contributor's values follow the sheet; our Gilino values for these signs were context guesses. The
   other 45 signs are their five inferred signs, `as` (read as a 25), two nulls (R~, a circled 32), B.58 and B.3?.
2. **Language model** (shared `lang`, `it-cinquecento`, order 5, no spaces): our decode -2.183 per character; 1000
   shuffles of our key over the 76 valued signs used: best -3.113, none at or above the real key. Their decode
   (with their inferred values) -1.882. Our decode reads as Italian over the whole page (`decoded_ours_f102r.txt`):
   "hozi ce sono ritrovato a disnare col signore ... si è meco querelato havendo hauto carte da suo genero che vostra
   ecelentia ...".
3. **Image spot check**: f. 102r lines 1-5 (81 signs) compared sign by sign with view 164 at full resolution: all 81
   names agree; at three places the second digit cannot be told apart at this resolution (B.39/B.33 on lines 2 and 3,
   G.69/G.65 on line 1) and the transcription follows the reading. The contributor's own open list (OPEN §3) has B.39
   on line 2 as an image-check split. Line 6 begins with a sign that looks like B.33 on the image; they read B.39
   ("conte").
4. **B.58** checked on the R5258 sheet image: the nomenclator has B.55 Imperatore, B.56 Sua M.ta, B.57 Nassau, B.60
   Lasciau, B.62 Vicere, B.63 Don Hugo, B.66 Legato/Nuncio, B.71 Borbone; **no B.58**. It stays an open name code
   (the contributor's decoded text shows "mi", the value of D.58, as a placeholder).
5. **f. 102v** with our key (`measure_f102v.txt`, `decoded_ours_f102v.txt`): 102 of 118 signs valued, 94 of 102 agree
   with theirs; LM -2.597 against a best shuffle of -2.750 (0/1000), a thin margin. Words appear ("a suo genero",
   "vostra ecelentia", "potesse", "conformita", "ancora", "con desiderio si aspetta", "con le risposte di") but much
   of it does not read. The image (view 165) shows the line ends running into the gutter and show-through from the
   recto; agrees with the contributor's decision not to publish a reading of it.
6. **Coherent share of f. 102r** (estimated, not measured): about 28 of about 500 valued signs sit in the readings
   the contributor marks doubtful (Theophimo, fi(glio?) tavolo, pervitio, papre, ina, tompi, vechilza, the £ = l/et
   places, B.58, B.3?), so roughly 94% reads as sense. Below the 95% bar; with f. 102v unread the target is partial.
7. Counts measured with `docs/_check_profile.py --measure`: f. 102r 505 signs (94 distinct names incl. ? marks),
   f. 102v 118 signs.

## Remaining gaps
- f. 102v, seven cipher lines (118 signs): contributor's reading unconfirmed and not given; our key gives words but no continuous sense - blocker: open-codes; workable: needs a human sign-by-sign re-transcription; line ends in the gutter of a microfilm image
- f. 102v line ends at the gutter (about 8 signs) - blocker: illegible; the only image online is the BnF microfilm scan, where the last signs of each line curve into the binding
- name code B.58 (f. 102r line 2, the old man Bilia dined with) - blocker: open-codes; not on the R5258 nomenclator (checked on the sheet image); one occurrence; the context (an old lord whose son-in-law wrote to him about the Duke and conte Theophimo) does not name him
- about 28 doubtful signs on f. 102r (8 image-check splits, "Theophimo", "pervitio", "papre", "tompi", "vechilza", £ as l or et, B.3?) - blocker: open-codes; AI-only transcription, no human check; a human reading of view 164 at full size would settle most

## Escalation
- [x] siblings: no. 42 (same date, to the ambassador Taverna) opened on view 159: a different cipher, not this key; no decipherment or clear copy of no. 43 in fr. 3013 (contributor's search, and views 159-167 looked at here)
- [x] clear-pages: f. 102v clear text is the close, date, a postscript about the Emperor going to Valencia for Christmas, and the signature, not a decipherment
- [x] known-keys: R5258 (Bilia's key) applied; R5237 ("Cum Egr[egi]o Bilia", numeric alphabet) does not fit (contributor); R5256 is a different syllable table
- [x] print: CSP Spain iii/2, CSP Venice iv, L&P iv, Cryptiana searched by the contributor: nothing. Not checked by them or here: Cerioni 1970 (the Sforza key edition) and Giudici 2018
- [x] key-rebuild: five sheet-less signs given values from context by the contributor; x and θ values confirmed here on the R5258 sheet image; B.58 not on the sheet
- [x] retry: f. 102r and f. 102v decoded again here with our key; f. 102v stays unconfirmed

## Files

- `contributed/` — Harumi-Matsuba's files, unchanged (see `contributed/ATTRIBUTION.md`): transcriptions
  (`data/transcription_f102r.txt`, `data/transcription_f102v_unconfirmed.txt`), key (`data/key.tsv`), decoded f. 102r,
  their English documents (METHOD, READING, OPEN, PRIOR_CHECK), the three Codex transcriptions and the image-check
  verdicts.
- `decode_check.py` — our R5258 key applied to their transcription, comparison and LM control; `measure.txt`,
  `measure_f102v.txt`, `decoded_ours_f102r.txt`, `decoded_ours_f102v.txt`.
- `build_reveal.py` — writes `docs/reveal/bilia1527.json` (lines 1-6 of f. 102r).
- Page: `docs/bilia1527.html`; crops `docs/bilia1527_lead.jpg`, `bilia1527_f102r.jpg`, `bilia1527_f102v.jpg`.

## Sources

- BnF Français 3013, Gallica ark:/12148/btv1b9060138r, views 159-167; BnF archives et manuscrits cc494715.
- DECODE R5258 (https://de-crypt.org/decrypt-web/RecordsView/5258), ASMi Carteggio Sforzesco cart. 1591 no. 24; R5237
  (cart. 1591 no. 3).
- Harumi-Matsuba, bilia1527-public (GitHub), 20 Oct 2026; issue #55.
