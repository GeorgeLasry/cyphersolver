#!/bin/sh
# fetch.sh <outdir> <first_id> <count>: download Arkivalieronline images by contiguous id
out=$1; first=$2; n=$3; mkdir -p "$out"
i=0; while [ $i -lt $n ]; do id=$((first+i)); f="$out/$(printf %03d $((i+1)))_$id.jpg"
  [ -s "$f" ] || curl -s -m 60 -o "$f" https://api.rigsarkivet.dk/ao/v1/images/$id; i=$((i+1)); done
