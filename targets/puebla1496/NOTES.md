# Ferdinand and Isabella → De Puebla, Almazán, 21 June 1496, ciphered article (catalogue 616)

Status: no write-up. Contributed by WAINUT (https://github.com/WAINUTAI), 27 Oct 2026. The cipher was deciphered at
the time, and Bergenroth calendared it in 1862. This contribution adds the identification, a sample decoded with the
extant key, and a rule for reading the key's C ligatures.

AGS, Patronato Real, leg. 52, doc. 47. PARES description
[2207769](https://pares.cultura.gob.es/ParesBusquedas20/catalogo/description/2207769), viewer
[show/2207769](https://pares.cultura.gob.es/ParesBusquedas20/catalogo/show/2207769), 12 images, ff. 394r-399v. Old
stamp "T.c.Y.2", which is Bergenroth's "S. E. T. c. I. L. 2". PARES title: "Carta de los Reyes Catolicos al Doctor
Puebla sobre la urgencia de activar la amistad con Inglaterra por el perjuicio que se sigue al comercio español", 1496.

## What the unit holds

| image | folio | content | CSP Spain I (1862) |
|---|---|---|---|
| 1-3 | 394r-395r | clear draft, Ferdinand and Isabella to De Puebla: "Despues que vos escrivimos a xxj de junio pasado ...", ending "de la villa de Almaçan a vj de julio de xcvj" | no. 141, 6 July 1496, pp. 107-108 |
| 4 | 395v | 19th-century notes: "Almaçan a 6 de Julio de 1496"; "Copiada para los Sres. Pidal y Salva, hoy 23 de Agosto de 1859" | |
| 5-6 | 396r-396v | **the cipher**: "Traslado de un capitulo que se escrivio en una de xxj de junio de xcvj", clear words and Great Roman Numeral code | **no. 138, 21 June 1496, pp. 106-107** |
| 7-8 | 397r-397v | blank; note on 397v: "Nota: este capitulo de carta se ha descifrado y se halla inserto en la letra en claro en la minuta de la carta" | |
| 9-11 | 398r-399r | clear draft, closing leaves of the letter of 21 June 1496 (English carrying trade with France harms Spain), ending "de la villa de Almaçan a xxj de junio de xcvj" | no. 137, 21 June 1496, pp. 104-106 |
| 12 | 399v | blank | |

Bergenroth's no. 138 reads: "Ciphering of one article of the despatch, written the 21st June 1496. Doctor de Puebla.
... It begins with the words: 'y quanto alo que dezis que el Rey de Ynglaterre vos dixo que tenia buenas nuevas de los
negocios de Escocia' ... Written in the Latin numbers used as cipher. The key is extant."
[BHO pp. 99-107](https://www.british-history.ac.uk/cal-state-papers/spain/vol1/pp99-107),
[pp. 107-114](https://www.british-history.ac.uk/cal-state-papers/spain/vol1/pp107-114).

The PARES title comes from the clear draft of 21 June ("perjuicio ... al comercio"). The cipher on f. 396 is the
ciphered article of that letter. The plaintext exists twice: in the minuta of 21 June, which carries the article in
clear (note on f. 397v), and in Bergenroth's calendar, as an English abstract with the opening quoted. The
catalogue's "1496 (undated)" can be dated. The cipher is of 21 June 1496 and the second draft of 6 July 1496, both
written at Almazán.

## The key and the C ligatures

The key is AGS PTR leg. 52 doc. 33
([show/2207755](https://pares.cultura.gob.es/ParesBusquedas20/catalogo/show/2207755), 200 images). The entries used
here were read on key images 30, 37, 48, 50-54, 100-101, 110 and 116 (`key_excerpt.tsv`).

**C-count rule.** The scribe writes runs of C as ligatures, in three forms. On the key and on f. 396r:

- the plain "ar"-shaped ligature = CC (key image 110: 1778-1785, no mark);
- the same ligature with a superscript o = CCC (key images 48, 51, 116);
- a wider "m"-shaped ligature with an overbar = CCCC (key images 52-53).

The anchor is MDCLVII "o" = 1657 (key image 101). Tomokiyo notes only that "CC and CCC are in ligature". That note
alone does not settle the count. Read without the rule, the "que" group of line 1 could be taken as MDCCLXXXV, which
is one of the "poco ..." entries.

## The sample

`sample_transcription.txt` gives the heading and lines 1-3 of f. 396r. `decode_sample.py` writes
`sample_decryption.txt`:

> Traslado de un capitulo que se escrivio en una de xxj de junio de xcvj . ij[?] . **[dotor de puebla]**
> y quanto alo que dezis **[que] [el Rey de Inglaterra]** vos dixo que tenia buenas nuevas delos negocios de
> **[el Rey de Escocia]** esto no viene de otra parte sino que **[nuestro]**s ...

This is Bergenroth's quotation, group for group. The controls in the same script give no sentence. A shift of one
entry gives "dotor de talavera", "la Reyna de Inglaterra" and "el Reyno de Escocia". Reading every ligature as CC
gives 755, 1785, 788 and 721. Shuffling the groups gives, for example, "negocios de [dotor de puebla]".

Correction made in the check: the group in line 2 is **DCCCCXXI = "el Rey de Escocia"**, written with the wide
ligature and overbar. It is not "Escocia". In the key, 922 is "el Reyno de Escocia", and no bare "Escocia" entry
stands near it. The cipher therefore says "negocios de [el Rey de Escocia]". Bergenroth's "negocios de Escocia"
is his own short form, or the minuta's wording. Line 3 ("nuestros [...] que avemos enbiado") fits the no. 137
abstract: "the Spanish ambassadors have obtained a solemn promise from the King of Scots". Its groups are uncertain
and marked [?].

Reading and translation of the sample: `sample_reading.txt`, `sample_translation.txt`.

## Proposed catalogue change

616: an earlier-solution pointer. The cipher is CSP Spain I (1862) no. 138, pp. 106-107, the ciphered article of
Ferdinand and Isabella to De Puebla, Almazán, 21 June 1496, and the minuta of the same letter carries it in clear.
The same unit holds the clear drafts no. 137 (21 June 1496) and no. 141 (6 July 1496). Date: 21 June 1496. Direction:
Ferdinand and Isabella → De Puebla.

## Remaining gaps

- f. 396r from line 4 and f. 396v (about 45 lines) not transcribed - blocker: not-attempted; the extant key and the minuta would give the whole article, but the content is known from the minuta and CSP no. 138, so it was not done
- Line 3 groups (the first group, the group after "y", and the group before "ovieron") - blocker: illegible; doubtful at the largest size PARES serves for image 5 (1005 x 1402 px)
- The dating lines of the two clear drafts (ff. 394r-395r, 398r-399r) were read once and not re-checked - blocker: not-attempted; not needed for the identification
- Whether the 6 July 1496 draft (no. 141) was printed in the Colección de documentos inéditos (the 1859 copy "para los Sres. Pidal y Salva") - blocker: no-key-material; one search, no hit

## Escalation

- [x] siblings: the clear drafts in the same unit (ff. 394r-395r, 398r-399r); puebla1495 (catalogue 615, same key)
- [x] clear-pages: the minuta carries the article in clear (note on f. 397v)
- [x] known-keys: AGS PTR leg. 52 doc. 33, key images 30, 37, 48, 50-54, 100-101, 110, 116
- [x] print: CSP Spain I nos. 137, 138, 141 (BHO); the 1868 Supplement has no 1496 section
- [n/a] key-rebuild: the key is extant and needs no rebuilding
- [x] retry: line 2 group corrected to el Rey de Escocia; C-count rule applied to all groups

## Files

- `sample_transcription.txt`: heading and lines 1-3 of f. 396r
- `key_excerpt.tsv`: the key entries read, with their key images
- `decode_sample.py`: decoder and controls, standard library (`python decode_sample.py`)
- `sample_decryption.txt`: line-by-line output of the decoder
- `sample_reading.txt`, `sample_translation.txt`: the sample as sentences, and in English

No images are in the folder. The pages are on PARES (links above).
