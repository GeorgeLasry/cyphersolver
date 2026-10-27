# Biermann to Just Høeg (The Hague), Copenhagen 6 February 1675: cipher passage

Source: Rigsarkivet, TKUA Almindelig del, Conrad Biermanns kopibog 1675 (S-1418), pp. 39-39v,
Arkivalieronline images 042 (heading at the foot of p. 39, right page; id 48573993) and 043 (cipher on p. 39v,
left page; id 48573994).
Key: TKUA "Chiffer" 1670-1709, image 55 (`key.tsv`). Transcription: `transcription_1675-02-06_hoeg.txt`;
decipherment by `decode.py` (verso-pattern copy).

Clear text before the cipher: Biermann could not write on Tuesday; he cannot yet answer about the Spanish
ratification, the Grand Chancellor having been busy all week dispatching Duke August of Holstein-Plön and
M. de Knesebeck, sent by the Elector of Brandenburg, and an Imperial courier on the same subject. "... vous
jugerez aisement que dans l'estat ou sont ..."

## Line by line

| line | decipherment |
|---|---|
| 39v.17 | [dans l'estat ou sont] e n co re s le |
| 39v.18 | s a f fa i re s à l' e s ga |
| 39v.19 | r d de Sa Majesté e l le ne s |
| 39v.20 | ca u ro i t e s t re que di |
| 39v.21 | la to i re [Sad.te Altesse et M. Kne-] |
| 39v.22 | [sebeck] o n t ne a n t mo i n |
| 39v.23 | s te s mo i g {517: ne} de pa r ti |
| 39v.24 | r {405 = fo} r t co n te n t s co |
| 39v.25 | m p re n na n t s a s se z que |
| 39v.26 | Sa Majesté ne pe u t pa s [encores] fa i |
| 39v.27 | re da va n ta ge [Je suis.] |

## Reading

... vous jugerez aisément que, dans l'estat où sont encores les affaires, à l'esgard de Sa Majesté elle [la
résolution] ne sçauroit estre que dilatoire. Sadite Altesse [the Duke] et M. Knesebeck ont néantmoins
tesmoigné de partir fort contents, comprenants assez que Sa Majesté ne peut pas encores faire davantage.

(In English: Given the state of affairs, the answer the Brandenburg and Imperial envoys took away could only be
a delaying one on the King's part; the Duke and Knesebeck nevertheless left well satisfied, understanding that
the King cannot yet do more.)

## Measure

- Cipher tokens: 103 (counted by `decode.py`, verso-pattern copy).
- Tokens that give sense: 102 (99.0%). Not sense: 39v.23 `517` (mi), clear on the page, where "tesmoigné"
  needs 537 (ne).
- Values taken from context rather than key.tsv (also in `new_values.tsv`):
  - 405 = fo ("partir 405-r-t contents" = fort); the sheet has 415 = fo.
  - `?ss` (a ß-like sign) = m ("co-?-prenants").
  - `?Xl` = r (twice: "esgard", "partir").
  - The 9-like hook after 577 X (39v.26) labelled q (t) from context ("peut").
