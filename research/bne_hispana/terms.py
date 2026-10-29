from eu import run
terms=['cifrada','cifrado','cifradas','cifrados','"parcialmente cifrada"','"en cifra"','"con cifra"','descifrado','descifrada','descifrar','descifre','"cifra general"','"escrita en cifra"','criptografia','contracifra','nomenclator','xifrada','xifrat','"carta cifrada"','"documento cifrado"','"texto cifrado"','"escritura cifrada"','"letra cifrada"','"cifra" AND (carta OR minuta OR despacho OR oficio OR manuscrito)','cifra AND (embajador OR virrey OR secretario OR rey)','clave AND (carta OR cifra)','contraseña AND cifra','jeroglifico AND carta','abecedario AND cifra','secreta AND cifra']
for p,qf in [('bne','DATA_PROVIDER:"National Library of Spain"'),('es','COUNTRY:spain')]:
    for t in terms:
        run(t,qf,"raw/%s_%s.json"%(p,''.join(c for c in t if c.isalnum())[:40]))
