# Biermann to Just Høeg (The Hague), Copenhagen 12 January 1675: cipher passage

Source: Rigsarkivet, TKUA Almindelig del, Conrad Biermanns kopibog 1675 (S-1418), pp. 12v-13,
Arkivalieronline image 016 (heading and clear opening on p. 12v, left page; cipher on p. 13, right page;
id 48573967).
Key: TKUA "Chiffer" 1670-1709, image 55 (`key.tsv`). Transcription: `transcription_1675-01-12_hoeg.txt`;
mechanical decipherment: `python decode.py transcription_1675-01-12_hoeg.txt`.

Clear text before the cipher: no post from Høeg; the Swedish ambassador is paying his visits and has asked for
commissioners; his King is said to be displeased that he was so long on the road. "Il semble que ..."

## Line by line

| line | decipherment |
|---|---|
| 13.01 | {France} e t {Suède} ne de {31 = s} e s pe re n |
| 13.02 | t pa {31 = s} [tout a fait] de re {330: ga} g ne |
| 13.03 | r {l'Electeur de Brandebourg} [du moins et il est certain que] ce s de |
| 13.04 | u x co u ro n ne s fo n t t |
| 13.05 | ra i t te r so u b s ma i |
| 13.06 | n a ve c lu y [de sorte que les affaires] |
| 13.07 | [ayant changé de face en Alsace par la retraitte des] |
| 13.08 | [alliés vers Strasbourg il y] s t a c ra i n |
| 13.09 | d re que si le di t {l'Electeur de Brandebourg} re ma r |
| 13.10 | que que l que f ro i de u {8: r} a |
| 13.11 | la s si s te r la ja lo u si |
| 13.12 | e [et] le me co n te n te me n |
| 13.13 | t qui l a [d'ailleurs] de s i m pe ri |
| 13.14 | a u x ne le po r te n t [derechef] |
| 13.15 | a que l que p re ci pi te e re |
| 13.16 | so lu ti o n [M.] Gi o e qui e s t |
| 13.17 | e n Mo s co vi e [mande que sur les] |
| 13.18 | [representations qu'il luy a faites touchant] la r me |
| 13.19 | me n t de s {279 = Suédois} [il s'estoit declaré par] u n |
| 13.20 | se r me n t [qu'en cas que] la {Suède} a t |
| 13.21 | ta qua s t {le Roy} {67 = l'Empereur} o u {l'Electeur de Brandebourg} [il se] je |
| 13.22 | t te ro i t [d'abord avec toute] s se s |
| 13.23 | fo r ce s da n s la Li vo ni |
| 13.24 | e [a quoy peut estre il seroit assés facile de le] |
| 13.25 | [porter si] {les Estats Generaux} [vouloyent aussy contribuer de leur] |

## Reading

Il semble que la France et la Suède ne désespèrent pas tout à fait de regagner l'Electeur de Brandebourg du
moins, et il est certain que ces deux couronnes font traitter soubs main avec luy; de sorte que, les affaires
ayant changé de face en Alsace par la retraitte des alliés vers Strasbourg, il y [est] à craindre que si ledit
Electeur de Brandebourg remarque quelque froideur à l'assister, la jalousie et le mécontentement qu'il a
d'ailleurs des Impériaux ne le portent derechef à quelque précipitée résolution. M. Giøe, qui est en
Moscovie, mande que sur les représentations qu'il luy a faites touchant l'armement des Suédois, il [the Tsar]
s'estoit déclaré par un serment qu'en cas que la Suède attaquast le Roy, l'Empereur ou l'Electeur de
Brandebourg, il se jetteroit d'abord avec toutes ses forces dans la Livonie, à quoy peut-estre il seroit
assez facile de le porter si les Estats Généraux vouloyent aussy contribuer de leur costé.

(In English: France and Sweden have not given up hope of winning back the Elector of Brandenburg and are
negotiating with him in secret; after the allies' retreat in Alsace, any coolness in helping him might push
him, already jealous of the Imperials, into a rash decision. Giøe reports from Moscow that the Tsar has sworn
to throw all his forces into Livonia if Sweden attacks the King, the Emperor or the Elector, which the States
General could encourage.)

## Measure

- Cipher tokens: 205 (counted by `decode.py`; 162 in the clear line 13.25 is counted as a token).
- Tokens that give sense: 204 (99.5%). Not sense: 13.10 `8` (m), where "froideur" needs r (9): clear 8 on the
  page, kept as written.
- Values taken from context rather than key.tsv (also in `new_values.tsv`):
  - 31 = s (twice: "de-31-esperent", "pa-31") [the name range 25-276 elsewhere; here a filler for s].
  - 330 = ga here ("re-330-gner" = regagner); the sheet has 430 = ga; a 3/4 slip like 313 for 413 (9 Jan).
  - 279 = Suédois ("l'armement des 279"), as in the 9 Jan letter.
  - 67 = l'Empereur: "attaquast le Roy [25], 67 ou l'Electeur de Brandebourg [69]" confirms the sheet's
    "Kejseren?" over "Rigsfrau?".
  - 368 = di read with a doubtful last digit ("ledit").
  - Signs: `phi` for a hooked q-like sign ("regagner"), `q-` for the barred q ("Gioe"), `sq` = l.
