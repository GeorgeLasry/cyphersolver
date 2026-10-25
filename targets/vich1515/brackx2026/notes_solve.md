# vich1515: how the alphabet was recovered

## Method

The joint solver from `esp318no93` (`wsa4.c`): simulated annealing of a value for each sign (a letter, or one of
the 40 commonest letter pairs) and for each code group (a word, a syllable or a letter from a fixed list, or
"unknown"). The score is generative: a Spanish character 5-gram (*La Celestina* and *Don Quijote*) plus, for each
sign and group, n log(n / N), the cost of the encipherment given the key. That term is what keeps the search from
collapsing onto a few letters. Each run is 16 processes × 3 restarts.

The method was checked on Spanish controls (*Lazarillo de Tormes*, held out of the model) enciphered the same way,
up to the size of `esp318no93` (1,322 tokens, 54 sign types, 77 group types), where it recovers every letter, and on a
control matched to this letter (see below).

## Score history (best, per token)

| step | best | note |
|---|---|---|
| nothing fixed; shuffled tokens | −3.73; −4.56 | three values agree across the best keys |
| 6 signs fixed (`PHI GS Z O RH RS`) | −3.66 | 15 sign values agree |
| groups may also be single letters | −3.50 | 23 sign values agree; *ultimamente* appears |
| 24 signs fixed, groups free | −3.36 | *[ha]ueros*, *[di]uersos* |
| wide group options (syllables, chancery words) + 13 groups fixed | −3.37 | `zre`, `yin` settle |
| `sin` = *es* fixed | −3.37 | neutral for the score, required by context |
| `MH` = *f*, `CD` = *c*, `QH` = *x*, `PH` = *g* fixed | −3.37 | the last automatic pass; nothing new settles |

From the third step on, values were fixed only when the best runs agreed on them and the decoded contexts confirmed
them. Several were set from context against the runs' choice: `rak` = *con* (runs: *a*), `sin` = *es* (runs: *a*
or *e*), `MH` = *f* (runs: *l*).

## Control matched to this letter

`scripts/control_matched.py` enciphers a held-out Spanish text (*Lazarillo de Tormes*, Gutenberg 320) the way this
letter is enciphered: homophonic letter signs plus 8 letter-pair signs, and code groups for the 60 commonest words
and for 99 common syllables and letters inside spelled words (each used 22% of the time it fits). Size: 3,282 tokens
(this letter: 3,163), 1,907 signs (1,837), 38 sign types (37), 1,375 group tokens (1,326), 158 group types (159).

Solved with the same first step as this letter (`wsa4`, wide group options, nothing fixed; 300,000 iterations × 3
restarts × 16 runs), the five best runs all have **every sign token right**, and **35–44% of the group tokens**,
at −3.24 to −3.36 per token. This is the pattern seen here: the sign alphabet comes out reliably, the code groups
only in part, and they need reading by context.

## Reading the groups by context (step 2)

Done with the sign alphabet fixed, on the decode (`scripts/dec.py`: `text`, `ctx GROUP`, `freq`). A ranking of
candidate values by the 5-gram (`scripts/rank.py`) was tried as a guide; it favours short candidates under a plain
likelihood and long ones under a context-gain score, so values were decided from the contexts, not from the ranks.

**`sin` is two groups.** Page 3 shows *ſin* (two minims) before *pero* and *ſim* (three) before *cia*, and both side
by side on l. 10. `sin` = *es*, `sim` = *en*. The 151 tokens were split by the 5-gram in context
(`scripts/splitsin.py`; 60 close calls), and six close calls were read on line crops at 2× (`scripts/bands.py` finds
the lines, `scripts/crops.py` makes labelled sheets, `scripts/setsin.py` applies the readings). At 1,145 px most
minims are unclear, so the rest of the split is provisional.

**`X` has three values** (*r*, *s*, *z*); each token was given one by the 5-gram in context (`scripts/splitx.py`).
Also provisional.

**Pass 1:** `yob` = *por*, `pif` = *al*, `ynb` = *ni*, `bac` = *su*, `dem` = *yo*, `xns` = *muy*, `xnk` = *como*,
`bao` = *todo* (firm); `yem` = *papa*, `yaz` = *antes*, `suq` = *franceses* (tentative). Unread group tokens fell from
451 to 287.

**Pass 2:** only leads for rarer groups, mostly names (`rie`, `sod`, `sag`, `xoy`, `sio`: see `codebook.md`);
nothing adopted. Stopped there: the remaining groups occur 1–9 times each, mostly inside names or rare words, and
the doubtful `sin`/`sim` and `X` tokens limit what the contexts can settle.

| | types | tokens |
|---|---|---|
| firm | 27 | 932 (70%) |
| tentative | 11 | 107 (8%) |
| unread | 121 | 287 (22%) |

Working files of this step: `work/` (`v15s.txt`, `v15x.txt`: the transcription with the splits applied;
`splitsin.tsv`, `splitx.tsv`: the per-token choices and margins; `signs.txt`, `groups.txt`).

## Pass 3: reading by context, sources, images

**Sources consulted for a crib** (none gives the text of this letter):
- **PARES catalogue, AHN Estado 8715 N.73:** title only, *Carta cifrada de Fernando el Católico a Jerónimo de
  Vich*, 26 Oct 1515; no summary. N.72 (16 Oct 1515) is a clear letter on the Orihuela church, unrelated.
- **Calendar of State Papers, Spain, vol. II (Bergenroth), "Spain: 1515"** (british-history.ac.uk, pp. 251–276):
  no entry for 26 October. It gives the context:
  - no. 222, the league treaty of September 1515: art. 8 cites the alliance of "the late Pope Julius"; art. 24
    gives the Pope the right to excommunicate allies who refuse their obligations;
  - nos. 219 and 223: the Pope's treaty with Francis I, projected on 20 Sept and ratified with changes on 30 Sept;
  - no. 224: Ferdinand blames the Swiss, the Viceroy (Cardona) and Lorenzo de' Medici for delay, and tells the
    Emperor to go to Italy;
  - no. 240, Ferdinand to Vich, November 1515 (Simancas draft, Estado leg. 847 f. 116): it opens by referring to
    his letters of "the 26th of the previous month" and of 5 November (this letter), and says the Pope seems to
    have been playing a double game and may make peace with France.
- **Further Supplement to vols. 1–2 (Mattingly):** its 1515 pages were not reachable in text.
- **Zurita, *Historia del rey don Hernando*, and Sarrablo Aguareles's study of the king's letters to Vich:** not
  found online in searchable text.

The calendar entries were used as context only, to test readings (`bay` = *visorrey*, `suh` = *Emperador*, the
league, the excommunication clause, Pope Julius), not as a crib.

**Images.** PARES serves this record at 1,137–1,147 px wide at most. Every zoom value and viewer action tried on
`ViewImage.do` returns the same image or a 343 px thumbnail; the viewer has no tiles or IIIF. So the `sin`/`sim` and
`X` close calls and the single signs `CII`, `7H`, `Q`, `D` could not be re-checked; the split files are unchanged.

**Reading by context.** With the signs fixed, the decode was read as continuous text. Each unread group was set
from all its contexts together; `scripts/ctxw.py` prints them with wide context, and `scripts/rank2.py` ranks
candidate values by the Spanish 5-gram over the group options plus a list of names and chancery words of 1515
(`scripts/names_1515.txt`). The ranking was used only as a hint; it is noisy at this context length.

- **13 groups firm,** each confirmed in at least two contexts: `sag` = dicho, `suo` = esta, `yez` = persona,
  `xoy` = nuestra, `ynz` = parte, `bos` = tengo, `xif` = liga, `by` = ser, `see` = del, `teb` = Italia, `reh` =
  cosa, `sod` = dio(s), `dug` = uuestra. `xif` and `teb` replace the tentative *ar* and *las* of pass 2.
- **20 groups tentative,** listed in `codebook.md`, among them `bay` = *visorrey*, `suh` = *Emperador*, `rie` =
  *confederado*, `pnk` = *ayuda*, `beq`/`xnl` = *tierra*/*mar*.

| | pass 2 | pass 3 |
|---|---|---|
| firm | 27 types, 932 tokens (70%) | 40 types, 1,005 tokens (76%) |
| tentative | 11 types, 107 tokens (8%) | 29 types, 177 tokens (13%) |
| unread | 121 types, 287 tokens (22%) | 90 types, 144 tokens (11%) |

No sign value changed in this pass. The last round of reading added three tentative values and changed none of
the firm ones.

## The Terrateig crib

**Source.** Barón de Terrateig, *Política en Italia del Rey Católico, 1507–1516* (Madrid, CSIC, 1963), vol. I,
pp. 631–634 (pp. 665–668 of the PDF), quotes Ferdinand's letter to Vich of 26 October 1515 at length in Spanish, from
the minute: fn. 14 cites AGS Estado leg. 847 fol. 125 and Doussinague, *La política internacional de Fernando el
Católico* (1944), p. 520. The 1963 text is under copyright, so only page references, alignment results and short
phrases are kept here; the extracted quotations stay outside the repository.

**Method.** 15 passages on those pages are attributed to the letter of 26 October (others quote the reply to Vich's
letter of 4 October, the letters to the Swiss and to Urrea; those were tested and set aside). Each passage was
normalised (accents, *ç* → *c*, *j* → *i*, *v* → *u*, OCR slips such as *suygos* → *suyços*) and aligned with the
token stream by a gapped dynamic programme: a firm value must match (2 per wrong letter), a look-alike may take any of
its values free, a tentative value is free if it matches and costs 2.5 if it does not, an unread group takes 1–6
letters for 0.6 + 0.1 per letter, an unvalued sign 0–2 letters for 0.8, and an uncovered letter of the quotation or a
token giving nothing costs 2. The alignment is local in the letter and global in the quotation. **Control:** each
passage was replaced by 12 random passages of *Don Quijote* of the same length and aligned the same way; a passage
counts only if its cost per letter is under the best control by more than 0.1.

| passage | letters | where | cost per letter | best control |
|---|---|---|---|---|
| the long quotation (from *de uer que por la soberuia*) | 1,069 (about 250 words) | ll. 9–31 | **0.29** | 0.98 |
| *salido del cuydado en que estava* | 27 | l. 7 | **0.07** | 0.25 |
| the other 13 | — | — | at or above the control | |

Of the long quotation's 1,069 letters, 714 fall on firm values, which they match except at the places listed below.
One further phrase, *no son para haver plazer* (l. 6), matches word for word and was used for `ynb` = *para*
there. The rest was not adopted: short passages align to some place in any 5,000-letter text.

**What it settled** (`scripts/crib_apply.py`, `work/crib_tokens.tsv`):
- **Firm values changed:** `seg` *s* → *dicha* (*la dicha capitulacion*, and all 13 tokens read with it), `soo` *do*
  → *esto* (8 of 8). `yin` (*es*) is two groups: *paz* and *pues*; `ynb` (*ni*) is also *para* in three tokens;
  `sim` (*en*) is also *el* in three; `xny` is *nuestro* (*nuestro exercito*). These are split labels per token, as
  `sin`/`sim` and `X` were.
- **Unread or tentative groups now firm (27):** `be` *suycos*, `beo` *toda*, `dam` *ya*, `dah` *uos*, `tir` *iunta*,
  `zuy` *rey de francia*, `poz` *capitan general*, `bon` *tanto*, `yom` *principe*, `xez` *ninguna*, `pab` *ahunque*,
  `pib` *assimismo*, `sey` *fue*, `xnz` *necesidad*, `soq` *francia* (all with their other occurrences read the same
  way), and `gak` *con*, `xaz` *ninguno*, `dik` *voluntad*, `bip` *tiene*, `yee` *otra*, `sem` *exercito*, `nab` *lo*,
  `oso` *e*, `ip` *mucho* (one or two tokens each); `rue`, `sug`, `ral` (one token each) read *confederado*,
  *franceses*, *con* and are probably misread `rie`, `suq`, `rak`.
- **Tentative values confirmed (11):** `rie` *confederado*, `suq` *franceses*, `xin` *mal*, `yem` *papa*, `bay`
  *uisorrey*, `sio` *esta*, `san` *ello*, `xad` *lo*, `pnk` *ayuda*, `yed` *obligado*, `suh` *emperador*.
- **Tentative values contradicted:** `beo` (*e* → *toda*), `dah` (*esto* → *uos*), `zuy` (*frances* → *rey de
  francia*), `xny` (*e* → *nuestro* at 11.19), `SL` (*st* → *ll*: *marauillado*, *dello*), `LAM` (*an* → *u* at l. 29);
  `yaz` *antes* does not fit l. 14 (*pero*), where it is marked doubtful.
- **Signs:** `SL` = *ll* is now firm; `ZH` is *q* in two tokens before *-uisiere* (and by position in a third, l. 61,
  tentative); `LAM` is *u* in *pura*.
- **Look-alikes:** 38 tokens decided: `X` → *r* at 9.26, 10.19 and → *z* at 15.21, 21.21, 23.3, 26.4, 29.17; `sin` →
  *en* at 13.19, 20.27, 27.3, 27.8; `sim` → *es* at 28.15; the others confirmed. 13.19 had been read *es* on the image; the print overrules it. They are marked `crib` in
  `sin_x_tokens.tsv`.
- **Carried by context, tentative:** `xny` *nuestro* in *Dios nuestro Señor* (ll. 78, 83, 103); `yin` outside the
  quotation read *pues* (ll. 36, 39, 48) or *paz* (ll. 55, 64, 73) by context, and left unread at ll. 68, 77, 85.

**Firm values the quotation disagrees with** (not changed; for an image check): `O` *a* where the quotation has *c*
(*locura*, 10.24); `RS` *u* for *q* (*quan*, 16.2); `OT` *c* for *t* (16.18); `PSI` *t* for *l* (*echarle*, 27.13);
`ZO` *m* for *n* (28.14); `B8` *r* for *s*/*e* (26.25, 30.1); `Z` *a* for *s* (30.2); `rak` *con* for *que* (20.26).
Spelling differences (*i*/*y*, *hazer*/*fazer*) are the editor's normalisation or the minute's and were not counted.

**Measures.** Read share 0.636 → **0.773** (1,031 words, 303 holes); ll. 9–31 alone 0.914. Look-alike share 3.9% →
**3.2%**. Group tokens: firm 88% (82 types under split labels, 1,164 tokens), tentative 5% (17, 62), unread 8% (68,
100). Class unchanged: *decoded, not read*, now with a printed confirmation of ll. 9–31.

**The minute and Doussinague.** PARES: AGS Estado leg. 847 (record 4182083) holds the minutes of Ferdinand's
correspondence with Vich, 1507–1515; it is not digitised (its one sub-unit with images, EST,LEG,847,1, is an
unrelated copy of 1580). Doussinague 1944 was not found online (archive.org, HathiTrust, Google Books); archive.org
has only other books of his, lending-only.

## Rounds after the crib

Four rounds, each image-checked where a sign was in question; scripts `rounds_apply.py` and `rounds_reading.py` run
after `crib_apply.py` and `crib_reading.py`, then `renotate.py` and `assemble.py` (which puts the renotated bodies
into `reading_original.md` and `translation_en.md`). Measures: read share by the repository's
`research/reading_audit/v10_relabel.py` (`share`); look-alike readings as before: letters of `sin` read *en*/*el*
and of `X` read *s*/*z* where the model chose (not the crib or the image), over all decoded letters.

| round | what changed | read share | look-alike |
|---|---|---|---|
| after the crib | | 0.773 (1,031 words, 303 holes) | 165 of 5,235 (3.15%) |
| 1 | image checks of the eight places the quotation disputes, and `rue`/`sug`/`ral`: four transcription corrections (10.24 `OT`, 16.26 `suq`, 18.3 `rie`, 26.25 `PHI`), `PSI` = *l*; two flags (30.1–2) were alignment artefacts (*pu-ra necesidad* is right) | 0.774 | 3.15% |
| 2 | context: `yaz` *pero* (crib), `doc` *ui* and `ynh` *obra* (crib, *por obra viere*), 11 tentative values firm, `peb`, `dif`, `sof`, `xnp`, `zuf`, `sy`, `yae` read; `sifa`, `pefa` per token | 0.822 (1,097, 237) | 165 of 5,329 (3.10%) |
| 3 | `piq` *bien* | **0.824** (1,099, 235) | **165 of 5,337 (3.09%)** |
| 4 | solver ranking (all firm values fixed) of the remaining repeated groups: flat margins, nothing adopted; the round changed nothing | 0.824 | 3.09% |

Group tokens now: firm 93% (103 types, 1,236 tokens), tentative 1% (5, 13), unread 6% (60, 77). Lines 9–31, the
stretch the printed quotation covers, read at 0.949 (243 words, 13 holes). The class stays *decoded, not read*: the
look-alike share, 165 letters, is still above 3% (160 letters would meet it); with the read share under 95% it could
otherwise be at most *read in part*. Three values of round 2 also rest on phrases the letter shares with Ferdinand's
letter to the Swiss of the same month (Terrateig p. 634): `peb` *assi*, `yae` *otro* (l. 95) and `yin` *pues* (l. 77). Only
the crib or the image can confirm a look-alike token; context alone does not count.

## What remains

1. **The unread groups.** 60 types, 77 tokens, mostly occurring once; many are probably names (*por medio del […] de
   Pauia*) or rare words. The five tentative values need a second context each.
2. **`sin`/`sim` and `X`.** The per-token choices are by context; 60 `sin` close calls and the `X` sibilants need a
   better image than PARES serves (1,147 px). A request to the AHN for a high-resolution copy would settle them.
3. **`sio`.** Firm *esta* since the crib; the two contexts that do not fit (*santa empr[…]*, *conuenien[…]e*) may
   still be a second group, as `sin` was.
4. **A crib.** Terrateig's quotation covers ll. 9–31 (above). The rest needs the minute itself (AGS Estado leg. 847
   fol. 125, not digitised), Vich's answer, or Doussinague 1944, p. 520.
5. **The look-alike share** is 165 letters, 5 over the 3% limit: three `sin` close calls read on a sharper image (or
   five `X` tokens) would bring it under. The places the quotation disputes are settled (see "Rounds after the crib").
