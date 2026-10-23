# R97 — Cardinal Alessandrino to the nuncio Castagna, cipher of [Rome, 1568] (Spagna 6/I/5, ff. 88r–89v): reading

Rests on: the contemporary decipherment on the leaf bound after the cipher (`R97_decifrato_f90.txt`, DECODE cleartext
images DOC_R97_D1264 = f. 90r and DOC_R97_D1265 = f. 90v), found 23 Oct 2026 (r2g), and on the figures, read word by
word against it (`python reread_aless_align.py decode/DOC_R97_D1668_1668.txt all texts/R97_reading.md`; the four
pages run together). The decipherer's draft is fast and often loose; where it and the figures differ the figures are
followed, and several places he left blank or guessed are read from the figures (notes below): "il conte Ercole
Tasone" (he left dots), "riservare una orechia per N.S." (2 0 9 = "chi" as a syllable), "mette pericolo", "con
Turchi" (1 1 7 + 2 0 9), "Piali Bascià", "esortandolo a procurare … a preocupare Roma", "da lor parte". Code values
from this letter: 7070 Imbasciatore (with a following 2 = the plural "-i"), 4010 Re di Francia (as in R93 and R96;
Lasry's "Sua Santità" does not fit "oltra che [4010] mostreria che questi officii non sono fatti di suo consenso"),
2010 Imperatore, 8070 Ugonotti, 3050 Italia (written 3 0 5), 6050 Imbasciatore (as in R95), 4060 5050 = "il Duca di
Ferrara" (the decipherer's words; the codes are not otherwise attested), dotted 3 + 4 = "Principe di Condé" (the
decipherer's words). The decode of 23 Oct (beam search) is superseded.
Marks: [?word] partly carried, […] unread, [word] supplied, [NNNN] an unidentified code.

## Reading

Si è inteso per cosa certa che il Duca di Ferrara, [?per] mala satisfatione che habia forse sentito di N.S. in un
negotio de fuorusciti del contado di Bologna tratato qui in suo nome dal cavalier Gualengo, ha disegnato farne qualche
risentimento con Re; et venendo a cotesta corte il conte Ercole Tasone haverà facilmente particolare comissione di
parlarle in questa materia. Il quale ofitio non doveria esser fato da esso Imbasciatore, considerata la afetione
paterna che N.S. le porta et il poco rispeto che dalla parte sua si ha a questa santa sede, della quale esso è per
feudatario, non oservando le capitulationi della sua investitura et in spetie una che lo obliga a rendere li
fuorusciti di questo stato ogni volta che gli sieno dimandati. […] che ho voluto che V.S. sapia, acciò se ne sentise
ragionare possa dire a Re che sia contenta riservare una orechia per N.S., la quale si giustificarà di maniera che non
dubita di farne restar capaci tutti li principi, bisognando sentire che abiano le sue ragioni; ma se non sentirà
parlarne, non accaderà farne oficio alcuno, et starà […] avertita mentre il sopradeto si fermerà in corte, et mi
avisarà il sucesso di mano in mano.

Saria da vedere per mezo di N.S. che si levasse di […] mal Imbasciatore che è là in nome di Re di Francia, il quale fa
tanti cativi oficii per la Christianità, che se si comporta molto mete pericolo, sì come oferisce di unire li Ugonotti
insieme con li protestanti in una lega con Turchi per asaltare […] asediare da tutte le bande la povera Christianità;
et per stabilimento di deta lega afferma che presto sarano in Constantinopoli Imbasciatori del Principe di Condé et
delli protestanti, prometendo che dopo che sarà ruinato et destruto ogni cosa si unirano tuti insieme et sarano tuti di
una fede con li Turchi. Il qual discorso se ben a qualche altro tempo averia dato da ridere, ora è molto da temere per
la travagliata Christianità; sì che levandosi di là così cativo instrumento, oltra che Re di Francia mostreria che
questi oficii non sono fati di suo consenso, si faria ancora giovamento non picolo alle cose della Christianità.

Et per altra via se intende similmente che in Andrinopoli lo Imbasciatore [di] Re di Francia ha fato con Piali Bascià
et generale del mare molti mali oficii et contra N.S. et contra Imperatore et contra la Italia, esortandolo a procurare
dal Signore di venire con grandisima armata a preocupare Roma et N.S.; et questo ha fato non solo come Imbasciatore
[di] Francia ma anche de comissione delli principi protestanti, prometendo che presto sarano là […] Imbasciatori da
lor parte, et oferendo che in Italia facilmente et presto si manderiano infiniti Ugonotti a corompere li animi delli
Italiani.

## Notes on the figures

- "il Duca di Ferrara, [?per] mala satisfatione": 4 0 6 0 5 0 5 0 2 0 2 4 4 4 0 5 4 1 2 5 3 4 1 2 5 6 6. 4060 5050 read as
  the decipherer's "il Duca di Ferrara"; "2 0" is not "per" in the key.
- "sentito di N.S. in un negotio": 5 6 6 1 2 1 5 0 7 2 0 1010 2 6 0 1 6 0 6 6 3 5 1 2 5 (the decipherer "havuto ... nel").
- After "fuorusciti" (3 1 5 7 1 5 8 2 1 2, end of line 2) line 3 repeats "8 2 1 2" (-citi): the clerk's repetition.
- "con Re": 0 9 0 3010 (the decipherer "con S.M.").
- "il conte Ercole Tasone": 2 4 0 9 1 6 | 6 7 8 5 4 6 | 1 4 5 5 6 6 (9 = con); the decipherer left dots.
- "da esso Imbasciatore": 7 4 0 6 5 5 0 6 0 5 0 (6050, as in R95); the decipherer "da lui".
- "si ha a questa": 5 2 0 4 0 4 0 6090 — not a code 4040, but "ha" (4) and "a" (4) with nulls.
- "della quale esso è per feudatario": 7 6 4 4 0 309 4 6 0 6 5 5 0 6 0 5020 3 6 1 7 4 1 4 7 2 5 (the decipherer "alla").
- "et in spetie una": 0^. 2 6 0 5 9 6 1 2 6 0 1 6 4 (the decipherer "et spetialmente in una").
- "[…] che ho voluto": 2 6 0 2090 5 0 1 5 4 1 1 5; "2 6" not read (the decipherer "il che").
- "possa dire a Re che sia contenta riservare una orechia per N.S.": 9 5 5 4 0 7 2 7 6 0 4 0 3010 2090 5 2 4 0 9 1 6 6 1 4
  0 7 2 0 5 6 7 1 4 7 6 1 6 4 0 5 7 6 2 0 9 4 0 5020 1010 — orechia = 5 7 6 + 209 (chi) + 4.
- "starà […] avertita": 5 1 4 7 4 0 5 0 2 5 0 4 1 6 7 1 ? 1 4; "5 2 5" not read (the decipherer "però").
- "mentre il sopradeto si fermerà in corte et mi avisarà": 2 6 6 1 7 6 2 4 5 5 9 7 4 7 6 1 5 5 2 8^3 6 7 2 6^4 7 4 2 6 8 3? 7 1 6
  0^.0 2 2 0 4 1 2 5 6 7 4 (the transcription's doubtful 3 and 4 give fermerà; the decipherer "si scriverà in corte").
- "che si levasse di […] mal Imbasciatore": 2090 5 2 0 4 6 1 4 5 6 0 7 2 0 4 0 6 4 . 4 0 9 4 0 2 4 4 0 7070; "4 6 4 . 4 9 4"
  not read (the decipherer "di levar quel malo Imbasciatore").
- "che è là in nome di Re di Francia": 2090 6 0 4 4 0 2 6 0 6 5 2 6 0 7 2 0 4010.
- "che se si comporta molto mete pericolo, sì come oferisce": 2090 5 6 5 2 0 9 9 5 7 1 4 0 2 5 4 1 5 0 2 6 1 6 0 9 6 7 2 8 5 4 5
  0 5 2 0 4020 5 3 6 7 2 ? 3 6 (the decipherer "porta molti motti … et come offerisce").
- "con Turchi per asaltare […] asediare": 0 9 0 1 1 7 2 0 9 0 5020 4 5 4 4 1 4 7 6 0 9 0 4 5 6 7 2 4 7 6; the 9 before
  "asediare" not read.
- "Imbasciatori del Principe di Condé": 0 7 0 7 2 0 7 6 4 0 3^. 0 4 — 7070 + 2 (-i); dotted 3 + 4 read as the
  decipherer's "Principe di Condé".
- "Turchi": 1 1 7 + 2 0 9 (as Chiesa, chinea in R101).
- "oltra che Re di Francia mostreria": 5 4 1 7 4 0 2090 4010 2 5 5 1 7 6 7 2 4 — the decipherer "S.S. mostrarà".
- "Et per altra via se intende similmente": 0^.0 5020 4 4 1 7 4 1 2 4 5 6 2 6 1 6 6 7 6 5 2 2 2 6^4 3060.
- "lo Imbasciatore [di] Re di Francia": 4 5 0 7070 4010; no figures for "di" (also before "Francia", 7070 1050).
- "con Piali Bascià": 0 9? 0 9 2 4 4 2 0 8 4 5 8 2 4 — Piyale Pasha, kapudan of the Ottoman fleet.
- "contra Imperatore et contra la Italia, esortandolo a procurare": 9 1 7 4 2010 0^.0 9 1 7 4 4 4 0 3 0 5 6 5 5 7 1 4 6 7 5 4 5
  0 4 0 9 7 5 8 1 7 4 7 6.
- "di venire con grandisima armata a preocupare Roma et N.S.": 7 2 1 6 6 2 7 6 9 0 3 7 4 6 7 2 5 2 2 4 4 7 2 4 1 4 4 0 9 7 6 5 8
  1 9 4 7 6 7 5 2 4 0^.0 1010.
- "non solo come Imbasciatore [di] Francia ma anche de comissione delli principi protestanti": 2060 5 5 6^4 5 4020 7070 1050
  2 4 4 6 2090 7 6 8 5 2 2 5 2 5 6 6 7 6 4 2 ….
- "là […] Imbasciatori da lor parte": 4 4 0 5 2 2 6 2 0 5 0 7 0 7 2 0 7 4 0 4 5 7 0 9 4 7 1 6; "5 2 2 6 2 5" not read.
- "in Italia facilmente": 2 6 0 3 0 5 3 4 8 2 4 3060 (305 = 3050).
- "si manderiano infiniti Ugonotti": 5 2 2 4 6 7 6 7 2 4 6 5 2 6 3 2 6 2 1 2 8070.
- "delli Italiani": 7 6 4 2 0 3 0 5 6 2 (305 + n i), then filler.
