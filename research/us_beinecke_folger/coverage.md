# Coverage: Beinecke (Yale) and Folger sweep, 28 Oct 2026

All requests made from the built-in browser (the hosts sit behind an AWS WAF JavaScript challenge that answers
`curl` with an empty 202), one request every 2.5-3 s per host, User-Agent of the browser. No login, no CAPTCHA.

## Yale

### archives.yale.edu (Archives at Yale, ArchivesSpace)

- `GET /search?q[]=cipher&repo_id=11` and `GET /` both returned **403 Forbidden** (28 Oct 2026). Not retried.
  The same ArchivesSpace records are indexed in Quicksearch's "Archives or Manuscripts" data source (below),
  so the finding-aid components were still searched; only the per-component detail pages (notes, scope) were
  out of reach. Quicksearch's own detail page for an archival object redirects to archives.yale.edu and fails.

### search.library.yale.edu (Quicksearch), data source `/archives` (Orbis catalogue + ArchivesSpace components)

`/archives?q=<term>&per_page=100&page=n`, all pages harvested. Hit counts as shown by Quicksearch
(stemming: "cipher", "ciphers", "ciphered" and "in cipher" give the same 162):

| query | hits |
|---|---|
| cipher | 162 |
| ciphers | 162 |
| ciphered | 162 |
| "in cipher" | 162 |
| "partly in cipher" | 26 |
| cypher | 32 |
| cyphers | 32 |
| "in cypher" | 32 |
| "cipher letter" | 3 |
| "cypher letter" | 0 |
| cryptogram | 39 |
| cryptography | 20 |
| cryptographic | 16 |
| "secret writing" | 9 |
| "secret alphabet" | 0 |
| "secret characters" | 0 |
| nomenclator | 2 |
| chiffre | 6 |
| cifra | 15 |
| Geheimschrift | 0 |
| steganography | 5 |
| "code letter" | 5 |
| "in code" | 7,144 (phrase not honoured; first 1,000 screened by title only, nothing relevant) |
| decipher, decipherment, deciphered, "cipher key", "cipher telegram", cifrato, "en chiffre", chiffré, zifra, ziffer | run after "in code"; see README |

Distinct records harvested: 1,180 (most from "in code"); 270 from the cipher-family terms, all read by title,
date, call number and "Found in" path.

### collections.library.yale.edu (Yale Digital Collections, Blacklight JSON)

`/catalog.json?q=<term>&per_page=100` (description search):

| query | hits |
|---|---|
| cipher | 54 |
| ciphers | 54 |
| cypher | 9 |
| "in cipher" | 20 |
| "partly in cipher" | 13 |
| cryptogram | 4 |
| cryptography | 3 |
| "secret writing" | 2 |
| "secret alphabet" | 0 |
| nomenclator | 0 |
| chiffre / chiffres | 8 / 8 |
| cifra / cifre | 1 / 1 |
| Geheimschrift | 0 |
| ciphered | 0 |
| "cipher letter" | 0 |
| encoded / encrypted | 0 / 0 |
| code book (unquoted, useless) | 64,662 |

Call-number facets listed for digitised items: GEN MSS 146 (29 digitised), GEN MSS 817 (9), OSB MSS 2 (81),
OSB MSS 5 (32), OSB MSS 6 (5), OSB MSS 31 (4), OSB MSS FILE (636), GEN MSS 1495 (0), OSB MSS 64 (0),
WA MSS S-4203 (0), GEN MSS VOL 1120 / VOL 105 / 177 (0).

## Folger

### catalog.folger.edu (TIND)

`/search?p=<term>&rg=200&jrec=n&of=xm` (MARCXML), all pages; manuscripts picked by leader/06 = t, p, d, f
(46 manuscript records among the cipher-family hits), the rest (Baconian cipher books, printed Porta, Morland,
Wing items) screened by title.

| query | records |
|---|---|
| cipher | 247 |
| ciphers | 247 |
| cypher | 87 |
| cyphers | 87 |
| "in cipher" | 17 |
| "partly in cipher" | 3 |
| "cypher letter" | 1 |
| "cipher letter" | 0 |
| cryptogram | 36 |
| Cryptograms (genre) | 36 |
| cryptography | 63 |
| cryptographic | 9 |
| "secret writing" | 30 |
| "secret alphabet" | 0 |
| "secret characters" | 0 |
| nomenclator | 105 (printed Nomenclators, dictionaries) |
| chiffre | 13 |
| cifra | 4 |
| Geheimschrift | 3 |
| ciphered | 3 |
| cyphered | 1 |
| "in cypher" | 5 |
| steganography | 18 |
| "in code" | 2 |
| "numerical code" | 1 |
| "Ciphers (codes)" | 2 |
| decipher | 18 |
| deciphered | 103 |
| "cipher key" / "en chiffre" | 0 / 0 |
| code | 439 |
| alphabet | 782 |
| "invisible ink" | 5 |
| numbers (capped at 2,000) / secret (600) | screened by note text only |
