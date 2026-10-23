# R75 — Cardinal Francesco Barberini to the nuncio Ceva, cipher of Rome, 25 September 1632 (ASV SdS Francia 346, no. 2)

Rests on: the figures (`r75.retrans.txt`, re-transcribed from the images on 5 Oct 2026; one label corrected here,
`R75_corrections.tsv`) decoded with Lasry's key and the values adopted on 22-23 Oct 2026 (`b18_ceva_redecode.py` →
`r75.read3.txt`), read against the **contemporary decipherment on f. 82r** (`R75_decifrato_f82r.txt`; DECODE attachment
DOC_R75_D1145, labelled "082r.jpg [cleartext]", never opened before this re-read) and the 1632 interlinear on the cipher
page (`r75.interlinear.txt`). Where the decipherer and the figures differ, the figures are followed (list below). Word
alignment: `python research/reading_audit/b18_ceva_check.py r75` (every word carried by the figures or by f. 82r).
Spelling as the figures give it (the clerk writes doubled letters once); a code's word in the decipherer's spelling.
Marks: [?word] partly carried, [word] supplied, […] unread, [NNN] unidentified code.

## Reading

Le vitorie di Schombergh e della forza renderano per aventura più facile a V.S. il negotio del acomodamento di
Monsieur, ma più dificile asai quello del unione. Però è necessario ch'ella si sbraci a trovar motivi di persuadere
che ancora a detto compla per gli interessi di Francia l'unione. Io ne acennerò alcuni, et ella se ne serva secondo
li stimi […]. Il Cardinale Richelieu è avido di gloria, della quale non farà minor acquisto con l'unir le armi di
Francia vitoriose per asicurar la Religione Catolica di quello che sia stato portar le medesime armi alla vitoria.
Si asicura S.E. che ogni risolutione che farà non sarà ascrita hora a deboleza, sapendosi da tutti quanto posino
l'armi di Francia disimpegnate e vitoriose. Con la pace che può succedere dopo l'unione asicura S.E. le cose sue,
le quali in tempo di guerra sarano sempre in pericolo. È tempo che S.E. cominci a conoscere quanto sia pericolosa
alla Francia la potenza d'Olandesi, che cominciano hor mai a pensar a cose grandi et ad indrizar la […] loro a gli
Imperi. Consideri quanto sia oportuno alli vastisimi pensieri di quella natione estendere il loro dominio sino al
Mediteraneo con acquisto d'una piazza, e con quanto buon fondamento lo posono sperare in una revolutione del Regno
di Francia, alla quale è tanto sotoposto mentre hano tanto forze maritime e terestri. Consideri ancora S.E. che la
vitoria del Sueco è altretanto formidabile alla Francia quanto alla Germania. […] Ancora che se bene si agiustano
presentemente le cose con Monsieur, S.A. sarà sempre al medesimo, darà sempre orechie a consigli torbidi et haverà
chi gli li sugerisca; et un sucesor del Regno non si può restringer in maniera che sempre non habi libertà di salvar
in campagna. Però mentre vi è tema di moti interni bisogna cercar di compor gli esterni, che cagionerano e
fomenterano li domestici. Già S.E. è arivata a tal grado di gloria nelle cose di guerra che può con ragion temere
che la fortuna non si rivolti; cerchi dunque d'augumentarla con l'arti di pace, et se pur vuol seguitare ne gli
affari militari, indrizi le cose per intraprender guerra contro gli infedeli, che questa sola parte manca alla
gloria di S.E. In somma quanto le congiunture presente sono più contrarie alla sua negotiatione del unione, tanto più
deve V.S. pensar a ritrovar ragioni che la persuadano.

## Notes on the figures

- **Where the figures and f. 82r differ, the figures are followed**: "a V.S. il negotio" (411; f. 82r omits a V.S.);
  "che ancora a detto" (439; f. 82r "che à detto"); "se ne serva secondo li stimi […]" (figures `serva 494 li stimi v4`;
  f. 82r "se ne servirà secondo che giudicherà necessario"); "di Francia vitoriose" (84; f. 82r "della Francia"); "Si
  asicura S.E." (38; f. 82r "Si assicuri"); "che S.E. cominci a conoscere quanto sia" (315, 495, also the interlinear;
  f. 82r "che si cominci à conoscere che sia"); "di quella natione" (491; f. 82r "di Gostavo lo Svedese quella
  natione", the interlinear "di Goto natione"); "estendere"; "Consideri ancora S.E." (315; f. 82r omits S.E.); "del
  Sueco" (f. 82r "dello"); "quanto alla Germania" (495; f. 82r "che alla"); "le cose con Monsieur" (00; f. 82r "di
  Mons.r"); "contro gli infedeli" (f. 82r "con gl'infedeli"); "presente" (f. 82r "presenti"); "ritrovar".
- **Words carried by f. 82r alone** (no value of the key gives them; the figures are a code or garbled):
  Schombergh (357: `35 7 23` parsed i<723>; the decipherer's name, Henri de Schomberg, victor at Castelnaudary on
  1 Sept 1632), necessario (`98 423`), motivi (label 00 → 01 on the image), l'unione (`l st 054 ne`), Cardinale
  Richelieu (581), Religione Catolica (197), risolutione (`n 5`), Con [la] pace (`027`, `15 320`: pace = 153 + null 20,
  also R75 l.30 and R84 l.6), pensieri (`43 78 19 51 37 59 41` across the line end, garbled), revolutione (`n 4`),
  tanto (445), mentre (473, twice), S.A. (`o 4`; also a margin gloss "Monsieur S.A." on the cipher page), consigli
  (`al 9`), salvar (figures 85 = t, a slip; the interlinear also "salvar"), grado (`frad o`: 51 = f for g), nelle
  (`9 990 e`), di pace (`s o 3 720`), affari militari (`af 450 vsp 538 ri`), gloria (`floria`: 80 = f for g),
  negotiatione (`v 9`), Imperi (127; the interlinear "a gli Imperi[i?]").
- Carried in part by each: "d'augumentarla" (figures `d avg ch ementarla`, f. 82r "augumentarla"); "ritrovar" (figures
  `ri r rovar`, 70 = r for t; the 1632 interlinear "ritrovar", f. 82r "trovar").
- Left open: `serva 494 li stimi v4` (the decipherer's paraphrase does not match), `diolavse 1` at the head of l.21
  (no word in f. 82r or the interlinear), `la e8 loro` (f. 82r "la [?mira]", the interlinear "rep.la", neither read with
  certainty), the 88 between "a gli" and 127, and a stray 7 before "in pericolo" (`7 28`).
- Read on the image: l.3 "trovar motivi" is `59 24 01 31 85 35 75 17` (01 = m), not `00` (con) as transcribed; l.21
  "cose" is `71 31 94` (94 = se), not `97`.
- f. 82r is a working decipherment, not a copy of the figures: it improves the wording in places ("servirà secondo che
  giudicherà necessario", "che si cominci") and names Gustavus where the figures say only "quella natione".
