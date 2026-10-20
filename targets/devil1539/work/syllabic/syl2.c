// syllabic solver: sign -> cons[family[sign]] + vow[sign]; cons may be empty (vowel carrier), vow may be empty
#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <math.h>
#define NL 21
static const char *A="abcdefghilmnopqrstuxz";
float *lp; double uni[NL], luni[NL];
int ct[4096], N=0, S=0, F=0, fam[256], mk[256], K=0; char mnames[64][16]; char names[256][16], fnames[256][16];
static unsigned long long rs=88172645463325252ULL;
static inline unsigned long long xr(){ rs^=rs<<13; rs^=rs>>7; rs^=rs<<17; return rs; }
static inline double ur(){ return (xr()>>11)*(1.0/9007199254740992.0); }
int VOW[6]={0,4,8,12,18,-1}; // a e i o u none
int CONS[18]; int NC=0;
double lam;
int out[8192]; int M;
double score(int *cons,int *vow,double*lmo){
  M=0; for(int i=0;i<N;i++){ int c=cons[fam[ct[i]]], v=vow[mk[ct[i]]]; if(c>=0) out[M++]=c; if(v>=0) out[M++]=v; if(c<0&&v<0) out[M++]=0; }
  double s=0; int cnt[NL]={0}; for(int i=0;i<M;i++) cnt[out[i]]++;
  for(int i=0;i<4&&i<M;i++) s+=luni[out[i]];
  for(int i=4;i<M;i++) s+=lp[(((out[i-4]*NL+out[i-3])*NL+out[i-2])*NL+out[i-1])*NL+out[i]];
  if(lmo) *lmo=s/M;
  double chi=0; for(int l=0;l<NL;l++){ double e=uni[l]*M; chi+=(cnt[l]-e)*(cnt[l]-e)/(e+0.5); }
  return (s-lam*chi)/M*N;   // normalise to per-sign scale so length changes are not rewarded
}
int main(int argc,char**argv){
  // syl table ctfile famfile restarts iters lam seed shuffle
  FILE*f=fopen(argv[1],"rb"); lp=malloc(sizeof(float)*NL*NL*NL*NL*NL); if(fread(lp,sizeof(float),NL*NL*NL*NL*NL,f)){} fclose(f);
  char un[512]; sprintf(un,"%s.uni",argv[1]); f=fopen(un,"r"); for(int l=0;l<NL;l++){ if(fscanf(f,"%lf",&uni[l])){} luni[l]=log(uni[l]); } fclose(f);
  for(int l=0;l<NL;l++) if(!strchr("aeiou",A[l])) CONS[NC++]=l;
  // family file: lines "sign family"
  char fs[256][16], ff[256][16], fm[256][16]; int nf=0; f=fopen(argv[3],"r"); while(fscanf(f,"%15s %15s %15s",fs[nf],ff[nf],fm[nf])==3) nf++; fclose(f);
  int restarts=atoi(argv[4]); long iters=atol(argv[5]); lam=atof(argv[6]); rs^=atoll(argv[7])*2654435761ULL+1; int shuf=atoi(argv[8]);
  f=fopen(argv[2],"r"); char tok[64];
  while(fscanf(f,"%63s",tok)==1){ int k=-1; for(int s=0;s<S;s++) if(!strcmp(names[s],tok)){k=s;break;}
    if(k<0){ strcpy(names[S],tok); k=S++; const char*fn=tok; for(int j=0;j<nf;j++) if(!strcmp(fs[j],tok)) fn=ff[j];
      int fk=-1; for(int q=0;q<F;q++) if(!strcmp(fnames[q],fn)){fk=q;break;} if(fk<0){strcpy(fnames[F],fn); fk=F++;} fam[k]=fk; const char*mn="none"; for(int j=0;j<nf;j++) if(!strcmp(fs[j],tok)) mn=fm[j]; int mq=-1; for(int q=0;q<K;q++) if(!strcmp(mnames[q],mn)){mq=q;break;} if(mq<0){strcpy(mnames[K],mn); mq=K++;} mk[k]=mq; }
    ct[N++]=k; }
  fclose(f);
  if(shuf){ unsigned long long sv=rs; rs=shuf*7919ULL+13; for(int i=N-1;i>0;i--){ int j=xr()%(i+1); int t=ct[i];ct[i]=ct[j];ct[j]=t;} rs=sv; }
  int cons[256],vow[256],bc[256],bv[256],gc[256],gv[256]; double gbs=-1e18;
  for(int r=0;r<restarts;r++){
    for(int q=0;q<F;q++) cons[q]= ur()<0.15? -1 : CONS[xr()%NC];
    for(int s=0;s<K;s++) vow[s]=VOW[xr()%6];
    double cur=score(cons,vow,NULL), bs=cur; memcpy(bc,cons,sizeof cons); memcpy(bv,vow,sizeof vow);
    for(long it=0;it<iters;it++){
      double T=8*pow(0.2/8,(double)it/iters);
      int which=xr()%2, idx, old;
      if(which==0){ idx=xr()%F; old=cons[idx]; cons[idx]= ur()<0.1? -1 : CONS[xr()%NC]; }
      else { idx=xr()%K; old=vow[idx]; vow[idx]=VOW[xr()%6]; }
      double sc=score(cons,vow,NULL);
      if(sc>=cur || ur()<exp((sc-cur)/T)){ cur=sc; if(cur>bs){bs=cur; memcpy(bc,cons,sizeof cons); memcpy(bv,vow,sizeof vow);} }
      else { if(which==0) cons[idx]=old; else vow[idx]=old; }
    }
    if(bs>gbs){ gbs=bs; memcpy(gc,bc,sizeof bc); memcpy(gv,bv,sizeof bv); }
  }
  double lm; score(gc,gv,&lm);
  printf("%s %.4f lm %.4f F=%d K=%d S=%d ", shuf?"SHUF":"REAL", gbs/N, lm, F, K, S);
  for(int i=0;i<M;i++) putchar(A[out[i]]); putchar('\n');
  return 0;
}
