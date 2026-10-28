#!/usr/bin/env bash
# Rounds 42-47, run one after another at full power (115 long runs per target, own controls, shuffles).
cd "$(dirname "$0")"
export PYTHONUTF8=1
run(){ tag=$1; shift; echo "== $tag"; env "$@" python bigsolve.py "${ARGS[@]}" 2>&1 | grep -v Warning; env "$@" python bigsolve.py "${ARGS[@]}" --nulls 2>&1 | grep -v Warning; }
{
for m in la fr-modern de-modern; do ARGS=(homo 115); run "R42 homophones $m" DORA_MODEL=$m; done
ARGS=(misread 115 0); run "R43 phonetic 25 classes" DORA_TF=phon25 DORA_CMU="$DORA_CMU"
for c in ct_columns.txt ct_linesrev.txt ct_order132.txt ct_order213.txt; do ARGS=(misread 115 0 --ct=$c); run "R44 reading order $c" DORA_MODEL=en-modern; done
for m in nl-modern pt-modern da-modern sv-modern cy-modern hu-modern pl-modern; do ARGS=(misread 115 0); run "R45 $m" DORA_MODEL=$m; done
ARGS=(homo 115); run "R46 homophones en-elgar" DORA_MODEL=en-elgar
ARGS=(misread 115 0 --ct=ct_nosingletons.txt); run "R47 singletons as nulls" DORA_MODEL=en-modern
} > runs/r42_47.txt
