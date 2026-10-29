# Calames / Biblissima / FranceArchives (non-AN) sweep (28 Oct 2026)

51 candidates in `candidates.json` (30 from Calames, 21 from FranceArchives departmental, ANOM, SHD and library fonds).
All scored from the catalogue description; none viewed on the image (`seen: catalogue`).

## Method

- **Calames** (ABES, ~hundreds of French libraries' manuscript catalogues). The site is a JS front-end over
  `https://calames.abes.fr/prod/EadSearch.aspx?Query=Rech&<field>=<term>&from=1&to=100` (found in `pub/javascript/calames.js`;
  plain GET, no WAF; `q=` does not work, the field names are the form fields: `fullText`, `titre`, `indexSimple`+`typeIndex=sujet`).
  `Query=Detail&id=<id>` returns the item and its ancestors. `calames_harvest.py` ran 35 terms (chiffre/chiffré/chiffrée(s)/chifre,
  déchiffrement, écriture secrète, clef/clé du chiffre, cifra, cryptographie, nomenclateur ...) over the three fields:
  2,203 distinct hits (`calames_hits.json`). `calames_detail.py` fetched the detail of all 2,203 (`calames_detail.json`);
  a body-text regex (lettre chiffrée, en chiffre, déchiffr-, clef du chiffre ...) with noise filters left ~330 items, reviewed by hand.
  Accent-folded whole-word search means "chiffre" also returns monograms, statistics and page numbers: most hits are noise
  (Breuil prehistory cards, Great War postcards, alcohol statistics, Lenoir drawings ...).
- **FranceArchives** (`francearchives.gouv.fr/fr/search?es_escategory=archives&items_per_page=50&q=<term>&page=<n>`). Full text
  (notice excerpts included, unlike the title-only AN sweep). First answer is a JS redirect to `/redirect_<token>/<path>`;
  following it with a plain GET and a cookie jar works (no browser needed), but pages take 10-15 s. `fa_harvest.py`/`fa_harvest2.py`,
  ~55 phrase terms, 1,944 distinct cards (`fa_all.json`). Rows with `Lieu de conservation = Archives nationales` were dropped
  (covered by `../archives_nationales`); ANOM, SHD, MAE, departmental archives and libraries kept. After removing statistics,
  epigraphy ("déchiffrement" of inscriptions), post-1950 and noise, ~500 cards were reviewed; 21 rows written.
- Dedup: `known.py` plus `kn.py` (file-name summary) on every name and shelfmark; overlaps with `research/central_archives`
  (ANOM COL C14 21-25, C8 A 64, Mazarine Ms 4802, Yvelines E/3756) and `research/canada_latam` (Kerlérec 1758-59) were left out or
  noted. Prior art web-searched for the two top Calames clusters only (Christina/Hacki; Condé/Pichegru): nothing found.

## Best leads (importance x solvability)

1. **Montpellier H 258, Hacki to Queen Christina, Oct 1668-Apr 1669**: ~18 cipher sheets, with 8 neighbouring "mise en clair" sheets and one
   sheet glossed above each group (no. 228). Class A, cribs on the page. Same volume: nuncio (Corinth), Terlon 1671, Christina's own
   partly ciphered letters 1672, key table no. 354.
2. **ANOM COL C8 A 77 (Martinique, Bouillé), 17 Sep and 5 Dec 1778**: "chiffrée non décryptée" in the calendar itself. The repo's
   `mercier1761` key (C8 A 64) is the obvious first test; 18 further "(chiffrée)" letters 1779-82 in C8 A 78-81.
3. **Chantilly, Condé papers**: Ms 1967 (Pichegru negotiations 1795-97, tables at the start), Ms 1988 (letters ciphered as musical scores,
   1790-1800: unusual), key volume Ms 2157; Mazarin to Talon 1655-56 (Ms 1485; check Chéruel first).
4. **Institut, Collection Godefroy Ms 260-271**: Feuquières to Rorté 1634 (6 letters largely in cipher), Henri III/IV/Jeannin letters partly ciphered.
   Several are printed (Guadet, Rommel), which gives cribs. Ms Godefroy 168 holds Sillery/Mercoeur/Césy cipher keys (Peiresc's memoir).
5. **Condé 1651-52 ciphers** at AD Dordogne 2 E 1841-18; SHD GR 1KT 211 holds five Condé 1651 cipher letters with transcription and method.

## Key leads (bare keys or tables, no row)

Chantilly Ms 2157 (Chiffres et clés de l'Armée de Condé), Ms 1876, 1885, 1888 and 1905 (tables de déchiffrement at the end of volumes
of Condé / Marie de Gonzague papers); Masson Ms 305 (Desroches tables); Sorbonne MSRIC 44 f. 26 (chiffre de correspondance de M. Colonna
en Corse); Mazarine Ms 842 f. 70 (Chiave della cifra di Baldassar Castiglione, a Mazarine volume of Borghesi's copies); Mazarine Ms 3730 (Recueil de
chifres, probably monograms); Sainte-Geneviève Ms 3119 items 6-7 (treatises on writing in cipher, 17th c.) and Ms 1073 (stenographic table, 1690);
BULAC/Gagarine R48-8/9 (Karttunen 1911 and Biaudet 1910 studies on the Polish nuncio ciphers of the 16th century: prior art for any Polish
nunciature cipher); Mazarine M 12 (Grille pour alphabet secret, bare grille); Institut Ms 2495 VIII (Pasini/Rawdon Brown on the Venetian diplomatic cipher).

## Excluded (deciphered or attached decipherment)

- Sorbonne fonds Richelieu: ~120 letters of the maréchal de Richelieu (Vienna embassy 1725-28, MSRIC 30-33, and 1757 Hanover campaign
  MSRIC 58-59) carry "texte déchiffré entre les lignes": class A, closed on the page. Also the Dresde 1816 and Madrid 1817 letters
  ("Déchiffrement de ...") and the Feuquières/Terlon "chiffrée et décryptée" pair (MSRIC 14-21).
- Chantilly/Institut: Henri IV to Pisany 1593 (Eggimann MS 1792, "traduction jointe"; the Pisany pair is a repo target already);
  Louis XIV to Briord 1700 (Institut in-fol. 76, translation facing); Thiers Masson "Espagnols" 1810-11 ("avec déchiffrement");
  Broglie/Hennin 1752-64 (Institut Ms 1228/1234, "avec transcription"); Godefroy Ms 262 ff. 133-134 (Sillery 1594, "Déchiffrement").
- SHD GR 1KT 211 Condé (transcription attached, used as a key lead above); Préfecture de Police AA 295 Cadoudal (déchiffrement 207);
  Mazarine Ms 4802 Mazarin to Bentivoglio (already in the repo from `central_archives`).
- Statistical "en chiffres", WWI/WWII administrative "correspondance chiffrée" (AD Corrèze 550W/90, AD Oise 2 R 190 ...): no ciphertext kept.

## Blocked / not scrapable

- **Biblissima** (`portail.biblissima.fr`, `data.biblissima.fr/sparql`): behind Anubis proof-of-work, returns "Making sure you're not a bot". Not circumvented.
  Its manuscript records mostly mirror Calames/IRHT, so the loss is small.
- **CCFr** (`ccfr.bnf.fr`): redirect loop to an authentication page for scripts. Not used.
- **Mémoire/POP** (pop.culture.gouv.fr): photograph database, not manuscripts; Joconde/Palissy have only "chiffre" as monogram. Not swept.
- Departmental archives with their own viewers (not through FranceArchives) and the many Calames-less libraries were not searched individually.
- The Calames "chiffre" fullText set was parsed on titles and bodies, but only ~330 of 2,203 bodies were read; items whose notice never uses a cipher word are invisible.
- FranceArchives fetch is slow (10-15 s/page); "chiffrée" paged to 32 pages x 50 only; terms with more than 40 pages would have been cut (none reached it).

## Files

`calames_harvest.py`, `calames_detail.py`, `fa_harvest.py`, `fa_harvest2.py`, `fa_merge.py`, `make_calames.py`, `make_fa.py`, `assemble.py`, `kn.py`;
raw: `calames_hits.json`, `calames_detail.json`, `fa_all.json`, `fa_hits*.json`; `candidates.json` is the output.
