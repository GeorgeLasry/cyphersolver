"""v7 list 1: English translations of the Kauderbach 1754-55 readings (read/<doc>_reading.md -> read/<doc>_en.md).
    python research/reading_audit/t7_1_kauderbach.py
"""
import pathlib
D = pathlib.Path(__file__).resolve().parents[2] / 'targets' / 'kauderbach1754' / 'read'
H = ("<!-- English translation (Claude Opus 5.5, 23 Oct 2026) of read/{d}_reading.md, the French cipher text of {d} "
     "(Kauderbach, The Hague, {date}). Same holes: [...] an unread code group (mostly name positions), [?] doubtful, "
     "[?word] a doubtful word, [word] a word supplied by the reading. The capital sigla in brackets ([S./.], [Q./.], "
     "[P.], [J./. C./.] ...) are nomenclator names not identified, kept as they stand.{extra} -->\n\n"
     "# {d}, Kauderbach (The Hague), {date}: English translation\n\n## Translation\n\n")
T = {
'R2078': ('23 Dec 1754', '', """There has not been for a long time an assembly of the States of [Holl.] whose subjects of deliberation have been more
important and at the same time more embarrassing for this state. On the one side, the overture made by the Comte
d'Affry presents a thousand thorns, both as to the substance and as to the form of the conferences to be opened with
this pr[...]; on the other side, Colonel Yorke, who does not fall asleep in these circumstances, asks, in a memorial
which he has delivered to [...] and which she then had communicated by [...] to the States of [...], for explanations
on what [?] one may hold to with regard to the engagements which [...] has with [...]. It is on these two matters that
all the deliberations turn. This last step tends to support [?] those which [...] has made in the provinces to avoid
[?] the negotiation with [...], towards which the proposal of [...] of the [.] July was leading, for [?] which the
principal town of [...] and many others with it show an extreme inclination. It has at least served to put the [...]
policy to rout, which wanted to take up a preliminary advice on the mere overture of the Comte d'Affry and have it
carried to the States General, so as to bring about the negotiation with [...] and thus draw overtures from [...].
Even this view has been disconcerted, on the pretext that

the pr[...], still persisting [?] in wanting to treat only by word of mouth, have been obliged to ask for the orders of
their [?court] on this, which they are still awaiting, while requesting commissioners. It is doubtless in the
conferences with these commissioners that the Comte d'Affry will explain his commission more particularly,
conferences at which the Marquis de Bonnac will act and speak as head of the embassy, because the Comte [...] first,
and perhaps for his own interest, represented the propriety and necessity of it to his [court], although his first
instructions did not even allow him to proceed in everything in communication with the ambassador.

Finally they complain that the public has been given the idea that [...] did not want neutrality, but only required
that the state should declare whether it will take sides for or against [...]; and they make it clear enough that the
principal aim is to negotiate a [treaty] of neutrality."""),
'R1958': ('20 June 1755', '', """[here] that if the [Q./.] transport arrives there safely there will be no war in Europe.

[20 June 1755] Colonel Yorke has assured me anew that his court is very well disposed to the renewal of the [treaty,
Y] of subsidy, and that he did not doubt that Monsieur the Comte de Fleming, in whom [E./. P./.] had the greatest
confidence, would take this affair to heart on his arrival at Hanover. He added that here people were as yet neither
cold nor hot, and that he himself, in moments of impatience, felt inclined to the system of the anti-continentists
and to letting things on the Continent go as they [would]; that nevertheless he did not despair that, after the
example of [P./.], people here would follow [...], and that I could be assured that he would second our interests and
my steps here with all his strength when it was time to make them.

the present moment, on the Hanover side, seems the most suitable, while people there are still uncertain of events in
America, all the more as I have found [that people there] are of the idea in which [clear: people generally are]"""),
'R2079': ('6 July 1755', '', """[...] chagrin that no more vigour is shown. Monsieur Haslang writes to the Bavarian resident that he has the Duke of
Newcastle's word that his [Y./.] will be renewed, and that he has not the least anxiety on that score.

The prospects for the augmentation of the [Z./.] diminish from day to day, and there is almost no more hope that it
will take place; but I have strong reasons to believe that it will only be the better for our affairs, because, if
the first were made, the opponents would redouble their difficulties over the renewal of the [Y./.] of subsidies on
the usual pretext of inability, saying, as they already say loudly, that it is impossible to do both at the same time.
What is very astonishing is that the opposition makes not the least impression on the people; events and some degrees
more of fear would be needed to stir them. If it must be one of two things, [those of] Amsterdam will still consent to
the renewal of the [Y./.] rather than to the augmentation, which on their principles is an augmentation of the
Stadtholder's power. Monsieur Yorke is very c[...]"""),
'R2080': ('22 July 1755', '', """The principal reasons alleged in the debates there have been on this subject in the assembly of [S./.] come down in
substance to the following. Firstly, that if the danger with which the Low Countries are threatened is such as Lord
Holderness has made it known here, an augmentation of thirteen thousand men is not sufficient to turn it away.
Secondly, that it must be established before all things whether the danger is real for the Republic, and whether
there are no other means of putting it in safety than this feeble augmentation. Thirdly, that even if [S./.] could,
by means of an actual [?] money negotiation, find the funds for the proposed augmentation, that [?] is not enough, and
one must be sure that the other provinces will contribute to it equally, [S./.] being no longer able to bear the whole
burden alone; that in the state in which the finances of the other provinces are, and namely of Zeeland, Utrecht,
Friesland and Groningen, which on several occasions have gone as far as demonstration to prove their exhaustion, it is
not to be presumed that they will be more exact in furnishing their contingents than in the past, and that [S./.]
neither will nor can make the advances for them any longer. Fourthly, that it is very true that in case of necessity,
where [Q./.] should be bent on attacking the Republic, all good patriots ought to sacrifice to the last sou to fight
pro aris et focis [for hearth and altar]; but that it would first be necessary to come to an explanation with [Q./.]
and see whether there would not be a means of at least putting the Republic under cover. Finally, all the speeches
held on this come back to this: that if [?] all the provinces take a unanimous resolution with a promise to
contribute exactly, and [?] if the danger is real for the Republic, [S./.] are ready to make the last efforts; but
[?] that, since their finances do not allow them to make them from the present funds and revenues of the province, it
will of necessity be required to impose new taxes on the inhabitants and to publish yet another fiftieth penny, each
of the members offering themselves to contribute to the last sou if need be; but [?] that, if there are other means
to keep off a war in which the state has neither interest nor fault [?], they ought to be employed."""),
'R1959': ('5 Aug 1755', '', """The rumour that [E.M.] is in negotiation with [P.] does not seem to be entirely without foundation, and it is asserted
that some steps have really been taken with this prince, who is said to have promised, on certain conditions, to keep
quiet as long as the [J./. C./.] did not stir. The [M./.] partisans, who are very numerous, above all at Amsterdam, do
all they can to give credit to this news, though it is hardly believable. I notice that it greatly intrigues the
ambassador of [Q./.]. The latter has sounded me several times on the dispositions of [J./.] towards a [treaty, Y./.]
of subsidy with his own [court], to which I have constantly replied that I was not instructed, and that we had a
[?minister] in Paris, to whom it was more natural to address himself than to me."""),
'R2081': ('12 Aug 1755', '', """The [P.] are as little satisfied with [J./. C./.] as with the [S./.]. It seems to me that they suspect [U./.] of not
wanting at bottom to embrace [?] these things herself, and that all that has been done so far has been only to show the
[P.] that nothing has been neglected to satisfy them. Yet there are many reasons to believe that it does not depend on
the [...] will of [U./.] that things do not go otherwise, she who finds herself hampered by the situation of her
affairs within and without, and obliged to great caution. I know [?] from a good quarter that some taking up of arms,
or at least some abrupt step on the part of [Q./.], had been expected, which would have [...] the object of the
resolution of [S./.] and supported [?] the proposal of [U./.]; but up to now [Q./.] does not affect [...] and lulls
everyone to sleep by insinuating that she has no designs on the Low Countries, nor even on Hanover. Moreover, one sees
here only fears and difficulties on the part of [J./. C./.]. They say they know positively that Baron Kniphausen
declaims more strongly at Compiègne against the [P./.] than [Q./.] itself. The [Q./.] now themselves contradict the
alleged negotiation with [M./.]; they admit that some attempt was indeed made with that prince three months ago, but
that it did not take; that on the contrary he promised [Q./.] to do for her all he could, but that she would do well
to precipitate nothing and to try all the ways of moderation before [...]. Although the prospects are still little
favourable, people do not yet despair that they may change."""),
'R2082': ('15 Aug 1755', '', """The ambassador of [Q./.] asserts that [E.M./.] has written to the King his master a letter in his own hand to [...] [?]
that he had an army of a hundred and fifty thousand men at his service; and immediately after he added that his
[J./.] was more embarrassed by those who, for their particular interests, were working to kindle war in Europe than by
his declared enemies. The pr[...] [P./.] says loudly that, if people here will not take measures to put themselves in
a state of defence, [P./.] will abandon the Continent, and that she will not sacrifice her certain [?] advantages and
the only decisive occasion to humble [Q./.] to the pitiful conduct of [S./.], which, after having been warned enough,
will get out of the affair as best it can. [U./.] will push the augmentation with the utmost vigour at the next
assembly of [S./.]."""),
'R1044': ('29 Sept 1755', ' The clear phrase quoted inside the cipher is in ⟨ ⟩.', """[nothing ...] but the single reflection that [S.I.] can never have had deliberations more embarrassing than those of
today. One hears nothing but complaints from the members against [P.I.] that they make so many captures in Europe
without giving any reason for them to the public, whence it is believed that [G.I.] may take a pretext from it to fall
in fact on the Low Countries as well. The [M.I.] partisans, who are certainly very numerous, attribute only to this
prince the moderation of [G.] on that side, and it is easy to foresee where this idea will lead if it gains credit
[...] [?and well] in the very [?bitter] complaints which escaped some members in the present deliberations. It was
said that people had ⟨that the interest of the Republic was to be closely bound to England⟩ also act as a friend of
the Republic; that England would act as she had done during the last war, for more than twenty millions of prizes on
the subjects of the State; that this course was already beginning again, and that no mystery was made of threatening
to do more of it in case the State would not march at the pleasure of [P.I.], while so much indifference was shown for
the affairs of the Continent. I have these particulars from the very [...] [...]"""),
'R1043': ('25 May 1756', '', """The news of the negotiation between the [S?] and [?] is no longer a [?mystery] [...] [?three] months. Today there are
certain and positive advices that the [treaty, ÿ %] of which there has been talk for so long was signed at Versailles
on the second of this month; and according to what I have been [?told] confidentially, its object is, firstly, the
neutrality of the Low Countries; secondly, it must be stipulated in it that no power shall give any help to the enemy
of the other, which seems to imply something other than a general neutrality; and thirdly, [?that France] engages, it
is said, towards [?the Empress] not to be contrary to her with regard to the election of a King of the Romans. This
news has caused an extraordinary consternation here, because it is feared that there may be secret articles which go
further still. This had been suspected for several months, that there was something between the two courts, and the
suspicion acquired the strongest degree of probability since it was [learned] that the steps which the [P"] had had
taken at [ ] to bring her back had been fruitless. The [?English] complain strongly, and they make much of the
[subsidies] paid to [ ] during the last war, which amount to nine millions of pounds sterling. The [?nation] [?seems]
impatient to see how [people] will take this news, and whether she will follow the [...] system

[...] where a general reversal was foreseen. [...] his strong [?bond] with the [ ], who, finding herself [...] at the
assembly, begged the ambassador to tell her [...]; the ambassador of Spain joked a great deal with this lady, telling
her that it was a [...] as she [...] the ambassador.

the ambassador, where they had not yet been since he left the town; and many reflections were also made on this step.
The [ ] say, for the rest, that they have no news of the signing of the [treaty] with [ ], which does not prevent its
being known positively that the thing is real."""),
}
if __name__ == '__main__':
    for d, (date, extra, body) in T.items():
        (D / f'{d}_en.md').write_text(H.format(d=d, date=date, extra=extra) + body + '\n', encoding='utf8')
        print(d)
