# Biermann to Just Høeg (The Hague), Copenhagen 26 January 1675: cipher passage

Source: Rigsarkivet, TKUA Almindelig del, Conrad Biermanns kopibog 1675 (S-1418), pp. 31v-32,
Arkivalieronline image 035 (id 48573986; heading and cipher on p. 31v, left page; end on p. 32, right page).
Key: TKUA "Chiffer" 1670-1709, image 55 (`key.tsv`). Transcription: `transcription_1675-01-26_hoeg.txt`;
decipherment by `decode.py` (verso-pattern copy).

## Line by line

| line | decipherment |
|---|---|
| 31v.11 | [... tant que les choses demeureront dans cet Estat et que l'on] ne ve r |
| 31v.12 | ra po i n t d' a u t re s e {?Xl: f?} |
| 31v.13 | {313: fe} c t s de la re so lu ti o |
| 31v.14 | {26 = n} que {163} o n t p ri se i l |
| 31v.15 | fa u t d' a u t re s c ho |
| 31v.16 | se s que de s pa ro le s da |
| 31v.17 | n s u ne co n ju n c tu re |
| 31v.18 | co m me ce l le c y [ou] Sa |
| 31v.19 | Majesté pe u t a vo i r de s a |
| 31v.20 | va n ta ge s si co n si de |
| 31v.21 | ra b le s d' a i l le u r s |
| 31v.22 | [Lesquels Elle] n' a pa s vo u lu a c |
| 31v.23 | ce p te r [jusques icy] pa r u n pu |
| 31v.24 | {th: r} mo u ve me n t de gé {485 = ne} ro si |
| 31v.25 | té [et] d' i n c li na ti o n |
| 32.01 | po u r l' i n te r e t de {les Estats Generaux} [et] |
| 32.02 | de le u r s a l li e z [Sa Majesté en consideration de M. le Lieutenant Admiral de Ruyter ...] |

## Reading

Bienque vostre Relation du 25/15 de ce mois, qui a esté leüe aujourd'huy à Sa Majesté, contienne plusieurs
[choses] considérables, vous jugerez néantmoins aisément qu'on n'y peut rien répondre tant que les choses
demeureront dans cet estat et que l'on ne verra point d'autres effects de la résolution que [163] ont
prise. Il faut d'autres choses que des paroles dans une conjoncture comme celle-cy, où Sa Majesté peut
avoir des avantages si considérables d'ailleurs, lesquels Elle n'a pas voulu accepter jusques icy par un pur
mouvement de générosité et d'inclination pour l'interest des Estats Généraux et de leurs alliez.

(In English: Nothing can be answered while matters stand still and the resolution taken by [163] has no other
effect; words are not enough at a time when the King could have considerable advantages elsewhere, which he
has refused so far out of generosity and goodwill towards the States General and their allies.)

## Measure

- Cipher tokens: 169 (counted by `decode.py`, verso-pattern copy).
- Tokens that give sense: 166 (98.2%). Not sense: 31v.12 `?Xl` (read r in nine places elsewhere; here
  "effects" wants f); 31v.14 `163` (not on the key sheet; the plural subject of "ont prise", perhaps the
  States of Holland or the allies); 31v.24 `th`
  (i, where "pur" wants r). The last is clear on the page and kept as written. The 9-like hook in 31v.19 ("peut") is labelled q (t) from context.
- Values taken from context rather than key.tsv (also in `new_values.tsv`):
  - 485 = ne ("gé-485-rosité").
  - 26 = n ("résolutio-26"; confirmed by "dans u-26 pareil cas" in the 9 Feb letter).
  - 313 = fe ("ef-313-cts"), as in the 9 and 23 Jan letters.
  - `?Cn` (a C with a hook inside) = c (twice: "effects", "conjoncture").
  - `?Xl` = r once (31v.23 "par"), `cf` = u (32.02 "leurs").
