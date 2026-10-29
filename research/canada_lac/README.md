# Library and Archives Canada / Canadian manuscripts sweep (28 Oct 2026)

Follows `research/canada_latam/` (Canadiana printed search, LAC blocked by Cloudflare). Goal: reach the Canadian
manuscript holdings by other routes. Region "Americas". **17 candidates** in `candidates.json` (built by
`make_candidates.py`), all `seen: catalogue`; none viewed, because the LAC image server answered 503 to every
script request.

## The route that worked: New France Archives database (nouvelle-france.org)

The LAC/ANOM/BAnQ joint database "Archives de la Nouvelle-France" (over a million images; ANOM Colonies C11A-C11E,
C11B Île Royale, C13 Louisiana, F3, G1, plus LAC and BAnQ items) is served from `nouvelle-france.org`, **not** behind
the Cloudflare challenge that guards `recherche-collection-search.bac-lac.gc.ca`. Its search is a DataTables
server-side POST to `/eng/item/search` with the page's antiforgery token and cookie; `nfa.py` drives it, and
`nfa_details.py` pulls each record's detail page (`/eng/item/details?id=N`).

Terms (keyword column, accent-insensitive stemming): chiffre/chiffré (39), chiffrée (18), chiffres/chiffrés (15),
code (7), clef (12), en chiffre (2), traduite (2); cipher, cypher, déchiffr*, déchiffrement, contrechiffre: 0.
58 distinct records fetched (`nfa_details.json`, `nfa_scope.json`); most are noise ("chiffres mentionnés" in
accounts, "code civil", keys to storehouses). Kept **16** actual cipher despatches, 1734-1760.

The descriptions split cleanly in two:

- **Title only, no summary** ("Lettre chiffrée de Vaudreuil de Cavagnial au ministre."): the describers could not
  read the text. Vaudreuil 8, 10, 16 Apr 1759 and 13 Aug 1760, Trémais 6 Nov 1759. These are the best leads (cls B).
- **Detailed content summary** with quotations (Beauharnois 1744-45, Hocquart 1745, Saint-Ovide 1734): the letter was
  deciphered, probably interlinear or in the bureau. Kept as cls A at low importance, in case the decipherment is
  partial; drop them at merge if the images show full interlinear text.

## Best leads (ranked)

1. **Vaudreuil → minister, 13 Aug 1760**, COL C11A 105 ff.147-152 (6 images), Montréal, three weeks before the
   capitulation. Unsummarised. Check against the calames_biblissima row "Vaudreuil to Berryer announcing in figures the
   loss of the colony" (may be another copy).
2. **Vaudreuil → minister, 8 Apr 1759**, C11A 104 ff.54-66 (13 images): the longest unsummarised cipher letter.
3. **Vaudreuil → minister, 10 Apr 1759**, C11A 104 ff.68-72 (5 images).
4. **Trémais → minister, 6 Nov 1759**, C11A 104 ff.346-347v: the commissaire sent to audit Bigot (Affaire du Canada).
5. **Saint-Ovide → minister, 28 Oct 1734**, C11B 15 ff.121-138v (35 images), Louisbourg; summarised, but "ff.137-138v
   ne sont pas transcrits".
6. Drucourt & Prévost 22 Oct 1757 (Halifax raid plan), Duquesnel 1 Dec 1740, Bourville 3 Aug 1740 (Louisbourg).
7. Beauharnois 1744 (×5) and 1745, Hocquart June 1745 (×2): read at the time, judging by the summaries.

Also 1 McGill hit (Dawson-Harrington fonds, MG1022-6-126, 1891-92, "cypher" in OCR text), importance 1.

## Key leads (bare keys and cribs)

- **"Chiffre ou code de Montcalm et de Vaudreuil au cours des deux années 1757 et 1758"**, ANOM COL C11E 10
  ff.285-290v, 10 images (nouvelle-france.org id 15213). Likely the key family for the 1759-60 Vaudreuil letters and
  for the Montcalm 1758 "lettre chiffrée" already listed by research/central_archives.
- **Beauharnois & Hocquart → minister, 31 Oct 1746, "Lettre chiffrée, traduite"**, COL C11D 8 ff.119-127v (id 7665,
  18 images): cipher with its decipherment, a crib for the 1744-46 governor's cipher. Left out as a candidate because
  it is deciphered.
- Ministry ciphers issued: Beauharnois received a cipher for correspondence with Saint-Ovide (C11A 61 f.282, 30 Sept
  1734, id 18254); Vaudreuil acknowledged the ministry cipher (C11A 101 f.105, 22 Sept 1756, id 27032). Pontleroy had
  no cipher in 1758 (id 27424) and asked Vaudreuil to have his Quebec report ciphered in 1759 (id 27548).
- A deciphered copy may sit in the 19th-century **LAC transcripts of C11A** on heritage.canadiana.ca ("Archives des
  Colonies: Série C 11 A (transcrits)", reels C-2380 ff.; C11B reels C-9291 ff.; C11E reels C-11032 ff.). The reels
  have no full text and no folio index, so finding a folio means paging the reel.

## Routes tried

| Route | Result |
|---|---|
| LAC Collection Search `/eng/Home/Result`, `/eng/Home/Search`, `central.bac-lac.gc.ca/.redirect`, legacy `collectionscanada.gc.ca/lac-bac/results/arch` (MIKAN) | 403, Cloudflare challenge page, every one. WebFetch: 403. Not bypassed. |
| open.canada.ca CKAN (`package_search`) | LAC publishes only corporate reports, no archival-description dataset. |
| LAC image server `central.bac-lac.gc.ca/.item?id=e000874969&op=img&app=nf` (images behind nouvelle-france.org) | 503 "temporarily unable to look up this record" (also with deepzoom and pdf ops). One test image only. |
| heritage.canadiana.ca | Open, but item records are whole microfilm reels with generic titles (fielded `ti:` search works); "cipher" matches only noise. Useful as an image route for C11A/C11B/C11E transcripts and the Haldimand reels ("Haldimand papers from the British Library", reels H-1440 ff.). |
| Archives Canada portal (archivescanada.accesstomemory.ca), incl. OAI and API | AtoM JavaScript challenge ("Verifying your browser"). Same on Archeion (Ontario), UBC RBSC, Dalhousie, MemoryNS, U of T, McMaster; Vancouver City Archives: captcha. Not bypassed. |
| McGill Archival Collections (AtoM) | Open. `atom.py`: cipher 5, cypher 1, chiffre/ciphered/"code book"/cryptogram/"invisible ink"/"secret writing" 0. One weak hit kept. |
| BAnQ advitam | Radware captcha. Not bypassed. |
| ANOM IREL, archivescanadafrance | Home page only / connection refused; not needed once nouvelle-france.org worked. |
| BL searcharchives JSON (Haldimand Add MS) | `catalog.json?q=` redirects to the home page; not scriptable this way. BL is another sweep's ground. |
| Claude in Chrome | Extension not connected, so no real-browser route to LAC. |
| Web search | Haldimand cipher/Vermont, Vaudreuil/Montcalm chiffre, Beauharnois/Saint-Ovide ciphers, Fenian/McMicken codes: no published decipherments and no further named items. |

## Not reached

- LAC item-level descriptions of MG 21 (Haldimand), RG 7 G21 Governor General's numbered files ("cypher telegrams"),
  RG 9 / RG 24 militia and defence, RG 25 External Affairs code telegrams, MG 26 Macdonald papers (Fenian secret
  service): all sit behind the Collection Search challenge. Haldimand's BL originals (Add MS 21661-21892) belong to the
  BL sweep; research/tna_discovery already lists the Carleton Papers Clinton-Haldimand cyphers.
- Gouzenko 1945 (Soviet material; out of scope or in other repositories), WWI German sabotage in Canada, HBC (no
  manuscript ciphers found by the earlier pass), Riel 1885: nothing citable found.
- nouvelle-france.org images: retry the LAC image server later or open the records in a normal browser.

## Files

`nfa.py` (search), `nfa_details.py` (detail pages), `nfa_hits.json`, `nfa_details.json`, `nfa_scope.json`,
`atom.py` + `atom_archivalcollections_library_mcgill_ca.json` (McGill), `make_candidates.py`, `candidates.json`.
