# R1139 — Giuliano Caprile to Alfonso I d'Este, Eger, 6 April 1521: the cipher postscript slip (ASMo, Ambasciatori, Ungheria b. 4/28 no. 13) — partial reading

Status: partial reading; the document stays *decoded, not read* (clean-sentence share of this body 0.18 on
`_check_reading.py`, 2 of 11 sentences; 0.45 counting only the explicit holes; see `R1139_reread_log.md`).

Rests on: the figures only. No contemporary decipherment, gloss or clear copy exists (DECODE R1139 has three page
images and no attachment; the 20th-century MTA copies of the file leave the cipher out; Somogyi 2025 prints only the
16 Feb 1521 postscript). The ten cipher lines of the slip (IMG_R1139_I5752_P2) were re-read on quarter-line strips
at 2.2x of the native image, labels corrected (`R1139_corrections.tsv`, corrected file `R1139_transcription_b18.txt`),
and decoded with key21 (`beam21.py` priors; per-sign output from `research/reading_audit/b18_caprile_beam.py`). Every
word below was checked against the signs in `R1139_reread_log.md` (alignment table there). The covering letter (P1,
clear, "Ex Agria 6 aprilis 1521") and the clear end of the slip ("Expettarò sino a S. Georgio se venisse messo o
commissio de V. Ex.a, poi mi aviarò verso Italia ...") are not part of the reading body.
Marks: [?word] partly carried, [word] supplied, […] unread, [4817] [17] figures with no key value (codes).

## Reading

Post. Il custode, quando a Buda, com[?e] i' scrisi, et è tornato gubernator de [4817]. […] decime, et fa ogni
cosa per […] io [17] […]; a si tenuto Agria in oficio. [?E] credo dia ogni [?ato] e qualche cosa a le ma […] custode;
per anchora si n'è intrato [?ci] in castelo. Et cosi la venuta sua in Italia, [?a] de che vi scrivi, qua[…] li teneva
per ferma, è andata in [?vero]. Il che vedendo io, bel belo li go fato moto deli danari del suo debito, come mi dise
meser [?a] Alfonso. Lui m'ha resposto, dice [?te] voler andar in Italia quando al dare te […]. […] Milan […] andiate.
Parlaremo a longo sopra ciò, et se i bisionran danari in [?presto], per andar ve ne darò. Vedrò quel mi darà, [?e]
il tut[o] reportarò a V. Ex.

## Notes on the figures

- "quando a Buda": Z+ T DIV r QB | UT o o a PSI q — the o o pair is b (key, as in "debito", "bel belo").
- "com[?e] i' scrisi": z 4 o B m+ PHI x RC n+ L — the sign 4 has no key value; e is what the word needs. 4 also stands
  in "de 4 8 1 7" (L01 end) and before "credo" (L02 end), where e does not make a word in the first case, so 4 = e is
  not adopted.
- "et è tornato gubernator": K ss | h oSLo AST p q f CE | w a o o y x DIV T h CE AST (K = et, as in V1921).
- "[4817]" (L01 end) and "[17]" (L02): written as the figures 4 8 1 7 and 1 7; tested as letters and as numerals in
  pass 5 (3 Oct 2026), nothing fits; left as codes.
- "et fa ogni cosa": K f UT | oSLo w DIV L | PHI QB m+ q — f = f here (f has both t and f in key21_counts: t 14, f 3).
- "a si tenuto Agria in oficio": UT n+ RC | f y DIV LAM h e | q w AST L q | L p | QB AMP RC TH b oSLo.
- "si n'è intrato": p+ B | DIV y | B p h x T f oSLo — p+ (crossed p, the only one in the letter) given s by the
  sense; "[?ci]" is PHI RC before DIV ("c i n castelo"), one i for "ci in".
- "Et cosi": Z K (3 K) = et; "la venuta sua in Italia": ff T | LAM y DIV o h UT | n+ LAM p | B DIV | RC f T n B q.
- "[?a] de che vi scrivi": q+ (q with a stroke through the stem, the only one) r y | PHI o y | LAM B | m+ PHI x RC o.
- "per ferma": EL ss AST (the looped sign after "teneva" is EL, not CE: corrected) | f y x HH T.
- "in [?vero]": B p | 1 ss x oSLo — 1 (a minim) taken as v here only; not adopted as a key value.
- "bel belo": o o ss n | D y A CE — o o = b, D = b (key), n = l, A = l: "bel bello", gently.
- "li go fato moto": ff L | w oSLo | f q QB | QB HH CE h oSLo — QB = t in "fato" (QB has t 4 in key21_counts).
- "come mi dise meser [?a] Alfonso": TH CE z y | HH B | PSI RC o t ss | z y n+ ss AST | 8 q q ff AMP o oSLo DIV m QB — the
  isolated cross t = s (key21_counts s 5); one q (a) more than "meser Alfonso" needs.
- "quando al dare te": x o a q DIV r CE | UT ff | PSI q x y | f ss; then q+ PHI o 1 1 (two minims) unread.
- "et se i bisionran danari": K m+ ss | o RC | o o B n+ B CE DIV | AST T DIV | PSI UT p q x RC — "bisionran" as the figures
  spell it (bisogneranno).
- "in [?presto]": B DIV | CE AST y n+ f CE — CE for p is off the key (CE = o, 72 times); the sense wants presto.
- "il tut[o] reportarò a V. Ex.": c B ff | h LAM QB | x y EL oSLo f q x CE | UT | a CE Z — the final o of "tuto" is not
  written; "V. Ex." is a CE Z (u e x).
