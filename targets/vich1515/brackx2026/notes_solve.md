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

## What remains

1. **The unread groups.** 90 types, 144 tokens, mostly occurring once or twice; many are probably names (*Luys de
   […]*, *por medio del […] de Pauia*) or rare words. The tentative values need a second context each.
2. **`sin`/`sim` and `X`.** The per-token choices are by context; 60 `sin` close calls and the `X` sibilants need a
   better image than PARES serves (1,147 px). A request to the AHN for a high-resolution copy would settle them.
3. **`sio`.** It reads *esta* in three contexts but not in two others; it may cover two groups, as `sin` did.
4. **A crib.** Vich's answer, or a deciphered copy made in Rome, would confirm the group values; none was found.
