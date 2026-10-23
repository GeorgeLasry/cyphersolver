# HCPortal 503 (HStAM 4 h Nr. 1411, ff. 15-16), Malsburg to Landgrave Wilhelm V, Wesel, Jan 1637 — reading of the cipher

Rests on: `f015.txt` (the "Triplicat", one faint block) and `f016.txt` (the letter of 30 Jan [/9 Feb] 1637, two blocks),
transcription agents checked by Bourdeau, decoded with `key.txt` unchanged (`research/reading_audit/b08_dec.py`), the
breaks checked on the HCPortal original scans (hstam_4_h_1411_0015, 0016; fetched 22 Oct 2026 into the session
scratchpad; batch b08). f. 16 has heavy show-through from the enclosure list on the other side. f. 17 is the address
side (no cipher). No contemporary decipherment, no clear copy, no edition. Code values: `{Compagnien}` = 273,
`{die Staaten}` = 188 (grade I, `codes.txt`).

State (22 Oct 2026, batch b08): decoded, not read; clean-sentence share of the reading body 0.375 (raw decode 0.389); holes: open codes and signs in most sentences. Log: `HCP496-509_reread_log.md`.

Conventions: `{...}` a code with a context value; `[120]` an unvalued code; `<H#>` an unvalued sign; `[?word]` partly
carried; `[word]` supplied; `[…]` unread. Spelling as the cipher gives it: the b08 normalisation (`research/reading_audit/b08_norm.py`) was undone on 23 Oct 2026 (batch r2b, `research/reading_audit/r2b_mals_denorm.py`: each word restored to the form its figures or the transcribed clear words give, e.g. alhir, Feint, schleinig, hette, dan, one); modern spelling only in the English file. punctuation added. ⟨...⟩ = clear words
written in the letter around the cipher. Paragraphs: the f. 15 block (Triplicat); f. 16 block 1 (two paragraphs);
f. 16 block 2.

## Reading

⟨… ich habe ihm⟩ beim [122] u<4#> [?Resolution] auf [129] Schreiben angehalten. Es ist aber derselbe itz mit [120] wegen des Verlust vor Hermanstein in der […] ⟨und⟩ hatt die Gedancken ni<A#> alle bei einander.

⟨… weil er in Staadische protection genommen ist,⟩ [120] will noch von keinem [202] wissen; sagt, er erwarte Bauregart alle Tage wider. ⟨Und⟩ Hoff schreibet noch [?kürtzlich], das Borigart noch nie Audiens gehabt. Ich habe [120] andeiten [?lassen], das [129] nach Anfang des Traicte zu Minden ⟨und⟩ <+> Aufkündigung des Stilstants an die 9 {Compagnien} [193] ⟨und⟩ <f> ⟨und⟩ 9 {Compagnien} [212], wie auch sch[…] {Compagnien} Tragons [?schon] [?…]teil [?geworben], ⟨und⟩ 2 Teils zu werben Patente albereits ausgeteilt [?hetten]. Solten sie nun in irer voller Werbung [?gehindert] werden, so würden sie in aller irer Intention ⟨und⟩ Actio[n] gehemmet, welches dan dem König ⟨und⟩ gemeinen Wesen mehr als {die Staaten} […] particulir Schaden bringen [würde].

Zu deme [?hette] Hoff [?berichtet], das ihm were [?angedeutet] worden, wie das der Ambassadeur schon Ordre [XX], die auf den leizten [?December] schiene <4H#> <o>ch Reichs[…]dalen solte, dan er noch [201] in Deitschlant ligen hätte. Er hat sich aber nirgend zu verstehen wollen ⟨und⟩ wirt bald von hir [?ziehen]. Sorge derwegen, man werde sich auf die Golder, vil weniger auf die [?abgeredete] Termine verlassen ⟨und⟩ […] machen kommen.

⟨Ich habe dieses … bis EfGl. ich einweinig⟩ vons <triangle> ⟨mein Meinung überschreiben können, und dünket mich, es werde EfGl. nicht abhanden gehen.⟩ Er redet aber nirgend von Friedmachen. Sagt, er wolte einen Finger [?auf] der F[au]st drumb geben, dass <H#> den [?bewussten] Brieff von hir vor [120] Ankunft weggeschicket hätte; dann ihn deuchte, {die Staaten} er alsdan mit viel ruhigerem Gemüth dienen könnte. Zu dem wirt er über <e> Pferde notwendig mitbringen müssen. Er sihet aber itzo keine Gelegenheit, zu [129] zu kommen.

## Notes

- "Bauregart", "Borigart": `76 70 S 25 61 43 39 30 26` and `76 93 25 69 43 39 30 26`, Beauregard twice, in two spellings.
- "Audiens": `nie F# 27 69 84 83 77` = nie + crossed-F sign + diens; F# is valued au in the key.
- "lassen": `15 39 T 61 22` = la + ff-sign + en; partly carried.
- "schon … teil geworben": `X 12? 22? 94 G 78 / 43 79 98 73 25 9 61 22` = sch p n t ei l / gewor 9 en; the 9 must be b; the
  word before "teil" is not carried.
- "hetten": `82 61 L? …` the l. 16-17 run is "he <H#> / en"; the crossed H here stands where tt is needed, as again in
  "he <H#> e" (= hette) in l. 27; elsewhere on the page it gives ll (wi<H#> = will, a<H#>e = alle, fo<H#>er = voller,
  wo<H#>en = wollen). Its value is not one letter pair, so the words that need tt are marked partly carried.
- "hette Hoff berichtet": `21 16 L 89 82 35 B 76 61 25 66 N 26 C 61 94` = he tt o hoff bericht mm et; o for e and a stray
  mm-sign.
- "Ambassadeur": `28 56 [blotted group] 10 39 W 55 32 79 58 65` = am [blot] bassadeur.
- "ziehen": `98 36 21 48 63` = wihen; w for z.
- "Golder": a payment term ("auf die Golder, vil weniger auf die abgeredete Termine"); partly understood.
- "würde" in "Schaden bringen [würde]" is supplied: the run ends at "bringen".
- f. 15 "in der […]": `27 16 30 37 70 10 61 97 71 44 48 72 55 / L` = der waberuneha tt; no word comes out.
