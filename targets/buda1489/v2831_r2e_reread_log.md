# Re-reading log, Vestigia 2831 p. 1, p. 2 ll. 1-17 and p. 4 cipher lines with the original key (r2e, 23 Oct 2026, Claude Opus 5.5)

## Starting point

Demoted 23 Oct 2026 (v3): p. 1, p. 2 ll. 1-16 and the p. 4 cipher lines scored 0.519 explicit-hole on their numbered
lines (`v2831_reading.md`), read 18-22 Sept with Somogyi's reconstructed key; the original key R5411 had not been
applied to them. No contemporary decipherment, copy or edition exists (b25 log step 1; nothing new found).

## What was done

1. Plates: Vestigia originals in the main checkout (`img/v2831_p1r.jpg`, `_p2r.jpg`, `_p4r.jpg`; DECODE has no record of
   2831 and serves no other negative). Row finder and crops: `research/reading_audit/r2e_crop.py`, `r2e_z.py` (crops in
   the session scratchpad, reread/r2e/). Every cipher line cropped at 1.7x in thirds, doubtful stretches at 2.4-3.5x.
2. Sign strings written line by line with R5411 values (`trans/v2831p1_r2e.md`, `v2831p2_r2e.md`, `v2831p4_r2e.md`),
   each decoded and segmented, look-alike letters and holes counted per line; corrections against the 1989 passes in
   `trans/v2831_r2e_corrections.tsv`.
3. **p. 2 has 31 lines**: its first line ("referto, che questo Zuan Corvino ... se faria lo parentato") was never
   transcribed; old p. 2 L1-L16 are L2-L17, b25's L17-L30 are L18-L31.
4. Key values adopted (each holds at every occurrence on these pages): M+ = Regina (p. 1 L13, L18, L26; p. 2 L12;
   were "[la sua Maesta]"); a# = Vostra Dominatio (p. 2 L08, L10 twice, L11; p. 1 L22; p. 4 L02; were Ex.tia Vostra or
   "ma"); o+ = Imperatore (p. 1 L05, L08; the 1989 "♀"); M̄ = Zuan Corvino (p. 2 L01); x̄ / xo = ma ("ma non tanto",
   "prima", "sapientissma"); ƀ = fa (fare p. 1 L07, p. 2 L14, p. 4 L01; facto p. 1 L23; faria p. 2 L01); bˣ = ni
   (cortesani); nᵒ = pp (lappetito); ƒ = ff (affirmando); q̥ = ri (Federico); q^o = re (dire, recevere, riuscire; not in
   the key, holds at every occurrence, as on R1098).
5. Withdrawn 1989 readings not carried by the figures: "etiam" (p. 1 L12, p. 2 L07), "havuto" (p. 1 L29), "quelle
   coniecture pri[ma] [de]" (now "questi coniecture: prima"), "con lo [Imperatore]" (p. 1 L13: "col Ser.mo Re"),
   "et non tanto" (L03: "ma non tanto").
6. Third pass on b25's lines: p. 2 L28-L29 "per [?messere] Francesco fara replicare el ma[…]" (the first group of L29 is
   Francesco, not "f-r-a-n-o-e"); L20 and L25 checked, no gain. p. 3 not re-cropped in this pass.
7. **Reading** `v2831_r2e_reading.md`, English `v2831_r2e_en.md`; aligned word by word with the per-line decodes,
   supplied words bracketed, the writer's spelling kept.
8. **Score** (`v2_score.py`, it): body **0.642 explicit-hole (34/53)**, plain 0.321, hole rate 0.117 (before 0.519
   explicit-hole). By page: p. 1 0.552 (ll. 1-21 0.70, ll. 22-29 0.22, the stained part), p. 2 ll. 1-17 0.80, p. 4
   0.33 (three sentences). b25 part (`v2831_p2p3_reading.md`) after the third pass: 0.466 explicit-hole (was 0.483 /
   0.542 on b17; sentence count changed with the merge).
9. **Look-alike letters**: 13 letters of about 2,000 (0.7%), well under 3%.
10. **Share of cipher signs read** (first measurement): of 2,338 cipher signs on p. 1 ll. 3-29, p. 2 ll. 1-17 and p. 4
    (nulls excluded), 358 stand in groups not read: **0.847 of the signs read** (p. 1 0.82, p. 2 0.89, p. 4 0.76). p. 1
    ll. 1-2 (Somogyi) are read in full and not in the count. For p. 2 ll. 18-31 and p. 3 only a word-based figure exists:
    hole rate 0.164, i.e. about 0.84 of words.

## Result

p. 1, p. 2 ll. 1-17 and the p. 4 cipher lines: **read** (0.642 explicit-hole; a reader can follow the argument from
the Diet to the Neapolitan ambassador's mission, the Corvinus-Federico match, the courtiers' gibe and Maffeo's advice;
p. 1 ll. 22-29 stay fragmentary under the stain at the right edge, which is the outside blocker). Grade B.
p. 2 ll. 18-31 and p. 3 stay **decoded, not read** (0.466).

## Open

- p. 1 ll. 21-29 right-hand ends: stain (illegible).
- legible groups that do not segment with the full key (p. 1 L04 two -ione words, L11, L12, L22, L24; p. 2 L09, L15,
  L16; p. 4 L02; and b25's list for p. 2 ll. 20-31 and p. 3): three passes done; a fourth with the `lang/` Italian model
  as a segmenter over the decoded strings is the next step (not attempted).
- the o-form (b by the key, t in most words) and the torn X-& columns of R5411: no key material.
