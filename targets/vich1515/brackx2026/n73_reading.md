# vich1515: reading in the writer's spelling, line by line

AHN Estado 8715 N.73, Ferdinand the Catholic to Jerónimo de Vich, Pedrezuela, 26 October 1515. The cipher text only;
the clear docket (*a 26 de octubre 1515*), opening (*videlicet iterum*) and close (*en Pedrezuela a xxvj de otubre de
dxv*) are outside it.

**What it rests on.** Each line is the decode of the same line of the repository's transcription
(`n73_transcription.txt`), with the sign values in `keys/signs.txt` and the group values in `keys/groups.json`; the
token-by-token alignment is in `tokens.tsv`. The spelling is the decode's: no accents, no normalisation, no letter
changed (`u` for *v*, `i` for *j*, *Xpiandat*, *flaquesa*, *dignidas* as decoded). Word division, capitals and
punctuation are editorial. A word broken at a line end ends with `-` and continues on the next line.

**Notation:**
- plain words: carried by firm values;
- `[x]`: a letter supplied (nothing in the cipher carries it);
- `[?word]`: a doubtful word: the decode gives it only in part (a letter differs or is missing);
- `{?word}`: a tentative value of a code group (or of a tentative sign such as `LAM` = *an*); inside a word only the
  tentative stretch is braced (`est{?an}`);
- `[?3 groups]`: a run of unread code groups, sized; `[?sign]` / `[?2 signs]` signs with no value; `[?5 letters]` decoded
  letters that make no word; parts joined by commas (`[?1 group, 3 letters]`). A label glued to letters marks a gap
  inside a word (`co[?sign]eos`).

**Look-alike readings.** `sin`/`sim` (*es*/*en*) and `X` (*r*/*s*/*z*) are read token by token. Six `sin` tokens
were read on the image and 38 `sin`/`sim`/`X` tokens in ll. 9–31 are decided by the printed quotation of the letter
(Terrateig 1963, see `notes/solve_notes.md`, "The Terrateig crib"); every other choice is model-assigned. Two image
readings disagree with the print: 13.19 (*es* on the image, *en* printed) now follows the print, and 12.11 (*es*,
where the print has *de mi uisorrey*) is left as read. Each token,
with its basis and the model's margin, is listed in `sin_x_tokens.tsv`.

## Reading

```
  1  [?1 group] esta haueros [?escrito] estos dias con diuerso[s]
  2  co[?sign]eos, por [?1 group] y por tierra, y ultimamente por mar, a los
  3  xui de esta [?3 groups, 1 sign, 5 letters] las uuestras de x[?sign]uii del [?4 letters]
  4  [?3 letters] de [?3 letters] de esta que tierra por tierra las que dezis que me haueys
  5  [?escrito] por mar, no las [?2 groups, 1 sign, 1 letter] y ahunque las [?1 group]s que por los del
  6  uuestras letras [?1 group, 3 letters] no son para hauer [?plazer] con
  7  ellas pero [?8 letters] del cuydado en que estaua de no te-
  8  ner muchos dias hauia letras uuestras y [?1 group] a responder a lo
  9  contenido en ellas, digo que no puedo dexar de estar
 10  muy malcontento de uer que por la soberui[a] y locu-
 11  ra de suycos de no querer esperar a que nuestro exercito se iuntase con [?ellos]
 12  [?1 letter] y por la remision es mi uisorrey y capitan general de tardar tanto en
 13  iuntarse se hayan puesto todas las cosas de Italia en el pe-
 14  ligro, que oy estan pero para con uos [?1 letter] mucho [?mas] marauillado
 15  y peor contento estoi de uer la flaqueza del papa
 16  y [?quan] determinado esta de concertarse con franceses, no
 17  guardando en ello lo que esta capitulado, que ninguno de
 18  los confederados no pueda hazer paz ni tregua con ningu-
 19  [n] principe sin sabiduria y uoluntad de todos los confederados, y pues en esto ha
 20  quebrado la dicha capitulacion, no espero [?que] en
 21  ninguna otra cosa la ha de guardar, ahunque [?el] uos haya, como dezis
 22  prometido que asentara la dicha paz con Francia sin peri-
 23  uizyo de las captulaciones que con el emperador y comi-
 24  go tiene asentadas y assimismo guardara lo que por la capi-
 25  tulacion de la liga general esta capitulado y que
 26  toda uez que el emperador y yo y suycos quisieremos resistir al
 27  rey de francia y entender en echarle de Italia [?el] ayudara para ello como
 28  por la dicha [?capitulacion] es obligado, porque esta paz que
 29  quiere asentar con franceses, la haze por fuerca y pu-
 30  ra necesidad de todo esto como [?sign]e dicho, yo no creo ni creere sino
 31  lo que por obra uiere [?sign] pero uos al papa no le haueys de
 32  asomar [?ni] [?dezir] [?palabra] ninguna de esto sino solo esfor-
 33  carle de mi parte, ni que por esta [?aduersidad], que por so-
 34  beruia y lo aura de suycos hauemos [?1 group] no desmay[?1 letter]
 35  ni enflaquesca [?2 groups] esta con [?1 group, 9 letters]
 36  ni [?8 letters] que damos tantos principes [?xpianos] y en
 37  [?1 group] que le hauemos de [?ayudar] y poner nuestras personas y
 38  estados por si y por la yg[?sign]ia [?1 letter] que es [?1 group] que le
 39  quisiese ofender, y pues con es ayuda de Dios y de tantos principes [?2 letters]
 40  [?2 groups, 5 letters] no le [?30 letters]
 41  [?4 letters] y acuerdese que de la [?3 letters] {?me} [?1 group, 5 letters] es de papa
 42  Iulio, pero al fin Dios no [?desampara] [?7 letters] y Dios [?1 group]
 43  [?4 letters] a los de la liga muy [?1 group, 6 letters] los [?3 letters] de la yglia,
 44  y que assi tengo por certisimo que [?2 groups] si los confederados perseue-
 45  ramos en lo que esta asentado con la [?1 group, 2 letters] y constan-
 46  cia que [?1 group] lo [?7 letters] y que solo ha [?permitido] esta [?3 letters]
 47  [?2 letters] ni prouar si le somos constantes seruidores
 48  y que pues suycos quieren tornar a [?uenir] y es emperador [?4 letters] que uerna
 49  en persona y [?1 group] me de la [?empresa] y yo perseuero [?1 group] en
 50  lo de [?2 groups, 3 letters] y es que [?3 letters] ayudara echar franceses de Italia, que su [?1 sign, 1 letter]
 51  por su parte deue [?hazer] lo mismo y [?mostrar] que su esf-
 52  uerco y [?1 group, 10 letters] de Leon porque [?2 groups]
 53  [?1 group, 12 letters] ganara haziendo lo assi tanto de lo
 54  [?16 letters] su flaquesa y que considere bien
 55  que si alguna [?12 letters] de hauer con [?el] rey de francia [?7 letters]
 56  todos los confederados en ella porque la de su [?1 sign, 5 letters] no [?7 letters]
 57  ni dar al rey de francia ni poder {?me}ior hazer lo que qui-
 58  siere en Italia y [?1 group] que lo ha ya [?1 group] apoderarse del estado [?1 group, 2 letters]
 59  y poner persona de su mano [?4 letters] su mo pontifica-
 60  do por ser senor de lo espiritual y tenporal de la ygl-
 61  ia, por poder meior [?hazer] lo que {?q}uisiere es toda la
 62  Xpiandat, que es lo que ha muchos anos que desean los franceses y lo
 63  quieren y que por esto me paresce que es ninguna {?me} su [?1 sign, 1 letter] deue escu-
 64  char ninguna paz del rey de francia sino asentando la todos los confederado[s] [?2 letters] iuntame-
 65  porque de esta {?me} [?1 group] segura y muy [?1 group] y [?9 letters] la su
 66  [?1 sign, 4 letters] lo no puede ser mas peligrosa y [?6 letters] ni
 67  la dignidas de su persona y al estado de la yglia, y tome en-
 68  xenplo de la [?2 groups] que es papa Iulio [?6 letters] con [?2 letters]
 69  [?1 group] Luys de Francia muerto por medio del [?1 group] de Pauia, que no
 70  solo no la guardo, pero puso con ella [?1 group, 2 letters] necesidad al papa y a obligado
 71  yglia, y nacio della la cisma y todas [?las] necesidades y tra-
 72  baios que [?1 group, 5 letters] lo [?1 group] no pudi [?1 group] [?el] rey de francia [?5 letters] si la
 73  dicha paz [?1 group] no se asentara, y que [?mire] bien su [?1 sign, 1 letter] que por per-
 74  suasion de [?sus] parientes y personas inclinadas a
 75  franceses no haga cosa que [?10 letters] su [?1 group, 4 letters] procu-
 76  re de echarle [?1 group] y que Dio[s] le [?7 letters] yo por
 77  que estoi dello muy malcontento del dicho mi uisorrey pero que pues [?3 letters]
 78  nuestro senor assi lo [?9 letters] por prouar si {?so}mos
 79  constantes [?2 letters] seruirle en la dicha santa [?empresa]
 80  que todos le deuemos dar gracias por ello, y tra-
 81  baiar de proseguir [?1 group, 11 letters] y mas [?5 letters]
 82  [?fuercas] y con mas union y conformidad la dicha nuestra
 83  santisim[a] liga, ni que con es ayuda de Dios nuestro senor
 84  salgamos con nuestra [?9 letters] y que yo espero en todo
 85  en [?diuina] clemencia, que [?1 group] la [?1 group] que tenemos [?1 group] la
 86  defension de Italia en muy [?1 group] y la de [?12 letters]
 87  [?3 groups, 22 letters] muy cum-
 88  plida [?1 group] y [?1 group] yo la tengo [?1 group] por mas [?1 group] por [?1 group] los dicho[s] [?3 letters]
 89  [?11 letters] han quedado muy quebrados y ame-
 90  drentados de la dicha [?1 group] y que yo perseuerando como pe-
 91  rseuero en la dicha liga y cumpliendo lo que por mi
 92  parte soy obligado, [?he] escrito al dicho mi uisorrey y capitan general [?repre-]
 93  [?hendiendole] grauemente de la dicha su neglige-
 94  [?ncia] y [?mandandole] muy estrechamente que de {?aqui}
 95  a delante se guarde de [?7 letters] otro tal y [?2 letters]
 96  y que assimismo le [?he] enbiado a [?1 sign, 5 letters] que si los dichos suycos
 97  [?13 letters] en [?13 letters] a en
 98  fauor de nuestra santisim[a] liga, como yo tengo por [?3 letters] que lo ha-
 99  ran, que esta [?1 group, 2 letters] sin dilacion alguna se [?1 group] con
100  ellos como [?15 letters] y con buen conseio
101  todo lo que sea [?2 letters] y [?conueniente] esta e como la defension y conserua-
102  cion de Italia y como la resistencia de franceses hasta e-
103  charlos de Italia con es ayuda de Dios nuestro senor, y que assimismo [?he] es-
104  crito al emperador rogandole que uenga [?3 letters] ninguna
105  [?9 letters] en la dicha [?empresa] como lo ha [?enbiado]
106  a ofrescer al papa por [?2 letters] de que yo les ruego
107  muy afectuosamente que no desmayen, como
108  tengo por [?1 group] que no lo haran, y que continuando su si-
109  ngulos [?1 group] y esfuerco [?3 letters] en por
110  parte en la dicha nuestra santisima liga, y hagan y procur-
111  en con suma diligencia [?2 letters] fauor [?1 group] todo lo que
112  sea [?1 group] y [?conueniente] esta e como la defension y conseruacion
113  de Italia y como la resistencia de los dicho[s] franceses [?4 letters]
114  [?7 letters] con que la faltando los otros confederados yo [?1 letter]
115  [?1 group, 4 letters] faltar ni [?faltare] iamas a la defension de [?1 group]
116  y a la prosecucion de la dicha [?empresa], y a esta pro-
117  posito les enbia a dezir y ofrescer todo lo
118  que mas [?1 group, 6 letters] que conuenga como esforcar lo [?2 letters]
119  ni [?1 group, 3 letters] los y como [?1 group] sino [?17 letters]
120  a la dicha [?empresa] [?9 letters] ella [?5 letters] {?me} [?4 letters]
121  alguna y [?hazer me eys] [?1 group, 1 letter] con duplicadas
122  y triplicadas uias {?por} mar y por tierra, lo que es todo
123  lo suso dicho [?10 letters] lo que mas [?1 group] se ofres-
124  cieren
```

## Measured

| | words | holes and doubtful words | read share |
|---|---|---|---|
| ll. 1–124, the repository's measure (`research/reading_audit/v10_relabel.py`) | 1,099 | 235 | **0.824** |
| ll. 9–31, the stretch covered by Terrateig's quotation | 243 | 13 | 0.949 |
| ll. 1–124 after the crib, before the rounds | 1,031 | 303 | 0.773 |
| ll. 1–124 before the crib (commit e10b519) | 839 | 480 | 0.636 |

Marks in the reading: 9 words carrying a tentative value `{?…}`, 51 doubtful words `[?word]`, 9 words with a supplied
letter, and the unread runs (76 unread groups, 13 unvalued signs, 91 runs of letters that make no word). Every
tentative value counts as a hole, as the bar requires. The sentence score (`v2_score.py`) was not rerun after the crib
(before it: 0.058, 4 of 69 clean sentences).

**Look-alike share.** Letters resting on the second member of a look-alike pair and decided neither by the image nor
by the crib: 57 tokens transcribed `sin` and read *en* (114 letters) and 51 `X` read *s* or *z* (51 letters): 165 of
the 5,337 decoded letters, **3.09%** (3.9% before the crib), still above the 3% limit (160 letters would meet it).

**Class.** *Decoded, not read*: the look-alike readings are above 3%; with under 95% of words read as sense it could
otherwise be at most *read in part*. The change is that
ll. 9–31 now rest on a printed text of the letter (Terrateig's quotation, about 250 words), which settles 45 group
values and 38 look-alike tokens there; outside that stretch the reading is as before plus the values carried over
and those read in the four rounds after the crib (`notes/solve_notes.md`).
Stretches build sentences (ll. 7–31, 33–34, 37–38, 57–61, 69–71, 73–75, 77–80, 89–94, 101–104, 106–110). A sharper
image of the `sin`/`sim` and `X` tokens, or the minute in Simancas (AGS Estado leg. 847), is what would move it further.
