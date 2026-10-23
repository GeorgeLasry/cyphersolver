# Re-reading log, R5029 (23 Oct 2026, Claude Opus 5.5; REREAD_BRIEF, batch b37)

## Starting point

Reading audit (22 Oct): "decoded, not read". `dec.txt` decrypted every letter-spelled passage with Mírka's key, but the
clear text of p3R-p5L was excerpted ("Casse(?) ...", "durchschnid ... «102» ..."), so about half the sentences did not
build. No reading file existed: before = 0.00.

## 1. Is there a text already?

- DECODE R5029 record page (`decode/rec5029.htm`, main checkout, git-ignored): five images and Mírka's xlsx; no
  transcription, comment block, "cleartext" image or decipherment attachment. Status "Non-decrypted".
- All five images opened at full resolution (crops in the scratchpad, `b37_crop.py`): no interlinear or marginal
  decipherment anywhere. P5 right and P1 are blank versos (P1 shows P5L through the paper). The brown line-beginnings in
  the left margins of P3L, P4L and P5L and one line at their heads belong to a second, larger sheet folded under the
  letter; only its first letters show (perhaps the "beyligende Copia" of p2, but not legible) - not reachable.
- Neighbouring records R5025-R5028 were fetched and scanned on 5 Oct 2026 (glosses for 78, 99, 103, 167 only).
- Print: none known for a private letter of the brothers in the family archive.

Result: no text of the letter exists; read it on the image (step 2).

## 2. Read on the image

- The clear text transcribed line by line from the full-resolution crops with the cipher groups in place:
  `R5029_transcription.txt`. Every cipher group re-checked; no label changed.
- Corrections to the clear context in `ct.txt` (`R5029_corrections.tsv`): *Casse(?)* -> *lasse hiermit die zeit
  vergehe*; *durchschnid* -> *durchgehends* [?*ausstrechen*]; *Grentze* -> [?*Breunsche*]; *Wartheimber* ->
  *Wertheimber* (Samson Wertheimer, the court banker, fits "will ... nicht mehr zuhalten"). ct.txt and dec.txt updated.
- Doubtful clear words: a barred abbreviation, twice (P4L l. 9 "der [..] von Madrit zurückh gekommene currier", l. 15
  "zu zeit der [..] Accession"), Spanish fits both but the letters are not secure: [?hisp.]; [?abfertige] (p2);
  [?ausstrechen] (p3R); [?Breunsche] (p4R).
- Key: no change to Mírka's letter table (it holds at every letter group). Codes: no value adopted beyond Mírka's list
  and the sibling glosses. Two further sense-only proposals from the alphabetical order of the nomenclator, kept as
  holes: 101 [?eröffnen] (between 99 Engländer and 103 Eugen; "Eugen selben schon über 2 monathe [182] [101] lasse"),
  225 [?Wien] (after 213 Starhemberg; "der curier ... zu [225] angelanget"). 151 cannot be Mírka's "Kaiserin"
  (Kayserin would follow 152 Kayser); 102 would fit *Euer* ("[102] belieben ... den letzten versuch zu thun"); left open.
- The full text identifies the writer: the plenipotentiary who must open the Congress (of Cambrai), quoting an order
  that names "der Graf von Windischgräz" for the Spanish accession made with Beretti Landi at The Hague, writing to a
  brother at court ("von dort aus", "an allerhöchsten orth vorlegen"): Ernst Friedrich to Leopold Viktorin.
- Earlier NOTES gist corrected: *selbst widerrathen [146] eine Excusation zu machen* = the Emperor advised
  **against** making an excuse (not "advised to make").

## 3. Alignment

`b37_align.py R5029_transcription.txt R5029_reading.md` -> `R5029_align.txt`: 605 reading words; the 18 not matched
one-to-one are expansions of abbreviations (*E: E:* Euer Excellenz, *gehors:* gehorsamst, *I: K: M:*) or words joined
across a line break. One supplied word, bracketed: [dem] (before *Prinz*).

## 4. Bar

- `b17_score.py` (LANG_=de): **0.615** (32/52 clean), hole rate 0.126; with HOLES=1: **0.846** (44/52). Both recorded;
  the de word list does not know 1721 spellings (*werckh*, *zurückh*, *uillen*) or the Latin tags.
- `_check_reading.py --file` on the whole file (header and notes included): 0.462 (pointer only).
- Look-alikes: none (numerical cipher; the 4/5 distinction was settled on 5 Oct).
- Reader's judgement: the sentences hold except two clauses where open codes cluster ("Kayser aber will [168]
  verliehre Compagnie und die [181] [206] worden"; "damit [?nicht] seine, ich hat der Prinz [206] umb dessen dienste
  zu [?haben]"). The letter's content can be translated throughout (`R5029_en.md`).

Verdict: **read** (grade B), 19 codes open with an outside blocker (no key material: no gloss in the siblings; the
brothers' other letters in karton 202 are not on DECODE).
