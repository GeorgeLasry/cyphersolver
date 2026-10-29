# rows for build.py (exec'd inside build.py; uses add(), V, R)
LPV="11001939bsb"; V2="10278829bsb"; V3="11332111bsb"; CG="gri_33125005958521"
GEN_PRIOR="open (checked 28 Oct 2026: the printed volume says undeciphered; full-text search of the volume finds no later decipherment; repo grep finds no target; web search not run, importance below 3)"
# ---------- Henry VIII era (Letters and Papers) ----------
for (d,pos,note) in [
 ("15 Aug 1526","entry immediately before no. 2400 (Add. at f.111b)","Rome, 15 Aug 1526, Latin, signed; 'Cipher, undeciphered; mutilated'"),
 ("17 Aug 1526","entry immediately before no. 2404","Rome, 17 Aug 1526, mutilated; 'The cipher undeciphered'"),
 ("21 Aug 1526","entry immediately before no. 2418 (Cotton Vit. B. viii f.113 per margin)","Rome, 21 Aug 1526, 2 pp., mutilated; 'The cipher undeciphered'; reports the death of the Duke of Sessa"),
 ("30 Aug 1526","entry immediately before no. 2444","Rome, 30 Aug 1526; 'Cipher, undeciphered; mutilated'"),
 ("5 Sep 1526","entry immediately before no. 2463","Rome, 5 Sep 1526, mutilated; 'The cipher undeciphered'")]:
    add(1526,d,"Rome despatch to Wolsey, %s, cipher undeciphered (War of the League of Cognac)"%d,"Henry VIII's Rome agents (Ghinucci/Casale, to confirm from LP header) → Wolsey","Rome","Latin","England",LPV,"LP IV pt 2, "+pos,"B",
      "Brewer's calendar: "+note+". The Rome agents' cipher is of the family whose other letters survive with Tuke's interlinear decipherments (Tomokiyo's Lee-Worcester key), so a key from siblings may apply. Not checked against DECODE record by record.",
      "Wolsey's Rome intelligence in the run-up to the Sack of Rome; the cipher parts are what the editor withheld.",3,2,3,
      "Open LP IV pt 2 at the entry; read the cited MS (Cotton Vitellius B. viii) on BL images; check whether Tuke's decipher exists on an adjacent folio.",
      prior="open (checked 28 Oct 2026: LP says undeciphered; repo has no target for these Rome 1526 letters; cryptiana/HistoCrypt not searched)",q="cipher undeciphered")
add(1527,"5 Jun 1527","Valladolid despatch to Wolsey, 5 June 1527, passages in cipher undeciphered","Probably Ghinucci/Lee/Poyntz → Wolsey (LP header not captured)","Valladolid","English","England",LPV,"LP IV pt 2, entry immediately before no. 3153","B",
 "Brewer: 'Hol., pp.10. Some passages in cipher undeciphered. Add.' Same embassy whose other cipher letters (Lee-Worcester) are in this repo's catalogue; this one is not.",
 "Imperial court after the Sack of Rome, as seen by the English embassy.",3,3,2,"Find the BL MS ref in the LP entry; apply the Lee-Worcester key already used for Cotton Vespasian C IV (repo targets/lee1526).",
 prior="open (checked 28 Oct 2026: repo has sibling Lee-Worcester letters only)",q="Some passages in cipher undeciphered")
add(1527,"22 Jul 1527","Duplicate of a despatch of 22 July 1527, partly in cipher undeciphered (plan to free Clement VII)","unknown → Wolsey","unknown","Latin","England",LPV,"LP IV pt 2, item 2 under the entry preceding no. 3292","C",
 "Brewer: 'Duplicate of the preceding, partly in cipher, undeciphered. Headed: Dupplicata sub die 22 Julii 1527.' Lat., mutilated, pp. 2.",
 "A fragment on detaching France from the Emperor.",2,2,3,"Read the LP entry (the preceding paragraph names the letter); locate in BL Cotton.",prior=GEN_PRIOR,q="Duplicate of the preceding, partly in cipher")
add(1527,"27 Oct 1527","Burgos despatch to Wolsey, 27 Oct 1527, two passages in cipher undeciphered","Ghinucci/Lee/Jerningham (to confirm) → Wolsey","Burgos","English","England",LPV,"LP IV pt 2, entry immediately before no. 3524","B",
 "Brewer: 'Burgos, 27 Oct. 1527. Signed. Pp.3. Two passages in cipher, undeciphered. Add. Endd.'",
 "Charles V's reaction to the English treaty, from the Lee-Worcester embassy.",2,3,2,"Check LP IV pt 2 no. 3523 and the BL volume; apply the Lee-Worcester key.",prior=GEN_PRIOR,q="Two passages in cipher, undeciphered")
add(1517,"8 Nov 1517","Rome, 8 Nov 1517: Latin letter to Wolsey, part cipher undeciphered (collectorship, Peter Vannes)","Papal-court correspondent (to confirm) → Wolsey","Rome","Latin","England",V2,"LP II pt 2, entry immediately before no. 3782 (Add. f.211)","C",
 "Brewer: 'Hol., pp.10, Lat., part cipher, undeciphered.' Rome, 8 Nov 1517; mentions the Tournay bull licence and Vannes's collectorship.",
 "Early Wolsey-Rome correspondence; an early Tudor ambassadorial cipher use.",3,2,4,"Open LP II pt 2 at the entry; identify the writer and the MS.",prior=GEN_PRIOR,q="part cipher, undeciphered")
for (d,pl,pos,note) in [("2 Apr 1518","Arranda","entry immediately before no. 4057","Hol., pp. 9, mostly cipher; encloses Sir J. Stile's letter on the English ambassadors' arrival"),
                        ("30 Jun 1518","Saragossa","entry immediately before no. 4278","Hol., pp. 6, mostly cipher; Aragonese Cortes oath to Charles"),
                        ("16 Aug 1518","Saragossa","entry immediately before no. 4885","Hol., pp. 6, mostly cipher; Navarre ambassador, Cortes of Aragon")]:
    add(1518,d,"Spanish court despatch to Wolsey, %s, mostly in cipher, undeciphered"%d,"Thomas Spinelly (to confirm from LP header) → Wolsey",pl,"English","England",V2,"LP II pt 2, "+pos,"C",
      "Brewer: '"+note+", undeciphered'. A long, mostly ciphered letter with no sibling decipherment in the volume.",
      "Charles V's first months in Spain as seen by the English resident.",4,3,3,
      "Open LP II pt 2 at the cited number; find the BL (Vesp. C i) folio; compare with Spinelly letters already deciphered (repo targets/spinelly1517).",
      prior="open (checked 28 Oct 2026: LP says 'mostly cipher, undeciphered'; repo has targets/spinelly1517 for 1517 only; cryptiana/HistoCrypt not searched)",q="mostly cipher, undeciphered")
# Ghinucci 1530
for (d,pos,n) in [("late Jan 1530","entry preceding no. 6141 (Hol., mutilated; duplicate also in cipher)","Venice/Padua: Hebrew and Greek MS search for the Divorce"),
                  ("22 Jan 1530","entry preceding no. 6158 (Vit. B. xiii)","Hebrew scholar, book of Sanctes"),
                  ("25 Jan 1530","entry preceding no. 6167","money for the dispensation, the Datary"),
                  ("26 Jan 1530","entry preceding no. 6169","papal control of the friars"),
                  ("2 Feb 1530","entry preceding no. 6190 (Vit. B. xiii f.33b)","Florentine affairs"),
                  ("2 Feb 1530 (second)","entry preceding no. 6192","Stokesley's arrival, Benet at Tarbes")]:
    add(1530,d,"Ghinucci (Bishop of Worcester) in Italy to Henry VIII, %s: cipher undeciphered, mutilated"%d,"Geronimo Ghinucci, Bishop of Worcester → Henry VIII","Italy (Bologna/Venice/Padua)","Latin","England",V3,"LP IV pt 3, "+pos,"B",
      "Brewer: 'Cipher, undeciphered; mutilated.' ("+n+"). Cotton Vitellius B. xiii (fire damaged). Planta's 1802 catalogue lists 'five letters in cypher, not deciphered, said to be from the Bp of Worcester' in the same volume. Worcester's cipher is the family used in his 1527-29 Spanish letters (Tuke decipherments).",
      "The Divorce campaign: Ghinucci's Italian reports on theologians and manuscripts, cipher parts withheld.",4,2,3,
      "View the Cotton Vitellius B. xiii leaves (BL Digitised; DECODE if present); fire damage may decide; try the Lee-Worcester key.",
      prior="open (checked 28 Oct 2026: LP and Planta say undeciphered; no repo target for Vit. B. xiii; Tomokiyo's Lee-Worcester pages not re-read)",q="Cipher, undeciphered mutilated")
add(1529,"22 Oct 1529","Du Bellay (London) to Montmorency, 22 Oct 1529: beginning of the letter in cipher, undeciphered","Jean du Bellay → Anne de Montmorency","London","French","France",V3,"LP IV pt 3, no. 6019 'Du Bellay to Montmorency' (Le Grand)","C",
 "Brewer: '(The beginning of the letter is in cipher, undeciphered.)' Written as Wolsey's goods were seized.",
 "French ambassador's cipher account of Wolsey's fall.",4,2,4,"Compare with Du Bellay's ciphers in BnF (Le Grand ms.); check cipher tables (Lasry, Tomokiyo).",prior=GEN_PRIOR.replace("importance below 3","importance 4: cryptiana/HistoCrypt not yet searched"),q="beginning of the letter is in cipher")
# ---------- Cottonian catalogue (Planta 1802) ----------
add(1529,"12 and 15 Feb 1529","Bishop of Worcester (Ghinucci) to Wolsey, Valladolid, two originals chiefly in cypher not decyphered","Ghinucci → Wolsey","Valladolid","Latin","England",CG,"Planta catalogue, Cotton MS (Spanish embassy volume), item 93; also item 113 (22 Jul 1529 duplicate)","B",
 "Planta 1802: 'two origs. chiefly in cypher, not decyphered. Valladolid Feb. 12 and 15, 1529' and 'A paper chiefly in cypher, not decyphered; said to be a duplicate of a letter from the Bp. of Worcester of July 22, 1529'. Neighbours of 17/19 Feb are 'decyphered'. Volume number not captured near the hit: verify.",
 "The 1529 Spanish embassy on the Divorce, with the key family the neighbouring decipherments give.",4,3,2,
 "Find the Cotton volume in Planta (heading before item 93); view the BL leaves; build the key from the decyphered neighbours (class A/B).",
 prior="open (checked 28 Oct 2026: Planta says not decyphered; LP may calendar the content; Tomokiyo not re-read)",q="chiefly in cypher, not decyphered")
add(1526,"4 Mar 1526","Bishop of Worcester to Cardinal Wolsey, Rome, 4 March 1526, Latin in cypher not deciphered","Ghinucci → Wolsey","Rome","Latin","England",CG,"Planta catalogue item 16 (Cotton MS, Rome 1526 group)","B",
 "Planta: '16. The Bp. of Worcester, to Card. Wolsey. (Orig. Lat. in cypher, not deciphered.) Rome, March 4, 1526.' Item 17 is a plain letter.",
 "Earliest cipher letter of Ghinucci's Rome mission.",3,3,3,"Locate the Cotton volume (heading before item 16); check LP IV pt 2 for the calendared content.",prior=GEN_PRIOR.replace("importance below 3","importance 3: cryptiana not searched"),q="in cypher, not deciphered")
add(1560,"19 Jul 1560","Sir Nicholas Throckmorton (Paris) to Cecil, one of three letters, wholly in cypher and not explained","Nicholas Throckmorton → William Cecil","Paris","English","France",CG,"Planta catalogue, Cotton MS (Throckmorton/Cecil volume), item 18","B",
 "Planta: 'Three letters from sir Nic. Throckmorton, to Secretary Cecil; one of them wholly in cypher and not explained'. Throckmorton's cipher family is in the repo (targets/throck1569).",
 "The 1560 French crisis before the Treaty of Edinburgh.",4,3,3,"Find the Cotton MS and the CSP Foreign 1560-61 entry; try the Throckmorton key.",
 prior="open (checked 28 Oct 2026: repo targets/throck1569 covers 1569 only; cryptiana not searched)",q="wholly in cypher and not explained")
add(1575,"Aug 1575","Archbishop of Glasgow (Beaton) to his brother, a cypher not deciphered","James Beaton, Archbishop of Glasgow → his brother","unknown","unknown","Other",CG,"Planta catalogue, Cotton MS Caligula C. III, item 229","C",
 "Planta: '229. The Abp. of Glasgow, to his brother, (a cypher not deciphered.) Aug. 1575.'",
 "Marian exiles' cipher traffic.",3,2,4,"Look at Cotton Caligula C. III on BL; compare Beaton ciphers in Mary Queen of Scots correspondence (DECODE).",q="a cypher not deciphered")
add(1575,"11 Oct 1575 (as printed)","Bishop of Ross to Duke of Norfolk, a cypher not deciphered","John Leslie, Bishop of Ross → Duke of Norfolk","unknown","unknown","Other",CG,"Planta catalogue, Cotton MS Caligula C. III, item 224","C",
 "Planta: '224. The Bp. of Ross, to the D. of Norfolk, (a cypher not deciphered.) Oct. 11, 1575.' The date is wrong as printed (Norfolk d. 1572); probably c. 1570-71.",
 "Ross-Norfolk cipher of the Ridolfi era.",3,3,3,"View Cotton Caligula C. III; check Ross's cipher in the Tower examinations.",q="Bp. of Ross, to the D. of Norfolk")
# ---------- Edward VI / Mary Foreign ----------
E="cu31924028043614"; M="cu31924028043622"
add(1550,"1550 (calendar no. 97)","Dr Nicholas Wotton to the Lord Protector: first and larger part in cipher, undeciphered","Nicholas Wotton → Lord Protector (Somerset)","Imperial court","English","Central Europe","calendarofstatep00lond","CSP Foreign Edward VI, no. 97 (5 pp.)","B",
 "Turnbull: 'Five pages. The first and larger part in cipher, undeciphered' (about the Interim). Wotton's cipher is the family of his 1554 letters in this repo's catalogue (DECODE R8499 key R354).",
 "English view of the Augsburg Interim, from the ambassador to Charles V.",3,3,2,"Locate the TNA SP 68 piece in the calendar entry; try the Wotton key R354.",
 prior="open (checked 28 Oct 2026: repo has Wotton 1554 only; no 1550 reading found)",q="first and larger part in cipher")
for (y,d,corr,pos,nt,imp) in [
 (1551,"1551 (undated)","Sir Richard Morysine → Cecil","CSP Foreign Edward VI, no. 268","Two pages, partly in cipher, undeciphered; asks for money.",2),
 (1551,"Apr 1551","John Hales → Cecil","CSP Foreign Edward VI, no. 328 (attached to Morysine's of 28 April)","Two pages, five lines in cipher, undeciphered.",2),
 (1552,"Jul 1552","Christopher Mount → Council","CSP Foreign Edward VI, no. 549","Two pages, three lines in cipher, undeciphered (Diet of the Empire).",2),
 (1552,"early Dec 1552","Sir William Pickering → Council","CSP Foreign Edward VI, no. 588","Two pages, principally in cipher, undeciphered; Barnaby Fitzpatrick leaves the French court.",3)]:
    add(y,d,"%s (%s): %s"%(corr,d,nt),corr,"unknown","English","England",E,pos,"C",
      "Turnbull: "+nt+" No key recorded; originals in TNA SP 68.","Edward VI diplomacy; short cipher runs.",imp,2,3,"Locate the SP 68 piece named in the calendar; no key known.",prior=GEN_PRIOR,q="in cipher, undeciphered")
add(1553,"20 Mar 1553","Unsigned letter from Anet, almost entirely in cipher 'undecipherable', apparently to the French ambassador in England (calendar no. 637)","unknown (French court) → French ambassador in England","Anet","unknown","France",E,"CSP Foreign Edward VI, no. 637","C",
 "Turnbull: 'Letter, without signature, and almost entirely in cipher, undecipherable, apparently to the French Ambassador in England. Alludes to the reply given by the French King to the English resident at Paris...'",
 "French cipher intercepted in the last weeks of Edward VI.",3,2,4,"Open TNA SP 68; check French diplomatic cipher tables of the 1550s.",prior=GEN_PRIOR.replace("importance below 3","importance 3: cryptiana not searched"),q="almost entirely in cipher")
add(1554,"Jan 1554 (calendar no. 316)","Dr Wotton to the Council: first portion in cipher, undeciphered (liberation of Sir Gawen Carew)","Nicholas Wotton → Council","France","English","France",M,"CSP Foreign Mary, no. 316 (7.5 pp.)","B",
 "Turnbull: 'Seven pages and a half. The first portion in cipher, undeciphered'; the next item is dated 28 Jan. Year inferred from the calendar sequence: verify. Wotton key R354 exists.",
 "Wotton's French embassy at the start of Mary's reign.",3,3,2,"View TNA SP 69; try key R354.",prior="open (checked 28 Oct 2026: repo has Wotton 13 Jun 1554 only)",q="first portion in cipher")
add(1555,"c. Jan 1555 (calendar no. 453)","Dr Wotton to Queen Mary: a few lines in cipher undeciphered","Nicholas Wotton → Queen Mary","France","English","France",M,"CSP Foreign Mary, no. 453","B",
 "Turnbull: 'A few lines in cipher, undeciphered. One page.' Year inferred from sequence: verify.",
 "Wotton's report on French dealings with Philip and Mary.",2,3,2,"View TNA SP 69; try the Wotton key.",prior=GEN_PRIOR,q="A few lines in cipher, undeciphered")
# ---------- Elizabeth foreign ----------
F="calendarofstatep00grea_0"
add(1569,"1569 (calendar no. 285)","Sir Henry Norris (Paris) to Cecil: entirely in cipher, undeciphered","Henry Norris → William Cecil","Paris","English","France",F,"CSP Foreign Elizabeth 1569-71, no. 285","B",
 "Crosby: 'Entirely in cipher, undeciphered. Add. Endd., with seal. P. 1.' (year inferred from the volume: verify). The Cecil-Norris table (Tomokiyo, from Cabala) reads Norris siblings (repo targets/norreys1567).",
 "A clean test of the Cecil-Norris table on a letter not previously read.",3,3,2,"Find the SP 70 piece via the calendar; apply the Cecil-Norris table.",
 prior="open (checked 28 Oct 2026: repo norreys1567 covers Forbes's copies of seven letters; not this one)",q="Entirely in cipher, undeciphered")
add(1569,"1569 (calendar no. 575)","Letter 'for the most part in cipher, to which there is no key' (M. de la Vigne ill and discontented)","unknown","unknown","French","France",F,"CSP Foreign Elizabeth 1569-71, no. 575","C",
 "Crosby: 'A Letter for the most part in cipher, to which there is no key.'","Anonymous diplomatic cipher of 1569.",2,2,4,"View SP 70; no key.",prior=GEN_PRIOR,q="to which there is no key")
add(1570,"c. Apr 1570 (calendar no. 812)","Letter partly in the cipher of John Marsh, then the same wholly in cipher not deciphered (4 pp.)","unknown (Muscovy Company correspondent) → unknown","unknown","English","Other",F,"CSP Foreign Elizabeth 1569-71, no. 812 (Marsh cipher)","A",
 "Crosby: 'Written partly in the cipher of John Marsh. Pp. 3. 812. The above in cipher, not deciphered. Pp. 4.' The plain portion of the preceding entry is a crib for the 4-page cipher copy.",
 "Spanish/Netherlands intelligence of 1570 (Alva's attitude to the English).",3,4,2,"Open SP 70; use the plain/Marsh-cipher portion as crib.",prior="open (checked 28 Oct 2026: Marsh cipher not in repo)",q="in cipher, not deciphered")
add(1571,"1 Apr 1571 (calendar no. 1629)","Privy Council of Spain to the Inquisition, taken at Dumbarton: partly in cipher, most names undeciphered","unknown (Privy Council of Spain) → Inquisition","Dumbarton","unknown","Other",F,"CSP Foreign Elizabeth 1569-71, no. 1629","C",
 "Crosby: 'Partly in cipher with most of the names undeciphered. Add. Endd. by Burghley: taken in Dumbarton.' P. 1.",
 "Spanish state cipher captured with the Archbishop of Glasgow's papers.",3,2,4,"View the SP original; Philip II cipher family.",prior=GEN_PRIOR.replace("importance below 3","importance 3: cryptiana not searched"),q="most of the names undeciphered")
add(1562,"6 Dec 1562","Prince of Condé's camp before Paris to Queen Elizabeth: original in cipher, undeciphered","Louis de Bourbon, Prince of Condé → Queen Elizabeth","Camp before Paris","unknown","France","calendarstatepa03britgoog","CSP Foreign Elizabeth 1562, no. 1195 (immediately before Smith's no. 1196)","B",
 "Stevenson: 'Signed. Orig. In cipher, undeciphered. Add. Endd. Pp. 3.' Repo holds the Condé key R335 (targets/coligny1563), so the family may be available.",
 "Condé's appeal to Elizabeth at the height of the Le Havre affair.",4,3,3,"Open TNA SP 70; try the Condé cipher (DECODE R335) from repo targets/coligny1563.",
 prior="open (checked 28 Oct 2026: repo has the Condé key but no reading of this letter; cryptiana not searched)",q="Orig. In cipher, undeciphered")
add(1573,"17 May 1573","Sir Valentine Browne to Burghley, Berwick: enclosure partly plain, 'the rest in cipher not yet deciphered' (covenants England-Scotland)","Sir Valentine Browne → Lord Burghley (with Scottish enclosure)","Berwick","English","England","calendarofstatep10grea","CSP Foreign Elizabeth 1572-74, no. 966","C",
 "Crosby: '... the covenants between England and Scotland ... the rest was in cipher not yet deciphered. Berwick, 17 May 1573. Add. Endd. by Burghley.'",
 "Scottish party cipher in the last months of the civil war.",3,2,4,"View the SP 59 original; compare with Scottish ciphers in DECODE.",prior=GEN_PRIOR.replace("importance below 3","importance 3: cryptiana not searched"),q="the rest was in cipher not yet deciphered")
S8="calendarofstatep08grea"
add(1585,"1585 (no. 70)","Courcelles to Chateauneuf: 4 pp. French, partly in cipher not deciphered","Courcelles → Chateauneuf (French ambassador in London)","unknown","French","Other",S8,"CSP Scotland vol. VIII, no. 70","C",
 "Calendar: '4 pp. French. Partly in cipher not deciphered. Indorsed.'","French embassy cipher traffic in 1585.",3,2,4,"View the SP 53/52 piece; test the Chateauneuf cipher.",prior=GEN_PRIOR.replace("importance below 3","importance 3: cryptiana not searched"),q="Partly in cipher not deciphered")
add(1586,"early Mar 1586 (no. 598)","Thomas Fowler to Walsingham, Edinburgh: partly in cipher not deciphered","Thomas Fowler → Sir Francis Walsingham","Edinburgh","English","England",S8,"CSP Scotland vol. VIII, no. 598 (the item before no. 599)","B",
 "Calendar: '1 p. Holograph. Addressed. Indorsed. Partly in cipher not deciphered.' Walsingham's Scottish agents used a family key (repo cat. 81-82).",
 "James VI's entourage before the Treaty of Berwick.",3,3,2,"View SP 52; use the Walsingham-Wotton 1585 key set from the repo.",
 prior="open (checked 28 Oct 2026: repo covers Walsingham-Wotton 1585 (cat. 81-82), not Fowler)",q="Partly in cipher not deciphered")
# ---------- Elizabeth domestic ----------
D4="cu31924091775316"
for (y,d,it,nt) in [(1572,"Jan 1572 (Addenda item 4)","4","Countess of Northumberland and the Spanish embassy; italic passages cipher undeciphered"),
                    (1572,"Apr 1572 (Addenda item 28)","28","pardon for Norton; 3 pp.; italic passages cipher undeciphered"),
                    (1572,"Apr 1572 (Addenda item 31)","31","the Pope has written ...; 1.5 pp.; italic passages cipher undeciphered"),
                    (1573,"Apr 1573 (Addenda item 6)","6","reply to Burghley's of 25 May; 2.5 pp., unfinished; italic passages cipher undeciphered"),
                    (1573,"Jul 1573 (Addenda item 71)","71","Northumberland party at Dunkirk; 2 pp.; italic passages cipher undeciphered")]:
    add(y,d,"John Lee (spy) to Lord Burghley, %s: passages in cipher undeciphered"%d,"John Lee → Lord Burghley","Flanders","English","England",D4,"CSP Domestic Elizabeth Addenda 1566-79, Lee to Burghley item "+it,"C",
      "Green: "+nt+". Year and item number as inferred from the Addenda sequence: check dates in the volume.",
      "Burghley's spy in the Northumberland exile circle.",2,2,3,"Open the Addenda volume at the item; TNA SP 15; no key.",prior=GEN_PRIOR,q="passages in italics are in cipher undeciphered")
D3="cu31924091775274"; D2="cu31924091775373"
add(1592,"c. Jan 1592 (item 26)","John Bristowe [Moody] to William White: italic passages in cipher undeciphered","John Bristowe (alias Moody) → William White","unknown","English","England",D3,"CSP Domestic Elizabeth 1591-94, item 26","C",
 "Green: 'The italics are in cipher undeciphered.' (Wisbech prison, Jonas Meredith.) Date inferred: verify.","Recusant network letters from Wisbech.",2,2,3,"SP 12 piece via the calendar.",prior=GEN_PRIOR,q="The italics are in cipher undeciphered")
add(1593,"19 Jan 1593 (item 18)","H. Saint Main to Fitzherbert (draft by Phelippes): italics in cipher undeciphered, mercantile allusions disguise the purport","Saint Main → Thomas Fitzherbert","unknown","English","England",D3,"CSP Domestic Elizabeth 1591-94, item 18","B",
 "Green: '[Draft by Phelippes. 2.75 pp. The italics are in cipher, undeciphered. The allusions to mercantile affairs are only meant to disguise the purport of the letter.]'",
 "A Phelippes draft; mercantile cover code over cipher.",3,2,4,"SP 12/243; compare repo Phelippes work (targets/mendoza1589).",prior=GEN_PRIOR.replace("importance below 3","importance 3: cryptiana not searched"),q="allusions to mercantile affairs")
add(1594,"14 Mar 1594 (item 75)","Thomas Barnes to Charles Paget: draft by Phelippes, asterisked passages proved undecipherable","Thomas Barnes → Charles Paget","unknown","English","England",D3,"CSP Domestic Elizabeth 1591-94, item 75","B",
 "Green: 'Draft by Phelippes, endorsed by him Written by J. to A. The italics are in cipher, undeciphered; the passages marked by asterisks have proved undecipherable.' Brittany, Guernsey and Jersey.",
 "Brittany campaign intelligence.",3,2,4,"SP 12/247; Phelippes/Paget cipher family (DECODE).",prior=GEN_PRIOR.replace("importance below 3","importance 3: cryptiana not searched"),q="proved undecipherable")
add(1588,"28 Mar 1588 (item 10)","Father Holt to Cardinal Allen: 3 pp., asterisks mark passages in cipher undeciphered, italics deciphered by Phelippes","William Holt SJ → Cardinal William Allen","unknown","English","England",D2,"CSP Domestic Elizabeth 1581-90, item 10","A",
 "Green: '[3 pp., the asterisks represent passages in cipher undeciphered; the italics deciphers by Phelippes.]' The readable parts give a crib for the gaps.",
 "Armada-year Catholic cipher letter to Allen.",4,3,3,"SP 12/209 original and Phelippes decipher.",prior="open (checked 28 Oct 2026: calendar names the gaps; HistoCrypt/cryptiana not searched)",q="asterisks represent passages in cipher undeciphered")
add(1588,"Sep 1588 (item 43)","Charles Paget to Cardinal Allen: partly in cipher undeciphered","Charles Paget → Cardinal Allen","Brussels","English","England",D2,"CSP Domestic Elizabeth 1581-90, item 43 (1 p.)","B",
 "Green: '[1 page, partly in cipher undeciphered.]' The Duke of Parma did not come to Brussels. Year inferred: verify.","Paget's cipher use in 1588.",3,3,3,"SP 12/216; Paget cipher key (DECODE).",prior=GEN_PRIOR.replace("importance below 3","importance 3: cryptiana not searched"),q="partly in cipher undeciphered")
add(1611,"Jul-Aug 1611","John Woodford to Sir Francis Nethersole: partly in cipher undeciphered (Du Buisson, Prince of Condé's offer)","John Woodford → Sir Francis Nethersole","unknown","English","England","1967calendarofstatep10greauoft","CSP Domestic James I 1611-18, entry before no. 60 (Aug 3)","C",
 "Green: 'M. Du Buisson arrived with letters from the Prince of Conde, offering the daughter of France in marriage to the Prince. Partly in cipher, undeciphered.'","Prince Henry's marriage negotiations of 1611.",2,2,3,"SP 14/65.",prior=GEN_PRIOR,q="Partly in cipher, undeciphered")
# ---------- Ireland ----------
add(1600,"c. Jun 1600 (no. 116)","Lord Barry (Buttevant) to Cecil/Privy Council: footnote 'Cipher not deciphered'","David Barry, Viscount Buttevant → Cecil","Ireland","English","England","1903calendarofstatep09greauoft","CSP Ireland Elizabeth 1599-1600, no. 116","C",
 "Mahaffy footnote 'Cipher not deciphered' on a petition for the castle of Conyhie.","Munster in the Nine Years War.",1,2,3,"SP 63/207.",prior=GEN_PRIOR,q="Cipher not deciphered")
add(1600,"30 Jun 1600 (no. 133)","Sir Henry Dockwra, Derry, to the Privy Council: footnote 'Cipher not deciphered'","Henry Dockwra → Privy Council","Derry","English","England","1903calendarofstatep09greauoft","CSP Ireland Elizabeth 1599-1600, no. 133","C",
 "Mahaffy footnote on the delivery of James FitzThomas: 'Cipher not deciphered'.","Derry garrison, Nine Years War.",2,2,3,"SP 63/207.",prior=GEN_PRIOR,q="Cipher not deciphered")
add(1601,"22 Mar 1601 (no. 98)","Captain Humphrey Covert to Cecil: 'Cipher undeciphered'","Humphrey Covert → Sir Robert Cecil","Ireland","English","England","1905calendarofstatep10greauoft","CSP Ireland Elizabeth 1600-01, no. 98","C",
 "Mahaffy footnote: 'Cipher undeciphered'.","Nine Years War.",1,2,3,"SP 63/208.",prior=GEN_PRIOR,q="Cipher undeciphered")
# ---------- Clarendon ----------
CV1="calendarofclaren01bodluoft"; CV4="calendarofclaren04bodluoft"
for (y,d,t,corr,pos,note) in [
 (1645,"15 Dec 1644 (orig.) / 18 Jan 1645 dup.","Charles I to Ormond, duplicate of 15 Dec 1644 letter, in cypher, not decyphered","Charles I → Marquis of Ormond","Clarendon State Papers vol. I, no. 1815 (rec. 6 Mar 1645 by Col. John Barry)","In cypher, not decyphered; the preceding letter no. 1813 is 'decyphered by Ormond'."),
 (1646,"Aug/Sep 1646","Charles I (Newcastle) to Ormond: wishes a safe way of intelligence; duplicate original in cypher, not decyphered","Charles I → Marquis of Ormond","Clarendon State Papers vol. I, no. 2312","'In cypher. A duplicate original; not decyphered.'"),
 (1648,"early 1648 (reply to Ormond/Digby of 2-3 Dec)","Charles I to Ormond, cypher in duplicate, not decyphered (answers Ormond and Digby despatch of 2-3 Dec)","Charles I → Marquis of Ormond","Clarendon State Papers vol. I, no. 2401","'Cypher. In duplicate, not decyphered.'"),
 (1648,"29 Apr 1648","Sir Edward Hyde (Jersey) to Secretary Nicholas: nearly all in cypher, not deciphered (secret commission under the Great Seal, Glamorgan?)","Sir Edward Hyde → Sec. Sir Edward Nicholas","Clarendon State Papers vol. I, no. 2505","'Nearly all in cypher, not deciphered. Some expressions point to a secret commission under the Great Seal; possibly that of Glamorgan.'"),
 (1646,"Sep 1646 (no. 2320)","Sir Edward Hyde (Jersey) to Lord Digby: a portion interspersed with cypher, not decyphered","Sir Edward Hyde → George, Lord Digby","Clarendon State Papers vol. I, no. 2320","'A portion of the letter interspersed with cypher, which is not decyphered.'"),
 (1645,"1645 (entry before the Jermyn letter of 31 Aug)","Sir Henry Bennet (Rome) to a lord: great part in cypher, 'still undecyphered' (praises Digby's negotiations, wants recall)","Sir Henry Bennet → unknown","Clarendon State Papers vol. I, entry before the Jermyn letter of Aug 31 (OCR number 1946/1947)","'A great part of this is in cypher, which is still undecyphered.'")]:
    add(y,d,t,corr,"unknown","English","England",CV1,pos,"A" if "Ormond" in corr else "B",
      "Ogle & Bliss: "+note+" Neighbouring Ormond ciphers are decyphered in the same volume (e.g. 'Decyphered on following paper'), so the royalist Charles-Ormond key can be rebuilt from siblings.",
      "Charles I's secret instructions in the Irish negotiations of 1645-48 (Glamorgan treaty, Ormond peace).",4 if "Ormond" in corr or "Nicholas" in corr else 3,3,3,
      "View Bodleian MS Clarendon (images via Bodleian Digital if available); build the key from the 'decyphered' siblings.",
      prior="open (checked 28 Oct 2026: repo catalogue says Ormond-Hyde ciphers are known for other letters; no reading of these entries; cryptiana not re-read)",q="not decyphered")
for (y,d,t,corr,pos,note,vol) in [
 (1659,"12/22 May 1659","De Vieux to Du Chastel: intercepted letter, copy by Marces, partly in cipher not deciphered","Chevalier de Vieux → Du Chastel","Clarendon State Papers vol. IV, entry (571); also Cal. S.P. Dom. 1658-9 p. 346","Partly in cipher not deciphered; copy by Marces.",CV4),
 (1659,"18/28 Jun 1659","Hyde to Bennet no. 3: passage in undeciphered cipher (Parliament, Fleetwood, Monck; expresses promise wonders)","Sir Edward Hyde → Sir Henry Bennet","Clarendon State Papers vol. IV, Vol. 62 f. 208","[In undeciphered cipher:] 'Several expresses from England promise wonderful things if the King will come'.",CV4),
 (1659,"Jul 1659","Intercepted letter, French, several passages in cipher not deciphered (taxes, Lockhart at Dunkirk)","unknown (intercepted by Marces)","Clarendon State Papers vol. IV, Vol. 63 ff. 33-4","[Several passages in cipher not deciphered follow.]",CV4),
 (1659,"Aug 1659","Enclosure: a note in undeciphered cipher with the Lockhart/Mazarin conference letters","unknown","Clarendon State Papers vol. IV, Vol. 64 f. 220v","Enclosure: a note in undeciphered cipher (220v).",CV4),
 (1659,"1659 (undated)","John Crosby to William Redcrosse [Thurloe?]: intercepted letter almost entirely in undeciphered cipher","John Crosby → William Redcrosse","Clarendon State Papers vol. IV, f. 352 (copy by Marces)","A brief note almost entirely in undeciphered cipher.",CV4),
 (1660,"17 Feb 1660","Mordaunt to Sec. Nicholas (?): address in cipher not deciphered, latter part deciphered","Viscount Mordaunt → Sec. Nicholas?","Clarendon State Papers vol. IV, Vol. 69 ff. 164-5","The latter part in deciphered cipher. Address in cipher not deciphered.",CV4),
 (1660,"10/20 May 1660","[Marces] (Paris) to Hyde: 4.5 lines undeciphered cipher","Marces → Sir Edward Hyde","Clarendon State Papers vol. V, May 1660","[4.5 lines undeciphered cipher.]","calendarofclaren05bodl")]:
    add(y,d,t,corr,"unknown","English","England",vol,pos,"B",
      "Routledge: "+note+" The Hyde/Marces royalist ciphers of 1659-60 are largely deciphered in the same volumes; these are the remaining gaps.",
      "Restoration conspiracy intelligence; Marces was Hyde's Paris interceptor.",2,3,2,
      "Bodleian MS Clarendon 62-72; try the royalist key from deciphered siblings; Tomokiyo has Hyde keys.",
      prior="open (checked 28 Oct 2026: repo targets/hyde covers other 1659 letters; not these items)",q="undeciphered cipher")
add(1661,"1/11 Nov 1661","Newsletter almost entirely in undeciphered cipher, French, 4 pp.","unknown","unknown","French","England","calendarofclaren05bodl","Clarendon State Papers vol. V, Vol. 73 ff. 249-50","C",
 "Routledge: 'Newsletter. [Almost entirely in undeciphered cipher.] Fr. 4 pp.'","A rare long ciphered newsletter in Hyde's papers after the Restoration.",3,2,4,"Bodleian MS Clarendon 73.",prior=GEN_PRIOR.replace("importance below 3","importance 3: cryptiana not searched"),q="Almost entirely in undeciphered cipher")
# ---------- Commonwealth Domestic ----------
CW="cu31924091770432"
for (d,pos,corr,nt,imp) in [
 ("Jan 1656 (item 67, Vol. CXXIII)","CSP Domestic Commonwealth 1655-56, no. 67 (see note p. 122)","Thomas Ross → Sec. Nicholas, Cologne","2.75 pp.; italics are cyphers, undecyphered; Norfolk and Suffolk rising (Hobart)",3),
 ("Jan 1656 (item 88)","CSP Domestic Commonwealth 1655-56, no. 88","T. Ross → Sec. Nicholas","1 p.; italics cypher, undecyphered; private articles of the treaty with France",2),
 ("Feb 1656 (Vol. CXXIV, item 13)","CSP Domestic Commonwealth 1655-56, no. 13","D. Wise → T. Ross","2 pp.; italics in cypher chiefly undecyphered; Cromwell and Spain",2),
 ("Feb 1656 (item 76)","CSP Domestic Commonwealth 1655-56, no. 76","Sec. Nicholas → Joseph Jane","2.75 pp.; italics in cypher, not deciphered; stars represent words with no key",3),
 ("21 Feb 1656 (item 89)","CSP Domestic Commonwealth 1655-56, no. 89","T. Ross → Sec. Nicholas, Cologne","2 pp.; italics cyphers undecyphered; Pile's mistress means the King's affairs",2),
 ("29 Feb 1656 (item 109)","CSP Domestic Commonwealth 1655-56, no. 109","T. Ross → Sec. Nicholas","1 p.; italics in cypher, undecyphered",2),
 ("22 Mar 1656 (item 55)","CSP Domestic Commonwealth 1655-56, no. 55 (Vol. CXXV)","T. Ross → Sec. Nicholas, Cologne","2 pp.; italics cyphers undecyphered; Massey and the Presbyterians",2),
 ("20 May 1656 (item 50)","CSP Domestic Commonwealth 1655-56, no. 50","T. Ross → Nicholas","2 pp.; italics cyphers undecyphered; Hopton, Pile, Blake",2),
 ("Jun 1656 (item 62)","CSP Domestic Commonwealth 1655-56, no. 62 (Mrs Ross to Jack Trethwey, enclosing John Weston to the King)","Mrs Ross / John Weston → Charles II","0.5 p.; italics cyphers undecyphered; Wildman proposal",2),
 ("Jun 1656 (item 107)","CSP Domestic Commonwealth 1655-56, no. 107","T. Ross → Sec. Nicholas, Bruges","2.5 pp.; italics cyphers undecyphered; decimation, Valenciennes",2)]:
    add(1656,d,"Royalist agent letter, %s: italicised cipher passages undecyphered (Ross/Nicholas series)"%d,corr,"Cologne/Bruges","English","England",CW,pos,"A",
      "Green: "+nt+". Preface: the Nicholas-Jane letters are 'ordinary figure cypher' decyphered from Jane's interlineations; the Ross-Nicholas ones use another cypher with no key. The editor deciphered much of the series, so the gaps are small.",
      "Charles II's exile court intelligence (after Penruddock, the Spanish alliance).",imp,3,3,
      "TNA SP 18 vol. 123-125; rebuild the key from the 'decyphered' parts of siblings.",
      prior="open (checked 28 Oct 2026: preface says no key survives for the Ross series; Thurloe State Papers not searched)",q="italics cyphers undecyphered")
# ---------- Heathcote ----------
H="cu31924028044646"
add(1664,"13 Jun 1664","Sir Henry Bennet to Sir Richard Fanshawe: six pages of cipher, undeciphered (duplicate of cipher parts of letters of 8 Apr, 12 May, 2 Jun)","Sir Henry Bennet → Sir Richard Fanshawe","Whitehall → Madrid","English","England",H,"HMC Heathcote MSS (Fanshawe papers), 13 Jun 1664","A",
 "HMC 1899: 'Six pages of cipher, undeciphered, headed: This is a duplicate of that part of Mr. Secretary's letters in cipher to your Excellency of April 8th, May 12th and June 2nd ...'. The 6 Oct 1664 item says the key 'is amongst the papers'.",
 "Anglo-Spanish policy 1664, Fanshawe's embassy at Madrid.",4,4,2,"Locate the Heathcote collection (HMC report p. cited in OCR); the key is in the same papers per HMC.",
 prior="open (checked 28 Oct 2026: HMC Heathcote full text only; no published decipherment found; Fanshawe's Letters (1702) not searched)",q="pages of cipher, undeciphered")
add(1664,"6 Oct 1664","Sir Henry Bennet to Sir Richard Fanshawe: eight pages of cipher, not deciphered, 'but the key for which is amongst the papers'","Sir Henry Bennet → Sir Richard Fanshawe","Whitehall → Madrid","English","England",H,"HMC Heathcote MSS (Fanshawe papers), 6 Oct 1664","A",
 "HMC: 'Eight pages of cipher, not deciphered, but the key for which is amongst the papers. They prove to be the cipher part of the letter dated August 25th in the printed letters (p. 283)'. So the plaintext is in print: a ready crib.",
 "Anglo-Spanish negotiations of 1664; a crib-plus-key cipher pair.",3,5,1,"Find the HMC Heathcote collection and Fanshawe's printed letter of 25 Aug 1664, p. 283.",
 prior="open (checked 28 Oct 2026: HMC text says the plaintext is in print; not read against it)",q="key for which is amongst the papers")
# ---------- JQA ----------
J="fordsjohnadams04adamrich"
for (d,pos,nt,y) in [("June 1811","Writings of J. Q. Adams vol. IV, despatch from St Petersburg to the Secretary of State, 22 Jun 1811 area","half a line of cipher not deciphered (Russia, Turkey, the two provinces)",1811),
                     ("2 Nov 1811","Writings of J. Q. Adams vol. IV, despatch to the Secretary of State, St Petersburg, 2 Nov 1811","three groups of cipher noted as in error and undeciphered",1811),
                     ("27 May 1812","Writings of J. Q. Adams vol. IV, despatch to the Secretary of State, St Petersburg, 27 May 1812","two and three lines of cypher not decyphered (Sweden's neutrality, Orders in Council)",1812),
                     ("25 Jun 1812","Writings of J. Q. Adams vol. IV, despatch to the Secretary of State, St Petersburg, 25 Jun 1812","remainder of letter, apart from a few lines, undecyphered",1812)]:
    add(y,d,"John Quincy Adams (St Petersburg) to Secretary of State Monroe, %s: cypher passages not decyphered"%d,"John Quincy Adams → James Monroe (Secretary of State)","St Petersburg","English","Americas",J,pos,"B",
      "Editor Ford: "+nt+". State Department diplomatic cipher of the period; the repo has a jqa/ working folder and erving1807.",
      "Russia on the eve of Napoleon's invasion, in US despatches.",3,3,3,"Compare with existing repo JQA work; Library of Congress/NARA despatch images.",
      prior="open (checked 28 Oct 2026: repo notes JQA is not in the Armstrong code; Ford text states undecyphered; Adams Papers microfilm not consulted)",q="cypher not decyphered")
# ---------- Kaunitz ----------
add(1750,"1750 (Kaunitz-Koch)","Puisieux to d'Hautefort: letter in 'le chiffre non dechiffre' / 'chiffre a quadro', read at Vienna only in part","Marquis de Puisieux → comte d'Hautefort","Versailles → Vienna","French","France","correspondancese00kaun","Kaunitz-Koch secret correspondence, the postscript beginning 'J'avois tort de marquer a V.E.'","B",
 "Text: 'il luy a ecrit, mais dans le chiffre non dechiffre ... le bonheur veut que Monsieur de Puissieux continue a se servir de celuy que nous avons' and 'chiffre a quadro qu'ils croyent indechiffrable'. The Austrians read one French cipher ('the one we have') but not the 'quadro' cipher.",
 "Austrian black-chamber reports on French cipher traffic.",3,2,4,"Find the underlying HHStA Vienna record; the book is the secret correspondence of Kaunitz with Koch.",
 prior="open (checked 28 Oct 2026: not found in repo; Lasry/Waldispuehl not searched)",q="chiffre non déchiffré")
