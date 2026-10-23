# Re-reading log, R1036 (23 Oct 2026, Claude Opus 5.5; REREAD_BRIEF, batch b19)

## Starting point

Reading audit (22 Oct): "decoded, not read". `R1036_machine_decipherment.txt` split words into letters, carried
DECODE's key misreadings ("hot", "cerd", "dak?") and the dash error of the transcription; only the Greek-project passage
had been normalised (30 Sept, in NOTES), on corrections never applied to the decoder.

## 1. Is there a text already?

- DECODE R1036 re-fetched with the project cookie: 9 images and one attachment, DOC_R1036_D2265 (DECODE's ciphertext
  transcription, = `R1036_transcription.txt`). Every image opened (main checkout `R1036_p1-9.png`): no interlinear,
  margin or slip decipherment; images 5419/5421 and 5420/5422 photograph the same pages twice. A cut-off NB in the lower
  left margin of the last page (image 5423) cannot be read at the edge of the photograph.
- Nationaal Archief: 3.01.25 inv. 610 and 1.02.13 inv. 114 (the 1765 codebook) have no scans online. No edition or
  calendar known (NOTES, Prior work).

## 2. Corrections applied (decode_1765.py, regenerated)

- `R1036_SEPT30`: the 30 Sept key re-readings and alphabetical-place fixes (54^" alhoewel, 314^" behalven, 941^_
  observeeren, 47^_ k, 327 el, 92^_ houden, 121 die, 862^^ het, 448^" con, 223^o veele, 743 dat, 853^_ niet, 559 gehad,
  80 eeren, 135 barred circle zoek, 299 favoriet, 231^o verder); 191 = ens.
- The "^_" DECODE writes after a comma is no longer read as a mark on the next group (normalize_group).
- Transcription: on image 5416 the interlinear group after 362^_ is 191, not 19 ("jong ens").
- From `R1038_scan_readings.tsv`, two "high" readings that fit their only context: 52^o "sedert eenigen" ("alhoewel het
  sedert eenigen [tijd] van het bewuste griekse project geheel stil is"), 71^" "appuyeeren" ("en hun appuyeeren daarop
  te verzoeken"). Not adopted, though read "high", because they do not fit: 178 eerst (later adopted by the R1040 pass,
  where it fits), 553 hoog(st) gedachte, 723 gevangen, 797 gering.
- The R1040 context pass (`R1040_part2_reread_log.md`) added values that also fit R1036: 617^" courier (2x), 178 eerst,
  161 t, 227^" atie, 339^_ man (Rumanzow), 341^_ mari + 343^_ me (maritime acte; meest; menins), 316^" belang, 801^"
  deel (oordeelde). R1036 now has 1,681 of 1,719 groups with a value.

## 3. DECODE key-transcription misreadings (R1038_key_misreadings.tsv)

Constant letter confusions of the R1038 transcriber, normalised in the reading because the corrected form fits every
occurrence (contexts listed by the b19 check):

| DECODE | read | n | contexts |
|---|---|---|---|
| hot | hof | 13 | de antwoort van de hof van Frankryk; het hof van Engeland; aan dit hof te communiceeren |
| chi | che | 8 | Americaensche, Roomsche, Pruyssische (6) |
| cerd | eerd | 10 | geoccupeerd, geaccepteerd, gedetailleerd, gearrangeerd, expliceerd ... |
| ock | ook | 4 | zy heeft ook onlangs; daarover ook |
| toc | toe | 5 | tot nog toe, toekomende, daartoe, toezenden, toegebragt |
| hetten | hebben | 3 | hebben laaten volgen, verslag gedaan hebbende, konnen hebben |
| tri | f | 3 | Frankryk (3) |
| voornocond | voornoemd | 5 | voornoemde (5) |
| zaaon | zaam | 2 | werkzaamheid, genoegzaam |
| geneeg | genoeg | 3 | genoegen genomen (2), genoegzaam |
| dezolve | dezelve | 2 | aan dezelve, met dezelve |
| maaden | maaken | 2 | te maaken (2) |
| di zen | dezen | 3 | in dezen (3) |

13^_ "hot" is written "hof" everywhere, also where the sense is plural (the code does not mark it).

## 4. Reading and scores

`R1036_reading.md` (whole despatch, clear opening and close read on images 5415 and 5423), `R1036_en.md`; decode
`R1036_decode.txt`. Word check (`SUBS=R1038_key_misreadings.tsv b19_wordcheck.py`): every unbracketed word is carried.

| measure | share |
|---|---|
| `_check_reading.py` (modern Dutch list) | 0.09 |
| `b17_score.py` LANG_=nl | 0.056 (6/108) |
| `b17_score.py` HOLES=1 (explicit holes only) | 0.769 (83/108) |

As for battier1686 and dedem1788, the checker's Dutch list does not know the period and code spellings (zyn, gelyk,
Pruyssische, antwoort). Paragraphs on the Greek project, the Armed Neutrality and Prussia's accession, the Vice
Chancellor's reply and the peace negotiations build coherent sentences; the paragraph on England and the American
colonies and the one on the rumours have several holes in a row; the last cipher paragraph does not join the previous
one. Set read, grade B. Open: 38 groups without a value (R1038 cells lost in the binding shadow or too faint) and the
line cut off at the top of image 5417.
