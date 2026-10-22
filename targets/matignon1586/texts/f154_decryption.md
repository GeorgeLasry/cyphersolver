# f154: decoder output with key_contrib.json

Saved output of `KEY=key_contrib.json python dec.py f154_cipher.txt` (run 22 Oct 2026; the same decoder and key that
`measure.py --key key_contrib.json` scores, 21 Oct 2026). Raw machine decode: the first block is the joined,
word-segmented text, then one numbered line per manuscript line. Unkeyed tokens (`BOX`, `?`, unknown codes)
take whatever letter the language model prefers and are not read; `+`/`*` mark code groups. The prose
reading of the leaf, where one exists, is in the `f*_reading.md` file.

```
nuu en que le ceine nous estions lors pour le payement de edel monstree qui auoient este faicte ea noe gens de guete la que le est deuenu i encores depuis peut plus grande nous le dict ca ie ment n ayant peut uui+re les d au tee monstree sitost que de coustume ou stume et aucuns des car itaines ayans i au rine eue uol date que lon leur uouloit faire a an que roune r testu m idem d uenir une sedition a les le igno le parmi eue auec des la ne m ie es et des iceue re+n ces si est ranee s qu il n est uos sible de plu ar s rus que sa uouloir c aban doy er le semr des et mena sser de llier les en se ie ne s dont monsieur du mayne est en n et eleue i ne que ie uous an eure qu il en est pit iable estant esperc et ue le a tre hension de ueoir a tiue r quelque grand scandale en ceste armv ostre et ne iant aucun moyen de noster si promptement lon a sion ey parce que ceue qui nou sauoie it promis de nous prester ie d lus a rendre a paris lorsque nous y auons enuoye le soai s d s tresorier auec nos obligations et l s messes il l sont faict de ne ose les dissi culte et proteste qu ils neur este roient pas s n escu que ie ne miu blige a ne seul en mon priue nom et que ie ne a in se leur pro m en redi boui ce que le une leurseroit rendu a paris alen reueue de sorle qu il est force que ie sois icy retenu pour ceste on a sion dont ie uenin i que ie ne sortiray que ie ni sois obligee ourc lus de quarante mil escus en mon priue nom qui sera remarque pour s ne signale fol ie qui considerer ele temps ou nous aoa er qui peut

1 nuu en que le ceine nous estions lors pour le payement de edel
2 monstree qui auoient este faicte ea noe gens de gue
3 tel a que le est deuenu i encores depuis peut plus gran
4 de nous le dict ca ie ment n ayant peut uui+re les d au tee
5 monstree sitost que de coustume ou stume et aucuns des ca
6 r itaines ayans i au rine eue uol date que lon leur
7 uouloit faire a an que roune r testu m idem d uenir
8 une sedition a les le igno le parmi eue auec des la
9 ne m ie es et des iceue re+n ces si est ranee s qu il n est
10 uos sible de plu ar s rus que sa uouloir c aban doy er les em
11 r des et mena sser de llier les en se ie ne s dont monsieur du mayne e
12 st en n et eleue i ne que ie uous an eure qu il en est pit
13 iable estant esperc et ue le a tre hension de ueoir
14 a tiue r quelque grand scandale en ceste armv ostre et n
15 ei ant aucun moyen de noster si promptement lon a
16 sion ey parce que ceue qui nou sauoie it promis de nous prester ie
17 d lus a rendre a paris lorsque nous y auons enuoye le
18 soai s d s tresorier auec nos obligations et l
19 s messes il l sont faict de ne ose les dissi culte
20 et proteste qu ils neur este roient pas s n escu
21 que ie ne miu blige a ne seul en mon priue nom et que
22 ie ne a in se leur pro m en redi boui ce que le une
23 leurseroit rendu a paris alen reueue desor l
24 e qu il est force que ie sois icy retenu pour ceste
25 on a sion dont ie uenin i que ie ne sortiray que ie ni
26 sois obligee ourc lus de quarante mil escus en
27 mon priue nom qui sera remarque pour s ne signale
28 fol ie qui considerer ele temps ou nous aoa er qui peut
```
