#!/bin/bash
# acc.sh lang table restarts iters lam
for k in 0 1 2 3 4 5; do
  out=$(./hs $2 ctl_$1$k.txt $3 $4 $5 $k 0 | head -1); pt=$(cat ctl_$1$k.pt)
  dec=$(echo "$out" | awk '{print $5}'); sc=$(echo "$out" | awk '{print $2, $4}')
  acc=$(python3 -c "a='$dec';b='$pt';print(round(sum(x==y for x,y in zip(a,b))/len(b),2))")
  echo "$1$k $sc acc=$acc"
done
