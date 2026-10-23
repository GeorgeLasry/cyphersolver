# R1064 reread log (r2q, 23 Oct 2026, Claude Opus 5.5)

**Before.** `R1064.md`, keyed decode of the 13 numbered paragraphs: translation wave v7 scored 0.57 on explicit holes
(§§9-13 do not build); set to decoded, not read. Measured again here on its reading body: plain 0.646 (51/79),
explicit 0.785 (62/79), hole rate 0.072.

**Register copy.** Fagel register, NA 1.10.29 inv. 5186 scans 62R, 63L, 63R, margin "No 136. Dat: 1. Fevrier 1757. A:
à R:". Scans fetched through the NA IIIF server (b32_na_iiif.py, 2400 px); WAINUT's Gemini transcription checked line
by line on all three pages. Two misreadings: 63R "du 10. Janvier" is "du 18. Janvier"; 63L "ou de le taire" is "ou de
Se taire". Otherwise word for word (the dotted deletion on 62R line 21 and the struck "Paris" on 63R are as the model's
notes say). `R1064_corrections.tsv`.

**Alignment.** `wainut/align/R1064.tsv`: 996/1,201 keyed groups at the register's word (0.829; shuffled 0.153). The
non-matching groups were gone through one by one:

Figures followed (another word, every group with a value that holds elsewhere):
- 225-234 au se-ne-cha-l de qui-n-ti-n: "au Senechal de Quintin". The register has "au (-) ne et soit Mr de Quintin"
  (blank, then "ne" and "soit" dotted for deletion and "et" interlined): the clerk did not make out the title. The old
  keyed reading had "au sieur Charles de Quintin".
- 164 point (948): "ne consentiront point"; register "pas".
- 797-798 [125] point: "n'est point un Traité"; register "n'est pas".
- 756 étoit (842): "combien il étoit important"; register "est".
- 920-923 la ta re: "ou de la taire"; register (scan) "ou de Se taire".
- 1203-1205 re [718] rés: "Vous remarquerez"; register "Vous remarqué".
- 1212-1221 re-garde-oit les deux ca-pi-ta[-]ne-s et le chirurgien: "regardoit les deux Capitaines et le Chirurgien";
  the register lacks "les deux Capitaines" and has a dotted "et" in their place.

Register kept (the figure's key value is wrong or the figures have no word of their own):
- 151 1068 (son, 17 matches elsewhere) where the register has "Il est à presumer": a slip in the cipher or a homophone.
- 268 876 (la) at "le même homme"; 469 834 (elles) in "Bel-le Isle"; 460 202 (a) at "vouloir"; 536 642 (nonante, never
  confirmed) at "50"; 543 148 (juste) at "Italien" (147 = italien: a one-digit slip?); 633-634 at "le peux"; 695 749 at
  "donner"; 1018 704 at "Lanzi"; 1041-1042 635 771 at "24"; 1082-1084 978 634 114 at the date (no value).
- Spelling and abbreviation (fortes/forts, chez/ches, Roy, etc.) and the syllable splits of names (Libourne, Coutrai,
  Lowendal, Subtile).

Groups the register passes over (left out of the reading, as the contemporary decipherer left them):
- 317-323 qui [103] il m a [178] cette, between "mais" and "encouragement": a false start in the encipherment
  ("mais ... cet encouragement"), the register has "mais cet encouragement".
- 663 146 (key intelligences, once elsewhere at "lligence") between "je prendrai" and "avec lui".
- 514-515 29 108 ("je" + no value) after "de ses observations." (the old reading "[107] Je [108].").
- 471 878 (le) after "Belle Isle". (516, key j, is i/j: at the register's letter 16 times over the ten letters, e.g.
  "J'aurai", "verrai"; the 16 places with no register letter are the aligner's word-end splits, not extra words.)

**Reading.** `R1064_reading.md`: the register text in its order (the cipher's paragraphs are set out of order on the
pages), clerk's spelling, with the figure readings above; catchword "avec avec" and two line-break splits (l'au roit,
l'in stant) joined; the clerk's two footnotes at the end. Scores (v2_score.py, French): plain 0.764 (55/72), explicit
1.0 (72/72), hole rate 0.006. The 17 sentences under the plain bar fail only on Mr, names (Urvoy, Hatzel, Lacombe,
Orreri, Lanzi, Perieux, Maurepas, Omeri, Coutrai, Perot Imbert, Montaran, Cremille, Orfeüil, Oller), numbers (50, 24)
and the clerk's spellings (paroitront, onereux, aparent, Harang, aujourdhuy, Suplement). No look-alike alternates: the
words rest on the register, the figures checked where they differ.

**Open.** The few groups listed above that the register passes over; the passport date figures 978 634 114 have no key
value (the date is the register's). English: `R1064_en.md`.
