# Re-reading log, N.45 (22-23 Oct 2026, Claude Opus 5.5; REREAD_BRIEF, batch b16)

## Starting point

Reading audit (22 Oct): decoded, not read. The repository had line-by-line decoder output for pp. 3-15
(`n45_pp03-09_v2_decoded.txt`, `n45_pp10-15_v2_decoded.txt`) with broken word division, wrong letters and bracketed
groups on most lines. Scored as it stood (both files together, `_check_reading.py --file`): **0.213** clean sentences.

## Step 1: is there a text already?

No. All 16 PARES images of the record (12751390) were opened: p. 1 is a blank wrapper with the date note "De 4 de
Abril 1511", p. 2 blank, pp. 3-15 cipher, p. 16 the address ("Por el Rey", seal; note "1511 Abril 4, Sevilla").
PARES records no decipherment and none is bound with it. The deciphered siblings (N.46, N.52BIS, N.41, 8714 N.39,
N.12) are other letters; Terrateig 1963 (which may print it) is not online, as before. A PARES search for neighbouring
Vich records was refused (HTTP 429) on 22 Oct and was not repeated.

## Step 2: reading on the figures

- Built line by line on the compact decode (`research/reading_audit/b16_vich_dec.py`) in `n45_build.txt` (390 lines,
  the figures' own spelling), punctuated as an editor would; rendered with `b16_vich_render.py` and modernised in
  orthography with `b16_vich_modern.py` into `n45_reading.md`.
- **Image checks** (line strips `lines/s45pPP_NN.png`, three lines each, stacked with
  `research/reading_audit/b16_n45_strip.py`; crops only in the session scratchpad): every `fid` (25), every `fac`
  in a "dar" context, the `plix` lines, and about 40 further lines where the decode broke sense (pp. 3, 4, 6, 7, 8,
  9, 11). 33 label corrections, `n45a_corrections.tsv` (32, pp. 3-9) and `n45b_corrections.tsv` (1, pp. 10-15),
  applied with `b16_vich_fix.py` to make `n45_pp03-09_v3.txt` and `n45_pp10-15_v3.txt`:
  - **`fid` vs `fud`** (17 corrections). The transcriber wrote `fid` (despues) for two different groups. On the image
    the "dicho" places read `fud` (dicho): "el dicho duque" (0611, 0619, 0718, 0719), "las dichas tierras" (0507,
    0508, 0512), "el dicho negocio" (0723), "lo susodicho" (0603), "lo que dicho es" (0605), "los dichos casos" (0912,
    0924, 1005) ... The places that read "despues" (0302 "luego despues vino", 0309, 0403, 0515, 0803, 0811, 1022,
    1103) are `fid` on the image. So `fid` = despues and `fud` = dicho both hold; no new value.
  - **`plix` = `plirt`** (7). The sign transcribed `plix` is `plirt` (ni) on the image (0821-0823, 0915 checked; the
    same label at 0906, 0907, 0918): "si el papa vi**ni**ere en ella", "a Geronimo de Caba**ni**llas" (Ferdinand's
    ambassador with the Emperor), "que **ni** por compromiso **ni** por otra via la quiere hazer", "las dichas
    concordias **ni** la una dellas".
  - `fac` → `far` at 0419 ("si el quiere **dar** con la cabeça por las paredes", image reads far). Elsewhere `fac`
    is written with c on the image and reads "dichas" in five places (0436, 0626, 0814, 0915 "las dichas concordias",
    "de la manera que dicha es") but "dar" in four (0620/0718 "infeu-[dar]", 0708 "para [dar] en el campo del papa",
    0911 "ayu-[dar] al papa", 0802 "mu-[dar]"). Two values on one shape: **not adopted**; the "dar" places are
    `[?infeudar]`, `[?dar]`, `[?ayudar]`, `[?mudar]` in the reading.
  - 0310 `myk` → `my` (mal): "poca y [..] mal recaudo" (the B8 before it is b: "a la **B**astia").
  - 0313 `mel` → `mul` (negocio): "favor para todo su negocio".
  - 0316 `mem` → `mom` (ningun): "y no ningun de los que yo le suplicava".
  - 0611 `[dar]` → `dux` (duque): "al dicho duque".
  - 0614 `rug` → `pax` (su, with a superscript): "responda a su[s] y a la Yglesia".
  - 0706 `o to ... gh` → `oto ... g tt`: "pensionarios y **quatro** mil peones".
- Other image readings without a label change: 0703 "que el **va a** Italia" (3to b 7 hik), 0704 "para **Leon**"
  (Lyon), 0610 "si consejo [es] **esperar**".

## Proposed key values (for decode.py; not edited here)

- **`gid` = amor.** Carried by a sibling decipherment: 8714 N.39 line C0103 reads "dicho muchas palabras de grande
  **amor** y verdadera hermandad", where the cipher has `DE [ato][gqo] DE [gid] Y [sax]era`. All five other
  occurrences fit: N.45 0325 "que no tiene **amor** a mi ni a nuestra nacion de España", 0330 "me la dio no por
  **amor** sino por enemistarme con el rey", 0417 "hombre que ni me tiene **amor**", 1012 "que se faze por **amor** del
  emperador"; N.60 L0402 "respondo con el mismo **amor**". Used unbracketed in the reading (the aligner flags the four
  words because `decode.py` lacks the value).
- Not proposed (sense only, or contradicted): `pog` querer/quiero (fits 0911, 0927, 1201, N.60 L1306; not 0326
  "[pog] yo pondra"); `hug` havido/tenido (fits "he [hug] respecto", "he [hug] plazer", N.60; not 0433 "lo [hug]
  brevemente", where huz mas is wanted); `pie` recibi- (0611/0717 "de [pie]r en su obediencia", not 0625); `sum`
  stands for "tierra(s)" at 0507, 0515, 0520, 0929, 1504 but for a number at 0502 and 0512 ("le dan [sum] mil
  ducados"); `dax` probably a third duque group (1028 "tener por contrario al [dax]"), not checked elsewhere.

## Step 3: alignment

`research/reading_audit/b16_vich_align.py`, run per half (`n45_align.tsv`, both halves concatenated): 3,984
unbracketed words, 3,968 carried at 0.6 or more. The 16 below 0.6 were checked by eye: four are `amor` (proposed `gid`
above); the rest are one- and two-letter words or a line-break fragment the decode carries ("la Sede" < lSEDELA, "el"
< PARAlEMPERADOR, "por" < POR[gid], "pue[..]" < spve, "em-", "lo", "se"). 15 `[?word]`, 424 `[..]`, 14 supplied
`[word]`/`[x]`/`[que]`/`[y]`.

## Step 4: the bar

`_check_reading.py --file` on the reading body (header cut): **0.601** (224 of 373 sentences clean; 4,335 words,
hole rate 0.127). Path: first full build 0.546; with the orthography modernised (WORDS entries appended to
`b16_vich_modern.py` for faz-/fiz- forms, -eys/-ays endings, x/j, and the ue diphthongs that the intervocalic-u rule
was turning into "lvego", "nveve", "nvestro") 0.583; image corrections and `amor` 0.592-0.598; `va a Italia`,
`quatro mil peones` 0.601. A test of extra semicolons before "y que" changed nothing (0.586) and was dropped. The
score is at the bar, not above it with margin; the reading is coherent in its argument (the complaint against
Julius II, the Venetian terms, Ferrara, Fabrizio Colonna's orders, the three charges) but pp. 3-4 and 7 keep holes
in most sentences.

## What stays open

- ~424 unread groups or letter runs, densest on p. 3 (complaint about the cardinals), p. 4 (priory of San Juan,
  the Naples churches) and p. 7 (the French king's preparations, the compromise on Ferrara) — blocker:
  **no-key-material** for the unread groups (`hno`, `hug`, `mun`, `myn`, `moy`, `cx`, `pie`, `pog`, `hng`, `sab`,
  `reg`, `fry` ... occur in no deciphered sibling); the letter-level garbles between them were checked on the image
  only in part — blocker for the rest: **not-attempted** (about 330 lines not viewed at strip level in this pass).
- The `fac` two-value problem (dichas / dar) — **no-key-material** (no sibling decipherment has `fac` in a "dar"
  place).
- Numbers (`[m]`, `sum` in 0501-0502, 0512; "las [..] lanças") — **no-key-material**.

## One sentence

"Y no me parece que seria cordura, si el quiere dar con la cabeza por las paredes, seguirle yo en ello." — "And it
does not seem to me that it would be wisdom, if he wants to beat his head against the walls, for me to follow him in
it." (p. 4, ll. 18-20, on Julius II.)

## Parent's integration (23 Oct 2026)

- The proposed values were checked with `b16_vich_kwic.py` over the whole corpus and adopted in `decode.py` with
  their evidence in `key.md` ("b16 additions"): `gid` amor (carried by 8714 N.39's decipherment), `sas` ver, `ree`
  poder, `sue` saber, `men` menester. The others named here stay `[?word]` and are listed in `key.md` as not adopted.
- `b16_vich_modern.py`: the rule that turned u into v after l/n/r (luego → lvego) was removed rather than patched word
  by word, and fragments next to a bracket ("[..]ia") are no longer looked up as whole words. The reading is now
  regenerated from the build by `research/reading_audit/b16_vich_make.py` (header above `<!-- body -->` kept; the
  body rendered and modernised; "Su B[eatitud]" written out).
- Regenerated score of the body: **0.601** (224 of 373 sentences; hole rate 0.127), unchanged.

- Revised 23 Oct 2026 (coordinator): the reading now keeps the figures' 1511 spelling (the modernised pass is withdrawn). Scores of the body: _check_reading 0.488 (182/373), explicit holes only (b17_score.py HOLES=1) 0.697 (260/373). Read sentence by sentence: the failing windows have two or three holes each and stay followable; kept read.
