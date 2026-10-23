# Re-reading log, R4500 cipher lines 1-7 (23 Oct 2026, Claude Opus 5.5; REREAD_BRIEF, batch b30)

## Starting point

Reading audit (22 Oct): lines 8-14 read; lines 1-7 (258 of 538 signs) "decoded, not read": the decode of ll. 2-4 is
garbled and the old normalised reading filled it with bracketed conjecture. Clean-sentence share before: no separate
reading of these lines (the conjecture text in R4500_decryption.md is not a reading).

## What was done

1. **Every file on the DECODE record** (R4500, main checkout `decode/rec4500.htm`): one image only,
   `IMG_R4500_I26572_P.jpg` (2628 x 3778); no DOC_* text, no attachment, no comment block with a decipherment.
   The 126 records of the volume (R4452-R4577, `decode/series/`) were all fetched in September: about 120 key sheets,
   no clear copy of this letter; the single-row alphabets R4467, R4491, R4520, R4525 are not this key. No key under
   another name was found in the series; the arcinsys inventory of HStAM 4 d Nr. 1218 lists the volume as Hesse-Kassel
   claves 1635-52 with no separate entry for this letter's key.
2. **The interlinear gloss** (the only contemporary text) re-read at 2-2.2x on native crops (scratchpad,
   research/reading_audit/b25_crop.py, b30_strips.py): above l. 1 "die Landt[…]"; between ll. 1 and 2 "insonderheit
   … ihr … gewalt … beschwerlich" (faded, cramped, partly over the clear text); between ll. 2 and 3 "das kann dieses
   orths halber observiren dagegen den selben"; between ll. 3 and 4 "etwas tentiret werden solte zumahl nicht
   unbewandt". The gloss stops at l. 4. It is not a letter-for-letter decipherment: it matches the signs at "dieses
   orts halber", "dagegen denselben", "etwas tentiert werden solte", "zumahl nicht unbewandt", but at "insonderheit"
   and "observiren" the signs give other letters ("…nur [?b]eit", "sast ueg ris sen").
3. **Signs** of ll. 2-3 re-checked against `cipher_tokens.txt` on the zooms: no transcription label changed (the
   tokens hold; the line 2 reading "1 2 7 1 2 / 6 0 0 8 θ / 4 0 9 / 1 2 ƒ / 6 7 w …" is what the scan shows). No key
   value changed: the readings that would mend l. 2 (insonderheit) need values that break ll. 8-14.
4. **Partial reading** `R4500_l01-07_reading.md`, aligned word by word with `reading_tokens.txt`: every unbracketed
   word is carried by its signs; supplied letters bracketed. ll. 4-7 now build a clause ("dagegen denselben etwas
   tentiert weren solte, zumahl nicht unbewandt, was und ob en gebührender manutenirung der [?Keiserm.] Mait. und
   [?des] Reich[s] …"; "gebührender" replaces the old "gebührend zur", from L05 end "rend" + L06 "erm").
   Letters on a look-alike alternate: 0 (9 = u/b is a homophone of the key, not a look-alike).
5. **Score** (b17_score.py, LANG_=de): 0.00 (0/5); explicit holes (HOLES=1) 0.20 (1/5). Below the bar.

## Result

Stays decoded, not read. ll. 1-3 do not build sentences.

## Open (blockers)

- l. 1 end (9 signs) and l. 7 (3 blotted signs, clear-text insertion): illegible on the only scan.
- ll. 2-3: illegible (the gloss, the only control, is faded and cramped and does not align with the signs; the
  signs themselves give no German without values that break the rest). A better image of HStAM 4 d Nr. 1218 no. 49
  is the next step (arcinsys may offer one on request).
