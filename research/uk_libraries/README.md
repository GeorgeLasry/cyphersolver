# UK libraries and archives sweep (29 Oct 2026)

Scope: Archives Hub, Cambridge (CUDL and ArchiveSearch), Bodleian Archives & Manuscripts, Medieval Manuscripts in
Oxford, TCD, NLW, NLS, NRS, Wellcome, Parliamentary Archives, Edinburgh University. `candidates.json` holds 15 rows
(built by `make_candidates.py`; hand-written from the raw hits below). None was viewed on the image.

## Method and counts

| Source | Route | Result |
|---|---|---|
| Wellcome | `api.wellcomecollection.org/catalogue/v2/works` (`wellcome.py`, `raw`: `wellcome_raw.json`), 14 terms, dated 1350-1950 | 2,531 records, 181 matched cipher words locally; almost all noise ("code" medical, engraved "cyphers" monograms). 1 candidate (MS 309 Gerlach). Galton diaries (1829-44, own cipher, key GALTON/1/1/7/2/1) excluded: key exists, 19th c. |
| Edinburgh Univ. | ArchivesSpace PUI (`aspace.py`, `raw_edinburgh.json`) | fuzzy search, no usable hit. |
| CUDL | in-page JSON `/search/JSONAdvanced` (needs a browser session; AWS WAF returns 202 to scripts) | 219 items, ~60 real. Nearly all marginal cipher notes in medieval recipe/medical MSS (Trinity O.1.65, O.7.23, R.14.30/32/44, Peterhouse 222, Newnham Renouf 1, Equatorie of the Planetis) and Genizah "ciphers" = verse counts. 1 candidate (Lambeth MS 2086 Rawley). |
| Cambridge ArchiveSearch | in-page crawl, 20 terms | 330 records, 182 with cipher words; mostly 20th-c. (Crewe cypher telegrams, Churchill, Bletchley). Pre-1800: Add.8863/3 (Ferdinand II → Mansfeld 1631, comes with decipherment: excluded), Dd.06.04 Castell, JM/A8/121/37 Jardine Matheson cipher keys (19th c., key lead). 1 candidate. |
| Bodleian A&M | in-page crawl, 29 terms (Anubis proof-of-work passes in a real browser) | 274 records, 214 with cipher words. ~42 Thurloe papers (Rawl. A.), Tanner, Carte, Rawl. C/D. Rhodes cypher telegrams (MSS. Afr. s. 228, 1888-1902, about 60, with translations) not listed as candidates. 6 candidate rows. |
| NRS online catalogue | ASP.NET postback crawl (`nrs.py`, `raw_nrs.json`), dated 1350-1950 | 528 records over 11 terms ("in code" is noise: Education Codes, railway telegraph codes). Core: GD406 Hamilton muniments, GD124 Mar and Kellie, GD158 Polwarth, GD112 Breadalbane, GD16 Airlie, CH12 Episcopal chest. 6 candidate rows. |
| Medieval MSS in Oxford | full-text catalogue search | fuzzy, 532 hits for "cipher"/"writing" etc., no cipher text items; skipped. |

## Best leads (importance x solvability)

1. NRS GD406/1/2181-2234: Charles I and agents' cipher letters 1647-48 catalogued "undeciphered" (overlaps `targets/hamilton`).
2. Bodleian Tanner 78/79: Walsingham → Harborne 1585, 1587 (key leads Tanner 79 f.56, f.214).
3. Lambeth MS 2086, Rawley's cipher (Greek + numerals), Bacon anecdotes, images on CUDL.
4. Wellcome MS 309 Gerlach 1572: 51-sign cipher, key bound in (class B, checkable).
5. Bodleian Rawl. A. Thurloe cipher items (Stouppe-Tarente, Mountagu, Pawly); check Birch's print first.

## Key leads (keys without ciphertext)

Bodleian Rawl. A. 33 pp. 748, 752; Rawl. A. 185 f. 289 (Pepys/Jenkins); Rawl. D. 749 f. 226 (figures cipher);
Carte 50 f. 405, Carte 194, Clarendon 94, Add. C. 276 (Strafford ciphers); Tanner 88 f. 1b (Astelie/Putean);
Talbot b. 29 (1799 keys); Fairfax 34 f. 68 (numeric 1-379); Harcourt dep. adds. 208 (War Dept Cypher Lexicon 1812);
NRS GD158/1494, 2423, 2525 (Polwarth ciphers), GD24/1/946 (Jacobite keys), GD26/15/58, GD220/3/190 (Montrose key 1648),
GD45/26/158; Cambridge JM/A8/121/37. Also MS Eng. misc. c. 382 and e. 475 (Wallis's deciphered copies; already in repo via Wallis).

## Not reached (blocked)

- **Archives Hub** (and thereby Hatfield, Longleat, Lambeth and most UK university collections): Cloudflare interactive challenge for scripts and for the in-app browser; not bypassed.
- **National Library of Wales** (archives.library.wales) and **NLS manuscripts**: same Cloudflare challenge.
- **TCD** digitalcollections.tcd.ie: security check page; manuscripts catalogue host did not resolve.
- **Lambeth Palace Library** own catalogue: 403 to scripts.
- **Parliamentary Archives**: now catalogued in TNA Discovery (other agent).
- Not used: full text of printed calendars (Thurloe, Hamilton Papers, HMC) to check each Bodleian/NRS item for an existing decipherment; candidates are marked accordingly.
- Excluded noise: royal cypher monograms, engravers' cypher books, Genizah verse-count "ciphers", Galton diaries (key survives), WWII/Bletchley and 20th-c. telegrams.
