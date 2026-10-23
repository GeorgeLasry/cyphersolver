# vich1515: sign and group values

**Firm** = fits every context and is confirmed in at least two independent ones (for the first 17 groups, also stable
in 10 of 10 of the best solver runs). **Tentative** = one or two good contexts, or a fit that leaves some contexts
unexplained.

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

Tentative or rare: `EQ` = *ma*, `LAM` = *an*, `SL` = *st*, `OS` = *le*, `D` = *nt* (one token), `V` (*m*?:
*a mandar*), `SUPNO` (an abbreviation mark after `bac`, as in *su s[antida]d*), `7H`, `CII`, `Q`.

**`X` has three values.** *r* in most words (*esperara, tardar, guardar, prometido, poder*), *z* in *hazer* and
*dezis*, and *s* in *resistir*, *asentadas*, *asentar*. The repo's transcription notes an `X` "often with a hooked
lower-left tail", so the forms are probably different signs, not separable at the PARES resolution (1,145 px). In
`brackx2026/work/v15x.txt` each `X` token is given *r*, *s* or *z* by the Spanish 5-gram in its context (`brackx2026/scripts/splitx.py`:
112 *r*, 50 *s*, 9 *z*); some are wrong (*sobesuia* for *soberuia*), so the per-token values are provisional.

## Code groups (159 types, 1,326 tokens)

Most groups stand for syllables or letters inside words; a minority are whole words or names.

| status | types | tokens |
|---|---|---|
| firm | 40 | 1,005 (76%) |
| tentative | 29 | 177 (13%) |
| unread | 90 | 144 (11%) |

**Firm:**

| group | n | value | evidence |
|---|---|---|---|
| `sud` | 97 | de | throughout |
| `no` | 93 | t | *capi[t]ulacion, prome[t]ido* |
| `zre` | 89 | que | clause openings |
| `sin` | 84 | es | *[es]perar, [es]piritu, [es]cuchar, no [es]pero, [es]trechamente* (see below) |
| `sim` | 71 | en | *resist[en]cia, dilig[en]cia, clem[en]cia, cumpli[en]do, [en]biado* (see below) |
| `xed` | 68 | la | *capitu[la]cion, capitu[la]do* |
| `rak` | 41 | con | *[con]tinuando, [con]stantes seruidores, [con]seruacion* |
| `gso` | 41 | l | *u[l]timamente, [l]etras* |
| `tok` | 40 | ha | *[ha]ueros, [ha]ueys, [ha]uemos* |
| `yob` | 38 | por | *por si y por la yglesia*, *dar gracias por*, *de la yglesia por poder mejor hazer*, *por X y por Y y ultimamente por Z* (the solver runs preferred *a*) |
| `bae` | 33 | si | |
| `xeb` | 32 | no | |
| `bne` | 28 | se | |
| `pif` | 21 | al | *espiritu[al] y tenpor[al] de la yglesia*, *ofrescer al papa* |
| `ynb` | 21 | ni | *no creo ni creere sino*, *con [ni]ngun*, *no desmayemos ni enflaquezcamos* |
| `bac` | 18 | su | *con [su]ma diligencia*, *[su]mo pontificado*, *de su mano*; before `SUPNO`, *su s[antida]d* |
| `yin` | 14 | es | |
| `xnk` | 14 | como | *perseuerando como perseuero*, *como lo ha enbiado* |
| `xoo` | 13 | mi | |
| `seg` | 13 | s | |
| `xno` | 12 | me | *ultima[me]nte, pro[me]tido* |
| `dem` | 11 | yo | *que yo espero en*, *y yo perseuero*, *desde que yo les ruego* |
| `bao` | 10 | todo | *[todo]s le deuemos dar gracias*, *de [todo]s los*, *todo lo que* |
| `su` | 9 | di | *[di]as, [di]uerso* |
| `xns` | 9 | muy | *mandandole muy estrechamente*, *les ruego muy afectuosamente* |
| `soo` | 8 | do | *[do]s dias* |
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

**`sin` and `sim` are two groups.** The transcription has 151 tokens of `sin` and 4 of `sim`. On the image (page 3,
ll. 8–10) the group is written with two minims (*ſin*) before *pero* (*espero*) and with three (*ſim*) before *cia*
(*clemencia*); l. 10 has both side by side (*ſin ſim*). So `sin` = *es* and `sim` = *en*. At the PARES resolution
the minims are often unclear, so the 151 tokens were assigned by the Spanish 5-gram in context
(`brackx2026/scripts/splitsin.py`): 85 *es*, 66 *en*, of which 60 are close calls. Six close calls were read on the images
(`brackx2026/scripts/setsin.py`); the rest are provisional and need a better image.

**Tentative** (one or two good contexts, or a fit that leaves a context unexplained):
- from pass 2: `xad` = lo, `xny` = e, `beo` = e, `xaf` = i, `be` = s, `rok` = s, `yem` = papa, `yaz` = antes,
  `suq` = franceses;
- `bay` = *visorrey*: *por la remision de mi [visorrey] … de tardar*, *muy malcontento del dicho mi [visorrey]*,
  *he escrito al dicho mi [visorrey] … reprehendiendole grauemente de la su negligencia*. Ferdinand blamed the
  Viceroy of Naples, Ramón de Cardona, for his delay before Marignano (Calendar of State Papers Spain II, no. 224);
- `suh` = *Emperador*: *he escrito al [Emperador] rogandole que venga*, *que el [Emperador] y yo … resistir*;
- `rie` = *confederado* (or another word for ally): *de todos los [rie]s*, *si los [rie]s perseueramos*;
- `san` = *ello* (*dar gracias por [ello]*, *no guardando en [ello]*); `sen` = *ella* (*lo contenido en [ella]s*);
- `xam` = *mas* (*no puede ser [mas] peligrosa*, *con [mas] union y conformidad*); `xin` = *mal* (*muy [mal]
  contento*, twice);
- `bel` = *señor* (*por ser [señor] de lo espiritual y temporal*; *ayuda de Dios e [señor]* is less clear);
- `baf` = *solo* (*no [solo] no la guardo, antes …*); `dah` = *esto* (*en [esto] ha … como dezis prometido*);
- `yed` = *obligado* (*lo que por mi parte soy [obligado]*; one other context does not fit);
- `pnk` = *ayuda* (*con … [ayuda] de Dios*, three times; *le hauemos de [ayuda]r*);
- `sio` = *esta* (*lo que [esta] capitulado / asentado*, *que oy [esta]n*; it does not fit *santa empr[…]* or
  *conuenien[…]e*, so it may cover two groups, as `sin` did);
- `beq` = *tierra*, `xnl` = *mar* (*cartas por [mar] y por [tierra]*; *correos por … y por [tierra] y ultimamente
  por [mar]*);
- `zuy` = *frances* (*ni dar al [frances] … poder mejor hazer lo que quisiere*, *resistir … [frances]*);
- `xeo` = *me* (*poder [me]jor hazer*); `doc` = *cart*, `pob` = *por* (*[cart]as [por] mar*); `boi` = *so*
  (*prouar si [so]mos constantes*).

**Leads, not adopted:** `xod` (*por medio del [xod] de Pauia*), `bon`/`yom` (*de Dios y de [bon]s [yom]s*), `peb`,
`zue`, `xez`, `dam`.

The other groups, mostly occurring once or twice, are not identified; many are probably names.
