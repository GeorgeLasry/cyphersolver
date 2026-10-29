import requests, re, time, os, json
ids="""letterspaperspt104greauoft letterspaperspt202greauoft letterspaperspt103greauoft letterspaperspt204greauoft letterspaperspt214greauoft letterspapersfor11lond letterspapersfor12lond lettterspapersfo0004jsbr_w1f6 lettersandpaper12offigoog letterspapersfor0007jame letterspapersfor10greauoft letterspapersfor01greauoft letterspapersfor0005jame Vol2Pt1LettersAndPapersForeignAndDomestic Vol3Pt1LettersAndPapersForeignAndDomestic Vol3Pt2LettersAndPapersForeignAndDomestic 10278829bsb 11001939bsb 10278837bsb 10278871bsb calendarofstatep08grea calendarofstatep00grea_0 calendarofstatep09grea_0 calendarofstatep0000mary_o4k2 calendarofstatep0000vari_q2n4 calendarofstatep0000mary_h2k1 calendarstatepa03britgoog calendarofstatep0000mary_l0t0 1905calendarofstatep10greauoft 1903calendarofstatep09greauoft calendarstatepa01britgoog calendarstatepa23offigoog calendarofstatep03greauoft calendarofstatep05grea calendarstatepa00igoog calendarstatepa00turngoog calendarstatepa01offigoog calendarofstatep10grea calendarofstatep12grea cu31924091770473 cu31924091770465 cu31924091770440 cu31924091770457 cu31924091770424 cu31924091754659 cu31924091775274 bub_gb_ELGK9pFXS50C calendarofclaren01bodluoft calendarofclaren04bodluoft calendarofclaren05bodl calendarofcarewm04lamb statepapersmary07greauoft calendarofstuart01grea calendarofstuart0003grea calendarofstuart07grea EighthReportHistoricalMSS reportonpepysman00grea reportonpepys00greauoft manuscriptsjmhe00heatgoog manuscriptsjmhe01heatgoog ReportOnTheManuscriptsOfTheMarquessOfDownshireV1Pt1 reportonmanuscri01greauoft reportonmanuscri02greauoft catholicrecordso0v58unse publicationsofsc37scot CatalogueOfAdditionsToTheMSS188287 cornwallispapers0000rees secretnegociatio00gardrich""".split()
for i in ids:
    p=f'_txt/{i}.txt'
    if os.path.exists(p): continue
    try:
        r=requests.get(f'https://archive.org/download/{i}/{i}_djvu.txt',timeout=180)
        if r.status_code!=200:
            print('FAIL',i,r.status_code);continue
        open(p,'wb').write(r.content)
        print(i,len(r.content),flush=True)
    except Exception as e: print('ERR',i,e)
    time.sleep(1)
