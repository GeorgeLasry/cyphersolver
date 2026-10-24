# Two transcriptions of the Catokwacopa advertisements (The Standard, 8 and 20 May 1875).
# OLD = the circulating text (as supplied by George); BNA = Thomas Ernst's British Newspaper Archive check (2018).
OLD = {
 1:("Str","Umem"), 3:("Catokwacopa","Poayatlgerty"), 4:("Olcabrokorlested","Dpeatcnrftin"),
 5:("Coomemega","Nvtinrdn"), 6:("Sesipyyocashostikr","Dmlurpinrtrcamur"), 7:("Rep","Etd"),
 8:("Itedconlec","Atndngtnsurs"), 9:("mistrl","Otenpu"), 10:("Hfsclam","Eftdorshpxn"),
 12:("caselcluchozamot","Ndtsfindseseo"), 13:("","Cotegr"), 14:("Mopredisco","Tavlysdinlge"),
 15:("Contoladsemot","Ngtndusdcndo"), 16:("Iadfilisat","Edrstneirs"), 17:("Qft","Ui"),
 18:("Cagap","Ndted"), 19:("Balmnopsemsov","iolapstedtioc"), 20:("Ap","AP"), 21:("Hodsam","Yxn"),
 23:("Iopotonrogfimsecharsenr","Wtubrfftrstendinhofsvmnr"), 24:("Tolshr","Dily"),
 25:("Itedjolec","Atdwtsurs"), 26:("mistrl","Oatvpu"), 27:("Ding","Y"), 28:("Declon","Arati"),
 29:("Ereflodbr","Rileohmae"),
}
BNA = dict(OLD)
BNA.update({
 6:("Sesipyyocashostikr","Dmlurpinrtrcamnr"), 10:("Hrsclam","Etfdorshpxn"),
 14:("Mopredisco","Tsvlysdinlge"), 19:("Balmnopsemsov","Iolapstedttoc"),
 23:("Iopotonrogfimsecharsenr","Wtubtrfftrstendinhofsvmnr"),
})
NUMS = {2:("53","18"), 11:("54, 3","18"), 13:("1. 6. 9.","Cotegr"), 20:("Ap. 139 (BNA 138)","A. P. 138"), 22:("55, 6","18. 18")}
# joined token pairs, to let a word span a token boundary (lowercase 'mistrl' may continue the lecture lines)
BNA[89]  = (BNA[8][0]+BNA[9][0],   BNA[8][1]+BNA[9][1])
BNA[2526]= (BNA[25][0]+BNA[26][0], BNA[25][1]+BNA[26][1])
BNA[2729]= (BNA[27][0]+BNA[28][0]+BNA[29][0], BNA[27][1]+BNA[28][1]+BNA[29][1])
BNA[1819]= (BNA[18][0]+BNA[19][0], BNA[18][1]+BNA[19][1])
