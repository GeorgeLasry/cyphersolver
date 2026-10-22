# f. 128 (R9877, duplicate R9878): Sessa to Charles V, Rome, 18 Apr 1524, the reading

Copied 22 Oct 2026 verbatim from NOTES.md, section 3. The cipher transcription is `transcription_f128.txt`; the key `key_working.md`.

## 3. Reading of ff. 128–131 (2026-09-18, in part; eight passes, see key_working.md)

Clear opening (f. 128r): *Teniendo escripto y cerrado el pliego del duplicado de xiiij deste que sera con esta, vi
una letra del obispo Verulano que esta en Constancia, de que aqui embio copia. Luego embie a Su Santidad a
suplicalle me mandase avisar de alguna particularidad para dar noticia della do conviniese. Mandome a mi Felice su
secretario, el qual me ha dicho que las letras que tiene son del dicho Verulano de vj y vij del presente, do dize
que hera acabada la dieta, y que Lucerna no concluyo de dar ayuda a franceses; que los cantones de Berna y Friburk
y Solodor, y para mas facilitarla y traer los animos del pueblo, publican que los suyços en Lombardia estavan
cercados y en grand peligro, con que juntava hasta el numero de ocho mill, que davan nombre de partir muy presto,
pero que el no podia saber el quando, por estar en Costancia donde algunos de sus amigos de Suyça le escrivian para
que exortase a Sus. que buscase alguna buena forma de paz. Esto es lo que me ha referido.*

Cipher (eight lines on f. 128r, one on f. 128v; the duplicate ff. 130–131 is token-for-token the same). Method:
every line cut into tokens by `tokens.py` (sheets in `tok/`, one PNG per token in `tok/*_tiles/`), the same done
for the deciphered siblings f. 138, ff. 168v, 170–171 and 322, and values assigned by aligning those against
their clears (f. 140, f. 172, f. 324). Transcription: [transcription_f128.txt](transcription_f128.txt).

> ¶ las dichas [vo]s no le las mostraron, que le ponen sospecha que desea aver algo que r-e-f-i-e-r-a de lo suso
> [ruc] [hay] no / **me parece que concuerda mucho con lo primero y postrero que el dicho obispo dize al maestro de
> postas** / hablé en la ora a Su Santidad a **pedirle que haya provisión** de [pa]-r-a los casos de suyços,
> persuadiéndole los m-re que r-ido los que no m-r-e-van / **pues tiene color para ello, aviendo començado** la
> plática de la paz y tregua r-[…] **entender lo que mas podré. Al visorrey escrivo en el mismo punto.**

Sense: Felice will not show Sessa the bishop's own letters, since they make him suspect that Sessa wants to get
something out of them for himself; Sessa nonetheless finds the report consistent with what the bishop writes to
the postmaster (Gabriel de Tassis: his Italian letter of 6 April, *tutti Elvetij son in arme … expedisca volando a
Milano et Roma*, is bound as f. 131); he went at once to the Pope to ask for a provision of money for the Swiss
business, persuading him that he has the colour (pretext) for it, having opened the peace-and-truce negotiation.
This is the news Bergenroth abstracts from the 22 April letter (CSP 643).

Pass 10 (the January 1525 letter R9897, same cipher, verbose clear on ff. 14v–15; fetched with the saved DECODE
cookie) attested `rad` = *dicha*, `boy`/`bez` = *-ido*, `Є` = *h*, `kel` = `kef` (*los*), and `lif 3` = *quiere*
(key_working.md, pass 10). Unread now: `vo` (the noun after *dichas*: the bishop's letters or their copies),
`z y` (the verb after *quiere*, *mostrar* from the sense), `per`, `rus`, `hay`, and the clause *los m-re que r-ido
los que no m-r-e-van*, where one sign value (probably `v`) is still wrong. The other 1525 letter, R9898 (14 pp.),
was then read through as well (pass 12): it seemed to carry no decipherment (wrong: see section 5, it has six marginal ones), so it gave only
contexts (`z y` also after *si*; `ruc`/`rus` is a person who *ha respondido*; `hud` again in *la plática de la paz*).
Pass 13 (the 24 July 1524 letter R9893, cipher f. 483 with its clear on f. 485) corrected `lif` to *mostrar*
(*ni se quiere mostrar* = `lep dim fa lif 3 α`, `fa` = *quiere*) and gave `zum` = *hay*, `tas` *cosa*, `luh`
*mundo*, `qit` *estado*, `lic` *monsieur*, `gel` *qual*. Open now: `vo`, `z y` (after *mostrar*; also after
*si* in 1525; probably a conjunction, *porque* or *diziendo*), `per`, `rus`/`ruc` (a person), and the clause
*los m-re que r-ido*.

Pass 14 matched templates of the unread tokens against every downloaded page (`tmatch.py`). The September 1523
letter R9834, whose cipher faces its clear on f. 38, gives `z y` = *-on* (*dilataron*, *concedieron*), so the first
sentence reads *las dichas [vo]s no le las mostraron*. `ruc` and `hay` occur only in the 14 April 1524 letter R9873,
which has no decipherment; `vo` and `per` match nowhere. Those four are the residue.

The seven 1523 Sessa letters DECODE marks "Decrypted" (R9676, R9691, R9693, R9781, R9834, R9836, R9841; about 50
pages, fetched into `img/` with the cookie) use **the same cipher** (`sof`, `gap`, `ram`, `bas`, `qes`, `lex`, `cih`
all recur; R9781's August 1523 cipher block has its clear on f. 651). They are the remaining source for the four
open groups; aligning them is the same token-sheet work as passes 1–13. Pass 11 (the rest of
R9897, ff. 10–13v, against ff. 14v–15) confirmed `hud` = *plática*, `rad` = *dicha*, and added *larga*, *fue*,
*esto*, *tiempo*, *para*, *después*, *llegar*, *miento*, but none of the five (key_working.md, pass 11).
