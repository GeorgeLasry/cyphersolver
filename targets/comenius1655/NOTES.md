# Comenius to Andreas Klobusiczky, cipher passages of 1655 (Unsolved Catalogue no. 474)

Status: no write-up yet. Contributed by WAINUT (https://github.com/WAINUTAI), 27 Oct 2026. The site page, the README
row and the catalogue changes are left to the maintainer; the proposals are in the pull request.

**In short.** The cipher sentence of 4 Aug 1655 was deciphered in print in 1892, in a footnote of Adolf Patera's
edition of Comenius's letters: "Poloniam periisse et papatum in illa". We transcribed it from both printed editions,
rebuilt the key from Patera's plaintext and checked it letter by letter. One letter does not fit (see below). The
cipher passage of 24 May 1655 is not deciphered: neither edition gives a decipherment, and our attempts gave no Latin.
The catalogue's "four letters, each with a ciphered sentence" is too generous. The 22 Jul letter used invisible ink,
which is not printed, and the 6 Sept letter says it has no secret text. We also found one short cipher word, "(iyy)",
in the body of the 4 Aug letter. It is not deciphered.

## The documents

Jan Amos Komenský (Comenius), then at Leszno in Great Poland, to Andreas Klobusiczky, councillor of Prince
George II Rákóczi of Transylvania. The originals are in the Hungarian National Archives, MNL OL (Budapest), E 190
Archivum familiae Rákóczi (the former Kamarai levéltár). They were not seen. EMLO gives the folios (5.t. 788
ff. 389-390v; 6962 ff. 351-354v; 5.t. 800 ff. 414-415v).

Two printed witnesses, both on archive.org, both read on the page images:

- Szilágyi (ed.), *Okmánytár II. Rákóczy György diplomacziai összeköttetéseihez*, Monumenta Hungariae Historica,
  Diplomataria XXIII (Budapest 1874), archive.org `okmnytriirkczyg01gygoog`. It prints the letters "from the original
  in the Hungarian Chamber Archive". It gives the ciphers without a decipherment.
- Adolf Patera (ed.), *Jana Amosa Komenského korrespondence* (Praha 1892), archive.org `bub_gb_xnVMAAAAYAAJ`.
  His notes say both letters were first printed in MHH XXIII.

| letter | Patera 1892 | MHH XXIII 1874 | secret text | state |
|---|---|---|---|---|
| 20 May 1655 | CLI, pp. 177-178 ([leaf n199](https://archive.org/details/bub_gb_xnVMAAAAYAAJ/page/n199)) | | none; refers to the "Schaumiana" read "ex pacto" | context only |
| **24 May 1655** | **CLII, p. 178** ([leaf n200](https://archive.org/details/bub_gb_xnVMAAAAYAAJ/page/n200)) | **no. CIII, pp. 178-179** ([leaf n194](https://archive.org/details/okmnytriirkczyg01gygoog/page/n194)) | **letter cipher, 50 letters and 3 numbers** | **not deciphered** |
| 22 Jul 1655 | CLIII | | invisible ink: "Addo occultiora pagina sequenti, carbo ostendet" | not printed |
| **4 Aug 1655** | **CLIV, ends p. 182** ([leaf n204](https://archive.org/details/bub_gb_xnVMAAAAYAAJ/page/n204)) | **no. CXXIX, pp. 217-219** ([leaf n235](https://archive.org/details/okmnytriirkczyg01gygoog/page/n235)) | **one cipher sentence, and the word (iyy)** | **sentence deciphered by Patera 1892; (iyy) open** |
| 6 Sept 1655 | CLV, from p. 182 ([leaf n204-n205](https://archive.org/details/bub_gb_xnVMAAAAYAAJ/page/n205)) | | "Occulta scriptura nihil scribo hac vice" | no secret text |

Patera's footnote on p. 182 says the 6 Sept letter is also printed in Szilágyi, *Transsylvania et bellum
boreo-orientale* I (1890) pp. 393-394. That volume was not checked.

## 4 Aug 1655 (document A): Patera's decipherment, checked

**Transcription** (`ct_1655-08-04.txt`). The sentence stands after "4 Aug. 55. Tuus totus" (no signature) and before
the address "Generosissimo Viro Domino Andreae de Klobusitz". It is the same in both prints:

    Nihil certius quam Cyhyqbma cgzbbttg, et CmCasda 69 655 m.

The archive.org OCR of Patera has "(>i) (555" for the digits. The page images have "69 655".

**Patera's footnote** (p. 182, note *): "Značí: Poloniam periisse et papatum in illa." ("It means: ...").
Patera does not say who made the decipherment. MHH gives none.

**Key** (`key_1655-08-04.tsv`, rebuilt by `check.py`). Plain to cipher: a=m, e=g, i=b or 6, l=h or 5, m=a, n=q or 9,
o=y, p=c (also C), r=z, s=t, t=s, u=d. "et" is written in clear. It is a letter substitution with digits as extra
signs (homophones) for i, l and n. The pairs a/m and s/t occur in both directions, so the table may be reciprocal
(am, bi, cp, du, eg, hl, nq, oy, rz, st). This is a guess and is not used.

**Decryption, line by line** (`plain_1655-08-04.txt`):

| cipher | plain |
|---|---|
| Cyhyqbma | poloniam |
| cgzbbttg | periisse |
| et | et (clear) |
| CmCasda | p a p **m** t u m, read papatum |
| 69 | in |
| 655 m | illa |

**One conflict.** The fourth letter of "CmCasda" is "a". Everywhere else cipher a is plain m, so the strict
decryption is "papmtum". Patera reads "papatum", which is the only sensible word. Both prints clearly have "a" (checked
on the zoomed images). So either the writer put a plain "a" there, or this is a slip in the original or in both
prints. It does not change the reading.

**Controls** (`check.py`, seed 1). A shuffled key gives "ltptnman lremmuur et lalnion is illa". The correct key on
letters shuffled inside each word gives "nolmioap rispeesi et pmautmp in lali". Both are gibberish.

**Reading** (`reading_1655-08-04.txt`):

> Nihil certius quam Poloniam periisse, et papatum in illa.

**English** (`translation_1655-08-04.txt`): "Nothing is more certain than that Poland has perished, and the papacy in
it."

**Context.** The letter reports the Swedish advance from Poznań on Warsaw in the summer of 1655, the flight of the
Catholic clergy and the seizure of their goods, and the Swedes fortifying Poznań and Kalisz "to subdue and keep"
Poland. Comenius hoped for the fall of Catholic Poland and urged Rákóczi to join Charles X Gustav. The cipher hides
the one sentence that says this outright.

**The word (iyy).** Near the end of the same letter: "Mire angitur bonus vir (iyy) de tantis sibi injectis remoris"
("The good man (iyy) is wonderfully troubled by the great delays put in his way"). MHH prints "iyy" in italic, as it
prints the cipher of 24 May. Patera prints it in roman type. The 4 Aug key gives "?oo" (with the reciprocal guess,
"boo"), which is not Latin. It may be a code name for the "good man", perhaps Schaum, who is named just before. It
stays open [?].

## 24 May 1655 (document B): not deciphered

**Transcription** (`ct_1655-05-24.txt`). The passage ends the letter. It follows news from a friend in England
dated 23 Apr 1655. Both prints set it in italic. [ſ/f?] marks the long-s glyph, which the italic does not separate
from f.

    Patera 1892: Lmqſxmyo. 7. Gpdlmuoyqnotlses: Pnofeyprp 865, ap 73 pyſ: pdyp: Xyopatus etc. etc.
    MHH 1874:    Lmqſxmyo.7. Gpdlmuoyqnotlses : Pnofeyprp 865, ap 73 pyſ: pdyp : Xyoapus. etc. etc.

The last word differs: "Xyopatus" (Patera), "Xyoapus" (MHH). Only the original can settle it. The archive.org OCR
of MHH has "Gpdlmnoyq'nothes"; the page has "Gpdlmuoyqnotlses". 50 letters, 17 distinct; numbers 7, 865, 73; word
lengths 8 / 16 / 9 / 2 / 3 / 4 / 8 (or 7). "pdyp" has the pattern ABCA.

**What was tried** (`check.py`, `anneal.py`, `plain_1655-05-24.txt`):

- The 4 Aug key, its inverse, and its pairs read as a reciprocal table: no Latin ("?ant?ao? ? e?u?a??on??s?t?t ...").
- The 4 Aug pairs combined with Caesar shifts on 22-, 23-, 24- and 26-letter alphabets: nothing.
- Caesar, affine and progressive shifts; Vigenère, Beaufort (both forms) and Porta with about 10,000 Latin keywords
  from Patera's Latin text, plus names (Schaum, Comenius, Rakoczi ...): nothing. These were run with research scripts
  that are not part of this folder.
- Annealing of a one-to-one letter substitution, with word division kept, scored by Latin 4-grams and a word bonus
  from `lang/lexicons/la.json.gz` (`anneal.py`). **Matched control:** the same annealer recovers two synthetic Latin
  texts of 56 and 50 letters exactly ("gallia est omnis diuisa in partes tres ...", "omnia uincit amor et nos cedamus
  amori ..."). On the 24 May passage it finds only nonsense, for example "empclman stheminapondecrc tongratyt ut tac
  that lantudic".

So the passage is not a simple substitution of Latin with this word division. It may use another key, contain names,
numbers or abbreviations, or be in another language. The layout ("... : ... 865, ap 73 ... : ... : ... etc. etc.")
looks like a list or a citation. In the 6 Sept letter Comenius cites Drabík's revelations by number and date, so
this could be something similar. That is a guess.

**A different key.** The 20 May letter says the April letters could not be read and should be read "eo modo, quo
Schaumiana legi necesse est ex pacto" (in the way the Schaum papers must be read, as agreed). This may refer to the
agreed invisible-ink method rather than to a letter cipher. MHH XXIII also has another writer's line "Haec Comenius
incognita scriptura", which fits invisible ink as Comenius's usual secret channel. A key for the 24 May passage was
not found.

## Prior art

- Patera 1892, p. 182, footnote: the decipherment of the 4 Aug sentence. This is the earlier solution.
- MHH XXIII (Szilágyi 1874), pp. 178-179 and 217-219: ciphertext only.
- EMLO (Comenius catalogue) marks the letters "Contains ciphered sentence" and notes no decipherment.
- Szilágyi, *Transsylvania et bellum boreo-orientale* I (1890), pp. 388-394: prints CLI, CLIII and CLV; not checked.
- The critical edition (*Dílo Jana Amose Komenského*, vol. 26, Academia) has reached 1641 (vol. 26/II, 2024), so the
  1655 letters are not yet edited there. Blekastad, *Comenius* (1969), was not checked. A web search found nothing on
  these ciphers.

## Remaining gaps

- **24 May 1655 passage (B).** No key material. Not a simple substitution of Latin (annealing with matched
  control). Needs the original (MNL OL E 190) to check the readings (Xyopatus or Xyoapus, the long s, the digits)
  and a key, for example one agreed for the "Schaumiana".
- **(iyy) in the 4 Aug letter.** Too short: three letters, not Latin under the 4 Aug key.
- **22 Jul 1655 (CLIII).** Invisible ink on the next page ("carbo ostendet"). It is not printed and may be visible
  only on the original. Needs physical access.

## Escalation

- Siblings: the 4 Aug key was tried on the 24 May passage and failed. The other Comenius letters to Klobusiczky and
  Rákóczi of 1654-1656 in Patera and MHH XXIII were not searched systematically for more cipher; that is a next step.
- Print: Patera 1892 and MHH XXIII were checked on the page images. Still to check: Szilágyi, *Transsylvania* I
  (1890); Blekastad 1969.
- Key rebuild: done for 4 Aug from Patera's plaintext. For 24 May, ciphertext-only annealing with a matched control
  failed.
- Retry: ask MNL OL for scans of E 190 (the three folio ranges above) and look in the Rákóczi chancery for a
  Comenius or Schaum cipher table.

## Files

- `ct_1655-08-04.txt`, `ct_1655-05-24.txt`: transcriptions from both prints, with the archive.org page links.
- `plain_1655-08-04.txt`: the 4 Aug decryption, line by line. `reading_1655-08-04.txt`, `translation_1655-08-04.txt`:
  the reading as sentences and in English.
- `plain_1655-05-24.txt`: the 24 May trials (not a reading).
- `key_1655-08-04.tsv`: the 4 Aug key.
- `check.py`: rebuilds the key, decrypts, shows the conflict, runs the controls and the 24 May key trials.
- `anneal.py`: the 24 May annealing with the two matched controls (about a minute).

Both scripts use the Python standard library and relative paths: `python check.py`, `python anneal.py`.

Work done with AI language-model agents. Every cipher letter quoted here was checked against the archive.org page
images of both prints, and a second agent re-checked the readings, the key and the page numbers independently.
