# Re-reading log, N.60 (AHN Estado 8715 N.60, Logroño, 1 Sep 1512) — b16, 22-23 Oct 2026, Claude Opus 5.5

## Starting point

Reading audit (22 Oct 2026): decoded, not read. `n60_v3_decoded.txt` is line-by-line decoder output: broken word
division, wrong letters, bracketed groups on most lines. `_check_reading.py --file n60_v3_decoded.txt`: clean share
**0.197** (129 of ~650 windows), hole rate 0.214.

## Step 1: is there a text already?

No. All 16 PARES images of the record were opened (local copies `img/n60_1..16.jpg` in the main checkout): pp. 1, 2
are blank (show-through only), p. 16 carries the address, the King's signature and the dorsal endorsements, with no
decipherment. pp. 3-15 are cipher only. PARES records no decipherment. The deciphered siblings (N.46, N.52BIS, N.41,
8714 N.39 and N.12) are other letters. Terrateig, *Política en Italia del Rey Católico* (1963), which may print the
Vich correspondence, is not online and was not seen (blocker for a printed text: needs-physical-access).

## Step 2: reading on the figures

- **Compact decode.** `research/reading_audit/b16_vich_dec.py` puts letters together, with code values in capitals.
- **Build.** The reading was built line by line in `n60_build.txt` (433 lines). It keeps the figures' spelling and
  joins words across the decoder's breaks.
- **Holes.** Where the sense needs a word the figures do not give, the word is bracketed: `[?word]` or `[word]`.
- **Image checks.** I checked these places on the strips (`lines/s60p03_*`, `s60p15_06..09`, crops in the session
  scratchpad `reread/n60/`):
  - **L0301:** the sign after *respondi* is the tilde-d (`bh` = a), giving "respondo a todas vuestras cartas".
  - **L0304-L0305:** the strips show "por la **flort** (liga) y para atajar". *quebrantamiento* stays doubtful: the
    figures give *quebranta-?-t* / *al-ento*, with plort where mi is wanted.
  - **L0321:** "para que nuestra **flort** (liga) se conserue", where the transcription had flart (me).
  - **L0318:** "[soi] va, es [men] que trabajeys": *men* is a code group, not letters.
  - **L1522-L1530 (owed since 5 Oct):** checked. L1530 begins with **fub** (not fih?) and the next group is **pif**
    (quando), not pef, giving "quando quisieren no podran". The `??` tokens of L1525-L1527 sit in paper holes (white
    gaps on the image): **illegible**. L1527-L1529 agree with the transcription ("creencia para el [..]; dadle buena
    esperança", "se de prisa en tomar las [fob]s de Milan y de [foz]").
- **Corrections.** Five label corrections are in `n60_corrections.tsv`, applied by `b16_vich_fix.py` to make
  `n60_transcription_v4.txt`.
- **Not done.** pp. 12-15 were not proofread token by token beyond L1516-L1530, and most of pp. 4-14 was not
  re-checked on the image. The reading brackets what the decode does not carry instead.

### Traps seen in this letter (not relabelled wholesale; read through in the reading, bracketed where unsure)

- **`b` letter.** In this hand the `b` label reads **i** as often as a: *Sbgurbdad* seguridad, *prbncipal*,
  *artbculo*, *grandbssimo*, *Ludtubco*. This is the tailed sign noted in key.md.
- **`QUvb` = qui.** It gives *quisiere*, *quien*, *quisiessen* (L1201, L1524, L1530).
- **`fer` (decode.py dio).** It fits *Dios* (+s), *medio*, "a Dios gracias" (about 20 places). But it gives Fe- in
  *Fernando* (L0629, L0823), *feudo* (L0709), *fechura* (L0722), *Federico* (L1120) and "poca fe" (L1011), and "de
  fuera" (L1510). Either two groups are merged in the transcription or the value is a syllable. Those words are
  `[?…]` and no change is proposed.
- **`fid` (despues) and `fud` (dicho).** These are confused: "del [fid] Maximiliano" = dicho four times (L0804,
  L0809, L0811, L0819). Those places are `[?dicho]`.
- **The group read `fug` (señor).** It stands for **entre** in at least five places: "discordia [entre] ellos"
  (L0426), "division [entre] los de la liga" (L0917), "para que [entre] en la liga" (L1021), "la dicha señoria
  [entre] assimismo en la liga" (L1211), "liga general [entre] los principes" (L1508). Elsewhere it is "nuestro
  Señor". This is a shape split that cannot be decided at PARES resolution, so those places are `[?entre]`. **Flag
  for review.**
- **`ats` = mos.** The letter run gives *-mos*: "somos hermanos" (L1014), "[deue]mos trabajar" (L1217), "podamos"
  (L1229). It is not relabelled; those words are `[?…]` where unclear.
- **`7o` (ll) for rr.** It gives *Navarra* in L0303 ("naua-7o-a"), as in N.57's *yerro* and *errado*. No change is
  proposed; the word is `[?Navarra]`.

## Proposed key values (used unbracketed in the reading; for the parent to adopt in decode.py)

Each holds at every occurrence in N.45/N.57/N.60 and the siblings (`b16_vich_kwic.py`):

| group | value | n | occurrences |
|---|---|---|---|
| `sas` | ver (syllable) | 9 | "no contento de [ver] que ni el papa quiere estar a mi consejo" (N.45 L0304); "[Ver]ona y Vicenza" (N.45 L0513); "perse[ver]aua" (N.60 L0325); "perse[ver]o constantissimamente" (L0510); "perse[ver]ando ellos" (L0701); "go[ver]nacion" (L0818); "no [ver]ian bien" (L0820); "vol[ver] a Italia" (L1402); L1323 "[fog] [ver]e ats" unclear around the group, not against |
| `ree` | poder (syllable) | 5 | "nos [?] a[poder]ar de Italia" (L0315), "se torne a [..] a[poder]ar de Italia" (L0309), "nos a[poder]assemos de Italia" (L0519), "pues tiene [poder] para ello" (L1214), "para [poder] salir" (N.45 L1204) |
| `sue` | saber | 3 | "hazedmelo [saber]" (L0326), "fazedme luego [saber] lo que" (N.45 L1515), "haueys de [saber] que el rey dize" (N.45 L0628) |
| `men` | menester | 3 | "es [menester] que trabajeys" (L0318), "remediar esto es [menester] que luego" (N.45 L0713), "es muy [menester] y conuiniente" (N.45 L0431) |

Proposed by sense but **not** used unbracketed (one or more occurrences do not fit, or too few):

- **`soi` tanto.** 7 of 8 fit: "en que [tanto] va", "sufrir [tanto]s gastos", "y en [tanto] que" (x2), "ha hecho
  [tanto] por la liga", "con [tanto] que los venecianos crezcan", "de quien yo [tanto]". L0601 "dize que [tanto] si
  durare la guerra" is weak. Used as `[?tanto]`.
- **`dup` contrario.** It fits "lo [contrario] de lo que por la liga" (L0416), "ningun [contrario] en aquel estado"
  (L0829), "son [contrario]s del Emperador" (L1421) and "si el papa no me fuere [contrario]" (L1431, L1432). N.57
  "lo uno esta [dup] de lo otro" and L0417 are unclear. Used as `[?contrario]`.
- **`fez` gasto.** It fits "tan infinitos [gasto]s" (L0406), "tan grande[s] [gastos]" (L0422), "otro [..] [gasto]"
  and "excessiuo [gasto]" (L0615) and "[tanto]s [gasto]s" (L0617). L1308 and L1424 are unclear. Used as `[?gasto]`.
- **`fob` fortaleza.** 5 of 7 fit; L0432 and L1321 do not. Used as `[?fortalezas]`.
- **`dop` camino.** It fits "del [camino] torcido que lleua" (L0320), but L0321 and L1506 are unclear. Left `[..]`.
- **Left open:** `phi` (34), `reg` (18), `pub` (14), `for` (10), `pog` (10), `pir`, `gox`, `geb` and the other
  groups. No single value fits their occurrences.

## Step 3: alignment

`python research/reading_audit/b16_vich_align60.py n60_build.txt n60_transcription_v4.txt n60_align.tsv`. This
runs the shared aligner unchanged, with the four proposed values added to the decoder in memory.

- **Counts.** 5,074 unbracketed words, of which 5,026 are carried at 0.6 or more of their letters. There are also 83
  `[?]` words, 606 `[..]` holes and 37 supplied `[...]` items; most of the supplied items are the `[eatitud]` of Su
  B[eatitud].
- **The 48 under 0.6, checked by eye.**
  - About 40 are one- to three-letter words the global alignment pairs elsewhere (de, el, la, a, y, se, un, han),
    and their letters stand in the line's decode.
  - The rest are *visorrey* (L0815, decode `MIvbstREY` as at L0803), *cada* (`cbda`), *trabajo* (`ttravabt`),
    *podido* x2 (`ptdbdt`), *trabajad* (`travabad`) and *cobrar* (`ctbrar`). All are carried through the b/i, t/o
    label confusions above.

## Step 4: score

The body only, after the orthography is modernised (`b16_vich_modern.py`, entries appended; Su B. written Su
Beatitud): **0.506** (246 of 486 sentences/windows), hole rate 0.147, 5,718 words. Before: **0.197** (raw decode).
Below the 0.60 bar, so N.60 **stays decoded, not read**, and the reading is kept as a partial reading.

- **Where it reads.** The letter's course is clear and most of it builds sentences:
  - the complaint against Julius II (pp. 3-5) and the list of grievances (p. 4);
  - the Maximilian Sforza plan with Mossen de Gurk (Matthäus Lang) and the marriage alternatives (pp. 6-8);
  - Venice, Parma, Piacenza, Modena and Reggio (p. 9), and the Vicenza concession (p. 10);
  - the spiritual arms against Louis XII, with Guyenne and Normandy (p. 11);
  - the Florentine pensions and the Cardinal of Sion (p. 12);
  - Ferrara after Milan (p. 13), the diversion in Guyenne (p. 14) and the general league (p. 15).
- **What holds it under the bar.** Holes stand in most sentences: about 12% of words are unread groups, and the
  lexicon misses many 1512 forms.

## What stays open, and the blocker

- **Unread code groups.** About 600 holes: phi, reg, pub, for, pog, pir, gox, geb and the others. Blocker:
  no-key-material. They are absent from all deciphered siblings, and context gives no value that holds at every
  occurrence (above).
- **The `fer` and `fug`/entre splits, and the b = a/i sign.** These are shape splits at the limit of PARES
  resolution. Blocker: needs-physical-access, or a higher-resolution image than PARES zoom 10.
- **L1525-L1527 `??`.** Blocker: illegible (paper holes).
- **A full proofread of pp. 4-14.** Not done in this pass. Blocker: not-attempted.
- **Terrateig 1963.** It may print the clerk's decipherment, which would close most holes. Blocker:
  needs-physical-access.

## Sentence with translation

"Y tened por articulo de muy grande importancia que se abreve la conclusion de la paz del Emperador y de los
venecianos" (L1015-L1017). In English: "And hold it an article of very great importance that the conclusion of the
peace between the Emperor and the Venetians be hastened."

## Files

- `n60_build.txt`, `n60_corrections.tsv`, `n60_transcription_v4.txt`, `n60_align.tsv`, `n60_reading.md`,
  `n60_en.md`, `n60_reread_log.md`.
- `research/reading_audit/b16_vich_align60.py`: a wrapper that adds the proposed values in memory.
- `research/reading_audit/b16_vich_modern.py`: WORDS entries appended.
- `research/reading_audit/b16_vich_kwic.py`: FILES now reads `n60_transcription_v4.txt`.

## Parent's integration (23 Oct 2026)

- The proposed values were checked with `b16_vich_kwic.py` over the whole corpus and adopted in `decode.py` with
  their evidence in `key.md` ("b16 additions"): `gid` amor (carried by 8714 N.39's decipherment), `sas` ver, `ree`
  poder, `sue` saber, `men` menester. The others named here stay `[?word]` and are listed in `key.md` as not adopted.
- `b16_vich_modern.py`: the rule that turned u into v after l/n/r (luego → lvego) was removed rather than patched word
  by word, and fragments next to a bracket ("[..]ia") are no longer looked up as whole words. The reading is now
  regenerated from the build by `research/reading_audit/b16_vich_make.py` (header above `<!-- body -->` kept; the
  body rendered and modernised; "Su B[eatitud]" written out).
- Regenerated score of the body: **0.504** (245 of 486 sentences; hole rate 0.147); below the bar, so N.60 stays
  decoded, not read, with this text kept as a partial reading.

- Revised 23 Oct 2026 (coordinator): the reading now keeps the figures' 1511 spelling (the modernised pass is withdrawn). Scores of the body: _check_reading 0.386 (188/487), explicit holes only (b17_score.py HOLES=1) 0.591 (288/487), under 0.60: stays decoded, not read.
