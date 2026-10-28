# Newberry coverage (28 Oct 2026)

Endpoints: CARLI I-Share Primo VE JSON API (primo.py; view 01CARLI_NBY:CARLI_NBY, scope MyInstitution, all Newberry
records), CARLI CONTENTdm dmwebservices (carli.py; nby_* collections), collections.newberry.org item pages (ndc.py),
archive.org (Butler 1937 checklist full text), newberry.org PDF checklists (Cusk English, Wall Italian, Wall French).
Raw hits: primo_hits.jsonl, carli_hits.jsonl, ndc_items.jsonl.

## Primo, all record types (hits)
cipher 372; cypher 258; ciphers 322; ciphered 144; deciphered 193; decyphered 13; cryptogram 16; nomenclator 133;
chiffre 159; chiffres 116; chiffree 79; cifra 35; cifras 73; cifrado 5; en cifra 10; Geheimschrift 2; secret writing 693
(500 fetched); partly in cipher 5; cipher letter 44; cipher code 83; telegraphic code 2; cipher telegram 2.
Almost all are printed books and articles (the Newberry holds many cryptography books). Not triaged individually.

## Primo, manuscripts facet (rtype=manuscripts; the useful filter)
cipher 15; cypher 10; ciphers 9; ciphered 3; decipher 0; deciphered 1; cryptogram 1; cryptography 1; nomenclator 1;
chiffre, chiffres, cifra, cifrado, cifras, cifrada, Geheimschrift, cifrata, zifra, ciffra, cyfra, cifrar, decifrado,
descifrado, enciphered, encoded, chiffre (accented), cifrato, Chiffren, clave, deciphering: 0 each;
secret writing 1; in code 22; code 22; cypher letter 2; steganography 1; invisible ink 3; sympathetic ink 1; coded 7;
code book 8; secret code 2; secret 25; hieroglyphic 1; private code 3; shorthand or code 1; in cypher 10; symbols 37;
numerical code 1; code words 1; numbers 121; in figures 75; telegram 10; spy 16; intelligence 5; key to the cipher,
cipher key, lettera in cifra, telegraph code, cablegram, partly in code, Deseret alphabet: 0 each.
Collection-type facet (finding-aid-level records) returned 0 for every cipher term.
All manuscript hits were read in context; real cipher content only in the items listed in README.

## CONTENTdm (collections.carli.illinois.edu), terms x 9 collections (chicago, eeayer, graff, mms, dig, pullman, rrlife, music, cgs)
cipher: nby_dig 1; cypher: nby_graff 1 (Wilkinson memorandum); ciphered, cryptogram, cifra, chiffre, nomenclator: 0;
in cipher: dig 1; code: dig 2, cgs 253 (Chicago Genealogist sheets, noise); secret writing: mms 1 (Colby letter, Civil
War, not checked); decipher: mms 4 (Civil War letters, likely handwriting difficulty), cgs 39 (noise).
Newberry Digital Collections (collections.newberry.org) search "cipher": 17 results, 17 checked; only the characters-table
page is a cipher (others: interviews, correspondence, a 1984 fiction excerpt titled "The Cipher").

## Printed guides searched
- Butler, Check list of manuscripts in the Edward E. Ayer collection (1937), archive.org full text: grep for cipher,
  cypher, cifra, chiffr, code, secret, decipher, clave, cryptog gave no cipher entries (only 'secretary', 'codex').
  OCR quality is poor; a miss is not proof.
- Cusk, Checklist of English manuscripts 1500-1865: Burr letter largely in cypher; coach painter's cipher book (monograms).
- Wall, Post-1500 Italian (378 items) and French (about 440) checklists: no cipher letters.
- Lietz / Robles calendars of Philippine documents and Greenlee/Luso-Brazilian guides: not available as text.

## Blocked
- archives.newberry.org / mms.newberry.org (ArchivesSpace finding aids): Cloudflare check (403 to script; challenge
  page persisted in the built-in browser). Stopped, not bypassed.
- OCLC ArchiveGrid and HathiTrust catalog search: 403 / challenge; stopped.
