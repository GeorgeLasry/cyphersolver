# Re-reading log, lopehurtado1523 (22 Oct 2026, Claude Opus 5.5; REREAD_BRIEF, batch b07)

## Starting point

Reading audit (22 Oct): R9846 read (from the clerk's clear on f. 133r); the other seven records "decoded, not read":
their clear text was transcribed, but the cipher runs gave word pieces with gaps in nearly every clause. The repository
held the token transcriptions (`r96*/r98*_cipher.txt`, `texts/R98*_transcription.md`), the per-letter decodes
(`read_r*.md`), the merged key and its decoder (`key_merged.tsv`, `decode_merged.py`), and the 21 Sept retry log.

## Step 1: is there a text already?

* **Contemporary decipherment.** None on the DECODE images of any of the seven: no interlinear, no margin, no slip.
  CSP Spain ii no. 548 (Bergenroth 1866) describes R9667 as "Autograph in cipher. Contemporary deciphering", so a
  decipherment existed at the RAH, but it is not among the two DECODE images (both openings checked again). R9846's
  clerk's clear (f. 133r) covers only its own letter. The R9667 "Claro" leaf is the Abbot of Nájera's (21 Sept).
* **Print.** CSP Spain ii abstracts only R9667 (548) and R9846 (617); the other six are not calendared (grep by Salazar
  folio, 21 Sept). The 548 abstract is used for two bracketed words of R9667 (`[?sospechava]`, `[?franceses]`).
* **Web.** A search on 22 Oct for the 1523-24 letters (Lope Hurtado, Rome, cifra, Salazar A-28/A-30) found nothing.
* **RAH Biblioteca Digital** (bibliotecadigital.rah.es, where the Salazar volumes or better images might be): the
  site answers only through an "Anubis" proof-of-work bot check; not passed (bot detection is not to be bypassed),
  so whether A-28/A-30 are digitised there was not checked. **Blocker for anything beyond the DECODE images.**

## Step 2: read on the images

The DECODE images are in the main checkout (`C:\Users\dbour\cypher\targets\lopehurtado1523\img\`, 3,300-3,600 px per
opening, about 1,700 px per page). Every cipher run of R9866, R9867, R9868, R9869, R9683 and R9667 was looked at on
crops at 1.0-1.6x (`research/reading_audit/b07_crop.py`; crops in the scratchpad only). Corrections and look-alike
resolutions are in `<doc>_corrections.tsv` (`research/reading_audit/b07_corrections.py`). What the images settle:

* **The ß-like barred sign (a) was often transcribed `ʇʇ` (r).** In a dozen words the slot needs a, and the image
  shows the ß-shaped sign: R9866 "se ha de vender", "y aprovecha", "dias", "a su Magestad"; R9868 "Colona", "parece",
  "[?Catania]"; R9867 "si se les ha de hazer". The key's ʇʇ = r stands; the transcription label was wrong.
* **`y ʇʇ` and `ʇʇʇ ʇʇ` are one sign, ɣ̶ = g**: "coligados", "enemigos" (R9866), "colegio" (R9868), "alargar",
  "[?lle]gue" (R9867).
* **The barred m (m̶) is f or c, and ʒ is p (h after m̶)**: "confiado", "desconfiados", "gratificar[l]e" (f);
  "an cobrado", "la costa", "provechosa" (c); "paz", "se pague", "cunplir", "palmo" (p); "fecho", "aprovecha" (ch).
* **A crossed double stroke after `yuc` reads v** in "enviado", "envio" (R9869 R1, R8).
* **Misread code groups**: R9869 R7 `xab` is `rab`; `ʒul` is `zul` (con); R9869 R4 `zaf` is `yaf` (es: "escusan");
  R9869 R8 `y m̶` is the code `ym` (fue: "quando fue elegido").

## Code groups settled or narrowed (probable unless said; key files not changed)

* `zm` = como: R9867 l21 "hare lo que suelo, como V. Mt. me lo a mandado"; R9866 R14 "tan provechosa como tengo
  escrito". Two of its four contexts.
* `ʃeg` = tengo: R9866 R14 "como tengo escrito"; R9869 R7 "no tengo por […] que aca seran sus obras conformes".
* `zub` = alla (1522 key, probable) now fits three contexts: R9866 R5 "la costa de alla", R9867 l23 "de lo que alla se
  me deve", R9866 R14 "con[…]oso" (not read).
* `zad`: R9868 R7 "el ausencia del zad de aqui", after the clear "la partida del señor arçobispo de Capua": zad is
  probably a look-alike of `zed` (arçobispo). R9867 l16/l18 do not read with it.
* `yob` = ducados (1522, probable) occurs in R9869 R1 but the words round it do not read.
* Still open: `rub`, `ʃug`, `zid`, `tol`, `tid`, `zib`, `xer`, `xir`, `xal`, `ʃal` (as "esta" in one place only), `yab`,
  `tas`, `toc`, `yic`, `co`, `ʒσ`, `y˙`, `3cgc`, `ʃta ⊙ apud` (R9869 R1 opening).

## Word-by-word alignment (step 3)

Each italic (cipher) word of the four 1524 readings was checked against its decode line and the image: a word is plain
when every sign carries it (key value, or a look-alike resolution listed in the corrections table), `[?…]` when part of
it is carried or it rests on a probable code value or one context, `[…]` when nothing reads. Words fixed in this pass:
R9869 "bueno" -> `[?bueno]` (the figures give r-u-e-n-o), a hole with no figures removed ("para [?poder] en Francia");
R9868 "a dos y tres" -> `[?a]` (the sign is ω, i/y); R9866 "como" -> `[?como]` (tan-t-o c-o), "tiene" -> `[?tiene]`
(the t is not written). Supplied words are bracketed: R9869 "llegado [alla]", "qual[qui]era"; R9867 "estan [?cerca]
[de] Sad.", "poco[s]".

## Result per document (clean-sentence share of the reading body, `research/reading_audit/b07_score.py`)

| doc | before | after | state | rests on |
|---|---|---|---|---|
| R9866 (28 Feb 1524, to Gattinara) | decoded, not read | **0.667, read (B)** | read | clear + 14 runs, most sentences carried; holes: rub-type codes, R3 "[?] por pocos", R9 opening |
| R9868 (20 Mar 1524, to Gattinara) | decoded, not read | **0.638, read (B)** | read | clear + 17 runs; f. 430v runs (Colonna, Vespasiano, Prospero) now read; holes: zid/ʃug, R14, R15 yic, toc |
| R9869 (28 Mar 1524, to the Emperor) | decoded, not read | **0.622, read (B)** | read | clear (f. 444v transcribed in full) + 12 runs; holes: R1 (money sent with Beaurain), R5, parts of R9-R11 |
| R9867 (4 Jan 1524, wholly cipher) | decoded, not read | 0.389 | decoded, not read | about half the sentences hold; ~15 open codes (rub, ʃug, tol, xer, xal, zad, xir, ʃal, co, ℮ ...) |
| R9683 (June 1523) | decoded, not read | 0.636 on the whole letter, but the cipher passage is not read | decoded, not read | the score is carried by the clear; 3 of the 5 cipher sentences are holes (1523 sign set unkeyed) |
| R9667 (5 May 1523) | decoded, not read | 0.767 on the whole letter, but the cipher runs read only in fragments | decoded, not read | clear dominates; runs A, B, D-F partial or unread; C read with CSP 548's topic |
| R9695 (8 July 1523, autograph draft) | decoded, not read | not attempted further | decoded, not read | struck draft in the 1523 sign set; clear transcription incomplete |

R9683 and R9667 pass the number because their clear text is three quarters of the letter; they are kept unread because
the step-4 test is the reader's, and their cipher passages, the part that was secret, do not build sentences. Their
partial readings are kept (`R9683_reading.md`, `R9667_reading.md`). R9846 was already read; its English translation
(`R9846_en.md`) is added.

## One sentence per document read

* R9866: *"que si no son vencidos, quedan vencedores, y lo de aca esta perdido. Su Magestad provea de dineros"* — "for
  if they are not beaten they remain the victors, and all here is lost. Let His Majesty provide money."
* R9868: *"Vaspasiano obedecele como al Prospero su padre"* — "Vespasiano obeys him [Cardinal Colonna] as he did Prospero
  his father."
* R9869: *"el papa envio a ofrecer a V. Mt. quando fue elegido"* — "[what] the Pope sent to offer Your Majesty when he
  was elected."

## What stays open and why

* R9867: open codes without a crib (rub, ʃug, tol, xer, xal, xir, ʃal, co, ℮, ʃφ) — blocker open-codes.
* R9683, R9667, R9695: the 1523 letter signs differ from the 1524 key (the 1522 notation fits some: & = o, H = e,
  ɭb = p, ∠ = v), and there is no 1523 crib; the contemporary decipherment of R9667 (CSP 548) is not imaged — blockers
  open-codes and needs-physical-access (RAH, Salazar A-28; the RAH digital library is behind a bot check).
* R9846 ff. 130v-132v: f. 133v of the clerk's clear is not imaged (needs-physical-access).
