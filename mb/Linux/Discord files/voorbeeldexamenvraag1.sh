#!/bin/bash

# Doel:         een tekstbestand met IP adressen klasseren per klasse
# Argumenten:   1: letter die gekleurd moet worden
#               2: bestand waarin gezocht moet worden
# Auteur:       Anton Thomas <anton.thomas@student.kdg.be>
# Datum:        20/05/2019
# Versie:       0.1

IFS=$'\n'
letter=$1
bestand=$2
rood="[0;31m"
reset="[0m"
ipregex="[[:alnum:]]*:([[:digit:]]{2,3})"
A=0
B=0
C=0

if [ $(id -u) != "0" ]; then
  echo "Dit script moet je als root uitvoeren"
  1>&2
  exit 1
fi

for lijn in `cat $bestand`; do
  if [[ $lijn =~ $ipregex ]]; then
      octet=${BASH_REMATCH[1]}
      if [[ $(($octet+1)) -gt 192 ]]; then
        let "C++"
      elif [[ $(($octet+1)) -gt 128 ]]; then
        let "B++"
      else
        let "A++"
      fi
  fi
done

if [[ $letter = "A" ]]; then
  echo -e "\e${rood}A:$A\n\e${reset}B:$B\nC:$C"
elif [[ $letter = "B" ]]; then
  echo -e "A:$A\n\e${rood}B:$B\n\e${reset}C:$C"
else
  echo -e "A:$A\nB:$B\n\e${rood}C:$C"
fi
