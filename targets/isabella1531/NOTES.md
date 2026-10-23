# Isabella of Portugal → Charles V, 1531 (catalogue 200; DECODE R9955, R9956)

Status: no write-up. Both letters deciphered at the time; both decipherment sheets transcribed and the letters read here on 23 Oct 2026 (b20), texts in `texts/`.

**23 Oct 2026, re-read (REREAD_BRIEF, batch b20; Claude Opus 5.5).** Every file on DECODE R9955/R9956 fetched with the
shared cookie (scratchpad only). The contemporary decipherments are on the records themselves: R9955 image P3 = doc. 196
(the three cipher passages), R9956 images P4/P8 = doc. 206. Clear text and decipherments transcribed from native-resolution
strips; figures spot-checked against the doc. 112 key printed by Luo (2021) p. 601 ("las necesidades", "despachandose
este correo de mercaderes ... sazon"): they agree. **Both read** (texts/R9955_reading.md, R9956_reading.md, English
`_en.md`, log `texts/R9955-R9956_reread_log.md`). Clean-sentence share of the bodies (b17_score.py, es): R9955 0.744,
R9956 0.714; explicit holes 1.00 for both; before: no text. R9956's address settles the recipient: "Al muy noble señor
mi sobrino Juan Vazquez, secretario de Su Mag.t". R9956 cipher: the Emperor well; Praet gone to France; no answer yet to
the Protonotary Gambara on the council; Siena exiles restored, Spanish infantry kept near; reports of the Turk. Its
decipherment sheet dates the copy "a x[?] de hebrero" against the letter's "a xj de enero de 1531".

**22 Oct 2026, reading audit** (George Lasry's test): no text of R9955 or R9956 is in the repository. Both are *decoded, not read* in profile.json; class already solved is kept (R9955 printed by Luo 2021; both deciphered at the time).

Earlier status (before the 22 Oct 2026 reading audit): no write-up

AGS, Estado, leg. 496 (2 records). DECODE lists both as "Non-decrypted", Isabella → Charles V, Brussels, 1531.

## Result: already read at the time; closed 2026-09-21

Tomokiyo's cryptiana page on Spanish ciphers of Charles V (cached at `targets/vasto1527/prior/spanish2C_now.htm`) covers both:

- **R9955** = AGS Estado 496 ff. 195-196: **Charles V to Isabella, Regensburg, 30 April 1532** (not Isabella to
  Charles, not 1531). Deciphered at the time on a separate sheet, whatever DECODE says. **Printed in Luo (2021) p. 285.**
  Cipher: AGS Estado leg. 1.1.1 doc. 112.
- **R9956** = AGS Estado 496 ff. 205-206: Brussels, 11 January 1531. Isabella was never in Brussels. Tomokiyo reads
  the signature as an abbreviation of "Covos Comendador Mayor" (Francisco de los Cobos). The addressee is "muy noble
  señor sobrino", probably Juan Vázquez de Molina. Deciphered at the time on a separate sheet. Cipher: the same
  general cipher, leg. 1.1.1 doc. 112.

Nothing to add. Images not viewed this session (the literature check came first, per the charles1536 lesson). The
catalogue entry is removed and the DECODE corrections are queued. Sibling: `targets/charles1536/` (R9957, R9952).

## Remaining gaps

- R9955: Luo's printed decipherment not copied - closed 23 Oct 2026: the contemporary sheet (doc. 196) transcribed instead; Luo cited
- R9956: the contemporary decipherment sheet - closed 23 Oct 2026: transcribed (doc. 206), letter read
- R9956: four doubtful words of the decipherment ([?avise], [?scripto], [?gracias], [?Yo]) and the clear line "De hebrero [...]" after the date - blocker: illegible (cramped abbreviations in the decipherer's hand; the writer's postscript line)
- R9955, R9956: cipher not decoded sign by sign against doc. 112, spot checks only - blocker: not-attempted (not needed for the reading; the key is printed as images in Luo 2021 p. 601)

## Escalation

- [x] siblings: charles1536 (R9957, R9952) is the same general cipher
- [x] clear-pages: the decipherment sheets on the DECODE images (R9955 P3, R9956 P4/P8) transcribed 23 Oct 2026
- [x] known-keys: AGS Estado leg. 1.1.1 doc. 112 (Tomokiyo)
- [x] print: Luo 2021 pp. 285-287 (R9955) checked and cited, not copied; R9956 not in Luo
- [n/a] key-rebuild: deciphered at the time
- [x] retry: 23 Oct 2026, both read from the sheets
