# HCPortal 507 (HStAM 4 h Nr. 1411, ff. 28-29), Malsburg to Landgrave Wilhelm V, 28 Mar 1637 (old style) — reading of the cipher

Rests on: `f028.txt` and `f029.txt` (transcription agents, checked by Bourdeau) decoded with `key.txt` unchanged
(`research/reading_audit/b08_dec.py`), read against the writer's own "Duplicat" of the letter, ff. 30-31 (HCPortal
508, `f030.txt`, `f031.txt`), which was enciphered separately with the same key and line breaks of its own; where the
two copies differ the reading follows the copy whose figures give a word (`HCP507_corrections.tsv`). Breaks looked at
on the HCPortal original scans (hstam_4_h_1411_0028-0031; fetched 22 Oct 2026 into the session scratchpad; batch b08).
No contemporary decipherment, no clear copy, no edition. Code values: `{Compagnien}` = 273, `{Regiment}` = 253,
`{die Staaten}` = 188 (grade I, `codes.txt`).

State (22 Oct 2026, batch b08): decoded, not read; clean-sentence share of the reading body 0.437 (before 0.271); holes: open codes and signs, place names outside the word list. Log: `HCP496-509_reread_log.md`. 23 Oct 2026 (batch r2k): read (B) on the German explicit-hole measure, 0.662 (47/71), after a reader's review on the decode and scan 0028 (log `HCP507-509_reread_log.md`); one word re-spelt from the figures (nitt).

Conventions: `{...}` a code with a context value; `[193]` an unvalued code; `<V>` an unvalued sign (V = the triangle);
`[?word]` partly carried; `[word]` supplied; `[…]` unread. Spelling as the cipher gives it: the b08 normalisation (`research/reading_audit/b08_norm.py`) was undone on 23 Oct 2026 (batch r2b, `research/reading_audit/r2b_mals_denorm.py`: each word restored to the form its figures or the transcribed clear words give, e.g. alhir, Feint, schleinig, hette, dan, one); modern spelling only in the English file. punctuation added; the
writer's own parentheses (/: … :/) kept as ( ). Bare figures (6, 1, 2, 3) are written in the cipher as figures.
⟨...⟩ = clear words written in the letter around the cipher.

## Reading

⟨Ich bin gestern abent … wieder glücklich angelangt und habe E. F. G. gnädiges Schreiben … dort mich funden,⟩ wolte mich nun zwar wohl sobalt mit <H#> Train von hier [?aufmachen] ⟨und⟩ zu Land, weil Dunkercker vor etlich Tagen auf den Watten annoch gelegen, durch [235] an bestimmten Ort mit Gottes Hülffe anlangen. Weil ich aber [193] [212] Stück ⟨und⟩ [197] mit bringen so <V>, der Feit aber (welcher noch zwischen [149] ⟨und⟩ Ruhr an die 6 {Compagnien} [193] <e> <n> {Compagnien} [200] ⟨und⟩ 1 {Compagnien} Tragons [?ligen] hat, auch noch <K> {Regiment} [212] auss Lottringen etwa <4#> [?Pferde] starck dazukommen) itzo zusammengehett ⟨und⟩ zu Felt will, so ist uberlant zu gehen nit tunlich; zu Wasser aber langweilig, ⟨und⟩ kan so schleinig nit zu Werck gerichtet werden, damm es erfordert viel Zeit, ehe man Schieffe, so zur See gehen ⟨und⟩ alhier nit zu bekommen sein, bestelt; ⟨und⟩ wohl an die <e> […] {Compagnien} [200] so notwendig von hier abgefurt werden muchen, zwölff {Compagnien} [213] Canons mit gehoriger [208] ⟨und⟩ [XX] Train darauf geladen ⟨und⟩ mit notturfftigen [194] ⟨und⟩ Futterungen versehen werden solten, sein musten, des grossen Unkostens gentzlichen zu geschweigen.

⟨Und⟩ kan contrari Wint kommen, dass man in <f> ⟨oder⟩ <K> Wochen nit einen Schrit weit hinder oder vor sich kommen kan. Zudem so musten die [168] umb einen freien Pass ersucht werden, damm kein Garnison ohn expressen Befehl ein solch Anzal Schieffe würde passiren lassen. Vors dritte würde der Feit [129] Intention darauch leicht abnemen ⟨und⟩ zuvorkommen. Viertens so kan auch über dieses aus disen Quartiren kein [193] (weill di alten {Compagnien} schwach sein ⟨und⟩ die newen nitt auff kommen), wie auch Stücke genommen werden, damm die Commendanten täglich deren beiderlei mehr begeren.

Es sein zwar di <0> newe zwölfpfündige Stücke von [220] alhir, aber noch nitt lavettiret; so hatt man auch keine Kugel ⟨und⟩ [197] Wagen, Constabels ⟨und⟩ Attilage. ⟨Und⟩ i<au> Wartenberg abgedancket, wirt auch nunmer mit [?Frantzosen] sich wider einlassen. Daher auf ihn oder sein {Regiment} ⟨…⟩ unt die Obristen Uffel ⟨und⟩ Karpf aus iren Posten (weill der Feint Feurmorsell ⟨und⟩ Stücke auch m[181] nach Warendorff gefwret, seine Intention aber man annoch nitt [?weiss]) nit zu nemen sein. So begert auch Uffell, weil sin [260] izo so schlecht [?aussehet], nit abzuzancken; auch wirt er ungern in [215] unter[…] stehen [?wollen].

⟨Aber das alles so muss zu fordern und sonderlich⟩ wegen Aussnemung der Völcker ⟨und⟩ wider Bestellung der Commendanten, wen Uffell ⟨und⟩ Carpf [?beide mitgehen] solten, mitt dem <V> alles erst uberlegt ⟨und⟩ abgeredet werden, ⟨welches damm seinen Zuschreiben nach in wenig Tagen alhier sein wird, erfahren⟩ unt Resolution von dem Concluso, wass [126] ⟨und⟩ [153] disen Sommer thun ⟨und⟩ wie balt sie zu Felt gehen werden; 2 ob sie {die Staaten} mitt in ihre Alliance nemen; 3 Musterplatz im Clevischen verstatte, <4#> [XX] bei Lehrort zen Pass ⟨und⟩ Repass über [174] geben ⟨und⟩ darzu eine Brücke herleihen wollen, mitt bringen [?will]. […] doch ohn alles Massgeben (wen es nur dech obigen Feintshalber ist geschehen kan) sich nitt zu übereilen, sondern erst des [122] Widerkunft auss m[214], der dan, sobalt er alhir wider angelangt ist, die [200] nemen ⟨und⟩ zu {die Staaten} gehen will, ⟨und⟩ wohin sich der Feint, welcher beisammn, ⟨weil auch⟩ Jan de Wert so zum Aufbruch sich zwischen Ruhr ⟨und⟩ [268] gefast machet, sich wenden werden, erst zu sehen ⟨und⟩ zu warten hetten.

Dan die Coniuction ⟨…⟩ nirgent eher ⟨und⟩ füglicher als bei Cloppenburg oder Vechte geschehen, damm sie eher von Minden zu Quackenbriegell als zu Verden anderall sein können, ⟨und⟩ haben sie Ossnabruck ander Seiten; kan auch vom Feint ihr kein Schade geschehen, damm Cloppenburg, Vechte, Wiltzhausen und Depholt schlecht besetz sein. Forstenau aber ist mit [oo] <s> […] [193] ⟨und⟩ <o> {Compagnien} [212] belegt; es ist aber die Hase dazwischen, dass sie also von dem Feit, der da in Garnison ist, sicher [?…] [216] wohl gehen ⟨und⟩ dass Reiderlant zuerst, wie der Manssfelter getahn, eingenommen werden kan. Damm die Friessen itzo 1 {Compagnien} [193] von <o>tkopffen werben, auch eine Schantze zwischen Stuckhaussen ⟨und⟩ Bossem an dem Pass, da man ubergehen kan, aufwerffen. […] sollen auch sein die Wege […] so bos, dass man mit Wagen ⟨und⟩ Pferden noch nit darin fortkommen kan.

⟨Habe dar … dieser verantwort,⟩ d[a]ss ich wegen dess Feints Zusammengehen ⟨und⟩ dess [160] Abwesenheit kein [193] [212] ⟨und⟩ Stücke auss den Garnisonen nehmen, auch dass Commendo verendern kan schleinig. ⟨…⟩ Sobalt aber der [122] kombt, soll {die Staaten} auf alle Puncten unterth ⟨unt⟩ aussfurlich beantwortet ⟨und⟩ der <V> sich schleinig durch einen ⟨oder⟩ den andern Weg zu [129] zu erheben pussiret werden. Ob ich aber [?gleichwohl] ⟨und⟩ <+> noch vor s[122] Widerkunft mit {die Staaten} Train allein auf [147] gehen soll, darauf erwarte ich Befehl, ⟨und⟩ will mich auf solchen Fall all Zeit gefast halten.

⟨… stehet bey demselben,⟩ Obrister Hohendorf ist ⟨unterweges bey mich⟩ kommen, berichtet, dass er den Rest von seinem [191] etwa <4H> man widerholten in den Fegesack geschicket hette, welcher vermeinte, mit seinen Völckern nunmehr dass Land vom Hadelen, so Sachsen-Lauenburg zustendig ist, einzunemen ⟨und⟩ daselbst Quartier zu suchen; ist auch nach m[123] zu [?Rantzo] gezogen.

## Notes

- Word division, i/j and u/v as the sense needs; "Feit" (= Feind, l. 12, 'ferEIt' in both copies), "dach" (= dass),
  "seher" (= eher), "zen" (= den), "dech" (= des), "darauch" (= daraus) are the writer's slips as the figures give them,
  kept.
- "ligen": f. 28 `99 Π? 54 79 83` (a gate-like sign), f. 30 `limen`; partly carried.
- "Pferde": f. 28 `pferi`, f. 30 `pnert`; "Pferd(e) starck".
- "bestimten": both copies write `be 7 imten`, the lone 7 standing for st.
- "wohl an di <e> […]": f. 28 `wohlandii [e] wen tt`, f. 30 `… [e] len tt`; no word comes out.
- "wider Bestellung": f. 28 has `[128] iderbeSTeLLeng`; f. 30 has `widerbeSTeLLung`, so the "128" of f. 28 is a w-group
  and is not read as the code for Cöln (corrections file).
- "i<au> Wartenberg abgedancket": `i S` in both copies; "ist" would need a t; open.
- "Frantzosen": `miTT rantzosiCH` in both copies; the F is not written and the ending is "sich"; partly carried.
- "weiss": `w EICH` (f. 30), struck 44 in f. 28; "aussehet": `AU e het`; "wollen": f. 28 `wo SCH en`, f. 30 `wo [U?] en`.
- "beide mitgehen": `bEI de mi LL gehen` in both copies; the ll-sign stands where t is needed.
- "will": f. 28 `wi SCH`, f. 30 `wi [U?]`, followed by clear words read differently in the two transcriptions.
- "gleichwohl": `m lEICH uohl` in both copies, m for g.
- "Rantzo": f. 29 `zu radt zo gezogen`, f. 31 `zu rantz o gezogen`.
- "Hohendorf", "Rest", "Forstenau aber" follow f. 31/f. 30 where f. 29 has `hohtndorf`, `rz st`, `AU waeer`.
- Place names: Lehrort (Lerort, the Rhine-Lippe ford by Wesel), Quakenbrück, Verden, Osnabrück, Cloppenburg, Vechta,
  Wildeshausen, Diepholz, Fürstenau, the Hase, the Reiderland, Stickhausen, Vegesack, Hadeln (Saxe-Lauenburg).
