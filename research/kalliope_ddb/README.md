# Kalliope + DDB (non-archive sectors) sweep (28 Oct 2026)

Metadata sweep of Kalliope (SRU) and of the Deutsche Digitale Bibliothek index outside Archivportal-D, following
`research/archive_sweep_2026-10/BRIEF.md`. `candidates.json` holds **6 rows**, all scored from the catalogue text
(`seen: "catalogue"`), none viewed on an image. `make_candidates.py` writes the file and is where rows are edited.

**Result in one line:** both sources are almost exhausted for this purpose. Kalliope was already swept by
`research/central_archives/` (`kalliope_sru.py`), and the DDB outside the archives sector is almost entirely printed
books, theses, journal articles and museum objects. Only one row (Gotha, 1567) is worth a follow-up.

## Method

- **Kalliope.** `https://kalliope-verbund.info/sru?version=1.2&operation=searchRetrieve&query=<term>&recordSchema=mods`
  (https only; http answers 301). A bare term searches all fields; `ead.title=` is title only; `ead.anywhere=`,
  `ead.content=`, `ead.addressee=` and similar return nothing useful. Phrase quotes are not honoured (a quoted phrase
  behaves like its words). 100 records per page, `startRecord` paging. `kal.py` (one query), `kal_harvest.py`
  (all terms, pages to the end, writes `kal_hits.json`), `kal_filter.py` (keeps records whose title, note or abstract
  contains a cipher stem).
- **Terms, run 1** (hits): chiffriert/-e/-en/-er 17; Chiffre/Chiffren/chiffre/chiffré 224; Geheimschrift(en) 114;
  Ziffern 446; dechiffriert 9; Dechiffrierung 12; entziffert 170; Entzifferung 160; verschlüsselt/-e 61;
  Kryptogramm 7; Geheimzeichen 3; Geheimalphabet 2; Geheimtinte 4; Geheimsprache 30; chiffrée 7; déchiffrer 18;
  cifra/cifre 3; cifrada 2; cifer 2; cipher 3; nomenclator 35; Nomenklator 3; Kryptographie 3; Chiffern 64; and
  about 60 variants that returned 0 (Chiffrenschlüssel, Chiffrierschlüssel, Ziffernschrift, cijfer*, ontcijfer*,
  cifrato, "in notis" ...). Full list is in `kal_harvest.py`'s input at the time; run 2 terms are in `kal_terms_run2.txt`
  (Geheimbrief, codiert, Geheimcode, Ziffer, Chiffer, Zeichenschrift, Steganographie ...).
- **Counts.** 2,666 distinct records (run 1) + 297 (run 2). Of these 441 had a cipher stem in title, note or abstract
  (`kal_kept.json`). Read as one-line contexts, all 441.
- **DDB.** `https://api.deutsche-digitale-bibliothek.de/2/search/index/search/select?q=<term>&rows=500&start=N&wt=json&fq=-sector_fct:sec_01`
  (the public Solr index, no key; `sec_01` = archives = Archivportal-D, excluded). `ddb_harvest.py` ran the Kalliope
  term list plus extras (chiffrier*, dechiffr*, verschlüssel*, geheimschrift*, Zahlenschrift, secret writing, cypher ...):
  **20,419 distinct records** (sectors: libraries 17,961, museums 1,638 + 458, others 362). Filtered to a cipher stem in
  label or description: 2,437 (`ddb_strong.json`). The 20 MB raw harvest was not kept; rerun the script to regenerate.

## Noise (why the yield is small)

- **Kalliope:** "Chiffre" = pseudonym or sigil of a reviewer (Zarncke / Literarisches Centralblatt, 120+ letters),
  "Chiffren" as a literary or philosophical term (Jaspers, Genazino, Basel Eichenwald "Chiffren für Orchester"),
  "Ziffern" = numerals, "basse chiffrée" music, "Nomenclator botanicus" (Steudel) and its publisher correspondence,
  "Geheimer Rat", Stammbuch dates, the Volkelt letters (already catalogue 528).
- **DDB:** the index covers digitised full text of books (Kapitel / Abschnitt / Hochschulschrift), so "decipher",
  "cipher", "Chiffre", "verschlüsselt" match modern science, cryptography theses, Enigma and Kryha machines (HNF museum),
  the Badisches Landesmuseum Orientalism posters ("Chiffre des Eigenen"), BSB / SBB music manuscripts "basse chiffrée".

## Rows (6)

| Row | Why kept |
|---|---|
| Kraus → Johann Wilhelm of Saxe-Weimar, 1567, key + four letters (Gotha Chart. A 40) | class A pair, 3/3/2, not digitised |
| SLUB Mscr.Dresd.N.103, Padua c. 1537, alchemical "Geheimschriften" | digitised, may be an alphabet only |
| Silbermann, Specificationen 1753 (Mscr.Dresd.App.3165 Bd. 6) | trade notes partly in cipher |
| Minna Werner ↔ Kinkel, Feb 1860 | private family cipher, low |
| SLUB Mscr.Dresd.J.345, alchemical "Geheimschrift" Bl. 248 ff. | low |
| Zofingen Pb 82, spells in Geheimschrift | low |

## Already held (dropped after `known.py`)

Wessenberg 1798 (Konstanz P 1839 5, 21; catalogue 521), Anderwert 1802 (A 33 12; 523), Ranke's Drakenburg letter (526),
Körner 4 Jul 1813 (527), Volkelt ↔ Seeliger (528), Wolzogen 1792-93 (525), Münster → Kestner 1819, Hohenlohe La 120 Bü 305,
Jung-Stilling diaries (rejected: transcripts survive), Rubens → Olivares 1629 (Rubens struck out the cipher himself),
Jablonski → Ráday 1704-12 (Latin plaintext under the cipher; rejected in `research/oldest/scan_2026-09-23`),
Musculus → Blarer 1554 (printed), Landgrave Moritz of Hesse alchemical Geheimschrift (Europeana sweep), Ilten papers
(`targets/ilten*`), Goethe's Chiffre-Briefe (resolution in hand), Corona Schröter ciphers (deciphered by Müller).

## Seen and left out

- **Louis XV → Touche de la M., Choisy 19 Jun 1752** (Coburg autographs): "Betr. vier chiffrierte Briefe", a letter about
  ciphered letters, no cipher in it.
- **Karl Stein → Goetzen, Königsberg 6 Sep 1808**, DHM 1988/1807, "Vorlage für einen chiffrierten Brief": a draft of
  a letter meant to be enciphered; the DDB record shows no ciphertext. The enciphered fair copy in the Goetzen papers
  (Silesia 1808, Prussian reform and rising plans) would be the target; look in the DHM Nachlass.
- **Gotha, Cyprian Chart. A 299 S. 675-676** "Chiffrierte Benediktion": undated, a few lines.
- St. Gallen Vadiana Ms 403 (1530): alchemical, the key to the Geheimschrift is on 102v (resolved).
- Stefan George → Stahl 1890 "Geheimcode": his invented Romance language, not a cipher.
- Basel UB: Camerarius "Geheimbrief an den König von Schweden" (1627): a secret letter, not enciphered.
- Stammbücher with "Geheimzeichen" (Halle ULB, Bamberg): friendship signs, not a cipher.

## Key leads (bare keys / tables, not rowed)

- Gotha Chart. A 40 Bl. 186a: the key of the 1567 row above.
- GWLB Hannover Ms XXIII 1234:31,1 pp. 386-391: "Chiffre-Tabelle" 1745-46 (already used for `ilten1743`).
- Basel UB (Bernoulli papers, Gotha Bestand): "Clé du chiffre de J. R. v. Patkul" (Miscellanae, Bl. 5-7).
- SLUB Dresden Buchhandschriften, Miscellanea historica 1699-1750, S. 295-297: "Table de chiffre", "Chifre du Chevalier Constantin".
- SBB Orientalia: "Alphabete und Arten von Chiffreschrift" (Syriac Sammelhandschrift 1827, Bl. 89v-92v) and "Mehrere Arten
  von Chiffre-Schrift" (Neo-Aramaic, 17th c., Bl. 1r-19v): oriental cipher alphabets.
- Gotha, Gerhard Gelehrtenbibliothek: magic manuscripts with inserted "Geheimalphabete (Brillenbuchstaben)", pre-1668.
- Hohenlohe-Zentralarchiv La 120 Bü 629: collection on steganography (book extracts).
- Printed with facsimile: Sebastian Schertlin's letters and the Geheimschriften of the Schmalkaldic League (BSB, Briefsammlung);
  Die Geheimschriften des Fürstbistums Münster 1650-78 (DNB, book); Tranchedino's codex (ONB 2398).

## Not reached / blockers

- Kalliope's free-text index is thin (about 3,000 records for all cipher stems). Archive finding aids that list
  "chiffriert" per letter sit in their own systems (Arcinsys, OLF, Findbuch.net); this is the Archivportal-D sweep's ground.
- No images were viewed, and the Gotha 1567 pieces have no digital copy.
- DDB object pages for the few leads were not fetched; Kalliope record pages were checked for Chart. A 40 only.
- Latin/French/Italian/Dutch queries returned almost nothing (Kalliope's coverage is German-language literary and
  Nachlass material; Dutch `cijfer*` gave 0).

## Scripts

`kal.py`, `kal_harvest.py`, `kal_filter.py` (Kalliope), `ddb_harvest.py` (DDB), `make_candidates.py`.
`kal_hits.json` (all Kalliope records), `kal_kept.json` (cipher-stem subset), `ddb_strong.json` (DDB subset).
