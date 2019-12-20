#!/bin/bash
IFS=$'\n'
file=vblinks.txt
regex=".*href=\"(.*)/.*\">(.*)</a>"

echo "----------------------------"
echo "Hier zijn de gevonden links:"

for lijn in `cat $file`; do
  if [[ $lijn =~ $regex ]]; then
    echo ${BASH_REMATCH[2]/amp;/} = ${BASH_REMATCH[1]}
  fi
done
echo "----------------------------"
