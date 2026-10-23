# Re-reading log, R8499 (23 Oct 2026, Claude Opus 5.5; REREAD_BRIEF, batch b28)

## Starting point

Reading audit (22 Oct): "decoded, not read". `final_v9.txt`: `docs/_check_reading.py --file` **0.102 clean
(10/98 sentences), hole rate 0.317, 1,164 words**. Eight transcription and key passes (NOTES, 22 Sept - 5 Oct) have
flattened at 75% of non-null signs firm, 68.9% judged as sense.

## 1. Is there a text already? Yes — the contemporary decipherment, Harley MS 1582 ff. 5r-7v, out of reach

- **Every DECODE record of Harley 1582** listed from the harvested DECODE list (`research/catalogue_harvest/decode/`,
  main checkout) and re-fetched with the cookie (`research/reading_audit/b28_fetch.py`): R8009, R8010, R8498, R8499,
  R8500-R8505.
  - R8499: six images (ff. 8r, 8v, 9r, 10v, binding views), no DOC_ attachment, no comment.
  - **R8009** ("Harley_ms_1582_8", N/A, 4 pages): an empty record, no images or files. Not ff. 5-7.
  - **R8010** ("Harley_ms_1582_8", 1553-1596, 4 images): opened all four; they are **ff. 263r-264v, "L'Estat du Roy
    de Navarre & de son party en France"** — the same leaves as R8505 (a duplicate record, logged for
    harley1582r8505), not the Wotton copy.
  - R8498: ff. 1-4 (Pickering 1553). R8500-R8504: Stafford 1586.
  So ff. 5r-7v are on no DECODE record under any name.
- **BL catalogue, 23 Oct 2026** (searcharchives.bl.uk 040-002047412): ff. 5r-7v "Letter of Nicholas Wotton (?) to
  Queen Mary I, 13 June 1554 (?). Probably a contemporary copy deciphering the letter at ff. 8r-10v." New: the record
  now states the volume **is digitised** ("digital images currently unavailable"), viewer ark
  `ark:/81055/vdc_100162940894.0x000001` (MDARK `vdc_100000000709.0x000059`). The IIIF routes that worked for other BL
  volumes return 403 / 404 for it (bl.digirati.io manifest 403 AccessDenied; iiif.bl.uk 404; api.bl.uk 404). When the
  BL restores the legacy images, ff. 5r-7v can be fetched by that ark without an imaging order.
- Print: not in CSP Foreign Mary, Tytler ii, CSP Scotland i (22 Sept); nothing new found.
- The key itself: DECODE R354 (SP 106/2 f. 162), already in use; no second copy on DECODE (`sibling_keys.md`).

## 2-3. Reading on the image

Not repeated: every line was re-read at full resolution on 5 Oct (v9), and the remaining unread and nonsense stretches
are tokens confirmed on the image whose R354 values give no English (signs absent from the key sheet, rare codes,
probable clerk's slips). A new pass on the same images and key cannot close them; the contemporary decipherment can.
No reading file was made: the sentences do not hold (see the audit examples "Carew the [?1] changes the French king it
[?1] to use to attempt").

## Result

Stays **decoded, not read**: 0.102 before, 0.102 after (no change). Blocker: **needs-physical-access** — the
contemporary decipherment ff. 5r-7v is digitised by the BL but the images are unavailable since the 2023 cyber-attack
(ark above); otherwise a BL imaging order. Look-alike letters: no new reading made, none counted.
