"""Independent check of issue #181 (Agarwal): decrypt Childs p.89, p.107, p.187 with the keys he names."""
import sys
sys.stdout.reconfigure(encoding='utf-8')
L='ADFGVX'
def untrans(ct,key,mode):
    k=len(key);n=len(ct)
    if mode=='rank':   # key[i] = rank (1-based) of column i; read columns in rank order
        order=sorted(range(k),key=lambda i:key[i])
    else:              # key lists the columns in the order they were read
        order=[x-1 for x in key]
    full,extra=divmod(n,k)
    lens=[full+(1 if c<extra else 0) for c in range(k)]
    cols={};pos=0
    for c in order:
        cols[c]=ct[pos:pos+lens[c]];pos+=lens[c]
    return ''.join(cols[c][r] for r in range(full+1) for c in range(k) if r<lens[c])
def sub(s,sq):
    out=''
    for i in range(0,len(s)-1,2):
        a,b=s[i],s[i+1]
        if a in L and b in L: out+=sq[L.index(a)*6+L.index(b)]
        else: out+='?'
    return out
def run(name,ct,key,sq):
    ct=ct.replace(' ','').replace('-','?')
    for mode in('rank','order'):
        for inv in(0,1):
            kk=key
            if inv:  # inverse permutation
                kk=[0]*len(key)
                for i,v in enumerate(key): kk[v-1]=i+1
            t=untrans(ct,kk,mode)
            print(name,mode,'inv' if inv else '   ',sub(t,sq))
sq1='UILOF9RCZVSX02G7QTD8WNB5JMHEKPY41A36'
k1=[3,16,4,15,7,12,18,6,17,8,19,1,13,10,2,14,11,9,5]
run('p110D',"XXGVF XFFFD AGGVG AGXAA XGXGX XAGVG FFXXF GVGGX XGA-- XAXXG GFGFX FAAFX XXFAV XGXFF DGGAG AXAXX XXDXX FXGGX XVFAD DFDFV GXFFV AFAGV DDFVG VFDXX FXAXF XGGFF DAFFD DDVXG AXFFV FVGAA FVGGG VGXDX VAXAF FXVGA FFAVF X",k1,sq1)
sq2='JZLH?R??S?T?MKDWU?V?B?P??FAO?GIX?CNE'
k2=[13,8,6,16,7,18,1,14,9,20,10,15,17,2,3,11,5,19,4,12]
run('p190G',"DGGXX XAFGX AAADV AAXVX VXXXX VVXGD FFXDX FADFD XVFFX VFXFV FVVXX XVXXX XXGXX XXGGX AFVGA ADXFG AFXVX AVFFV XVXDF ADDXA AVDFX FFDXX -FXXV DGVAX DDXVF DGXXD XXDX",k2,sq2)
run('p0924',"FGXDV VGGDV GGFGF VDAGD XAGVX VFGXG XGAFV DVVXD DVVVF GAGXA ADAGD FGGDG VXXGG XAXAV DGDFV AGGFG DFDFD GAFXG VGAFV GVDVD GDVGG FVXGD FVXVX AFVGV DVGVA VDXDX DVXDF DAGDA GVGFX VFFXA XDGAV AFFDD VDFAG AFVVA ADGFG V--GG GXFVG XXVXD AVGDG DFXGV ADVVG DGGGX GDVAV GGDVG DXAFG XAGDG VFAVV AVGVX VGAFD XFGDD XDXAV VGDAG GDVVG XAFVV FVXGV VXDFG FDGDG GFVGV",k1,sq1)
