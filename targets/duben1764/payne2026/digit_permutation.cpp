#include <algorithm>
#include <array>
#include <fstream>
#include <iostream>
#include <sstream>
#include <string>
#include <vector>
using namespace std;
int main(int argc,char**argv){
 array<int,1000> mask{};ifstream keys(argv[1]);string line;
 while(getline(keys,line)){if(line.empty()||line[0]=='#')continue;istringstream s(line);int c;s>>c;if(c>=0&&c<1000)mask[c]=1;}
 ifstream ct(argv[2]);vector<array<int,4>> xs;
 while(getline(ct,line)){istringstream s(line);int c,n;if(s>>c>>n)xs.push_back({c/100,c/10%10,c%10,n});}
 int o0=argc>3?argv[3][0]-'0':0,o1=argc>3?argv[3][1]-'0':1,o2=argc>3?argv[3][2]-'0':2;
 array<int,10> p{0,1,2,3,4,5,6,7,8,9};vector<pair<int,array<int,10>>> best;
 do{int sc=0;for(auto x:xs)sc+=mask[100*p[x[o0]]+10*p[x[o1]]+p[x[o2]]]*x[3];
  if(best.size()<30||sc>best.back().first){best.push_back({sc,p});sort(best.begin(),best.end(),greater<>());if(best.size()>30)best.pop_back();}
 }while(next_permutation(p.begin(),p.end()));
 for(auto b:best){cout<<b.first<<" ";for(int x:b.second)cout<<x;cout<<"\n";}
}
