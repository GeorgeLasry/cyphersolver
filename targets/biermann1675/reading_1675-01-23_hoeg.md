# Biermann to Just Høeg (The Hague), Copenhagen 23 January 1675: cipher passage

Source: Rigsarkivet, TKUA Almindelig del, Conrad Biermanns kopibog 1675 (S-1418), pp. 24v-25,
Arkivalieronline image 028 (id 48573979; heading and cipher on p. 24v, left page; end on p. 25, right page).
Key: TKUA "Chiffer" 1670-1709, image 55 (`key.tsv`). Transcription: `transcription_1675-01-23_hoeg.txt`;
decipherment by `decode.py` (verso-pattern copy).

## Line by line

| line | decipherment |
|---|---|
| 24v.12 | [... sinon qu'il faudra attendre] l' e f {313: fe} c t de ce |
| 24v.13 | que {180} vo u s a di t [et qu'il] |
| 24v.14 | [auroit esté a souhaitter que l'on eust] fa i t |
| 24v.15 | p lu s de re f le {6: x} i o n a |
| 24v.16 | u li e u o u vo u s e s te |
| 24v.17 | s [sur] le s c ho se s que vo |
| 24v.18 | u s y a ve z re p re se n |
| 24v.19 | te e s [il y a quelque temps] po u r p |
| 24v.20 | re ve ni r ce t a c ci de |
| 24v.21 | n t [mais a chose faite conseil est pris et] sa |
| 24v.22 | Majesté ne la i s se pa s de co |
| 24v.23 | n ti nu e r da n s se s bo |
| 25.01 | n ne s i n te n ti o n s po |
| 25.02 | u r le pu b li c [Le Duc Auguste de Plön vient ...] |

## Reading

Bienque la lettre que vous avez escritte à Monseigneur le Grand Chancellier le 21/11 de ce mois contienne un
avis fort important, je n'ay pu néantmoins répondre autre chose sinon qu'il faudra attendre l'effect de ce que
[180] vous a dit; et qu'il auroit esté à souhaitter que l'on eust fait plus de réflexion au lieu où vous estes
sur les choses que vous y avez représentées il y a quelque temps pour prévenir cet accident; mais à chose
faite conseil est pris, et Sa Majesté ne laisse pas de continuer dans ses bonnes intentions pour le public.

(In English: Biermann can only answer Høeg's important report by waiting to see what comes of what [180] told
him; The Hague should have paid more attention to Høeg's earlier warnings meant to prevent this mishap, but
what is done is done, and the King keeps his good intentions for the common cause.)

## Measure

- Cipher tokens: 122 (counted by `decode.py`, verso-pattern copy).
- Tokens that give sense: 120 (98.4%). Not sense: 24v.13 `180` (a name, not on the key sheet; "ce que 180
  vous a dit"); 24v.15 `6` (the digit 6 = q on the sheet, where "réflexion" needs x).
- Values taken from context rather than key.tsv: 313 = fe ("l'ef-313-ct"), as in the 9 Jan letter (the sheet
  and the 19 Jan letter have 313 = be). See `new_values.tsv`.
