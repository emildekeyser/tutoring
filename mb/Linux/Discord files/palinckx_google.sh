#!/usr/bin/env bash

#author: Niels Palinckx

echo "Script van: Niels Palinckx"
OS=$2
input=$1
IFS=$'\n'

count=0


if [ "$EUID" -eq 0 ]
then echo "You are not allowed to run this script as root!"
  exit 1;
fi

if [[ $# -eq 0 ]]; then
  echo "geen parameters ingegeven..."; exit 1; #if no parameters given exit with code 1;
fi
if [[ $# -gt 2 ]]; then
  echo "maximaal twee parameters!"; exit 1;
fi

if [[ $# -eq 1 ]]; then
  OS=$1
  input="./imagelist.txt"

fi

if [[ ! -s $input ]]; then
  echo "het bestand dat je meegaf bestaat niet of is leeg!"; exit 1;
fi

regex="($OS)-.*v([[:digit:]]*).*"

for line in  `cat $input` ;
do
  if [[ $line =~ $regex ]]; then
    group=${BASH_REMATCH[1]%%-*}
    date=${BASH_REMATCH[2]}

    if [[ ${date#} -eq 0 ]]; then #als er geen date aan is gevonden in een bepaalde lijn, stop met exit code 1;
      echo  "${group^^} has not been found with any dates"; exit 1;
    fi
    echo  "Found ${group^^} with date $date"
    #per lijn dat matcht met regex count + 1
    let "count++"
  fi
done

echo "Number of lines found: $count"

unset IFS
