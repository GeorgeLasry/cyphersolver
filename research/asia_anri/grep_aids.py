"""Grep the extracted finding-aid texts for cipher terms; writes aid_hits.txt (file, context)."""
import glob, re, sys
rx=re.compile(r'(?i)(cijfer(?:s|schrift|telegram\w*|code\w*|sleutel\w*)?|cyfer\w*|gecijferd\w*|ontcijfer\w*|chiffr\w*|dechiffr\w*|cipher\w*|cypher\w*|geheimschrift|codetelegram\w*|code[- ]?telegram\w*|telegram\w* in code|code ?boek\w*|codesleutel\w*|codes\b|\bcode\b|\bkode\b|kode rahasia|\bsandi\b|persandian|kawat sandi|berita sandi|sleutel\w*|\bkunci\b|geheime? code|radiogramw*|gecodeerdw*|decodw*|onderschepw*|berita rahasia|dengan kode)')
out=open('aid_hits.txt','w',encoding='utf8')
for f in sorted(glob.glob('pdf/*.txt')):
    t=open(f,encoding='utf8',errors='replace').read()
    for m in rx.finditer(t):
        w=m.group(0).lower()
        ctx=re.sub(r'\s+',' ',t[max(0,m.start()-300):m.end()+250])
        if re.search(r'verdeelsleutel|totaalcijfer|cijfers over|kode klasifikasi|kode arsip|kode pos|zie voor deze cijfers|cijfers die',ctx,re.I): continue
        out.write(f"{f[4:70]}\t{w}\t{ctx}\n")
