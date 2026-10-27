# Worklog: frederik1523 (catalogue 466)

- 2026-10-26 literature search: web search (Frederik/Lübeck 1523 cipher, Hanserecesse); Hanserecesse III/8 (1523-25) not among the archive.org scans (7 III-series items checked by text). Not on DECODE (catalogue check).
- 2026-10-26 access: whole series (epid 14908271, image ids from 41301821) downloaded from api.rigsarkivet.dk with ../biermann1675/fetch.sh into work/img (git-ignored).
- 2026-10-26 location: item slips at images 2 (item 1), 8, 59, 83, 90, 93 (item 8, id 41301913: "Sager vedr. forhandlingerne mellem hertug Frederik og Lübeck 1523. Delvis med anvendelse af zifferskrift. ... Pergamentsbreve E 16-23"), 130 (item 9). Item 8 = images 94-129.
- 2026-10-26 system: image 94 (copy, "Ex:", docket 1523 14/2, Lauen. Arch. XIII 47c) is clear Low German with single signs standing for names (circle-bar, circle-cross, gallows, barred IIII, rectangle, K, X, 4 ...). A name-sign code inside clear text, not a letter cipher.
- 2026-10-26 transcription: image 94 transcribed line by line with ad hoc sign labels (transcription_094.txt; 30 lines, 50 sign tokens, 15 sign types).
- 2026-10-26 hypothesis (contextual inference): the two signs in "den bedungeden tall der GG vnd IIII" are troops; rectangle = King Christian ("deme SQ aftobrekende"); QX = a prince on the troops' route.
- 2026-10-26 survey: survey_A.tsv (94-95) and survey_B.tsv (112-113) by agents; 95 continues 94 (dated "am dage Valentini"); 112-113 = clear copy of the alliance treaty. Survey stopped when the edition was found.
- 2026-10-26 literature (found): Hanserecesse III/8 (Schäfer & Techen 1910), HGV PDF hanserecesse_3_8_low.pdf. n. 292 = this letter (K1 = XIII 47c Konzept, ciphered), printed with all signs resolved; key strip Gemeinsch. Arch. XIII, 38 (Utenhof endorsement) on the plate facing p. 312; signs used nn. 279-354.
- 2026-10-26 control: own transcription vs printed n. 292: every label maps to one Ch. number; the guesses (rutere, knechte, koningk, bisschop van Bremen) agree.
- 2026-10-26 key: plate transcribed to key.tsv (Ch. 1-72).
- 2026-10-26 closed: existing decipherment in print; Status: no write-up; DECODE queue skip (not on DECODE).
- 2026-10-26 control: checked the transcription's disagreements with the print on the scan: l.16 corrected to the Lübeck sign; l.10 has the Frederik sign where the edition gives Lübeck (recorded). l.5 "12" = Hadersleven sign (Ch. 47); l.21 4-shape = Schonen (Ch. 60).
- 2026-10-26 reading: decryption_094.txt (signs resolved by the key; [?] words from the print) and translation_094_en.txt; profile outcome.texts added.
