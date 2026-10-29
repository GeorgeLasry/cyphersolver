# R66: per-line reversal patterns (boustrophedon etc.), strict substitution and <=6 slips, en-modern, full power
for p in 010 101 100 001 110 011; do
  PYTHONUTF8=1 python bigsolve.py misread 230 0 --ct=ct_rev$p.txt --noctl 2>&1 | grep -v Warning
done
DORA_NNULL=8 PYTHONUTF8=1 python bigsolve.py misread 230 0 --nulls 2>&1 | grep -v Warning | tail -8
for p in 010 101; do
  DORA_SLIP=both PYTHONUTF8=1 python bigsolve.py misread 230 6 --ct=ct_rev$p.txt --noctl 2>&1 | grep -v Warning
done
echo done
