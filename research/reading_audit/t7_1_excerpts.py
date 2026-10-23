"""v7 translate list 1: write Lasry-excerpt readings and English for the external-pointer entries (23 Oct 2026).

Each reading is the excerpt text of lasry_entry.md copied verbatim (his marks kept: [?] unread, [x] supplied, ? a
sign he leaves open); the English is ours, sentence for sentence, with the same holes.
    python research/reading_audit/t7_1_excerpts.py
"""
import pathlib
R = pathlib.Path(__file__).resolve().parents[2] / 'targets'

HEAD_R = ("# {title}: Lasry's excerpt\n\n"
          "George Lasry's reading, as excerpted in his BnF cipher research report (`lasry_entry.md`, copied verbatim). "
          "Written out 23 Oct 2026 (translation wave v7): **an excerpt only**; his full transcription and decryption are his "
          "and not in the repository. Excerpts, in order: {where}. Marks are his: [?] or ? unread, [x] supplied.\n\n## Reading\n\n")
HEAD_E = ("# {title}: English translation of Lasry's excerpt\n\n"
          "Translation (Claude Opus 5.5, 23 Oct 2026) of `lasry_excerpt_reading.md`, **an excerpt only** of the letter, "
          "the passages George Lasry printed in his BnF cipher research report ({where}); the rest of the letter is not in "
          "the repository. Same holes: [?] unread, [x] a word he supplied. His own translation is in `lasry_entry.md`.\n\n"
          "## Translation\n\n")

T = {
 'fr3321dc': dict(title='BnF Français 3321, f. 103r, letter signed DC, 20 May', where='f. 103r, first four lines', rd=[
  "Les affaires sont en tel termes qu'infalliblement la Ruyne de Espernon s'en ensuivra, ou de cest estat. Car l'union est si forte qu'elle peult mieux donner la loy que la recepvoir. Demain la req[ueste] s'en doibt partir, vous en aurez Incontinent la coppie Comme on vous envoye du reste."],
  en=["Affairs stand on such terms that the ruin of Épernon will infallibly follow from them, or the ruin of this state. For the union is so strong that it can better give the law than receive it. Tomorrow the pe[tition] is to leave; you will have the copy of it at once, as the rest is being sent to you."]),
 'fr3575f56': dict(title='BnF Français 3575, f. 56r, unsigned letter on Clermont', where='f. 56r, lines 7-13 (two overlapping excerpts, joined here) and lines 19-22', rd=[
  "…pas dans sa lettre et pretend ne povvoir obeir. Vovs scaves de qvelle importance est Clermont et ez [m]ains de qvi il entrera. C’est à vovs, Monsievr, à y povrveoir, ce qve vovs povvez faire librement car vovs estes av dessvs de l’envye, et ne me mettre en bvtte parce qve cela me rvineroi[t] envers cevx de la religion. Il i a avssy vn afa…",
  "[…]",
  "[b]on essient. C’est à vovs à adviser sy vovs lvy vovlez procvrer ce bien car ie tiens qv’il en est digne et ce cera chose profitable av service dv roy, à vovs et à moy."],
  en=["…not in his letter, and claims that he cannot obey. You know of what importance Clermont is, and into whose [h]ands it will pass. It is for you, Sir, to see to it, which you can do freely, for you are above envy; and not to make me a target, because that would rui[n] me with those of the religion. There is also a mat…",
  "[…]",
  "in [g]ood earnest. It is for you to consider whether you will obtain this favour for him, for I hold that he is worthy of it, and it will be a thing profitable to the King's service, to you and to me."]),
 'fr4696num': dict(title='BnF Français 4696, ff. 54r-55r, numerical cipher letter, 1589?', where='f. 55r, full cipher lines 1-6', rd=[
  "Piu sobria sara V.Ecc. nel scriuere in Italia, masime in modo che posi risapersi tanto. Sara meglio l’auuisare il serenisimo signor duca di Mantua frequentemente et per uia sicura de i sucesi di Francia. Sara sopra modo grato a S.A. a quale et a V.Ecc. tornara molto a conto."],
  en=["Your Excellency will be more sober in writing to Italy, especially in a way that it could become so widely known. It will be better to advise the Most Serene Lord Duke of Mantua frequently, and by a safe way, of the events of France. It will be exceedingly welcome to His Highness, and will turn greatly to the account of him and of Your Excellency."]),
 'gondi1594': dict(title='BnF Français 4700, ff. 9r-10r, Girolamo Gondi to the duke of Nevers, 15 May 1594', where='f. 9v, rows 10-13', rd=[
  "luogo di queste parti doppa la reductione di parigi non abbiamo auto qui alcuna lettere di monsieur di reuol ne daltri ne fatta alcuna dimostratione di ralegramento con noi et si ua dubitando che si sia stato fatto qualche cattiuo uffitio da"],
  en=["place in these parts. Since the reduction of Paris we have had here no letters from Monsieur de Revol nor from others, nor has any show of rejoicing been made with us, and it is being suspected that some bad office has been done by"]),
 'herbault1625': dict(title="BnF Français 3944, f. 99r, d'Herbault to Bullion, 29 July 1625", where='f. 99r, three complete cipher rows', rd=[
  "croions que les forces presentes des [Ennemis] et les considerations de M. de Savoye pour la conservation de ses estats nous imposeront une loy assez absolue pour ce regard"],
  en=["[we] believe that the present forces of the [enemies] and the considerations of Monsieur de Savoie for the preservation of his states will impose on us a law absolute enough in this regard"]),
 'jeannin1607': dict(title='BnF Français 3516, f. 86r, Villeroy / Henri IV to Jeannin, 1607', where='f. 86r, cipher lines 8-11', rd=[
  "comme à tous ceux qui affectionnent ceste union, sans toutefois par trop vous fonder ou confier aux belles parrolles de son agent, ny des autres qui penchent de son coste, car ilz sont tous trompeurs. Mais si nous"],
  en=["as to all those who favour this union, without however grounding yourselves too much on, or trusting too much in, the fine words of his agent, nor of the others who lean to his side, for they are all deceivers. But if we"]),
 'laboderie1608': dict(title='BnF Français 3516, ff. 59r-60v, La Boderie to Jeannin, 7 June 1608', where='f. 59v, four full cipher lines', rd=[
  "assez mal fondees, de sorte que tant s’en faut que je me promette rien de bien de ce commerage. J’ai peur qu’il ne produise que du mespris de part et d’autre, et de part et d’autre il semble que on y chemine que par maniere d’acquit."],
  en=["rather ill founded, so that I am far from promising myself any good from this godparenthood. I fear that it will produce nothing but contempt on both sides, and on both sides it seems that people go about it only for form's sake."]),
 'lerouge': dict(title='BnF Français 2971, f. 32r, F. Le Rouge to the Chancellor, 11 July', where='f. 32r, cipher lines 1-3', rd=[
  "… lettres du Roy à Seigneurie n’eussent sceu arriuer à meilleur poinct, aultant qu’elle [e]stoit mal contente apres la demonstration qu’elle auoit faicte pour le roi…"],
  en=["… the King's letters to the Signoria could not have arrived at a better moment, inasmuch as it [w]as displeased after the demonstration it had made for the King…"]),
 'louis1635': dict(title='BnF Français 3758, f. 117r, Louis XIII to Châtillon and Brézé, 30 June 1635', where='f. 117r', rd=[
  "Quand vous m’escriprez quelque chose d’importance souvenez vous que ce soit en chiffre. Car sy la despesche du xviiᵉ fust tombée entre les mains des Ennemis, ilz eussent appris [?] et en eussent tiré ?duantage."],
  en=["When you write me something of importance, remember that it be in cipher. For if the despatch of the 17th had fallen into the hands of the enemies, they would have learned [?] and would have drawn ?advantage from it."]),
 'lucinge1588': dict(title='BnF Italien 2242, Lucinge to the duke of Savoy, 9 and 18 June and 3 August 1588', where='f. 123r, six cipher lines and the clear closing; f. 131v, cipher lines 12-15; f. 132v, cipher lines 3-5; f. 122v, cipher lines 1-5 and 25-28; f. 124r, three cipher lines', rd=[
  "*f. 123r.* Soit qu’à ruiner [?] et en la ruine de cettuy celle de son fils y a esté comprise. [?] J’ay un escrit de [?] touchant les conditions de [?]. Ensemble un billet qui me sert de croyance. Je ne l’ose envoyer par la voye commune. J’attends quelque courrier que [?] m’envoyera pour le luy envoyer bien seurement. Cependant j’en ay voulu retenir ses particularitez, attendant plus sure commodité. Je prieray Dieu de tout mon cœur qu’il donne à V. A.,",
  "*f. 131v.* [l]eur desseing si, par le moyen de [?], de [?], le cardinal Farnese estoit créé pape, et aveq les voix de France y meller celles de Florence, et qu’en cette façon [?] se conduiroit mieux au but de ses prétention, que est de se faire esli[r]e roy, non pas de Toscane mais en Toscane (je ne scay quelle finesse il entend entre ce [?]). Il [v]",
  "*f. 132v.* [?] m’a asseuré que le comte de Soissons n’est point mal avec [?]. Cette princes[s]e de Condé est condamnée d’avoir la géhenne après le temps expiré durant lequel l’on ce do[u]te de sa groisse qu’elle a aleguée. On verra ce qu’il en…",
  "*f. 122v, lines 1-5.* ne veulent accorder. Les Parisiens ont forcé Corbueil et vont assieger Meleun. Ils tienent tous les pons de la riviere de Seine au dessus et dessous Paris. Rouan (dont [?] e[?]t [?] furent bien eastonnés), quand sa Mte y pensa aller, luy prierent de [?] venir pas et que le peuple se mutinoit au bruit qu[?] faisoit qu’il y vouloit fayre entrer ses garde[s]. Il n’y a ville de celles qui…",
  "*f. 122v, lines 25-28.* [Toutes]fois [?] envoya la lettre de sa fille à [?]. [?] la monstra à [?], luy disant : « Madame, si vous nous faisies souvent de ses traicts, vous nous feries penser à des choses que nous ne voudrions pas. » « Quoy, dict elle, vous me voudries tenir prisonniere ? » « Non Madame, nous vous lairrions plustost aller. »",
  "*f. 124r.* u qui perd le plus en cet accord qu'ils traictent mais il semble que [?] estant les ch oses reduictes a ce point et qu'il ne pouuoyt se uenger iacoit qu'il eut eu les moyens sans domage et danger a mieux faict de laisser passe[r] l'orage s'il est re"],
  en=["*f. 123r.* Whether in ruining [?], and in the ruin of this one that of his son has been included. [?] I have a writing from [?] touching the conditions of [?], together with a note that serves me as credence. I dare not send it by the common way. I am waiting for some courier whom [?] will send me, to send it to him quite safely. Meanwhile I have wished to keep back its particulars, awaiting a safer opportunity. I shall pray God with all my heart that He give Your Highness,",
  "*f. 131v.* [t]heir design, if, by means of [?], of [?], Cardinal Farnese were created pope, and to mix with the votes of France those of Florence, and that in this way [?] would make his way better to the goal of his pretension, which is to have himself ele[c]ted king, not of Tuscany but in Tuscany (I do not know what subtlety he means between these [?]). He [w]",
  "*f. 132v.* [?] has assured me that the Count of Soissons is not at all on bad terms with [?]. This princes[s] of Condé is condemned to have the question [torture] after the expiry of the time during which her pregnancy, which she has alleged, is being d[o]ubted. We shall see what of it…",
  "*f. 122v, lines 1-5.* will not agree. The Parisians have forced Corbeil and are going to besiege Melun. They hold all the bridges of the river Seine above and below Paris. Rouen (at which [?] a[?]d [?] were much astonished), when His Majesty thought of going there, begged him [?] not to come, and [said] that the people were mutinying at the rumour [?] was making that he wanted to bring his guard[s] into it. There is no town among those which…",
  "*f. 122v, lines 25-28.* [Never]theless [?] sent his daughter's letter to [?]. [?] showed it to [?], saying to her: “Madam, if you often played such tricks on us, you would make us think of things we would not wish to.” “What,” said she, “you would want to keep me prisoner?” “No, Madam, we would rather let you go.”",
  "*f. 124r.* …r who loses most in this agreement they are negotiating; but it seems that [?], things being reduced to this point, and since he could not avenge himself, although he had had the means without damage and danger, has done better to let the storm pas[s], if he is re…"]),
 'nevers1594gondi': dict(title='BnF Français 3622, f. 91r, the duke of Nevers to M. de Gondi, 27 March 1594', where='f. 91r, four complete body lines', rd=[
  "facent monstre sur les vieu? rooles parce qu’il y va grand perte. Rasseure le Roy qui l’auroit le tout à la fyn d’avril selon que vous me dites. Au demeurant, j’ay despesché aussy ? Asdrubal vers le Corse et eschevyns de Lyon pour l’affaire"],
  en=["[should] hold the muster on the ol? rolls, because a great loss is at stake in it. Reassure the King that he would have the whole of it at the end of April, as you tell me. For the rest, I have also despatched ? Asdrubal to the Corsican and the aldermen of Lyon for the business"]),
 'paleologue1562': dict(title='BnF Français 4687, f. 6r, Marguerite Paléologue (attribution) to the duke of Nevers, 1562-64', where='f. 6r, cipher rows 8-10', rd=[
  "Averia dat volontier a cuatr cento mila scudi per aver cuel stato et pareva ? ascoltase ? parla"],
  en=["[He] would willingly have given four hundred thousand scudi to have that state, and it seemed ? would listen ? speaks"]),
}

MONDESIR_EN = ("# Letter from Mondesir, Isle de France, 20 November 1769 (BnF Français 5581): English translation of Lasry's excerpt\n\n"
  "Translation (Claude Opus 5.5, 23 Oct 2026) of `lasry_excerpt_reading.md`, **an excerpt only**: the three passages George "
  "Lasry printed in his BnF cipher research report (f. 50v; f. 51r; f. 56r, lines 3-6); the rest of the letter is not in the "
  "repository. Same holes: [?] unread, [x] a letter he supplied. His own translation is in `lasry_entry.md`.\n\n## Translation\n\n"
  "even of his own trade; so one is, one may say, ignorant and presumptuous, stubborn as a Lower Breton, which one is; [?] lets "
  "himself be strongly prejudiced, often by the first comer; set in one's ideas, which one has seized promptly and put into "
  "execution without making any reflection or consulting anyone. So one commits many follies, and ordinances which one is "
  "obliged to go back on or leave without effect. [?] is quick to the point of passion and to excess…\n\n"
  "the prohibition on the speculation in the King's bills against piastres, on which one has been obliged to close one's eyes, "
  "as on the taxing of foodstuffs of every kind.\n\n"
  "And if afterwards they will grant me men and money, and I have two years of peace to prepare myself for war, they will see "
  "the difference between [one?] man and another.\n")

if __name__ == '__main__':
    for t, d in T.items():
        (R / t / 'lasry_excerpt_reading.md').write_text(HEAD_R.format(**d) + '\n\n'.join(d['rd']) + '\n', encoding='utf8')
        (R / t / 'lasry_excerpt_en.md').write_text(HEAD_E.format(**d) + '\n\n'.join(d['en']) + '\n', encoding='utf8')
        print('wrote', t)
    (R / 'mondesir1769' / 'lasry_excerpt_en.md').write_text(MONDESIR_EN, encoding='utf8'); print('wrote mondesir1769')
