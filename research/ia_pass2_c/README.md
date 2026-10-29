# Internet Archive, second pass C: non-English printed sources (28 Oct 2026)

Brief: `research/archive_sweep_2026-10/BRIEF.md`. Output: `candidates.json` (94 rows: class B 71, C 23; no edits to catalogue.json or docs/).

## Method
* fts endpoint (`fts.py`, same as `research/ia_fulltext`): `harvest.py` (68 phrase queries, fr/de/it/es/nl/pt/la/pl/sv, 3 pages) and `harvest2.py`
  (about 60 further queries, 6 pages): 1,756 + 3,074 volume hits (`hits_raw*.json`), mostly dictionaries, novels, Egyptology.
* Title filter -> `sel2.json` (284 volumes) and `sel3.json` (590); `dl.py` downloaded the OCR to the session scratchpad (not in repo).
* `extract.py`: negation phrase (non dechiffre, nicht aufgeloest, non decifrata, sin descifrar, niet ontcijferd ...) within 160 characters of a cipher word; 734 + 36 windows, read by hand with `show.py`.
* The productive route was not the phrase hits but catalogues/inventories found through them: `q.py` follow-up queries ("cifra sin traducir", "con algunas frases en cifra") led to the RAH Salazar y Castro catalogue (31 MB OCR, IA item `salazary-castro-22-nov-2016`), parsed in the session into entries and filtered to those with "cifra/cifrad/clave" and no mention of decipherment/translation (1,308 of 61,749 entries; `rows_salazar.py` holds the pre-1520 rows, `build.py` builds everything).
* Dedup: `known.py` on names/shelfmarks. DECODE has Salazar volumes 9/8, 9/17, 9/23-9/31, 9/34 only; A-10 to A-14, N-23 and A-87 ff. are absent.

## Counts
Phrase hits about 4,800 volumes; 320 volumes read as text; 770 windows; 94 rows kept: Salazar y Castro 1472-1513 (45), Salazar 1638-1656 (6 grouped rows), Lope de Soria archive 1931 catalogue (20), Farnese inventory (15), others (8).
Dropped as already in the repo: Nevers/Montholon ciphers (BnF fr. 4715, SOLVED_CATALOGUE), Vetesi 1705 (Fontes rerum Austriacarum), Soria A-17/Salazar 1517, Ferriz 1475, Leonor 1476, Despuig 1478, Claver 1500 (DECODE R9483-R9485, R9591, research/oldest B4). Dropped as not ciphertext: letters merely asking for or acknowledging a cipher; Egyptology/epigraphy "nicht entziffert"; Fersen "non dechiffre" footnotes on single words.

## Best leads
1. **RAH Salazar y Castro A-10/A-11/A-12/N-23, 1472-1513**: 45 cipher letters of Ferdinand the Catholic, the Great Captain (A-11 f. 270, 332, 366, 415-417; A-12 f. 1; A-8 ff. 199-208), Claver, Figueroa, Garci Lasso; not on DECODE; the cifra general RRCC and Parisi's work apply. Two are pre-1480 (Ferdinand to Juan II, 24 Aug 1472 and Apr 1478).
2. **Salazar A-87**, Philip IV and the Cardinal-Infante to Antonio Sarmiento 1638-39 (about 25 cipher letters).
3. **Salazar A-109** Medici cardinals to Haro, conclave 1655; **A-89/A-103** Don Juan Jose of Austria 1648-55.
4. **Farnese inventory**: Philip II to Alexander Farnese 1584 and 1590, Mendoza 1588, Philip II to Granvelle 1564; key tables are in fascio 397 (and fascio 1624).
5. **Falkenberg/Stallman to Gustavus Adolphus, Magdeburg 1631**: ciphered letters not resolved by the editor.

## Key leads (bare keys, not rows)
Salazar A-15 (inventory 1704-1711): "Cifra del visorrey", "Cifra general", Cifra Alonso de Silva-Garcilaso de la Vega (ff. 11-14), Cifra con Muros, Mauleon, bishop of Badajoz, archbishop of Zaragoza; N-65 f. 201 a Charles II cipher key; I-7 f. 148 Samper's cipher. Farnese fascio 397 (key tables), fascio 1624 (Alexander's key to his mother 1578-79), fascio 187 (Agocchi key). The A-15 sheets bear directly on `targets/garcilaso1498`, which lacked the key.

## Not reached / blockers
* Salazar entries of 1520-1529 (about 1,000, A-19 to A-26): not itemised; A-18 to A-22 are not among the DECODE volumes, so a next pass should check them against targets/lopehurtado*, sanchez1523, sessa* and keep the rest. Filtering was by absence of the words descifr/traducc, so some rows may have an attached decipherment not mentioned; the entry says "claro" for those.
* Whether RAH images of Salazar exist online was not checked (solvability scored 3 for the Ferdinand family on that assumption, 2 for undated/unknown senders).
* The Lope de Soria archive (1931 BRAH catalogue): present location unknown.
* German, Italian, Dutch, Portuguese: phrase queries gave almost nothing item-level (OCR quality; editors say "aufgeloest"). Nuntiaturberichte vols 6/14 only mark the cipher span ("Ende der Chiffer"), the decipherments are printed. Dutch/Portuguese/Polish/Latin queries returned no usable hits.
* Besancon (Castan) volume number for the Renard papers and Farnese fascio numbers come from OCR and are marked to confirm.
* Web prior-art checks were limited to two searches (Salazar/cifra general; Sarmiento 1638-39); the rest say "known.py" only.
