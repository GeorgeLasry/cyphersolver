# Re-reading log, R41 (22 Oct 2026, Claude Opus 5.5; REREAD_BRIEF, batch b00 helper)

## Starting point

Reading audit (22 Oct): "decoded, not read". `R41_decryption.txt` (DECODE D1705, KaJo, May 2016, Meister no. 40):
clean-sentence share 0.683, hole rate 0.102.

## 1. Is there a text already?

- DECODE "cleartext" images: D1067 = address leaf ("Blois 8 di Decembre … Cardinale Montalto"), D1068 = f. 296,
  covering letter "Dup.te", Blois 8 December 1588; D1069–D1070 = f. 297r–v, a second covering letter in clear, Blois
  [day illegible on the thumbnail] December 1588. Not decipherments.
- The cipher cites Montalto's cipher "di oto del pasato" (8 November), so it belongs to early December.
- Francia 27 not imaged. Tempesti not used.

## 2. Decode and repairs

- Batch decoder, scratch variant `dec2.py`, hand re-parsing with `fit.py`, as R32. This record decodes cleanly: the
  decoder's garbles were mostly vocabulary gaps (persistendo, hostagio, ascoltaria, riceueriano, auantagio, pasaporto,
  Ciamberi, necesitare, speditioni) and spurious dots (635, 021, 459, 912).
- Plain-figure sums closed by a null 8: "500 8 caualli" (twice), "4000 8 fanti" (decoder: "era eauali").
- Undotted 151 (la Francia ha riceuta), 196 (Sauoia), 129.
- "6 4 9 2" (R32's "contra") here reads "però" + a stray 2; "6 4 9" alone = però at 299v l. 12.

## 3. Image checks

None decisive (corroded leaves); transcriber notes 298r l. 21 dark at the start, where the reading holds.

## Result

Before 0.683 → after 0.819 clean-sentence share on the "## Reading" body (hole rate 0.102 → 0.069). By hand: 3 unread
stretches […] (opening, a word after "Siuiglia", closing) and 4 partly carried words in about 920 words. Every sentence
holds. Grade A.

## Still open, and why

The opening before "per lettere" (298r l. 1), two letters after "Siuiglia", "Io non lasai" partly carried, "[ue]nti
giorni", the closing formula. No parse fits the transcribed figures; Francia 27 would settle them.

## Word-by-word alignment (`reread_b00_align.py`, REREAD_BRIEF step 3)

- First run TOTAL R41: 923 words, 3 supplied, 10 partly. Bracketed d[i] Siuiglia, da[gli] Ugonotti; le era → l'era; Altezza → Alteza, caualli → cauali; moved the [f. 299r] marker inside rime-/-diare.
