# Morosini (nuncio, then legate in France) to Rome, 1587–89: the Meister no. 40 key — READ

Status: in progress

**23 Oct 2026, re-read r2d (Claude Opus 5.5):** R27, R35, R51, R57 regraded on the v2 measure
(`research/reading_audit/r2d_score.py`: reading body only, every `[?word]`, supplied word and unread stretch a hole).
Explicit-hole share R27 0.84, R35 0.84, R51 0.97, R57 0.85; the plain score (0.48-0.58) only reflects the clerk's single
consonants, which the word list does not know and which are not modernised, so for these 16th-century texts the
explicit-hole share is the bar. Read sentence by sentence they hold: **all four now read**, so every enclosure reads
(fraction_read 1.0, measured). The DECODE attachments were re-opened: R27's and R51's "cleartext" pngs are an address
leaf, a Latin letter and a clear covering letter, R35 and R57 have none; no decipherment. Holes checked on the images:
R27 137r l. 13 and 137v l. 3, R51 466r l. 3 (figures as transcribed) and 466v l. 8 (now read: "la quale, che so, non
era ancora montata"), R57 524r ll. 14-15 (as transcribed), R35 202v ll. 8-9 (a hole in the paper at "si [...]").
`research/reading_audit/r2d_mparse.py` enumerates the parses of a run of figures under Meister no. 40 for such checks.

**22 Oct 2026, re-read (batch b00, REREAD_BRIEF; Claude Opus 5.5 with six helpers):** 34 of the 35 enclosures now
read as sentences and are translated (`texts/<R>_reading.md`, `_en.md`, `_corrections.tsv`, `_reread_log.md`); R35
(the Spanish memorandum) still has too many holes. Method: a word-level decoder with a transcription-slip model
(`research/reading_audit/reread_b00_decode.py`, output `texts/<R>_worddecode.txt`), then every break re-parsed by hand
on the transcribed figures and, where a figure was in doubt, on image crops (`reread_b00_crop.py`; DECODE images via the
cookie, kept in the scratchpad), and each reading aligned word by word with its figures (`reread_b00_align.py`), with
every word the figures do not carry bracketed. What garbled the old decode: spurious nomenclator dots in DECODE's
transcriptions (250 = "Bles" in letters, 150, 214, 712 ...), real codes with the dot on the wrong figure or none, the
clerk's -mente abbreviation (m + null 8), numbers in plain figures between null 8s, single 8 as a null, and page order
(R30, R31, R43, R45, R47). No new code value. No contemporary decipherment on the DECODE images (the "cleartext" images
are covering letters); Rome's decipherments are in Francia 27 (Hübner 1870), not imaged; Tempesti 1754 paraphrases
many letters and was used for sense and names only. R35 is the Spanish ambassador's memorandum to the Queen Mother,
not a letter of Philip II. Class not read -> read in part; method -> read with known key; fraction_read measured
on items of the enclosures that read.

**22 Oct 2026, reading audit** (George Lasry's test: can a reader build coherent sentences and translate them?):
all 35 enclosures (R17-R58) are **decoded, not read**. The decode (Meister's key on DECODE's volunteer transcription)
is lowercase word-split output with garbled words in nearly every line; the gist follows, sentences cannot be built
without guessing (`docs/_check_reading.py`: 28-72% of sentences clean). Class read -> not read, method -> not solved
(the known key kept as a part); 0.998 (key coverage) withdrawn as a reading figure. The "Result: read" below is
superseded. Next: re-transcribe from the images where garbles cluster, starting with the shortest enclosures.

Catalogue item 243 (class B). ASV, Segreteria di Stato, Francia 22 ("Francia, card. Morosino, 1588 e 1589",
ff. 10–583, letters 25 July 1588 – 20 Sept 1589). DECODE R18–R22, R27–R49, R51, R52, R55–R58: 34 cipher
enclosures, items 22/1–31 and 22/34–37 (22/29 has no DECODE record; R23–R26 and R50 in the numeric run are other
material: R23 a key book, R24 Cologne 1721, R25 Portugal, R26 Spain 1736). Also R17 (Francia 18/3, 1587), filed
with the Bergamo/Nazareth despatches but in this key.

**Split on 14 Oct 2026** under the one-key rule (George Lasry, 14 Oct 2026):
- R53 and R54 (items 22/32–33, Tours and Moulins, spring 1589), in a second key (DECODE "F22b") that Lasry
  reconstructed in part, are now their own entry: [`targets/morosini1589/`](../morosini1589/NOTES.md), page
  `morosini1589.html` ("a different key, with its own page"). Their transcriptions, Lasry's key files and the
  decoder output moved there; the decoder stays here (`python decrypt.py --f22b`).
- R17 (Francia 18/3, ff. 233r–235v) moved in from [`targets/bergamo1585/`](../bergamo1585/NOTES.md): read on
  21 Sept 2026 with this key (section below).

**Result (19 Sept 2026, R17 21 Sept): read.** All 35 enclosures in this key read end to end with the key printed by
Meister: 0.998 of decoded units have a value (`measure.py`, 14 Oct 2026; letter slips not counted).

## Key

Meister, *Die Geheimschrift im Dienste der päpstlichen Kurie* (Paderborn 1906), pp. 393–394, no. 40:
"Con monsig. Moresino nuntio in Francia. 8 Giugno 1587", signed for by Francesco Sini, secretary of the
Bishop of Brescia (Morosini). DECODE attaches the scan (R18 DOC_3174.pdf) and Lasry's partial reconstruction
(DOC_3175.txt, Oct 2020); Lasry noted "full key in Meister" but no plaintext was posted, and DECODE lists the
records as "partially decrypted".

- Letters, homophones of 1–3 digits: a 21 212 2, b 24 42, c 25 52, d 26 62, e 35 153 5, f 30 03, g 40 04,
  h 41 14, i 17 171 7, k 60 06, l 50 05, m 20 02, n 10 01 0, o 91 191 9, p 70 07, qu 90 09, r 00 13 1,
  s 54 45 4, t 51 15 6, u 37 173 3, x 11, z 12, et 16 69 75, con 19 76 55; clusters cr 22 … tr 49.
- Words: non 61 71, che 56, chi 63, per 64, perche 65, percioche 66, accio 67, acchioche 72, nondimeno 77,
  come 79, ancora 92, ancorche 93, benche 94, qua 95, que 96, qui 97, quando 99.
- Nomenclator, three digits with a dot on the middle one (DECODE transcription `X Y^. Z`): 111 Papa,
  113 Re di Francia / S. M.tà Christ.ma, 116 Regina Madre, 129 Duca di, 131 Cardinale di, 133 Arcivescovo,
  161 quanto, 165 quello, 166 questo, 167 V. S. Ill.ma … 232 il già Re di Navarra (full list in decrypt.py).
- Nulls: 8 with any following digit (80–89).

Because the digits run on with no separators and homophones are 1, 2 or 3 digits long, the text is decoded by
a Viterbi/beam search over segmentations scored by the shared Italian 5-gram model (`lang/`, it-cinquecento,
no spaces): `python decrypt.py` → `decrypt_raw.txt` (per page) and `plaintext_by_record.txt` (per item).

Second key (F22b, R53/R54 only): now `targets/morosini1589/` (split 14 Oct 2026). R35 (22/14) is a Spanish copy of
Philip II's letter to the Queen Mother in this key (Meister no. 40); the Italian model still segments it.

## R17 (Francia 18/3, ff. 233r–235v), moved from bergamo1585

DECODE files R17 with R15/R16 as a Bergamo/Nazareth despatch. Its DECODE key (D3186, "ASV F22") is incomplete,
variable-length and not deterministic, with the note that the full key is Meister p. 393 no. 40; its decryption file
is a Java crash (NullPointerException). On 21 Sept 2026 `decrypt.py`, unchanged, read DECODE's transcription D1611
(TimB, Dec 2015; `R17_transcription_decode.txt`) on all five pages with 5 unknown codes (519, 911, 556, 722, 561):
the Duke of Lorraine and Guise, the German reiters, the Queen Mother, Schomberg (`R17_decryption.txt`; word breaks
by `../bergamo1585/split_words.py` in `R17_words.txt`). So R17 is a Morosini-period letter of 1587, not
Bergamo/Nazareth; the date within 1587 is not fixed.

## Grades

- Nomenclator glosses 113, 161, 165, 166 are H (Meister prints 113 as "Il Re di Francia, S. Mtà Christma";
  165/166 as "quelli/questi", which the text uses as quello/questo).
- Undotted-code reading: H in bulk; single-letter slips (transcription errors, homophone choice) are left as the
  decoder gives them, typically 1–3 %.
- Dotted codes not in Meister's list (e.g. 162, 191, 250, 516, 617, 716, 770): open, most are transcription
  slips of a dotted digit.

## Content

Per-item summaries: `summaries_a.md`, `summaries_b.md`. Highlights: the Council of Trent's publication and the
Gallican objections (Aug 1588); Estates of Blois; the murder of the Duke of Guise in the King's chamber on
23 Dec 1588 and the arrest of the Cardinal de Guise, Nemours, Elbeuf, Joinville, the Archbishop of Lyon and the
prévôt des marchands (R43); Tours and the royalist–Navarre rapprochement (1589); Moulins, June–July 1589.

## Prior art

No edition of Morosini's legation found (no Acta Nuntiaturae Gallicae volume; searched 19 Sept 2026). The
clear duplicates of the covering letters are transcribed on DECODE (R18/R19 DOC_1806/1807).
Images: DECODE, login; kept git-ignored (`img/`, `decode/*.png|pdf|htm`).

## Remaining gaps
- R35: the stretch after "si" (202v l. 8) and the last line (203r l. 19) - blocker: illegible; a hole in the paper (seen on the image 23 Oct 2026) and damaged paper
- short unread stretches inside the 35 readings (about 540 holes in 33,000 words: openings, closings, one-to-eight-figure groups no word parse fits) - blocker: not-attempted; many checked on the images and found transcribed as written (encipherer's slips; 23 Oct also R27, R51, R57, R35 lines), the rest not cropped (none for R42, R48); listed per record in texts/<R>_reread_log.md
- Rome's decipherments of these ciphers (ASV Segr. Stato Francia 27, cited by Hübner 1870) - blocker: needs-physical-access; not imaged online
- missing leaves (R46 between 382v and 383r, R47 after 385v; R17 233v and R22's last leaf not imaged) - blocker: needs-physical-access
- item 22/29 - blocker: needs-physical-access; no DECODE record for it; not imaged, so its key is not known

## Escalation
- [x] siblings: all 36 enclosures R18-R58 opened; R23-R26, R50 identified as other material; R53/R54 in a second key (now morosini1589); R17 in Francia 18 found to be in this key
- [x] clear-pages: every record's DECODE "cleartext" images viewed (22 Oct 2026): covering letters in clear and address leaves, no decipherment; no interlinear glosses on the cipher pages
- [x] known-keys: Meister no. 40 (1587) and Lasry's DOC_3175 reconstruction applied; the same key read R17
- [x] print: Tempesti, Vita di Sisto V (1754) II books VI-XIII paraphrases many letters (used for names and sense only); Hübner, Sixte-Quint (1870) locates Rome's decipherments in Francia 27 (not imaged); no edition of the legation
- [n/a] key-rebuild: Meister's key is complete for these records; every off-list dotted code turned out to be a spurious or misplaced dot (22 Oct 2026)
- [x] retry: 22 Oct 2026, every record re-parsed word by word on the figures, doubtful figures checked on image crops (55 corrections from the images), readings aligned word by word with the figures; 23 Oct 2026 R27, R35, R51, R57 holes re-checked on the images and regraded (all read)

## Assumptions for George's review

- Credit: George is credited here with his partial reconstruction of Meister no. 40 on DECODE R18 (DOC_3175, Oct
  2020, "full key in Meister"), the key these 35 records are read with. His F22b key (R53/R54) is credited on
  `morosini1589` only.
- R17 joins this entry on the evidence that Meister no. 40 reads it (5 open codes in five pages) and that the DECODE
  key note on R17 points to that key; the record itself is not dated, and its sender is assumed to be Morosini.
