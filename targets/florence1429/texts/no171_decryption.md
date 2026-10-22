# ASF Dieci di Balìa, Responsive 2 no. 171 (DECODE R3754): final decipherment

Copied verbatim from `READING.md`, section "Re-decipherment with the extended key (24 Sept 2026; supersedes the cipher parts above)", which supersedes the earlier working readings in that file. The key is Gabbrielli's 1863 table extended from the glossed siblings (`key_extended.md`); the token list is `cipher171.tsv`.

## Re-decipherment with the extended key (24 Sept 2026; supersedes the cipher parts above)

Every cipher token of no. 171 was re-transcribed from 3x crops of the deskewed page (`strips/Y171_*.png`, main
checkout) and deciphered with `key_extended.md`. The token list with value, key source and grade is
`cipher171.tsv`; `python targets/florence1429/measure171.py` counts it.

**Measured:** 99 cipher tokens (letters, nulls and word signs; a nomenclator sign counts as one token). 97 have a
value (98.0%); 94 (94.9%) at grade H or M. Two tokens have no value (⊀ ψ in run L7e). By source: 72 values from
Gabbrielli's 1863 table as printed, 16 from signs whose value was recovered from the sibling glosses, 5 nomenclator
entries, 4 from context only (the null 4 in PAVOLO, ⊡ = il Papa?, the word sign E = ella?, the null ϡ).

| run | signs | decipherment | change from 18 Sept |
|---|---|---|---|
| L2a | Ᵽ 4 ∵ ♀ +o ÷ 8 | PAVOLO (Paolo), 4 a null | ♀ = V; "∵ — 8" is ÷ (L) + 8 (O), not nulls |
| L3a | ᴗ ·:' 6 ℘ ⊐ ∂ 7 E | DI MADONN(A) | none |
| L3b | ᴗ ⊓̍ ϙ ô ∵ ⊐ ·:' E ‡ | CINTADINI (Gabbrielli's spelling in the gloss) | ϙ = N, ⊓̍ = I (Gabbrielli's second I) |
| L3c | ɣρ | [il Conte d'Urbino] (Gabbrielli's ov; gloss "il conte") | the sign read "≠" is ɣρ, the word sign |
| L4a | ■ ⊡ | [null] [il Papa?] | ■ is the null ▼ of nos. 21 and 171 L11c, so one word sign, not two |
| L4b | q Ħ ⊢ +o 6 ∵ 7 ᴗ ·:' E q‡ | [null] ACOMANDINO | none |
| L4c | ℘ ÷ ∂ | A LO (then clear text) | the last sign is ∂ (O), not ⊓; "a lui" withdrawn |
| L7a | ɧ ∵ ᴗ ∂ 7 E ℘ | MADONNA | none |
| L7b | ♀ ϡ 99 ∧ ▽ | PURE, ϡ a null | the group read "∯" is 99 (U), Gabbrielli's sign |
| L7c | π ⊔ 6 ·:' 7 Ħ | FEMINA | none |
| L7d | ς | E | none |
| L7e | ⊀ ψ | ? ? | ⊀ is the open 4 (T in nos. 21, 91, 92), not Gabbrielli's O; unread |
| L7f | π +o 8̊ ♀ ⊔ ô +o ʓ Ħ | SOSPETOSA | 8̊ and ô are Gabbrielli's S and T; π = S and ʓ = S remain single-letter values |
| L9a | oɣ | [Conte d'Urbino] | none |
| L11a | ↑ | [fanti] | none |
| L11b | +o– | [Dieci] (gloss "dieci") | read as a word sign, not as the start of a run |
| L11c | 6 ∵ ᴗ +o 7 ▼ E Ħ | MADON[▼]NA | ▼ is a null |
| L12a | Ч ∵ Γ° ▽ 9 ll ⊓ | PARENTI | ▽ is Gabbrielli's E; 9 = N now shown in no. 21 |
| L12b | ᴗ ·:' ô ɤ ᴗ # 7 ⊓ | CITADINI | # = I here; # is L in no. 21 |
| L12c | E | [ella?] | none |
| L13a | ɣ | [il Conte] (gloss "il conte") | read as the Conte word sign |

### Continuous reading of no. 171 (clear text as re-transcribed 18 Sept; decipherment in CAPITALS; word signs in [ ])

Magnifici potenti Signori miei, io sono stato qui mostrato per lettera … di questa … fatto questa mia, sentito
PAVOLO, … non n'averavamo e parlato però di una cosa et dell'altra, che sterino insieme più … DI MADONN[A] et
CINTADINI e [il Conte] … ma prosetto(?) che non li pare che [il Papa?] si[a] …, ACOMANDINO A LO…; sono stati così
parecchi … parlare, ma parebbe fusse più utile che qualunque commissione portata persona fusse et motivare de'
ragionamenti, che disputa Giovanni [= i Dieci] mandasse trombetta [= ambasciatore], perché dice che MADONNA [è]
PURE FEMINA E [? ?] SOSPETOSA, pure vedrendosi(?) coperto, se sapesse a fare, sapere et bene; ma non staza così
coperto. Anno sospetto di questo [Conte d'Urbino], detto non credo bisogni, ma pure delle cose … avere sospetto;
o detto … el modo che li parebbe, farebbe dimostrare fare … [fanti] et guache(?); che [= cavalli] e segretamente
[Dieci] dessi loro opera che metassono, et segretamente MADONNA et PARENTI [e] CITADINI promettessono e
obligassensi che, non obstante [ella?] dicesse e volesse el contrario, dico essi farebbono quello volesse
[il Conte]. E ragionamenti furono assai e lunghi … ma parmi volesse andasse più segreta. Racomandomi alla Signoria
vostra. Vostro servidore Galeotto de Fibindacci [da Ricasoli].

What the extended key changed in the sense: "Paolo" is spelled PAVOLO; the Count appears three times as his word sign
(lines 3, 9, 13); the Dieci are named as the ones to engage the men secretly (line 11); the pair on line 4 is one
word sign after a null. Still open: ⊀ ψ before SOSPETOSA (two signs), and the values resting on context (⊡, E).
The clear text of lines 1-3, 8-10 and 13-14 is a first-pass palaeographic reading and has not been re-checked.
