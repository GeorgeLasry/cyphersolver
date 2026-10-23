"""b17: write the run-by-run alignment tables for brulart1615 R2785 and R2786 (cipher run, figures as read on the
DECODE images, the contemporary interlinear decipherment, the check against Tomokiyo's key, the reading).

    python research/reading_audit/b17_brulart_align.py
"""
import pathlib
OUT = pathlib.Path(__file__).resolve().parents[2] / 'targets' / 'brulart1615' / 'texts'
HEAD = 'run\tfolio_row\tfigures_as_read\tcontemporary_decipherment\tkey_check\treading\n'

R2785 = [
    ("1", "83r r7", "81, 4pm ꝭ ʜ ft ö 5m p2'r 18, 10 l j", "mon oncle le Duc de Savoye prenoit conseil", "81=mon; ö=duc de Savoye; 18=con (conseil)", "mon oncle le duc de Savoye prenoit conseil"),
    ("2", "83r r7", "10, πxbyꝺgꝭ", "de revanche", "figure read 10 (bien) under the decipherer's 'de' (20=de expected); decipherment followed", "de revanche"),
    ("3", "83r r8", "20̄ 5̄ ꝺb67,q | 20, | ce | 5ff πʃʃ ft | 97, | πʒq91,xff j ʃʃq | la | ʒπʜjft", "se prevaloir de pretexte pour renouveller querelle", "20̄=se; 5̄=pre (prevaloir, pretexte); 20,=de; 97,=pour", "se prevaloir de ce pretexte pour renouveller la querelle"),
    ("4", "83r r9", "4, 7̄ ʜ j ft tto 10tto 85, ꝭ35, 97, 2'pntt x2'xffqTLq", "autre quelles raisons nous en pourrions divertir", "7̄=que, ʜ j=l l, ft=e, tto=s: quelles; 35,=en; 97,=pour; 4 (not in the key) under 'autre' (6=autre)", "[?autre] quelles raisons nous en pourrions divertir"),
    ("5", "83r r10", "30, ꝑεε 35, ꝺff", "estre offensee", "30=est; ꝑ εε = o ff; 35=en", "estre offensee"),
    ("6", "83r r10", "11, 7̄ 85, f91, tt", "bien que nous tous", "7̄=que; 91=ou (tous); 85 nous (decipherer; not in the key)", "bien que nous tous"),
    ("7", "83r r11", "(clear words, partly struck through, before 'faict')", "-", "struck letters read with doubt", "[?scaurions] [?presser]"),
    ("8", "83r r14", "ꞇbʜf x13ꝺ bgꝑ ꝭgffft tt", "tant d'accroches", "not checked sign by sign", "tant d'accroches"),
    ("9", "83r r15", "q̈ 20, ꝺff ʃvʜ | du | ʜguxfiqʒʃff bq 20, ʒ2'ꝭʃʒ | 8̄", "du duc de Mantoue de celuy du gouverneur de Milan qui", "q̈=duc de Mantoue; 20,=de (twice); 8̄=qui", "du duc de Mantoue [et] de celuy du gouverneur de Milan qui"),
    ("10", "83r r16", "7̄ 7̄ c2'lε2'ʌvʜfff 20, 20̄ ʃʃp2'mxπ 9,π π81,ttgBmꝺʃʃtt", "quelque difficulte de se joindre aux remonstrances", "7̄=que (twice); 20,=de; 20̄=se", "quelque difficulte de se joindre aux remonstrances"),
    ("11", "83r r18", "35, ꝭpπtt | ce | 8̄ 97B | sur | ꝭffʃB bgg2'vffq 20, ʃb wBgT 20, | mon", "en cores qui pourra cela arriver de la part de", "35,=en; 8̄=qui; 97=pour; 20,=de (twice); w B q T = p a r t", "encores ce qui pourra sur cela arriver de la part de mon"),
    ("12", "83r r19", "ꝭ ʃtt ö 20, ffbq ꝭp2'q la 18,T2'm vB 30̄ 20, 74tt fBꝏqfB #̄0", "oncle le duc de Savoye de surseoir continuation de mes exhortations", "ö=duc de Savoye; 18=con, 30̄=tion (continuation); 20,=de; 74=me +s (mes)", "oncle le duc de Savoye, de surseoir la continuation de mes exhortations"),
    ("13", "83r r20", "30̄tt | et | ꝑεε2'ꝭftt | envers les | obqT2fftto | tant | wBq", "offices partys par", "30̄=tion+s; ꝑ εε 2' ꝭ ft tt = o ff i c e s; w B q = p a r", "[exhorta]tions et offices envers les partys tant par"),
    ("14", "83v r1", "5̄ꝺpʜBmꝭff | 8̄ ʃtt | soyent | 2'mεqvꝺꝭrꝺffxπ | qui | w91,q", "prevoyance quilz Infructueux pour", "5̄=pre; 8̄=qui + l s; ε=f, q=r, π=x; 91=ou (pour)", "prevoyance qu'ilz soyent infructueux qui pour"),
    ("15", "83v r2", "2'xʃfq | a propos en | ꝭz2'ꝭft 18,2'ttpm ꝭrvπ 20, y2' 35, xφaꝭgʈtttto", "Juger [?] conioncture de my embarasser", "18=con; 20,=de; 35,=en (em-)", "juger a propos en [?ceste] conioncture de m'y embarasser"),
    ("16", "83v r3", "ꝭq | davantage apres | 3̄,π 10, π vttton | en la | 5̄ʔ2'ftπ 8̄ʃp ʃʃ2'B30̄", "avoir si bien reussy premiere negociation", "10,=bien; 5̄=pre; 30̄=tion", "avoir si bien reussy en la premiere negociation"),
    ("17", "83v r4", "tt ꝭBq2'mʜ 20 se π2'ʒ2'q B ʔttʒtt", "sieur marini de retirer a Gennes", "B=a q=r 2'=i m=n (Marini); 20=de", "sieur Marini de se retirer a Gennes"),
    ("18", "83v r5", "ttgu,tt ꝭgu ʃff bq 20, 20̄tt | affaires | xpyffʈ2'7̄tt 97, 84, 25, 8̄q", "soubz couleur de ses domestiques pour ne donner", "20,=de; 20̄+s=ses; 7̄=que; 97=pour; 84=ne", "soubz couleur de ses affaires domestiques pour ne donner"),
    ("19", "83v r6", "Bvꝭ xyη ʒmꝗ gB ʃtt φ", "aucun ombrage", "φ = delete sign", "aucun ombrage"),
    ("20", "83v r9", "y81, wptttto2' ... ꝭʃ ʔgtt 20, oqwφ ttwʔꝑtt", "m'est possible / [?lors] de [?propos]", "20,=de; the rest not carried", "[?m'est possible] [...]"),
    ("21", "83v r10", "20̄ wBtttto36, 35, ʔ91,xqBʃtt | 31,Bmʈ | ttꝺttwʃf", "se passent en l'Equidray estant suspect", "20̄=se; w B tt tto 36 = p a s s ent; 35,=en; 31=est + a n t", "se passent en [?l'Equidray], estant tousiours suspect"),
    ("22", "83v r11", "f 7̄ ηBq2'm 5̄ 84, wbqT bꝺ8 21,tt η91,ꝺffη80̄ittt 8̄ 93, 81,tt y 20, ꝺ", "que Marin prenne par ausdictz mouvemens qui ont este [?]", "7̄=que; η B q 2' m = M a r i n; 5̄ 84 = pre ne; 21=dict+s; 91=ou; 8̄=qui; 93=ont", "que Marin prenne par ses dictz mouvemens qui ont este [...]"),
    ("23", "83v r12", "ʒʃ | volontiers | ꝭ##ꝑη36, ftv wbq suy tto91,αtt fttwp2'q x35,", "fomentez par soubz [?] d'en", "36=ent; w b q = p a r; 91=ou (soubz); x=d 35=en", "[...] fomentez par [...] soubz [...] d'en"),
    ("24", "83v r13", "ꝗ#ꝑεε2'Tfq", "proffitter", "ꝗ=p #=r ꝑ=o εε=ff 2'=i T=t q=r", "profitter"),
    ("25", "83v r17-18", "θ ꝝ ꝗ tt tto o p u ꝺ L g ꝗ A a c g θ / b ƃ ꝝ ꝝ#ꝑ ꝛ ct θ ä ƃ̈ s̈ ꝺ ꝭ Ꞵ u tt tt ċ ⁚ ꝺ tt ꝺ tt θ", "(none)", "no French under the key; θ null, φ delete; Tomokiyo: probably nulls", "[...]"),
    ("26", "84r r2", "b ƃ ꝝ ꝝ# ct ꝛ to b ƃ ε ꝛ̈ o g g ₤ ʜ ʜ tt ʃʃ g g ʜ ʜ ʜ", "(none)", "no French under the key; doubled signs; probably nulls", "[...]"),
]

R2786 = [
    ("1", "109r r19", "ꝝ φ 23,", "d'un", "23 = du in the key; decipherer 'd'un'", "d'un"),
    ("2", "109r r20", "ʒꝗbttoψbʔff | 7, 7̄ i | 72,tt | c ꝁ 2' 4 41̄ | 3, | π ʔ g", "passage auquel ilz doibvent avoir regard", "7,=au 7̄=que + l (auquel); 72=il+s; 41̄=uent; 3=avoir", "passage auquel ilz doibvent avoir regard"),
    ("3", "109r r21", "ff f 20, 20̄ꝁʃʃqʔ 21̄ 7,bmT 35,ʔ6ʔ₣λ θ", "de [?sicher] si avant engagez", "20,=de; 20̄=se; 21̄=si; b m T = a n t; 35,=en, ʔ 6 ʔ ₣ λ = g a g e z; θ null", "de se [...] si avant engagez"),
    ("4", "109r r22", "θ | 97, ꝭ ʔ", "pour le", "97=pour; θ null", "pour le"),
    ("5", "109v r7", "to 71, ƃ 5̄ 20̄ m ʃʃ | λ φ ƃ ꝝ x b q ʔ 36, c 60, tto ₮T 20, π ꝗ ʃ ...", "jusques a present d'argent d'hommes et de reputation", "71=jusques; ƃ=a; 5̄=pre 20̄=se m=n ʃʃ=t; x=d b=a q=r ʔ=g 36=ent; 60=homme+s; 20=de", "jusques a present d'argent, d'hommes et de reputation"),
    ("6", "109v r8", "ꝁ b 2' m 18, ✕ ff m L 36, tt θ 16, 21 ꝭ ₤ b i ψ", "Incomoditez", "2' m 18 ✕ ff m L 36 tt = i n con v e n i ent s: inconvenients (the figures followed, not the decipherer); 16 car, 21 dict not glossed", "[...] inconvenients [16] [21] [...]"),
    ("7", "109v r9", "ꝁ ± f θ 8̄ 7̄, ʔ 75, ff q 93, 20, ʃʃ 91, f ff tto", "qui augmenteront de toutes", "8̄=qui; 75=ment; 93=ont; 20=de; ʃʃ 91 = t ou (toutes)", "qui augmenteront de toutes"),
    ("8", "109v r10-11", "λ ψ θ σ B g ꝭ ƃ 18, T L m χ b ꝭ ± ꝁ m 20, i b 54, ff ʃʃ θ", "par la continuation de la guerre et", "18=con; 20=de; i b = l a; 54=guerre; ff ʃʃ = e t, θ null", "par la continuation de la guerre et"),
    ("9", "109v r11", "35, 74, tt 74, 29̄ y ꝗ tto", "(none)", "35 en, 74 me, tt s, 74 me, 29̄ te, y m, ꝗ p, tto s: en mesme temps (decoded here)", "en mesme temps"),
    ("10", "109v r12", "θ (before clear 'perdent')", "-", "θ null", "-"),
    ("11", "109v r21", "ξ φ ꝁ A 5̄ dL ꝭ 35, 29̄ m c ꝗ ʃʃ T 7, ꝭ π 75,", "l'Intention aulcunement", "35 en 29̄ te m n (intention, partly); 7=au ... 75=ment (aulcunement)", "[...] l'intention [...] aulcunement"),
    ("12", "109v r22", "ꝁ ƃ θ | je vous asseure | θ ct b ꝁ 74, 31̄ ꝗ L", "a me [?]", "74=me; the rest not carried", "je vous asseure [...] a me [...]"),
    ("13", "109v r23", "ꝭ 10, x2'εψffπmχ | Je | φ | et vous | φ x", "bien differend", "10=bien; x=d 2'=i ε=f (differend)", "bien differend. Je [...] et vous [...]"),
    ("14", "110r r1", "laisse | φ ƃ̈ 6 a[?] φ 4 ꝁ 35 22̄ 35, 22,", "en son endroict", "35=en 22̄=son 35,22,=en droict", "laisse [...] en son endroict"),
]

for name, rows in (('R2785', R2785), ('R2786', R2786)):
    with open(OUT / f'{name}_align.tsv', 'w', encoding='utf8', newline='\n') as f:
        f.write(HEAD)
        for r in rows:
            f.write('\t'.join(r) + '\n')
    print(name, len(rows))
