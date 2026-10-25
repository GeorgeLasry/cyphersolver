# vich1515: reading in the original spelling, line by line

AHN Estado 8715 N.73, Ferdinand the Catholic to Jerónimo de Vich, Pedrezuela, 26 October 1515. The cipher text only;
the clear docket (*a 26 de octubre 1515*), opening (*videlicet iterum*) and close (*en Pedrezuela a xxvj de otubre de
dxv*) are outside it.

**What it rests on.** The decode in `decode_aligned.md` (signs `keys/signs.txt`, groups `keys/groups.json`). The
spelling is the decode's: no accents, no letter changed, `u` for *v* and `i` for *j* as decoded, *Xpiandat* as
written. Word division, capitals and punctuation are editorial. A word broken at a line end is written whole on the
line where it starts, with `-` at the end of that line.

**Notation:**
- plain words: carried by the decode with firm values;
- `[?word]`: a doubtful word: a tentative group value (e.g. `[?papa]`, `[?uisorrey]`), or a word the decode gives
  only in part;
- `[x]` inside a word: a letter supplied;
- `[?]`: one unread code group, an unknown sign, or a stretch of letters that does not make a word.

**Look-alike readings.** Two labels are read with more than one value by context: `sin`/`sim` (*es* or *en*; 151
tokens, of which 71 read *en*) and `X` (*r*, *s* or *z*; 59 tokens read *s* or *z*). Each of those choices rests on the
other member of a look-alike pair, not on a value confirmed on the image for that token. See the count below.

```
  1  [?] esta haueros [?escrito] estos dias con diuerso[s]
  2  co[?]eos, por [?] y por [?tierra], y ultimamente por [?mar], a [?los]
  3  xui de [?esta] [?] [?] [?] las uuestras de x[?]uii del [?]
  4  [?] de [?] de [?esta] que [?tierra] por [?tierra] las que dezis que me haueys
  5  [?escrito] por [?mar], no las [?] [?] [?] y ahunque las [?]s que por los del
  6  uuestras letras [?] [?] no son para hauer [?plazer] con
  7  ellas pero [?] del cuydado en que estaua de no te-
  8  ner muchos dias hauia letras uuestras y [?] a responder a [?lo]
  9  contenido en [?ellas], digo que no puedo dexar de estar
 10  muy malcontento de uer que por la soberui[a] y locu-
 11  ra de suycos de no querer esperar a que nuestro exercito se iuntase con [?ellos]
 12  [?] y por la remision es mi uisorrey y capitan general de tardar tanto en
 13  iuntarse se hayan puesto todas las cosas de Italia en el pe-
 14  ligro, que oy estan pero para con uos [?] mucho [?mas] marauillado
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
 30  ra necesidad de todo esto como [?]e dicho, yo no creo ni creere sino
 31  lo que por obra uiere [?] pero uos al papa no le haueys de
 32  asomar [?ni] [?dezir] [?palabra] ninguna de esto sino [?solo] esfor-
 33  carle de mi parte, ni que por esta [?aduersidad], que por so-
 34  beruia y lo aura de suycos hauemos [?] no desmay[?]
 35  ni enflaquesca [?] [?] [?esta] con [?] [?]
 36  ni [?] [?] que damos tantos principes [?xpianos] y en
 37  [?] que le [?hauemos] de [?ayudar] y poner nuestras personas y
 38  estados por si y por la yg[?]ia [?] que es [?] que le
 39  quisiese ofender, y [?pues] con es ayuda de Dios y de tantos principes [?]
 40  [?] [?] [?] no le [?] [?] [?] [?]
 41  [?] y acuerdese que de la [?] [?me] [?] [?] es de [?papa]
 42  Iulio, pero al fin Dios no [?desampara] [?] y Dios [?]
 43  [?] a [?los] de la liga muy [?] [?] [?los] [?] de la yglia,
 44  y que assi tengo por certisimo que [?] [?] si [?los] [?confederados] perseue-
 45  ramos en [?lo] que [?esta] asentado con la [?] y constan-
 46  cia que [?] [?lo] [?] y que [?solo] ha [?permitido] [?esta] [?]
 47  [?] ni prouar si le somos constantes seruidores
 48  y que [?pues] suycos quieren tornar a [?uenir] y es emperador [?] que uerna
 49  en persona y [?] me de la [?empresa] y yo perseuero [?] en
 50  [?lo] de [?] [?] [?] y es que [?] [?ayudara] echar [?franceses] de Italia, que su [?]
 51  por su parte deue [?hazer] [?lo] mismo y [?mostrar] que su esf-
 52  uerco y [?] [?] de Leon porque [?] [?]
 53  [?] [?] [?] ganara haziendo lo assi tanto de lo
 54  [?] [?] [?] su flaquesa y que considere bien
 55  que si alguna [?] [?] de hauer con [?el] rey de francia [?]
 56  todos [?los] [?confederados] en [?ella] porque la de su [?] [?] no [?] [?]
 57  ni dar al rey de francia ni poder [?meior] hazer lo que qui-
 58  siere en Italia y [?] que lo ha ya [?] apoderarse del estado [?] [?]
 59  y poner persona de su mano [?] su mo pontifica-
 60  do por ser [?senor] de [?lo] espiritual y tenporal de la ygl-
 61  ia, por poder meior [?hazer] lo que quisiere es toda la
 62  Xpiandat, que es [?lo] que ha muchos anos que desean [?los] [?franceses] y [?lo]
 63  quieren y que por esto me paresce que es ninguna [?me] su [?] deue escu-
 64  char ninguna [?paz] del rey de francia sino asentando la todos los confederado[s] [?] iuntame-
 65  porque de [?esta] [?me] [?] segura y muy [?] y [?] la su
 66  [?] [?lo] no puede ser [?mas] peligrosa y [?] ni
 67  la dignidas de su persona y al estado de la yglia, y tome en-
 68  xenp[?lo] de la [?] [?] que es [?papa] Iulio [?] con [?]
 69  [?] Luys de Francia muerto por medio del [?] de Pauia, que no
 70  [?solo] no la guardo, pero puso con [?ella] [?] [?] necesidad al papa y a [?obligado]
 71  yglia, y nacio della la cisma y todas [?las] necesidades y tra-
 72  baios que [?] [?] [?lo] [?] no pudi [?] [?el] rey de francia [?] si la
 73  dicha [?paz] [?] no se asentara, y que [?mire] bien su [?] que por per-
 74  suasion de [?sus] parientes y personas inclinadas a
 75  [?franceses] no haga cosa que [?] [?] su [?] [?] procu-
 76  re de echarle [?] y que Dio[s] le [?] yo por
 77  que estoi dello muy malcontento del dicho mi uisorrey pero que [?pues] [?]
 78  [?nuestro] [?senor] assi lo [?] por prouar si [?somos]
 79  constantes [?] seruirle en la dicha santa [?empresa]
 80  que todos le deuemos dar gracias por [?ello], y tra-
 81  baiar de proseguir [?] [?] [?] y [?mas] [?]
 82  [?fuercas] y con [?mas] union y conformidad la dicha nuestra
 83  santisim[a] liga, ni que con es ayuda de Dios [?nuestro] [?senor]
 84  salgamos con nuestra [?] y que yo espero en todo
 85  en [?diuina] clemencia, que [?] la [?] que tenemos [?] la
 86  defension de Italia en muy [?] y la de [?] [?]
 87  [?] [?] [?] [?] [?] [?] muy cum-
 88  plida [?] y [?] yo la tengo [?] por [?mas] [?] por [?] [?los] dicho[s] [?]
 89  [?] han quedado muy quebrados y ame-
 90  drentados de la dicha [?] y que yo perseuerando como pe-
 91  rseuero en la dicha liga y cumpliendo lo que por mi
 92  parte soy obligado, [?he] escrito al dicho mi uisorrey y capitan general [?repre-]
 93  [?hendiendole] grauemente de la dicha su neglige-
 94  [?ncia] y [?mandandole] muy estrechamente que de [?aqui]
 95  a delante se guarde de [?] otro tal y [?]
 96  y que assimismo le [?he] enbiado a [?] que si los dichos suycos
 97  [?] [?] [?] en [?] a en
 98  fauor de nuestra santisim[a] liga, como yo tengo por [?] que [?lo] ha-
 99  ran, que esta [?] [?] sin dilacion alguna se [?] con
100  [?ellos] como [?] [?] y con buen conseio
101  todo [?lo] que sea [?] y [?conueniente] [?esta] e como la defension y conserua-
102  cion de Italia y como la resistencia de [?franceses] hasta e-
103  charlos de Italia con es ayuda de Dios [?nuestro] [?senor], y que assimismo [?he] es-
104  crito al emperador rogandole que uenga [?] [?] ninguna
105  [?] en la dicha [?empresa] como lo ha [?enbiado]
106  a ofrescer al [?papa] por [?] de que yo les ruego
107  muy afectuosamente que no desmayen, como
108  tengo por [?] que no [?lo] haran, y que continuando su si-
109  ngu[?lo]s [?] y [?esfuerco] [?] en por
110  parte en la dicha nuestra santisima liga, y hagan y procur-
111  en con suma diligencia [?] fauor [?] todo [?lo] que
112  sea [?] y [?conueniente] [?esta] e como la defension y conseruacion
113  de Italia y como la resistencia de [?los] dicho[s] [?franceses] [?]
114  [?] con que la faltando [?los] otros [?confederados] yo [?]
115  [?] [?] faltar ni [?faltare] iamas a la defension de [?]
116  y a la prosecucion de la dicha [?empresa], y a [?esta] pro-
117  posito les enbia a dezir y ofrescer todo [?lo]
118  que [?mas] [?] [?] que conuenga como esforcar [?lo] [?]
119  ni [?] los y como [?] sino [?] [?] [?]
120  a la dicha [?empresa] [?] [?] [?] [?ella] [?] [?] [?me] [?]
121  alguna y [?hazer me eys] [?] [?] con duplicadas
122  y triplicadas uias [?por] [?mar] y por [?tierra], [?lo] que es todo
123  [?lo] suso dicho [?] [?lo] que [?mas] [?] se ofres-
124  cieren
```

## Measured

Counted on the reading above, a broken word counted once:

| | words | read as sense | holes and doubtful words | read share |
|---|---|---|---|---|
| ll. 1–124 | 1,335 | 844 | 491 | 0.63 |

A doubtful word (`[?word]`, including every tentative group value) counts as a hole, as the bar requires; with the
tentative group values counted as read the share would be higher, but they are not confirmed.

**Look-alike share.** Letters that rest on the second member of a look-alike pair: the 67 tokens
transcribed `sin` and read *en* (134 letters; the 4 transcribed `sim` are not counted) and the 59 `X` read *s* or *z*
(59 letters): 193 of the 4,900 decoded letters, **3.9%**, above the 3% limit. Only six of the `sin`
tokens were checked on the image (p. 3, ll. 8–10).

**Class.** *Decoded, not read* by the bar as written: under 95% of words read as sense, and look-alike readings above
3% without a contemporary text to confirm them. Stretches build coherent sentences (ll. 7–10, 14–19, 23–25, 33–34,
37–38, 57–61, 69–71, 73–75, 77–80, 89–94, 101–104, 106–110), so a better image of the `sin`/`sim` and `X` tokens is
what would move it to *read in part*.
