# Key used: Johnston to Seddon, 16 June 1863

- System: Vigenere with the standard tabula recta (cipher = plain + key, A = 0).
- Key: MANCHESTERBLUFF (15 letters), one of the keys known from other Confederate messages
  (with COMPLETEVICTORY and COMERETRIBUTION).
- Only the cipher words are enciphered. The key runs on from word to word and is not restarted.
  It advances by the length of each plaintext word.

| plaintext | key letters | expected | written |
|---|---|---|---|
| INVADE | MANCHE | UNICKI | UNIEK |
| KENTUCKY | STERBLUF | CXRKVNED | CXNKVNED |
| EXTEND | FMANCH | JJTRPK | JJTRRK |
| EAST | ESTE | ISLX | ISLX |
| TENNESSEE | RBLUFFMAN | KFYHJXEER | KFYHJEER |

## Encipherment slips on the leaf

- Key letter C applied as E, at both places where C falls (INVADE 4th letter, EXTEND 5th letter). Probably the
  clerk's copy of the key, or his reading of it, had E for C.
- KENTUCKY: the 3rd letter N was written in plain (the key letter E gives R).
- INVADE: the last letter is not written. TENNESSEE: one S (cipher X) is left out.

The key was not reconstructed here from the cipher alone. It was found by testing the known Confederate keys against
the crib on image 3. Cipher minus crib gives the key stream MANEH STARBLUF FMANEH ESTE RBLUFMAN without assuming the
key (check.py, section 2), and this is MANCHESTERBLUFF with the slips above.
