# HathiTrust sweep (28 Oct 2026)

Result: `candidates.json`, 54 rows (all `cls` C, `seen` = catalogue). Scores are from the printed calendar text only.

## What was blocked

Every HathiTrust endpoint answered with a Cloudflare challenge ("Just a moment...") or a 403, so nothing there was tried further:

- `catalog.hathitrust.org/api/volumes/brief/...` (403 Forbidden, Cloudflare)
- `catalog.hathitrust.org/Search/Home` (challenge page)
- `babel.hathitrust.org/cgi/ls` full-text search, `/cgi/pt` page view, `/cgi/pt/search` in-volume search (challenge page)

No workaround was attempted. Consequences: no Hathi volume ids or babel page links could be resolved; each row links the
archive.org copy of the same calendar volume (`https://archive.org/details/<id>`) and a Hathi catalogue title search
(unverified). WebSearch with `site:babel.hathitrust.org` returned nothing usable. Full-text search of Hathi remains
unreached; it is the single biggest gap (it would find the editions that archive.org does not hold).

## Method

archive.org is not blocked, and holds copies of the same public-domain printed calendars (Cornell, Michigan, BSB, Google
scans, "sim_" serials). `scan.py` (<=1 req/s, descriptive User-Agent) runs an archive.org advancedsearch, downloads each
`_djvu.txt`, and greps for editor notes such as "cipher undeciphered", "cypher, undecyphered", "not decyphered",
"chiffre non", "non decifrat", "ungeloest" etc. `extract.py` re-reads the volumes with hits (cached under `.work/`,
git-ignored) and captures entry number, page header, date and the note; `build_candidates.py` maps volume ids to
calendar names and de-duplicates the many archive.org scans of one volume; `finalize.py` adds two hand-checked rows and
fixes the ones I could check by eye. Scripts are re-runnable in that order.

Volumes scanned: about 210 archive.org texts. Series covered: Calendar of State Papers Domestic (Edward VI to William and
Mary, Commonwealth, Charles I and II), CSP Foreign (Edward VI, Mary, Elizabeth), CSP Colonial, HMC Salisbury (Cecil)
calendars (about 40 volumes), Calendar of the Clarendon State Papers, Calendar of the Stuart Papers, Calendar of
Confederate papers, HMC Fortescue. Hits: about 175 distinct note hits; 54 kept (the rest were index lines, editorial prefaces,
other-language false positives, or already in the repo).

## Dedup against the repo

`research/ia_meta/candidates.json` (another sweep, same printed calendars) already holds aggregate rows for: Edward VI nos. 97,
271/328/588 (Wotton, Morysine, Pickering), Elizabeth 1569-71 nos. 811-812, the Norton/Lee/Hunsdon 1572 intercepts, the
Phelippes intercepts of 1594, the E. F. Mak / Bankes letter, and the 1655-56 Commonwealth royalist letters. I dropped the
individual rows for the first five groups. The Commonwealth 1655-56 and 1659-60 rows are item-level versions of ia_meta's
aggregate rows: on merge, replace the aggregate with these rather than keep both. `known.py` found nothing else for the
names used (checked Pile, de Marces, Killegrew, Jennings, Bristowe, John Lee, Pickering, Wotton).
`targets/hyde/NOTES.md` is the Hyde-Barwick key, a different (superscription) question.

## Best leads (ranked)

1. HMC Salisbury Part IV (1892), CIPHER LETTER of 28 Feb 1594, printed p. 484-485, calendared "Undeciphered. 1 p."
   (Henri IV's coronation day, Chartres). Cecil Papers at Hatfield; index also lists a second reference ("55?", OCR)
   under "Cipher letters undeciphered", not resolved.
2. CSP Foreign Elizabeth 1572-74: Irish declaration of loyalty to the Catholic cause with the armada on the Irish coast,
   London, 14 Jun 1574, "a considerable portion not deciphered".
3. CSP Foreign Elizabeth 1572-74 no. 4: Killegrew to Burghley, 17 Mar 1572, "There be at Stirling, yet undeciphered".
4. CSP Domestic Elizabeth Addenda 1566-79 no. 59: Jennings to the Countess of Northumberland, 1572, "the whole letter is in
   cipher undeciphered".
5. CSP Foreign Mary no. 453: Wotton to Queen Mary, 4 Jan 1555 (a few lines); CSP Domestic Commonwealth 1659-60:
   Nicholas/Hyde to de Marces and Inchiquin extracts in "Italics cypher undecyphered" (about 25 items, numeric cipher in
   no. 502); CSP Domestic Commonwealth 1655-56 Ross/Pile to Nicholas (about 16 items).

## Key leads

None found as bare keys. Note for the 1659 set: the Hyde-Barwick key (THE=370, 1-692) is in targets/hyde; Stuart Papers
vol. 3 prefaces list partly "undeciphered" Jacobite cipher names (editor's lists, not ciphertext).

## Caveats

- Entry numbers, correspondents and dates come from regex on OCR; `correspondents` = "unknown" and "entry (no. not captured)"
  mean the heading was not captured, not that it is unknown in the book. Verify on the page before merging.
- The Burlamachi 1620 row and the 1659 French-correspondence extracts may carry the note of the neighbouring entry.
- "Undeciphered" in a calendar usually means the editor could not read it, but the original may be deciphered by
  the contemporary clerk (Phelippes, Wallis); that has not been checked.
- Solvability is 1-2 throughout: no images were viewed; TNA SP scans are not freely online.

## Dead ends / not reached

- HathiTrust full-text and catalogue (blocked, above).
- Other series not scanned: Calendar of Treasury Papers, Carte/Ormonde, Thurloe State Papers, Official Records of the Rebellion,
  Continental Congress / state archives (the first batch of those queries was cut off by a shell exit; not re-run), HMC reports
  other than Salisbury/Fortescue, Calendars of Spanish and Venetian papers (these decipher in the text), Jacobite/Stuart
  intercept volumes, German/French/Italian editions (chiffre non dechiffre, ungeloest patterns ran but found nothing in the
  English-heavy volumes scanned).
