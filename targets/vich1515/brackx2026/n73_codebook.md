# vich1515: sign and group values

**Firm** = fits every context and is confirmed in at least two independent ones (for the first 17 groups, also stable
in 10 of 10 of the best solver runs), or read off Terrateig's printed quotation of the letter (ll. 6–31; Terrateig
1963, pp. 631–634, see `notes/solve_notes.md`, "The Terrateig crib"; basis `crib` in `keys/groups.json`).
**Tentative** = one or two good contexts, or a fit that leaves some contexts unexplained.

## Signs (37 types, 1,837 tokens)

| sign | value | | sign | value |
|---|---|---|---|---|
| `PHI` | s | | `TH` | o |
| `X` | r, s or z (see below) | | `RH` | e |
| `O` | a | | `RS` | u |
| `YH` | y | | `KH` | i |
| `Z` | a | | `B8` | r |
| `FH` | n | | `OT` | c |
| `GS` | d | | `CT` | p |
| `ZO` | m | | `BO` | i |
| `AH` | g | | `ZH` | e |
| `MH` | f (*esforçarlo, fuerço, ofrescer*) | | `N8` | b |
| `DH` | n | | `CD` | c (*cuydado, capitulacion*) |
| `QH` | x (*dexar, Xpiandad*) | | `PH` | g (*de guardar*) |
| `SS` | q | | `LO`, `PSI` | t |

`SL` = *ll* (*marauillado*, *dello*; crib, was tentative *st*). `ZH` is *q* in two tokens before *-uisiere* (label
`ZHq`, crib; a third, l. 61, `ZHqt`, tentative).

Tentative or rare: `EQ` = *ma*, `LAM` = *an* (but *u* in *pura*, l. 29, label `LAMu`, crib), `OS` = *le*, `D` = *nt* (one token), `V` (*m*?:
*a mandar*), `SUPNO` (an abbreviation mark after `bac`, as in *su s[antida]d*), `7H`, `CII`, `Q`.

**`X` has three values.** *r* in most words (*esperara, tardar, guardar, prometido, poder*), *z* in *hazer* and
*dezis*, and *s* in *resistir*, *asentadas*, *asentar*. The repo's transcription notes an `X` "often with a hooked
lower-left tail", so the forms are probably different signs, not separable at the PARES resolution (1,145 px). In
`work/v15x.txt` each `X` token is given *r*, *s* or *z* by the Spanish 5-gram in its context (`scripts/splitx.py`:
112 *r*, 50 *s*, 9 *z*); some are wrong (*sobesuia* for *soberuia*), so the per-token values are provisional. In
ll. 9–31 the crib decides 21 `X` tokens (labels `Xr`/`Xs`/`Xz` in `work/v15c.txt`; seven changed).

## Code groups (1,326 tokens; types counted by split label)

Most groups stand for syllables or letters inside words; a minority are whole words or names.

| status | types | tokens |
|---|---|---|
| firm | 103 | 1,236 (93%) |
| tentative | 5 | 13 (1%) |
| unread | 60 | 77 (6%) |

After the crib (before the rounds that followed it): firm 82 types, 1,164 tokens (88%); tentative 17, 62 (5%);
unread 68, 100 (8%). Before the crib: firm 40, 1,005 (76%); tentative 29, 177 (13%); unread 90, 144 (11%). The
values set in the rounds after the crib are listed at the end; where they differ from an entry above, the end
section holds.

**Firm:**

| group | n | value | evidence |
|---|---|---|---|
| `sud` | 97 | de | throughout |
| `no` | 93 | t | *capi[t]ulacion, prome[t]ido* |
| `zre` | 89 | que | clause openings |
| `sin` | 81 | es | *[es]perar, [es]piritu, [es]cuchar, no [es]pero, [es]trechamente* (see below) |
| `sim` | 71 | en | *resist[en]cia, dilig[en]cia, clem[en]cia, cumpli[en]do, [en]biado* (see below); three tokens are *el* (`siml`, below) |
| `xed` | 68 | la | *capitu[la]cion, capitu[la]do* |
| `rak` | 41 | con | *[con]tinuando, [con]stantes seruidores, [con]seruacion* |
| `gso` | 41 | l | *u[l]timamente, [l]etras* |
| `tok` | 40 | ha | *[ha]ueros, [ha]ueys, [ha]uemos* |
| `yob` | 38 | por | *por si y por la yglesia*, *dar gracias por*, *de la yglesia por poder mejor hazer*, *por X y por Y y ultimamente por Z* (the solver runs preferred *a*) |
| `bae` | 33 | si | |
| `xeb` | 32 | no | |
| `bne` | 28 | se | |
| `pif` | 21 | al | *espiritu[al] y tenpor[al] de la yglesia*, *ofrescer al papa* |
| `ynb` | 18 | ni | *no creo ni creere sino*, *con [ni]ngun*, *no desmayemos ni enflaquezcamos*; three tokens are *para* (`ynbp`, below) |
| `bac` | 18 | su | *con [su]ma diligencia*, *[su]mo pontificado*, *de su mano*; before `SUPNO`, *su s[antida]d* |
| `xnk` | 14 | como | *perseuerando como perseuero*, *como lo ha enbiado* |
| `xoo` | 13 | mi | |
| `seg` | 13 | dicha | crib: *la dicha capitulacion*; *la dicha paz* (was *s*) |
| `xno` | 12 | me | *ultima[me]nte, pro[me]tido* |
| `dem` | 11 | yo | *que yo espero en*, *y yo perseuero*, *desde que yo les ruego* |
| `bao` | 10 | todo | *[todo]s le deuemos dar gracias*, *de [todo]s los*, *todo lo que* |
| `su` | 9 | di | *[di]as, [di]uerso* |
| `xns` | 9 | muy | *mandandole muy estrechamente*, *les ruego muy afectuosamente* |
| `soo` | 8 | esto | crib: *pues en esto*; *de todo esto*, *[esto]y* (was *do*) |
| `xo` | 4 | ra | |

**Firm, added in pass 3** (each fits every context and is confirmed in at least two):

| group | n | value | evidence |
|---|---|---|---|
| `sag` | 7 | dicho | *lo suso[dicho]*, *de los [dicho]s franceses escomulgados*, *al [dicho] mi …* |
| `suo` | 7 | esta | *[esta]dos por si y por la yglesia*, *porque [esta] es que quiere asentar con franceses*, *ni que por [esta] aduersidad*, *la liga general [esta] capitulado* |
| `yez` | 5 | persona | *poner [nuestra]s [persona]s y estados*, *poner [persona] de su mano en el sumo pontificado*, *la dignidad de su [persona]*, *[persona]s inclinadas a franceses* |
| `xoy` | 5 | nuestra | *en fauor de [nuestra] santisima liga*, *con [nuestra] intencion*, *poner [nuestra]s personas* |
| `ynz` | 4 | parte | *de mi [parte]*, *por su [parte] deue hazer lo mismo*, *lo que por mi [parte] soy obligado* |
| `bos` | 4 | tengo | *[tengo] por certissimo que*, *como yo [tengo] por …* |
| `xif` | 6 | liga | *la [liga] general*, *nuestra santisima [liga]*, *perseuero en la [liga]* (was tentative *ar*) |
| `by` | 4 | ser | *constantes [ser]uidores*, *constantes en [ser]uirle*, *no puede [ser] mas peligrosa*, *por [ser] señor de lo espiritual* |
| `see` | 8 | del | *la flaqueza [del] papa*, *contento [del] dicho mi …*, *apoderarse [del] …* |
| `teb` | 8 | Italia | *las cosas de [Italia] en peligro*, *echar franceses de [Italia]*, *la defension / conseruacion de [Italia]*, *hasta echarlos de [Italia]* (was tentative *las*) |
| `reh` | 3 | cosa | *las [cosa]s de Italia*, *no haga [cosa] que …* |
| `sod` | 9 | dio | *[Dio]s* in *ayuda de [Dio]s*, *al fin [Dio]s no desampara*; *por me[dio] del …* |
| `dug` | 3 | uuestra | *las [uuestra]s de xvii*, *auia letras [uuestra]s*, *por las [uuestra]s letras* |

**Firm, from the Terrateig crib** (read off the quotation; "+ctx" = the other tokens read the same way):

| group | n | value | evidence |
|---|---|---|---|
| `xad` | 50 | lo | crib +ctx (was tentative) |
| `sio` | 13 | esta | crib +ctx (was tentative) |
| `yem`, `suq`, `pnk` | 6 each | papa, franceses, ayuda | crib +ctx (were tentative) |
| `be` | 5 | suycos | *locura de suyços*, *el Emperador y yo y suyços* |
| `zuy` | 5 | rey de francia | *al rey de Francia* (was tentative *frances*) |
| `dam` | 5 | ya | *se [ya]n*, *vos [ya]* (*hayan*, *haya*) |
| `xez` | 5 | ninguna | crib +ctx |
| `rie` | 5 | confederado | crib +ctx (was tentative) |
| `beo` | 4 | toda | *toda vez*, *todas las cosas* (was tentative *e*) |
| `bon` | 4 | tanto | *de tardar tanto* |
| `san`, `suh` | 4 each | ello, emperador | crib +ctx (were tentative) |
| `dah` | 3 | uos | *para con vos* (was tentative *esto*) |
| `tir` | 3 | iunta | *se juntase*, *juntarse* |
| `yom` | 3 | principe | crib +ctx |
| `pib` | 3 | assimismo | crib +ctx |
| `xnz` | 3 | necesidad | crib +ctx |
| `bay`, `xin`, `yed` | 3 each | uisorrey, mal, obligado | crib +ctx (were tentative) |
| `poz` | 2 | capitan general | *mi visorrey y capitan general* |
| `pab`, `sey`, `soq` | 2 each | ahunque, fue, francia | crib +ctx |
| `xaz` | 2 | ninguno | crib |
| `gak`, `dik`, `bip`, `yee`, `sem`, `nab`, `oso`, `ip` | 1 each | con, voluntad, tiene, otra, exercito, lo, e, mucho | crib |
| `rue`, `sug`, `ral` | 1 each | confederado, franceses, con | crib; probably misread `rie`, `suq`, `rak` |

**Split labels from the crib** (one transcribed group, two values; split per token like `sin`/`sim`):

| label | from | n | value | basis |
|---|---|---|---|---|
| `yinz` | `yin` | 3 | paz | crib (*la paz*); was *es* |
| `yinp` | `yin` | 2 | pues | crib (*pues en esto*) |
| `yinzt`, `yinpt` | `yin` | 3 each | paz, pues | tentative, by context (ll. 55, 64, 73; 36, 39, 48); ll. 68, 77, 85 (`yinu`) unread |
| `ynbp` | `ynb` | 3 | para | crib (*para con vos*; l. 6 *no son para haver plazer*) |
| `siml` | `sim` | 3 | el | crib (*en el peligro*, *que el Emperador*) |
| `xnyn` | `xny` | 1 | nuestro | crib (*nuestro exercito*) |
| `xnyt` | `xny` | 3 | nuestro | tentative: *Dios nuestro Señor* (ll. 78, 83, 103) |

**`sin` and `sim` are two groups.** The transcription has 151 tokens of `sin` and 4 of `sim`. On the image (page 3,
ll. 8–10) the group is written with two minims (*ſin*) before *pero* (*espero*) and with three (*ſim*) before *cia*
(*clemencia*); l. 10 has both side by side (*ſin ſim*). So `sin` = *es* and `sim` = *en*. At the PARES resolution
the minims are often unclear, so the 151 tokens were assigned by the Spanish 5-gram in context
(`scripts/splitsin.py`): 85 *es*, 66 *en*, of which 60 are close calls. Six close calls were read on the images
(`scripts/setsin.py`); the rest are provisional and need a better image.

**Tentative** (one or two good contexts, or a fit that leaves a context unexplained); the ones the crib confirmed
or contradicted are in the tables above:
- from pass 2: `xny` = e (3 tokens outside the crib), `xaf` = i, `rok` = s, `yaz` = antes (it does not fit l. 14,
  where the quotation has *pero*);
- `sen` = *ella* (*lo contenido en [ella]s*);
- `xam` = *mas* (*no puede ser [mas] peligrosa*, *con [mas] union y conformidad*);
- `bel` = *señor* (*por ser [señor] de lo espiritual y temporal*; *ayuda de Dios e [señor]* is less clear);
- `baf` = *solo* (*no [solo] no la guardo, antes …*);
- `beq` = *tierra*, `xnl` = *mar* (*cartas por [mar] y por [tierra]*; *correos por … y por [tierra] y ultimamente
  por [mar]*);
- `xeo` = *me* (*poder [me]jor hazer*); `doc` = *cart*, `pob` = *por* (*[cart]as [por] mar*); `boi` = *so*
  (*prouar si [so]mos constantes*);
- the context labels `xnyt`, `yinpt`, `yinzt` (above).

**Leads, not adopted:** `xod` (*por medio del [xod] de Pauia*), `peb`, `zue`. (`bon`, `yom`, `xez`, `dam` are now
firm from the crib.)

The other groups, mostly occurring once or twice, are not identified; many are probably names.

## Rounds after the crib

Set by `scripts/rounds_apply.py` (values, per-token labels, image corrections) and `scripts/rounds_reading.py`
(reading and English lines); the round log is in `notes/solve_notes.md`.

**Corrected or newly firm:**

| group | value | basis | evidence |
|---|---|---|---|
| `yaz` | *pero* (was tentative *antes*) | crib + context | *que oy estan, pero, para con uos* (l. 14, the printed text); *pero al fin Dios no desampara* (42), *pero he salido del cuydado* (7), *pero uos al papa* (31), *pero puso* (70), *pero que* (77) |
| `doc` | *ui* (was tentative *cart*) | crib + context | *por obra ui-ere* (l. 31; the printed text ends *por obra viere*); *triplicadas uias por mar y por tierra* (122) |
| `ynh` | *obra* | crib | l. 31 (as above); the token at l. 52 is kept apart (`ynhu`, unread) |
| `sifa` | *al* | crib | *resistir al rey de francia* (l. 26); `sif` at l. 45 stays unread |
| `peb` | *assi* | context | *nuestro Señor assi lo ha permitido* (78; the letter to the Swiss of the same date has the phrase); *y que assi tengo por certissimo* (44); *haziendo lo assi* (53) |
| `dif` | *una* | context | *alg-una paz* (55); *sin dilacion alg-una* (99); *mencion alg-una* (121) |
| `sof` | *defension* | context | *la defension y conseruacion* (101, 112); *a la defension de* (115) |
| `xnp` | *mucho* | context | *ha muchos anos que desean los franceses* (62); *de no tener muchos dias* (8) |
| `zuf` | *quiere* | context | *pues suycos quieren tornar* (48); *y lo quieren* (63) |
| `sy` | *estado* | context | *al estado de la yglesia* (67); *apoderarse del estado* (58) |
| `yae` | *otro* | crib + context | *faltando los otros confederados* (114; a phrase Terrateig quotes); *en otro tal yerro* (95; the letter to the Swiss) |
| `piq` | *bien* | context | *que considere bien que si alguna paz* (54–55); *que mire bien su S[antida]d* (73) |
| `bel` | *señor* | context | *Dios nuestro Señor* (83, 103); *nuestro Señor* (78); *por ser señor de lo espiritual* (60) |
| `xnyt` | *nuestro* | context | *Dios nuestro Señor* (78, 83, 103) |
| `xnl`, `beq` | *mar*, *tierra* | context | *por mar y por tierra* (122); *por […] y por tierra … por mar* (2); *por mar* (5) |
| `xam` | *mas* | context | *no puede ser mas peligrosa* (66); *con mas union y conformidad* (82); *mas biuas fuercas* (81) |
| `sen` | *ella* | context | *con ellas* (7); *contenido en ellas* (9); *en ella* (56); *puso con ella* (70) |
| `baf` | *solo* | context | *sino solo esforcarle* (32); *que solo ha permitido* (46); *no solo no la guardo* (70) |
| `xaf` | *i* (= *y*) | context | *que uenga y* (104); *y con duplicadas* (121); *y sin dilacion* (99) |
| `xny` | *e* | context | *e-scomun-* (86, 88, 113); `xnyn` = *nuestro* at 11.19 (crib) |
| `yinpt`, `yinzt` | *pues*, *paz* | context | *y pues con esa ayuda de Dios* (39), *pues suycos* (48), *pues … lo ha permitido* (77); *escuchar ninguna paz* (64), *la dicha paz no se asentara* (73) |

**Tentative:** `pefa` = *aqui* (*de aqui adelante se guarde*, 94); `rok` = *s*, `xeo` = *me*, `boi` = *so*, `pob` =
*por* (as before).

**Sign:** `PSI` = *l* (was *t*): its only token, *echarle* (27.13), as printed.

**Transcription corrections on the image** (PARES, page 1): 10.24 `O` → `OT` (*lo[c]ura*); 16.26 `sug` → `suq`; 18.3
`rue` → `rie`; 26.25 `B8` → `PHI` (*resistir*). Checked and left as transcribed: 16.2 `RS` (the cipher has *uuan* for
*quan*), 16.18 `OT` (*concertarse*; the print has *contentarse*), 20.26 `rak` (*con* where the print has *que*), 28.14
`ZO` (*capitulaciom*), 23.20 `ral` (written *ral*).

**Leads, not adopted** (one context, or contexts that disagree): `sep` *entonces* (46; 72 does not fit), `pnd` *agora*
(44; 81 does not fit), `zoq`, `bnz`, `zue`, `xil`, `tox`, `yis`, `saf`; a solver ranking with all firm values fixed
gives flat margins for them.
