# BnF fr. 15573 ff. 379r–381v: French text as produced by the key (partial reading, v1.0 work)

Despatch in Matignon's Cipher-3, autumn 1586 (sender probably Matignon; addressed to the King).
Images: Gallica `btv1b90618780` views 740–745, Source gallica.bnf.fr / BnF.

**Status: near-complete reading (v0.5); open items listed.** 2,837 signs were read by Claude Opus 5.5 against a sign sheet (five passes, voted), then:

- sign classes the sheet had merged were told apart on the image (version 0.5: B/Bn, xi/eps, 9t/z3, S/Sq, 14/4, oo, each change asked of the reader twice and looked at by eye; version 0.5: xi/zz, S/6, S/Gc and the code signs Noo and 13, decided by eye on contact sheets of every occurrence, see `stageF-relabel.json`);
- five image-decided correction rounds on the unresolved stretches (a change only where two reader asks agree and the image supports it);
- names, places and period spellings added to the lexicon (`lexicon-additions-v1.tsv`), and an elision rule (l', d', qu'...).

The decoder runs a whole page at a time. It may use another pass's name for a sign at a cost; every such use is recorded in the kit's decode.json under `switches`.

**How the text was made:**

- The letters come only from the key (`data/key-cipher3.json`, revision 9): Tomokiyo's table plus values aligned on the 1586 decipherments of a sister letter (fr. 15572 ff. 277-280) and on the 1585 decipherment of another Cipher-3 letter (fr. 15570 ff. 271-273). A code group such as *le_roy_de_navarre* is one key value and is written with underscores.
- Where a sign has two values (y = t or n; 8 = v or o; d = f or *vostre*; # = i or r; Lq = o or y...), the word decoder chose one with the period French lexicon. The choice is recorded in `data/<page>/key.json`.
- Every remaining gap is listed with its cause in `unresolved-v10.md`.

**How to read the two versions:**

- **Literal** is the key's output with no spaces; · marks a sign with no value.
- **Normalised** has only spaces added by code. A stretch in [brackets] matched no dictionary word. A word that runs on to the next line ends in =. No letter is changed.
- Reader accuracy on known text was about 0.93–0.96 per sign, so expect roughly one sign in twenty to be wrong.

## f. 379r (view 740; 589 letter positions, signs read as sense 0.9503)

### Literal

```
 1 lbfyacequilpliaistavostremaie
 2 stemepouaderluydoneradu
 3 ispourlettredevostrearmeeneueulasa
 4 isonquiestprochedeluiueretque
 5 ilnyarienquiincymodetantc
 6 paysquelusplacesquisontsurla
 7 liuieredegaroneentretolou
 8 seubpourdeauladontceulxdela
 9 ovtellereligiontirentde
10 grandesdacessurlesmarcu
11 andisesuomevostremaiesteuei
12 siluyplaistcequilsonnim
13 poseasainteaaselleparlescvm
14 issionsquele_roy_de_navarreenafayonexpedier
15 dontielusenenuoyeaconie
16 setfontlesemblaaleacaumont
17 enaumasdeuerdutempesch
18 entletraficquequecomerceetco
19 nsequementleriueaudela
20 conptablieetconuoyquisont
21 lesplusclairsdeniesdont
22 vostremaiestepeltfaireestaten·ilme
```

### Normalised (word breaks by code)

```
 1 [l] [b] fy a ce quil pli aist a vostre maie=
 2 ste me pou a der luy doner adu=
 3 is pour lettre de vostre armee neueu la sa=
 4 ison qui est proche de lui uer et que
 5 il ny a rien qui in cy mode tant [c]
 6 pays quelus places qui sont sur la
 7 li uie re de garone entre tolou=
 8 se [u] [b] pour de au la dont ceulx de la
 9 ov telle religion tirent de
10 grandes da ces sur les marc u=
11 an dise suo me vostre maieste uei
12 si luy plaist ce quil son nim=
13 pose a sainte a a selle par lescv m=
14 ission [s] que le_roy_de_navarre en a fay on expedier
15 dont ie luse nenuoye a con ie
16 set font le sembla a le a cau mont=
17 e nau mas de uer du tempes ch=
18 ent le trafic que que comer ce et co=
19 n se que ment le riue au de la
20 conptablie et con uoy qui sont
21 les plus clairs de nies dont
22 vostre maieste [p] el [t] faire estat en [·] il me
```

## f. 379v (view 741; 566 letter positions, signs read as sense 0.9082)

### Literal

```
 1 seambletuilseraplusa
 2 propusdecomencerparlapourneto
 3 erladineriuraeretantpourle
 4 soullaigementdeuossubie
 5 tsqueosterlefoienausdicts
 6 delareligionetetauoirdvostres
 7 ruiceplustostquedallerata
 8 queuerunefortemplaceoulesi
 9 egepouroynestresilong
10 queueseruittoutcequevostrearmee
11 puuroinexploicterencest
12 aneetquinanorneroittantde
13 faueuretunillyteaubiende
14 uosafairesetpourcestefei
15 sifmaiestelauoitagreab
16 lcilseroitaesoingquevostrear
17 mesacheminastnblancen
18 aeryaconvostrepllanuillebpos
19 etcuallaisetcefaisannell
20 tiendroitensuspensles
21 ·placesdelaitnvng·dung
22 costeetdelautreaergera
23 sainctevostrepsetcastilloni
```

### Normalised (word breaks by code)

```
 1 se amble tu il sera plus a
 2 pro pus de comencer par la pour net o
 3 er la diner iura er etant pour le=
 4 s ou [ll] aige ment de uos subie=
 5 ts que oster le foi en aus dict [s]
 6 de la religion et et auoir [d] vostre s=
 7 r uice plustost que daller a ta
 8 que uer une fort em place ou le si=
 9 ege pour oy nestre si long
10 queue seruit tout ce que vostre armee
11 [p] uu roi nexploicte renc est
12 a ne et qui na norne roit tant de
13 faueur et uni [ll] y teau bien de
14 uos a faire set pour ceste fei=
15 s if maieste lauoit agrea [b]
16 [l] cil seroit a [e] soing que vostre ar=
17 mes acheminast [n] blanc en
18 a er y a con vostre [p] [ll] an uille [b] pos
19 etc [u] allais et ce faisan ne [ll]
20 tiendroit en suspens les
21 [·] places de lait nvng [·] dung
22 coste et de lautre a er ge [r] a
23 saincte vostre [p] set castillon [i]
```

## f. 380r (view 742; 571 letter positions, signs read as sense 0.9126)

### Literal

```
 1 enuoieavdeuilleroyune
 2 ·eniedelevrequeleudeclerua
 3 otaescriptpassantparcepais
 4 aungdesesamislequelmela
 5 enuoyeetprienestredesc
 6 ouuertparcequec·aseroitlusos
 7 tertout·moiendetplusry
 8 ayensauoirquimeselooitchose
 9 ppreiudiciablemdovostreaseruice
10 iestimequedelavostremaiestepou
11 rarecongnoistrecequicepe
12 ultespererparledeviseildud
13 ictcleruantaquitrouueralep
14 lquieeisetleponfortprepares
15 asonhumeurdelanegociati
16 ondemessieursdelenoncourt
17 poignyetpresidentarulart
18 tiestimequesile_roy_de_navarrenatrotevdeg
19 disposeaprendresonpart
20 pouelebruicnestquilnau
21 velapourabeaucoupprofit
22 eralereutauireacequevostremaiest
```

### Normalised (word breaks by code)

```
 1 enuoie av de uilleroy une
 2 [·] en ie de levre que leu de cler ua
 3 ota escript passant parce pais
 4 a ung de ses amis lequel me la
 5 enuoye et prie nestre desc=
 6 ouuert parce que [c] [·] a seroit lu sos=
 7 ter tout [·] moi en det plus ry
 8 ay en sauoir qui me se looit chose
 9 [p] preiudiciable [m] do vostre a seruice
10 [i] estime que de la vostre maieste pou=
11 r a recongnoistre ce qui ce pe=
12 ult esperer parle devise il du d=
13 ict cler uan ta qui trouuer alep
14 [l] qui [e] [e] [i] set le [p] on fort prepare s=
15 a son humeur de la negociati=
16 on de messieurs de le non court
17 [p] oi [g] ny et president ar [u] lart
18 ti estime que si le_roy_de_navarre na trot ev de [g]
19 dispose a prendre son part
20 pou [e] le bru [i] [c] nest quil na u=
21 ve la pour a beaucoup profit=
22 er aler eut au ire a ce que vostre mai est
```

## f. 380v (view 743; 594 letter positions, signs read as sense 0.9342)

### Literal

```
 1 desirelesforcesduso
 2 ntlelongdelariuieredelisle
 3 etuiuentlaouilspeuuentet
 4 continuentleursfortyfi
 5 cetionscomeiayaduerts
 6 imai·estepourleregartdagen
 7 avostreseursimaintientellela
 8 ufortifieretrecheroe
 9 aforcesmmoienslaouelle
10 peuldyquimpiselleafortpeude
11 moienslesponsulsmqueon
12 escriptquilssontfort
13 mariaseueoirreduictpen
14 lestatetdeuoyilssontler
15 eceueurquenicullierquiestaag
16 enauqueueliescriuiadesqueie
17 sceusquelesarmyesestoientpl
18 aoseseteusrespocedelusqui
19 lsatetferoitaquicequeyetlusgand
20 foisdestoitdallersasarecepte
21 amarmandemaislafriandis
22 etlelaroitquifaictquebaillanttro
23 iscetsescusaavostreseurlon
24 lusencomptecinqdeensquies
```

### Normalised (word breaks by code)

```
 1 desire les forces du so=
 2 nt le long de la riuiere de lisle
 3 et uiuent la ou ils peuuent et
 4 continu ent leurs fort y fi
 5 cetions come iay ad uert s=
 6 i mai [·] este pour le regart dage n=
 7 a vostre seur si maintien telle la=
 8 u fortifier etre che roe
 9 a forces [m] moi ens la ou elle
10 peu [l] dy qui [m] pis elle a fort peu de
11 moi ens les pons ul [s] [m] que on
12 escript quils sont fort
13 maria se ueoir re du [i] [c] [t] [p] en
14 lestat et de uoy ils sont le r=
15 eceu eu [r] que ni [c] [u] [ll] ier qui est aag=
16 e nau queue lies cri uia des que ie
17 sceus que les ar mye sestoient [p] l=
18 a ose set eus res [p] o ce delus qui=
19 l sa tet feroit a qui ce que y et lus gand
20 fois destoit daller sa sa recepte
21 a marmande mais la friand [i] s=
22 et le laroit qui faict que baillant tro=
23 is cet sescusa a vostre seur lon
24 lu sen compte cinq de ens qui es
```

## f. 381r (view 744; 619 letter positions, signs read as sense 0.9179)

### Literal

```
 1 pourcausequilnetarienfaictetquei
 2 esunlietreshumblementvostre
 3 maiestequetellemescuancete
 4 nedemeureimpugnyelildeu
 5 erditacestehdeulequinse
 6 aseysemilescuscestchose
 7 desimauuaiseconseouetctil
 8 yenaunganmlacquiferalese
 9 mblaaleeiespereetladillig
10 encedevdegpurguesilsyour
11 uorraiaapresentementest
12 aduurniquele_roy_de_navarreadeslibleledera
13 menerauecluyasonretourdela
14 nguedoclesquedechastillon
15 dandossetescualdevostreossauec
16 leplusdeforcesquipouratantde
17 piedquedecheuallesudecaste
18 lnaultetpraielontleiechacu
19 nungiregimentetbearnai
20 oieetpuallosseetcedoibuent
21 ioindreaussiauecleditdele_roy_de_navarre
22 ilsf·nneouielearuictmais
23 cestchosequeienetientasseuree
```

### Normalised (word breaks by code)

```
 1 pour cause quil net a rien faict et que i=
 2 e sun lie treshumblement vostre
 3 maieste quet elle mescu an cete
 4 ne demeure impugny el il de u=
 5 er dit a cest eh deu le quinse
 6 a se y se mil escus cest chose
 7 de si mauuaise con se ou etc til
 8 y en a ung an [m] lac qui fera le se=
 9 mbla a le [e] ies pere et la dillig=
10 ence dev de [g] pur gue sil sy ou [r]
11 uorrai a a presentement est
12 ad uu [r] ni que le_roy_de_navarre a des li ble le de ra=
13 mener auec luy a son retour de la=
14 nguedoc les que de chastillon
15 dan dos set escu al de vostre os sauec
16 le plus de forces qui pour a tant de
17 pied que de cheual le su de caste=
18 lnau [l] tet [p] [r] a ie lont le ie chacu=
19 n ung [i] regiment et bearn a i=
20 oie et pu a [ll] osse et ce doibuent
21 ioindre aussi auec le dit de le_roy_de_navarre
22 ils [f] [·] [n] ne ou ie le ar ui [c] [t] mais
23 cest chose que ie ne tient asseuree
```

## f. 381v (view 745; 325 letter positions, signs read as sense 0.9322)

### Literal

```
 1 quilsfontsortirdelarti
 2 lleriedenauarainsetqueuauec
 3 deulxpiecesdeaameriequiso
 4 amontflotquinquilsdoib
 5 uentanesptersuragenyasa
 6 uoirdesseingdeestchosetou
 7 teasseureeietayaduertsleues
 8 quelyquede·baiourdanmapres
 9 entementescriptquecestdur
10 asquiestalleenespaignedparle
11 rauroyetluyfairequeloueofre
12 iecroyquecestacherchermo
13 yensdesalyxlauollonneses
```

### Normalised (word breaks by code)

```
 1 quils font sortir de larti=
 2 llerie de nau a rains et queu auec
 3 deulx pieces de a amer ie qui so
 4 amont flot quin quils doib=
 5 uent a nes [p] ter sur age ny a sa=
 6 uoir dessein [g] de est chose tou=
 7 te asseuree ieta y ad uerts leues=
 8 que ly que de [·] [b] a iour dan ma pres=
 9 entement escript que cest dur=
10 as qui est allee nespaigne [d] parle=
11 r au roy et luy faire que lou eo [f] re
12 ie croy que cest a chercher mo=
13 yens de sa ly [x] lau o [ll] on ne ses
```

