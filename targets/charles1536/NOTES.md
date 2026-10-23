# Charles V to the Empress Isabella (1536) and to Prince Philip (1543), AGS Estado (DECODE R9957, R9952) — NOTES

Status: in progress. Both letters read on 23 Oct 2026 (re-read b18, below); the write-up (page, ledgers) is still to do.

**22 Oct 2026, reading audit** (George Lasry's test): R9957 is here only as fragments of its contemporary decipherment (pp. 17-18; Luo's 2021 print not copied) and R9952 has no text at all; both are *decoded, not read*. Class already solved is kept because R9957 is in print (Luo 2021, p. 287).

**23 Oct 2026, re-read (REREAD_BRIEF, batch b18).** Both letters now read (`texts/`; log `texts/R9952-R9957_reread_log.md`).
- **R9952** (Cremona, 19 June 1543): the contemporary decipherment on ff. 13-14 bis ("del Emperador a Su Al.", images
  P12-P18, P20) transcribed line by line (`texts/R9952_decifrado_ff13-14.txt`) and checked against the figures of ff.
  10-12: the clear words left inside the cipher runs and Tomokiyo's code words (go para, pi enemigo, xu dinero) all
  stand where the decipherment has them; the figures' "dexandolo" is followed over the decipherer's "dexando". Reading
  `texts/R9952_reading.md` (0.683 clean sentences; 1.00 on explicit holes), English `texts/R9952_en.md`. It is the
  Farnese offer made through the Marqués del Vasto (two million in gold and a census for the investiture of Milan to
  Ottavio Farnese), the arguments for and against, a loan from the Duke of Florence and the barons of Naples, and
  orders to Andrea Doria against the Turkish fleet.
- **R9957** (Borgo San Donnino, 17 May 1536): the cipher runs of ff. 270r-273v read sign by sign from the images under
  the key AGS Estado leg. 1.1.1 doc. 169 (Luo 2021 pp. 603-606; `texts/R9957_key169.md`), in three run files
  (`texts/R9957_runs_A.md`, `_B.md`, `_C.md`: signs, decode, comparison with Luo per run); the last passage from the
  contemporary decipherment on f. 274r (`texts/R9957_decifrado_f274.txt`). Luo's edition (pp. 287-290, in copyright,
  PDF in the main checkout `targets/caracciolo1537/prior/luo2021.pdf`) used only as a check, cited, not copied; 14
  places where the figures differ from her text are followed, and "Gonçalo de Ayora" (stamp 0005) is cipher she prints
  as clear. Reading `texts/R9957_reading.md` (0.629 clean sentences; 0.953 on explicit holes), English `texts/R9957_en.md`.
  The superseded first-pass transcriptions `trans_p1-9.txt`, `trans_p10-18.txt` are kept for the record.

Earlier status (before the 22 Oct 2026 reading audit): no write-up

**Verdict: both letters were already read. R9952 was deciphered at the time. R9957 was deciphered and printed by
Wanruo Luo (2021) from its original key.** Catalogue entry 199 ("Charles V (Burgos) to Isabella of Portugal /
Prince Philip, 2 ciphertexts") is resolved and removed. Checked in one session on 2026-09-21.

## The two records are two unrelated letters

| record | shelfmark | what it is | DECODE status |
|---|---|---|---|
| R9957 | AGS Estado leg. 496, ff. 270–274 (18 images) | Charles V to the Empress Isabella; clear text with long cipher passages. Dated at the end "Del Burgo de Sādonyn a xvii de Mayo de MDxxxvi", signed "Yo el Rey". | Non-decrypted |
| R9952 | AGS Estado leg. 59, ff. 10–14 (20 images) | Charles V to Prince Philip, Cremona, 19 June 1543 (docket f. 10: "Cremona ... al Príncipe ... del Emp.or a xix de Junio 1543") | Partially decrypted |

- **Place and date of R9957.** "Burgo de Sādonyn" is **Borgo San Donnino** (now Fidenza, near Parma), on the
  Emperor's road north from Rome in May 1536. It is not Burgos. The date line reads xvii (17) May. DECODE gives
  8 May, and Tomokiyo gives 18 May. The catalogue's "Burgos, Spain" comes from DECODE's origin field.
- **R9952 was never an Isabella letter.** Its DECODE note ("Correspondence between the emperor and the empress
  … 1531 and 1532") was copied across the leg. 496 batch.
- **Image order.** R9957's DECODE images are out of archive order. The stamps give P4 = 0005, P5 = 0007,
  P6 = 0006, P7 = 0008, P8 = 0011 and P11 = 0004; scan 0010 is P10. The cipher runs on in stamp order.

## Prior solution (the contamination question)

- **R9957.** Tomokiyo, cryptiana "Spanish ciphers during the reign of Charles V", update section on Luo (2021)
  (copy in `targets/vasto1527/prior/spanish2C_now.htm`): "Charles V to Isabelle de Portugal, Burgos, 18 May 1536,
  AGS,EST,LEG,496,270-274. DECODE R9957. Deciphered and printed in Luo (2021) p.287. The cipher used is AGS,
  Est. Leg. 1.1.1 doc. 169."
  - Source: Wanruo Luo, *El lenguaje cifrado de Isabel de Portugal (1530-1539)*, doctoral thesis, Universitat de
    València 2021 (dir. Júlia Benavent), RODERIC.
  - The key (AGS Estado leg. 1.1.1 doc. 169) was used between Isabella and Charles V in 1535–38. It combines a
    homophonic alphabet, double letters and syllables (base sign plus vowel stroke, or the numbers 32–91), code
    figures 92–211 and graphic signs. Dotted signs and numbers from 212 up are nulls.
  - Found here after a partial transcription and a failed alignment attempt (below). The existing reading was not
    used to solve anything here.
- **R9957 was also partly deciphered at the time, inside the letter.**
  - p. 16 (scan 0016) has two interlinear glosses: "quatrocientas o q[uinient]as lanças d'armas" and "los arneses
    y las cubiertas".
  - The lower half of p. 17 and the top of p. 18 hold a decipherment, in a rapid second hand, of the long cipher
    passages on pp. 16–17. It covers the German troops (25–30,000 men for Italy, more to be raised in Germany and
    Flanders), the Count of Nassau and "nuestro mayordomo" entering France from the Luxembourg side, and the
    diversion of the French King's forces. The clear phrases "que ninguna cosa puede ser mas provechosa que" and
    "juntamente con lo q", left in clear inside the cipher, recur in it.
  - The cipher on pp. 1–14 has no decipherment on the leaves.
- **R9952.** It is deciphered in the margins of ff. 10–12 and fully on ff. 13–14, "del Emperador a Su Al[teza]".
  Its subject is the Farnese offer through the Marqués del Vasto: two million ducats and a yearly census for the
  investiture of Milan for the Duke of Camerino (Ottavio Farnese). Tomokiyo, same page: "Deciphered in the margin.
  The cipher matches Charles V-Prince Philip Cipher (1545)", with additional code words.

## What was tried here before the prior reading was found

1. DECODE metadata and all 38 images fetched with the saved cookie (`img/`, git-ignored; not public domain).
2. Two transcription subagents (`trans_p1-9.txt`, `trans_p10-18.txt`). These are first passes: glyph naming was not
   unified between them, two "4" shapes were merged, and on pp. 3–9 and 13–14 they read from reduced views.
3. Crib alignment: the p. 16–17 cipher against the p. 17–18 decipherment and the two p. 16 glosses, with the hard-EM
   aligner from `targets/balbases1677/align2.py` (`align.py`, `tx/`).
   - It did not converge: the sign tables came out random.
   - The ratio of about 1.5 plaintext letters per transcribed token fits the doc. 169 syllable system.
   - The token boundaries in the transcription did not match the system's signs (base sign plus vowel stroke;
     numbers 32–91 as syllables).
4. Literature check (`targets/vasto1527/prior/spanish2C_now.htm`) found the Luo reading and the key's shelfmark.

## If anyone reopens it

Luo's key (AGS Estado leg. 1.1.1 doc. 169, her p. 603) and her edition (p. 287) are the starting point. The
transcriptions here are not good enough to check her reading sign by sign.

## Remaining gaps

- R9957: run 1 (a tear after "bien de"; "se [?gra…] e"), parts of the dense blocks B25 and B28 (stamp 0011), a faded fold in run C2 (stamp 0013), a tear in run C5 (stamp 0014) - blocker: illegible
- R9957: run B16 (stamp 0009, about 14 signs, no sentence under the key; Luo prints no cipher there), two figures with no value in run C2 ([43], [6]), the sign 7° and the 52/53 value in dinero - blocker: no-key-material
- R9952: "paresce […]" (f. 13 bis v) and the last word after "scripto" (f. 14 bis r) - blocker: illegible
- Closed 23 Oct 2026: R9957 Luo's text not in the repository (now read from the figures and the f. 274r decipherment); R9952 decipherment not transcribed (now transcribed and read)

## Escalation

- [x] siblings: R9952 and R9957 separated (two unrelated letters)
- [x] clear-pages: R9957 pp. 16-18 glosses and decipherment found; R9952 ff. 10-14 decipherment found
- [x] known-keys: Luo's key AGS Estado leg. 1.1.1 doc. 169 identified
- [x] print: Luo 2021 p. 287 (R9957)
- [x] key-rebuild: crib alignment on pp. 16-17 did not converge (21 Sept); not needed: the original key doc. 169 (Luo pp. 603-606) read the runs (23 Oct)
- [x] retry: 23 Oct 2026 (b18): R9957 read from the figures with the doc. 169 key and the f. 274r decipherment; R9952 ff. 13-14 transcribed and read
