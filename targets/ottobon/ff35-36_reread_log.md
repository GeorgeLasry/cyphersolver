# Re-reading log, Ottobon 1589 first piece, ff. 35r-36v (23 Oct 2026, Claude Opus 5.5; REREAD_BRIEF, batch b31)

## Starting point

Reading audit (22 Oct): first piece "decoded, not read" (`reading.txt` ff. 35r-36v; f. 35r a few clauses, ff. 35v-36v
mostly `[...]` and low lines). Second piece (ff. 37r-38r) already read; not part of this batch.

## 1. Is there a text already? No

- **DECODE R2252** fetched logged in again on 23 Oct 2026 (`research/reading_audit/b31_fetch.py`): 9 images
  `IMG_R2252_I16036..16044` (two-page openings, about 3100-3270 x 2390-2570 px, i.e. about 1550 px per page), the
  same files and sizes as the copies already in the main checkout (`img/decode/`); no document attachment, no
  transcription, no comment block, status N/A, "Inline plaintext: No". No higher-resolution version exists on DECODE.
  Page 3 (ff. 35v-36r) viewed whole again: heavy bleed-through from both sides, text lines about 30 px high, digits
  2/7, 3/5/8, 0/8 not separable (as found on 9 Oct with 2x crops).
- Valle de la Cerda's decipherment is lost (BNE catalogue, Mss/994 item 5: "no tiene contracifra ni declaración por
  hauerse perdido"); the Mss/994 siblings R2248-R2262 hold no copy (opened 9 Oct).
- **Key**: the Council of Ten's Zifra Prima (ASVe CX Cifre b. 4 reg. 16 ff. 64-65 = DECODE R1789) is the key, with two
  homophones added; nothing further to find in the inventory.
- **Register copy / print**: ASVe Senato, Deliberazioni Secreta (Francia), 27 April 1589, not online; CSP Venice viii,
  Hübner, Desjardins, Morosini, De Thou checked 9 Oct without the text. BL Add MS 30635 (de Maisse's letters "avec
  les responses") not digitised.

## 2. Score of the existing reading

Reading body built from `reading.txt` ff. 35r-36v (low lines as holes): b17 `LANG_=it` **0.161 (5/31)**, the same
with `HOLES=1`, hole rate 0.34-0.39. For comparison the second piece (ff. 37r-38r), state read since 22 Oct, scores
0.351 plain and 0.541 explicit holes only: below the brief's 0.60 bar, flagged for review.

## 3. Decision

No new text, image or key material reachable; no reading change. **Kept decoded, not read**: blocker
needs-physical-access (a 400-dpi reproduction of BNE Mss/994 ff. 35-36 or the ASVe register copy). Look-alike count
not applicable (no new reading).
