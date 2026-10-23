# Re-reading log, R1136 (22-23 Oct 2026, Claude Opus 5.5; REREAD_BRIEF, batch b18)

## Starting point

Reading audit (22 Oct): "decoded, not read". `beam21_r1136_pass5.txt` scores 0.0 on `_check_reading.py` (0/7); 66.9 %
of decoded letters inside claimed phrases (pass 4/5), [..] in nearly every line.

## 1. Is there a text already?

- **DECODE.** Record page and every linked file re-fetched with the project cookie on 22 Oct 2026
  (`research/reading_audit/b18_caprile_fetch.py`, scratchpad only): two page images (I5740 letter with the cipher,
  I5741 address), no attachment, transcription or comment. Neighbours R1135-R1140: images only (see the R1139 log).
- **Contemporary decipherment.** None: no gloss over the twelve cipher lines, no slip, no copy in the 1519-20 file
  (the 1882 b/c copies belong to the 1519 two-tier letters, `../caprile1519/NOTES.md`).
- **Print.** Somogyi 2025 does not treat this letter's cipher (she prints only R1138/V1920); she mentions the 2,000
  ducats lent to Ippolito "1520. március elején" from Bakócz, which is the period, not this text. The MTA copies omit
  the cipher. No edition known.
- **Vestigia.** V1876 = this letter (images in the main checkout `targets/caprile1519/img/v/v1876_*.jpg`): same leaf.

The reading has to come from the figures.

## 2. Reading on the image

The cipher block (IMG_R1136_I5740_P1, x 860-2960, y 900-1880) cut into quarter-line strips at 2x with the contrast
stretched (`b18_caprile_lines.py`, CUTOFF=3, line centres y 966-1802 every 76 px), checked against `r1136_pass4.txt`
line by line (L01-L06 strip by strip; L07-L12 against the decode at the breaks). The ink is pale brown and a stain
covers the left third of L01-L03; the pass-4 labels hold where the strips are clear, and **no label was changed** (so
no corrections file). Per-token decode with `b18_caprile_beam.py`.

New words at key values over pass 4/5: "a in gran presia […]amato a Buda, et dicono eser conclusi" (L04: "a Buda" is UT
D o PSI T, D = b, o = u; pass 4 had "[..] dicono esser conclusi"), "et l'altro in titulo" (L07), "par questa via" (L09,
EL = p), "secondo patrone", "e vedrò intendere il" (L11).

Proposals not adopted (same table as R1139): 4 = e (L05 "4 p y HH B" = "e nemi…", L10 "QB 4 x ss" and L12 "4 Z AMP ss"
give no word); "1 7" = ve (L06 "cosi [17] ne tenir" would be "così ve ne tenir", but the value fails in R1139 L01).
"[…]amato" in L04: o o σ T HH q h oSLo; "chiamato" would need c-h-i where the signs give b/h-h/s-a.

## 3. Alignment

Each word of `R1136_reading.md` set against its signs (word-by-word groups in its "Notes on the figures"). Bracketed:
[?Asi] (8 T n+ B), [?altro] (RC for r), gu[…]ernator (Z), […]amato, vo[…]stra (an f with no place), su[…] (m+ a o RC),
[?ma] (K). No unbracketed supplied word.

## 4. Score and decision

`b17_score.py` (body only, it): **0.0 (0 of 9 sentences)**, holes 0.37; 0.0 also counting only explicit holes. Every
sentence has two or more unread stretches. **Stays decoded, not read**; kept as a partial reading.

## 5. What stops it (blockers)

- L01-L03 left third under the stain (about six signs, "#" in the transcription) — **illegible**.
- The rest: the signs are legible at 2x, but the stretches that do not read turn on signs whose value key21 cannot
  settle (QB/8, c/CE/e, AMP/EL, the sign 4, 1 7, o o before σ). The five texts in this key (R1136, R1138, R1139, V1920,
  V1921; Vestigia's cipher-flagged records of the file, checked 2 Oct 2026) are all used; the look-alike table and the
  pen-shape study (pass 5-6, 3 Oct) found no consistent split, and this pass found no value that holds across every
  occurrence — **no-key-material**.

Before → after: 0.0 (`beam21_r1136_pass5.txt`, 0/7) → 0.0 on the reading body (0/9).
