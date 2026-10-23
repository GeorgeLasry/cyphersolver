# Re-reading log, R9873 and R9898 (23 Oct 2026, Claude Opus 5.5; REREAD_BRIEF, batch b23)

## Starting point

Reading audit (22 Oct 2026): both letters "decoded, not read". Their only texts were the line-by-line working files
`r9873_cipher.txt` / `r9898_cipher.txt` ((a) cipher, (b) decode) and the English gists `read_r9873.md` / `read_r9898.md`.
`_check_reading.py --file`: r9873_cipher.txt 0.13 clean sentences (56/430), r9898_cipher.txt 0.16 (91/568); the gists
0.565 / 0.564 (English summaries, not texts). There was no reading file to score with `b17_score.py`.

## 1. Is there a text already?

- **DECODE records** (re-fetched logged in by the caller on 23 Oct 2026, `research/reading_audit/b23_fetch.py`; copies
  in the session scratchpad `reread\R9872 … R9899`). R9873: 8 images, no attachment, transcription or comment; every
  image opened: clear text and cipher only, no interlinear, marginal or slip decipherment. R9874 (ff. 86-87) = R9873 P6
  again plus f. 86v (bleed-through of the f. 86r postscript) and the address leaf f. 87r: nothing new. R9898: 7 images,
  no attachment; only the six marginal decipherments already used in pass 16 (ff. 150r, 152r, 153v, 154r, 154v, 156r).
- **R9899** (A-34 ff. 194-195, Sessa, Rome, x March 1525; a new sibling of the same cipher). f. 194r ends in four cipher
  lines and f. 194v opens with nine more (`f~ ꝑ db coh ges gap dim …`); none has a decipherment, and the faint text on
  f. 195r is an offset of another leaf, not a decipherment. One short run on f. 194v **does** carry a marginal
  decipherment in the second hand: "Su Sd. no querria estar de mejor animo y todos sus ministros van por el mesmo stilo"
  beside `f~ coh ler hog get 3 sof f~ mejor animo f~ ꝑ cot ꝑo cih ꝑo li lep ꝑo ott 3 Jim f~ van por el mismo stilo`
  (crop `reread\R9899\b23_194v_cip.png`). It gives `hog` = *querria* (new), and confirms `coh` Su Sd., `ler` no,
  `get 3` estar (3 = r), `cot ꝑo` todos, `cih ꝑo` sus, `li lep ꝑo ott 3 Jim` mi-ni-s-t-r-os (li = mi, lep = ni as a
  syllable). `hog` occurs once more, in R9898 f. 156r (`saf hog α ⅄ α ꝍ`, unread around it); in R9873 not at all.
- **Print / online.** CSP Spain ii 636 (the triplicate with its contemporary deciphering, Gayangos MS) and 637
  (Goicoechea's 19th-century decipherment of R9873) are English abstracts only (`csp/csp2_636_638.txt`). Quick web
  searches (BNE Biblioteca Digital Hispánica, RAH Biblioteca Digital, general) found neither the Gayangos triplicate nor
  Goicoechea's reading online. Lead not followed (a download would need the user's go-ahead): Olga Kolosova's thesis
  *El lenguaje secreto de la diplomacia de Carlos V (1521-1527)* (Valencia 2016/17; TESEO lists a PDF; book edition
  Salamanca 2024) describes 17 chancery ciphers of 1520-30 from RAH and BNE material and names Sessa among the
  correspondents: it may print this key.

## 2. Building the readings

Each letter was written out as continuous Spanish in the period spelling (`r9873_reading.md`, `r9898_reading.md`),
folio by folio in the order of the working file: the clear passages it quotes, and the (b) decode of the cipher runs
joined into sentences. Marks as the brief: `[?word]` partly carried (every tentative value, pass 16 "(tentative)" and
all pass 17 values, and every spelled word that needs one sign read as an unlisted look-alike or one letter mended),
`[word]` supplied, `[…]` unread. Open code groups are written `[…kam]` (ellipsis first) so that `_check_reading.py`
counts them as holes: a bare `[kam]` matches its pattern for a resolved code word and would score as a known word.
Clear passages the working file does not transcribe stand as "[clear text not transcribed]" paragraphs (one token after
the checker's code-word substitution, so dropped from the sentence count, not counted as a hole).

Word-level changes against the (b) lines, all from the figures:
- R9873 f. 81r 1b *t-e-r-[lep=ni]-a* is **ternia** (would hold [the cortes]), not a non-word; CSP 636 "hold cortes in
  Burgos, Aragon and Catalonia".
- R9873 f. 81r 13b *a-t-a-r-a-r* is **atajar** (`α ott α 3 α ꝍ`, `3` read as its i/j value).
- R9873 f. 82r 3b *la de mostra-[tt3]-o-n* is **la demostracion** (`sof lif tt3 4 do`: `tt3` = c-i, as `nf 4 tt3 ram`
  = po-di-do in the same line, `tt` c/d).
- R9873 f. 82r 4b *[cer]-en-do-se* is **teniendose**, and f. 82r 7b *so-s-[cer]-[lar]* **sostenimiento** (`cer` = teni,
  `lar` = miento: see 3).
- R9873 f. 82v 10b: the (b) line has *no toma grand aliento*; `net` is *halla* (pass 16, R9898 f. 154v margin), so
  **no halla grand aliento**.
- R9873 f. 82r 20b *(h)e-cho* is `mjn ⅄ g` = ha-z-e: **no se haze ninguno**; `qu` = o (see 3).
- R9873 f. 82r 14b *y-m-p-o-si-b-i-l-i-dad*: the figures have `do` (n): **ynposibilidad**.
- R9873 f. 83r 16b *vin-[x]-se* is `bog x dim` = veni-e-sse: **veniesse**.
- R9873 f. 86r 6b-7b *[ꝍ α] mas h-u-r-o* is **jamas huvo** (`ꝍ` read as j and as v); *j-u-z-g-a-n* likewise needs `ꝍ`
  = j. `ꝍ` as i/j recurs (*d-ꝍ-f-i-c-u-l-t-a-d*, *so-b-r-ꝍ-no*, *a-con-se-ꝍ-a-do*): a second six-shape not yet
  separated from r; counted as look-alike letters, not adopted as a value.
- R9873 f. 86r 4a / f. 82r 22a *y-r-r-e-s-o-l-u-c-ion*: `ꝑ do x g ꝑo(=) q b ttt boz` = y-n-r-e-so-lu-cion, **ynresolucion**
  (`x` = r); f. 83v 5a likewise **ynreparable**.
- R9873 f. 86r 10b *por e-s-a f-r-o-n-t-e-r-a-s*: the (b) skipped `tt`; with `tt` = s, **esas fronteras**.
- R9873 f. 83r 26b *se-n-t-ir*, *mirando si-en-p-r-e* etc. are written as the figures spell them (*sienpre*).
- R9898: *advesarios*, *sienpre*, *haze* as the figures spell them; *grand-s*, *es-p-r-r-h-en-c-ia* bracketed.

## 3. Key values (pooled across R9873, R9898, R9899, f. 128 and the 1523-25 siblings)

Adopted (each holds in every occurrence met; the ones resting on sense alone are flagged for review):

| group | value | evidence | flag |
|---|---|---|---|
| `gal` | embia- | R9898 f. 150r margin "se ha enbiado" over `dim njn gal ram`; R9873 f. 81v *el papa gal-va* (embiava, the Lodi money), f. 82r *quatro mill gal-r-a* (embiara) | attested |
| `hog` | querria | R9899 f. 194v margin "Su Sd. no querria estar" over `coh ler hog get 3 sof` | attested (new sibling) |
| `kaz` | -mente | R9898 f. 154v margin "grandemente" = `nuh kaz`; R9873 *ultima-kaz*, *demasiada-kaz* | attested |
| `lar` | miento | homophone of `lac` (R9897); so-s-teni-*lar*, c-r-e-c-i-*lar*, de-s-c-a-y-*lar*, so-s-t-e-ni-*lar* | review (homophone by sense) |
| `cer` | teni | *cer-en-do-se* teniendose, *so-s-cer-lar* sostenimiento (R9873 f. 82r) | review (sense) |
| `sur` / `luc` | parte | *por esas sur-s* (R9873 f. 80v, f. 86r), *por esas luc-s ni por las de Inglaterra* echoing the clear *en essas partes y en las de Ingalaterra* (f. 81r); R9898 *por la sur francesa*, *por su sur* | review (sense) |
| `tt` | s (plural ending) | *esa-tt sur-s*, *esa-tt fronteras*, *amigo-tt*; `tt` is c/d inside words (*po-tt3-do*, *demostra-tt3-on*) | review |
| `gul` | si | five contexts: *gul la paz veniesse*, *gul V.Md. deliberase*, *pretenderan gul*, *no gul se ha de hazer*, R9898 *gul lo efetase* | review (sense) |
| `nuf` | gente | *disolver la nuf* (R9873), *hiziesen nuf a su costa* (R9898) | review (sense) |
| `qu` | o | *ningun-qu de los…* (R9873), *para otro ningun-qu* (R9898) | review (sense) |
| `reb` | dezi- | R9873 f. 81r *he lo tornado a reb-r a Su Sd.*; R9660 (1523) *y quiero lo reb-r que*, *reb-en-do les que por … no se ha de pagar*, *de tig reb-r la* = contra-dezir-la (`tig` contra, pass 16) | review (sense, four contexts) |
| `dis` | servido | R9660 *se muestra muy dis-r de V.Md.* (servidor), *lo que sera dis*, *tiene por dis*; R9873 f. 86r *a Su Sd. y a sus dis-r-es* (servidores), f. 82v *V.Md. se as[ag] dis* | review (sense) |
| `gom` / `lo` / `ror` | quatro / mill / ducado | clear f. 81v *tomaron los de Lodi … quatro mill ducados*, then cipher *los dichos gom lo ror-s que se perdieron*; `lo ror` again with numbers (f. 82v x3, R9898 *bup ror*) | gom: review (one context) |

Not adopted (kept `[?value]` in the readings): every pass-17 value (`cas` tiene, `var` agora, `rac` dize, `pam` paga,
`xoc` socorr-, `leg` mucho, `len`/`lon` buen-, `3ar` aca, `yer` Florencia, `gig` quisie-, `yeg` antes, `fe` fue, `pus`
florentines, `sir` supli-, `kif` Lombardia, `gob` ello, `cox` cobra, `ꝑan` ex-, `Jam` llam-) and the pass-16 tentative
ones (`hay` aunque, `cex` trata-, `ges` embaxador, `lin` necesidad, `bun` visorrey, `hoz` dich-/dix-). `hay`: in R9873
f. 81r *y la [fum] hay en los partidos* it does not read *aunque*; left tentative. `kam`: *al kam de su casa* (f. 81v)
and *me responde a mi kam* (f. 82v, CSP "Madame Margaret") do not share a value; open. `mjn` reads *ha* in eight
contexts and *Italia* in three (*se venia a mjn*, *la guerra de mjn*, *la venida de V.Md. en mjn*): two groups
transcribed alike or a homograph; *Italia* kept `[?Italia]`.

Open groups after pooling (R9873): `sig`, `sas`, `fum`, `qat` (x3), `siz` (x2), `sul`, `som` (x2), `tup`, `col`
(x2), `ce3ꝍ`, `kam` (x2), `hoz`, `liz`, `kag`, `yam` (x2), `kar`, `la`, `kuf`, `cio` (x2), `njh`, `oap`, `cod`, `ꝑar`
(x2), `rin`, `sub`, `ben`, `yih`, `ag`, `pel`, `bot`, `bax`, `von`, `bez`, `ba`, `vin`, `ycr`, `jaz`, `gil`,
`caz` (x2), `3il`, `kun`, `lez` (x2), `hug`, `jes`, `ciz`, `got`, `yud`, `mjg`, `rir`, `ois`, `yid`, `hot`, `nuc`,
`kor`, `gud`, `hon`, `xoc`. Each was looked up in R9898, R9899 (f. 194r-v cipher), f. 128 and the concordance of pass 17:
none gains a deciphered occurrence. Those that also occur in R9660 (1523; `sas`, `fum`, `qat`, `yam`, `cio`, `cod`, `yih`,
`ag`, `lez`, `hug`, `yud`, `yid`, `kor`, `hon`, `ben`) were read in their R9660 contexts (`../sessa1523/reading_r9660.txt`,
concordance by grep): `reb` and `dis` close (table above); `yid` = *favo(r)* fits three of four contexts (*en yid-r de
Su Sd.*, *el yid-r*, *yid-r que a V.Md.*) but not R9873 *al yid-r de poz*, not adopted; the rest stay single-sense.

## 4. Image checks (crops in the session scratchpad `reread\R9873\`, `reread\R9899\`)

- R9873 f. 83r ll. 19-24 (P2 right, native 3368 px, then 2x): the transcription stands. l. 21 `… dim ꝍ ꝑ do ꝑ hay 4 ꝑ z
  leg hud …`: `hay` confirmed (straight descender, not `hag`); the two signs after `dim` may be `f~ v` rather than `ꝍ ꝑ`,
  but neither reading makes a word (*m-n-y*), so the label was not changed. No transcription labels changed in b23, so
  no corrections tsv.
- R9899 f. 194r foot, f. 194v, f. 195r: see 1.

## 5. Alignment

`research/reading_audit/b23_sessa_align.py` aligns every unbracketed reading word, folio by folio, with the words the
working file carries (the (b) decode, the clear quotes, the margins). R9873: 1,720 reading words, 1,534 unbracketed,
1,358 matched in order, 176 matched within 40 words or as a mend listed in section 2, **0 not carried**. R9898: 2,284
words, 1,897 unbracketed, 0 not carried except the four words of the date line "De Roma a xxiiij de hebrero", carried by
the section header of the working file (flagged only by position).

Look-alike letters (signs read as their second value, counted by the script on the (a)/(b) line pairs that pair sign for
letter, in words that stand unbracketed): **R9873 63** on 84 of 126 line pairs (`3` as i 38, `ꝍ` as i/u/v/d 10, `Ɉ` as
u/v 6, `Є`/`ε` as i/y 3, `3` as j 1, `3` as l 1, `x` as r 1, `tto` as z 1, `⅄` as e 1, `∠` as t 1), plus about six in
the hand mends of section 2 on unpaired lines (*atajar*, *jamas*, *huvo*, *juzgan*, *ynresolucion* x2); about 95
estimated over the whole letter. **R9898 21** on 106 of 159 pairs (`3` as i 9, `Ɉ` as u 6 and as n 4, `ꝍ` as d 1 and i
1). `3` = i is attested since pass 2 (two three-shapes), so most of the count is a second value, not a doubt.

## 6. Scores (reading body only)

| | before (working file, `_check_reading`) | after, `_check_reading --file` | b17 plain | b17 HOLES=1 |
|---|---|---|---|---|
| R9873 | 0.13 (56/430) | 0.409 (72/176) | 0.399 (63/158) | **0.715 (113/158)**, hole rate 0.097 |
| R9898 | 0.16 (91/568) | 0.29 (63/217) | 0.273 (54/198) | **0.47 (93/198)**, hole rate 0.148 |

The plain figures are low because the es word list does not know the 1524 spelling (*ternia*, *assegurara*,
*ynresolucion*, *sostinimiento*, *advesarios*, *estonces*); the explicit-hole share is the bar.

## 7. Decision

- **R9873: read** (grade B). 0.715 on explicit holes, and the sentences hold through ff. 80v-82v, 83v-84r and the
  postscript: the cortes in Burgos, Aragon and Catalonia, Capua from Blois with the truce articles, the two proposals
  (Capua to England, the French pension to Henry VIII), the Lodi money, the Pope's irresolution and Foglietta, the
  exchange money found through the bishops of Salamanca and Ávila, the nuncio's letters from England and Wolsey's
  "honest colour", Sessa's advice on friends and enemies, Alberto Pio, and the postscript on the disbanding and
  Picardy. The one stretch that does not hold is f. 83r ll. 19-25 (the coming to Italy, *odiosa*, the league with Leo X),
  where several groups and spelled runs stay open in a row. The reading follows no text of the time (none survives in
  reach); CSP 636 agrees topic by topic.
- **R9898: decoded, not read.** 0.47 on explicit holes. The six margin runs, the clear passages and f. 151v-152r read;
  the bleed-through pages (ff. 150v-151r, 155v) and most of ff. 152v-154r do not: spelled runs that make no word in
  nearly every sentence (*c-e-ve-d-a*, *p-e-e-g-a-d-y-i-os*, *e-o-c-a-do*) and some 140 single-context groups.
  Blocker: illegible (bleed-through; sign shapes not resolvable at 1.5x or 2x, no other image) and no-key-material
  (single-context groups with no deciphered occurrence in any sibling).

## 8. fraction_read

Tokens of the documents that read / all, cipher tokens as counted in pass 16-17 (`measure_read.py`; profile
`ciphertexts`): f. 128 116 + R9873 2,473 = 2,589 of 5,648 = **0.458** (R9898's 3,059 not counted).
