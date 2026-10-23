# HCPortal 496 (HStAM 4 h Nr. 1411, f. 3), Malsburg to the councillors at Kassel, 5/15 Jan 1637 — reading of the cipher

Rests on: `f003.txt` (Bourdeau's hand transcription of f. 3, one cipher line per scan line) decoded with `key.txt`
unchanged (`research/reading_audit/b08_dec.py`), the breaks checked on the HCPortal original scan
(hstam_4_h_1411_0003, 2946 x 2312, fetched 22 Oct 2026 into the session scratchpad; batch b08). No contemporary
decipherment on the leaf or the address side (f. 4), no clear copy, no edition (NOTES, Escalation). Code values:
`{Cöln}` = 128 (grade I, from context, `codes.txt`).

State (22 Oct 2026, batch b08): **read** (B); clean-sentence share of the reading body 0.667 (`research/reading_audit/b05_score.py`); holes: open codes and signs. Log: `HCP496-509_reread_log.md`.

Conventions: `{...}` a code with a context value; `[201]` an unvalued code; `<+>` an unvalued sign; `[?word]` partly
carried; `[word]` supplied; `[…]` unread. Spelling as the cipher gives it: the b08 normalisation (`research/reading_audit/b08_norm.py`) was undone on 23 Oct 2026 (batch r2b, `research/reading_audit/r2b_mals_denorm.py`: each word restored to the form its figures or the transcribed clear words give, e.g. alhir, Feint, schleinig, hette, dan, one); modern spelling only in the English file. Punctuation added. ⟨...⟩ = clear words written in the letter around the cipher.

## Reading

⟨… gemachet,⟩ das ich auch noch nit weis, wo hervor unsre Garnisonen hirnechst der Unterhalt her, so in Frucht ⟨und⟩ [201] bestehet, genommen werden soll; ⟨das⟩ die Contributiones vom platten Lande sowol alhir als in [239] ein Ende haben. ⟨Und⟩ wirt man nunmer alle Monat auf <+> [?…]tman [193] ⟨und⟩ <f> [273] an [210] zwölf <4#> Virtel casselische Virtel; weill die Unterofficirer duppelt Commis bekommen ⟨und⟩ [144] […] haben.

Es ist noch Zeit, das man sich beim König von Ungern angebe wegen der Fridenstractaten ⟨und⟩ salvum conductum vor <H#> Gesanten nach {Cöln} sollicitire. [176] wirt one [140] nit anfangen zu tractiren. Auf disem itzigem Zug [?steet] gar biel; derowegen Bettage hoch [?nötig] sein.

## Notes

- The first block follows the clear words "… gemachet," and ends before the clear sentence "Es sitzet auch itzo ein
  Capitain vom feind Doctor …"; the second block is the postscript written under "Der Herren Dienstwilliger".
- "unsre": the figures give u n P(ss) 13 r e (`unssre`); 13 is clear on the scan, so the writer doubled the s.
- "bestehet": `91 49 O 6? / 82 84 94` = be st ? / het; the group cut at the right edge of the line ("6?") must be an
  e-group (16 or 61), so the word is carried.
- "her, so in Frucht": the figures give `82 48 65` = her (82 is clear on the scan), not "der".
- `<+> 60 57 87 31` = <+> t m a n: the sign is a cross written like a t-stroke; a "Hauptman" or "Feldman" would need a
  value for it that no other occurrence confirms, so the word is left open.
- `[144] C 25 Y' X 9?`: after the code, a small c (not the capital mm sign), r, a dotted ei-sign, sch and a doubtful 9;
  no word comes out ("…reisch…"), so the clause is a hole.
- `<H#>` (crossed H) gives ll elsewhere; "vor ll Gesanten" is not a word, so the sign is open here.
- "steet": `O 48 7? 61 26` = st e 7 e t; the 7 sits against a blot; "stehet" would need a 72 (h) whose 2 is lost in the
  blot. "nötig": `83 7? 26 36 43` = n 7 t i g; the same 7 stands where ö is needed. One sign cannot be both h and ö, so
  both words are marked partly carried.
- "biel" = viel (b for v, as elsewhere in these letters).
