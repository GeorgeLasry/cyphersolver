# Prior-work check: BnF Français 3013 no. 43 (Bilia to the Duke of Milan, Burgos, 22 Nov 1527) and no. 42

Checked on 2026-10-20 (JST) by a reviewer who took no part in the decipherment and tried to find earlier readings.

## Category
**Not found.** This is not a claim of "first". **In the places searched (listed below, 2026-10-20) no earlier decipherment or plaintext of no. 43 was found.**
- No edition, article or catalogue printing the text of no. 43 was found.
- On the images, no contemporary decipherment notes are visible (but not every frame was inspected; see below).
- No. 42 (ff. 99r-v) is in a different cipher and was not the subject here; no earlier reading was found for it either.

## Main evidence
1. BnF finding aid for Français 3013: no. 42 "Lettre, en italien, avec chiffre, de BILIA... al signor JO. Francesco Zaberna..." (Fol. 99); no. 43 "Lettre, en italien et en chiffre, de JO. ANTONIO BILIA... duca de Milano... De Burgos, XXII novembris 1527" (Fol. 105 in the catalogue). It does not mention a decipherment. Read via a copy of the finding aid at NoAutopilot/cipher-lab, sources/bnf-findingaids/2026-10-09/cc494715.html. Catalogue folio numbers are 3 higher than the ink folio numbers.
2. Cyphersolver (dbourdeau/cyphersolver, origin/main 0258b8ab, 2026-10-18; unchanged after fetch): CATALOGUE.md line 59 lists nos. 42-43 as "keys in hand" with no reading. No match for 3013, Bilia, Zaberna, R5258 or R5237 in the titles and bodies of all 52 issues; PR #34 concerns Gilino and only uses R5258 as the key.
3. Existing use of the same key R5258: Gilino to Francesco II Sforza (15 Sep 1527, Cotton Vespasian C IV ff. 214-218, DECODE R8572), in Cyphersolver (targets/gilino1527, docs/gilino1527.html) and Cryptiana ("Servo el Gilino's Cipher with Superscript Digits (1527)"). That is a different letter, not a reading of no. 43. The key sheet is docketed "Cum equite Bilie / extracta ex cifris", i.e. drawn from Bilia's correspondence.
4. Printed calendars (full-text _djvu.txt from archive.org, grepped):
   - CSP Spain iii/2 (calendarorleters0003vari): the November 1527 entries (Burgos, 10, 13, 15, 22 Nov etc.) contain no Bilia/Billia/Zaberna item. Gayangos's notes say "Billia and Bilia, who in January 1526 represented the Duke of Milan in Spain" and "Francesco Viglia, Villa or Billia... Milanese agent... The Duke had then in Spain another agent named Giulino, Gilino... whose prefix was Camillo". So the person is known, but **no plaintext or decipherment of this ciphertext is printed**. Gayangos gives the first name Francesco, the catalogue "Jo. Antonio" (identity not checked).
   - Calendar of State Papers Venice iv (calendarofstatep4187brow): Taverna is indexed as the Duke of Milan's ambassador in France (Zuan Francesco de Taberna/Taverna; pp. 345, 381, 395, 487, 1079; letters 407, 409, 480). No Bilia entry. Consistent with no. 42's addressee but not relevant to the reading.
   - Letters and Papers iv (letterspaperspt204greauoft, lettersandpaper11offigoog): no Bilia/Billia/Zaberna/Taverna (OCR grep only; variants Biglia, Viglia, Bylia, Zabarna also absent).
5. Cryptiana (Last-Modified): unsolved.htm (2026-10-19 23:08 GMT), GL.htm (2026-10-15), francis.htm (2023-12-07), crypto.htm (2026-10-15), spanish2C.htm (2026-10-02), spanish2.htm (2025-10-03), spanish.htm (2022-05-29), henryviii.htm (2024-10-09), wolsey.htm (2022-01-10), AlonsoSanchez.htm (2025-09-08): no Bilia/Zaberna/Taverna/3013 (only the Gilino article). Blog feed (cryptiana.blogspot.com, 143 posts, Last-Modified 2026-10-18 22:21 GMT): nothing.
6. Cryptoole idx.json (854 entries, Last-Modified 2026-10-17 18:37 GMT): no Bilia/Zaberna/Taverna/fr. 3013. R5258 appears only as a key record (Carteggio Sforzesco 1591_24).
7. GitHub: NoAutopilot/cipher-lab (main, latest commit 2026-10-20T02:17Z): no path names with Bilia/Zaberna/3013/R5258; fr. 3013 appears only as an exclusion ("bourdeau-named:fr.3xxx") in three files under sources/solver-diffs. pangoleen/cipher-readings (877 paths), el-descifrador/cabinet-noir (502 paths) and the names of all 10 BravoBravoIX repositories: nothing. Code search (gh api search/code, 8 s spacing, 10 queries): the only relevant hits are Cyphersolver and cipher-lab.
8. DECODE (https://de-crypt.org/decrypt-web/RecordsView/5258 and /5237): the public part shows key records. 5258 = Carteggio_Sforzesco_scat._n.1591_24 (Simple/Homophonic/Nomenclatures; "Access mode: Authentication required"); 5237 = 1591_3 (Numerical). A record for fr. 3013 could not be searched: RecordsSearch is an input form and was not usable here.
9. Gallica images (btv1b9060138r, IIIF 1500 px; f159-f167 downloaded): viewed f159, f160 (no. 42), f164, f165 (no. 43) and f167 (address of no. 43). No contemporary decipherment is visible between lines or in the margins (only show-through, and the clear-text address, closing and signature). f161, f162, f163, f166 were downloaded but not viewed.

## Searched, nothing found
- Any edition, article or catalogue giving the plaintext of the Bilia/Zaberna/Taverna letters (all the above).
- Web search (5 queries combining Bilia, Zaberna, Taverna, Cerioni, Sforza): nothing relevant.

## Could not be checked (outside the conclusion)
- **Cerioni 1970** (La diplomazia sforzesca nella seconda meta del Quattrocento e i suoi cifrari segreti): text not opened. The title points to the later 15th century. Cyphersolver's CATALOGUE.md line 59 says the keys for nos. 42-43 are printed there; whether 1527 keys are in it is unverified (doubtful from the title; based on search snippets only, so not used as evidence).
- Giudici, "La cancelleria segreta sforzesca al tempo del duca Francesco II (1522-1535)", Reti Medievali Rivista 19/2 (2018), DOI 10.6092/1593-2214/5871: full text not obtained (doi.org timed out).
- The original or finding aid for ASMi Carteggio Sforzesco, Spagna 1527, other studies using Cerioni; the Calendar of State Papers Milan: not opened.
- Google Books and full-text search inside archive.org books: not done (archive.org was used only to locate volumes by title and fetch _djvu.txt).
- DECODE records for fr. 3013 and DECODE images (login required).
- The cipher-lab tree from the GitHub API was truncated (truncated=true, 61,315 paths), so the path-name grep is not exhaustive; code search was used to compensate, with no guarantee of completeness.
- Cryptiana milan.htm, sforza.htm, italian.htm, italy.htm return 302 (target not followed).

## Notes
- No earlier reading was found, but Gayangos (CSP Spain iii/2) already records that Bilia was the Duke of Milan's agent in Spain; this can be cited for the person.
- R5258 was drawn from Bilia's correspondence and already reads Gilino's letter (Cyphersolver, Cryptiana). Applying it to no. 43 is a new application, but the discovery of the key predates it.
