# HCPortal 507 and 509 reread log (23 Oct 2026, batch r2k)

## Why

Batch b08 (22 Oct) decided 507 (ff. 28-29) and 509 (ff. 32-33) on the plain clean-sentence share (0.437, 0.545). For
German before 1700 the brief takes the explicit-hole share (`v2_score.py`) plus a reader's judgement; on that measure
the two score 0.662 and 0.659. 509's German news extracts in the second hand were also never transcribed (gap
blocker not-attempted).

## HCPortal 507 (ff. 28-29)

- Spelling: `research/reading_audit/r2b_mals_denorm.py HCP507_reading.md f028.txt f029.txt --alt f030.txt f031.txt`
  found one more normalised form, "noch nit lavettiret" -> "nitt" (f. 28 `niTT`); applied. No other b08 normalisation
  left. The reading was otherwise restored by r2b.
- Reader's review: the reading body read sentence by sentence against the b08_dec decode of f. 28-29 and the writer's
  duplicate ff. 30-31 (`HCP507_corrections.tsv`, 9 readings from the duplicate). The sentences hold: the journey by
  land or by sea and the four objections (contrary wind, passes from the States, the enemy forestalling, no troops or
  guns to spare), the twelve-pounders without carriages, Wartenberg discharged, Uffel and Karpf, the questions for
  the States (alliance, muster place in Cleves, passage over the Rhine at Lerort and a bridge), the conjunction at
  Cloppenburg or Vechta, the Reiderland, Hohendorf and Hadeln. Holes are the unvalued codes (193, 212, 200, 122, 129,
  ...), the signs (V, K, 4#, e, f, o) and about a dozen partly carried words, each marked.
- Scan spot check (hstam_4_h_1411_0028, crop `reread/r2k/z28_a.jpg`): the line "Und 39 A 11 78 39 54 61 Und 36 Z 37 70
  30 26 ..." confirms the transcription of "aTTilage Und i AU wartenberg": the open "i<au> Wartenberg" (no t for "ist")
  is in the figures, not a misreading.
- Look-alike alternates: none chosen against a figure's value; the emendations rest on the writer's own duplicate.
- Score (`v2_score.py`, de): plain 0.38 (27/71), explicit holes **0.662** (47/71), hole rate 0.111; unchanged by the
  one re-spelling. A stricter variant counting unvalued signs and sign labels (`r2k_score.py`) gives the same 0.662.
- Decision: **read (B)**.

## HCPortal 509 (ff. 32-33): the German extracts transcribed

The clear text of the second hand (a fast Kurrent) was transcribed line by line on autocontrast crops of the HCPortal
scans at 2-3x (0032 y 1420-2500, 0033 y 220-1500; crops `reread/r2k/y32_*`, `z32_*`, `y33_*`, `z33_*`). The cipher
runs were not re-read (b08 decode, `f032_corrected.txt`, `f033.txt`). Transcription as read (line breaks of the
scan, `|`; [?] an unread word, [?word] doubtful):

f. 32, extract 1 (heading "Extract <cipher> schreiben / aus <cipher> vom 16/26 Mart. 1637."):
1 In Franckreich ist man nicht wohl zufrieden, dass der Hertzog von Parma, wie man [?nicht] vermeinet, |
2 gehabt eine neutralitet gehandelt zu haben, sich auch verpflichtet [?Saindetta] den besten importanten |
3 Platz dem Hertzog von Medina Viceroy von [?Sicilien] in handen zu stellen Und dass in Piacenza Und |
4 Parma [?Hochdeutsche] Und Italianer unter [?] mit [?einigen] officirern in guarnison gelegt werden sollen; |
5 Herr [?] Landtgraff [?] das [?wesen] thut wohl seine sache in acht zu nehmen Und Franckreich, dass er |
6 ihm darin die hand [?bieten], [?verspricht] auch dass demselben [?widerumb] eine gute [...] ; |
7 Es ist ein Werck das [?gar] viel meritiret, Und da er nit will, solten [?ihr] [?selbst] das encouragiren so viel [?bey] der [?Zustandt] |
8 leiden will, ob ist allzeit besser etwas gethan Und dadurch seine gewogenheit zu bezeugen, als nichts |
9 248 solte billich das <cipher> weil <cipher> Und also |
10 durch denselben [?directe] [?] [?oder] etwas solte ihm können, dahin das OO am meisten geneigt, ob |
11 ist aber vor erst das hier <cipher> als <cipher> |
12 <cipher> gleich wohl helt <cipher> bis |
13 sicherheit vom schluss mit Franckreich kömbt, Immittelst überlegt man wie 188 Und AA contentement zu geben |
14 Und wohin <cipher> [?] [?], ob [?sich] [?] XX oder [square] nach GG scheinet |
15 abzuführen, doch ist gut zu apparent, das 155 mit hülffe CC soll ahnnehmen <cipher> |
16 <cipher> Und damit bringt [?ex] [?] nach <cipher> zu thun; da das [?Al]- (struck word) |
17 (above: ist) liance geschlossen, wirdt <cipher> müssen, 155 solle vermög derselben [?sonsten] |
18 <cipher> Und: <cipher> Und das demselben seine Commission [?empfangen] |

f. 33:
1 Da aber gleich die alliance nicht geschlossen wirdt, hat gleichwohl <cipher> |
2 <cipher> mit GG AA oder KK |
3 In Engellandt gehet man damit umb eine Comp. nach Ost Indien [?aufzurichten], dann der König die |
4 gerechtigkeit der Admiralitet Und acten (struck: unter) seinem Siegel zu geben [?versprochen], wie auch |
5 die [?bey] [?ihren] Congnesten zu maintenieren; Metter tijt compt Herman met wambas en |
6 de broeck. Staet te hopen dat metter tijt ock sal volgen; das Pfältzische manifest |
7 so ziemblich weitleuffig, wirdt balt heraus kommen; |
8 V F 13 123 5 April / 26 Mart. 1637 |
9 Sonsten stehen die handlungen mit Schweden, Franckreich Und Engellandt <cipher> |
10 <cipher> gehen <cipher> mit LL habe ich auch [?beweglichst] (above: anhalten) |
11 [?sache] [?gewust] <cipher> |
12 Hat der Pass durch [?] [?offen] [?] sagt man [?frey] [?dass] der Kauffleut zu [?Andorff] [?geschehen] |
13 ob wirdt berichtet, dass la Valette mit einem Heer die Mosell herab kommt Und 20000 |
14 man in Italien geschickt werden; Es hat es mit dem bündt zwischen Franckreich Und |
15 Engellandt [?schwer] [?zu] [?haben] sein, darumb weil Franckreich will, dass man [?Schweden] Und |
16 Hollandt mit lassen begreiffen solle; Schweden will itzo von St. Chaumond etliche |
17 erklerung wissen, ob Franckreich offenbar feindt sein wolle mit dem Kayser, |
18 Franckreich will den König in Ungarn nicht kennen als Königl. König; |
19 21 73 B 24 35 156 17/27 Martij 1637 |
20 Zu Paris hat man mit abfertigung Hertzog Bernhards von Sachsen Und la Valette |
21 so viel zu thun, dass andere verrichtungen Und expeditiones verschoben werden. |
22 Der Hertzog von Rohan hat eine gute victori wider die Spanier erhalten, so haben |
23 die Frantzosen [?] [?Landtgrund] Und [?] 1200 man erlegt Und 200 gefangen |
24 [?dessen] die relation des Curirers [?gemeldet], der Obrist Roß hat vor wenig tagen |
25 ein Gallasisch Regiment geschlagen. |

The 28 Sept transcription's guesses "Ist Frankreich", "Ihr? feindes, ob Herr", "wie jeg-", "dermög ... hanstat" are
replaced ("In Franckreich", "[?] [?], ob [?sich] [?]", "wie 188", "vermög derselben [?sonsten]"). The text is set
into `HCP509_reading.md` around the decoded runs, English in `HCP509_en.md`.

Score (`v2_score.py`): whole reading body plain 0.244 (19/78), explicit holes 0.667 (52/78), hole rate 0.109 (before
0.659, 29/44); split: the French letter (fr) 0.933 explicit (plain 0.733), **the German extracts (de) 0.50 explicit**
(24/48, hole rate 0.163).

Decision: **decoded, not read** kept. The pooled 0.667 clears the bar only through the French letter; the German
extracts, which carry most of the record's cipher (the French letter has five short runs), fall to 0.50 once their
doubtful words count as holes. In the f. 32 extract nearly every cipher-bearing sentence holds an unvalued code or
sign (248, 129, 155, 148, 133, 126, OO, AA, XX, square, GG, CC) and the second hand leaves single words unread. The
extracts are no longer not-attempted: what stays open is (a) the codes and signs (no key material: they are not in
key.txt and occur once or twice, no named parallel; their referents are persons and powers in the London/Hague
correspondence) and (b) about 30 words of the fast second hand unread or doubtful at 2-3x on the HCPortal scans
(illegible on the available images).
