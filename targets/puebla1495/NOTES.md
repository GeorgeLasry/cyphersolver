# Ferdinand and Isabella → De Puebla, Tortosa, 28 Dec. [1495], cipher copy (catalogue 615)

Status: no write-up. Contributed by WAINUT (https://github.com/WAINUTAI), 27 Oct 2026: the letter is identified
and its content is in print (Bergenroth 1862). A sample is decoded with the extant key. The full cipher copy is not
transcribed.

AGS, Patronato Real, leg. 52, doc. 124. PARES description
[2207846](https://pares.cultura.gob.es/ParesBusquedas20/catalogo/description/2207846), viewer
[show/2207846](https://pares.cultura.gob.es/ParesBusquedas20/catalogo/show/2207846), 4 images. Old mark "T. c. Y. 2"
(Tratados con Inglaterra, leg. 2) on pp. 1 and 4; foliation 664-665. A modern note on p. 4 reads: "Carta de los
RR.CC. al doctor Puebla en cifra incompleta". The PARES title ("sobre tratos de comercio con Inglaterra") comes from
the merchant cover words of the copy ("la conpania", "los factores", "mercaderias").

## What the letter is

It is a ciphered copy of the despatch of Ferdinand and Isabella to Rodrigo González de Puebla, Tortosa,
28 December 1495. The despatch is dated "1496" because the Spanish year began at Christmas.

- Bergenroth, *Calendar of State Papers, Spain*, vol. I (1862), **no. 113, pp. 72-75**: an English abstract of the
  clear draft (S. E. T. c. I. L. 2), with quotations.
  [BHO pp. 72-79](https://www.british-history.ac.uk/cal-state-papers/spain/vol1/pp72-79).
- Same volume, **no. 114, p. 75**: "The same despatch written in cipher. There are some alterations in the wording,
  but the substance is exactly the same. Spanish. Written in two different keys of cipher, one of which is extant."
- Bergenroth printed no decipherment of the cipher copy. The 1868 Supplement starts in 1498.

The evidence for the match comes from the clear words of doc. 124 (sample_transcription.txt):

| doc. 124 | CSP Spain I no. 113 |
|---|---|
| p. 2: "se le escrivio a catorze de mayo ... veynte de junio ... veynte e uno de jullio ... veynte e dos de agosto ... veynte e dos de setienbre con Salvador Duarte" | "Have written to him on the 14th of May, 20th of June, 21st of July, 22nd of August, 22nd of September" |
| p. 1: "nueve", "otra ... diez e siete", "otra ... treynta" | "Have received his letters of 9th of September, and 11th, 17th, and 30th of October" |
| p. 2: "agora que los factores de la conpania son venidos con la corte aqui a Tortosa" | dated Tortosa, 28 December |
| p. 1: Diego de Soria, Iohn de Santagadea, Diego Lopez de Ayala (clear) | the couriers and forwarders of nos. 113 and 117 |

Control: we split the BHO pages for CSP I pp. 57-107 into 42 calendar items and scored each against the five
sending dates of p. 2. Only no. 113 matches, and it matches all five; the next best item matches one. Out of 2,000
random five-date sets, none matched three dates in any item.

Is doc. 124 no. 114 itself? Probably, but this is not proven. No. 114 is "in two different keys", and we saw only the
Great Roman Numeral code on the lines we read. The endorsement of no. 113 mentions three copies, one by Valmarada
by sea and two via Diego de Soria. Doc. 124 may be another of those copies. Either way, no. 113 gives the
content.

## The code and the sample

The code is Puebla's Great Roman Numeral code. Its key is AGS PTR leg. 52 doc. 33
([show/2207755](https://pares.cultura.gob.es/ParesBusquedas20/catalogo/show/2207755), 200 images): an alphabetical
list of words and names numbered in Roman figures. Tomokiyo (cryptiana, "Spanish ciphers") lists doc. 124 under this
code, and he publishes many of its values.

Script forms, read on the key and in doc. 124: jV = M, d = D, dc = DC, **da = DCC**, dar = DCCC, ar = CCC. A small
ring is written over the C ligature and over final iiij/viij. The C-count of the ligatures follows the rule set out
in `targets/puebla1496/NOTES.md`.

`key_excerpt.tsv` holds the entries used here, with the key image each was read on. `decode_sample.py` applies them
to `sample_transcription.txt` and writes `sample_decryption.txt`. p. 1, ll. 6-8 decode as:

> nos fiso [?883] Diego Lopez de Ayala [?1374] **de** nueve **de otubre y** otra **de** diez e siete **de otubre y** otra
> **de** treynta **de otubre que** [?1335]

(bold = code groups). The controls in the same script give no Spanish. A shift of one entry gives "oyd" or
"paciencia" for every "otubre", and leaves "de" and "y" with no value. Shuffling the groups gives "diez e siete otubre",
"nueve que de".

Corrections made in the check (27 Oct 2026):

1. The month group is **jVda iiij = MDCCIIII = "otubre"** (key image 105, which has "oy" MDCCII, "oyd" MDCCIII,
   "otubre" MDCCIIII). The first pass had read it as "jVdc iiij" and left the month open.
2. **DCCCLV = "dotor de puebla"** is now read on the key (image 48; 854 is "dotor de talavera"). Before this, it was
   taken from Bergenroth's no. 117.
3. Key image 105 has MDCXCV as "otro/otra". Tomokiyo lists "otras".

Reading and translation of the sample: `sample_reading.txt`, `sample_translation.txt`. The key confirms the lines,
and so do the five dates in no. 113.

## A difference from the print

The cipher copy reads "de nueve **de otubre**". Bergenroth's abstract of the draft has "9th of September, and
11th ... of October". We saw no "onze" in the lines read. This may be one of the "alterations in the wording" of
no. 114, or a slip in one of the two texts. It does not affect the identification.

## Proposed catalogue change

615: an earlier-solution pointer. The content is in CSP Spain I (1862) no. 113, pp. 72-75, an abstract of the clear
draft. The cipher copy is no. 114, p. 75 ("substance exactly the same"), or a sibling copy. The catalogue's "CSP Spain
I not matched" should go. Date: Tortosa, 28 Dec. 1495. Direction: Ferdinand and Isabella → De Puebla.

## Remaining gaps

- The cipher copy beyond the sample (most of pp. 1-4) - blocker: not-attempted; the extant key would give a full reading, but it would only add the wording differences Bergenroth mentions, so it was not done
- Groups 883, 1374, 1335, 1813, 852, 868, 1221 and the "xxix" on p. 2 l. 1 have no value yet - blocker: open-codes; their key images were not opened
- Whether the ring over the C ligature ever adds a C - blocker: open-codes; the rule from the 616 key images is applied, but it was not checked group by group here

## Escalation

- [x] siblings: puebla1496 (catalogue 616, same code and key); CSP I nos. 117, 121, 130 for the couriers
- [x] clear-pages: the clear words of pp. 1-2 used for the identification
- [x] known-keys: AGS PTR leg. 52 doc. 33, key images 20, 24, 49, 51-53, 55, 60, 66, 80, 100, 103-106, 111
- [x] print: CSP Spain I pp. 57-107 (BHO), nos. 113-114; the 1868 Supplement starts in 1498
- [n/a] key-rebuild: the key is extant and needs no rebuilding
- [x] retry: month group corrected to otubre; DCCCLV read on the key

## Files

- `sample_transcription.txt`: p. 1 ll. 6-8 and p. 2 ll. 1-6
- `key_excerpt.tsv`: the key entries used, with their key images
- `decode_sample.py`: decoder and controls, standard library (`python decode_sample.py`)
- `sample_decryption.txt`: line-by-line output of the decoder
- `sample_reading.txt`, `sample_translation.txt`: the sample as sentences, and in English

No images are in the folder. The pages are on PARES (links above).
