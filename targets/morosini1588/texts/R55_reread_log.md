# Re-reading log, R55 (22 Oct 2026, Claude Opus 5.5; REREAD_BRIEF, batch b00 helper)

## Starting point

Reading audit (22 Oct): "decoded, not read". `R55_decryption.txt` (DECODE D1719 under Meister no. 40) gave the gist
(Soissons captured, the King's movements) with garbles in most lines; `_check_reading.py` 0.588.

## 1. Is there a text already?

- Clear heading on 516r as transcribed by DECODE: "Molins a gl XI di Giugno 1589".
- DECODE "cleartext" images D1089, D1105 (contact sheet): a covering letter in clear and its address leaf; no
  decipherment, no interlinear glosses.
- Rome's decipherments (Francia 27) are not imaged; Tempesti has the capture of Soissons only in outline.

## 2. Hand re-parsing (R55_corrections.tsv)

About one word in seven re-parsed, nearly all carried by the figures: con tuto che, duplicati, Renes, auanzare,
Chate[au]giron (where Soissons was in fact captured, June 1589), Mercurio, "la morte del conte di …", barili, fauila,
"cadè et acese", "restò arso", Charteres, Bogianci, baricate, spauento, "mi ha deto", Suizeri, San Gian di Lona,
Casimiro, "il duca d'Epernone" (DECODE dot on the wrong figure of 129; decoder "il re per non e preso"), Montereo
Faultiona (Montereau-Fault-Yonne), "Giorgio da Uoi, normando", "io non lo tengo tuto per uero".
- A new observation for the key: "8 9 8" (three times) and "8 0 8" (twice) stand between sentences; they carry no word
  and look like a separator (a figure between null 8s). Worth checking on the other Moulins letters.
- No image check was needed.

## 3. Alignment (reread_b00_align.py)

`TOTAL R55: 385 words, 0 supplied, 1 partly` after two spelling fixes (acese, trouaua as the figures give them).
516v: 1144 of 1151 figures used (the unparsed last line).

## Result

Before: 0.588. After: 0.727 on the "## Reading" body (391 words). By hand: 5 unread stretches, 4 partly carried words,
3 supplied letters/words in about 385 words. Grade A: the sentences hold throughout; holes are the opening, one clause
on 516r l. 19–20, a name, and the closing line.

## Still open, and why

- 516r l. 3 opening; the clause "[…] che la disfata a Charteres … d'Umena […]" (516r ll. 19–20: the verb is not
  carried); the count's name "Santignan?" (516r l. 16, first figure uncertain); the closing line 516v l. 17. Not checked
  on the image (no outside blocker); Francia 27 would settle them.
