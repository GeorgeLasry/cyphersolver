"""r2n (23 Oct 2026): write battier1686 readings/r2n/<doc>_reading.md and _en.md for the thirteen located passages.
    python research/reading_audit/r2n_readings.py
Each reading: header comment (what it rests on), '## Reading' body (cipher text, Battier's spelling; clear text only where
read on the scan, marked 'clear:'), notes. Holes: [?word] partly carried, [word] supplied, [123] group without sense, […] unread."""
import pathlib
ROOT = pathlib.Path(__file__).resolve().parents[2]
D = ROOT / 'targets' / 'battier1686' / 'readings' / 'r2n'
D.mkdir(parents=True, exist_ok=True)

HDR = ('Built 23 Oct 2026 by Claude Opus 5.5 (REREAD_BRIEF, batch r2n) from tokens/{tok} (NA 3.01.18 inv. 401, read group by '
       'group on the full-resolution NA scan) decoded with the inv. 1209 key (key/letters.py, key/dict/*.tsv; new rows in '
       'key/dict/r2n.tsv, each looked up on the key scans). {extra} Spelling as the key and the letter table give it; '
       'word division editorial. [?word] = doubtful mark or digit, or carried only in part; [word] = supplied; [123] = '
       'a group whose key value gives no sense; [...] = unread; (…) = clear text not transcribed here.')

P = {}

P['1687-01-02'] = dict(
    title='Battier to Fagel, Madrid, 2 January 1687 (scans 35R, 36L)', tok='s035R_r2n.txt',
    extra=('An interlinear decipherment of the time, in a second hand, stands over most groups; it was read where legible '
           'and the reading follows the key where the two agree (30 codes and the letter runs) and the interlinear where '
           'the key gives no sense (marked in the notes). The clear text of 35R before the second run was read on the scan.'),
    nl='''Myn Heer. De affaires van dit Hoff blyven in eene staet, dat is te seggen in [?een] [703], en is niemant die op
het remedieren gedenckt.

Verleden donderdagh soude men een nieuwe Gouverneur voor de Nederlanden kiesen, maer by mangel van gelt is het niet
geschiedt: 160 duisent stucken van 8 syn uyt Sevilla hier aengekomen, doch schynt het dat de Koningh het minste daer by
heeft; want Mt., die aan de Koninginne duysent pistolen voor een nieuwjaar woude geven, heeft soo veel niet konnen
vinden, [?als] niet vierhondert pistolen voor [?sy] [?persoon] innen. [361] [448] eweduwe, die Syne Majesteyt al voor
ses [?jaeren] gehadt [...], noch het is niet te [?begrypen] [...] alle [?saecken] [...] [409].

[36L] (…) en noch dat men niet gaern sigh van de nabuyren dwingen laat, de pragmatica te veranderen; niettemin geloof
ick vast dat se het [?ook] altemaal sullen moeten doen.''',
    en='''Sir. The affairs of this court remain in a state, that is to say in [?a] [703], and there is nobody who thinks of
remedying them.

Last Thursday a new governor for the Netherlands was to be chosen, but for lack of money it was not done: 160 thousand
pieces of eight have arrived here from Seville, yet it seems that the King has the least share of them; for His Majesty,
who wished to give the Queen a thousand pistoles for the New Year, could not find so much, [?but] not four hundred pistoles
for [?her] [?person]. [361] [448] [the] widow, whom His Majesty has had already for six [?years] [...], still it is not to
be [?understood] [...] all [?affairs] [...] [409].

[36L] [...] and also that one does not willingly let oneself be forced by the neighbours to change the pragmatic; none
the less I firmly believe that they will [?also] have to do it all.''',
    notes='''- Interlinear and key agree on: dat is te seggen in, niemant die op het remedieren gedenckt, die aan de Koninginne
  duysent pistolen voor een nieuwjaar woude geven, heeft soo veel niet konnen vinden, niet vierhondert pistolen voor,
  weduwe, Syne Majesteyt al voor ses, gehadt, het is niet te, alle, en noch dat men niet gaern sigh van de nabuyren dwingen
  laat de pragmatica te veranderen, niettemin geloof(t) ick vast dat se het ... altemaal sullen moeten doen.
- Key against interlinear: 10:703 is "rabat" in the key (scan 54L), the clerk wrote "een" and a word in the margin that I
  cannot read; 5:331 "geloof" (the clerk "gelooft"). 11:484 is 'Sex.' in the key transcription (the clerk "ses jaeren"): ses.
- From the interlinear only: [?als] (key 273 gives no sense in blocks 1 and 14), [?sy] [?persoon] (437, 254: no block
  checked gives persoon; 10:254 is pertinentelyke), [?jaeren] (405 308 + letters arn), [?begrypen], [?saecken]; 361, 448 and
  the end of the run (1 121 54 577 ... 216 35 409) remain without a reading.''')

P['1687-03-13a'] = dict(
    title='Battier to Fagel, Madrid, 13 March 1687, first letter (scan 54R)', tok='s054R_r2n.txt',
    extra='No contemporary decipherment.',
    nl='''Maar men wil dat Oropeza voor Cogolludo, voor Melgar en voor Balbaces ook noch spreken sal: voor Cogolludo, om
alsdan Melgars Vader te contenteren, de soon doch na Romen te senden en hem [886] de wegh na Napels te senden; voor
Melgar, soo het eerste niet aengaet; en voor Balbaces, soo de [?beyde] niet aangaan, om hem te esloigneren.''',
    en='''But it is intended that Oropesa shall also speak for Cogolludo, for Melgar and for Balbases: for Cogolludo, so as
then to content Melgar's father, yet to send the son to Rome and [886] to send him the way to Naples; for Melgar, if the
first does not come off; and for Balbases, if [?both] do not come off, to get him away.''',
    notes='''- 886 carries a mark not settled (1:886 arghlistigh, 8:886 give no sense).
- 2:750 beyde: the mark over 750 read as a tilde; 8:750 nodigen gives no sense.
- Cogolludo, Melgar, Balbaces and Oropeza are spelled out in cipher letters.''')

P['1687-03-13b'] = dict(
    title='Battier to Fagel, Madrid, 13 March 1687, second letter (scan 55R)', tok='s055R_r2n.txt',
    extra='Continues the 55L block (WAINUT, wainut/r24_1687/tokens/s055L.txt: "... en by den Amb. v. Venetien en"). No contemporary decipherment.',
    nl='''(…) seght de Keyserinne dat er daarnaar weynigh aan gelegen is, of Spaigne, die doch in soo slechten Staat is,
sich daarmede [888] of niet; maar om de consequentie wille sal sich Spaigne daar toe niet brengen laten.''',
    en='''[...] the Empress says that it matters little whether Spain, which is in any case in so poor a state, [888] itself
with it or not; but for the sake of the consequence Spain will not let itself be brought to it.''',
    notes='''- 2:888 is a blank row in the key (scan 16R2); a verb such as bemoeyt is expected. 15:513 weynigh and 15:683 wille
  carry the reversed-c mark.''')

P['1687-06-10'] = dict(
    title='Battier to Fagel, Madrid, June 1687 (scan 67L)', tok='s067L_r2n.txt',
    extra='The 67R passages are WAINUT\'s (wainut/r24_1687). No contemporary decipherment.',
    nl='''(…) men is sooals verdrucken aan alle kanten, dat men self niet tegen de onderdanen met sak en pak [?tesmogneren]
kan, en daarom (…)''',
    en='''[...] one is as it were oppressed on all sides, so that one cannot even [?bear witness] against the subjects with
bag and baggage, and therefore [...]''',
    notes='''- The letters after 11:212 (met sak en pak) spell t-e-s-m-o-g-n-e-r-e-n; perhaps te(s)moigneren; not settled.
- 13:377 verdrucken: the struck third digit is faint.''')

P['1687-07'] = dict(
    title='Battier to Fagel, Madrid, July 1687 (scan 69L)', tok='s069L_r2n.txt',
    extra='Supersedes the r2j draft (tokens/s069L_r2j_draft.txt): l. 3 re-read (843 struck, 925 with the bar). No contemporary decipherment.',
    nl='''Van dagh worden des Conings gedachten dat men namentlyke met dese declaratie niet konde te vrede zyn, en in
Engelandt moste aanhouden om aangemoedight [e] en met de articulen van de Indien overeenkomen de explicatie te hebben,
aen S. Keyserl. (…)''',
    en='''Today the King's thoughts are [...] that one could namely not be content with this declaration, and must insist in
England, to be encouraged [e] and to agree with the articles of the Indies, to have the explanation, to His Imperial
[Majesty] [...]''',
    notes='''- A stray cipher letter 6 (e) stands after aangemoedight.
- 11:843 de Indien: the struck digit is the middle one on the scan, but 12:843 (trevis) gives no sense; taken as block 11.''')

P['1687-08'] = dict(
    title='Battier to Fagel, Madrid, August 1687 (scan 73R)', tok='s073R_r2n.txt',
    extra='No contemporary decipherment.',
    nl='''(…) en [?de] Hofmeester seer veranderlyke is, veeltyts moeyte [?g] hebben sich te mainteneren, soo de heeren
Iesuiten haar werk hier niet van maken.''',
    en='''[...] and [?the] Hofmeister is very changeable, [he will] often have trouble maintaining himself, if the
Jesuit fathers do not make it their business.''',
    notes='''- 90 carries a backslash-like mark (3:90 is not in the key transcription); de taken.
- A single cipher letter 92 (g) stands between moeyte and hebben.''')

P['1687-09-11'] = dict(
    title='Battier to Fagel, Madrid, 11 September 1687 (scan 78R)', tok='s078R_r2n.txt',
    extra='Two cipher runs. No contemporary decipherment.',
    nl='''(…) en worden noch [260] [117] [?geslagen] en [779] de Paltz [60].

Daer is (…) en dat self s[?de] president v. Castille en den Connestable v. Castille, die hem meest tegen waeren, nu
voor [?h]em spreken; Jae men seght dat, sint Spaigne op de soon van Paltz denckt, eenige na Brussel geschreven hebben
(…)''',
    en='''[...] and [260] [117] are still [?struck] and [779] the Palatinate [60].

There is [...] and that even the President of Castile and the Constable of Castile, who were most against him, now speak
for him; indeed it is said that, since Spain is thinking of the son of the Palatine, some have written to Brussels [...]''',
    notes='''- First run (9 groups): 4:260 gedissipeert, 11:117 noemen, 1:779 allyckewel and 8:60 minnaar give no sense; marks not
  settled. Not read.
- 'iem' (40 19 88) for hem: 40 is i in the letter table.''')

P['1687-09-25'] = dict(
    title='Battier to Fagel, Madrid, 25 September 1687 (scan 80R)', tok='s080R_r2n.txt',
    extra='Four cipher runs with clear text between them (read on the scan). No contemporary decipherment.',
    nl='''(…) verwachte brieven van Weenen en de Paltz tarderen, en (…) een wenck gegeven, dat soo den Keyser voor den
soon van Paltz den Coninge [?aanspraak] en Paltzgraaf [894] [9x9] eenighe aangenaam voorslagen dede, Spanien licht daer
toe resolveren soude. (…) Oock is nu weder heel en al stil van de komste van de Hr. Hartogh van Medina Celi;
[?president v. Castille] hebben de [432] aan Syne Majesteyt dat [422] Hertogh van Medina Celi door een poort inquam, hy
soo voort een andere wilde uyttrecken: want anders niet als confusies en continuele menées souden gemachineert worden
als allebeyde [379] Madrid [756]. Oock is weyniger apparentie als ooyt, dat men (…)''',
    en='''[...] expected letters from Vienna and the Palatinate are delayed, and [...] a hint given that, if the Emperor made
the King [?an approach] for the son of the Palatine and [the] Count Palatine [894] [9x9] some agreeable proposals, Spain
would easily resolve to it. [...] Also, all is quiet again about the coming of the Duke of Medinaceli; [?the President of
Castile] [432] to His Majesty that [422] if the Duke of Medinaceli came in by one gate, he would at once go out by
another: for nothing but confusion and continual intrigues would be contrived [if] both [379] Madrid [756]. Also there is
less likelihood than ever that one [...]''',
    notes='''- Struck groups 77 (L01) and 46c^ (L03) omitted, as Battier struck them.
- Open: 894, 9x9 (smudged), 432, 422 (10:422 gepractiseert), 379, 756; 1:349 aanspraak doubtful; 11:794 with the
  struck first digit doubtful; 'hebben' (5:880) does not agree with a single subject.''')

P['1687-12-18'] = dict(
    title='Battier to Fagel, Madrid, 18 December 1687 (scans 93R, 94L)', tok='s093R_r2n.txt and tokens/s094L_r2n.txt',
    extra='Clear text between the runs read on the scan. 94R ll. 1-5 are WAINUT\'s; 94R after l. 5 is a separate entry. No contemporary decipherment.',
    nl='''Myn Heer. Den grand maistre heeft voor 8 daghen met de Italianse post van [888] [oa] aan syn agent en Don Pedro
Alvares, die in syn naem de eerste tentative hadde gedaan, en door den Hr. Dn. M. de Lira tot antwoort bekomen, dat als
de propositie van den Keyser gedaan wierde, S. Mt. alsdan de saecke in consideratie wilde nemen, geschreven dat syn
doorluchtigheit, nadat syn regiment i[n] winter quartier soude hebben genomen, per post na Weenen wilde [178] en [?den
Keyser] soecken daer toe te disponeren.

Maer met de laetste Vlaenderse post heeft men vernomen, dat sd wel te Weenen was [883], maar sich wat onpasselick
bevont, en daarom den Keyser nae Presborgh niet hadde kunnen volgen, [?soo] dat sd eerst met de naeste post soude nader
schryven.

En omdat men schryft dat den Hr. Marckgraef van Baden tot principalen Keyserl. Commissaris na Regensburg gedestineert is,
soo wort gelooft dat den grandmaistre met het gouvernement van de Nederlandt en traineet, om eerst te sien of [?den
Keyser] niet de presidence van de krygh s raadt aan sd wil opdragen; want men twyffelt of sd de selve voor het gouvernement
van de Nederlandt en sal preferéren. Niettemin is noch [212] of Syne Majesteyt [256] en [?wachten] of [e] sich selven,
ondertussen de Hr. Melgar, Leganez, of iemand anders tot Successeur van de Hr. Gastañaga destineren sal.''',
    en='''Sir. Eight days ago, by the Italian post, the Grand Master wrote from [888] [oa] to his agent Don Pedro Alvares, who
had made the first attempt in his name and had received as answer from Don M. de Lira that, if the proposal were made by
the Emperor, His Majesty would then take the matter into consideration, that His Highness, after his regiment had gone
into winter quarters, would go [178] by post to Vienna and seek to dispose [?the Emperor] to it.

But by the last Flanders post one has learnt that His Highness was indeed at Vienna [883], but found himself somewhat
unwell, and therefore had not been able to follow the Emperor to Pressburg, [?so] that His Highness would write more
fully by the next post.

And since it is written that the Margrave of Baden is destined as principal Imperial Commissioner to Regensburg, it is
believed that the Grand Master is dragging his feet over the government of the Netherlands, to see first whether [?the
Emperor] will not entrust the presidency of the war council to His Highness; for it is doubted whether His Highness would
prefer it to the government of the Netherlands. Nevertheless it is still [212] whether His Majesty [256] and [?waits]
whether [e] himself, meanwhile [whether he] will destine Melgar, Leganés or someone else as successor to Gastañaga.''',
    notes='''- sd = S.D. (syn Doorluchtigheit), spelled in cipher letters. 'onpasselick' and 'traineet' as the letters give them.
- Open: 888 (with mark) and the letters o a after it; 178; 883 (2:883 blaakt); 212
  (2:212 beladen); 256 (2:256 beloert).
- [?den Keyser]: the groups read 4:447 and 4:448 (both 'idem' in the key); 4:446 den Keyser, the row above, fits both
  places; a misread or a slip, not settled.
- 12:409 syn (read 489 on the scan in three places: Battier's 0 and 8 run together; the key has 12:409 syn, confirmed by
  the 32R contemporary list).''')

P['1687-12-18b'] = dict(
    title='Battier to Fagel, Madrid, 18 December 1687 (scan 94R after l. 5)', tok='s094R_r2n.txt',
    extra='No contemporary decipherment.',
    nl='''(…) aan haar rage abandonnére en is daar op [406] [?bekraghtigen] van [706] des heer schonenbergs [238] de meeste
oorsaak is dat men niet alleen geordonneert heeft [116] en [653] [724] e [?geimagineert] te k offe na [312] van saken te
doen euaderen maar ook in toekomende aan alle andere [830] introduceren. Het welck ick dan aan de selve in antwoort hebbe
te wete gedaan.''',
    en='''[...] abandon to their rage, and is thereupon [406] [?confirm] of [706] of Mr Schonenberg [238] the main cause is
that one has not only ordered [116] and [653] [724] [?imagined] [...] [312] of affairs [...] but also in future to
introduce to all others [830]. Which I then let them know in reply.''',
    notes='''- Decoded, not read: 406 (6:406 incommodabel), 706 (11:706 soberheyt), 238, 116, 653, 724, 312, 830 give no sense;
  'te k offe na' and 'euaderen' are letter runs without a settled word.''')

P['1688-01-01'] = dict(
    title='Battier to Fagel, Madrid, 1 January 1688 (scan 95R)', tok='s095R_r2n.txt',
    extra='No contemporary decipherment.',
    nl='''Ick hebbe niet kunnen vernomen wat den grandmaistre met dese post [861] heeft, want de Heylige daghen hebben belet
dat men elckeen niet heeft kunnen spreecken.''',
    en='''I have not been able to learn what the Grand Master [861] by this post, for the holy days have prevented one from
speaking to everyone.''',
    notes='- 861 with the struck first digit: the key row (scan 59R2) is not legible on the crop.')

P['1688-01-29b'] = dict(
    title='Battier to Fagel, Madrid, January 1688 (scan 99L)', tok='s099L_r2n.txt',
    extra='Scan 99 (not downloadable in r2j) was the b17 copy. Three cipher runs; clear text between them read on the scan. No contemporary decipherment.',
    nl='''(…) dat ick niet van 60m ponden Vlaems maer wel van 60m guldens hebb geschreven, [i] welk ook de waerheyt is.
Ick wist wel dat den Biechtvader van S. Mt., de welcke voor desen met den Bisschop heeft gestudeert, en syn goede vrint
is, neuens bottello en carnero het meeste daer by hebben gedaan; dat noch den Raet van Staet, noch den Raet van
Vlaenderen in haer consulte aan S. Mt. van 't gelt gheen mentie hebben gemaeckt, en dat mootereye gelyk men b heeft [886]
voor sich heeft [688] Spargement, maar [878] ick voor een [214] van [?Syne Hoogheyt] [?bekraghtigen] consideratie [154]
te [980].''',
    en='''[...] that I wrote not of 60 thousand pounds Flemish but of 60 thousand guilders, which is also the truth. I knew
well that the King's confessor, who formerly studied with the Bishop and is his good friend, [and] Nuñez Botello and
Carnero had done the most in it; that neither the Council of State nor the Council of Flanders made any mention of the
money in their consulta to His Majesty, and that Monterey(?) [...]''',
    notes='''- Decoded, not read as a whole: the third run (33 groups) has 886, 688, 878, 214, 154, 980 without sense; runs 1-2 read.
- neuens bottello, carnero, mootereye as the letters give them (Nuñez Botello? Carnero; Monterey?).''')

P['1688-02-26b'] = dict(
    title='Battier to Fagel, Madrid, 26 February 1688 (scan 102L)', tok='s102L_r2n.txt',
    extra='A faint interlinear decipherment of the time stands over both runs; only scattered words are legible (dan, Biechtvader, Theatin, Grand Maistre).',
    nl='''(…) soo veel weet ick voor seecker dat [?die] Hertogh van Holsteyn aan [420] opesa [335] [499] Biecht-Vader een
Theatin (…) eerst eenige conferentien met de [114] ministers over dit [603] moste [800] welsprekende sonder twyffel is
van wegens de [505] van de grandmaistre, en dat hy in weynigh dagen een antwoort geven soude.''',
    en='''[...] so much I know for certain that [the] Duke of Holstein to [420] [Or]opesa [335] [499] confessor, a Theatine
[...] first some conferences with the [114] ministers about this [603] must [800] eloquent without doubt is on behalf of
the [505] of the Grand Master, and that he would give an answer within a few days.''',
    notes='''- Decoded, not read: 420, 335, 499, 114, 603, 800, 505 without sense; the interlinear is too faint to supply them.
- 2:825 Biecht-Vader agrees with the interlinear 'Biechtvader'; the letters 31 25 6 2 31 7 32 'theatin' with 'Theatin'.''')

P['1688-03-11'] = dict(
    title='Battier to Fagel, Madrid, 11 March 1688 (scan 103R)', tok='s103R_r2n.txt',
    extra='Three short cipher runs; clear text read on the scan. No contemporary decipherment.',
    nl='''Men heeft my gisteren willen doen geloven dat het met den grandmaistre weder af is, dat den Graef van Melgar nu oock
een somme gelt offereert, en dat daerom den Hertogh van Holsteyn desisteert, als vreesende niet te obtineren, maer omdat
oock geseyt wordt, dat den Spaansen Amb.r tot Lissabon met Mr. Novelly correspondeert en voorstelt aan den prins Charle
het Grand Maisterschap te cederen, of voor den Grand Maistre dan dispensatie van de Paus te eysschen om de Infante te
trouwen, en hem het gouvernement van de Nederlandt op te dragen, soo kan ick U Wel Ed. Gestr. noch niet eygentlick
seggen, wat van beyden waer is.''',
    en='''Yesterday I was given to believe that it is off again with the Grand Master, that the Count of Melgar is now also
offering a sum of money, and that the Duke of Holstein therefore desists, fearing not to obtain it; but since it is also
said that the Spanish ambassador at Lisbon is corresponding with Mr Novelly and proposing to Prince Charles to cede the
Grand Mastership, or else to ask a dispensation from the Pope for the Grand Master to marry the Infanta, and to entrust
him with the government of the Netherlands, I cannot yet tell Your Honour exactly which of the two is true.''',
    notes='- All 30 groups decode; 4:471 Hertogh van Holsteyn (caret).')

for doc, d in P.items():
    head = HDR.format(tok=d['tok'], extra=d['extra'])
    (D / f'{doc}_reading.md').write_text(
        f"<!-- {head} -->\n\n# {d['title']}\n\n## Reading\n\n{d['nl']}\n\n## Notes\n\n{d['notes']}\n", encoding='utf-8')
    (D / f'{doc}_en.md').write_text(
        f"<!-- English translation of readings/r2n/{doc}_reading.md (Claude Opus 5.5, 23 Oct 2026, batch r2n). Same holes; modern spelling. -->\n\n"
        f"# {d['title']}\n\n## Translation\n\n{d['en']}\n", encoding='utf-8')
    print(doc)
