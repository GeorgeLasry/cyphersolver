# vich1515: reading in the writer's spelling, line by line

AHN Estado 8715 N.73, Ferdinand the Catholic to Jerónimo de Vich, Pedrezuela, 26 October 1515. The cipher text only;
the clear docket (*a 26 de octubre 1515*), opening (*videlicet iterum*) and close (*en Pedrezuela a xxvj de otubre de
dxv*) are outside it.

**What it rests on.** Each line is the decode of the same line of the repository's transcription
(`n73_transcription.txt`), with the sign values in `brackx2026/keys/signs.txt` and the group values in `brackx2026/keys/groups.json`; the
token-by-token alignment is in `texts/n73_tokens.tsv`. The spelling is the decode's: no accents, no normalisation, no letter
changed (`u` for *v*, `i` for *j*, *Xpiandat*, *flaquesa*, *dignidas* as decoded). Word division, capitals and
punctuation are editorial. A word broken at a line end ends with `-` and continues on the next line.

**Notation:**
- plain words: carried by firm values;
- `[x]`: a letter supplied (nothing in the cipher carries it);
- `[?word]`: a doubtful word: the decode gives it only in part (a letter differs or is missing);
- `{?word}`: a tentative value of a code group (or of a tentative sign such as `SL` = *st*); inside a word only the
  tentative stretch is braced (`{?ayuda}r`, `e{?st}a`);
- `[?3 groups]`: a run of unread code groups, sized; `[?sign]` / `[?2 signs]` signs with no value; `[?5 letters]` decoded
  letters that make no word; parts joined by commas (`[?1 group, 3 letters]`). A label glued to letters marks a gap
  inside a word (`co[?sign]eos`).

**Look-alike readings.** `sin`/`sim` (*es*/*en*) and `X` (*r*/*s*/*z*) are read token by token. Only six `sin` tokens
were read on the image; every other choice is model-assigned. Each token, with its basis and the model's margin, is
listed in `texts/n73_sin_x_tokens.tsv`.

## Reading

```
  1  [?1 group] {?esta} haueros [?escrito] dos dias con diuerso[s]
  2  co[?sign]eos, por [?1 group] y por {?tierra}, y ultimamente por {?mar}, a {?lo}s
  3  xui de {?esta} [?3 groups, 1 sign, 5 letters] las uuestras de x[?sign]uii del [?4 letters]
  4  [?3 letters] de [?3 letters] de {?esta} que {?tierra} por {?tierra} las que dezis que me haueys
  5  [?escrito] por {?mar}, no las [?2 groups, 1 sign, 1 letter] y [?1 group] las [?1 group, 1 letter] que por {?lo}s [?3 letters]
  6  uuestras letras [?1 group, 3 letters] no son ni [?hauer] [?6 letters] con
  7  {?ella}s {?antes} [?8 letters] del cuydado en que estaua de no te-
  8  ner [?1 group, 1 letter] dias hauia letras uuestras y [?1 group] a responder a {?lo}
  9  contenido en {?ella}s, digo que no puedo dexar de [?estar]
 10  muy {?mal}contento de uer que por la [?soberuia] y {?lo} au-
 11  ra de [?1 letter] de no querer esperar a que [?1 group, 1 letter] se [?1 group] se con [?2 letters]
 12  [?1 letter] y por la remision es mi {?uisorrey} y [?1 group] de tardar [?1 group] en
 13  [?1 group, 1 letter] se se ha [?1 group, 1 letter] esto {?e}s las cosas de Italia es en pe-
 14  ligro, que oy {?esta}n {?antes} ni con {?esto}s [?1 group] {?mal}[?11 letters]
 15  y peor contento [?doy] de uer la flaquesa del {?papa}
 16  y [?4 letters] determinado esta de [?1 group] certarse con [?1 group], no
 17  guardando en {?ello} {?lo} que {?esta} capitulado, que [?1 group] de
 18  {?lo}s [?1 group, 1 letter] no pueda hazer, es ni tregua con ningu-
 19  [?1 group] sin sabiduria y [?1 group] de todos {?lo}s {?confederado}s, y [?siendo] ha
 20  quebrado las capitulacion[?1 letter], no espero con [?2 letters]
 21  [?2 groups] cosa la ha de guardar [?1 group] en {?esto} ha [?1 group] como [?dezis]
 22  prometido que asentara las [?2 letters] con [?1 group] sin [?4 letters]
 23  yo de las captulaciones que [?1 group] en {?emperador} y comi-
 24  go [?1 group] asentadas y [?1 group] guardara [?1 group] que por la capi-
 25  tulacion de la liga general esta capitulado y que
 26  [?1 letter] uer que en {?emperador} y yo y [?12 letters] [?resistir] [?1 group]
 27  {?frances} y [?10 letters] echarle de Italia en {?ayuda}[?2 letters] ni {?ello} como
 28  por las capitulacio[?1 letter] en {?obligado}, porque esta es que
 29  [?quiere] asentar con {?franceses}, la [?1 group, 3 letters] por [?1 group, 7 letters]
 30  [?1 group, 2 letters] de todo [?2 letters] como [?sign]e dicho, yo no creo ni creere sino
 31  {?lo} que por [?1 group, 1 sign, 7 letters] {?antes} {?esto} al {?papa} no le haueys de
 32  [?6 letters] la [?1 group, 12 letters] de [?2 letters] sino {?solo} esfor-
 33  carle de mi parte, ni que por esta [?aduersidad], que por so-
 34  beruia y lo aura de [?1 letter] hauemos [?1 group] no desmay[?1 letter]
 35  ni enflaquesca [?2 groups] {?esta} con [?1 group, 9 letters]
 36  ni [?6 letters] que damos [?2 groups, 6 letters] nos y en
 37  [?1 group] que le [?hauemos] de [?ayudar] y poner nuestras personas y
 38  estados por si y por la yg[?sign]ia [?1 letter] que es [?1 group] que le
 39  quisiese ofender, y es con [?2 letters] {?ayuda} de Dios y de [?2 groups, 4 letters]
 40  [?2 groups, 5 letters] no le [?28 letters]
 41  [?4 letters] y acuerdese que de la [?3 letters] {?me} [?1 group, 5 letters] es de {?papa}
 42  Iulio, {?antes} al fin Dios no [?desampara] [?7 letters] y Dios [?1 group]
 43  [?4 letters] a {?lo}s de la liga muy [?1 group, 6 letters] {?lo}s [?3 letters] de la yglia,
 44  y que [?1 group] tengo por certisimo que [?2 groups] si {?lo}s {?confederado}s perseue-
 45  ramos en {?lo} que {?esta} asentado con la [?1 group, 2 letters] y constan-
 46  cia que [?1 group] {?lo} [?7 letters] y que {?solo} ha [?permitido] {?esta} [?3 letters]
 47  [?2 letters] ni prouar si le somos constantes seruidores
 48  y que es [?1 group, 14 letters] y es {?emperador} [?4 letters] que uerna
 49  en persona y [?1 group] me de la [?empresa] y yo perseuero [?1 group] en
 50  {?lo} de [?2 groups, 3 letters] y es que [?3 letters] {?ayuda}ra echar {?franceses} de Italia, que su [?1 sign, 1 letter]
 51  por su parte deue [?hazer] {?lo} mismo y [?mostrar] que su esf-
 52  uerco y [?1 group, 10 letters] de Leon porque [?2 groups]
 53  [?1 group, 12 letters] ganara haziendo {?lo} [?2 groups] de {?lo}
 54  [?16 letters] su flaquesa y que considere [?1 group]
 55  que si alg[?1 group, 1 letter] [?10 letters] de hauer con [?2 letters] {?frances} [?7 letters]
 56  todos {?lo}s {?confederado}s en {?ella} porque la de su [?1 sign, 5 letters] no [?7 letters]
 57  ni dar al {?frances} ni poder {?me}ior hazer {?lo} que qui-
 58  siere en Italia y [?1 group] que {?lo} ha [?2 groups] apoderarse del [?2 groups, 2 letters]
 59  y poner persona de su mano [?4 letters] su mo pontifica-
 60  do por ser {?senor} de {?lo} espiritual y tenporal de la ygl-
 61  ia, por poder meior [?hazer] {?lo} que [?quisiere] [?3 letters] la
 62  Xpiandat, que es {?lo} que ha [?1 group, 5 letters] que desean {?lo}s {?franceses} y {?lo}
 63  [?1 group, 1 letter] y que por [?2 letters] me parece que es [?1 group] {?me} su [?1 sign, 1 letter] deue escu-
 64  char [?1 group, 2 letters] del {?frances} sino asentando la todos {?lo}s [?confederados] [?1 group, 4 letters]
 65  porque de {?esta} {?me} [?1 group] segura y muy [?1 group] y [?9 letters] la su
 66  [?1 sign, 4 letters] {?lo} no puede ser {?mas} peligrosa y [?6 letters] ni
 67  la dignidas de su persona y al [?1 group] de la yglia, y tome en-
 68  xenp{?lo} de la [?1 group, 2 letters] que es {?papa} Iulio [?6 letters] con [?2 letters]
 69  [?1 group] Luys de [?1 group] muerto por medio del [?1 group] de Pauia, que no
 70  {?solo} no la guardo, {?antes} puso con {?ella} [?2 groups, 2 letters] al {?papa} y a {?obligado}
 71  yglia, y nacio de e{?st}a la cisma y [?2 letters] la [?1 group, 4 letters] y tra-
 72  baios que [?1 group, 5 letters] {?lo} [?1 group] no pudi [?1 group, 2 letters] {?frances} [?5 letters] si la
 73  [?1 group, 3 letters] no se asentara, y que [?1 group, 4 letters] su [?1 sign, 1 letter] que por per-
 74  suasion de [?sus] parientes y personas inclinadas a
 75  {?franceses} no haga cosa que [?10 letters] su [?1 group, 4 letters] procu-
 76  re de echarle [?1 group] y que Dio[s] le [?7 letters] yo por
 77  que doy de e{?st}o muy {?mal}contento del dicho mi {?uisorrey} {?antes} que es [?3 letters]
 78  [?1 letter] {?senor} [?1 group] {?lo} [?9 letters] por prouar si {?so}mos
 79  constantes [?2 letters] seruirle en la santa [?empresa]
 80  que todos le deuemos dar gracias por {?ello}, y tra-
 81  baiar de proseguir [?2 groups, 4 letters] y {?mas} [?5 letters]
 82  [?1 group, 4 letters] y con {?mas} union y conformidad la nuestra
 83  santisim[a] liga, ni que con [?2 letters] {?ayuda} de Dios [?1 letter] {?senor}
 84  salgamos con nuestra [?9 letters] y que yo espero en todo
 85  en [?diuina] clemencia, que es la [?1 group] que tenemos [?1 group] la
 86  defension de Italia en muy [?1 group] y la de [?12 letters]
 87  [?3 groups, 22 letters] muy cum-
 88  plida [?1 group] y [?1 group] yo la tengo [?1 group] por {?mas} [?1 group] por [?1 group] {?lo}s dicho[s] [?3 letters]
 89  [?11 letters] han quedado muy quebrados y ame-
 90  drentados de las [?1 group] y que yo perseuerando como pe-
 91  rseuero en la liga y cumpliendo {?lo} que por mi
 92  parte soy {?obligado}, [?he] escrito al dicho mi {?uisorrey} y [?1 group, 3 letters] [?repre-]
 93  [?hendiendole] grauemente de la su neglige-
 94  [?ncia] y [?mandandole] muy estrechamente que de [?1 group]
 95  a delante se guarde de [?1 group, 7 letters] tal y [?2 letters]
 96  y que [?1 group] le [?he] enbiado a [?1 sign, 5 letters] que si {?lo}s dichos [?1 letter]
 97  [?1 group, 23 letters] en [?1 letter] a en
 98  fauor de nuestra santisim[a] liga, como yo tengo por [?3 letters] que {?lo} ha-
 99  ran, que esta [?1 group, 2 letters] sin dilacion alg[?1 group] se [?1 group] con
100  {?ello}s como [?15 letters] y con buen conseio
101  todo {?lo} que sea [?2 letters] y [?conueniente] {?esta} e como la [?1 group] y conserua-
102  cion de Italia y como la resistencia de {?franceses} hasta e-
103  char{?lo}s de Italia con [?2 letters] {?ayuda} de Dios [?1 letter] {?senor}, y que [?1 group, 1 letter] [?he] es-
104  crito al {?emperador} rogandole que uenga [?1 group, 3 letters]
105  [?9 letters] en la [?empresa] como {?lo} ha [?enbiado]
106  a ofrescer al {?papa} por [?2 letters] de que yo les ruego
107  muy afectuosamente que no desmayen, como
108  tengo por [?1 group] que no {?lo} haran, y que continuando su si-
109  ngu{?lo}s [?1 group] y [?esfuerco] [?3 letters] en por
110  parte en la nuestra santisima liga, y hagan y procur-
111  en con suma diligencia [?2 letters] fauor [?1 group] todo {?lo} que
112  sea [?1 group] y [?conueniente] {?esta} e como la [?1 group] y conseruacion
113  de Italia y como la resistencia de {?lo}s dicho[s] {?franceses} [?4 letters]
114  [?7 letters] con que la faltando {?lo}s [?1 group, 1 letter] {?confederado}s yo [?1 letter]
115  [?1 group, 4 letters] faltar ni [?faltare] iamas a la [?1 group] de [?1 group]
116  y a la prosecucion de las [?empresas], y a {?esta} pro-
117  posito les enbia a dezir y ofrescer todo {?lo}
118  que {?mas} [?1 group, 6 letters] que conuenga como esforcar {?lo} [?2 letters]
119  ni [?1 group, 3 letters] {?lo}s y como [?1 group] sino [?1 group, 15 letters]
120  a las [?empresas] [?9 letters] {?ella} [?5 letters] {?me} [?4 letters]
121  alg[?1 group] y [?hazer me eys] [?1 group, 1 letter] con duplicadas
122  y triplicadas {?cart}as {?por} {?mar} y por {?tierra}, {?lo} que es todo
123  {?lo} suso dicho [?10 letters] {?lo} que {?mas} [?1 group] se ofres-
124  cieren
```

## Measured

| | words | holes and doubtful words | read share |
|---|---|---|---|
| ll. 1–124, the repository's measure (`research/reading_audit/v10_relabel.py`) | 839 | 480 | **0.636** |

Marks in the reading: 148 words carrying a tentative value `{?…}`, 50 doubtful words `[?word]`, 6 words with a supplied
letter, and the unread runs (140 unread groups, 9 unvalued signs, 140 runs of letters that make no word). Every
tentative value counts as a hole, as the bar requires. The sentence score (`research/reading_audit/v2_score.py`, Spanish) is 0.058 clean
sentences with explicit holes (4 of 69).

**Look-alike share.** Letters resting on the second member of a look-alike pair: the 67 tokens transcribed `sin` and read
*en* (134 letters) and the 59 `X` read *s* or *z* (59 letters): 193 of the 4,900 decoded letters, **3.9%**, above the 3%
limit, and only 6 of them checked on the image.

**Class.** *Decoded, not read*: under 95% of words read as sense, and look-alike readings above 3% without a contemporary
text to confirm them. Stretches build sentences (ll. 7–10, 14–19, 23–25, 33–34, 37–38, 57–61, 69–71, 73–75, 77–80,
89–94, 101–104, 106–110). A sharper image of the `sin`/`sim` and `X` tokens, or a printed text of the letter, is what
would move it.
