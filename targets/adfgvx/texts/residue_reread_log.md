# Re-reading log, the residue entry (23 Oct 2026, Claude Opus 5.5; REREAD_BRIEF, batch b24)

Entry: `outcome.texts` residue22, "decoded, not read": p. 164 F-G-X, p. 164 VFGAG, VGADA p. 215 (partial in 2017) and
ten messages with no reading (pp. 73, 152, 153 VFVAX, 153 AXVAA, 158, 170, 176 GGDAA, 189, 198, 217).

## 1. Is there a text already?

- Web search for readings after 2017: a decipherment of a 27 Nov 1918 message of about 170 letters was posted by
  "prinz" on 17 Sept 2026 and reported by The Neuron (18 Sept 2026) and news sites, credited to an AI model:
  keyword TRUPPENVERSCHIEBUNG (a key Childs gives on pp. 214-215 for use from 9 Dec), plaintext "EIN ENGLISCHER KREUZER
  EINLIEG X SEWASTOPOL X S4STEN X EIN GESCHWADER DER X ALLIIERTEN FOLGT 26STEN X". Childs p. 217 is the residue
  message of 170 letters. Not reproduced by others in the reports.
- The 2017 Cipherbrain thread (`research/top50/arts/46_comments.txt`) re-read for the partials: Baertl (comment 39)
  gives a full corrected VGADA text ("ABS X MIDIV 5 X EILMELDG X 24N X 24N X ARMADA KERTSCH X BRINGT ENTENTE FLOTTE ZWO
  DIVISIONEN X NEUSEELAENDER X ENGL X U X FRANZO X MIT X NUR OHL X KORPS FRISCH X 3Y52"), shortened to "..." in this
  file before; Norbert (comments 32, 42-47) gives his edits and the p. 164 fragments.

## 2. Checked on the figures

**p. 217 — read.** `research/reading_audit/b24_adfgvx_217.py` (output `p217_b24_check.txt`): the columnar
transposition by TRUPPENVERSCHIEBUNG turns the 170 received letters into 85 ADFGVX pairs; the 85 plaintext letters map
onto them one to one (23 distinct pairs, 23 distinct letters; no pair carries two letters and no letter two pairs). A
wrong plaintext or a wrong transposition would break that at once. The recovered cells sit in a keyword-shaped square
(row A: T R U P E 4; row D: N · S C 2 H). Both readings of the key numbers give the same result. Reading
`p217_reading.md` (X rendered as punctuation, letter-for-letter line in the notes), English `p217_en.md`. Body score
(LANG_=de) 0.50 (1/2; "einlieg", "sewastopol" not in the word list), explicit holes 1.00. Every letter carried by
its pair; look-alike count: none (the ADFGVX letters are not ambiguous in the transcription).
The same transposition with the 23 cells, applied to the nine other open messages, gives noise (0.52-0.76 of pairs
known, no words).

**VGADA p. 215 — stays partial.** `b24_adfgvx_vgada.py` (output `vgada_b24_alignment.txt`): Norbert's two inserted
five-letter groups (after the gap group 6 and after group 43) with the Nov 22-24 key reproduce his raw decrypt
letter for letter. Against Baertl's text: 97 of 129 letters carried by both cells, 11 by one cell (Baertl's letter
among the six allowed), 1 by none; 20 of Baertl's letters contradict the received cells, and only 5 of those 20 are
explicable as one-cell transmission errors. "S4N" (twice), which Baertl makes "24N", is what the cells give, and
p. 217 writes a date "S4STEN" the same way. Partial reading `vgada_partial_reading.md` with Baertl's emended words as
`[?word]`: 14 of 30 words, 0.00 clean. Before that, a blind residual search (gaps.py anneal, the three length-22 keys,
two free edits, 6 restarts) gave noise: the insertions at the marked places are what make it decrypt.

**p. 164 F-G-X and VFGAG — not retried.** 44 marked lost letters each (and, per Norbert, a whole line missing from the
transcript of the first): about every other plaintext letter has one or no cell, so Norbert's fragments ("TEMESVAR",
"MIRCO NACH WESTEN UND SUEDEN WEG", "SONST KEINE EREIGNISSE VON BEDEUTUNG") are what the cells allow.

## Result

| message | before | after | rests on / blocker |
|---|---|---|---|
| p. 217 | open, no reading | read, 0.50 clean (1/2), explicit holes 1.00 | 2026 decipherment checked as known plaintext (one-to-one, 85 pairs) |
| VGADA p. 215 | partial | partial, 0.00 (Baertl's text is part emendation) | needs-physical-access: the transmission gaps; Childs's book pages |
| p. 164 x2 | partial | unchanged | needs-physical-access: 44 lost letters each, a line missing from the transcript |
| nine others | open | open | no-key-material: no known key fits, incl. the p. 217 key |

fraction_read 0.49 → 0.533 (2,115 of 3,966 letters). Credit for p. 217 belongs to "prinz" (not yet in
contributors.json; not added here).
