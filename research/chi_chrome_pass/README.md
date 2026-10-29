# Chicago finding aids behind Cloudflare: Chrome pass (28 Oct 2026)

The script sweeps (chi_newberry, chi_northwestern, chi_carli_uic, chi_consortium) could not reach five ArchivesSpace
or portal sites because of Cloudflare/403. The user passed the checks in their own Chrome (Claude in Chrome); the
searches below ran from that tab as same-origin `fetch` calls, about one per second. No check was bypassed by Claude.

Result: 2 candidates (candidates.json), both needs_archive_scan "yes".

1. **Newberry, Charles Williamson papers (VAULT Ayer MS 1006), Box 10 f. 794: "Document written in code (content
   unknown), ca. 1805".** Williamson was Burr's go-between with the British government in 1804-06. Importance 4.
2. Newberry, CB&Q Records, Perkins correspondence, subseries 3 P4.9 "Ciphers", 1877-82, Box 615 ff. 8192-8193.
   Probably railroad telegraph codes; weak.

## Key leads and excluded items
- Newberry, Woolson family papers, Box 1 f. 30-31: *Life of Elijah Woolson*, "written entirely in cipher" by Ira K.
  Woolson (ca. 1850s), with a copy "copied from cipher" by Alvin M. Woolson. Deciphered (the copy is the
  decipherment), so excluded; a check of the copy against the cipher would be a quick test target.
- Newberry, Field Enterprises records (Chicago Daily News), Box 4 f. 52: private code used by Victor Lawson with
  Harriet Dewey, 1906. A code key; messages not described.
- Newberry, Grierson papers (VAULT Ayer MS 3039), Box 3 f. 153: Caziare to "Gen'l Gordon" re cyphers, 1869.
  A letter about army cyphers; no ciphertext described.
- Newberry, CB&Q telegraph cipher code 1897 (Box 91 f. 673), Pullman "Telegraphic Cipher Code Instructions" 1938:
  code books.
- Northwestern, McCormick misc. museum catalogs: "Telegraph cipher of R.S. McCormick & Co., Saint Louis (1884)",
  a commercial code book.
- Chicago History Museum, William Rattle Plum papers (via the consortium portal): "military cipher notebooks", Civil
  War. Plum wrote *The Military Telegraph during the Civil War* (1882); the notebooks are likely Union route-cipher
  keys. Key lead for the Union route-cipher entries already in the catalogue (army1865).

## Coverage

| Site | Terms | Hits | Result |
|---|---|---|---|
| findingaids.library.northwestern.edu (all record types) | 27 terms | cipher 4, ciphers 1, "in cipher" 2, decipher 7, deciphered 13, "code book" 2, codebook 8, "secret code" 2, "in code" 1, encoded 41, rest 0 | noise: music scores titled "cipher", "difficult to decipher" handwriting notes, legislation/survey codebooks, 1935 Ethiopia-aid letters (Moore, Donawa) that only mention cable code, the 1884 McCormick telegraph code |
| archives.newberry.org (all record types) | 31 terms | cipher 11, ciphers 5, "in cipher" 5, deciphered 2, cryptogram 1, chiffre 1, "in code" 1, "private code" 1, cyphers 1, telegraphic 22 (not read), rest 0 | items above; "deciphered" = legibility notes; cryptogram = Steppenwolf play; "Chiffre K.A." = McMurtrie correspondent name |
| archives.depaul.edu | 15 terms | cypher 1 (a person named Cypher) | nothing |
| archivesspace.uic.edu | 15 terms | cypher 1 (Cypher Club scrapbook), "code book" 1 (1990s Code Book Changes), coded 1 (report forms) | nothing |
| explore.chicagocollections.org (collection-level only) | cipher, cypher, "in cipher", cryptogram, "code book", "secret writing", "secret code", "in code", "invisible ink", decipher | cipher 13 collections, decipher 5, cryptogram 3, "code book" 2, "in code" 1, cypher 1 image, rest 0 | collection-level matches; only new one is the CHM Plum papers |

Not reached: Newberry's "telegraphic" 22 hits (railroad/Pullman telegrams, not read); full CHM catalogue (left to the
chi_pritzker_chm_cpl sweep).
