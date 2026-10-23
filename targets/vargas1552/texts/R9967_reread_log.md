# Re-reading log, R9967 (23 Oct 2026, Claude Opus 5.5; REREAD_BRIEF, batch b36)

## Starting point

Reading audit (22 Oct): "decoded, not read": nothing of the letter was in the repository; the ruling (deciphered in the
margin, Imperial Cipher of 1544-1554) rested on Tomokiyo's cryptiana entry, and the DECODE images had never been viewed.
No reading file: before = 0.00.

## 1. Is there a text already? Yes, on the letter

- `research/reading_audit/b36_fetch.py` fetched DECODE R9967 logged in: 16 images (`IMG_R9967_I46378_P1..P16`, about
  1850 x 2600 px), no transcription, document or comment block. Every image opened (scratchpad `reread/R9967/`). The
  DECODE image numbers are not in page order; the archive's own numbers in the image headers (0001-0016) are, and the
  decipherment runs on continuously in that order: 0001 = P1, 0002 = P3, 0003 = P4, 0004 = P2, 0005 = P5, 0006 = P16,
  0007 = P8, 0008 = P6, 0009 = P7, 0010 = P9, 0011 = P10, 0012 = P11, 0013 = P14, 0014 = P13, 0015 = P12 (blank),
  0016 = P15 (address and docket).
- The letter: clear opening; a long cipher passage (0001-0011, each cipher block struck through with a saltire after
  deciphering); clear paragraphs on the conde de Pitigliano, Piedmont and don Fernando de Gonzaga with three shorter
  cipher runs (0011-0013); the date *De Venecia xxv de Agosto MDLij*; a postscript of the 25th (0013-0014); the signature
  *Fran.co de Vargas*; address and docket *El Embax.or de Venecia xxv de Agosto MDLij*.
- **The decipherment** is in a second hand in the left margins, at the foot of each page and over the shorter runs
  between the lines. It is one continuous text: a page's foot and the next page's top carry the decipherment of the
  cipher lines that follow. Transcribed in full: `R9967_decipherment.txt`, page by page, marked [M] margin, [F] foot,
  [T] top, [I] interlinear, [C] clear text.
- Neighbouring records: R9966 (Caracciolo, Milan, leg. 1184) and R9968 (Mantua, leg. 1454) are other letters; the
  decipherment is on R9967 itself. Print: not searched further (Tomokiyo gives no edition; the decipherment on the
  leaves is complete).

## 2. The decipherment against the cipher

No key is in the repository (Tomokiyo's reconstruction of the Imperial Cipher of 1544-1554 and the Ruiz de Alday 1866
key are outside it), so the cipher was not decoded sign by sign. Checks made instead (`R9967_code_check.tsv`):

- **Clear words inside the cipher lines** agree with the decipherment word for word wherever they occur (0001 l. 1
  *Tengo aviso de buen lugar que*; 0002 *dixo en secreto aun confidente suyo (de do lo he entendido) que*; 0002 *podria
  ser fuese, y assi es de presumir*; 0003 *en que se podria dezir mucho si no fuese tan notorio*; 0004 *Y tambien podra
  ser que se aya persuadido ... porque aunque mas sea fuera de proposito, nunca faltan*; 0005 *pues en otra cosa no
  entienden*; 0006 *De aqui vengo a concluir (sino me engaño) que*; 0010 *y no puede haver temeridad en juzgar para este
  effecto*; 0012-0013 *no erraria mucho por ser ... como a V. Mag.d he scripto*, *creo ciertamente que si*).
- **Code groups** recur with the same decipherment: `ager` = *cardenal* (three times), `pollo` = *papa* (five times),
  `s-o` = *el*, `x-o` = *del*, `n-o` = *al*. At 0005 the decipherer wrote *su Santidad* for `s-o pollo` (el papa).
- Not checked: the letter values of the spelled runs, sign by sign (no key here). Blocker for a sign-level check:
  no-key-material in the repository; the decipherment itself is not in doubt where the clear words and codes can be
  compared.

## 3. Reading and score

`R9967_reading.md`: the whole letter, the cipher passages from the decipherment and the clear paragraphs from the
original, in the writer's and decipherer's spelling, abbreviations expanded (*vuestra magestad*, *cardenal*,
*embaxador* ...). Word-by-word alignment with `R9967_decipherment.txt`: every unbracketed word is in the decipherment or
in the clear text; one supplied word, *[parte]* (the margin breaks off after *qualquiere*). Eight places in the marginal
hand were not made out at DECODE's resolution and are marked `[?word]` or `[…]` (Notes in the reading). **Look-alike
letters: 0** (the reading follows the decipherer's hand, not a decode).

| | before | after |
|---|---|---|
| reading body, b17 plain (LANG_=es) | no reading (0.00) | **0.701 (169/241)** |
| reading body, b17 HOLES=1 (Spanish 1552) | - | **0.996 (240/241)** |

The plain figure falls on 1552 spelling (*screvi*, *paresciendome*, *dessea*, *havia*, *yda*, *ymbidia*) and names.
Reader's judgement: the sentences hold and translate (`R9967_en.md`); the letter is a coherent despatch on Siena, the
Pope, the Duke of Urbino, the conde de Pitigliano and the French plans for Naples.

## Result

Read from the contemporary decipherment on the letter (grade A for the cipher passages, which follow the decipherer's
text; the eight uncertain words are in the marginal hand, not in the cipher).

## Open

- Eight words of the marginal hand (*[?desde luego]*, *[?descuido]*, *[?se fiaran] ... segun […]*, *[?hazerse]*,
  *ny nunca […]*, *sobre aver de […]*, *[?lo arribado]*, *[?hechos]*) and the cardinal's name *[?Mignanelo]*: blocker
  illegible at DECODE's resolution (about 1850 x 2600 px; PARES serves AGS images at most about 915 x 1250 px, lower
  still); only the AGS originals would settle them.
- A sign-by-sign check of the spelled cipher runs against the Imperial Cipher of 1544-1554: no-key-material in the
  repository.
