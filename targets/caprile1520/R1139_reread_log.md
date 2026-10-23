# Re-reading log, R1139 (22-23 Oct 2026, Claude Opus 5.5; REREAD_BRIEF, batch b18)

## Starting point

Reading audit (22 Oct): "decoded, not read". The pass-4/5 decode (`beam21_r1139_pass4.txt`) was unspaced with
[..] holes in most of its ten lines; 89.7 % of decoded letters fell inside claimed phrases, but the phrases did not
join into sentences.

## 1. Is there a text already?

- **DECODE.** Record page and every linked file re-fetched with the project cookie on 22 Oct 2026
  (`research/reading_audit/b18_caprile_fetch.py`, images to the session scratchpad only): R1139 has three page images
  (I5751 letter, I5752 slip, I5753 address) and no attachment, transcription or comment. The neighbours R1135-R1140
  (fetched the same way) carry only images; R1138 is the 16 Feb 1521 letter Somogyi printed; R1137 is Cistarelli's
  figure cipher (another key); R1140 is outside this key.
- **Contemporary decipherment.** None on the slip, the letter or the address leaf. The clear end of the slip
  ("Expettarò sino a S. Georgio se venisse messo o commissio de V. Ex.a, poi mi aviarò verso Italia per far
  reverentia a V. Ex.a ...") follows the cipher but does not repeat it.
- **Print.** W. Somogyi (2025) prints only the 16 Feb 1521 postscript (R1138, Vestigia 1920); her article quotes no
  cipher of this slip (full-text search of `../caprile1519/lit/somogyi2025.pdf` for the date, custode, rejtjel: the
  only cipher passages she deciphers are R1138/V1920). The MTA 20th-century copies (MTA Ms 4999/2) omit the
  cipher passages (her n. 48). No other edition known.
- **Vestigia.** V1922 = this letter; images already in the main checkout (`targets/caprile1519/img/v/v1922_*.jpg`); same
  leaves, no gloss.

So the reading has to come from the figures.

## 2. Reading on the image

Each cipher line cut into quarter strips at 2.2x of the native 3240 x 4320 image (`b18_caprile_lines.py`, line centres
y 2140-2770), compared sign by sign with `r1139_pass4.txt`, then decoded with key21 per line, each token's value printed
(`b18_caprile_beam.py`). Five labels corrected (`R1139_corrections.tsv`, file `R1139_transcription_b18.txt`): p+ in
L03, q+ in L04, EL for CE and D for B? in L05, "q+ PHI o 1 1" for "q? PHI o #" at the end of L07.

Key values: nothing new adopted. Used only values already in key21 or its counts, chosen per occurrence where the
sign is a known homophone: f = f in "fa", "ferma", "fato" (key21_counts f: t 14, f 3); QB = t in "fato" (QB: o 20,
t 4); t (isolated cross) = s in "dise" (t: s 5); D = b ("bel belo", as "Bachiensis" in R1136); K = et; o o = b.
Proposals tested and NOT adopted because they fail elsewhere:

| proposal | where it works | where it fails |
|---|---|---|
| 4 = e | L01 "com[4]" = come; L02 end "[4] credo" | L01 end "de 4 8 1 7" gives no word; R1136 L05, L10, L12 give none either |
| 1 = v (minim) | L05 "in [1]ero" = in vero; L07 end "1 1" could be u | "1 7" (L02, R1136 L06) gives no word with any 7 |
| 1 7 = ve | R1136 L06 "cosi [17] ne tenir" ("così ve ne tenir"), R1139 L02 "o[17]rnala" (governala, g missing) | L01 "de 4 8 1 7"; needs a g that is not written in L02 |
| CE = p | L09 "in [p]resto" | CE = o in 72 occurrences (pass 5) |

New readings from the strips, all at key values: "bel belo li go fato moto" (L05-L06; was "[..] li go fato"), "et se i
bisionran danari in [?presto], per andar ve ne darò" (L08-L09; "bisionran" as the figures spell bisogneranno), "il
custode, quando a Buda" (o o = b), "a si tenuto Agria in oficio", "et cosi la venuta sua in Italia, [?a] de che vi
scrivi, qua[…] li teneva per ferma, è andata in [?vero]".

## 3. Alignment

Every word of `R1139_reading.md` was set against its signs (the "Notes on the figures" list there gives the sign
groups word by word). Words the signs do not fully carry are bracketed: com[?e] (4), [?E] (4 c), [?ato] (q K CE), [?ci]
(one i for "ci in"), [?a] (q+), [?vero] (1), [?a] before Alfonso (an extra q), [?te] (f ss), [?presto] (CE for p), [?e]
(c), tut[o] (the o is not written). No unbracketed word is supplied.

## 4. Score and decision

`b17_score.py` (body only, it): **0.18 clean (2 of 11 sentences)**, holes 0.21; 0.45 when only the explicit holes are
counted (HOLES=1), since the checker's Italian word list does not know the Ferrarese forms (go, belo, meser, scrisi,
reportarò). Below the bar (0.60): **stays decoded, not read**; the reading is kept as a partial reading.

## 5. What stops it (blockers)

- "4 8 1 7" (L01) and "1 7" (L02): figures with no key value; tested as letters and as numerals (pass 5) and as the
  proposals above; no code list exists — **no-key-material**.
- Single-occurrence signs p+, q+ and the sign 4 (six occurrences in two letters): the only texts in this key are
  R1136, R1138, R1139, V1920 and V1921 (Vestigia's cipher-flagged records of the file, checked 2 Oct 2026), all already
  used; nothing settles them — **no-key-material**.
- L02 "per […] io [17] […]", L03 "a le ma […] custode", L07 end "q+ PHI o 1 1" and L08 start "[…] Milan […] andiate": the
  signs are legible and labelled; the values that would make words are not in the key (the same signs 4, 1, 7, q+) —
  **no-key-material**.
- L10 end of the cipher: one sign into the clear text — **illegible**.

Before → after: 0.0 (`_check_reading.py` on `beam21_r1139_pass4.txt`, 0/6) → 0.18 on the reading body (2/11); 0.45 on
explicit holes only.
