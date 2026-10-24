# Archives nationales / FranceArchives sweep (first pass, 24 Oct 2026)

A title search of the FranceArchives portal (which carries the Archives nationales inventories plus departmental,
SHD, ANOM and other French holdings) for cipher words, checked against the repo ledgers and DECODE. This is a
candidate list. No target has been opened from it yet. BnF/Gallica was swept separately (`../gallica_sweep`).

## Method

- **Endpoints.** `https://francearchives.gouv.fr/fr/search?es_escategory=archives&items_per_page=50&q=<term>&page=<n>`
  returns item-level result cards (`.fa-sr-card`: title, Cote, Période, Fonds, Lieu de conservation). The item pages
  are `/fr/facomponent/<sha1>`. The site sits behind a WAF that blocks curl ("Attack detected"), so the harvest ran
  as `fetch()` calls in the in-app browser. The page count comes from the "page 1 sur N" in the title.
- **SIV** (`siv.archives-nationales.culture.gouv.fr`) returned HTTP 503 all session, to curl and in the browser. The
  AN inventories reached this sweep only through FranceArchives.
- **Terms** (24): "lettre(s) chiffrée(s)", "en chiffre", "lettre(s) en chiffre", déchiffrement, déchiffré(e),
  "non déchiffré(e)", "clé/clef de chiffre", "table(s) de chiffre", cryptogramme, "écriture secrète", cifra,
  "dépêche(s) chiffrée(s)", "chiffre(s) diplomatique(s)", "grille de chiffre", "partie en chiffre", "en partie chiffrée".
- **Counts.** 849 raw hits, 769 unique, 156 with a cipher word in the title. After dropping epigraphy/Maya/Breuil
  "déchiffrement", statistics ("en chiffre") and post-1950 rows, 29 pre-1950 cipher rows are kept in `hits.json`.
  Only 2 of the 769 are flagged as digitised, and neither is a cipher item.
- **Known check.** Each cote and name was grepped in `catalogue.json`, `README.md`, `SOLVED_CATALOGUE.md`, `targets/`
  and `research/`, with no hit. DECODE (`research/catalogue_harvest/decode/list.json`, 10,106 records) has **no
  Archives nationales record at all**. The French holdings on DECODE are BnF (~540) and AD Nord B 19/297-298 (11).

## Best leads (candidates, none digitised)

| # | Holder / cote | Date | What | Note |
|---|---|---|---|---|
| 1 | AN 402AP/13 (Mornay et Soult) | 1549-1623 | Duplessis-Mornay "lettres chiffrées (B-V)" plus **the cipher** of Mme de Mornay's correspondence with Mme du Bourget | Ciphertext and key in one box. Mornay's *Mémoires et correspondance* (1824-25) should be checked before anyone opens it |
| 2 | AN CC//499-545 dossier 209 (Cour des pairs) | 1816 | Cipher letter to General Jacquemard, in a police dossier (affaire du 13 février 1820) | Bonapartist conspiracy. No reading found |
| 3 | AN O/3 Maison du Roi, dossier 7 | 1800-1812 | Perruchon accounts: "correspondance tronquée et en partie chiffrée" | Royalist emigré network |
| 4 | AN T//478/1 | 1684-1793 | General Biron (Lauzun) papers, "lettres chiffrées" | Biron's 1792-93 army letters |
| 5 | AD Charente-Maritime 4 J 1524 | 1623-1732 | Robert de Boissiran, correspondence "dont plusieurs lettres chiffrées" | Private, possibly from the 1620s Huguenot La Rochelle era |
| 6 | Archives d'Alsace (Strasbourg) C 645 | 1760-1763 | Choiseul to Kau, letters partly in cipher (Folard, Munich) | Intendance d'Alsace |
| 7 | AN 557AP/10 (Bruant des Carrières) | 1672-1674 | 25 pieces: Bruant's cipher tables with the court, Louvois, Courtin (Liège) | **Keys only.** Useful against Bruant/Louvois ciphers elsewhere, e.g. Vincennes A1 |
| 8 | AD Seine-et-Marne 142J5 | 22 Dec 1699 | Unsigned letter from Rome to the abbé Bossuet, partly in cipher | Likely printed decoded in Urbain-Levesque, *Correspondance de Bossuet* t.12 (archive.org `correspondancede12boss`). Check that before calling it new |

## Closed leads

- **Trésor des chartes J 941-968** (Moltzan 1519, Albany 1527, Vachon): each entry says "(et déchiffrée)" or is the decipherment.
- **Consular letters** (Marine/AE B/I: Cádiz 1719-22, St Petersburg 1745, Algiers 1750-73, Amsterdam 1778), **ANOM** Montcalm 1758
  and La Luzerne 1782: the inventory summarises each letter's content, so they were deciphered at the time or the file holds a clear copy.
  The ciphered originals could still be useful as key-recovery material, since the plaintext summary is known.
- **Directoire AF/III**: Zwanziger 1796 has its decipherment (pp. 67-69). Reinhard 1795 is a decipherment. The Hoche-Clarke letters
  (pp. 84, 108) are summarised, so they are low priority; check Hoche's printed correspondence.
- **SHD Bruix 1799**: the Talleyrand cipher letter is filed next to its decipherment. Froc de La Boulaye's letters are summarised.
- **Marie-Antoinette / Fersen (440AP)**: a known corpus, already studied (the Fersen ciphers and the redaction work).
- **Bibliothèque Thiers Ms Masson 302**: the Desroches papers are "traduites", so deciphered.
- **F/17 / F/12/2273** (an III): proposals for stéganographie and arcanographie, which are cipher systems, not messages.
- **1890-1945** dépêches chiffrées, WWI Section du chiffre, Riom 2W/69: administrative or service files, kept with the clear texts.
- **MAE La Courneuve** (1AE, 53MD, CPCOM) hits: noted and skipped, as the brief asked.

## Limits

- This is a title/abstract search only. AN ambassador and consular volumes rarely say "chiffre" in their abstracts, so real
  coverage is much larger. SIV was down, so AN-only inventories not published to FranceArchives were not reached.
- No candidate is digitised. Every lead needs a reading-room visit or a reproduction order.
- No print check was done on leads 1-6 beyond a web search. Mornay (1824) and Bossuet (Urbain-Levesque) are the obvious first checks.
