# Re-reading log, R291 (22 Oct 2026, Claude Opus 5.5; REREAD_BRIEF, batch b01)

## Starting point

Reading audit: "decoded, not read", clean share of the old decrypt 0.046. Four register pages (pp. 38-39 + two
unnumbered), almost all cipher; despatch "B." of Vienna 11 August 1629.

## What was done

1. **Existing text?** Kiewning 1897 Nr. 157 (Wien 1629 Aug. 11, dechiffr. 6 Sept., Nunz. di Germania 119 fol. 37-40),
   edition lines 23569-23630. It is a German regest with two Italian quotations. `reread_b01/R291_align.txt` confirms:
   every chunk costs 1.06-1.21 per letter except the "così per la spesa accennata ... in Germania" chunk (0.35). The two
   quoted passages are taken from the print (OCR corrected: "S. S*" = S. S.tà, "4 gl'" = a gl', "eome" = come, "l'nso" =
   l'uso, "pereona" = persona); the decode agrees with them ("compeacici apaicae così amreuol mente il pensio ...
   interesi di cao mia"; "prima di havere o per mode gli asa in Germania").
2. **The rest from the figures.** The whole decode was dumped with its codes (`reread_b01_decode` tokens) and read run by
   run; every break was resolved from the letter values of the 6956 key or left as a hole. The clear text was read on the
   scans: date "Vienna 11 di Agosto 1629", address, register letter "B.", the underlined docket "Con occasione di visitare
   il Sig. Duca di Neoburgh", and on p. 2 "non po:|tendosi perciò [?indovinar] se" (DECODE: "non ??:").
3. Points settled on the scan or by the figures:
   * first groups 57 8 567 8 69 = "per occasione di" (DECODE 9 for 5; `R291_corrections.tsv`);
   * "di lì a [272]iro giorni" = quattro (27 = qu; the regest has "Nach 4 Tagen");
   * "figlia del [344] alberto di [259] frateulo di sua moglie" = duca Alberto (di Baviera): the figures spell "alberto";
     Kiewning's regest has "Herzogs Alfons von Baiern", an error of the regest (Albrecht VI of Bavaria was the brother of
     Wolfgang Wilhelm's first wife Magdalena, d. 1628). The coordinator may want this noted.
   * "in[320]modo" read "incommodo" ([320] in the C range); "dal [457] venuto alla fede [309]" and "abiurato l'[457] e
     professata la fede [309]": 309 = cattolico/-a (six contexts in R291, all fitting), 457 = heresia (two contexts).
   * "uiue uostis o{Duca di Mantova}oa{Sua Altezza}" = "vivae vocis oraculo" (Kiewning prints the phrase in the regest);
   * "[?con]solatione": the decoder's {Monsignore} (522) is 52 = con + a misread 2(3).

## Holes and why

* [750] (three times: "havesse [750] [750] questo pensiero", "il frutto del discorso [750] li giorni adietro"): a group
  meaning "fatto / di" or "già"; not settled.
* [405], [796], [573], [557], [690], [697], [762], [279], [440], [966], [239], [469]: three-digit groups with no stable
  value across the batch; [440] "un padre [440] allhora suo confessore" is probably Gesuita (regest: "einem Jesuiten"),
  [279] after "Paolo" probably Quinto (regest: Paul V.), both left as groups because only the regest gives them.
* "gli erano stat[e] p[…] […] principesse": the figures "p{367} i et{299} lo" do not resolve.
* "della sua […] casa", "in […] o in terzo grado", "la dispensa di N. S. […] per l'una": groups 330, 233, 232 + letters,
  unresolved.
* "e si [?lasciò] […] che le sarebbe piaciuto ... per mandar[la] […] all'instanze di [?pace]": letters garbled
  ("si alote rocogliere", "confor{tuttavia}"); not checked on the scan line by line.
* "e l'altro […]", "di poter […] delle entrate": "che d u{occasione}", "maca{massime}e"; unresolved.
* "Non ho […] di darne": "p[725]i[693] {far}ciar" — perhaps "potuto tralasciar", groups unknown.
* The despatch breaks off at the foot of p. 4 ("come [469] qu—"); the continuation is not on this record.

## Group values proposed

* 309 = cattolico/-a (R291 six contexts; R292 "dichiararsi [309]").
* 457 = heresia (R291 two contexts).
* 567 = occasione (already in the batch list) confirmed on the scan at the opening.

## Result

Read in part: the sentences hold except where three-digit groups are unknown; clean-sentence share 0.584
(`docs/_check_reading.py --file`, was 0.046). The sense of every paragraph agrees with Kiewning's regest.
