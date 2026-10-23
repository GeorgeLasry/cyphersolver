# Paris nunciature, bishop of Bergamo, 1585–86 (ASV Segr. Stato Francia 18; DECODE R15, R16) — NOTES

Status: read (re-read 23 Oct 2026, b24: R16 read with the whole Ragazzoni nomenclator from Meister p. 324-325, the DECODE record's own attachment D3195). Was: not read (reading audit, 22 Oct 2026).

**Result (withdrawn 22 Oct 2026, reading audit: decoded, not read): read** (R16 0.974 measured, 21 Sept 2026; open: name codes 18/48 and scattered transcription slips; see
Remaining gaps). R15 read before (Lasry); R16 read here with the same F18 key. Write-up: docs/bergamo1585.html.

**23 Oct 2026, re-read (REREAD_BRIEF, b24): R16 read** (`R16_reading.md`, `R16_en.md`, log `R16_reread_log.md`).
The DECODE record carries an attachment no session had opened, **D3195 = Meister p. 324-325**, with the whole
Ragazzoni nomenclator (names; x4+ Cardinale ... denari; stroked x4 Sua Santita, Sua Maesta ...; hooked x6 che, per,
come ...; x8+ quanti, questi ...; struck x0 essendo, non, lettere ... mente, pace; dotted x4 Religione Cattolica,
Catolici, Heretici, Guerra ...): `key_ragazzoni_meister_full.txt`. `decode_with_key.py` also ate the 8 of 84+, 86ꜧ,
80- as a null. New beam decoder `research/reading_audit/b24_bg_decode.py` + 16 labels corrected on the images
(`R16_corrections.tsv`); 29 = et (Meister). "18 and 48" were decoder misparses: 70 + 18 = the Ambassador of the Duke
of Ferrara; "uers·48" is "uerso". The heading reads **7 March 1586** (DECODE: 3). Body 0.757 clean sentences.
Content: Guise tells the nuncio through the Ferrarese ambassador that the King means to make peace with the heretics
once the money from the sale under the bull is in; Guise would take the peace for Metz and money; the clergy's
congregation inclines to appeal to a future council.

22 Oct 2026, reading audit (George Lasry's test: can sentences be built and translated?): **R16 is decoded, not
read**, so the "Result: read" above is withdrawn. The decode with Lasry's F18 key and Meister's nomenclator is one
run-on block, words run together, name tags misplaced, an open group or slip in nearly every clause; the gist follows
(Guise, Metz, the sale under the bull, the clergy's appeal to a council), the sentences have not been built. Class now
not read, method not solved; 0.974 is the share of units with a value, withdrawn as a reading figure.

**Split on 14 Oct 2026** under the one-key rule (George Lasry, 14 Oct 2026): R17 (Francia 18/3), filed in the same
volume but in Meister's key no. 40, moved to [`targets/morosini1588/`](../morosini1588/NOTES.md) (page
`morosini1588.html`, "a different key, with its own page"), with `R17_transcription_decode.txt`,
`R17_decryption.txt` and `R17_words.txt`. Its record is kept below for the history of the entry.

Catalogue entry 242. Checked on 2026-09-21 as part of a sweep of the Paris-nunciature records on DECODE (see
[targets/damiata1624/](../damiata1624/NOTES.md) for the 1625 volume).

## The three records

- **R15** (Francia 18/1, ff. 7r–v): **already read.** Lasry's decryption (DOC D3102) with the F18 key (D3103,
  fixed-length homophonic; "also found in Meister p. 324 and in the French book, Ragazzoni"). Nothing added.
- **R16** (Francia 18/2, f. 206r–v; cleartext heading "3 di Marzo 1586"): **decrypted here, in part.** DECODE's
  decryption file for R16 (D3104) is byte-for-byte the R15 decryption (19,639 bytes, same text), attached to the
  wrong record, so R16 had never actually been decrypted. The F18 key (D3105, same as R15's) applied to the DECODE
  transcription D1610 (TimB) with `decode_with_key.py` gives readable Italian at once: 1,410 letter pairs, 66
  unknown (transcription slips and phase breaks). Output in `R16_decryption.txt`.
  Content: *hoggi il [58] mi ha mandato a dire … la bolla … la congregatione del clero … mal contenti dela
  concessione dela bolla … l'alienatione … appellarsi ad futurum concilium …* — the French clergy's resistance
  to the papal bull permitting the alienation of church property, 1586.
  **Nomenclator (same day):** Meister p. 324 no. 2 prints Ragazzoni's 1583 Paris key, the same letter alphabet with
  its nomenclator (OCR in the main checkout's `targets/vatican5/meister.txt`, ll. 59655–59920; realigned in
  `meister324_nomenclator.txt`). Added to the decoder with a one-digit resync for transcription slips: unknowns fall
  from 66 to 18. Confirmed by context: 26¸ che, 36¸ per, 28+ questi, 98+ essere, 20- non, 0^. con, 34 Re
  Christianissimo, 58 Duca di Guisa (who asks for Metz), 14 Nostro Signore. **Not confirmed:** 18 and 48 (Meister's
  Ferrara/Parma) turn up where no duke fits; the 1586 table may have moved them. The letter: Guise will not let the
  King sell church property under the bull unless he gets Metz and money; the clergy's assembly means to appeal to a
  future council, hoping for the Pope's help.
  **Open (was):** about 20 nomenclator codes marked with a cedilla, + or – (26¸, 28+, 36¸, 20-, 58, 34, 70, …) are
  not in Lasry's key. 26¸ behaves like *che*, 20- like *non*, 58 is a person (probably the King or a prelate), 34
  another (probably the Pope). Filling them needs context work or Meister's full table.
- **R17** (Francia 18/3, ff. 233r–235v): **moved to morosini1588 on 14 Oct 2026** (different key). Record of 21 Sept: Meister p. 393 no. 40 (Morosini, 1587), already
  keyed in `targets/morosini1588/decrypt.py`, reads DECODE's transcription D1611 on all five pages with 5 unknown codes:
  the Duke of Lorraine and Guise, the German reiters, the Queen Mother, Schomberg (`R17_decryption.txt`). So R17 is
  a Morosini-period letter (1587–88), not Bergamo/Nazareth. Earlier note: DECODE's key (D3186, ASV F22) is a different system:
  variable-length and *not deterministic* (1–3 digit elements, 8 and 80–89 null). The note says it is incomplete
  and that the full key is Meister p. 393 no. 40. DECODE's decryption file is a Java crash (NullPointerException),
  so R17 had no decryption before this.

## Files

`key_F18_lasry.txt` (DECODE D3105), `R16_transcription_decode.txt` (DECODE D1610), `decode_with_key.py`,
`R16_decryption.txt`. Images are on DECODE (login); not re-transcribed here: the R16 reading rests on TimB's
transcription.

## Remaining gaps

- R16 '[?futurum]' (futu + a dotted 3 and 9) and the last eleven digits of f. 206v - blocker: no-key-material; not in Meister's table, no word
- R16 five letters on look-alike digits (si [?e], [?ocorendo], [?l'aleenatione], [?fata], [?vedo]) - blocker: illegible; the writer's 5 closes like an 8, his 7 takes a hook
- closed 23 Oct 2026 (b24): R16 decoded, not read (read); codes 18 and 48 (decoder misparses, not open codes); the ~16 unknown pairs (labels corrected on the images)

## Escalation

- [x] siblings: R15-R17 all opened; R16 decryption file found to be a copy of R15; R17 is in another key (now morosini1588)
- [x] clear-pages: 23 Oct 2026 - R16's attachments D984-D987 are the clear covering letter of 7 March 1586 ('con cifra duplicata'), not a decipherment
- [x] known-keys: Lasry F18 key (D3105) and Meister p. 324 no. 2 (Ragazzoni 1583) fit R16; Meister p. 393 no. 40 (Morosini) fits R17 only
- [x] print: Meister 1906 key tables used; no printed decipherment of R16 sought beyond Meister
- [x] key-rebuild: 23 Oct 2026 - not needed: the whole nomenclator is Meister p. 324-325 (DECODE attachment D3195)
- [x] retry: 23 Oct 2026 - slip positions re-read on the images (16 labels), beam decoder b24_bg_decode.py

## Assumptions for George's review

- Credit: George is credited here with the F18 key (D3103/D3105) and his R15 decryption (D3102), which his DECODE
  files document; R16 is read with that key. His R18 file for Morosini's key (D3175) and his F22 note on R17 (D3186)
  belong to the Meister no. 40 entry, `morosini1588`, not here.
