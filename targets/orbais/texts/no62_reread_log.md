# Re-reading log, BnF fr. 3413 no. 62 (23 Oct 2026, Claude Opus 5.5; REREAD_BRIEF, batch b31)

## Starting point

Reading audit (22 Oct): "decoded, not read": `no62_decryption.md` was one line per cipher group; the letter's clear
text had never been transcribed, so the runs stood as isolated words.

## 1. Is there a text already?

No contemporary decipherment, copy or edition (NOTES: Tomokiyo's cryptiana nevers.htm discusses it; fr. 3612, his
key source, is not digitised). The letter is not a DECODE record. Every page of the letter was opened at full
resolution (Gallica `btv1b52510705j` views 259-262 through openapi.bnf.fr IIIF, `research/reading_audit/b29_gallica.py`;
scratchpad `reread/orbais/`): ff. 126r, 126v, 127r written, f. 127v the address *A Monsieur / Monsieur l'Abbé d'Orbais
Con.er au Conseil estably a Paris pour la S.te Union / A Paris* with nothing else but bleed-through of f. 127r (no hidden
cipher on the verso).

## 2. Read on the image

The clear text of ff. 126r-127r transcribed line by line from 1700-px strip crops (`b31_crop.py`), and the fourteen
cipher runs set in place (the signature *Baron* stands on f. 126v, last line, before *presente ses treshumbles
recommandations* on f. 127r). No transcription label of `no62_cipher.txt` changed; no key change.

Tried again on C and V2 with the clear context now complete (*pour ce qui touche [C]*; *maintenant que vous serez à
vostre [V2] si l'histoire est vraye*): with æ = e fixed by S1b and I, C gives v-o-?-a-e-?-s and V2 et-f-e-g-r-e; no
word fits both the values and the clause (*vos amis*, *vos pays*, *abbaye*, *Champaigne* each need two or more values
against the key). Still unread.

## 3. Alignment

Every word of the reading is either clear text on the page or the reading of a cipher run in `no62_decryption.md`;
the cipher words were aligned with their sign groups (Notes of the reading). Supplied words: none. **Look-alike
letters: 0** (every cipher letter rests on its sign's own value as transcribed; the ⊡/◻, ħ/H, ⋕/tt distinctions were
settled on the image on 22 Sept and 5 Oct and are distinct signs, not alternates).

## 4. Scores

| | clean-sentence share |
|---|---|
| before | no reading body (group list) |
| b17 plain (`LANG_=fr`) | **0.882 (45/51)**, hole rate 0.038 |
| b17 `HOLES=1` | 1.0 (51/51) |
| cipher-bearing sentences only (by hand) | 6/7: only *[Ƃ] depeschera [ʃ] dedans deux jours le doien* has two holes in eight words |

Reader's judgement: the letter reads as connected French prose throughout; the holes are two short runs (C, V2) and
three single code signs.

## Open

- `Ƃ`, `ʃ` (S1), `τ` (G): single code signs, no value in any reachable key - blocker no-key-material.
- C, V2: values missing from Tomokiyo's partial table; fr. 3612 not digitised - blocker no-key-material. A full
  sign-by-sign transcription of fr. 4715 f. 2 (lines 7, 9-11, 13, 16, 18, 21-29) might supply some of them
  (not-attempted).
