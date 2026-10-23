# Re-reading log, R33 (22 Oct 2026, Claude Opus 5.5; REREAD_BRIEF, batch b00)

## Starting point

Reading audit (22 Oct): "decoded, not read". `R33_decryption.txt` (character model on DECODE's D1697 under Meister
no. 40): the subject clear (the clergy and the Council of Trent) but garbled words in most lines ("terra tolera",
"ognuno di scendendo", "eletore sentio niza in premi"). Clean-sentence share 0.511.

## 1. Is there a text already?

- DECODE images: 8 cipher pages (189r–192v) and 11 "cleartext" images (contact sheet checked; two read in part):
  clear despatches and avvisi of the same weeks (Paris, Savoy, Spanish armada), ff. 188–197. Not decipherments. No
  interlinear glosses on the cipher pages.
- Print: Tempesti, *Vita di Sisto V* (1754) II, book VII §§ XXXI–XXXV (scratchpad OCR ll. 1339–1420) paraphrases the
  letter point by point, including the four reservations and the legate's four arguments. Used for sense only. Rome's
  decipherments (Francia 27) not imaged.

## 2. Word decode and hand re-parse

From `R33_worddecode.txt`; about one word in eight re-parsed by hand (`R33_corrections.tsv`, 94 rows). Causes:
- Decoder's wrong splits on correct figures: "ci uoria" (decoder "uiuo ria"), "dicendo", "non la uogliono",
  "le loro esentioni" (decoder "eletore sentio niza"), "s'ofersero", "aquetarli", "pontiglio d'honore", "onde", "ma anco
  santi", "era honesto", "come madre pia", "guardasigilo", "io risposi", "spontare", "andarò".
- The -mente abbreviation m + 8, twelve times (ultimam., liberam., grandem., ostinatam., grauem., priuatam.,
  ligitimam., specialm., ragionam[ento], distintam., risolutam., compitam.) and "bo. mem.".
- Codes the decoder missed or misread: 135 (dot on the 3), 213 (dot on the 1, twice), 151, 226 (once undotted), 141
  (undotted in "quelli del clero"); "2 1 2^. 6" in "come madre" is a spurious dot.
- About 30 single-figure slips taken from context (tsv "figures+context").

## 3. Image checks (crops, scratchpad only)

- 189r l. 12 and 190r l. 12 (the transcriber's "? ? ?"): holes eaten through the paper by the ink; the figures are lost.
- 192r l. 24 – 192v l. 1 ("a qualche min…"): 192r ends "2 1 2 9 0 2 1 5 0 5 6 2 0 1 7 0 1" as transcribed; 192v l. 1
  has faint figures in the left margin not transcribed; the word stays unread.

## Result

Before 0.511 → after 0.729 clean-sentence share (on the "## Reading" body). By hand: 13 unread stretches ([…]) and
about 15 partly carried words in about 1,540 words; every sentence of the argument carries. Grade B (about 30
figure-context corrections; several holes are physical).

## Still open, and why

- 189r l. 1 (opening), l. 7, l. 8; 190r l. 1 ("[?dui anni]"); 192v ll. 4–5: no word parse of the transcribed figures
  (no outside blocker; a further image pass could close some).
- 189r l. 12, 189v l. 12, 190r l. 12, 190v l. 21, 192v l. 8: holes in the paper (image): blocker = damage.
- 192r l. 24 – 192v l. 1: one word ("min…") not read; 192v margin figures faint.
- 192v l. 9: the closing figures (with 221 lettere) not read.
