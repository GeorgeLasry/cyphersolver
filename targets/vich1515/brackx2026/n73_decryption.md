# vich1515: the decode aligned with the transcription

AHN Estado 8715 N.73. For each line: `T` the repository's transcription (`work_n73_tokens.txt`, `?` removed); `S` the
labels as used for decoding where they differ: the token splits (`sin`/`sim`, `X` as `Xr`/`Xs`/`Xz`, `yin`, `ynb`,
`xny`, `sifa`, `pefa` read per token, see `n73_sin_x_tokens.tsv` and `n73_codebook.md`) and four transcription
corrections made on the image (10.24 `OT`, 16.26 `suq`, 18.3 `rie`, 26.25 `PHI`); `V` each token's value; `D` the
decoded line. In `V` and `D`: signs in lower case; firm code groups in CAPITALS; tentative groups in {braces};
unread groups as [group]; a sign with no value as <SIGN>. Generated from `n73_tokens.tsv`.

```
  1 T: sef sio tok RS RH B8 TH PHI sin O X KH no TH soo PHI su Z PHI rak su RS RH B8 PHI TH
    S: sef sio tok RS RH B8 TH PHI sim O Xs KH no TH soo PHI su Z PHI rak su RS RH B8 PHI TH
    V: sef=[sef] sio=ESTA tok=HA RS=u RH=e B8=r TH=o PHI=s sim=EN O=a Xs=s KH=i no=T TH=o soo=ESTO PHI=s su=DI Z=a PHI=s rak=CON su=DI RS=u RH=e B8=r PHI=s TH=o
    D: [sef]ESTAHAuerosENasiToESTOsDIasCONDIuerso
  2 T: CD TH CII RH TH PHI yob xil YH yob beq YH RS gso no KH ZO Z xno FH LO RH yob xnl Z xad PHI
    V: CD=c TH=o CII=<CII> RH=e TH=o PHI=s yob=POR xil=[xil] YH=y yob=POR beq=TIERRA YH=y RS=u gso=L no=T KH=i ZO=m Z=a xno=ME FH=n LO=t RH=e yob=POR xnl=MAR Z=a xad=LO PHI=s
    D: co<CII>eosPOR[xil]yPORTIERRAyuLTimaMEntePORMARaLOs
  3 T: QH RS KH sud sio TH ne RS V B8 zo KH ZH zoq xed PHI dug PHI sud QH V RS KH BO CD see OT Z xo
    V: QH=x RS=u KH=i sud=DE sio=ESTA TH=o ne=[ne] RS=u V=<V> B8=r zo=[zo] KH=i ZH=e zoq=[zoq] xed=LA PHI=s dug=UUESTRA PHI=s sud=DE QH=x V=<V> RS=u KH=i BO=i CD=c see=DEL OT=c Z=a xo=RA
    D: xuiDEESTAo[ne]u<V>r[zo]ie[zoq]LAsUUESTRAsDEx<V>uiicDELcaRA
  4 T: GS TH YH sud GS TH OT sud sio zre beq yob beq xed PHI zre sud X KH PHI zre xno tok RS RH YH PHI
    S: GS TH YH sud GS TH OT sud sio zre beq yob beq xed PHI zre sud Xz KH PHI zre xno tok RS RH YH PHI
    V: GS=d TH=o YH=y sud=DE GS=d TH=o OT=c sud=DE sio=ESTA zre=QUE beq=TIERRA yob=POR beq=TIERRA xed=LA PHI=s zre=QUE sud=DE Xz=z KH=i PHI=s zre=QUE xno=ME tok=HA RS=u RH=e YH=y PHI=s
    D: doyDEdocDEESTAQUETIERRAPORTIERRALAsQUEDEzisQUEMEHAueys
  5 T: sin O B8 KH no TH yob xnl xeb xed PHI V RH pn zoq YH pab xed PHI xiz PHI zre yob xad PHI see
    S: sim O B8 KH no TH yob xnl xeb xed PHI V RH pn zoq YH pab xed PHI xiz PHI zre yob xad PHI see
    V: sim=EN O=a B8=r KH=i no=T TH=o yob=POR xnl=MAR xeb=NO xed=LA PHI=s V=<V> RH=e pn=[pn] zoq=[zoq] YH=y pab=AHUNQUE xed=LA PHI=s xiz=[xiz] PHI=s zre=QUE yob=POR xad=LO PHI=s see=DEL
    D: ENariToPORMARNOLAs<V>e[pn][zoq]yAHUNQUELAs[xiz]sQUEPORLOsDEL
  6 T: PHI dug PHI gso RH no B8 Z PHI X no saq PHI xeb PHI TH FH ynb tok RS RH B8 OT xed X RH B8 rak
    S: PHI dug PHI gso RH no B8 Z PHI Xz no saq PHI xeb PHI TH FH ynbp tok RS RH B8 OT xed Xs RH B8 rak
    V: PHI=s dug=UUESTRA PHI=s gso=L RH=e no=T B8=r Z=a PHI=s Xz=z no=T saq=[saq] PHI=s xeb=NO PHI=s TH=o FH=n ynbp=PARA tok=HA RS=u RH=e B8=r OT=c xed=LA Xs=s RH=e B8=r rak=CON
    D: sUUESTRAsLeTraszT[saq]sNOsonPARAHAuercLAserCON
  7 T: sen PHI yaz KH RH PHI Z B8 KH GS TH see CD RS YH GS Z GS TH sim zre suo RS Z sud xeb no sin
    S: sen PHI yaz KH RH PHI Z B8 KH GS TH see CD RS YH GS Z GS TH sim zre suo RS Z sud xeb no sim
    V: sen=ELLA PHI=s yaz=PERO KH=i RH=e PHI=s Z=a B8=r KH=i GS=d TH=o see=DEL CD=c RS=u YH=y GS=d Z=a GS=d TH=o sim=EN zre=QUE suo=ESTA RS=u Z=a sud=DE xeb=NO no=T sim=EN
    D: ELLAsPEROiesaridoDELcuydadoENQUEESTAuaDENOTEN
  8 T: RH B8 xnp PHI su Z PHI tok RS KH Z gso RH no B8 Z PHI dug PHI YH dej Z B8 sin CT TH DH sud B8 Z xad
    V: RH=e B8=r xnp=MUCHO PHI=s su=DI Z=a PHI=s tok=HA RS=u KH=i Z=a gso=L RH=e no=T B8=r Z=a PHI=s dug=UUESTRA PHI=s YH=y dej=[dej] Z=a B8=r sin=ES CT=p TH=o DH=n sud=DE B8=r Z=a xad=LO
    D: erMUCHOsDIasHAuiaLeTrasUUESTRAsy[dej]arESponDEraLO
  9 T: rak no sin KH GS TH sin sen PHI su AH TH zre xeb CT RS RH GS TH sud QH Z X sud suo X
    S: rak no sim KH GS TH sim sen PHI su AH TH zre xeb CT RS RH GS TH sud QH Z Xr sud suo Xr
    V: rak=CON no=T sim=EN KH=i GS=d TH=o sim=EN sen=ELLA PHI=s su=DI AH=g TH=o zre=QUE xeb=NO CT=p RS=u RH=e GS=d TH=o sud=DE QH=x Z=a Xr=r sud=DE suo=ESTA Xr=r
    D: CONTENidoENELLAsDIgoQUENOpuedoDExarDEESTAr
 10 T: xns xin rak no sin no TH sud RS ZH B8 zre yob xed PHI TH N8 RH X RS BO YH xad O RS
    S: xns xin rak no sim no TH sud RS ZH B8 zre yob xed PHI TH N8 RH Xr RS BO YH xad OT RS
    V: xns=MUY xin=MAL rak=CON no=T sim=EN no=T TH=o sud=DE RS=u ZH=e B8=r zre=QUE yob=POR xed=LA PHI=s TH=o N8=b RH=e Xr=r RS=u BO=i YH=y xad=LO OT=c RS=u
    D: MUYMALCONTENToDEuerQUEPORLAsoberuiyLOcu
 11 T: B8 Z sud be sud xeb zre B8 RH X sin CT RH B8 Z X O zre xny sem bne tir bne rak sin
    S: B8 Z sud be sud xeb zre B8 RH Xr sin CT RH B8 Z Xr O zre xnyn sem bne tir bne rak sin
    V: B8=r Z=a sud=DE be=SUYCOS sud=DE xeb=NO zre=QUE B8=r RH=e Xr=r sin=ES CT=p RH=e B8=r Z=a Xr=r O=a zre=QUE xnyn=NUESTRO sem=EXERCITO bne=SE tir=IUNTA bne=SE rak=CON sin=ES
    D: raDESUYCOSDENOQUErerESperaraQUENUESTROEXERCITOSEIUNTASECONES
 12 T: PHI YH yob xed B8 RH xoo bae TH FH sin xoo bay YH poz sud no Z B8 GS O X bon sin
    S: PHI YH yob xed B8 RH xoo bae TH FH sin xoo bay YH poz sud no Z B8 GS O Xr bon sim
    V: PHI=s YH=y yob=POR xed=LA B8=r RH=e xoo=MI bae=SI TH=o FH=n sin=ES xoo=MI bay=UISORREY YH=y poz=CAPITAN GENERAL sud=DE no=T Z=a B8=r GS=d O=a Xr=r bon=TANTO sim=EN
    D: syPORLAreMISIonESMIUISORREYyCAPITAN GENERALDETardarTANTOEN
 13 T: tir B8 bne bne tok dam FH yin no TH beo PHI xed PHI reh PHI sud teb sin sim CT RH
    S: tir B8 bne bne tok dam FH yinp no TH beo PHI xed PHI reh PHI sud teb sim siml CT RH
    V: tir=IUNTA B8=r bne=SE bne=SE tok=HA dam=YA FH=n yinp=PUES no=T TH=o beo=TODA PHI=s xed=LA PHI=s reh=COSA PHI=s sud=DE teb=ITALIA sim=EN siml=EL CT=p RH=e
    D: IUNTArSESEHAYAnPUESToTODAsLAsCOSAsDEITALIAENELpe
 14 T: gso KH AH B8 TH zre TH YH sio FH yaz ynb rak dah X ip xin ZO Z B8 O RS KH SL Z GS TH
    S: gso KH AH B8 TH zre TH YH sio FH yaz ynbp rak dah Xs ip xin ZO Z B8 O RS KH SL Z GS TH
    V: gso=L KH=i AH=g B8=r TH=o zre=QUE TH=o YH=y sio=ESTA FH=n yaz=PERO ynbp=PARA rak=CON dah=UOS Xs=s ip=MUCHO xin=MAL ZO=m Z=a B8=r O=a RS=u KH=i SL=ll Z=a GS=d TH=o
    D: LigroQUEoyESTAnPEROPARACONUOSsMUCHOMALmarauillado
 15 T: YH CT RH TH B8 rak no sin no TH soo KH sud RS RH B8 xed MH xed zre X Z see yem
    S: YH CT RH TH B8 rak no sim no TH soo KH sud RS RH B8 xed MH xed zre Xz Z see yem
    V: YH=y CT=p RH=e TH=o B8=r rak=CON no=T sim=EN no=T TH=o soo=ESTO KH=i sud=DE RS=u RH=e B8=r xed=LA MH=f xed=LA zre=QUE Xz=z Z=a see=DEL yem=PAPA
    D: ypeorCONTENToESTOiDEuerLAfLAQUEzaDELPAPA
 16 T: YH RS RS O FH sud LO RH B8 xoo FH O GS TH suo sud gak OT RH X no Z B8 bne rak sug xeb
    S: YH RS RS O FH sud LO RH B8 xoo FH O GS TH suo sud gak OT RH Xr no Z B8 bne rak suq xeb
    V: YH=y RS=u RS=u O=a FH=n sud=DE LO=t RH=e B8=r xoo=MI FH=n O=a GS=d TH=o suo=ESTA sud=DE gak=CON OT=c RH=e Xr=r no=T Z=a B8=r bne=SE rak=CON suq=FRANCESES xeb=NO
    D: yuuanDEterMInadoESTADECONcerTarSECONFRANCESESNO
 17 T: AH RS Z X GS O FH GS TH sin san xad zre sio OT Z CT KH no RS xed GS TH zre xaz sud
    S: AH RS Z Xr GS O FH GS TH sim san xad zre sio OT Z CT KH no RS xed GS TH zre xaz sud
    V: AH=g RS=u Z=a Xr=r GS=d O=a FH=n GS=d TH=o sim=EN san=ELLO xad=LO zre=QUE sio=ESTA OT=c Z=a CT=p KH=i no=T RS=u xed=LA GS=d TH=o zre=QUE xaz=NINGUNO sud=DE
    D: guardandoENELLOLOQUEESTAcapiTuLAdoQUENINGUNODE
 18 T: xad PHI rue PHI xeb CT RS RH GS Z tok X RH B8 yin ynb no B8 RH AH RS Z rak ynb FH PH RS
    S: xad PHI rie PHI xeb CT RS RH GS Z tok Xz RH B8 yinz ynb no B8 RH AH RS Z rak ynb FH PH RS
    V: xad=LO PHI=s rie=CONFEDERADO PHI=s xeb=NO CT=p RS=u RH=e GS=d Z=a tok=HA Xz=z RH=e B8=r yinz=PAZ ynb=NI no=T B8=r RH=e AH=g RS=u Z=a rak=CON ynb=NI FH=n PH=g RS=u
    D: LOsCONFEDERADOsNOpuedaHAzerPAZNITreguaCONNIngu
 19 T: yom bae FH PHI Z N8 KH GS RS B8 KH O YH dik sud bao PHI xad PHI rie PHI YH yin sin soo tok
    S: yom bae FH PHI Z N8 KH GS RS B8 KH O YH dik sud bao PHI xad PHI rie PHI YH yinp sim soo tok
    V: yom=PRINCIPE bae=SI FH=n PHI=s Z=a N8=b KH=i GS=d RS=u B8=r KH=i O=a YH=y dik=VOLUNTAD sud=DE bao=TODO PHI=s xad=LO PHI=s rie=CONFEDERADO PHI=s YH=y yinp=PUES sim=EN soo=ESTO tok=HA
    D: PRINCIPESInsabiduriayVOLUNTADDETODOsLOsCONFEDERADOsyPUESENESTOHA
 20 T: zre N8 B8 O GS TH xed seg OT Z CT KH no RS xed OT KH TH FH xeb sin CT RH B8 TH rak sin
    S: zre N8 B8 O GS TH xed seg OT Z CT KH no RS xed OT KH TH FH xeb sin CT RH B8 TH rak sim
    V: zre=QUE N8=b B8=r O=a GS=d TH=o xed=LA seg=DICHA OT=c Z=a CT=p KH=i no=T RS=u xed=LA OT=c KH=i TH=o FH=n xeb=NO sin=ES CT=p RH=e B8=r TH=o rak=CON sim=EN
    D: QUEbradoLADICHAcapiTuLAcionNOESperoCONEN
 21 T: xez yee reh xed tok sud PH RS Z B8 GS O X pab sin dah tok dam xnk sud X KH PHI
    S: xez yee reh xed tok sud PH RS Z B8 GS O Xr pab sim dah tok dam xnk sud Xz KH PHI
    V: xez=NINGUNA yee=OTRA reh=COSA xed=LA tok=HA sud=DE PH=g RS=u Z=a B8=r GS=d O=a Xr=r pab=AHUNQUE sim=EN dah=UOS tok=HA dam=YA xnk=COMO sud=DE Xz=z KH=i PHI=s
    D: NINGUNAOTRACOSALAHADEguardarAHUNQUEENUOSHAYACOMODEzis
 22 T: CT X TH xno no KH GS TH zre Z X sin no Z B8 O xed seg yin rak soq bae FH CT RH X KH
    S: CT Xr TH xno no KH GS TH zre Z Xs sim no Z B8 O xed seg yinz rak soq bae FH CT RH Xr KH
    V: CT=p Xr=r TH=o xno=ME no=T KH=i GS=d TH=o zre=QUE Z=a Xs=s sim=EN no=T Z=a B8=r O=a xed=LA seg=DICHA yinz=PAZ rak=CON soq=FRANCIA bae=SI FH=n CT=p RH=e Xr=r KH=i
    D: proMETidoQUEasENTaraLADICHAPAZCONFRANCIASInperi
 23 T: RS KH X dem sud xed PHI OT Z CT no RS xed CD KH TH FH sin zre ral sim suh YH OT TH xoo
    S: RS KH Xz dem sud xed PHI OT Z CT no RS xed CD KH TH FH sin zre ral siml suh YH OT TH xoo
    V: RS=u KH=i Xz=z dem=YO sud=DE xed=LA PHI=s OT=c Z=a CT=p no=T RS=u xed=LA CD=c KH=i TH=o FH=n sin=ES zre=QUE ral=CON siml=EL suh=EMPERADOR YH=y OT=c TH=o xoo=MI
    D: uizYODELAscapTuLAcionESQUECONELEMPERADORycoMI
 24 T: AH TH bip Z X sin no Z GS O PHI YH pib AH RS Z X GS O B8 Z nab zre yob xed OT Z CT KH no
    S: AH TH bip Z Xs sim no Z GS O PHI YH pib AH RS Z Xr GS O B8 Z nab zre yob xed OT Z CT KH no
    V: AH=g TH=o bip=TIENE Z=a Xs=s sim=EN no=T Z=a GS=d O=a PHI=s YH=y pib=ASSIMISMO AH=g RS=u Z=a Xr=r GS=d O=a B8=r Z=a nab=LO zre=QUE yob=POR xed=LA OT=c Z=a CT=p KH=i no=T
    D: goTIENEasENTadasyASSIMISMOguardaraLOQUEPORLAcapiT
 25 T: RS xed OT KH TH FH sud xed xif AH RH FH ZH B8 pif suo OT Z CT KH no RS xed GS TH YH zre
    V: RS=u xed=LA OT=c KH=i TH=o FH=n sud=DE xed=LA xif=LIGA AH=g RH=e FH=n ZH=e B8=r pif=AL suo=ESTA OT=c Z=a CT=p KH=i no=T RS=u xed=LA GS=d TH=o YH=y zre=QUE
    D: uLAcionDELALIGAgenerALESTAcapiTuLAdoyQUE
 26 T: beo RS RH X zre sim suh YH dem YH be ZH RS KH bae RH B8 ZH ZO TH PHI B8 RH bae B8 no KH X sif
    S: beo RS RH Xz zre siml suh YH dem YH be ZHq RS KH bae RH B8 ZH ZO TH PHI B8 RH bae PHI no KH Xr sifa
    V: beo=TODA RS=u RH=e Xz=z zre=QUE siml=EL suh=EMPERADOR YH=y dem=YO YH=y be=SUYCOS ZHq=q RS=u KH=i bae=SI RH=e B8=r ZH=e ZO=m TH=o PHI=s B8=r RH=e bae=SI PHI=s no=T KH=i Xr=r sifa=AL
    D: TODAuezQUEELEMPERADORyYOySUYCOSquiSIeremosreSIsTirAL
 27 T: zuy YH sin no sin sud B8 sin ZH CD tok B8 PSI RH sud teb sin pnk B8 Z ynb san xnk
    S: zuy YH sim no sim sud B8 sim ZH CD tok B8 PSI RH sud teb sim pnk B8 Z ynbp san xnk
    V: zuy=REY DE FRANCIA YH=y sim=EN no=T sim=EN sud=DE B8=r sim=EN ZH=e CD=c tok=HA B8=r PSI=l RH=e sud=DE teb=ITALIA sim=EN pnk=AYUDA B8=r Z=a ynbp=PARA san=ELLO xnk=COMO
    D: REY DE FRANCIAyENTENDErENecHArleDEITALIAENAYUDAraPARAELLOCOMO
 28 T: yob xed seg OT Z CT KH no RS xed CD KH TH ZO sin yed yob zre suo yin zre
    S: yob xed seg OT Z CT KH no RS xed CD KH TH ZO sin yed yob zre suo yinz zre
    V: yob=POR xed=LA seg=DICHA OT=c Z=a CT=p KH=i no=T RS=u xed=LA CD=c KH=i TH=o ZO=m sin=ES yed=OBLIGADO yob=POR zre=QUE suo=ESTA yinz=PAZ zre=QUE
    D: PORLADICHAcapiTuLAciomESOBLIGADOPORQUEESTAPAZQUE
 29 T: ZH RS KH RH B8 ZH Z bne FH no Z B8 rak suq xed tok X oso yob sey B8 OT Z YH CT LAM
    S: ZHq RS KH RH B8 ZH Z bne FH no Z B8 rak suq xed tok Xz oso yob sey B8 OT Z YH CT LAMu
    V: ZHq=q RS=u KH=i RH=e B8=r ZH=e Z=a bne=SE FH=n no=T Z=a B8=r rak=CON suq=FRANCESES xed=LA tok=HA Xz=z oso=E yob=POR sey=FUE B8=r OT=c Z=a YH=y CT=p LAMu=u
    D: quiereaSEnTarCONFRANCESESLAHAzEPORFUErcaypu
 30 T: B8 Z xnz sud bao soo xnk V RH sag dem xeb OT B8 RH TH ynb OT B8 RH ZH B8 RH bae xeb
    V: B8=r Z=a xnz=NECESIDAD sud=DE bao=TODO soo=ESTO xnk=COMO V=<V> RH=e sag=DICHO dem=YO xeb=NO OT=c B8=r RH=e TH=o ynb=NI OT=c B8=r RH=e ZH=e B8=r RH=e bae=SI xeb=NO
    D: raNECESIDADDETODOESTOCOMO<V>eDICHOYONOcreoNIcreereSINO
 31 T: xad zre yob ynh doc RH B8 ZH 7H yaz dah pif yem xeb gso RH tok RS ZH YH PHI sud
    V: xad=LO zre=QUE yob=POR ynh=OBRA doc=UI RH=e B8=r ZH=e 7H=<7H> yaz=PERO dah=UOS pif=AL yem=PAPA xeb=NO gso=L RH=e tok=HA RS=u ZH=e YH=y PHI=s sud=DE
    D: LOQUEPOROBRAUIere<7H>PEROUOSALPAPANOLeHAueysDE
 32 T: Z PHI TH ZO Z B8 xed sud X KH X OT Z xed N8 B8 Z xez sud soo bae xeb baf sin MH TH B8
    S: Z PHI TH ZO Z B8 xed sud Xs KH Xs OT Z xed N8 B8 Z xez sud soo bae xeb baf sin MH TH B8
    V: Z=a PHI=s TH=o ZO=m Z=a B8=r xed=LA sud=DE Xs=s KH=i Xs=s OT=c Z=a xed=LA N8=b B8=r Z=a xez=NINGUNA sud=DE soo=ESTO bae=SI xeb=NO baf=SOLO sin=ES MH=f TH=o B8=r
    D: asomarLADEsiscaLAbraNINGUNADEESTOSINOSOLOESfor
 33 T: OT O B8 gso RH sud xoo ynz ynb zre yob suo Z GS RS RH CD bae GS Z no zre yob PHI TH
    V: OT=c O=a B8=r gso=L RH=e sud=DE xoo=MI ynz=PARTE ynb=NI zre=QUE yob=POR suo=ESTA Z=a GS=d RS=u RH=e CD=c bae=SI GS=d Z=a no=T zre=QUE yob=POR PHI=s TH=o
    D: carLeDEMIPARTENIQUEPORESTAaduecSIdaTQUEPORso
 34 T: N8 RH B8 RS KH Z YH gso TH O RS B8 Z sud be tok RS RH ZO TH PHI zoq xeb sud PHI ZO Z YH
    V: N8=b RH=e B8=r RS=u KH=i Z=a YH=y gso=L TH=o O=a RS=u B8=r Z=a sud=DE be=SUYCOS tok=HA RS=u RH=e ZO=m TH=o PHI=s zoq=[zoq] xeb=NO sud=DE PHI=s ZO=m Z=a YH=y
    D: beruiayLoauraDESUYCOSHAuemos[zoq]NODEsmay
 35 T: ynb sin MH xed zre X OT Z pin pud sio rak xom sin MH RS ZH ZO TH YH Z
    S: ynb sim MH xed zre Xs OT Z pin pud sio rak xom sin MH RS ZH ZO TH YH Z
    V: ynb=NI sim=EN MH=f xed=LA zre=QUE Xs=s OT=c Z=a pin=[pin] pud=[pud] sio=ESTA rak=CON xom=[xom] sin=ES MH=f RS=u ZH=e ZO=m TH=o YH=y Z=a
    D: NIENfLAQUEsca[pin][pud]ESTACON[xom]ESfuemoya
 36 T: ynb ZO TH yin gso RH zre GS Z ZO TH PHI bon PHI yom PHI QH TH KH Z xeb PHI YH sin
    S: ynb ZO TH yinpt gso RH zre GS Z ZO TH PHI bon PHI yom PHI QH TH KH Z xeb PHI YH sim
    V: ynb=NI ZO=m TH=o yinpt=PUES gso=L RH=e zre=QUE GS=d Z=a ZO=m TH=o PHI=s bon=TANTO PHI=s yom=PRINCIPE PHI=s QH=x TH=o KH=i Z=a xeb=NO PHI=s YH=y sim=EN
    D: NImoPUESLeQUEdamosTANTOsPRINCIPEsxoiaNOsyEN
 37 T: zek zre gso RH tok RS RH ZO DH TH PHI sud pnk PHI YH CT TH DH RH B8 xoy PHI yez PHI YH
    V: zek=[zek] zre=QUE gso=L RH=e tok=HA RS=u RH=e ZO=m DH=n TH=o PHI=s sud=DE pnk=AYUDA PHI=s YH=y CT=p TH=o DH=n RH=e B8=r xoy=NUESTRA PHI=s yez=PERSONA PHI=s YH=y
    D: [zek]QUELeHAuemnosDEAYUDAsyponerNUESTRAsPERSONAsy
 38 T: suo GS TH PHI yob bae PHI YH yob xed YH AH Q KH Z rok SS RS ZH sin zih zre gso RH
    V: suo=ESTA GS=d TH=o PHI=s yob=POR bae=SI PHI=s YH=y yob=POR xed=LA YH=y AH=g Q=<Q> KH=i Z=a rok={S} SS=q RS=u ZH=e sin=ES zih=[zih] zre=QUE gso=L RH=e
    D: ESTAdosPORSIsyPORLAyg<Q>ia{S}queES[zih]QUELe
 39 T: SS RS KH bae RH bne TH MH sin sud X YH yin rak sin pnk sud sod PHI YH sud bon PHI yom PHI RS RH
    S: SS RS KH bae RH bne TH MH sim sud Xr YH yinpt rak sin pnk sud sod PHI YH sud bon PHI yom PHI RS RH
    V: SS=q RS=u KH=i bae=SI RH=e bne=SE TH=o MH=f sim=EN sud=DE Xr=r YH=y yinpt=PUES rak=CON sin=ES pnk=AYUDA sud=DE sod=DIO PHI=s YH=y sud=DE bon=TANTO PHI=s yom=PRINCIPE PHI=s RS=u RH=e
    D: quiSIeSEofENDEryPUESCONESAYUDADEDIOsyDETANTOsPRINCIPEsue
 40 T: no Z DH xel sin sax xeb gso RH sin OS Z DH LO RH FH soo PHI CT B8 KH EQ X KH OS BO TH PHI no RS B8 ZH
    S: no Z DH xel sin sax xeb gso RH sim OS Z DH LO RH FH soo PHI CT B8 KH EQ Xr KH OS BO TH PHI no RS B8 ZH
    V: no=T Z=a DH=n xel=[xel] sin=ES sax=[sax] xeb=NO gso=L RH=e sim=EN OS=le Z=a DH=n LO=t RH=e FH=n soo=ESTO PHI=s CT=p B8=r KH=i EQ=ma Xr=r KH=i OS=le BO=i TH=o PHI=s no=T RS=u B8=r ZH=e
    D: Tan[xel]ES[sax]NOLeENleantenESTOsprimarileiosTure
 41 T: Z GS TH PHI YH Z OT RS RH B8 sud bne zre sud xed xoo PHI xeo sut OT RH sod sin sud yem
    V: Z=a GS=d TH=o PHI=s YH=y Z=a OT=c RS=u RH=e B8=r sud=DE bne=SE zre=QUE sud=DE xed=LA xoo=MI PHI=s xeo={ME} sut=[sut] OT=c RH=e sod=DIO sin=ES sud=DE yem=PAPA
    D: adosyacuerDESEQUEDELAMIs{ME}[sut]ceDIOESDEPAPA
 42 T: KH RS gso BO TH yaz pif MH KH FH sod PHI xeb sud PHI Z ZO CT O X bae OT Z PHI O YH sod PHI ne
    S: KH RS gso BO TH yaz pif MH KH FH sod PHI xeb sud PHI Z ZO CT O Xs bae OT Z PHI O YH sod PHI ne
    V: KH=i RS=u gso=L BO=i TH=o yaz=PERO pif=AL MH=f KH=i FH=n sod=DIO PHI=s xeb=NO sud=DE PHI=s Z=a ZO=m CT=p O=a Xs=s bae=SI OT=c Z=a PHI=s O=a YH=y sod=DIO PHI=s ne=[ne]
    D: iuLioPEROALfinDIOsNODEsampasSIcasayDIOs[ne]
 43 T: PHI sod Z xad PHI sud xed xif xns sin no RS X O bnz xad PHI sin PHI sud xed YH AH gso BO O
    S: PHI sod Z xad PHI sud xed xif xns sim no RS Xr O bnz xad PHI sim PHI sud xed YH AH gso BO O
    V: PHI=s sod=DIO Z=a xad=LO PHI=s sud=DE xed=LA xif=LIGA xns=MUY sim=EN no=T RS=u Xr=r O=a bnz=[bnz] xad=LO PHI=s sim=EN PHI=s sud=DE xed=LA YH=y AH=g gso=L BO=i O=a
    D: sDIOaLOsDELALIGAMUYENTura[bnz]LOsENsDELAygLia
 44 T: YH zre peb bos yob OT RH X no KH X BO ZO TH zre byo pnd bae xad PHI rie PHI CT RH X bne RS
    S: YH zre peb bos yob OT RH Xr no KH Xs BO ZO TH zre byo pnd bae xad PHI rie PHI CT RH Xr bne RS
    V: YH=y zre=QUE peb=ASSI bos=TENGO yob=POR OT=c RH=e Xr=r no=T KH=i Xs=s BO=i ZO=m TH=o zre=QUE byo=[byo] pnd=[pnd] bae=SI xad=LO PHI=s rie=CONFEDERADO PHI=s CT=p RH=e Xr=r bne=SE RS=u
    D: yQUEASSITENGOPORcerTisimoQUE[byo][pnd]SILOsCONFEDERADOsperSEu
 45 T: ZH X O ZO TH PHI sin xad zre sio Z bne FH no O GS TH rak xed sif X Z YH rak PHI no Z FH
    S: ZH Xr O ZO TH PHI sim xad zre sio Z bne FH no O GS TH rak xed sif Xr Z YH rak PHI no Z FH
    V: ZH=e Xr=r O=a ZO=m TH=o PHI=s sim=EN xad=LO zre=QUE sio=ESTA Z=a bne=SE FH=n no=T O=a GS=d TH=o rak=CON xed=LA sif=[sif] Xr=r Z=a YH=y rak=CON PHI=s no=T Z=a FH=n
    D: eramosENLOQUEESTAaSEnTadoCONLA[sif]rayCONsTan
 46 T: OT KH Z zre sep xad MH ZH X KH ZO TH PHI YH zre baf tok CT RH ZO KH no BO GS TH sio B8 RH RS
    S: OT KH Z zre sep xad MH ZH Xr KH ZO TH PHI YH zre baf tok CT RH ZO KH no BO GS TH sio B8 RH RS
    V: OT=c KH=i Z=a zre=QUE sep=[sep] xad=LO MH=f ZH=e Xr=r KH=i ZO=m TH=o PHI=s YH=y zre=QUE baf=SOLO tok=HA CT=p RH=e ZO=m KH=i no=T BO=i GS=d TH=o sio=ESTA B8=r RH=e RS=u
    D: ciaQUE[sep]LOferimosyQUESOLOHApemiTidoESTAreu
 47 T: sin ynb CT X TH RS O B8 bae gso RH PHI TH ZO TH PHI rak PHI no O FH no sin by RS KH GS TH B8 sin
    S: sim ynb CT Xr TH RS O B8 bae gso RH PHI TH ZO TH PHI rak PHI no O FH no sin by RS KH GS TH B8 sin
    V: sim=EN ynb=NI CT=p Xr=r TH=o RS=u O=a B8=r bae=SI gso=L RH=e PHI=s TH=o ZO=m TH=o PHI=s rak=CON PHI=s no=T O=a FH=n no=T sin=ES by=SER RS=u KH=i GS=d TH=o B8=r sin=ES
    D: ENNIprouarSILesomosCONsTanTESSERuidorES
 48 T: YH zre yin be zuf FH no TH X FH O B8 Z RS ZH ynb X YH sin suh GS TH X RH zre RS ZH B8 FH O
    S: YH zre yinpt be zuf FH no TH Xr FH O B8 Z RS ZH ynb Xs YH sin suh GS TH Xs RH zre RS ZH B8 FH O
    V: YH=y zre=QUE yinpt=PUES be=SUYCOS zuf=QUIERE FH=n no=T TH=o Xr=r FH=n O=a B8=r Z=a RS=u ZH=e ynb=NI Xs=s YH=y sin=ES suh=EMPERADOR GS=d TH=o Xs=s RH=e zre=QUE RS=u ZH=e B8=r FH=n O=a
    D: yQUEPUESSUYCOSQUIEREnTornaraueNIsyESEMPERADORdoseQUEuerna
 49 T: sin yez YH bupo xno sud xed sin CT X RH PHI O YH dem CT RH X bne RS ZH X TH bu sin
    S: sim yez YH bupo xno sud xed sin CT Xr RH PHI O YH dem CT RH Xr bne RS ZH Xr TH bu sim
    V: sim=EN yez=PERSONA YH=y bupo=[bupo] xno=ME sud=DE xed=LA sin=ES CT=p Xr=r RH=e PHI=s O=a YH=y dem=YO CT=p RH=e Xr=r bne=SE RS=u ZH=e Xr=r TH=o bu=[bu] sim=EN
    D: ENPERSONAy[bupo]MEDELAESpresayYOperSEuero[bu]EN
 50 T: xad sud tok TH noo pef YH sin zre X RH B8 pnk B8 O RH OT tok X suq sud teb zre bac PHI SUPNO
    S: xad sud tok TH noo pef YH sin zre Xs RH B8 pnk B8 O RH OT tok Xr suq sud teb zre bac PHI SUPNO
    V: xad=LO sud=DE tok=HA TH=o noo=[noo] pef=[pef] YH=y sin=ES zre=QUE Xs=s RH=e B8=r pnk=AYUDA B8=r O=a RH=e OT=c tok=HA Xr=r suq=FRANCESES sud=DE teb=ITALIA zre=QUE bac=SU PHI=s SUPNO=<SUPNO>
    D: LODEHAo[noo][pef]yESQUEserAYUDAraecHArFRANCESESDEITALIAQUESUs<SUPNO>
 51 T: yob bac ynz sud RS ZH tok X RH X xad xoo PHI ZO TH YH ZO TH PHI no X O X zre bac sin MH
    S: yob bac ynz sud RS ZH tok Xz RH Xs xad xoo PHI ZO TH YH ZO TH PHI no Xr O Xs zre bac sin MH
    V: yob=POR bac=SU ynz=PARTE sud=DE RS=u ZH=e tok=HA Xz=z RH=e Xs=s xad=LO xoo=MI PHI=s ZO=m TH=o YH=y ZO=m TH=o PHI=s no=T Xr=r O=a Xs=s zre=QUE bac=SU sin=ES MH=f
    D: PORSUPARTEDEueHAzesLOMIsmoymosTrasQUESUESf
 52 T: RS RH X OT TH YH ynh PHI PHI TH TH X TH CT KH Z PHI sud gso RH TH FH yob zre bin zoh
    S: RS RH Xr OT TH YH ynhu PHI PHI TH TH Xs TH CT KH Z PHI sud gso RH TH FH yob zre bin zoh
    V: RS=u RH=e Xr=r OT=c TH=o YH=y ynhu=[ynhu] PHI=s PHI=s TH=o TH=o Xs=s TH=o CT=p KH=i Z=a PHI=s sud=DE gso=L RH=e TH=o FH=n yob=POR zre=QUE bin=[bin] zoh=[zoh]
    D: uercoy[ynhu]ssoosopiasDELeonPORQUE[bin][zoh]
 53 T: AH xad X BO YH KH TH FH RH O YH bnz AH Z FH O X Z tok X KH sin GS TH xad peb bon sud xad
    S: AH xad Xr BO YH KH TH FH RH O YH bnz AH Z FH O Xr Z tok Xz KH sim GS TH xad peb bon sud xad
    V: AH=g xad=LO Xr=r BO=i YH=y KH=i TH=o FH=n RH=e O=a YH=y bnz=[bnz] AH=g Z=a FH=n O=a Xr=r Z=a tok=HA Xz=z KH=i sim=EN GS=d TH=o xad=LO peb=ASSI bon=TANTO sud=DE xad=LO
    D: gLOriyioneay[bnz]ganaraHAziENdoLOASSITANTODELO
 54 T: rok B8 KH TH boi X RH CT X ZH KH sin su bac MH xed zre X Z YH zre rak bae sud B8 RH piq
    S: rok B8 KH TH boi Xs RH CT Xr ZH KH sin su bac MH xed zre Xs Z YH zre rak bae sud B8 RH piq
    V: rok={S} B8=r KH=i TH=o boi={SO} Xs=s RH=e CT=p Xr=r ZH=e KH=i sin=ES su=DI bac=SU MH=f xed=LA zre=QUE Xs=s Z=a YH=y zre=QUE rak=CON bae=SI sud=DE B8=r RH=e piq=BIEN
    D: {S}rio{SO}sepreiESDISUfLAQUEsayQUECONSIDEreBIEN
 55 T: zre bae pif AH dif yin bne MH RS B8 Z CT RS RH sud tok RS RH B8 rak sin zuy sin sin no X O
    S: zre bae pif AH dif yinzt bne MH RS B8 Z CT RS RH sud tok RS RH B8 rak sin zuy sin sin no Xr O
    V: zre=QUE bae=SI pif=AL AH=g dif=UNA yinzt=PAZ bne=SE MH=f RS=u B8=r Z=a CT=p RS=u RH=e sud=DE tok=HA RS=u RH=e B8=r rak=CON sin=ES zuy=REY DE FRANCIA sin=ES sin=ES no=T Xr=r O=a
    D: QUESIALgUNAPAZSEfurapueDEHAuerCONESREY DE FRANCIAESESTra
 56 T: GS TH bao PHI xad PHI rie PHI sin sen yob zre xed sud bac PHI SUPNO PHI TH xad xeb bae X RS RH bae
    S: GS TH bao PHI xad PHI rie PHI sim sen yob zre xed sud bac PHI SUPNO PHI TH xad xeb bae Xr RS RH bae
    V: GS=d TH=o bao=TODO PHI=s xad=LO PHI=s rie=CONFEDERADO PHI=s sim=EN sen=ELLA yob=POR zre=QUE xed=LA sud=DE bac=SU PHI=s SUPNO=<SUPNO> PHI=s TH=o xad=LO xeb=NO bae=SI Xr=r RS=u RH=e bae=SI
    D: doTODOsLOsCONFEDERADOsENELLAPORQUELADESUs<SUPNO>soLONOSIrueSI
 57 T: xeb ynb GS O X pne pif zuy ynb CT TH sud X xeo KH TH B8 tok X RH B8 xad zre SS RS KH
    S: xeb ynb GS O Xs pne pif zuy ynb CT TH sud Xr xeo KH TH B8 tok Xz RH B8 xad zre SS RS KH
    V: xeb=NO ynb=NI GS=d O=a Xs=s pne=[pne] pif=AL zuy=REY DE FRANCIA ynb=NI CT=p TH=o sud=DE Xr=r xeo={ME} KH=i TH=o B8=r tok=HA Xz=z RH=e B8=r xad=LO zre=QUE SS=q RS=u KH=i
    D: NONIdas[pne]ALREY DE FRANCIANIpoDEr{ME}iorHAzerLOQUEqui
 58 T: bae RH B8 ZH sin teb YH sef zre xad tok dam sib O CT TH sud X O B8 bne see sy soe YH MH
    S: bae RH B8 ZH sim teb YH sef zre xad tok dam sib O CT TH sud Xr O B8 bne see sy soe YH MH
    V: bae=SI RH=e B8=r ZH=e sim=EN teb=ITALIA YH=y sef=[sef] zre=QUE xad=LO tok=HA dam=YA sib=[sib] O=a CT=p TH=o sud=DE Xr=r O=a B8=r bne=SE see=DEL sy=ESTADO soe=[soe] YH=y MH=f
    D: SIereENITALIAy[sef]QUELOHAYA[sib]apoDErarSEDELESTADO[soe]yf
 59 T: gso KH O YH CT TH FH RH B8 yez sud bac ZO O xeb sin sin bac ZO TH CT TH FH no KH MH BO O O
    V: gso=L KH=i O=a YH=y CT=p TH=o FH=n RH=e B8=r yez=PERSONA sud=DE bac=SU ZO=m O=a xeb=NO sin=ES sin=ES bac=SU ZO=m TH=o CT=p TH=o FH=n no=T KH=i MH=f BO=i O=a O=a
    D: LiayponerPERSONADESUmaNOESESSUmoponTifiaa
 60 T: GS TH yob by bel sud xad sin CT KH B8 BO no RS pif YH no sin CT TH B8 pif sud xed YH AH gso
    S: GS TH yob by bel sud xad sin CT KH B8 BO no RS pif YH no sim CT TH B8 pif sud xed YH AH gso
    V: GS=d TH=o yob=POR by=SER bel=SENOR sud=DE xad=LO sin=ES CT=p KH=i B8=r BO=i no=T RS=u pif=AL YH=y no=T sim=EN CT=p TH=o B8=r pif=AL sud=DE xed=LA YH=y AH=g gso=L
    D: doPORSERSENORDELOESpiriTuALyTENporALDELAygL
 61 T: KH O yob CT TH sud B8 xno KH TH X tok X RH X xad zre ZH RS KH bae RH X ZH sin beo xed
    S: KH O yob CT TH sud B8 xno KH TH Xr tok Xz RH Xs xad zre ZHqt RS KH bae RH Xr ZH sin beo xed
    V: KH=i O=a yob=POR CT=p TH=o sud=DE B8=r xno=ME KH=i TH=o Xr=r tok=HA Xz=z RH=e Xs=s xad=LO zre=QUE ZHqt=q RS=u KH=i bae=SI RH=e Xr=r ZH=e sin=ES beo=TODA xed=LA
    D: iaPORpoDErMEiorHAzesLOQUEquiSIereESTODALA
 62 T: QH CT KH O FH GS Z no zre sin xad zre tok xnp PHI O xeb PHI zre sud X RH O FH xad PHI suq YH xad
    S: QH CT KH O FH GS Z no zre sin xad zre tok xnp PHI O xeb PHI zre sud Xs RH O FH xad PHI suq YH xad
    V: QH=x CT=p KH=i O=a FH=n GS=d Z=a no=T zre=QUE sin=ES xad=LO zre=QUE tok=HA xnp=MUCHO PHI=s O=a xeb=NO PHI=s zre=QUE sud=DE Xs=s RH=e O=a FH=n xad=LO PHI=s suq=FRANCESES YH=y xad=LO
    D: xpiandaTQUEESLOQUEHAMUCHOsaNOsQUEDEseanLOsFRANCESESyLO
 63 T: zuf FH YH zre yob soo xno CT O X sin OT ZH zre sin xez xeo bac PHI SUPNO sud RS RH sin OT RS
    S: zuf FH YH zre yob soo xno CT O Xr sin OT ZH zre sin xez xeo bac PHI SUPNO sud RS RH sin OT RS
    V: zuf=QUIERE FH=n YH=y zre=QUE yob=POR soo=ESTO xno=ME CT=p O=a Xr=r sin=ES OT=c ZH=e zre=QUE sin=ES xez=NINGUNA xeo={ME} bac=SU PHI=s SUPNO=<SUPNO> sud=DE RS=u RH=e sin=ES OT=c RS=u
    D: QUIEREnyQUEPORESTOMEparESceQUEESNINGUNA{ME}SUs<SUPNO>DEueEScu
 64 T: OT tok B8 xez yin see zuy bae xeb O X sin no O FH GS TH xed bao PHI xad PHI rie EQ tir xno
    S: OT tok B8 xez yinzt see zuy bae xeb O Xs sim no O FH GS TH xed bao PHI xad PHI rie EQ tir xno
    V: OT=c tok=HA B8=r xez=NINGUNA yinzt=PAZ see=DEL zuy=REY DE FRANCIA bae=SI xeb=NO O=a Xs=s sim=EN no=T O=a FH=n GS=d TH=o xed=LA bao=TODO PHI=s xad=LO PHI=s rie=CONFEDERADO EQ=ma tir=IUNTA xno=ME
    D: cHArNINGUNAPAZDELREY DE FRANCIASINOasENTandoLATODOsLOsCONFEDERADOmaIUNTAME
 65 T: no RH yob zre sud sio xeo byo bne AH RS xo YH xns ril YH Z X sin no QH FH GS TH xed bac
    S: no RH yob zre sud sio xeo byo bne AH RS xo YH xns ril YH Z Xs sin no QH FH GS TH xed bac
    V: no=T RH=e yob=POR zre=QUE sud=DE sio=ESTA xeo={ME} byo=[byo] bne=SE AH=g RS=u xo=RA YH=y xns=MUY ril=[ril] YH=y Z=a Xs=s sin=ES no=T QH=x FH=n GS=d TH=o xed=LA bac=SU
    D: TePORQUEDEESTA{ME}[byo]SEguRAyMUY[ril]yasESTxndoLASU
 66 T: PHI SUPNO D TH xad xeb CT RS RH sud by xam CT RH gso KH AH X TH PHI O YH GS O xeb PHI Z ynb
    S: PHI SUPNO D TH xad xeb CT RS RH sud by xam CT RH gso KH AH Xr TH PHI O YH GS O xeb PHI Z ynb
    V: PHI=s SUPNO=<SUPNO> D=nt TH=o xad=LO xeb=NO CT=p RS=u RH=e sud=DE by=SER xam=MAS CT=p RH=e gso=L KH=i AH=g Xr=r TH=o PHI=s O=a YH=y GS=d O=a xeb=NO PHI=s Z=a ynb=NI
    D: s<SUPNO>ntoLONOpueDESERMASpeLigrosaydaNOsaNI
 67 T: xed GS KH AH FH BO GS Z X sud bac yez YH pif sy sud xed YH AH gso BO Z YH no TH ZO RH sin
    S: xed GS KH AH FH BO GS Z Xs sud bac yez YH pif sy sud xed YH AH gso BO Z YH no TH ZO RH sim
    V: xed=LA GS=d KH=i AH=g FH=n BO=i GS=d Z=a Xs=s sud=DE bac=SU yez=PERSONA YH=y pif=AL sy=ESTADO sud=DE xed=LA YH=y AH=g gso=L BO=i Z=a YH=y no=T TH=o ZO=m RH=e sim=EN
    D: LAdignidasDESUPERSONAyALESTADODELAygLiayTomeEN
 68 T: QH sin CT xad sud xed yin yis zre sin yem KH RS gso KH TH Z X sin no TH rak sin
    S: QH sim CT xad sud xed yinu yis zre sin yem KH RS gso KH TH Z Xr sin no TH rak sin
    V: QH=x sim=EN CT=p xad=LO sud=DE xed=LA yinu=[yinu] yis=[yis] zre=QUE sin=ES yem=PAPA KH=i RS=u gso=L KH=i TH=o Z=a Xr=r sin=ES no=T TH=o rak=CON sin=ES
    D: xENpLODELA[yinu][yis]QUEESPAPAiuLioarESToCONES
 69 T: zil gso RS YH PHI sud soq ZO RS RH X no TH yob xno sod see xod sud CT Z RS KH O zre xeb
    S: zil gso RS YH PHI sud soq ZO RS RH Xr no TH yob xno sod see xod sud CT Z RS KH O zre xeb
    V: zil=[zil] gso=L RS=u YH=y PHI=s sud=DE soq=FRANCIA ZO=m RS=u RH=e Xr=r no=T TH=o yob=POR xno=ME sod=DIO see=DEL xod=[xod] sud=DE CT=p Z=a RS=u KH=i O=a zre=QUE xeb=NO
    D: [zil]LuysDEFRANCIAmuerToPORMEDIODEL[xod]DEpauiaQUENO
 70 T: baf xeb xed AH RS O X GS TH yaz CT RS PHI TH rak sen sin xaq xnz pif yem YH O yed
    S: baf xeb xed AH RS O Xr GS TH yaz CT RS PHI TH rak sen sin xaq xnz pif yem YH O yed
    V: baf=SOLO xeb=NO xed=LA AH=g RS=u O=a Xr=r GS=d TH=o yaz=PERO CT=p RS=u PHI=s TH=o rak=CON sen=ELLA sin=ES xaq=[xaq] xnz=NECESIDAD pif=AL yem=PAPA YH=y O=a yed=OBLIGADO
    D: SOLONOLAguardoPEROpusoCONELLAES[xaq]NECESIDADALPAPAyaOBLIGADO
 71 T: YH AH gso KH O YH FH O OT KH TH sud SL Z xed OT BO PHI ZO Z YH beo PHI xed EQ xnz sin YH no X Z
    S: YH AH gso KH O YH FH O OT KH TH sud SL Z xed OT BO PHI ZO Z YH beo PHI xed EQ xnz sin YH no Xr Z
    V: YH=y AH=g gso=L KH=i O=a YH=y FH=n O=a OT=c KH=i TH=o sud=DE SL=ll Z=a xed=LA OT=c BO=i PHI=s ZO=m Z=a YH=y beo=TODA PHI=s xed=LA EQ=ma xnz=NECESIDAD sin=ES YH=y no=T Xr=r Z=a
    D: ygLiaynacioDEllaLAcismayTODAsLAmaNECESIDADESyTra
 72 T: N8 O KH TH PHI zre sep KH RS LAM TH xad zef xeb CT RS su son sin zuy tok X RH X bae xed
    S: N8 O KH TH PHI zre sep KH RS LAM TH xad zef xeb CT RS su son sin zuy tok Xz RH Xs bae xed
    V: N8=b O=a KH=i TH=o PHI=s zre=QUE sep=[sep] KH=i RS=u LAM=an TH=o xad=LO zef=[zef] xeb=NO CT=p RS=u su=DI son=[son] sin=ES zuy=REY DE FRANCIA tok=HA Xz=z RH=e Xs=s bae=SI xed=LA
    D: baiosQUE[sep]iuanoLO[zef]NOpuDI[son]ESREY DE FRANCIAHAzesSILA
 73 T: seg yin yis xeb bne O X sin no O X Z YH zre xoo X RH piq bac PHI SUPNO zre yob CT RH X
    S: seg yinzt yis xeb bne O Xs sim no O Xr Z YH zre xoo Xs RH piq bac PHI SUPNO zre yob CT RH Xr
    V: seg=DICHA yinzt=PAZ yis=[yis] xeb=NO bne=SE O=a Xs=s sim=EN no=T O=a Xr=r Z=a YH=y zre=QUE xoo=MI Xs=s RH=e piq=BIEN bac=SU PHI=s SUPNO=<SUPNO> zre=QUE yob=POR CT=p RH=e Xr=r
    D: DICHAPAZ[yis]NOSEasENTarayQUEMIseBIENSUs<SUPNO>QUEPORper
 74 T: bac Z bae TH FH sud bae PHI CT O X KH sin no sin YH yez PHI KH FH OT gso BO FH O GS Z PHI O
    S: bac Z bae TH FH sud bae PHI CT O Xr KH sim no sin YH yez PHI KH FH OT gso BO FH O GS Z PHI O
    V: bac=SU Z=a bae=SI TH=o FH=n sud=DE bae=SI PHI=s CT=p O=a Xr=r KH=i sim=EN no=T sin=ES YH=y yez=PERSONA PHI=s KH=i FH=n OT=c gso=L BO=i FH=n O=a GS=d Z=a PHI=s O=a
    D: SUaSIonDESIspariENTESyPERSONAsincLinadasa
 75 T: suq xeb tok AH O reh zre bae O no xo KH RH X O bac CT Z PHI Z zaf CT X TH OT RS
    S: suq xeb tok AH O reh zre bae O no xo KH RH Xs O bac CT Z PHI Z zaf CT Xr TH OT RS
    V: suq=FRANCESES xeb=NO tok=HA AH=g O=a reh=COSA zre=QUE bae=SI O=a no=T xo=RA KH=i RH=e Xs=s O=a bac=SU CT=p Z=a PHI=s Z=a zaf=[zaf] CT=p Xr=r TH=o OT=c RS=u
    D: FRANCESESNOHAgaCOSAQUESIaTRAiesaSUpasa[zaf]procu
 76 T: X RH sud RH OT tok X gso RH saf YH zre sod gso RH O OT RS RH X GS TH dem yob
    S: Xr RH sud RH OT tok Xr gso RH saf YH zre sod gso RH O OT RS RH Xr GS TH dem yob
    V: Xr=r RH=e sud=DE RH=e OT=c tok=HA Xr=r gso=L RH=e saf=[saf] YH=y zre=QUE sod=DIO gso=L RH=e O=a OT=c RS=u RH=e Xr=r GS=d TH=o dem=YO yob=POR
    D: reDEecHArLe[saf]yQUEDIOLeacuerdoYOPOR
 77 T: zre soo YH sud SL TH xns xin rak no sin no TH see sag xoo bay yaz zre yin sud PHI
    S: zre soo YH sud SL TH xns xin rak no sim no TH see sag xoo bay yaz zre yinpt sud PHI
    V: zre=QUE soo=ESTO YH=y sud=DE SL=ll TH=o xns=MUY xin=MAL rak=CON no=T sim=EN no=T TH=o see=DEL sag=DICHO xoo=MI bay=UISORREY yaz=PERO zre=QUE yinpt=PUES sud=DE PHI=s
    D: QUEESTOyDElloMUYMALCONTENToDELDICHOMIUISORREYPEROQUEPUESDEs
 78 T: xny bel peb xad tok X xoo no KH GS TH yob CT X TH RS O X bae boi ZO TH PHI
    S: xnyt bel peb xad tok Xs xoo no KH GS TH yob CT Xr TH RS O Xr bae boi ZO TH PHI
    V: xnyt=NUESTRO bel=SENOR peb=ASSI xad=LO tok=HA Xs=s xoo=MI no=T KH=i GS=d TH=o yob=POR CT=p Xr=r TH=o RS=u O=a Xr=r bae=SI boi={SO} ZO=m TH=o PHI=s
    D: NUESTROSENORASSILOHAsMITidoPORprouarSI{SO}mos
 79 T: rak PHI no O FH no sin sin by RS BO X gso RH sin xed seg PHI O FH no Z sin CT X sio
    S: rak PHI no O FH no sin sin by RS BO Xr gso RH sim xed seg PHI O FH no Z sin CT Xr sio
    V: rak=CON PHI=s no=T O=a FH=n no=T sin=ES sin=ES by=SER RS=u BO=i Xr=r gso=L RH=e sim=EN xed=LA seg=DICHA PHI=s O=a FH=n no=T Z=a sin=ES CT=p Xr=r sio=ESTA
    D: CONsTanTESESSERuirLeENLADICHAsanTaESprESTA
 80 T: zre bao PHI gso RH sud RS RH ZO TH PHI GS O X AH X O OT KH Z PHI yob san YH no xo
    S: zre bao PHI gso RH sud RS RH ZO TH PHI GS O Xr AH Xr O OT KH Z PHI yob san YH no xo
    V: zre=QUE bao=TODO PHI=s gso=L RH=e sud=DE RS=u RH=e ZO=m TH=o PHI=s GS=d O=a Xr=r AH=g Xr=r O=a OT=c KH=i Z=a PHI=s yob=POR san=ELLO YH=y no=T xo=RA
    D: QUETODOsLeDEuemosdargraciasPORELLOyTRA
 81 T: N8 O KH Z X sud CT X TH bne AH RS BO X pnd rok xaz X sin YH xam N8 BO RS O B8
    S: N8 O KH Z Xr sud CT Xr TH bne AH RS BO Xr pnd rok xaz Xr sin YH xam N8 BO RS O B8
    V: N8=b O=a KH=i Z=a Xr=r sud=DE CT=p Xr=r TH=o bne=SE AH=g RS=u BO=i Xr=r pnd=[pnd] rok={S} xaz=NINGUNO Xr=r sin=ES YH=y xam=MAS N8=b BO=i RS=u O=a B8=r
    D: baiarDEproSEguir[pnd]{S}NINGUNOrESyMASbiuar
 82 T: sey X OT O PHI YH rak xam RS ynb TH FH YH rak MH TH X xoo GS O GS xed seg xoy
    S: sey Xs OT O PHI YH rak xam RS ynb TH FH YH rak MH TH Xr xoo GS O GS xed seg xoy
    V: sey=FUE Xs=s OT=c O=a PHI=s YH=y rak=CON xam=MAS RS=u ynb=NI TH=o FH=n YH=y rak=CON MH=f TH=o Xr=r xoo=MI GS=d O=a GS=d xed=LA seg=DICHA xoy=NUESTRA
    D: FUEscasyCONMASuNIonyCONforMIdadLADICHANUESTRA
 83 T: PHI Z FH no BO X BO ZO xif ynb zre rak sin pnk sud sod PHI xny bel
    S: PHI Z FH no BO Xs BO ZO xif ynb zre rak sin pnk sud sod PHI xnyt bel
    V: PHI=s Z=a FH=n no=T BO=i Xs=s BO=i ZO=m xif=LIGA ynb=NI zre=QUE rak=CON sin=ES pnk=AYUDA sud=DE sod=DIO PHI=s xnyt=NUESTRO bel=SENOR
    D: sanTisimLIGANIQUECONESAYUDADEDIOsNUESTROSENOR
 84 T: PHI pif AH O ZO TH PHI rak xoy tok no sin OT KH TH FH YH zre dem sin CT RH X TH sin bao
    S: PHI pif AH O ZO TH PHI rak xoy tok no sim OT KH TH FH YH zre dem sin CT RH Xr TH sim bao
    V: PHI=s pif=AL AH=g O=a ZO=m TH=o PHI=s rak=CON xoy=NUESTRA tok=HA no=T sim=EN OT=c KH=i TH=o FH=n YH=y zre=QUE dem=YO sin=ES CT=p RH=e Xr=r TH=o sim=EN bao=TODO
    D: sALgamosCONNUESTRAHATENcionyQUEYOESperoENTODO
 85 T: sin RS KH FH O OT gso RH ZO sin OT KH O zre yin xed rae zre no sin RH ZO TH PHI sue xed
    S: sim RS KH FH O OT gso RH ZO sim OT KH O zre yinu xed rae zre no sim RH ZO TH PHI sue xed
    V: sim=EN RS=u KH=i FH=n O=a OT=c gso=L RH=e ZO=m sim=EN OT=c KH=i O=a zre=QUE yinu=[yinu] xed=LA rae=[rae] zre=QUE no=T sim=EN RH=e ZO=m TH=o PHI=s sue=[sue] xed=LA
    D: ENuinacLemENciaQUE[yinu]LA[rae]QUETENemos[sue]LA
 86 T: sud MH sin bac TH FH sud teb sin xns taq YH xed sud xny PHI OT TH ZO RS FH su sin PHI
    S: sud MH sim bac TH FH sud teb sim xns taq YH xed sud xny PHI OT TH ZO RS FH su sin PHI
    V: sud=DE MH=f sim=EN bac=SU TH=o FH=n sud=DE teb=ITALIA sim=EN xns=MUY taq=[taq] YH=y xed=LA sud=DE xny=E PHI=s OT=c TH=o ZO=m RS=u FH=n su=DI sin=ES PHI=s
    D: DEfENSUonDEITALIAENMUY[taq]yLADEEscomunDIESs
 87 T: tox KH RS PHI no BO X BO ZO OT pif MH tox sin xib GS O X Z rok sin PHI xns OT RS ZO
    S: tox KH RS PHI no BO Xs BO ZO OT pif MH tox sin xib GS O Xr Z rok sim PHI xns OT RS ZO
    V: tox=[tox] KH=i RS=u PHI=s no=T BO=i Xs=s BO=i ZO=m OT=c pif=AL MH=f tox=[tox] sin=ES xib=[xib] GS=d O=a Xr=r Z=a rok={S} sim=EN PHI=s xns=MUY OT=c RS=u ZO=m
    D: [tox]iusTisimcALf[tox]ES[xib]dara{S}ENsMUYcum
 88 T: CT gso KH GS O bnz YH zue dem xed bos pud yob xam xil yob zue xad PHI sag EQ xny
    V: CT=p gso=L KH=i GS=d O=a bnz=[bnz] YH=y zue=[zue] dem=YO xed=LA bos=TENGO pud=[pud] yob=POR xam=MAS xil=[xil] yob=POR zue=[zue] xad=LO PHI=s sag=DICHO EQ=ma xny=E
    D: pLida[bnz]y[zue]YOLATENGO[pud]PORMAS[xil]POR[zue]LOsDICHOmaE
 89 T: PHI OT TH ZO RS FH sin sin PHI tok FH zre GS O GS TH xns zre N8 X O GS TH PHI YH O xno GS
    S: PHI OT TH ZO RS FH sim sin PHI tok FH zre GS O GS TH xns zre N8 Xr O GS TH PHI YH O xno GS
    V: PHI=s OT=c TH=o ZO=m RS=u FH=n sim=EN sin=ES PHI=s tok=HA FH=n zre=QUE GS=d O=a GS=d TH=o xns=MUY zre=QUE N8=b Xr=r O=a GS=d TH=o PHI=s YH=y O=a xno=ME GS=d
    D: scomunENESsHAnQUEdadoMUYQUEbradosyaMEd
 90 T: X sin no O GS TH PHI sud xed seg por YH zre dem CT RH X bne RS RH X O FH GS TH xnk CT
    S: Xr sin no O GS TH PHI sud xed seg por YH zre dem CT RH Xr bne RS RH Xr O FH GS TH xnk CT
    V: Xr=r sin=ES no=T O=a GS=d TH=o PHI=s sud=DE xed=LA seg=DICHA por=[por] YH=y zre=QUE dem=YO CT=p RH=e Xr=r bne=SE RS=u RH=e Xr=r O=a FH=n GS=d TH=o xnk=COMO CT=p
    D: rESTadosDELADICHA[por]yQUEYOperSEuerandoCOMOp
 91 T: RH X bne RS RH X TH sin xed seg xif YH OT RS ZO CT gso BO sin GS TH xad zre yob xoo
    S: RH Xr bne RS RH Xr TH sim xed seg xif YH OT RS ZO CT gso BO sim GS TH xad zre yob xoo
    V: RH=e Xr=r bne=SE RS=u RH=e Xr=r TH=o sim=EN xed=LA seg=DICHA xif=LIGA YH=y OT=c RS=u ZO=m CT=p gso=L BO=i sim=EN GS=d TH=o xad=LO zre=QUE yob=POR xoo=MI
    D: erSEueroENLADICHALIGAycumpLiENdoLOQUEPORMI
 92 T: ynz PHI TH YH yed KH RH sin OT X BO no TH pif sag xoo bay YH poz X RH CT X RH KH RH
    S: ynz PHI TH YH yed KH RH sin OT Xr BO no TH pif sag xoo bay YH poz Xs RH CT Xr RH KH RH
    V: ynz=PARTE PHI=s TH=o YH=y yed=OBLIGADO KH=i RH=e sin=ES OT=c Xr=r BO=i no=T TH=o pif=AL sag=DICHO xoo=MI bay=UISORREY YH=y poz=CAPITAN GENERAL Xs=s RH=e CT=p Xr=r RH=e KH=i RH=e
    D: PARTEsoyOBLIGADOieEScriToALDICHOMIUISORREYyCAPITAN GENERALsepreie
 93 T: su sin GS TH gso RH AH X O RS RH ZO sin no RH sud xed seg bac FH RH AH gso BO AH RH
    S: su sim GS TH gso RH AH Xr O RS RH ZO sim no RH sud xed seg bac FH RH AH gso BO AH RH
    V: su=DI sim=EN GS=d TH=o gso=L RH=e AH=g Xr=r O=a RS=u RH=e ZO=m sim=EN no=T RH=e sud=DE xed=LA seg=DICHA bac=SU FH=n RH=e AH=g gso=L BO=i AH=g RH=e
    D: DIENdoLegrauemENTeDELADICHASUnegLige
 94 T: OT BO YH ZO FH GS O FH GS TH gso RH xns sin no X RH OT tok xno FH no RH zre sud pef
    S: OT BO YH ZO FH GS O FH GS TH gso RH xns sin no Xr RH OT tok xno FH no RH zre sud pefa
    V: OT=c BO=i YH=y ZO=m FH=n GS=d O=a FH=n GS=d TH=o gso=L RH=e xns=MUY sin=ES no=T Xr=r RH=e OT=c tok=HA xno=ME FH=n no=T RH=e zre=QUE sud=DE pefa={AQUI}
    D: ciymndandoLeMUYESTrecHAMEnTeQUEDE{AQUI}
 95 T: O sud xed FH no RH bne AH RS O X sud sud OT O KH RH X sin yae no pif YH RH TH
    S: O sud xed FH no RH bne AH RS O Xr sud sud OT O KH RH Xs sin yae no pif YH RH TH
    V: O=a sud=DE xed=LA FH=n no=T RH=e bne=SE AH=g RS=u O=a Xr=r sud=DE sud=DE OT=c O=a KH=i RH=e Xs=s sin=ES yae=OTRO no=T pif=AL YH=y RH=e TH=o
    D: aDELAnTeSEguarDEDEcaiesESOTROTALyeo
 96 T: YH zre pib gso RH KH RH sin N8 KH O GS TH O V O FH GS Z X zre bae xad PHI sag PHI be
    S: YH zre pib gso RH KH RH sim N8 KH O GS TH O V O FH GS Z Xs zre bae xad PHI sag PHI be
    V: YH=y zre=QUE pib=ASSIMISMO gso=L RH=e KH=i RH=e sim=EN N8=b KH=i O=a GS=d TH=o O=a V=<V> O=a FH=n GS=d Z=a Xs=s zre=QUE bae=SI xad=LO PHI=s sag=DICHO PHI=s be=SUYCOS
    D: yQUEASSIMISMOLeieENbiadoa<V>andasQUESILOsDICHOsSUYCOS
 97 T: KH RS LAM BO RH X sin dam N8 RS sin no TH TH N8 TH gso RS BO RH X sin xaf O sin
    S: KH RS LAM BO RH Xr sin dam N8 RS sim no TH TH N8 TH gso RS BO RH Xs sim xaf O sim
    V: KH=i RS=u LAM=an BO=i RH=e Xr=r sin=ES dam=YA N8=b RS=u sim=EN no=T TH=o TH=o N8=b TH=o gso=L RS=u BO=i RH=e Xs=s sim=EN xaf=I O=a sim=EN
    D: iuanierESYAbuENTooboLuiesENIaEN
 98 T: MH O RS TH X sud xoy PHI Z FH no BO X KH ZO xif xnk dem bos yob rak zre xad tok
    S: MH O RS TH Xr sud xoy PHI Z FH no BO Xs KH ZO xif xnk dem bos yob rak zre xad tok
    V: MH=f O=a RS=u TH=o Xr=r sud=DE xoy=NUESTRA PHI=s Z=a FH=n no=T BO=i Xs=s KH=i ZO=m xif=LIGA xnk=COMO dem=YO bos=TENGO yob=POR rak=CON zre=QUE xad=LO tok=HA
    D: fauorDENUESTRAsanTisimLIGACOMOYOTENGOPORCONQUELOHA
 99 T: X O FH zre sin no pif roy xaf bae FH GS BO xed OT KH TH FH pif AH dif bne tar rak
    S: Xr O FH zre sin no pif roy xaf bae FH GS BO xed OT KH TH FH pif AH dif bne tar rak
    V: Xr=r O=a FH=n zre=QUE sin=ES no=T pif=AL roy=[roy] xaf=I bae=SI FH=n GS=d BO=i xed=LA OT=c KH=i TH=o FH=n pif=AL AH=g dif=UNA bne=SE tar=[tar] rak=CON
    D: ranQUEESTAL[roy]ISIndiLAcionALgUNASE[tar]CON
100 T: san PHI xnk tok X RH X RS ynb GS O X no FH no RH YH rak N8 RS sin rak bne KH TH
    S: san PHI xnk tok Xz RH Xs RS ynb GS O Xr no FH no RH YH rak N8 RS sim rak bne KH TH
    V: san=ELLO PHI=s xnk=COMO tok=HA Xz=z RH=e Xs=s RS=u ynb=NI GS=d O=a Xr=r no=T FH=n no=T RH=e YH=y rak=CON N8=b RS=u sim=EN rak=CON bne=SE KH=i TH=o
    D: ELLOsCOMOHAzesuNIdarTnTeyCONbuENCONSEio
101 T: bao xad zre bne O xeb YH rak RS RH ynb sin sio RH xnk xed sof YH rak bne X RS O
    S: bao xad zre bne O xeb YH rak RS RH ynb sin sio RH xnk xed sof YH rak bne Xr RS O
    V: bao=TODO xad=LO zre=QUE bne=SE O=a xeb=NO YH=y rak=CON RS=u RH=e ynb=NI sin=ES sio=ESTA RH=e xnk=COMO xed=LA sof=DEFENSION YH=y rak=CON bne=SE Xr=r RS=u O=a
    D: TODOLOQUESEaNOyCONueNIESESTAeCOMOLADEFENSIONyCONSErua
102 T: OT KH TH FH sud teb YH xnk xed X RH bae PHI no sin OT KH O sud suq tok PHI no O RH
    S: OT KH TH FH sud teb YH xnk xed Xr RH bae PHI no sim OT KH O sud suq tok PHI no O RH
    V: OT=c KH=i TH=o FH=n sud=DE teb=ITALIA YH=y xnk=COMO xed=LA Xr=r RH=e bae=SI PHI=s no=T sim=EN OT=c KH=i O=a sud=DE suq=FRANCESES tok=HA PHI=s no=T O=a RH=e
    D: cionDEITALIAyCOMOLAreSIsTENciaDEFRANCESESHAsTae
103 T: OT tok X xad PHI sud teb rak sin pnk sud sod PHI xny bel YH zre pib KH RH sin
    S: OT tok Xr xad PHI sud teb rak sin pnk sud sod PHI xnyt bel YH zre pib KH RH sin
    V: OT=c tok=HA Xr=r xad=LO PHI=s sud=DE teb=ITALIA rak=CON sin=ES pnk=AYUDA sud=DE sod=DIO PHI=s xnyt=NUESTRO bel=SENOR YH=y zre=QUE pib=ASSIMISMO KH=i RH=e sin=ES
    D: cHArLOsDEITALIACONESAYUDADEDIOsNUESTROSENORyQUEASSIMISMOieES
104 T: OT X KH no TH pif suh X TH AH O FH GS TH gso RH zre RS sin AH O xaf sin xez
    S: OT Xr KH no TH pif suh Xr TH AH O FH GS TH gso RH zre RS sim AH O xaf sin xez
    V: OT=c Xr=r KH=i no=T TH=o pif=AL suh=EMPERADOR Xr=r TH=o AH=g O=a FH=n GS=d TH=o gso=L RH=e zre=QUE RS=u sim=EN AH=g O=a xaf=I sin=ES xez=NINGUNA
    D: criToALEMPERADORrogandoLeQUEuENgaIESNINGUNA
105 T: Z sin no sin sud X sin xed seg sin CT X RH PHI O xnk xad tok sin N8 BO O GS TH
    S: Z sin no sim sud Xs sim xed seg sin CT Xr RH PHI O xnk xad tok sin N8 BO O GS TH
    V: Z=a sin=ES no=T sim=EN sud=DE Xs=s sim=EN xed=LA seg=DICHA sin=ES CT=p Xr=r RH=e PHI=s O=a xnk=COMO xad=LO tok=HA sin=ES N8=b BO=i O=a GS=d TH=o
    D: aESTENDEsENLADICHAESpresaCOMOLOHAESbiado
106 T: Z TH MH X sin OT RH X pif yem yob sin sud zre dem gso sin X RS RH AH TH
    S: Z TH MH Xr sin OT RH Xr pif yem yob sin sud zre dem gso sin Xr RS RH AH TH
    V: Z=a TH=o MH=f Xr=r sin=ES OT=c RH=e Xr=r pif=AL yem=PAPA yob=POR sin=ES sud=DE zre=QUE dem=YO gso=L sin=ES Xr=r RS=u RH=e AH=g TH=o
    D: aofrEScerALPAPAPORESDEQUEYOLESruego
107 T: xns O MH RH OT no RS TH PHI O xno FH no RH zre xeb sud PHI ZO Z YH sin xnk
    V: xns=MUY O=a MH=f RH=e OT=c no=T RS=u TH=o PHI=s O=a xno=ME FH=n no=T RH=e zre=QUE xeb=NO sud=DE PHI=s ZO=m Z=a YH=y sin=ES xnk=COMO
    D: MUYafecTuosaMEnTeQUENODEsmayESCOMO
108 T: bos yob rel zre xeb xad tok X sin YH zre rak no KH FH RS O FH GS TH bac bae
    S: bos yob rel zre xeb xad tok Xr sin YH zre rak no KH FH RS O FH GS TH bac bae
    V: bos=TENGO yob=POR rel=[rel] zre=QUE xeb=NO xad=LO tok=HA Xr=r sin=ES YH=y zre=QUE rak=CON no=T KH=i FH=n RS=u O=a FH=n GS=d TH=o bac=SU bae=SI
    D: TENGOPOR[rel]QUENOLOHArESyQUECONTinuandoSUSI
109 T: DH AH RS xad X dol YH sin MH RS RH X OT TH CT RS RH sin yob
    S: DH AH RS xad Xs dol YH sin MH RS RH Xr OT TH CT RS RH sim yob
    V: DH=n AH=g RS=u xad=LO Xs=s dol=[dol] YH=y sin=ES MH=f RS=u RH=e Xr=r OT=c TH=o CT=p RS=u RH=e sim=EN yob=POR
    D: nguLOs[dol]yESfuercopueENPOR
110 T: ynz sin xed seg xoy PHI O FH no KH X BO ZO O xif YH tok AH O FH YH CT X TH OT RS X
    S: ynz sim xed seg xoy PHI O FH no KH Xs BO ZO O xif YH tok AH O FH YH CT Xr TH OT RS Xr
    V: ynz=PARTE sim=EN xed=LA seg=DICHA xoy=NUESTRA PHI=s O=a FH=n no=T KH=i Xs=s BO=i ZO=m O=a xif=LIGA YH=y tok=HA AH=g O=a FH=n YH=y CT=p Xr=r TH=o OT=c RS=u Xr=r
    D: PARTEENLADICHANUESTRAsanTisimaLIGAyHAganyprocur
111 T: sin rak bac ZO O su gso BO AH sin OT BO O sin MH O RS TH X saf bao xad zre
    S: sin rak bac ZO O su gso BO AH sim OT BO O sin MH O RS TH Xr saf bao xad zre
    V: sin=ES rak=CON bac=SU ZO=m O=a su=DI gso=L BO=i AH=g sim=EN OT=c BO=i O=a sin=ES MH=f O=a RS=u TH=o Xr=r saf=[saf] bao=TODO xad=LO zre=QUE
    D: ESCONSUmaDILigENciaESfauor[saf]TODOLOQUE
112 T: bne O yeb YH rak RS RH ynb sin sio RH xnk xed sof YH rak bne X RS O OT KH TH FH
    S: bne O yeb YH rak RS RH ynb sin sio RH xnk xed sof YH rak bne Xr RS O OT KH TH FH
    V: bne=SE O=a yeb=[yeb] YH=y rak=CON RS=u RH=e ynb=NI sin=ES sio=ESTA RH=e xnk=COMO xed=LA sof=DEFENSION YH=y rak=CON bne=SE Xr=r RS=u O=a OT=c KH=i TH=o FH=n
    D: SEa[yeb]yCONueNIESESTAeCOMOLADEFENSIONyCONSEruacion
113 T: sud teb YH xnk xed X RH bae PHI no sin OT KH O sud xad PHI sag suq xny PHI OT TH
    S: sud teb YH xnk xed Xr RH bae PHI no sim OT KH O sud xad PHI sag suq xny PHI OT TH
    V: sud=DE teb=ITALIA YH=y xnk=COMO xed=LA Xr=r RH=e bae=SI PHI=s no=T sim=EN OT=c KH=i O=a sud=DE xad=LO PHI=s sag=DICHO suq=FRANCESES xny=E PHI=s OT=c TH=o
    D: DEITALIAyCOMOLAreSIsTENciaDELOsDICHOFRANCESESEsco
114 T: ZO FH sin sin PHI rak zre xed MH pif no O FH GS TH xad PHI yae PHI rie PHI dem FH
    V: ZO=m FH=n sin=ES sin=ES PHI=s rak=CON zre=QUE xed=LA MH=f pif=AL no=T O=a FH=n GS=d TH=o xad=LO PHI=s yae=OTRO PHI=s rie=CONFEDERADO PHI=s dem=YO FH=n
    D: mnESESsCONQUELAfALTandoLOsOTROsCONFEDERADOsYOn
115 T: CT TH O TH zos MH pif no O X ynb MH pif no X RH KH O ZO Z PHI O xed sof sud reb
    S: CT TH O TH zos MH pif no O Xr ynb MH pif no Xr RH KH O ZO Z PHI O xed sof sud reb
    V: CT=p TH=o O=a TH=o zos=[zos] MH=f pif=AL no=T O=a Xr=r ynb=NI MH=f pif=AL no=T Xr=r RH=e KH=i O=a ZO=m Z=a PHI=s O=a xed=LA sof=DEFENSION sud=DE reb=[reb]
    D: poao[zos]fALTarNIfALTreiamasaLADEFENSIONDE[reb]
116 T: YH O xed CT X TH bne OT RS OT KH TH FH sud xed seg sin CT X RH PHI Z YH O sio CT X TH
    S: YH O xed CT Xr TH bne OT RS OT KH TH FH sud xed seg sin CT Xr RH PHI Z YH O sio CT Xr TH
    V: YH=y O=a xed=LA CT=p Xr=r TH=o bne=SE OT=c RS=u OT=c KH=i TH=o FH=n sud=DE xed=LA seg=DICHA sin=ES CT=p Xr=r RH=e PHI=s Z=a YH=y O=a sio=ESTA CT=p Xr=r TH=o
    D: yaLAproSEcucionDELADICHAESpresayaESTApro
117 T: CT TH bae no TH gso sin sin N8 BO O GS O sud X BO X YH TH MH X sin OT RH X bao xad
    S: CT TH bae no TH gso sin sim N8 BO O GS O sud Xs BO Xs YH TH MH Xr sin OT RH Xr bao xad
    V: CT=p TH=o bae=SI no=T TH=o gso=L sin=ES sim=EN N8=b BO=i O=a GS=d O=a sud=DE Xs=s BO=i Xs=s YH=y TH=o MH=f Xr=r sin=ES OT=c RH=e Xr=r bao=TODO xad=LO
    D: poSIToLESENbiadaDEsisyofrEScerTODOLO
118 T: zre xam dor RH X KH sud PHI zre rak RS sin AH O xnk sin MH TH X OT O X xad EQ
    S: zre xam dor RH Xs KH sud PHI zre rak RS sim AH O xnk sin MH TH Xr OT O Xr xad EQ
    V: zre=QUE xam=MAS dor=[dor] RH=e Xs=s KH=i sud=DE PHI=s zre=QUE rak=CON RS=u sim=EN AH=g O=a xnk=COMO sin=ES MH=f TH=o Xr=r OT=c O=a Xr=r xad=LO EQ=ma
    D: QUEMAS[dor]esiDEsQUECONuENgaCOMOESforcarLOma
119 T: FH O ynb yex xad PHI YH xnk zue bae xeb KH RS LAM BO RH X sin dam N8 RS sin no TH
    S: FH O ynb yex xad PHI YH xnk zue bae xeb KH RS LAM BO RH Xr sin dam N8 RS sim no TH
    V: FH=n O=a ynb=NI yex=[yex] xad=LO PHI=s YH=y xnk=COMO zue=[zue] bae=SI xeb=NO KH=i RS=u LAM=an BO=i RH=e Xr=r sin=ES dam=YA N8=b RS=u sim=EN no=T TH=o
    D: naNI[yex]LOsyCOMO[zue]SINOiuanierESYAbuENTo
120 T: O xed seg sin CT X RH PHI Z N8 RS sin RS O FH xaf OT sen bae FH sin xeo OT KH TH DH
    S: O xed seg sin CT Xr RH PHI Z N8 RS sim RS O FH xaf OT sen bae FH sin xeo OT KH TH DH
    V: O=a xed=LA seg=DICHA sin=ES CT=p Xr=r RH=e PHI=s Z=a N8=b RS=u sim=EN RS=u O=a FH=n xaf=I OT=c sen=ELLA bae=SI FH=n sin=ES xeo={ME} OT=c KH=i TH=o DH=n
    D: aLADICHAESpresabuENuanIcELLASInES{ME}cion
121 T: pif AH dif YH tok X RH X xno RH YH PHI bok xaf rak GS RS CT gso KH OT Z GS O PHI
    S: pif AH dif YH tok Xs RH Xr xno RH YH PHI bok xaf rak GS RS CT gso KH OT Z GS O PHI
    V: pif=AL AH=g dif=UNA YH=y tok=HA Xs=s RH=e Xr=r xno=ME RH=e YH=y PHI=s bok=[bok] xaf=I rak=CON GS=d RS=u CT=p gso=L KH=i OT=c Z=a GS=d O=a PHI=s
    D: ALgUNAyHAserMEeys[bok]ICONdupLicadas
122 T: YH no X KH CT gso KH OT Z GS Z PHI doc Z PHI pob xnl YH yob beq xad zre sin bao
    S: YH no Xr KH CT gso KH OT Z GS Z PHI doc Z PHI pob xnl YH yob beq xad zre sin bao
    V: YH=y no=T Xr=r KH=i CT=p gso=L KH=i OT=c Z=a GS=d Z=a PHI=s doc=UI Z=a PHI=s pob={POR} xnl=MAR YH=y yob=POR beq=TIERRA xad=LO zre=QUE sin=ES bao=TODO
    D: yTripLicadasUIas{POR}MARyPORTIERRALOQUEESTODO
123 T: xad bac PHI TH sag bne KH BO X KH RH X ZH YH xad zre xam pae bne TH MH X sin
    S: xad bac PHI TH sag bne KH BO Xr KH RH Xs ZH YH xad zre xam pae bne TH MH Xr sin
    V: xad=LO bac=SU PHI=s TH=o sag=DICHO bne=SE KH=i BO=i Xr=r KH=i RH=e Xs=s ZH=e YH=y xad=LO zre=QUE xam=MAS pae=[pae] bne=SE TH=o MH=f Xr=r sin=ES
    D: LOSUsoDICHOSEiirieseyLOQUEMAS[pae]SEofrES
124 T: OT KH RH X FH
    S: OT KH RH Xr FH
    V: OT=c KH=i RH=e Xr=r FH=n
    D: ciern
```
