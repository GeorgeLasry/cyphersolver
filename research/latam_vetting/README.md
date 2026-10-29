# Latin American leads: vetting, 28 Oct 2026

The six leads from the Latin American sweeps whose images are online (plus 1471, the crib for 1470), checked against
the catalogue vetting bar (README Conventions). `vet_<id>.json` holds each vetting block as written into
`research/leads.json` / `catalogue.json`; `<id>_sample.txt` holds transcription samples and trial readings.

| Lead | Item | Verdict | Where it went |
|---|---|---|---|
| 1500 | Varela → Moreira de Castro, Asunción 13 Feb 1850 (ANA-AHRP-PY-558-1-31 item 13) | open | promoted to the catalogue |
| 1523 | López Méndez → Bolívar, London 29 Jan 1819 (AGN Colombia SAA-I.17,25,D.24) | open | promoted; most of the 15 cipher words already read from context in `1523_sample.txt`, four values open |
| 1470 | Cipher telegrams to Setembrino de Carvalho, Ceará 1914 (CPDOC FSC pce 1914.03.10/4) | key_lookup | closed: the pencil decipherment of the 14 Mar telegram gives the per-word Vigenère key MFTDBSJV, which reads six more; 10 Mar and 20 May mostly recovered ciphertext-only |
| 1471 | Vespasiano → Setembrino, 7 Oct 1914 (FSC cont 1914.10.07/2) | read | closed: every cipher word glossed on the sheet (key LBQPOHVJ) |
| 1526 | Leticia war telegrams 1932 (AGN Colombia GARV) | key_lookup | closed: the day-of-week key on GARV..1.1.4 ff. 43r-44r (`1526_key_garv114.tsv`) reads the GARV..2.2.4 telegrams; numeric telegram f. 151 untested |
| 1530 | Cienfuegos → Casa-Irujo, Havana 1819 (AGI Estado 12 N.14) | not vetted | still a lead: PARES refused every request (HTTP 429); Galende 2000 prints the vowel-digit system and names this document, so it is probably a key lookup once seen |
| 1531 | Expedition for the Venezuelan/Colombian insurgents, 1820 (AGI Estado 64 N.46) | not vetted | still a lead: PARES blocked, nothing seen |

1470 and 1526 are quick targets to read in their own right (key on the file); they are closed as catalogue leads
because the gate keeps key lookups out of the open catalogue.
