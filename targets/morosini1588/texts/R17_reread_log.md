# Re-reading log, R17 (22 Oct 2026, Claude Opus 5.5; REREAD_BRIEF, batch b00)

## Starting point

Reading audit (22 Oct): "decoded, not read". `targets/morosini1588/R17_decryption.txt` is the character-model
decryption of DECODE's transcription (TimB, Dec 2015, speech recognition; "S" marks a sign that may be 5 or 8) under
Meister no. 40, run together without word division (`_check_reading.py` scores it 0.94 only because the run-together
text gives the checker few word boundaries to fault; it is not a reading).

## 1. Is there a text already?

- DECODE images: 5 cipher pages (233r, 234r, 234v, 235r, 235v; 233v not imaged) and 2 "cleartext" images (ff. 231r,
  232r; contact sheet checked): covering letters in clear signed by the archbishop of Nazareth (Fabio Mirto
  Frangipani), Paris 27 August 1586 and 27 July 1586, not decipherments. No interlinear glosses on the cipher pages.
- Tempesti's *Vita di Sisto V* covers 1588–89 (the scratch OCR); nothing on this enclosure. No print found.

## 2. Word decode and hand re-parsing

`R17_worddecode.txt` from `reread_b00_decode.py`; the decoder gave the sense of most lines. Re-parsed by hand
(`R17_corrections.tsv`, 50 rows):
- Dotted codes with the dot on the wrong figure, which the decoder read as other codes or rejected: 113 written
  "1 1^. 3" and "1^. 1 3" (decoder: [<911?>], 111 il Papa), 166 written "1 1^. 6 6" (decoder: 116 Regina Madre,
  which made "Regina Madre tordine"), 221 "2 2^. 1", 217 "2 1^. 7", 227 "2^. 2 7", 129 "1 2^. 9"; spurious dots on
  letters (519 = t o in "ispedito"; "5^. 6" in qualche and che).
- A code without its dot: 146 (danari) in "trouati danari per pagare".
- Vocabulary gaps where the figures were right: soprema, rinouando, ispedito, saputo, comandaua, ch'ha seco,
  Sciumbergh (Schomberg), Beleure (Bellièvre), pretermeto, inconueniente iremediabile, tre Stati, si uada.
- "Re" spelled in letters (1 153) besides the code 113: "con il Re", "il Re sia per uoltare", "dichiarare il Re".
- The encipherer writes 63 (chi) for che twice (234v l. 2, 235r l. 12): read [?che].
- Image checks (crops, scratchpad only): 233r ll. 1–5 (opening and the paragraph end: transcription confirmed, the
  unparsed groups are on the page), 233r l. 18 ("soprema sua autorità": two 4s the transcription dropped), 234v ll. 2–3
  (63 9 9 confirmed), 234v l. 8 (Sciumbergh), 235r ll. 4–5 ("tanto": 2, not 3; the number before "leghe" unclear).

## 3. Alignment

`python reread_b00_align.py R17 --trans ../../targets/morosini1588/R17_transcription_decode.txt`:
`TOTAL R17: 831 words, 2 supplied, 8 partly`. All ten flags were checked: they are the aligner's handling of codes
with a displaced or spurious dot (persuaso before "9 1^. 1 3"; duo corieri at "2 1^. 7", the plural of 217 not in its
expansion list; qualche at "5^. 6"; tanti before "2^. 2 7"; che at "5 6^."), and the figures carry those words.
"maresciale" was changed to "marsciale" (the figures have no e); "mes[i in] suo" to "me[si in] suo".

## Result

Before: 0.94 on the run-together decryption (not comparable). After: 0.75 clean-sentence share on the "## Reading"
body (hole rate 0.068). By hand: 7 unread stretches ([…]), 5 partly carried words ([?]), 3 supplied pieces, in about
830 words; every sentence of both passages is carried. Grade A-/B: sentences hold throughout; about a dozen
figure-context corrections (tsv).

## Still open, and why

- 233r l. 4 end and l. 5 start (8 0 0 4 4 5 7 0 / 7 0 5 1 4 9 2 1 1 5 0 0): no parse; checked on the image (no
  transcription slip) — the encipherer's slips.
- 234r l. 1 (0 2 7 9 5 0 1 6^. 6 4 1 0 8 before "quanto era stata"): the start of the 234r passage, whose beginning is
  on a page not in the record (233v not imaged).
- 235r l. 5, the number of leagues (1 8 8 4 9 0 0 3 5 1 5 3): unclear on the image.
- 235v ends in mid-word ("che io po…"); the continuation is not in the record.
- Date: the cipher carries none; the record's covering letters are of July/August 1586, the content fits 1587.

## r2p, 23 Oct 2026 (Claude Opus 5.5): every hole checked on the DECODE images

Each hole located on its transcription line (`research/reading_audit/r2p_holes.py`), the line looked at on the image
(IMG_R17_*, scratchpad `reread/r2p/crops`), cancellation strokes looked for (none on these pages), the figures parsed
under Meister no. 40 (`r2p_parseall.py`, the `r2d_mparse.py` enumeration).
- 233r l. 1 opening "4 5 1 9 1 8" (as transcribed): so / sto / sero; the first figures of the page, no context fixes a
  word. Blocker: too-short.
- 233r l. 4 end "8 0 0 4 4 5 7 0" and l. 5 start "7 0 5 1 4 9 2 1 1 5 0 0 8": as transcribed; l. 4 ends in a
  paragraph rule after them. Best parses "gsppertratr", "gseinpersoatr": no word sequence. Blocker: no-key-material
  (figures clear, no parse under the key: the encipherer's slip).
- 233r l. 11: the image has "8 9 0 1 2 6 5" (a single null 8, then 9 01 26 5): "Onde" is carried and filled.
- 234r l. 1: the image adds nulls DECODE leaves out ("8 0 2 7 9 5 8 0 166. 4 1 0 8 161."). "0 2" (m) ends a word begun on
  the missing leaf (233v not imaged) - blocker: needs-physical-access; "5 8 0 166. 4 1 0" between "come" and "quanto"
  parses only as l/en + questo + sn/hn - blocker: no-key-material.
- 234r l. 11 "[?danno]": the image has a null 8 before it, "8 2 6 3 1 0 1 9" = d u n con/r o: d and n carried, the rest
  is not; kept partly. Blocker: no-key-material.
- 234v l. 2 "[?che]": "8 6 3 9 9" = chi quando as written; kept. 234v l. 4 "me[si in]": "2 0 5 | 4 3 7 9" = me, suo; the
  rest of mesi and the preposition are not written; kept. Blocker for both: no-key-material.
- 235r l. 4 "[uenire]": nothing written between "modo" and "esendo" (looked at); supplied, kept.
- 235r l. 5, the number of leagues: the image reads "2 1 8 8 4 9 0 0 5 3? 7? 5 3 8" before "50 35 40 14 5" (leghe) and
  disagrees with DECODE ("8 4 9 0 0 5 1 5 3") in the crowded middle; no parse either way. Blocker: illegible.
- 235r l. 6 "qu[i]": "8 9 6 8" = que between nulls (96 for 97 qui); kept partly. Blocker: no-key-material.
- 235r l. 11 "[?la]": the image has "8 5 2 1 2" = null 85, a: only the a of "la" is written; kept partly.
- 235r l. 12 "[?che]": "6 3" = chi as written; kept.
- 235v l. 21 "po[…]": the last figures of the page "8 7 0 9 1" = po; the letter goes on beyond 235v (not in the record).
  Blocker: needs-physical-access.
Result: 1 hole filled (Onde); 14 left, each with its blocker.
