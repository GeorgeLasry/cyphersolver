# HCPortal 497 (HStAM 4 h Nr. 1411, ff. 12-13), Malsburg to Landgrave Wilhelm V, Wesel, 7/17 Jan 1637 — reading of the numerical cipher

Rests on: `f012.txt` (Bourdeau's transcription of scan 0012, one cipher line per scan line; f. 13 is the address side,
no cipher) decoded with `key.txt` unchanged (`research/reading_audit/b08_dec.py`), the breaks checked on the HCPortal
original scan hstam_4_h_1411_0012 (2834 x 4284, fetched 23 Oct 2026 into the session scratchpad; batch r2b, log
`HCP497-506_reread_log.md`). No contemporary decipherment on the leaf or the address side, no clear copy, no edition
(NOTES, Escalation). The separate ten-line letter-cipher block at the foot of the page is another system and has its
own entry (`alphabetic/`). Code values: `{Cöln}` = 128, `{Hamburg}` = 130, `{Regiment}` = 253, `{die Staaten}` = 188
(grade I, from context, `codes.txt`).

Conventions: `{...}` a code with a context value; `[148]` an unvalued code; `<XX>` an unvalued sign; `[?word]` partly
carried; `[x]` a letter or word no figure carries; `[…]` unread. Spelling as the cipher gives it (u/v, i/j merged by the
key); nouns capitalised and punctuation added. ⟨...⟩ = clear words written in the letter around the cipher. The plain H
sign stands for ll (anstellen, alleine, soll er) and, as in the sibling letters, for tt (Mittel, mit-); it is read so
where only tt gives the word.

## Reading

⟨… so lang als möglich mainteniren werden,⟩ ich weis nun nicht, wie ich [?den] Weg anstellen [?soll], ⟨und⟩ ob <H#> noch in [148] oder bei der Armee sein [?…], eine Reisse noch vor sich gehen solte ⟨und⟩ <XX> meine Abfertigun[?g] [259] oder [258] schicken konten oder wolten; wurde ville Zeit [?…] ⟨das was ich …⟩

⟨… und H. Stadthalter annoch nicht wieder kommen,⟩ dass ich die Recrute ⟨und⟩ Vererungsgelder vor Dalwigs ⟨und⟩ Ebersteins {Regiment}, wie auch d[?ie] [?Leibguarde] mitnemen kan, ⟨als will ich bey des Herrn … abgeschickten botten⟩ und [?…] oder bei Zeigern {die Staaten} Ordre meines w[ei]tern Verhaltens, ob ich <6> alleine zu [129] zu kosten Mittel suchen oder <XX> alhir gelassen Train mitt bringen soll, erst erwarten; dan durch Friesslant mitt Wagen ⟨und⟩ Pferden zu gehen ist unmoglich. ⟨Wolten auch EfGl. bei …⟩

Es ist von guter Hant avisiret, dass man zu Regenspurg geschlossen, <H#> Gesanten nach {Cöln} keinen salvum conductum zu erteilen. [?Hiergegen] berichtet mich der Statthalter Nesselrot, dass der Bischoff von Wirzburg an ihn im Augustto geschriben, wen [129] beim Konig von Bomen, nunmer aber dem Romischen Konige, einkemen, diselben noch woll einen guten Friden erhalten solten. Mitt der [140] wurde man durch [137] apart zu {Hamburg} oder Lubeck tracti[r]en lassen. ⟨Es ist in den Spanischen guarnisonen …⟩

## Notes

- Block 1 follows the clear words "… so lang als möglich mainteniren werden,"; block 2 follows "… und H. Stadthalter
  annoch nicht wieder kommen,"; block 3 stands under the date "Datum Wesel den 7/17 Januarij Ao 1637" and before the
  signature flourish.
- "den Weg anstellen soll": the figures give `16 63 98 84 54 …` = en weg (no d-group at the head of the line) and
  `35 N` = so-ch at the end; read on the scan as written, so both words are partly carried.
- "sein [?…], eine Reisse": `… 68 G 83 37 48 | G 83 49 30 Y P 61` = s ei n w e | ei n e r ei ss e. "w e" gives no
  word before "eine Reisse"; left open.
- "Abfertigun[?g]": the last group of the line is a doubtful "5?" where a g-group is needed.
- "wurde ville Zeit [?…]": `29 49 18 | 84 83` = g e w | e n, then the clear text; no word ("gewinnen" would need
  more groups).
- "d[?ie] [?Leibguarde]": `27 9? | Y 10 34 71 39 97 27 84` = d 9 | ei b g u a r d e; the 9 is doubtful and no l-group
  stands before "eib".
- "und [?…] oder bei Zeigern": `71 83 27 94 70 42 7?` = u n d t a m 7; after "und" no word.
- "w[ei]tern Verhaltens, ob ich": `37 L 94 16 97 83` = w tt t e r n; `… 74 35 76 66 D` = s o b i ch (the s closes
  "Verhaltens"). `6?` before "alleine" is an unexplained figure.
- "Hiergegen": `82 16 25 66 | 49 43 48 63` = h e r i | e g e n.
- "diselben": the e is the figure 16 written above the line ("dis{16}lben").
- "tracti[r]en": `… 80 60 66 63 49 83` = c t i n e n; the scan (block 3, last line) shows 63 (n) where an r-group is
  needed, so the r is bracketed.
- "Mitt der [140]": `42 66 H 46 49 97` = m i <H> d e r; the scan shows the crossed H, read tt here.
