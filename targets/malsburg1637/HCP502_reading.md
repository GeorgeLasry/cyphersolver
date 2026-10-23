# HCPortal 502 (HStAM 4 h Nr. 1411, f. 14), Malsburg to Landgrave Wilhelm V, Wesel, 16/26 Jan 1637 — reading of the cipher

Rests on: `f014.txt` (transcription agent, checked by Bourdeau) decoded with `key.txt` unchanged
(`research/reading_audit/b08_dec.py`), the breaks checked on the HCPortal original scan (hstam_4_h_1411_14, 2854 x
4200, fetched 22 Oct 2026 into the session scratchpad; batch b08). The right edge of the sheet is torn and folded: the
last group of many lines is partly or wholly lost (marked `?` in the transcription). No contemporary decipherment, no
clear copy, no edition. Code values: `{Cöln}` = 128, `{Regiment}` = 253 (grade I, `codes.txt`).

State (22 Oct 2026, batch b08): decoded, not read; clean-sentence share of the reading body 0.167 (before 0.143); holes: open codes and signs in nearly every sentence, torn edge. Log: `HCP496-509_reread_log.md`.

Conventions: `{...}` a code with a context value; `[145]` an unvalued code; `<+>` an unvalued sign; `[?word]` partly
carried; `[word]` supplied (here only letters lost at the torn edge); `[…]` unread. Spelling as the cipher gives it: the b08 normalisation (`research/reading_audit/b08_norm.py`) was undone on 23 Oct 2026 (batch r2b, `research/reading_audit/r2b_mals_denorm.py`: each word restored to the form its figures or the transcribed clear words give, e.g. alhir, Feint, schleinig, hette, dan, one); modern spelling only in the English file.
Punctuation added. ⟨...⟩ = clear words written in the letter around the cipher.

## Reading

⟨… erwarten,⟩ [?hoffe] aber doch noch am Ende dises Monats, wofern mir das Wette[r], der Weg ⟨und⟩ [145] newe Werbungen in [235] daran nit verhind[e]rlich sein, mich an bestimte Ort neben [XX] Hoffstat [?einzustellen].

⟨Den 15/25 huius⟩ ist die Proviandirung Hermansteins [?vorgenommen], ⟨und⟩ füret Obristl Hoffman das Volck, deme […]molbram, Captain Helwigsch mit vom Roten ⟨und⟩ Adria von Carpens [191] mitt <f> au man [193] neben <o> {Regiment}stucken mi[t]gegeben. Der [200] seint etwa <K> <4#> ⟨und⟩ <m> [?gewesen]; kommen i[n] [262] Tagen schwerlich dahin. Haben iren Weg […] Molheim über die [266] auf Siburg ⟨und⟩ <4#> die rechte Stra[ss]e von {Cöln} auf [189] genommen, ⟨und⟩ nit mer als <+> au casselisch[e] Virtel [210] bei sich.

⟨Jan de Wert ist in persona zu Cölln und hat sein Volck in den Stifft Münster gelegt;⟩ wirt ihnen one Zweiffel nachgehen. Wen das [?geschicht], so wirt Obristl Hoffman [?die Lohngerat] hin auf Marpurg ⟨und⟩ [215] oder Corbach, Brilen [138] ⟨und⟩ so wide[r] seine Garnison gehen. ⟨Gott gebe ihnen Glück,⟩ das es sowol als […] Hanau [?abgehe].

[SS] hat mit eigen Handen an seiner geheimbten Rahte [?geschrieben], ⟨dass sich nun recht alle Gemüter … zum Fürsten …⟩.

⟨… dazu dan⟩ er und sei[n] Her[r] [?Bruder] ⟨gute Beförderung thun wollen;⟩ ⟨welches alles⟩ auf die Unkosten nach [?Hermanstein] gehen. ⟨… sobald ich herfahre,⟩ wie es denen auf der […]e nach Hermanstein gehet, ⟨will ich … überschreiben.⟩

## Notes

- Letters in plain brackets are the values of groups lost or half lost at the torn right edge where one letter is
  certain from the word (Wette[r], verhind[e]rlich, mi[t]gegeben, i[n], Stra[ss]e, wide[r], sei[n]); a lost group that
  the word does not fix is `[…]`.
- "deme […]molbram": `27 61 56 48 3? / 57 93 15 76 97 55 42`; the last group of l. 12 is cut (a 30-group); no name
  "…molbram" is known to us, so the hole stays.
- `neben o 253 ST 47 80 92 61 83` = "neben o Regimentstucken": a small o with a point before the code, not a figure
  group; open.
- "gewesen": the figures give `ge a e sen` (28 = a, where a w-group is needed); partly carried.
- "die Lohngerat hin": `27 66 84 99 73 21 22 29 49 97 87 96 82 66 63` = dielohngerathin; the sense of "Lohngerat" is not
  clear to us.
- "abgehe": `55 7? 29 16 21 79` = a 7 gehe; the lone 7 (also in HCPortal 496) has no value in the key.
- "geschrieben": `… 18 / 49 63 54 16 X 66 61 …` = "w / enge schrieben"; the writer seems to have begun a word at the line
  end; the participle is carried, the w-group is not.
- "Bruder": `21 48 65 10 46 24 46 61 25` = her b d u d e r; "Herr Bruder" with d for r once; partly carried.
- "Hermanstein" in block 4: `82 84 25 42 39 63 M Y ?` = herman + mm-sign + ei + cut group; the mm-sign stands where st
  is needed.
