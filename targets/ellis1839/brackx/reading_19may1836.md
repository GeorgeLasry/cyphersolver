# Ellis to Forsyth, Mexico, 19 May 1836: reading of the coded part (NARA M97 roll 8, frames 15–19)

The decode of `ct_f015L.txt` … `ct_f019R.txt` (1,383 groups, read from the images) with the jqa table and
the values in `dec.py`, written as words. The clerk's clean copy (frames 20–23) is not used to supply anything:
where the decode does not give a word, the word is marked.

**Notation:** the text is the clerk's clean copy; `[?word]` marks a word the decode does not give. Whether a word is
given is decided mechanically (`readmeasure.py`): the decoded groups are aligned letter by letter with the
clean text, each group allowed its table value, the table's listed alternatives, and the corrections in
`ellis_values.tsv`; a word is read when all its letters come from matching groups (a plural *s* the code omits is
allowed), or when the decoded letters differ only by doubled letters or, in words of 7+ letters, one edit (Ellis's
spellings such as *execuion*, *profered*, *discusion*). The despatch opens and closes in clear; the
coded part begins inside the sentence on the Santa Anna celebrations.

## Reading

[?procession], and the ringing of [?bells]. [?In] these [?impressions] it appears I was not mistaken, as [?we]
received information several days since from the interior announcing the important intelligence of the capture of
Santa Anna the President of this republic, by the people of Texas. The Diario (government paper) of this day admits
the fact, and a proclamation has been [?issued] by the President ad interim, [?placed] at the corners of the
[?streets], appealing to the soldiery and citizens to rise and rescue their President from the imprisonment of his
enemies, the infamous rebels of Texas. The effect of this movement time alone can fully disclose. I am however
inclined to believe the people are not disposed to [?obey] the call of those in authority; and so far as military
force is relied [?on] to release their [?illustrious] President, I am confident it must fail. The national congress
have resolved to prosecute the war against Texas with the utmost vigour, notwithstanding [?Santa] [?Anna] [?has]
[?written] to general Filisola, now the commander in chief of the army, to fall back on San [?Antonio] de [?Bexar] and
Goliad, and that the preservation of his life depended upon the faithful execution of these orders. The policy pursued
by the government here if carried to its full extent, will [?jeopard] the life of him for the preservation of whose
person and fame it is said all the resources of the nation must be called into action. Daily and nightly cabinet
councils have been held to devise some [?mode] by which they [?may] relieve the country from its present extremity,
and in these consultations our government has not been free from [?unjust] imputations in relation to its course in
the Texas war. A portion of the cabinet is exceedingly unfriendly to the United States, and would not hesitate to come
to an open rupture with us if they thought they could be sustained by the feeling of the nation in such an unwise and
impolitic step. As self confident as this government may be in their physical [?strength] and military prowess, I have
[?never] thought for a [?single] moment they would be guilty of such an indiscretion: nevertheless this subject has
been under discussion, as I believe, in the secret [?sittings] of ministers; and the alleged reason for entertaining
such a question is the supposed interference of the United States in the war of Texas. Those who advocate such
measures calculate on relieving themselves from difficulty, if it becomes necessary, [?through] the mediation of
England. General [?Tornel], Secretary of war, is at the head of this faction and entertains the most bitter and
rancorous feelings against the United States, and [?avails] himself of every opportunity in and out of congress to
excite the malignant prejudices of a fanatical people against our countrymen. For the truth of this statement I refer
you to the tone and [?temper] of the Diario the [?mouthpiece] of the ministry. General Tornel at this time has more
power than any man in office and upon the decisions of the government in all things, even in his mad schemes of
ambition to [?embroil] his country in a war with his neighbors of the [?north]. Corro, the President ad interim, is
said to be a good man not enjoying the entire confidence of either political party. The acting minister of foreign
affairs is an intelligent and agreeable gentleman but essentially Mexican in his feelings, and I fear without those
enlarged and liberal views so necessary to enable an enlightened statesman to [?elevate] his country to an enviable
[?rank] among the nations of the [?earth]. [?It] is stated that the Texas government has proffered to release [?Santa]
Anna if Mexico will acknowledge her independence and give the United States as a [?guarantee] for the faithful
observance of the treaty. The proceedings of the national congress up to this period would seem to preclude the
possibility of this conciliatory measure being adopted. The influence of [?Santa] Anna, however, is still great, and
we must await the developement of future events to predict the probable issue of the present excitement in the public
mind. From every thing I can learn and see, I doubt not this unfortunate country is on the eve of another political
[?convulsion], and if it should burst forth under the present highly excited state of party feeling, I am apprehensive
it will be attended with a degree of misery and [?horror] [?unparallelled] in the civil contests of Mexico. This can
be avoided only by the firmness, unity, wisedom and [?overwhelming] strength of the liberal party if they do not
quarrel among [?themselves] they may put down the ultra central party at a single blow, re-establish the constitution
of 1824 and restore peace and tranquillity to the republic. I shall take every occasion to [?advise] you of all
[?important] [?facts] that may be deemed of interest to the department of state. I have the honor to be your most
[?obedient]

## Measure

827 words (*1824* counted as one). With the jqa table as it stands, 682 are given by the decode (0.826). With the
values and corrections in `ellis_values.tsv` that rest on two or more contexts or a dated check (71 groups),
754 (**0.912**); adding the 26 single-context values (tentative), 779 (**0.942**). Ellis's own spellings (*execuion*,
*profered*, *discusion*, *wisedom*) count as read. The rest are mostly Ellis's slips against the code and groups used
once; pushing past 0.95 would need single-context values fitted to the clean copy, which would measure the crib, not
the decode. So the decode alone is *read in part*; the despatch is read from the clerk's decipherment on the film.

