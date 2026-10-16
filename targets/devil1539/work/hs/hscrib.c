// homophonic substitution solver: 5-gram conditional log-probs + letter-frequency chi2 penalty
#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <math.h>
#define NL 21
static const char *A="abcdefghilmnopqrstuxz";
float *lp; double uni[NL], luni[NL];
int ct[4096], N=0, S=0; char names[256][16];
static unsigned long long rs=88172645463325252ULL;
static inline unsigned long long xr(){ rs^=rs<<13; rs^=rs>>7; rs^=rs<<17; return rs; }
static inline double ur(){ return (xr()>>11)*(1.0/9007199254740992.0); }
double lam;
double score(int *key, double *lmout){
  int p[4096]; double s=0; int cnt[NL]={0};
  for(int i=0;i<N;i++){ p[i]=key[ct[i]]; cnt[p[i]]++; }
  for(int i=0;i<4&&i<N;i++) s+=luni[p[i]];
  for(int i=4;i<N;i++){ int id=(((p[i-4]*NL+p[i-3])*NL+p[i-2])*NL+p[i-1])*NL+p[i]; s+=lp[id]; }
  if(lmout) *lmout=s/N;
  double chi=0; for(int l=0;l<NL;l++){ double e=uni[l]*N; chi+=(cnt[l]-e)*(cnt[l]-e)/(e+0.5); }
  return s-lam*chi;
}
int pickletter(){ double r=ur(),c=0; for(int l=0;l<NL;l++){ c+=uni[l]; if(r<c) return l;} return NL-1; }
int main(int argc,char**argv){
  if(argc<8){fprintf(stderr,"usage: hs table ctfile restarts iters lambda seed rtl [shuffle]\n");return 1;}
  FILE*f=fopen(argv[1],"rb"); lp=malloc(sizeof(float)*NL*NL*NL*NL*NL); fread(lp,sizeof(float),NL*NL*NL*NL*NL,f); fclose(f);
  char un[512]; sprintf(un,"%s.uni",argv[1]); f=fopen(un,"r"); for(int l=0;l<NL;l++){ fscanf(f,"%lf",&uni[l]); luni[l]=log(uni[l]); } fclose(f);
  int restarts=atoi(argv[3]); long iters=atol(argv[4]); lam=atof(argv[5]); rs^=atoll(argv[6])*2654435761ULL+1; int rtl=atoi(argv[7]);
  int shuf=argc>8?atoi(argv[8]):0;
  // read tokens line by line
  f=fopen(argv[2],"r"); char line[65536];
  while(fgets(line,sizeof line,f)){
    int lt[4096],ln=0; char*tok=strtok(line," \t\r\n");
    while(tok){ int k=-1; for(int s=0;s<S;s++) if(!strcmp(names[s],tok)){k=s;break;}
      if(k<0){ strcpy(names[S],tok); k=S++; } lt[ln++]=k; tok=strtok(NULL," \t\r\n"); }
    for(int i=0;i<ln;i++) ct[N++]= rtl? lt[ln-1-i] : lt[i];
  }
  fclose(f);
  if(shuf){ unsigned long long save=rs; rs=shuf*7919ULL+13; for(int i=N-1;i>0;i--){ int j=xr()%(i+1); int t=ct[i];ct[i]=ct[j];ct[j]=t;} rs=save; }
  int fixedk[256]; for(int s=0;s<S;s++) fixedk[s]=-1;
  if(argc>10){ const char*cr=argv[9]; int off=atoi(argv[10]); int L=strlen(cr);
    if(off+L>N){ printf("BAD\n"); return 0; }
    for(int i=0;i<L;i++){ int l=strchr(A,cr[i])-A; int sgn=ct[off+i];
      if(fixedk[sgn]>=0 && fixedk[sgn]!=l){ printf("INCONSISTENT\n"); return 0; } fixedk[sgn]=l; } }
  int key[256],best[256],gbest[256]; double gbs=-1e18;
  for(int r=0;r<restarts;r++){
    for(int s=0;s<S;s++) key[s]= fixedk[s]>=0? fixedk[s] : pickletter();
    double cur=score(key,NULL), bs=cur; memcpy(best,key,sizeof(int)*S);
    double T0=10, T1=0.2;
    for(long it=0;it<iters;it++){
      double T=T0*pow(T1/T0,(double)it/iters);
      int s=xr()%S; if(fixedk[s]>=0) continue; int old=key[s], s2=-1, old2=0;
      if(ur()<0.25){ s2=xr()%S; if(fixedk[s2]>=0){ s2=-1; continue;} old2=key[s2]; key[s]=old2; key[s2]=old; }
      else key[s]= ur()<0.5? pickletter() : (int)(xr()%NL);
      double sc=score(key,NULL);
      if(sc>=cur || ur()<exp((sc-cur)/T)){ cur=sc; if(cur>bs){bs=cur; memcpy(best,key,sizeof(int)*S);} }
      else { key[s]=old; if(s2>=0) key[s2]=old2; }
    }
    if(bs>gbs){ gbs=bs; memcpy(gbest,best,sizeof(int)*S); }
  }
  double lm; score(gbest,&lm);
  printf("%s %.4f lm %.4f ", shuf?"SHUF":"REAL", gbs/N, lm);
  for(int i=0;i<N;i++) putchar(A[gbest[ct[i]]]); putchar('\n');
  for(int s=0;s<S;s++) printf("%s=%c ",names[s],A[gbest[s]]); putchar('\n');
  return 0;
}
