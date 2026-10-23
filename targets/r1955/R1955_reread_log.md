# Re-reading log, R1955 (23 Oct 2026, Claude Opus 5.5; REREAD_BRIEF, batch b32)

## Starting point

Reading audit (22 Oct): "decoded, not read". WAINUT's decode with the envoy table (from the Dutch decipherments on
R1050/R1051) gives a value to 95 of 360 groups; the rest have none. Clean-sentence share before: no reading (0.00).

## What was done

1. **The DECODE record.** R1955 fetched again with the project cookie (research/reading_audit/b28_fetch.py): two page
   images (IMG_R1955_I13453_P1, I13454_P2, 5472 x 3648) and no attachment, no comment block, no transcription. Both
   pages opened at full size: the clear heading "Lettre du Roi de Prusse au Secretaire Michell du 28 Decemb. 1751",
   the clear opening, 362 numbers, "à Berlin ce 28e Decemb.", "Signé Féderic". No interlinear or marginal
   decipherment, no slip. Neighbouring records R1954 and R1958 (Kauderbach, inv. 201) and the empty R1956 are not part
   of this letter.
2. **Other DECODE records in the same code.** The cached DECODE list (research/catalogue_harvest/decode/list.json)
   searched for Michell, Prussia, Frederick and KHA inv. 196-198: the only Michell records are R1050, R1051 (his
   reports, envoy code, the table's source), R1955 and R1957 (cabinet code). R2824 (Prussia key 1746) was rejected in
   hellen1752 (a Dutch key for van Reede). The envoy table (rebuilt with key1751/scripts/envoy_key.py: 512 pairs, 271
   codes) covers only 8-12% of the Hellen letters R1049, R1953 and the 1763 set, the level of chance, so von der
   Hellen did not use this code and his letters add nothing to the table. The table is a two-part code (values are not
   in alphabetical order of the numbers), so missing values cannot be interpolated.
3. **The Hague decipherment registers (Nationaal Archief 1.10.29 Fagel, IIIF via service.archief.nl,
   research/reading_audit/b32_na_iiif.py; the inventory PDF of 1.10.29 read for section IV "Ontcijferde brieven").**
   - inv. 5177 (register 1751-1752, 187 scans): the heading strip of every scan checked (b32_sheet.py contact sheets).
     The register is grouped by envoy: von der Hellen's reports and the letters to him (Nov-Dec 1751, in clear), then
     scans 95-101 the six cabinet-code letters to Michell, copied in figures and marked "Nonsense ou autre Clef", then
     Kauderbach, Elsacker, Durand and "Lettre du Sr de M." of 22 Sept - 13 Oct 1752. No copy or decipherment of the 28
     Dec 1751 rescript.
   - inv. 5208 ("Van Von Maltzahn ('Sieur M'), Pruisisch gezant in Groot-Brittannië, 1751-1753"; the 'Sieur M' of
     these years is Michell, 157 scans): every heading checked. Scans 5-16 "Lettres du Sieur M. de 1751" (his reports,
     from 19 Oct 1751); scans 17-22 "Lettres Ecrites au Sieur M. en Novemb. et Decemb. 1751", nos. 1-8, dated 2 Nov to
     7 Dec 1751, in clear with the decoded words underlined; scans 23-156 Michell's reports of 1752-1753 in clear. The
     letters to Michell are the ministerial rescripts (no. 1, 2 Nov 1751, opens "Le dernier Courrier m'a aporté Vôtre
     Depêche du 19 Octobre passé", not the wording of the cabinet letter of that date copied in 5177), so the Dutch did
     read the rescript series in this code, but the run stops at no. 8 (7 Dec 1751); the rescript of 28 Dec is not in
     it. The copies are clear text only (no figures), so they add no code values either.
4. **Print.** Not repeated (Politische Correspondenz 8-9 searched on 19 Sept and by WAINUT's circular test; the
   ministerial rescripts are not printed).

## Result

Unchanged: decoded, not read (0.00). No decipherment of this letter has been found, and no new key material.

## Open

- R1955, 265 of 360 groups without a value - blocker: no-key-material. Leads not reachable online: the KHA originals
  of Michell's reports (A31 inv. 198) whose clear text is in Fagel 5208 would give cipher/clear pairs (KHA is not
  digitised); a later Fagel register (5178, 1753) was not opened because the letter is of Dec 1751.
- The other 5208 rescripts (nos. 1-8, Nov-Dec 1751) show the series was read in The Hague; their cipher originals are
  not on DECODE.
