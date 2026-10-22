# Feynman cipher no. 2: decryption (copied from NOTES.md, "Independent decryption")

Copied verbatim from NOTES.md: the output of `decrypt.py` (two alternating alphabets, even-length words reversed,
Viterbi word segmentation). Solution first published by David Vierra, May 2023. Bracketed words garble where the
encoder broke his own alternation rule; note "ale is", not Housman's "ale's".

WHY IF TIS DANCING YOU WOULD BE THERE IS BRISKER PIPES THAN POETRY SAY FOR WHAT WERE HOP YARDS MEANT OR WHY
WAS BURTON BUILT [ON TRENT] OH MANY A PEER OF ENGLAND [BREWS] LIVELIER LIQUOR THAN THE MUSE AND MALT DOES MORE
THAN MILTON CAN TO JUSTIFY GODS WAYS TO MAN ALE MAN ALE IS THE STUFF TO DRINK FOR FELLOWS WHOM IT HURTS TO THINK

Check (`verify.py`, re-encryption of the plaintext): first 118 characters exact; 208/261 overall. The mismatch
regions decode directly to ENGLAND BREWS (both words under A2) and to "…MAN ALE MAN ALE… THE STUFF … DRINK FOR
FELLOWS WHOM IT HURTS TO THINK" (the encoder's wording of line 27 differs slightly from Housman's printed text).
