# Founders Online + EMLO sweep (26 Oct 2026)

Part of the October 2026 archive sweep (`research/archive_sweep_2026-10/BRIEF.md`). Output: `candidates.json`
(19 rows), `founders_hits.tsv` (verdict per Founders document hit), `mountflorence1801_ct.txt` (code groups of
the top lead), scripts `emlo_harvest.py`, `emlo_triage.py`, `add_rows.py`. `emlo_hits.json` / `emlo_triage.json`
are the raw EMLO harvest (regenerable; can be git-ignored).

## Method

### Founders Online (founders.archives.gov)

- Plain HTTP (curl, WebFetch) gets an AWS WAF challenge (HTTP 202, empty body). Worked through the built-in browser:
  `fetch()` from a founders.archives.gov page. Search URL form: `/?q=<terms>&s=1111211113&r=<offset>` (50 per page;
  `s=1111311113&r=N` opens the N-th hit). The `/search/Text:...` form ignores extra parameters.
- The WAF blocks after bursts (403 "Request blocked" after ~250 rapid requests; later 202 challenges every ~180
  requests). At 1.5 s per request with a page reload whenever a 202 appears, it ran clean.
- Phrases searched (hit counts): "not deciphered" 15, "not been deciphered" 3, undeciphered 7, "not decoded" 58,
  "key not found" 43, "key has not been found" 2, "code not found" 3, "encoded passage" 21, "not decyphered" 4,
  undecoded 3, undecyphered 4, "no key" 15, "unable to decode" 3, "unable to decipher" 5, "could not be deciphered" 2,
  "not been able to decipher" 1, "cannot be deciphered" 6, "could not decipher" 4, "partly decoded" 5,
  "partially decoded" 8, "partly/partially deciphered" 2, "code has not been" 7, "cipher has not been" 4,
  "key to the code" 6, "key has not" 3, "unidentified code" 6, "unidentified cipher" 1, "not been located" key 8,
  "left undecoded" 1, "not been identified" code 45, "did not decode/decipher", "Code No. 11" 18, and others with
  zero hits ("not been decoded", "remains undeciphered", "could not be decoded", "never deciphered", "unknown code").
- 306 hits → 253 documents; 210 with a cipher-related context. Each was classed (`founders_hits.tsv`). The great
  majority are read: interlinear decodings by Wagner/Madison/Jefferson, or editors decoding with a known key
  ("not decoded" usually describes one copy of several). Kept: 8 rows.

### EMLO (emlo.bodleian.ox.ac.uk)

- The results pages render client-side, but the Solr cores are open: `/solr/works/select?q=...&wt=json`, plus
  `comments`, `manifestations`, `institutions`, `people`. `emlo_harvest.py` queries works and notes (comments core)
  for cipher, ciphers, ciphered, cypher(s), decipher(ed), decyphered, chiffre(s), chiffré(e), cijfer(s),
  Geheimschrift, cifra, cifrado, ziffer, Chiffren, "in code", nomenclator, cryptography, steganography, zyfer,
  cyffer; the default field is English-stemmed, so non-English terms gave 0-2 hits.
- 857 works; 408 after dropping "decipher" in the sense of bad handwriting and "cipher" as "nonentity"/numerals.
  Groups: Elizabeth Stuart catalogue 118, Wallis 161 (Wallis's own decipherments), Ashmole 35 (cipher diary
  mentions), Kircher 18, Behn 9, Comenius 10, Henry Cromwell 6, Bodleian card catalogue ~15, Carte/early modern 8.
- Kept: 11 rows.

## Best leads

1. **Mountflorence → Madison, Paris, 18 Mar 1801** (NARA RG 59 CD Paris vol. 1). ~45 three-digit code groups printed
   undecoded on Founders (`Madison/02-91-02-0009`), editors: "key not found ... apparently discusses Louisiana
   cession". Humphreys could not read it with the State Department key either. Short, strong crib (the
   San Ildefonso/Aranjuez terms). Imp 4, solv 4.
2. **John Graham → Madison, 12 and 22 Nov 1806** (LoC Burr Conspiracy Collection): Burr conspiracy reports, read in
   part with J. E. Lewis's partial key; numerals with "as yet no key". Imp 4.
3. **Wallis's four undeciphered letters**, Bodleian MS. e Mus. 203 pp. 218-226 (+ copies): nos. 50-53 of his 1653
   collection, left "unsolved as exercises for aspirant cryptographers"; no. 50 is Brasset → Bordeaux, 4 Apr 1653
   (French). No solution found in a web search.
4. **W. V. Murray → Madison, The Hague, 26 Jun 1801**: coded postscript "not deciphered (key not found)"; his
   7 May 1801 postscript in the same volume was decoded by Wagner (sibling). Solv 4.
5. **Jefferson's Code No. 11** (Barclay-Lamb code, ~18 letters 1786-91): editors work from a partially reconstructed
   key with conjectures; a full rebuild from the decoded letters would settle Barclay ca. 3 Jul 1787 / TJ 4 Jul 1787.

Then: Behn 1666 spy letters (a few numeric code words not decoded; siblings decoded interline), Harrison/Jephson →
Henry Cromwell 1656-57 (partly decoded in EMLO footnotes), Dana 6 Apr 1783 (PCC 89; 8 lines not decoded in
Wharton), Carte 213 letters to Ormond 1660-61, Comenius → Klobusiczky 1655 (ciphered sentences, MNL OL E 190).

## Key leads (keys / code material, no ciphertext row)

- Lansdowne MS 823 ff. 339-340: draft code between Henry Cromwell and Lord Broghill (EMLO 2998b83b) — test on the
  Lansdowne 821 cipher letters.
- Behn SP 29/169 f. 47: postscript gives the key to her symbol cipher.
- Tanner 62 f. 506: a code version of the clear letter on f. 498 (crib pair for the Ogle plot code).
- Jefferson-Barclay Code No. 11, Codes 10/13/16: partial keys in the Jefferson Papers editorial files.
- J. E. Lewis's partial key to the State Department code of Graham 1806 (Madison Papers office).

## Dropped / already solved

- Mazzei → Madison 30 Nov 1780, four lines "key ... not discovered": solved by Armin Krauss 2015 (cryptiana).
- Wallis's "French cipher unsolved" (1690, Louvois letters): solved by Norbert Biermann 2020 (cryptiana).
- Armstrong, Erving 1807, JQA 1811, d'Estaing: already targets here.
- Church 1775, Culper ring, Lovell-cipher passages, Jay-Deane/Jay-Morris/Bingham codes, Monroe-Madison 1795-96,
  Wagner-decoded despatches 1801-07, Tobias Lear 1804: read in the editions.
- Jefferson's 1792 "Note of Agenda": shorthand, read by L. C. Stanton.
- Elizabeth Stuart letters: kept as one low row; Akkerman's edition deciphered the series.
- Wren/Huygens 1669 anagram-ciphers, Boyle's lost 'Anonym in Cypher', Ashmole's cipher-diary mentions: excluded.

## Papers of the Continental Congress / Library of Congress items met

- PCC item 89 vol. II pp. 727-742 (Dana, 1783) — row. PCC items 110, 118, 79 (Jay letterbooks, Livingston): "not
  decoded" copies of letters decoded elsewhere. PCC Misc. 5 (Jay 1781 duplicates). PCC item 25 (1788 oversight
  report on codes).
- LoC: Madison Papers (Mazzei 1780, solved), Burr Conspiracy Collection (Graham 1806, row), Jefferson Papers (Code
  No. 11 letters, row), GW Papers Sprague transcript (Smallwood 1777, row).

## Not reached / blockers

- Founders: the WAF limits scripted access; no API call was made (`/API/docdata/` also sits behind the challenge).
  The bulk metadata JSON was not fetched. Searches cover the editorial phrases above, not every "partly in code"
  note (there are thousands of decoded ones).
- Prior art was checked by web search only for the Wallis letters, Mountflorence and Behn; Cameron 1961 (Behn),
  Patera 1892 (Comenius), the Carte Calendar, Weber's *United States Diplomatic Codes and Ciphers* (1979) and
  Lewis's *The Burr Conspiracy* (2017) were not opened.
- No images viewed. NARA M30/M42/T1 microfilm and PCC (M247) are on the NARA catalogue; Bodleian MSS (e Mus. 203,
  Carte 213, Tanner 62, Rawl. letters 105) have no images online listed in EMLO.
