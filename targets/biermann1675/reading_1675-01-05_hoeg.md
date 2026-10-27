# Biermann to Just Høeg (The Hague), Copenhagen 5 January 1675: cipher passage

Source: Rigsarkivet, TKUA Almindelig del, Conrad Biermanns kopibog 1675 (S-1418), pp. 4-4v,
Arkivalieronline images 007 (heading at the foot of p. 4, right page; id 48573958) and 008 (cipher on p. 4v,
left page; id 48573959).
Key: TKUA "Chiffer" 1670-1709, image 55 (`key.tsv`). Transcription: `transcription_1675-01-05_hoeg.txt`.
NB `decode.py` matches only labels of the form p<digits>.<line>; for the verso labels (p4v.03) it was run
through a copy with the pattern widened to `p\d+v?\.\d+` (no other change).

Clear text before the cipher: Biermann has barely time to acknowledge Høeg's packets of 31 December and
4 and 7 January, "et pour vous dire quand a la ratification d'Espagne que comme ..."

## Line by line

| line | decipherment |
|---|---|
| 4v.03 | [tion d'Espagne que comme] le c ha n ge |
| 4v.04 | me n t a r ri ve da n s le s |
| 4v.05 | a f fa i re s pa r [l'entrée des Suedois] |
| 4v.06 | [dans les Estats de M. l'Electeur de Brandenbourg] re |
| 4v.07 | n d la mi ti e de sa Majesté p lu |
| 4v.08 | s ne ce s sa i re [qu'auparavant] a |
| 4v.09 | u x a l li e z i l fa u d |
| 4v.10 | ra le s vo i r ve [mo = ni?] r [et] te s |
| 4v.11 | mo i g ne r mo i n s de m p |
| 4v.12 | re s se me n t [en toutes choses que peut] |
| 4v.13 | [estre on n'auroit fait sans cela, bien qu'asseurement] |
| 4v.14 | la co n du i te de {Spanien} [a l'esgard] |
| 4v.15 | [de lad.te ratification est asses] e x t ra o |
| 4v.16 | r di na i re [veu qu'elle] po u vo |
| 4v.17 | i t [bien] p re vo i r que la la |
| 4v.18 | n gu e e s pa g no le s |
| 4v.19 | [n'estant pas] s ce u e [376 = de?] [beaucoup de] pe |
| 4v.20 | r so n ne s [et ainsy ne pouvant estre asses] |
| 4v.21 | [bien] e n te n du e [pour cognoistre si] la |
| 4v.22 | t ra du c ti o n sa c co r de |
| 4v.23 | a ve c l' o ri gi na l [on ne pouvoit manquer de faire difficulté de l'accepter.] |

## Reading

... et pour vous dire quand à la ratification d'Espagne, que comme le changement arrivé dans les affaires
par l'entrée des Suédois dans les Estats de M. l'Electeur de Brandenbourg rend l'amitié de Sa Majesté plus
nécessaire qu'auparavant aux aliez, il faudra les voir ve[ni]r [?] et tesmoigner moins d'empressement en
toutes choses que peut-estre on n'auroit fait sans cela, bien qu'asseurement la conduite de l'Espagne à
l'esgard de ladite ratification est assez extraordinaire, veu qu'elle pouvoit bien prévoir que la langue
espagnole n'estant pas sceue de [?] beaucoup de personnes, et ainsi ne pouvant estre assez bien entendue
pour cognoistre si la traduction s'accorde avec l'original, on ne pouvoit manquer de faire difficulté de
l'accepter.

(In English: Since the Swedish entry into Brandenburg makes the King's friendship more necessary to the
allies than before, Denmark should let them come and show less eagerness in everything than it might
otherwise have done. Spain's handling of the ratification is nonetheless odd: it should have foreseen that,
Spanish being understood by few here and the translation impossible to check against the original, the
text was bound to meet objections.)

## Measure

- Cipher tokens: 165 (counted by `decode.py`, verso-pattern copy).
- Tokens that give sense: 164 (99.4%). Not sense: 4v.10 `518` (mo), where "voir venir" needs 538 (ni);
  the 518 is clear on the page and is kept as written (scribal slip, likely).
- Sign identified by shape after comparison with the 9 Jan letter: the cross with one bar and a curled top
  (4v.09, 4v.15) is set1 X (b-, ƀ) = x, as in 'ceux' on p. 9v; it reads 'aux aliez', 'extraordinaire'.
- Values taken from context rather than the key sheet:
  - `?Xl` (an X with a looped top, 4v.17) = r: "prevoir". Distinct from the plain X (u) on the same page.
  - `376` (4v.19) = de: "sceue de beaucoup de personnes"; not on the key sheet (367 = de there): a
    transposition of 367, or an unrecorded homophone.
  - `a` (4v.11), written like a 6/delta, taken as set1 M (alpha) = m: "d'empressement".
